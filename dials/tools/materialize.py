#!/usr/bin/env python3
"""materialize.py — rebuild dials/state/ from dials/runs/ (FEED.md §2, §8).

state/ is derived and never hand-edited. This script is deterministic: the same runs/ tree produces the same
bytes (sorted keys, fixed column order, fixed float formatting), which is what test_materialize.py checks.

Usage: python3 -I dials/tools/materialize.py [--root dials] [--out dials/state]

Outputs
  ledger.json     every forecast id ever registered, with its latest registration and its resolution if any
  scoreboard.json rolling Brier / log score over resolved forecasts (all, last 20) by kind; Brier recomputed
                  from (p, outcome) and compared with the brier each run logged — a mismatch is reported, not hidden
  weights.csv     one row per run that carries a cone (dials) with H2/H3 medians, B bands, P(conf), state, s2, s3
  standoff.csv    one row per standoff run: H2/H3 R+ R- F E
  lens.csv        SUP PRIN NEO HYP TOP8 per run
  fields.csv      the field columns per run that carries point readings
  cone.csv        the raw cone log fields per run
  register.json   the gatherers' _status_<group>.json files, merged
  latest.json     run_id / run_at of the latest run of each kind
"""
import argparse, csv, glob, io, json, math, os, sys

FIELD_COLS = ["DFII10", "T5YIFR", "WTI", "IG", "HY", "CCC", "ICSA_4wk", "DGS10", "DGS30", "DXY_broad", "SPX", "E1_1m", "E2_1m", "E4_1m", "E5_1m", "E6_1m", "E7_1m", "E8_1m"]


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fmt(x):
    if x is None:
        return ""
    if isinstance(x, bool):
        return str(x).lower()
    if isinstance(x, float):
        return repr(x) if not x.is_integer() else str(int(x)) if abs(x) < 1e15 else repr(x)
    return str(x)


def csv_text(cols, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(cols)
    for r in rows:
        w.writerow([fmt(r.get(c)) for c in cols])
    return buf.getvalue()


def brier(p, o):
    return (p - o) ** 2


def logscore(p, o):
    q = p if o == 1 else 1 - p
    q = min(max(q, 1e-6), 1 - 1e-6)
    return math.log(q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="dials"); ap.add_argument("--out", default=None)
    a = ap.parse_args()
    R = a.root; out = a.out or os.path.join(R, "state")
    runs_dir = os.path.join(R, "runs")
    run_dirs = sorted(d for d in glob.glob(os.path.join(runs_dir, "*")) if os.path.isdir(d) and os.path.exists(os.path.join(d, "run.json")))
    runs = []
    for d in run_dirs:
        h = load(os.path.join(d, "run.json"))
        h["_dir"] = d
        runs.append(h)
    runs.sort(key=lambda h: (str(h.get("run_at")), h["run_id"]))

    ledger, resolved_by_id = {}, {}
    weights, standoff, lens, fields, cone_rows = [], [], [], [], []
    latest = {}
    mismatches = []
    for h in runs:
        rid, d, kind = h["run_id"], h["_dir"], h["kind"]
        if h.get("mode") != "rolled-summary":
            latest[kind] = {"run_id": rid, "run_at": h.get("run_at")}
        fp = os.path.join(d, "forecasts.json")
        if os.path.exists(fp):
            f = load(fp)
            for r in f.get("registered", []):
                prev = ledger.get(r["id"])
                rec = dict(r); rec["kind"] = kind; rec["last_seen_run"] = rid
                if prev:
                    rec["first_registered_run"] = prev.get("first_registered_run", prev.get("registered_run"))
                    rec["history"] = prev.get("history", []) + [{"run": prev["last_seen_run"], "p": prev["p"]}]
                else:
                    rec["first_registered_run"] = r.get("registered_run") or rid
                    rec["history"] = []
                ledger[r["id"]] = rec
            for r in f.get("resolved", []):
                rec = dict(r); rec["kind"] = kind; rec["resolved_in_run"] = rid
                rec["brier_recomputed"] = round(brier(r["p"], r["outcome"]), 6)
                rec["log_score"] = round(logscore(r["p"], r["outcome"]), 6)
                if r.get("brier") is not None and abs(rec["brier_recomputed"] - r["brier"]) > 1e-9:
                    mismatches.append({"id": r["id"], "logged": r["brier"], "recomputed": rec["brier_recomputed"], "run": rid})
                resolved_by_id[r["id"]] = rec
        cp = os.path.join(d, "cone.json")
        if os.path.exists(cp):
            c = load(cp)
            if kind == "dials":
                H2, H3 = c.get("H2") or [None] * 3, c.get("H3") or [None] * 3
                b2, b3 = c.get("H2_IQR_B") or [None] * 2, c.get("H3_IQR_B") or [None] * 2
                weights.append({"run_id": rid, "run_at": h.get("run_at"), "mode": h.get("mode"), "H2_A": H2[0], "H2_B": H2[1], "H2_C": H2[2], "H2_B_q25": b2[0], "H2_B_q75": b2[1],
                                "H3_A": H3[0], "H3_B": H3[1], "H3_C": H3[2], "H3_B_q25": b3[0], "H3_B_q75": b3[1], "P_B_conf": c.get("P_B_conf"), "P_C_conf": c.get("P_C_conf"),
                                "drift_B": c.get("drift_B"), "state": c.get("state"), "s2": c.get("s2"), "s3": c.get("s3"), "hand_weights": c.get("hand_weights", False)})
                cone_rows.append({"run_id": rid, "run_at": h.get("run_at"), **{k: (json.dumps(v) if isinstance(v, (list, dict)) else v) for k, v in c.items() if k not in ("source", "published_band")}})
            elif kind == "standoff":
                H2, H3 = c["H2"], c["H3"]
                standoff.append({"run_id": rid, "run_at": h.get("run_at"), "H2_Rp": H2["R+"], "H2_Rm": H2["R-"], "H2_F": H2["F"], "H2_E": H2["E"],
                                 "H3_Rp": H3["R+"], "H3_Rm": H3["R-"], "H3_F": H3["F"], "H3_E": H3["E"], "method": c.get("method")})
        lp = os.path.join(d, "lens.json")
        if os.path.exists(lp):
            l = load(lp)
            lens.append({"run_id": rid, "run_at": h.get("run_at"), **{k: l.get(k) for k in ("SUP", "PRIN", "NEO", "HYP", "TOP8")}})
        rp = os.path.join(d, "readings.json")
        if os.path.exists(rp):
            r = load(rp)
            if isinstance(r.get("fields"), dict):
                fields.append({"run_id": rid, "run_at": h.get("run_at"), **{k: r["fields"].get(k) for k in FIELD_COLS}})

    # ledger: attach resolutions
    for i, rec in resolved_by_id.items():
        if i in ledger:
            ledger[i]["resolution"] = rec
        else:
            ledger[i] = {"id": i, "kind": rec["kind"], "p": rec["p"], "criterion": None, "resolves": None, "registered_run": None, "first_registered_run": None,
                         "last_seen_run": rec["resolved_in_run"], "history": [], "resolution": rec, "note": "resolved line only; registration predates the migrated run folders"}
    for rec in ledger.values():
        rec["status"] = "resolved" if rec.get("resolution") else "open"
    ledger_out = {"forecasts": [ledger[k] for k in sorted(ledger)], "n_open": sum(1 for v in ledger.values() if v["status"] == "open"), "n_resolved": len(resolved_by_id)}

    # scoreboard
    def board(items):
        items = sorted(items, key=lambda r: (r.get("resolved_in_run"), r["id"]))
        out = {"n": len(items)}
        if items:
            out["brier_mean"] = round(sum(r["brier_recomputed"] for r in items) / len(items), 6)
            out["log_score_mean"] = round(sum(r["log_score"] for r in items) / len(items), 6)
            last = items[-20:]
            out["brier_last20"] = round(sum(r["brier_recomputed"] for r in last) / len(last), 6)
            out["n_last20"] = len(last)
        return out
    sb = {"all": {}, "brier_logged_vs_recomputed_mismatches": mismatches}
    for kind in sorted({r["kind"] for r in resolved_by_id.values()} | {"dials", "standoff"}):
        sb["all"][kind] = board([r for r in resolved_by_id.values() if r["kind"] == kind])

    # register from the gatherers' status files
    register = {}
    for p in sorted(glob.glob(os.path.join(R, "_status_*.json"))):
        try:
            s = load(p)
            register[s.get("group") or os.path.basename(p)[8:-5]] = s
        except Exception as e:  # a malformed status file is reported, not fatal
            register[os.path.basename(p)] = {"error": f"unreadable: {e}"}

    os.makedirs(out, exist_ok=True)
    def put(name, text):
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(text)
    put("ledger.json", json.dumps(ledger_out, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    put("scoreboard.json", json.dumps(sb, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    put("weights.csv", csv_text(["run_id", "run_at", "mode", "H2_A", "H2_B", "H2_C", "H2_B_q25", "H2_B_q75", "H3_A", "H3_B", "H3_C", "H3_B_q25", "H3_B_q75", "P_B_conf", "P_C_conf", "drift_B", "state", "s2", "s3", "hand_weights"], weights))
    put("standoff.csv", csv_text(["run_id", "run_at", "H2_Rp", "H2_Rm", "H2_F", "H2_E", "H3_Rp", "H3_Rm", "H3_F", "H3_E", "method"], standoff))
    put("lens.csv", csv_text(["run_id", "run_at", "SUP", "PRIN", "NEO", "HYP", "TOP8"], lens))
    put("fields.csv", csv_text(["run_id", "run_at"] + FIELD_COLS, fields))
    cone_cols = ["run_id", "run_at"] + sorted({k for r in cone_rows for k in r} - {"run_id", "run_at"})
    put("cone.csv", csv_text(cone_cols, cone_rows))
    put("register.json", json.dumps(register, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    put("latest.json", json.dumps(latest, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"materialized {len(runs)} runs -> {out}: ledger {ledger_out['n_open']} open / {ledger_out['n_resolved']} resolved; "
          f"dials Brier {sb['all'].get('dials', {}).get('brier_mean')} (n={sb['all'].get('dials', {}).get('n')}); mismatches {len(mismatches)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
