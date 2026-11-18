#!/usr/bin/env python3
"""The narrative ledger: the claims the discourse is making, measured.

Reads what the gatherers already write (dials/voices, dials/consensus, dials/events, data/gdelt), the latest scorer
run (dials/runs/<id>: readings, forecasts, cone) and the history layer's live query, and writes:

  narratives/ledger.json       every narrative with its holders per sweep (verbatim positions kept), bandwidth by
                               channel, each prediction's current reading, the evidence tally and the lifecycle label
  narratives/ledger.md         the same, readable
  narratives/bandwidth.csv     narrative x sweep: holders, opposed, mentions, arguments
  narratives/baseline.md       the bull, bear and pig cases assembled from the ledger, the measured dial points and
                               the system's own branch weights beside the holders
  narratives/bias_log.json/.md the catalogue of judgment in the model (event lines, likelihood-ratio tiers, state
                               thresholds, fork probabilities, hazard odds) beside the measured alternative where one exists

Nothing here carries a likelihood ratio and nothing here moves a branch weight: the ledger measures what is being
said, by whom, how loudly, and what the data say about it. Matching is deterministic (case-insensitive substring on
the words in narratives/map.json), so the counts are reproducible and the words that matched are recorded.

Run from the repository root: python3 -I narratives/tools/narratives.py [--run <RUN_ID>] [--check] [--unassigned]
"""
import csv, glob, json, math, os, re, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAR = os.path.join(ROOT, "narratives")
DIALS = os.path.join(ROOT, "dials")
MAP = os.path.join(NAR, "map.json")

# The layer's own three settings (listed in the bias log so they are not hidden judgment).
ENTRY_HOLDERS = 2     # distinct holders in the window for a narrative to enter the baseline
PIG_LOW = 0.34        # support share at or below which a held narrative is "crowded, unsupported"
PIG_HIGH = 0.66       # support share at or above which an unheld narrative is "unpriced, supported"

SIGN_OK = {"bull": {"bull"}, "bear": {"bear", "bear-bonds"}, "bear-bonds": {"bear-bonds", "bear"}, "neutral": {"bull", "bear", "bear-bonds", "neutral"},
           "contested": {"bull", "bear", "bear-bonds"}, "n/a": {"bull", "bear", "bear-bonds", "neutral", "n/a"}}
SIGN_AGAINST = {"bull": {"bear", "bear-bonds"}, "bear": {"bull"}, "bear-bonds": {"bull"}, "neutral": set(), "contested": set(), "n/a": set()}


def jload(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return default


# ---------------------------------------------------------------- the sweeps
def item_text(it):
    parts = [it.get("name") or "", it.get("title") or "", it.get("position") or "", it.get("sign_basis") or ""]
    for n in it.get("numbers") or []:
        if isinstance(n, dict):
            parts.append(n.get("claim") or "")
    return " ".join(p for p in parts if p).lower()


_KW = {}


def _found(k, text):
    """A keyword starts at a word boundary and may be the stem of a longer word ('refinanc' finds 'refinancing');
    'tail' does not find 'retail'. Keywords that begin with a non-word character ('$300', ' gw') are matched as given."""
    r = _KW.get(k)
    if r is None:
        kl = k.lower()
        r = _KW[k] = re.compile((r"\b" if re.match(r"\w", kl) else "") + re.escape(kl))
    return r.search(text) is not None


def match(nar, text):
    """The map's words found in the text: a match needs one strong word or two weak ones."""
    strong = [k for k in nar.get("keywords_strong", []) if _found(k, text)]
    weak = [k for k in nar.get("keywords_weak", []) if _found(k, text)]
    ok = bool(strong) or len(weak) >= 2
    return ok, strong, weak


def read_sweeps():
    out = []
    for fn in sorted(glob.glob(os.path.join(DIALS, "voices", "*.json"))):
        v = jload(fn, {})
        date = os.path.basename(fn).replace(".json", "")
        items = [it for it in v.get("items", []) if it.get("kind") in ("voice", "argument") and (it.get("position") or it.get("name"))]
        out.append({"date": date, "file": os.path.relpath(fn, ROOT), "items": items, "status": v.get("status"), "n_items": len(items)})
    return out


def holders_per_sweep(nar, sweeps):
    rows = []
    for sw in sweeps:
        holders, opposed, mentions, arguments, quotes, numbers = {}, {}, 0, 0, [], []
        for it in sw["items"]:
            text = item_text(it)
            ok, strong, weak = match(nar, text)
            if not ok:
                continue
            mentions += 1
            sign = (it.get("sign") or "n/a")
            key = it.get("key") or it.get("name") or "?"
            who = it.get("name") or key
            if it.get("kind") == "argument":
                arguments += 1
                key = "arg:" + (it.get("name") or "")[:40]
                who = "arg: " + (it.get("name") or "")[:72]
            if sign in SIGN_OK.get(nar["sign"], set()) and sign not in ("n/a", "neutral"):
                holders[key] = {"name": who, "sign": sign, "as_of": it.get("as_of"), "kind": it.get("kind"), "lane": it.get("lane"), "matched": strong[:3] + weak[:3]}
                for x in it.get("numbers") or []:
                    if isinstance(x, dict) and x.get("claim"):
                        numbers.append({"name": who, "as_of": it.get("as_of"), "claim": x["claim"][:240], "checkable_against": (x.get("checkable_against") or "")[:160]})
            elif sign in SIGN_AGAINST.get(nar["sign"], set()) and strong:
                opposed[key] = {"name": who, "sign": sign, "as_of": it.get("as_of"), "kind": it.get("kind"), "matched": strong[:3]}
            if len(quotes) < 6 and it.get("position"):
                quotes.append({"name": who, "as_of": it.get("as_of"), "sign": sign, "url": it.get("url"), "matched": strong[:3] + weak[:3],
                               "position": (it.get("position") or "")[:420]})
        rows.append({"sweep": sw["date"], "n_items": sw["n_items"], "holders": sorted(holders.values(), key=lambda h: h["name"]), "n_holders": len(holders),
                     "holder_share": round(len(holders) / sw["n_items"], 3) if sw["n_items"] else None,
                     "opposed": sorted(opposed.values(), key=lambda h: h["name"]), "n_opposed": len(opposed),
                     "mentions": mentions, "arguments": arguments, "quotes": quotes, "numbers": numbers})
    return rows


# ---------------------------------------------------------------- the other channels
def gdelt_summary(series):
    p = os.path.join(ROOT, "data", "gdelt", f"{series}_timelinevol.json")
    g = jload(p)
    if not g:
        return None
    tl = g.get("timeline", [])
    data = next((t.get("data", []) for t in tl if "Volume" in (t.get("series") or "")), tl[0].get("data", []) if tl else [])
    vals = [(d["date"][:8], float(d["value"])) for d in data if d.get("value") is not None]
    vals = [(d, v) for d, v in vals if v > 0][-90:]  # gap and zero days excluded, as the run does
    if len(vals) < 10:
        return None
    xs = [v for _, v in vals]
    d7 = sum(xs[-7:]) / len(xs[-7:]); ma = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - ma) ** 2 for x in xs) / max(1, len(xs) - 1)) or 1e-9
    return {"series": series, "query": g.get("query_details", {}).get("title"), "last_date": vals[-1][0], "d7": round(d7, 4), "ma90": round(ma, 4),
            "z": round((d7 - ma) / sd, 2), "n_days": len(vals)}


def consensus_summary():
    fns = sorted(glob.glob(os.path.join(DIALS, "consensus", "*.json")))
    if not fns:
        return None
    c = jload(fns[-1], {})
    items = [i for i in c.get("items", []) if i.get("kind") == "consensus" and i.get("ratings")]
    tot = {"strong_buy": 0, "buy": 0, "hold": 0, "sell": 0, "strong_sell": 0}
    ups = []
    for i in items:
        for k in tot:
            tot[k] += int(i["ratings"].get(k) or 0)
        if i.get("price") and i.get("pt_median"):
            ups.append(i["pt_median"] / i["price"] - 1)
    n = sum(tot.values()) or 1
    ups.sort()
    return {"as_of": os.path.basename(fns[-1]).replace(".json", ""), "tickers": len(items), "ratings": n,
            "buy_share": round((tot["strong_buy"] + tot["buy"]) / n, 3), "hold_or_sell_share": round((tot["hold"] + tot["sell"] + tot["strong_sell"]) / n, 3),
            "pt_upside_median": round(ups[len(ups) // 2], 3) if ups else None}


def event_hits(dial_map):
    """Event-sweep hits mapped to narratives by their candidate dial (the words before the first space or parenthesis)."""
    out = {}
    for fn in sorted(glob.glob(os.path.join(DIALS, "events", "*.json"))):
        e = jload(fn, {})
        for it in e.get("items", []):
            cd = (it.get("candidate_dial") or "").strip()
            code = re.split(r"[\s(]", cd)[0] if cd else ""
            for nid in dial_map.get(code, []) + dial_map.get(cd, []):
                out.setdefault(nid, []).append({"as_of": it.get("as_of"), "dial": cd[:60], "late": it.get("late"),
                                                "text": (it.get("name") or it.get("headline") or "")[:220], "file": os.path.relpath(fn, ROOT)})
    for nid in out:
        out[nid] = sorted({(h["as_of"], h["text"]): h for h in out[nid]}.values(), key=lambda h: h["as_of"] or "")[-8:]
    return out


# ---------------------------------------------------------------- the latest run and the history layer
def latest_run(kind="dials", run_id=None):
    runs = sorted(d for d in glob.glob(os.path.join(DIALS, "runs", "*")) if os.path.isdir(d) and os.path.basename(d).endswith("-" + kind))
    if run_id:
        runs = [d for d in runs if os.path.basename(d) == run_id] or runs
    if not runs:
        return None
    d = runs[-1]
    return {"id": os.path.basename(d), "readings": jload(os.path.join(d, "readings.json"), {}), "forecasts": jload(os.path.join(d, "forecasts.json"), {}),
            "cone": jload(os.path.join(d, "cone.json"), {}), "dir": os.path.relpath(d, ROOT)}


def all_forks():
    """Every fork ever registered or resolved across the run folders: id -> latest state."""
    reg, res = {}, {}
    for fn in sorted(glob.glob(os.path.join(DIALS, "runs", "*", "forecasts.json"))):
        f = jload(fn, {})
        for r in f.get("registered", []):
            if r.get("id"):
                reg[r["id"]] = {**r, "_run": os.path.basename(os.path.dirname(fn))}
        for r in f.get("resolved", []):
            if r.get("id"):
                res[r["id"]] = {**r, "_run": os.path.basename(os.path.dirname(fn))}
    led = jload(os.path.join(DIALS, "state", "ledger.json"), {})
    for r in led.get("forecasts", []) if isinstance(led, dict) else []:
        if r.get("id") and r.get("outcome") is not None and r["id"] not in res:
            res[r["id"]] = r
    return reg, res


def calibration():
    """The orchestrator's own record: resolved forks bucketed by the probability it registered, from dials/state/ledger.json."""
    led = jload(os.path.join(DIALS, "state", "ledger.json"), {})
    buckets = {"<0.2": [0, 0], "0.2-0.4": [0, 0], "0.4-0.6": [0, 0], "0.6-0.8": [0, 0], ">=0.8": [0, 0]}
    n = 0; brier = 0.0
    for r in led.get("forecasts", []) if isinstance(led, dict) else []:
        res = r.get("resolution") or {}
        if res.get("outcome") is None:
            continue
        p = float(res.get("p") or r.get("p") or 0)
        k = "<0.2" if p < 0.2 else "0.2-0.4" if p < 0.4 else "0.4-0.6" if p < 0.6 else "0.6-0.8" if p < 0.8 else ">=0.8"
        buckets[k][0] += 1; buckets[k][1] += int(res["outcome"]); n += 1; brier += float(res.get("brier") or (p - int(res["outcome"])) ** 2)
    sb = jload(os.path.join(DIALS, "state", "scoreboard.json"), {})
    return {"n_resolved": n, "brier_mean": round(brier / n, 3) if n else None, "scoreboard": (sb.get("all") or {}).get("dials"),
            "buckets": {k: {"n": v[0], "fired": v[1], "rate": round(v[1] / v[0], 2) if v[0] else None} for k, v in buckets.items()}}


def bucket_of(p, cal):
    if p is None:
        return None
    k = "<0.2" if p < 0.2 else "0.2-0.4" if p < 0.4 else "0.4-0.6" if p < 0.6 else "0.6-0.8" if p < 0.8 else ">=0.8"
    b = cal["buckets"].get(k, {})
    return f"the orchestrator's record in the {k} bucket: {b.get('fired')} of {b.get('n')} resolved forks fired" + (f" ({b.get('rate')})" if b.get("rate") is not None else "") if b.get("n") else f"no resolved fork yet in the {k} bucket"


def cond_true(cond, fd):
    """'zone in stress,acute' / 'level >= 100' / 'level <= -5' against a fields_detail entry."""
    if not fd:
        return None
    m = re.match(r"zone in ([\w,]+)", cond)
    if m:
        return (fd.get("zone") or "") in m.group(1).split(",")
    m = re.match(r"level\s*(>=|<=|>|<)\s*(-?[\d.]+)", cond)
    if m and fd.get("level") is not None:
        lv, op, x = float(fd["level"]), m.group(1), float(m.group(2))
        return {">=": lv >= x, "<=": lv <= x, ">": lv > x, "<": lv < x}[op]
    return None


FIELD_ALIASES = {"SPX": "SP500", "ICSA_4wk": "ICSA", "WTI": "WTI_spot", "TP": "TP", "Brent": "Brent_dated"}


def field_reading(run, ref):
    """A field from the run's fields_detail (by name or alias), or an equity lens 'E6_1m' from its lenses block."""
    rd = (run or {}).get("readings", {})
    fd = rd.get("fields_detail", {})
    if ref in fd:
        return fd[ref]
    if FIELD_ALIASES.get(ref) in fd:
        return fd[FIELD_ALIASES[ref]]
    m = re.match(r"^(E\d+)_(1m|3m)$", ref)
    if m:
        lens = rd.get("lenses", {}).get(m.group(1))
        if lens and lens.get(m.group(2)) is not None:
            return {"level": lens[m.group(2)], "zone": None, "date": rd.get("run_at", "")[:10], "note": (rd.get("lenses", {}).get("notes", {}).get(m.group(1)) or "")[:160],
                    "d1m": None, "d3m": lens.get("3m"), "pct_window": None, "pct_1y": None}
    return None


def history_summary():
    q = jload(os.path.join(ROOT, "history", "analogs", "us_2026ytd.json"), {})
    rates = {}
    p = os.path.join(ROOT, "history", "climatology", "event_rates_by_era.csv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            rates[(r["era"], r["regime"], r["target"])] = (int(r["n"]), float(r["rate"]))
    return q, rates


def read_prediction(pr, run, reg, res, hist, rates):
    out = dict(pr)
    k = pr["kind"]
    if k in ("fork", "fork_nonfire"):
        r = res.get(pr["ref"]); g = reg.get(pr["ref"])
        if r is not None:
            fired = int(r.get("outcome") or 0) == 1
            out["status"] = "resolved"; out["fired"] = fired; out["p_registered"] = r.get("p", g.get("p") if g else None)
            out["evidence"] = r.get("evidence", "")[:200]; out["resolved_in"] = r.get("_run")
            out["supports"] = (fired if k == "fork" else not fired)
        elif g is not None:
            out["status"] = "open"; out["p_registered"] = g.get("p"); out["resolves"] = g.get("resolves"); out["criterion"] = (g.get("criterion") or "")[:160]
            out["supports"] = None
        else:
            out["status"] = "unregistered"; out["supports"] = None
    elif k == "history":
        s = (hist.get("summary") or {}).get(pr["ref"])
        if s:
            out["analogs"] = s.get("analogs"); out["climatology"] = s.get("climatology"); out["description"] = s.get("description")
        out["supports"] = None
    elif k == "history_rate":
        eras = sorted({e for (e, rg, t) in rates if t == pr["ref"] and rg == "all"})
        if eras:
            e = eras[-1]; n, rate = rates[(e, "all", pr["ref"])]
            out["era"] = e; out["n"] = n; out["rate"] = rate
        out["supports"] = None
    elif k == "field":
        fd = field_reading(run, pr["ref"])
        if fd:
            out["reading"] = {kk: fd.get(kk) for kk in ("level", "zone", "pct_1y", "pct_window", "d1m", "d3m", "date", "transition", "note")}
            out["supports"] = cond_true(pr["condition"], fd)
        else:
            out["supports"] = None
    elif k == "stage":
        out["reading"] = (run or {}).get("readings", {}).get("stage", {}).get(pr["ref"]); out["supports"] = None
    elif k == "hazard":
        hz = {}
        for kk, v in ((run or {}).get("forecasts") or {}).items():
            if kk.startswith("hazards") and isinstance(v, dict):
                hz = v
        out["monthly_odds"] = hz.get(pr["ref"]); out["supports"] = None
    return out


# ---------------------------------------------------------------- the bias log
def bias_log(run, reg, cal=None):
    """Where judgment enters the model, beside the measured alternative where one exists."""
    cal = cal or calibration()
    items = []
    fd = (run or {}).get("readings", {}).get("fields_detail", {})
    def band(ref):
        f = fd.get(ref)
        return f"{ref} {f.get('level')} on {f.get('date')}: {f.get('zone')} ({f.get('pct_window')}th pct of window, {f.get('pct_1y')}th of 1y)" if f else "field not in the run"
    for ref, line, tier, note in (("IG", "100 bp", "x2 B", "event line"), ("IG", "115 bp", "B element", "event line"), ("DFII10", "3.0", "x4 B and C", "event line"),
                                  ("DFII10", "2.5", "x2 A", "event line"), ("ICSA_4wk", "+20% from the low", "x4 B", "event line"), ("TP", "1.0", "C element", "event line")):
        items.append({"kind": "event line", "what": f"{ref} at {line} carries {tier}", "value": line, "source": "dials/rulings.md ruling l; macro-dials SKILL.md",
                      "measured_alternative": "the percentile-band zone of the same field (ruling l): " + band(ref), "why_judgment": "anchored on precedents a six-year window does not contain"})
    for tier, lr, sigma, examples in (("strong", 4.0, 0.50, "capex cut by a principal; pulled hyperscaler deal; 30y tail >= 3 bp with dealers > 15%; claims +20%; neocloud default; GPU rental -20%; real 10y through 3.0"),
                                      ("moderate", 2.0, 0.35, "IG through 100; coupon increase; Nvidia AR > revenue a third quarter; lab round downsized; core CPI >= 0.4 twice; broad convergence"),
                                      ("default", 1.5, 0.25, "any other scored event; a zone transition; convergence"), ("weak", 1.2, 0.15, "an index at a new high; a single week's flow print")):
        items.append({"kind": "likelihood-ratio tier", "what": f"{tier} tier x{lr} (log-normal sigma {sigma})", "value": lr, "source": "macro-dials SKILL.md, Likelihood-ratio tiers",
                      "measured_alternative": "none yet: the skill's own queued item (tier calibration on the periphery-first episode table, Beta-binomial posterior per tier); the history layer's ladder rungs are the nearest measured conditional rates",
                      "why_judgment": examples})
    items.append({"kind": "calibration record", "what": f"{cal['n_resolved']} resolved forks; mean Brier {cal['brier_mean']}", "value": cal["brier_mean"], "source": "dials/state/ledger.json, dials/state/scoreboard.json",
                  "measured_alternative": "; ".join(f"{k}: {v['fired']}/{v['n']}" + (f" ({v['rate']})" if v['rate'] is not None else "") for k, v in cal["buckets"].items() if v["n"]),
                  "why_judgment": "not a judgment: the measured record every fork probability above is read against"})
    items.append({"kind": "narrative-layer setting", "what": f"entry rule {ENTRY_HOLDERS} distinct holders; pig cut-offs at support share <= {PIG_LOW} (crowded, unsupported) and >= {PIG_HIGH} (unpriced, supported)", "value": f"{ENTRY_HOLDERS}; {PIG_LOW}/{PIG_HIGH}",
                  "source": "narratives/tools/narratives.py", "measured_alternative": "none: round-number cut-offs chosen at the layer's first build so that the asymmetry table is a counted rule rather than a reading", "why_judgment": "the layer's own three settings; changed prospectively only"})
    items.append({"kind": "state thresholds", "what": "numeric state label: B >= 20 at H2 / >= 30 at H3; A below 0.25 on both shares, B-LEANING at s2 >= 0.75", "value": "20/30; 0.25/0.75",
                  "source": "dials/rulings.md ruling j", "measured_alternative": "none: a two-point calibration to the Oct 30 and Nov 2, 2026 hand reads; to be revisited after resolved weeks", "why_judgment": "set so the first two reads came out where they had been called by hand"})
    items.append({"kind": "branch set", "what": "three branches (A grow out of it, B capex bust, C debt crunch) with hand-written confirmation criteria", "value": "A/B/C",
                  "source": "macro-dials SKILL.md, Branches and their signatures", "measured_alternative": "the narrative ledger: the branches as narratives beside the discourse's own, with the same evidence tally (narratives/ledger.md)",
                  "why_judgment": "the hypothesis set is the author's; rulings 'principle' (2026-11-03) already says never to assume only the named branches exist"})
    for fid, g in sorted(reg.items()):
        if not g.get("resolves"):
            continue
        items.append({"kind": "fork probability", "what": f"{fid}: {(g.get('criterion') or '')[:120]}", "value": g.get("p"), "source": g.get("_run"),
                      "measured_alternative": bucket_of(g.get("p"), cal), "why_judgment": "the orchestrator's p, adjustable +/-10 on discourse", "note": (g.get("note") or "")[:200],
                      "resolves": g.get("resolves"), "cluster": g.get("cluster")})
    hz = {}
    for kk, v in ((run or {}).get("forecasts") or {}).items():
        if kk.startswith("hazards") and isinstance(v, dict):
            hz = v
    for name, p in sorted(hz.items()):
        items.append({"kind": "hazard odds", "what": name, "value": p, "source": (run or {}).get("id"), "measured_alternative": "none yet (per-month odds revisited each run)", "why_judgment": "rough per-month odds"})
    return items


# ---------------------------------------------------------------- the assembly
def lifecycle(rows):
    hs = [r["n_holders"] for r in rows]
    if not hs or max(hs) == 0:
        return "unheld (mentions only)" if any(r["mentions"] for r in rows) else "silent"
    if len(hs) >= 2 and hs[-1] == 0 and max(hs[:-1]) > 0:
        return "fading"
    if len(hs) >= 2 and hs[-1] > hs[0] and hs[-1] >= max(hs[:-1]):
        return "growing"
    if hs[-1] > 0 and (len(hs) == 1 or all(h == 0 for h in hs[:-1])):
        return "emerging"
    return "held"


def evidence_tally(preds):
    f_true = sum(1 for p in preds if p["kind"] == "field" and p.get("supports") is True)
    f_n = sum(1 for p in preds if p["kind"] == "field" and p.get("supports") is not None)
    fk_sup = sum(1 for p in preds if p["kind"] in ("fork", "fork_nonfire") and p.get("status") == "resolved" and p.get("supports"))
    fk_res = sum(1 for p in preds if p["kind"] in ("fork", "fork_nonfire") and p.get("status") == "resolved")
    fk_open = [(p["ref"], p.get("p_registered")) for p in preds if p["kind"] in ("fork", "fork_nonfire") and p.get("status") == "open"]
    return {"fields_true": f_true, "fields_evaluable": f_n, "forks_supporting": fk_sup, "forks_resolved": fk_res, "forks_open": fk_open,
            "support_share": round((f_true + fk_sup) / (f_n + fk_res), 2) if (f_n + fk_res) else None}


def build(run_id=None):
    m = jload(MAP)
    sweeps = read_sweeps()
    run = latest_run("dials", run_id)
    reg, res = all_forks()
    hist, rates = history_summary()
    cons = consensus_summary()
    hits = event_hits(m.get("dial_map", {}))
    cone = (run or {}).get("cone", {})
    weights = {"H2": dict(zip("ABC", cone.get("H2", []))), "H3": dict(zip("ABC", cone.get("H3", []))), "run": (run or {}).get("id")} if cone else {}
    standoff = (run or {}).get("readings", {}).get("standoff_export", {})
    ledger = []
    for nar in m["narratives"]:
        rows = holders_per_sweep(nar, sweeps)
        preds = [read_prediction(p, run, reg, res, hist, rates) for p in nar.get("predictions", [])]
        g = gdelt_summary(nar["gdelt"]) if nar.get("gdelt") else None
        distinct = {}
        for r in rows:
            for h in r["holders"]:
                distinct[h["name"]] = h
        entry = {"id": nar["id"], "title": nar["title"], "sign": nar["sign"], "lane": nar["lane"], "branch": nar.get("branch"), "statement": nar["statement"],
                 "falsifier": nar.get("falsifier"), "incentive_tags": nar.get("incentive_tags", []), "note": nar.get("note"),
                 "sweeps": rows, "lifecycle": lifecycle(rows),
                 "bandwidth": {"holders_latest": rows[-1]["n_holders"] if rows else 0, "holders_distinct": len(distinct), "holders_distinct_names": sorted(distinct),
                               "holders_by_sweep": [r["n_holders"] for r in rows],
                               "opposed_by_sweep": [r["n_opposed"] for r in rows], "mentions_by_sweep": [r["mentions"] for r in rows],
                               "arguments_by_sweep": [r["arguments"] for r in rows], "gdelt": g,
                               "sell_side": cons if nar["sign"] == "bull" and nar["lane"] in ("strategist", "capital") else None},
                 "event_hits": hits.get(nar["id"], []), "predictions": preds, "evidence": evidence_tally(preds),
                 "system_weight": ({"branch": nar["branch"], "H2": weights["H2"].get(nar["branch"]), "H3": weights["H3"].get(nar["branch"]), "run": weights.get("run")}
                                   if weights and nar.get("branch") in ("A", "B", "C") else
                                   ({"branch": "standoff", "H2": standoff.get("H2"), "H3": standoff.get("H3")} if nar.get("branch") == "standoff" and standoff else None))}
        ledger.append(entry)
    cal = calibration()
    bias = bias_log(run, reg, cal)
    out = {"built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "map_version": m.get("version"), "sweeps": [{"date": s["date"], "file": s["file"], "items": s["n_items"], "status": s["status"]} for s in sweeps],
           "run": (run or {}).get("id"), "branch_weights": weights, "consensus": cons, "calibration": cal, "narratives": ledger, "bias_log_n": len(bias),
           "lenses": (run or {}).get("readings", {}).get("lenses", {}), "discourse": (run or {}).get("readings", {}).get("discourse", {}), "games": (run or {}).get("readings", {}).get("games", {})}
    return out, bias, m


def _weight_cell(sw):
    h2 = sw.get("H2")
    if h2 is None:
        return ""
    if isinstance(h2, dict):
        return "standoff " + " / ".join(f"{k} {v}" for k, v in h2.items())
    return f"{h2} ({sw.get('branch')})"


def pct(x, d=0):
    return "" if x is None else f"{100 * x:.{d}f}%"


def write_md(out, m):
    L = ["# The narrative ledger", "",
         f"Built {out['built']} from {len(out['sweeps'])} voices sweeps ({', '.join(s['date'] for s in out['sweeps'])}), the event sweeps, the consensus pages, the GDELT "
         f"timelines, the scorer run `{out['run']}` and the history layer's live query. Matching is deterministic on the words in `map.json`; the words that "
         "matched are printed with each quote. A *holder* is a tracked voice or argument whose sign agrees with the narrative's and whose item matched its words; "
         "*opposed* counts items of the opposite sign that matched one of its strong words (a proxy for opposition, not a reading of the argument); *mentions* count every matched item. Nothing here moves a branch weight: the system's own weight is printed beside the holders as one "
         "more voice.", ""]
    L += ["## At a glance", "", "| narrative | sign | lifecycle | holders by sweep | opposed | GDELT z (series) | evidence: fields true / evaluable | forks supporting / resolved | open forks (p) | system weight H2 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for n in out["narratives"]:
        b = n["bandwidth"]; e = n["evidence"]; sw = n.get("system_weight") or {}
        gz = f"{b['gdelt']['z']} ({b['gdelt']['series']})" if b.get("gdelt") else ""
        L.append(f"| {n['title'][:70]} (`{n['id']}`) | {n['sign']} | {n['lifecycle']} | {' → '.join(str(x) for x in b['holders_by_sweep'])} | {' → '.join(str(x) for x in b['opposed_by_sweep'])} | {gz} | "
                 f"{e['fields_true']} / {e['fields_evaluable']} | {e['forks_supporting']} / {e['forks_resolved']} | {', '.join(f'{r} ({p})' for r, p in e['forks_open'])} | "
                 f"{_weight_cell(sw)} |")
    L.append("")
    if out.get("consensus"):
        c = out["consensus"]
        L += [f"Sell-side alignment (N4, {c['as_of']}): {pct(c['buy_share'], 1)} of {c['ratings']} ratings across {c['tickers']} registered tickers are buy or strong buy; median price-target upside {pct(c['pt_upside_median'], 0)}. "
              "This is the sell side's bandwidth on the bull narratives, printed beside them and never added to the holder counts.", ""]
    for n in out["narratives"]:
        L += [f"## {n['title']}", "", f"`{n['id']}` · sign **{n['sign']}** · lane {n['lane']} · branch {n.get('branch')} · lifecycle **{n['lifecycle']}**", "", n["statement"], ""]
        if n.get("note"):
            L += [f"*{n['note']}*", ""]
        L += ["**Holders by sweep.**", "", "| sweep (items) | holders | opposed | mentions | arguments |", "|---|---|---|---|---|"]
        for r in n["sweeps"]:
            L.append(f"| {r['sweep']} ({r['n_items']}) | {', '.join(h['name'] for h in r['holders']) or '—'} ({r['n_holders']}) | {', '.join(h['name'] for h in r['opposed']) or '—'} ({r['n_opposed']}) | {r['mentions']} | {r['arguments']} |")
        L.append("")
        allq = [q for r in n["sweeps"] for q in r["quotes"]]
        hq = [q for q in allq if q["sign"] in SIGN_OK.get(n["sign"], set()) and q["sign"] not in ("n/a", "neutral")]
        quotes = (hq[-4:] if len(hq) >= 2 else (hq + [q for q in allq if q not in hq])[-4:])
        if quotes:
            L += ["**In their words** (the latest matched positions; words that matched in brackets).", ""]
            for q in quotes:
                L.append(f"- {q['name']} ({q['as_of']}, {q['sign']}) [{', '.join(q['matched'][:4])}]: {q['position'][:300]}{'…' if len(q['position']) > 300 else ''}")
            L.append("")
        nums = [x for r in n["sweeps"] for x in r["numbers"]]
        if nums:
            checkable = [x for x in nums if re.search(r"repo|fred|treasurydirect|bls|bea|nipa|z\.1|h\.8|fiscaldata|sec |8-k|10-q|10-k|s-1|gdelt", x["checkable_against"].lower())
                         and not re.search(r"no repo|not checkable|not a macro series", x["checkable_against"].lower())]
            shown = (checkable[-6:] if len(checkable) >= 3 else (checkable + [x for x in nums if x not in checkable])[-6:])
            L += [f"**Numbers the holders put on it** ({len(nums)} in the window, {len(checkable)} naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).", ""]
            for x in shown:
                L.append(f"- {x['name'][:40]} ({x['as_of']}): {x['claim'][:200]} — *check against: {x['checkable_against'][:100] or 'not stated'}*")
            L.append("")
        b = n["bandwidth"]
        chan = []
        if b.get("gdelt"):
            g = b["gdelt"]; chan.append(f"GDELT {g['query']}: 7-day volume {g['d7']} against a 90-day mean of {g['ma90']}, z {g['z']} (to {g['last_date']})")
        if b.get("sell_side"):
            chan.append(f"sell side: {pct(b['sell_side']['buy_share'], 1)} buy ratings, median target upside {pct(b['sell_side']['pt_upside_median'])}")
        if chan:
            L += ["**Other channels.** " + "; ".join(chan) + ".", ""]
        if n["event_hits"]:
            L += ["**Event-sweep hits mapped to this narrative** (dated evidence, not holders).", ""]
            for h in n["event_hits"][-5:]:
                L.append(f"- {h['as_of']} [{h['dial']}]{' late' if h.get('late') else ''}: {h['text'][:200]}")
            L.append("")
        L += ["**Predictions and what the data say now.**", "", "| kind | prediction | reading | supports? |", "|---|---|---|---|"]
        for p in n["predictions"]:
            k = p["kind"]
            if k in ("fork", "fork_nonfire"):
                if p.get("status") == "resolved":
                    rd = f"resolved in {p.get('resolved_in')}: {'fired' if p.get('fired') else 'did not fire'} (registered p {p.get('p_registered')}); {p.get('evidence', '')[:120]}"
                elif p.get("status") == "open":
                    rd = f"open, p {p.get('p_registered')}, resolves {p.get('resolves')}"
                else:
                    rd = "not registered"
            elif k == "history":
                a = p.get("analogs") or {}; c = p.get("climatology") or {}
                rd = f"analogs (n {a.get('n')}): p25 {a.get('p25', 0):.1f} / median {a.get('p50', 0):.1f} / p75 {a.get('p75', 0):.1f}; climatology median {c.get('p50', 0):.1f} (p25 {c.get('p25', 0):.1f}, p75 {c.get('p75', 0):.1f})" if a else "no analog summary"
            elif k == "history_rate":
                rd = f"{p.get('era')}: {pct(p.get('rate'), 1)} of {p.get('n')} country-years" if p.get("rate") is not None else "no rate"
            elif k == "field":
                r = p.get("reading") or {}
                if r and r.get("zone") is None:
                    rd = f"{p['ref']} {r.get('level')} (3m {r.get('d3m')}; {r.get('date')}){': ' + r['note'] if r.get('note') else ''}"
                elif r:
                    rd = f"{p['ref']} {r.get('level')} ({r.get('zone')}, {r.get('pct_window')}th pct; Δ1m {r.get('d1m')}, Δ3m {r.get('d3m')}; {r.get('date')})"
                else:
                    rd = "field not in the run"
            elif k == "stage":
                rd = str(p.get("reading") or "")[:160]
            elif k == "hazard":
                rd = f"monthly odds {p.get('monthly_odds')}"
            else:
                rd = ""
            sup = {True: "yes", False: "no", None: "—"}[p.get("supports")]
            L.append(f"| {k} | {p['text']} | {rd} | {sup} |")
        e = n["evidence"]
        L += ["", f"Evidence tally: {e['fields_true']} of {e['fields_evaluable']} field conditions in the predicted direction; {e['forks_supporting']} of {e['forks_resolved']} resolved forks supporting; "
              f"{len(e['forks_open'])} open. Support share {e['support_share'] if e['support_share'] is not None else '—'} (counted, not weighted).", ""]
        if n.get("system_weight"):
            sw = n["system_weight"]
            if isinstance(sw.get("H2"), dict):
                L += [f"The system's own position (the standoff watch's export): H2 " + ", ".join(f"{k} {v}" for k, v in sw["H2"].items()) + "; H3 " + ", ".join(f"{k} {v}" for k, v in (sw.get("H3") or {}).items()) + " — printed here as one more holder.", ""]
            else:
                L += [f"The system's own position: branch {sw['branch']} at {sw.get('H2')} (H2) / {sw.get('H3')} (H3) in run `{sw.get('run', out['run'])}` — printed here as one more holder, scored like the rest.", ""]
        L += [f"**Falsifier.** {n['falsifier']}", "", "**Incentive tags** (a reader's discount, never the system's): " + "; ".join(n["incentive_tags"]) + ".", ""]
    L += ["## Reading rules", "",
          "- Holders are counted, never weighted: a narrative held by five newsletter writers and one by two asset managers print as 5 and 2.",
          "- Mentions include opposed and neutral items; the holder count is the narrative's bandwidth among the roster, the opposed count a proxy for its opposition (opposite sign, strong word).",
          "- The sweeps differ in size (the item count is printed beside each date), so a fall in holders can be a smaller sweep; `bandwidth.csv` carries holders as a share of the sweep's items as well. The lifecycle label is computed on raw counts and is a description, not a forecast.",
          "- GDELT z is the 7-day volume against the trailing 90 days of non-zero days; the orchestrator's N1 uses the same files (its MA4 and z3m differ in window).",
          "- A prediction's 'supports' is a counted condition (a field zone, a resolved fork), not an inference; open forks print their registered probability, which is the orchestrator's judgment (see the bias log).",
          "- The history legs are what followed states like the present one in the 18-country record; they are base rates, not forecasts.",
          "- Nothing here changes a branch weight. The ledger is the stated side of G3 made explicit and scorable.", ""]
    return "\n".join(L)


def write_baseline(out):
    nars = out["narratives"]
    def rank(ns):
        return sorted(ns, key=lambda n: (-n["bandwidth"]["holders_distinct"], -n["bandwidth"]["holders_latest"]))
    bulls = rank([n for n in nars if n["sign"] == "bull"])
    bears = rank([n for n in nars if n["sign"] in ("bear", "bear-bonds")])
    w = out.get("branch_weights", {})
    L = ["# The baseline cases", "",
         f"Assembled {out['built']} from the narrative ledger: the bull and bear cases are the narratives of each sign ranked by how many tracked voices hold them in the latest sweep, "
         "each with its evidence tally; the pig case is the asymmetry between how loudly a narrative is held and how much the data support it. No probability is assigned "
         "here. The system's branch weights from the latest run are printed as one more holder's position. Any later adjustment is a user's bias and goes in the bias log.", ""]
    if w:
        L += [f"**The system's position** (run `{w.get('run')}`): H2 A {w['H2'].get('A')} / B {w['H2'].get('B')} / C {w['H2'].get('C')}; H3 A {w['H3'].get('A')} / B {w['H3'].get('B')} / C {w['H3'].get('C')}.", ""]
    def case(title, ns):
        L.append(f"## {title}"); L.append("")
        if not ns:
            L.append("No narrative of this sign is held in the latest sweep."); L.append(""); return
        L.append("| rank | narrative | distinct holders in the window | latest sweep | sweeps held | opposed (latest) | evidence support | open forks | the one check that would settle it |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        for i, n in enumerate(ns, 1):
            b = n["bandwidth"]; e = n["evidence"]
            names = ", ".join(x[:28] for x in b["holders_distinct_names"])
            entry = "" if b["holders_distinct"] >= ENTRY_HOLDERS else f" *(below the {ENTRY_HOLDERS}-holder entry rule: emerging)*"
            L.append(f"| {i} | {n['title'][:80]}{entry} | {b['holders_distinct']} ({names[:120]}) | {b['holders_latest']} | {sum(1 for x in b['holders_by_sweep'] if x)} of {len(b['holders_by_sweep'])} | {b['opposed_by_sweep'][-1] if b['opposed_by_sweep'] else 0} | "
                     f"{e['fields_true']}/{e['fields_evaluable']} fields, {e['forks_supporting']}/{e['forks_resolved']} forks | {len(e['forks_open'])} | {n['falsifier'][:110]} |")
        L.append("")
    case("The bull case (as the discourse holds it)", bulls)
    case("The bear case (as the discourse holds it)", bears)
    # pigs: asymmetry between bandwidth and evidence
    L += ["## The pig case (asymmetries)", "",
          "Where the crowd and the data disagree. *Crowded and unsupported*: held by many, with most of its checks against it. *Unpriced and supported*: held by few, with most of its checks for it. "
          f"Both are listed with their counts; a narrative needs at least two evaluable checks to appear, *held* means {ENTRY_HOLDERS} or more distinct holders in the window, and the cut-offs are support shares of {PIG_LOW} and {PIG_HIGH} (the layer's own settings, listed in the bias log). Which way to lean is the reader's call.", "", "| asymmetry | narrative | distinct holders | evidence support | reading |", "|---|---|---|---|---|"]
    scored = [n for n in nars if n["evidence"]["support_share"] is not None and n["sign"] in ("bull", "bear", "bear-bonds")
              and (n["evidence"]["fields_evaluable"] + n["evidence"]["forks_resolved"]) >= 2]
    for n in scored:
        h = n["bandwidth"]["holders_distinct"]; s = n["evidence"]["support_share"]
        if h >= ENTRY_HOLDERS and s <= PIG_LOW:
            L.append(f"| crowded, unsupported | {n['title'][:80]} | {h} | {s} | held by {h} distinct voices in the window while {n['evidence']['fields_true']} of {n['evidence']['fields_evaluable']} field checks and {n['evidence']['forks_supporting']} of {n['evidence']['forks_resolved']} resolved forks point its way |")
        elif h < ENTRY_HOLDERS and s >= PIG_HIGH:
            L.append(f"| unpriced, supported | {n['title'][:80]} | {h} | {s} | held by {h} voice{'s' if h != 1 else ''} in the window while {n['evidence']['fields_true']} of {n['evidence']['fields_evaluable']} field checks point its way |")
    if L[-1].startswith("|---"):
        L.append("| — | no asymmetry by the counted rule this round | | | |")
    L.append("")
    # measured dial points
    run = out.get("run")
    L += ["## The measured dial points", "", f"The fields as the run `{run}` read them — level, zone by the percentile-band rule, and the change — the baseline every narrative above is checked against. "
          "A hand line that differs from the band is a bias and is listed in the bias log.", ""]
    L += ["| field | level | zone | window pct | 1y pct | Δ1m | Δ3m | date |", "|---|---|---|---|---|---|---|---|"]
    fd = {}
    try:
        fd = jload(os.path.join(DIALS, "runs", run, "readings.json"), {}).get("fields_detail", {})
    except Exception:
        pass
    for k in sorted(fd):
        f = fd[k]
        L.append(f"| {k} | {f.get('level')} | {f.get('zone')} | {f.get('pct_window')} | {f.get('pct_1y')} | {f.get('d1m')} | {f.get('d3m')} | {f.get('date')} |")
    L.append("")
    lenses = out.get("lenses") or {}
    if lenses:
        L += ["**Equity lenses** (relative returns, percentage points; the run's note beside each).", "", "| lens | 1m | 3m | note |", "|---|---|---|---|"]
        for k in sorted(kk for kk in lenses if kk != "notes"):
            v = lenses[k]
            if isinstance(v, dict) and ("1m" in v or "3m" in v):
                L.append(f"| {k} | {v.get('1m')} | {v.get('3m')} | {(lenses.get('notes', {}).get(k) or '')[:150]} |")
        L.append("")
    disc = out.get("discourse") or {}
    if disc:
        L += ["**Discourse panel** (the run's N1–N6 reads; no likelihood ratio is carried by any of them).", ""]
        for k in sorted(disc):
            v = disc[k]
            L.append(f"- {k}: {(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))[:260]}")
        L.append("")
    games = out.get("games") or {}
    if games:
        L += ["**Games** (the run's G1–G4 reads).", ""]
        for k in sorted(games):
            v = games[k]
            L.append(f"- {k}: {(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))[:260]}")
        L.append("")
    L += ["## How to use this", "", "- The cases are the hypothesis set the discourse is offering. Test them; do not adopt them.",
          "- A narrative enters the baseline when two distinct holders carry it within the window; single-voice claims are marked emerging and stay in the ledger.",
          "- Adjusting a dial, a probability or a zone against this baseline is a known bias: record it in `bias_log.json` with the reason, and it is scored against the baseline when the fork resolves.", ""]
    return "\n".join(L)


def write_bias_md(bias):
    L = ["# The bias log — where judgment enters the model", "",
         "Every number in the model that a person or the orchestrator set rather than measured, beside the measured alternative where one exists. The purpose is not to remove judgment but to "
         "know where it is, so that a result can be split into what the data said and what the operator added — and so that a public reader of the dials can later set their own values "
         "against the same baseline and have the difference recorded as theirs.", "", "| kind | what | value | measured alternative | why it is judgment | note | source |", "|---|---|---|---|---|---|---|"]
    for b in bias:
        L.append(f"| {b['kind']} | {b['what'][:120]} | {b['value']} | {str(b['measured_alternative'])[:170]} | {str(b['why_judgment'])[:120]} | {(b.get('note') or '')[:140]} | {b['source']} |")
    L += ["", "Procedural rulings (hysteresis, scoring windows, what counts as a turn) live in `dials/rulings.md` and are rules of measurement rather than predictions; they are not repeated here.", ""]
    return "\n".join(L)


def main():
    run_id = None
    if "--run" in sys.argv:
        run_id = sys.argv[sys.argv.index("--run") + 1]
    out, bias, m = build(run_id)
    os.makedirs(NAR, exist_ok=True)
    json.dump(out, open(os.path.join(NAR, "ledger.json"), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(NAR, "ledger.md"), "w").write(write_md(out, m))
    open(os.path.join(NAR, "baseline.md"), "w").write(write_baseline(out))
    json.dump({"built": out["built"], "items": bias}, open(os.path.join(NAR, "bias_log.json"), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(NAR, "bias_log.md"), "w").write(write_bias_md(bias))
    with open(os.path.join(NAR, "bandwidth.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["narrative", "sweep", "sweep_items", "holders", "holder_share", "opposed", "mentions", "arguments"])
        for n in out["narratives"]:
            for r in n["sweeps"]:
                w.writerow([n["id"], r["sweep"], r["n_items"], r["n_holders"], r["holder_share"], r["n_opposed"], r["mentions"], r["arguments"]])
    held = sum(1 for n in out["narratives"] if n["bandwidth"]["holders_latest"])
    print(f"narratives: {len(out['narratives'])} in the map, {held} held in the latest sweep ({out['sweeps'][-1]['date'] if out['sweeps'] else '-'}), run {out['run']}, {len(bias)} bias items -> narratives/ledger.md, baseline.md, bias_log.md")
    if "--unassigned" in sys.argv:
        sweeps = read_sweeps()
        for sw in sweeps[-1:]:
            print(f"unassigned items in {sw['date']} ({sw['n_items']} items): matched no narrative")
            for it in sw["items"]:
                if not any(match(nar, item_text(it))[0] for nar in m["narratives"]):
                    print(f"  {it.get('kind', '')[:3]} {str(it.get('sign')):10} {(it.get('name') or '')[:36]:36} | {(it.get('position') or it.get('title') or '')[:140]}")
    if "--check" in sys.argv:
        bad = []
        for n in out["narratives"]:
            if not n.get("falsifier"):
                bad.append(f"{n['id']}: no falsifier")
            if not any(r["mentions"] for r in n["sweeps"]):
                bad.append(f"{n['id']}: matched nothing in any sweep")
            if n["sign"] not in ("n/a", "neutral", "contested") and not n["predictions"]:
                bad.append(f"{n['id']}: no predictions")
        for b in bad:
            print("CHECK", b)
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
