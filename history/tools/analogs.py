#!/usr/bin/env python3
"""Analog retrieval on the JST panel: the empirical cone.

Given a state vector (a country-year from history/jst/features.csv, or a query file with today's values and their
provenance), standardize the chosen features across the panel, find the nearest country-years, and report what
followed them — crises, growth, real equity and house-price returns, rate and unemployment changes — as quantiles,
beside the same outcomes for the whole panel (the climatology, i.e. the no-skill reference).

Nothing here assumes a branch. The analogs are real paths that happened; their forward outcomes are the cone.

Usage
  python3 -I history/tools/analogs.py --iso USA --year 2007
  python3 -I history/tools/analogs.py --query history/analogs/us_2025_query.json
Options
  --k 15                 number of distinct analog episodes (one per country within a +-5-year window)
  --features credit,debt,rates,activity,valuation   feature groups (default all)
  --regime nonpeg|peg|any  restrict candidates by monetary regime: nonpeg = peg_type FLOAT or BASE (the anchor
                         country of a system is not pegged), peg = PEG (default any)
  --from-year 1870       earliest candidate year
  --min-coverage 0.6     minimum share of the chosen features the query and the candidate must both have
  --out history/analogs  output directory (a .md and a .json per query)
"""
import argparse, csv, json, math, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_features, load_jst  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
GROUPS = {
    "credit":    ["loans_gdp", "d3_loans_gdp", "d5_loans_gdp", "mort_gdp"],
    "debt":      ["debt_gdp", "d5_debt_gdp", "deficit_gdp", "r_minus_g"],
    "rates":     ["ltrate", "term_spread", "real_ltrate_expost", "cpi_infl"],
    "activity":  ["rgdp_pc_growth", "unemp", "d1_unemp", "iy", "ca_gdp"],
    "valuation": ["eq_dp", "real_eq_capgain_3y", "real_hp_growth_3y"],
}
OUTCOMES = [  # name, description
    ("crisis_1_3y", "systemic crisis within 1-3 years (share)"),
    ("rgdp_pc_1y", "real GDP per capita, next 1 year (%)"),
    ("rgdp_pc_3y", "real GDP per capita, next 3 years cumulative (%)"),
    ("req_1y", "real equity total return, next 1 year (%)"),
    ("req_3y", "real equity total return, next 3 years cumulative (%)"),
    ("rhp_3y", "real house prices, next 3 years cumulative (%)"),
    ("dltrate_1y", "long rate change, next 1 year (pp)"),
    ("dltrate_3y", "long rate change, next 3 years (pp)"),
    ("dunemp_3y", "unemployment change, next 3 years (pp)"),
    ("dloans_gdp_3y", "bank loans/GDP change, next 3 years (pp of GDP)"),
]


def pct(x):
    return None if x is None else 100.0 * x


def forward(jst, iso, y):
    """Forward outcomes from the raw (overridden) sheet."""
    def g(k, dy=0):
        r = jst.get((iso, y + dy))
        return None if r is None else r.get(k)

    def cum_real(key, n, infl_key="cpi"):
        tot = 1.0
        for k in range(1, n + 1):
            v, c0, c1 = g(key, k), g(infl_key, k - 1), g(infl_key, k)
            if v is None or c0 in (None, 0) or c1 is None:
                return None
            tot *= (1 + v) / (c1 / c0)
        return tot - 1

    def cum_growth(key, n):
        a, b = g(key, 0), g(key, n)
        return None if a in (None, 0) or b is None else b / a - 1

    nxt = [g("crisisJST", k) for k in (1, 2, 3)]
    out = {
        "crisis_1_3y": None if any(v is None for v in nxt) else (1.0 if any(v == 1 for v in nxt) else 0.0),
        "rgdp_pc_1y": pct(cum_growth("rgdpmad", 1)),
        "rgdp_pc_3y": pct(cum_growth("rgdpmad", 3)),
        "req_1y": pct(cum_real("eq_tr", 1)),
        "req_3y": pct(cum_real("eq_tr", 3)),
        "rhp_3y": None,
        "dltrate_1y": None if g("ltrate", 1) is None or g("ltrate") is None else g("ltrate", 1) - g("ltrate"),
        "dltrate_3y": None if g("ltrate", 3) is None or g("ltrate") is None else g("ltrate", 3) - g("ltrate"),
        "dunemp_3y": None if g("unemp", 3) is None or g("unemp") is None else g("unemp", 3) - g("unemp"),
        "dloans_gdp_3y": None,
    }
    hp0, hp3, c0, c3 = g("hpnom"), g("hpnom", 3), g("cpi"), g("cpi", 3)
    if None not in (hp0, hp3, c0, c3) and hp0 and c0 and c3:
        out["rhp_3y"] = pct((hp3 / c3) / (hp0 / c0) - 1)
    l0, l3, g0, g3 = g("tloans"), g("tloans", 3), g("gdp"), g("gdp", 3)
    if None not in (l0, l3, g0, g3) and g0 and g3:
        out["dloans_gdp_3y"] = 100 * (l3 / g3 - l0 / g0)
    return out


def quantiles(vals):
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    def q(p):
        i = (len(v) - 1) * p
        lo, hi = int(math.floor(i)), int(math.ceil(i))
        return v[lo] + (v[hi] - v[lo]) * (i - lo)
    return {"n": len(v), "p25": q(0.25), "p50": q(0.5), "p75": q(0.75), "mean": sum(v) / len(v)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iso"); ap.add_argument("--year", type=int); ap.add_argument("--query")
    ap.add_argument("--k", type=int, default=15); ap.add_argument("--features", default="credit,debt,rates,activity,valuation")
    ap.add_argument("--regime", default="any"); ap.add_argument("--from-year", type=int, default=1870)
    ap.add_argument("--min-coverage", type=float, default=0.6); ap.add_argument("--out", default="history/analogs")
    a = ap.parse_args()

    feats = [f for gname in a.features.split(",") for f in GROUPS[gname]]
    rows = load_features()
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    peg = {k: v.get("peg_type") for k, v in jst.items()}

    # the query vector
    prov = {}
    if a.query:
        qj = json.load(open(a.query))
        q = {k: v["value"] for k, v in qj["features"].items()}
        prov = {k: v for k, v in qj["features"].items()}
        qname, qlabel = qj.get("name", os.path.basename(a.query)), qj.get("label", a.query)
        exclude = set()
    else:
        qr = next(r for r in rows if r["iso"] == a.iso and r["year"] == a.year)
        q = {f: qr.get(f) for f in feats}
        qname, qlabel = f"{a.iso}_{a.year}", f"{a.iso} {a.year} (from features.csv)"
        exclude = {(a.iso, y) for y in range(a.year - 5, a.year + 6)}
    q = {f: q.get(f) for f in feats}
    q_have = [f for f in feats if q[f] is not None]
    if len(q_have) / len(feats) < a.min_coverage:
        sys.exit(f"query covers {len(q_have)}/{len(feats)} features; below --min-coverage")

    # robust standardization across the panel (median / MAD per feature), on candidate rows
    REG = {"any": None, "nonpeg": {"FLOAT", "BASE"}, "peg": {"PEG"}, "FLOAT": {"FLOAT", "BASE"}, "PEG": {"PEG"}}
    allowed = REG.get(a.regime, {a.regime})
    cands = [r for r in rows if r["year"] >= a.from_year and (r["iso"], r["year"]) not in exclude
             and (allowed is None or peg.get((r["iso"], r["year"])) in allowed)]
    scale = {}
    for f in q_have:
        vals = sorted(r[f] for r in cands if r.get(f) is not None)
        if len(vals) < 50:
            continue
        med = statistics.median(vals)
        mad = statistics.median(abs(v - med) for v in vals) or (statistics.pstdev(vals) / 1.4826 if len(vals) > 1 else 1.0)
        scale[f] = (med, 1.4826 * mad if mad else 1.0)
    use = [f for f in q_have if f in scale]

    # distances
    scored = []
    for r in cands:
        have = [f for f in use if r.get(f) is not None]
        if len(have) / len(feats) < a.min_coverage:
            continue
        d2 = sum(((q[f] - scale[f][0]) / scale[f][1] - (r[f] - scale[f][0]) / scale[f][1]) ** 2 for f in have)
        scored.append((math.sqrt(d2 / len(have)), r, have))
    scored.sort(key=lambda t: t[0])
    # one episode per country within +-5 years
    picked, taken = [], set()
    for d, r, have in scored:
        key = (r["iso"], r["year"])
        if any((r["iso"], y) in taken for y in range(r["year"] - 5, r["year"] + 6)):
            continue
        picked.append((d, r, have)); taken.add(key)
        if len(picked) >= a.k:
            break

    # outcomes: analogs vs climatology (all candidate rows)
    an_out = [forward(jst, r["iso"], r["year"]) for _, r, _ in picked]
    cl_out = [forward(jst, r["iso"], r["year"]) for r in cands]
    summary = {}
    for name, desc in OUTCOMES:
        summary[name] = {"description": desc,
                         "analogs": quantiles([o[name] for o in an_out]),
                         "climatology": quantiles([o[name] for o in cl_out])}

    # write
    os.makedirs(os.path.join(ROOT, a.out), exist_ok=True)
    base = os.path.join(ROOT, a.out, qname)
    res = {"query": qlabel, "features_used": use, "features_requested": feats, "query_values": {f: q[f] for f in use},
           "query_provenance": prov, "regime": a.regime, "from_year": a.from_year, "k": a.k, "candidates": len(cands),
           "analogs": [{"iso": r["iso"], "year": r["year"], "distance": round(d, 3), "features_matched": len(have),
                        "values": {f: r.get(f) for f in use}, "outcomes": o} for (d, r, have), o in zip(picked, an_out)],
           "summary": summary}
    json.dump(res, open(base + ".json", "w"), indent=1)
    L = [f"# Analogs for {qlabel}", "",
         f"Features used ({len(use)} of {len(feats)} requested): {', '.join(use)}. Candidates: {len(cands)} country-years "
         f"(regime {a.regime}, from {a.from_year}); the query's own country within ±5 years is excluded. Distance is the "
         f"root-mean-square of robust z-score differences over the features both sides have. One episode per country "
         f"within ±5 years.", "",
         "## Query", "", "| feature | value | provenance |", "|---|---|---|"]
    for f in use:
        p = prov.get(f, {})
        L.append(f"| {f} | {q[f]:.4g} | {p.get('source', 'features.csv')} |")
    L += ["", f"## The {len(picked)} nearest episodes", "",
          "| # | country | year | distance | crisis in 1-3y | rGDP/cap next 3y | real equity next 3y | real houses next 3y | Δ long rate 3y | Δ unemp 3y |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for i, ((d, r, have), o) in enumerate(zip(picked, an_out), 1):
        def fmt(v, suf=""):
            return "—" if v is None else f"{v:+.1f}{suf}"
        L.append(f"| {i} | {r['iso']} | {r['year']} | {d:.2f} | {'yes' if o['crisis_1_3y'] == 1 else ('no' if o['crisis_1_3y'] == 0 else '—')} | "
                 f"{fmt(o['rgdp_pc_3y'], '%')} | {fmt(o['req_3y'], '%')} | {fmt(o['rhp_3y'], '%')} | {fmt(o['dltrate_3y'], ' pp')} | {fmt(o['dunemp_3y'], ' pp')} |")
    L += ["", "## What followed: analogs vs climatology", "",
          "| outcome | analogs p25 / p50 / p75 (n) | climatology p25 / p50 / p75 (n) |", "|---|---|---|"]
    for name, desc in OUTCOMES:
        s = summary[name]
        def qs(x):
            if not x:
                return "—"
            if name == "crisis_1_3y":
                return f"share {x['mean']:.0%} (n={x['n']})"
            return f"{x['p25']:+.1f} / {x['p50']:+.1f} / {x['p75']:+.1f} (n={x['n']})"
        L.append(f"| {desc} | {qs(s['analogs'])} | {qs(s['climatology'])} |")
    L += ["", "Climatology is the same outcome over every candidate country-year: the no-skill reference. Where the analog "
          "quantiles sit inside the climatology's, the state vector carried information; where they do not, it did not. "
          "Nothing here is a forecast of the dials' branches; it is the record's answer to 'what followed states like this one'.", ""]
    open(base + ".md", "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
