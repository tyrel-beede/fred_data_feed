#!/usr/bin/env python3
"""The live US query vector: the 20 base analog features for a current year, built from the JST sheet through 2020
and the FRED bridge (history/bridge/us/, pulled by bridge_pull.py in the workflow) from 2021, with Shiller's workbooks
(history/corporate/raw/SHILLER/) for dividends, equity prices and house prices.

Join rules (history/bridge/join_rules.json, written here): each JST column that the bridge carries is joined either at
level (rates, ratios, the fiscal flows: the 2016-2020 overlap ratio is within a few percent of 1) or by a ratio splice
chained at the last overlap year (indices and aggregates with their own base or definition: CPI, house prices, real
GDP per capita, loans, mortgages, the current account). The overlap table is recomputed and written every run from
the stored JST values, so the ratios are measured, not remembered. Nothing in the JST sheet is edited.

For the current year the bridge rows are year-to-date means (rates, indices, levels) or year-to-date sums (flows); a
flow is annualized by the quarters observed; nominal GDP for the current year is the mean of the quarterly SAAR
series from the corporate layer when the annual series has not printed.

Usage: python3 -I history/tools/live_query.py --year 2026 [--out history/analogs/us_2026ytd_query.json]
Then:  python3 -I history/tools/analogs.py --query history/analogs/us_2026ytd_query.json
"""
import argparse, csv, json, os, re, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
import corporate_build as cb  # noqa: E402  (Shiller readers)

ROOT = os.path.dirname(os.path.dirname(HERE))
BRIDGE = os.path.join(ROOT, "history", "bridge")
OVERLAP = (2016, 2020)

# JST column -> (bridge series, aggregation, unit scale bridge->JST unit, join rule, note)
MAP = {
    "ltrate": ("DGS10", "mean", 1.0, "level", "10-year Treasury constant maturity, annual mean of daily"),
    "stir": ("TB3MS", "mean", 1.0, "level", "3-month bill, annual mean of monthly"),
    "cpi": ("CPIAUCSL", "mean", 1.0, "ratio", "CPI-U 1982-84=100 against the JST base: ratio chained at 2020"),
    "unemp": ("UNRATE", "mean", 1.0, "level", "unemployment rate, annual mean of monthly"),
    "gdp": ("GDPA", "last", 1.0, "ratio", "nominal GDP, annual, billions; JST vintage differs by under 1%"),
    "debtgdp": ("GFDEGDQ188S", "mean", 0.01, "ratio", "federal debt / GDP, percent -> ratio"),
    "revenue": ("FYFR", "last", 1e-3, "level", "federal receipts, fiscal year, millions -> billions"),
    "expenditure": ("FYONET", "last", 1e-3, "level", "federal outlays, fiscal year, millions -> billions"),
    "money": ("M2SL", "mean", 1.0, "level", "M2, annual mean of monthly, billions"),
    "narrowm": ("BOGMBASE", "mean", 1.0, "level", "monetary base, billions as FRED now reports it (JST US narrow money is the base)"),
    "hpnom": ("CSUSHPISA", "mean", 1.0, "ratio", "Case-Shiller national, Jan 2000=100: ratio chained at 2020"),
    "ca": ("IEABC", "sum", 1e-3, "ratio", "current account, quarterly millions summed -> billions; annualized by quarters observed"),
    "rgdpmad": ("A939RX0Q048SBEA", "mean", 1.0, "ratio", "real GDP per capita, chained 2017$ -> Maddison 1990 int$: ratio chained at 2020"),
    "tloans": ("TOTLL", "mean", 1.0, "ratio", "loans and leases in bank credit, billions; JST total loans are broader: ratio chained at 2020"),
    "tmort": ("HHMSDODNS", "mean", 1e-3, "ratio", "household mortgages, millions -> billions; JST mortgages differ in scope: ratio chained at 2020"),
}
BASE = ["loans_gdp", "d3_loans_gdp", "d5_loans_gdp", "mort_gdp", "debt_gdp", "d5_debt_gdp", "deficit_gdp", "r_minus_g", "ltrate",
        "term_spread", "real_ltrate_expost", "cpi_infl", "rgdp_pc_growth", "unemp", "d1_unemp", "iy", "ca_gdp", "eq_dp",
        "real_eq_capgain_3y", "real_hp_growth_3y"]


def read_series(sid):
    p = os.path.join(BRIDGE, "us", f"{sid}.csv")
    out = []
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try:
                out.append((r["date"], float(r["value"])))
            except (ValueError, KeyError):
                pass
    return out


def annual(obs, y, how):
    v = [val for d, val in obs if d.startswith(str(y))]
    if not v:
        return np.nan, 0
    if how == "mean":
        return float(np.mean(v)), len(v)
    if how == "last":
        return v[-1], len(v)
    return float(np.sum(v)), len(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=time.gmtime().tm_year)
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    Y = a.year
    jst = {r["year"]: r for r in load_jst(apply_overrides=True) if r["iso"] == "USA"}

    def J(y, k):
        r = jst.get(y)
        return np.nan if r is None or r.get(k) in (None, "") else float(r[k])

    # ---- 1. the bridge, in JST units, and the overlap -> join rules
    rules, overlap_rows = {}, []
    ext = {}  # year -> {jst column: value} for years > 2020 (and the overlap years, for the check)
    for col, (sid, how, scale, rule, note) in MAP.items():
        obs = read_series(sid)
        vals = {}
        for y in range(OVERLAP[0], Y + 1):
            v, n = annual(obs, y, how)
            if np.isnan(v):
                continue
            if how == "sum" and y == Y and n < 4:
                v = v * 4.0 / n  # annualize the current year's flow by the quarters observed
            vals[y] = (v * scale, n)
        ratios = {y: J(y, col) / vals[y][0] for y in range(OVERLAP[0], OVERLAP[1] + 1) if y in vals and not np.isnan(J(y, col)) and vals[y][0]}
        for y, rr in ratios.items():
            overlap_rows.append({"jst_column": col, "series": sid, "year": y, "jst": f"{J(y, col):.6g}", "bridge_in_jst_units": f"{vals[y][0]:.6g}", "ratio": f"{rr:.4f}"})
        k = 1.0
        if rule == "ratio" and ratios:
            k = ratios[max(ratios)]  # chain at the last overlap year
        rules[col] = {"series": sid, "aggregation": how, "scale": scale, "rule": rule, "factor": k,
                      "overlap_ratios": {str(y): round(r, 4) for y, r in ratios.items()}, "note": note}
        for y, (v, n) in vals.items():
            ext.setdefault(y, {})[col] = (v * k, f"FRED {sid} {y} ({how} of {n} obs){' x ' + format(k, '.4g') if rule == 'ratio' else ''}")
    # nominal GDP for the current year, if the annual series has not printed: mean of the quarterly SAAR series
    if "gdp" not in ext.get(Y, {}):
        qp = os.path.join(ROOT, "history", "corporate", "raw", "FRED-Z1", "gdp_nominal_q.csv")
        if os.path.exists(qp):
            q = [float(r["value"]) for r in csv.DictReader(open(qp)) if r["date"].startswith(str(Y))]
            if q:
                ext.setdefault(Y, {})["gdp"] = (float(np.mean(q)) * rules["gdp"]["factor"], f"FRED GDP quarterly SAAR, mean of {len(q)} quarters of {Y} x {rules['gdp']['factor']:.4g}")
    # investment share: real investment / real GDP from the bridge, checked against JST iy over the overlap
    gp, gc = read_series("GPDIC1"), read_series("GDPC1")
    iy_b = {}
    for y in range(OVERLAP[0], Y + 1):
        i, ni = annual(gp, y, "mean"); g, ng = annual(gc, y, "mean")
        if not np.isnan(i) and not np.isnan(g) and g:
            iy_b[y] = (i / g, ni)
    iy_ratios = {y: J(y, "iy") / iy_b[y][0] for y in range(OVERLAP[0], OVERLAP[1] + 1) if y in iy_b and not np.isnan(J(y, "iy"))}
    k_iy = iy_ratios[max(iy_ratios)] if iy_ratios else 1.0
    rules["iy"] = {"series": "GPDIC1/GDPC1", "rule": "ratio", "factor": k_iy, "overlap_ratios": {str(y): round(r, 4) for y, r in iy_ratios.items()},
                   "note": "real investment / real GDP against JST nominal I/GDP: ratio chained at 2020"}
    for y, (v, n) in iy_b.items():
        ext.setdefault(y, {})["iy"] = (v * k_iy, f"FRED GPDIC1/GDPC1 {y} (mean of {n} quarters) x {k_iy:.4g}")
    # Shiller: dividend yield, equity capital gain, house prices
    sh = cb.read_shiller(); hp = cb.read_fig31()
    def sh_year(y, key):
        v = [sh[(y, m)].get(key, np.nan) for m in range(1, 13) if (y, m) in sh]
        v = [x for x in v if not np.isnan(x)]
        return (float(np.mean(v)), len(v)) if v else (np.nan, 0)
    dp = {}
    for y in range(OVERLAP[0], Y + 1):
        d, nd = sh_year(y, "d"); p, npx = sh_year(y, "p")
        if not np.isnan(d) and not np.isnan(p) and p:
            dp[y] = (d / p, min(nd, npx))
    dp_ratios = {y: J(y, "eq_dp") / dp[y][0] for y in range(OVERLAP[0], OVERLAP[1] + 1) if y in dp and not np.isnan(J(y, "eq_dp"))}
    rules["eq_dp"] = {"series": "Shiller D/P (annual mean of monthly)", "rule": "level", "factor": 1.0,
                      "overlap_ratios": {str(y): round(r, 4) for y, r in dp_ratios.items()}, "note": "S&P composite dividend yield; JST eq_dp is the same concept"}
    for y, (v, n) in dp.items():
        ext.setdefault(y, {})["eq_dp"] = (v, f"Shiller ie_data D/P {y} (mean of {n} months)")
    px = {}
    for y in range(OVERLAP[0] - 4, Y + 1):
        p, n = sh_year(y, "p")
        if not np.isnan(p):
            px[y] = (p, n)
    cg_ratios = {}
    for y in range(OVERLAP[0], OVERLAP[1] + 1):
        if y in px and (y - 1) in px and not np.isnan(J(y, "eq_capgain")):
            cg_ratios[y] = (px[y][0] / px[y - 1][0] - 1) - J(y, "eq_capgain")
    rules["eq_capgain"] = {"series": "Shiller P (annual mean of monthly), yearly change", "rule": "level", "factor": 1.0,
                           "overlap_differences": {str(y): round(r, 4) for y, r in cg_ratios.items()}, "note": "nominal capital gain of the S&P composite against JST eq_capgain (differences, not ratios)"}
    for y, (p, n) in px.items():
        if (y - 1) in px:
            ext.setdefault(y, {})["eq_capgain"] = (p / px[y - 1][0] - 1, f"Shiller ie_data P {y}/{y - 1} (annual means, {n} months in {y})")
    hpn = {y: hp[y]["nominal_hpi"] for y in hp if "nominal_hpi" in hp[y]}
    hp_ratios = {y: J(y, "hpnom") / hpn[y] for y in range(OVERLAP[0], OVERLAP[1] + 1) if y in hpn and not np.isnan(J(y, "hpnom"))}
    k_hp = hp_ratios[max(hp_ratios)] if hp_ratios else 1.0
    rules["hpnom_shiller"] = {"series": "Shiller Figure 3.1 nominal home price index (annual mean of monthly)", "rule": "ratio", "factor": k_hp,
                              "overlap_ratios": {str(y): round(r, 4) for y, r in hp_ratios.items()},
                              "note": "used for hpnom when it runs later than Case-Shiller in the bridge (same underlying index after 1987)"}
    for y, v in hpn.items():
        if y > OVERLAP[1] and ("hpnom" not in ext.get(y, {})):
            ext.setdefault(y, {})["hpnom"] = (v * k_hp, f"Shiller Figure 3.1 nominal HPI {y} x {k_hp:.4g}")

    # ---- 2. the extended annual row set: JST through 2020, the bridge after
    def V(y, k):
        if y <= OVERLAP[1]:
            v = J(y, k); return (v, f"JST USA {y} {k}") if not np.isnan(v) else (np.nan, "")
        e = ext.get(y, {}).get(k)
        return e if e else (np.nan, "")
    def val(y, k):
        return V(y, k)[0]
    def ratio(aa, bb):
        return np.nan if np.isnan(aa) or np.isnan(bb) or bb == 0 else aa / bb
    def growth(y, k, n=1):
        aa, bb = val(y, k), val(y - n, k)
        return np.nan if np.isnan(aa) or np.isnan(bb) or bb <= 0 or aa <= 0 else (aa / bb) ** (1.0 / n) - 1.0
    def loans_gdp(y): return ratio(val(y, "tloans"), val(y, "gdp"))
    def mort_gdp(y): return ratio(val(y, "tmort"), val(y, "gdp"))
    def real_hp(y): return ratio(val(y, "hpnom"), val(y, "cpi"))
    def real_eq_capgain(y, n):
        tot = 1.0
        for k in range(n):
            cg, infl = val(y - k, "eq_capgain"), growth(y - k, "cpi")
            if np.isnan(cg) or np.isnan(infl):
                return np.nan
            tot *= (1 + cg) / (1 + infl)
        return tot ** (1.0 / n) - 1.0
    ng, lt, st, infl, dg = growth(Y, "gdp"), val(Y, "ltrate"), val(Y, "stir"), growth(Y, "cpi"), val(Y, "debtgdp")
    rhp0, rhp3 = real_hp(Y), real_hp(Y - 3)
    F = {
        "loans_gdp": loans_gdp(Y), "d3_loans_gdp": loans_gdp(Y) - loans_gdp(Y - 3), "d5_loans_gdp": loans_gdp(Y) - loans_gdp(Y - 5),
        "mort_gdp": mort_gdp(Y), "debt_gdp": dg, "d5_debt_gdp": dg - val(Y - 5, "debtgdp"),
        "deficit_gdp": ratio(val(Y, "expenditure") - val(Y, "revenue"), val(Y, "gdp")),
        "r_minus_g": lt - 100 * ng, "ltrate": lt, "term_spread": lt - st, "real_ltrate_expost": lt - 100 * infl, "cpi_infl": infl,
        "rgdp_pc_growth": growth(Y, "rgdpmad"), "unemp": val(Y, "unemp"), "d1_unemp": val(Y, "unemp") - val(Y - 1, "unemp"),
        "iy": val(Y, "iy"), "ca_gdp": ratio(val(Y, "ca"), val(Y, "gdp")), "eq_dp": val(Y, "eq_dp"),
        "real_eq_capgain_3y": real_eq_capgain(Y, 3),
        "real_hp_growth_3y": np.nan if np.isnan(rhp0) or np.isnan(rhp3) or rhp3 <= 0 else (rhp0 / rhp3) ** (1 / 3) - 1,
    }
    inputs = {  # which underlying values each feature used (for provenance)
        "loans_gdp": [(Y, "tloans"), (Y, "gdp")], "d3_loans_gdp": [(Y, "tloans"), (Y, "gdp"), (Y - 3, "tloans"), (Y - 3, "gdp")],
        "d5_loans_gdp": [(Y, "tloans"), (Y, "gdp"), (Y - 5, "tloans"), (Y - 5, "gdp")], "mort_gdp": [(Y, "tmort"), (Y, "gdp")],
        "debt_gdp": [(Y, "debtgdp")], "d5_debt_gdp": [(Y, "debtgdp"), (Y - 5, "debtgdp")], "deficit_gdp": [(Y, "expenditure"), (Y, "revenue"), (Y, "gdp")],
        "r_minus_g": [(Y, "ltrate"), (Y, "gdp"), (Y - 1, "gdp")], "ltrate": [(Y, "ltrate")], "term_spread": [(Y, "ltrate"), (Y, "stir")],
        "real_ltrate_expost": [(Y, "ltrate"), (Y, "cpi"), (Y - 1, "cpi")], "cpi_infl": [(Y, "cpi"), (Y - 1, "cpi")],
        "rgdp_pc_growth": [(Y, "rgdpmad"), (Y - 1, "rgdpmad")], "unemp": [(Y, "unemp")], "d1_unemp": [(Y, "unemp"), (Y - 1, "unemp")],
        "iy": [(Y, "iy")], "ca_gdp": [(Y, "ca"), (Y, "gdp")], "eq_dp": [(Y, "eq_dp")],
        "real_eq_capgain_3y": [(y, k) for y in (Y, Y - 1, Y - 2) for k in ("eq_capgain", "cpi")] + [(Y - 3, "cpi")],
        "real_hp_growth_3y": [(Y, "hpnom"), (Y, "cpi"), (Y - 3, "hpnom"), (Y - 3, "cpi")],
    }
    features, missing = {}, []
    for f in BASE:
        v = F[f]
        if isinstance(v, float) and np.isnan(v):
            lacking = [f"{k}@{y}" for y, k in inputs[f] if np.isnan(val(y, k))]
            missing.append(f"{f} (no value for {', '.join(lacking)})"); continue
        features[f] = {"value": float(v), "source": "; ".join(sorted({V(y, k)[1] for y, k in inputs[f]}))}
    ytd = sorted({f"{k}: {ext[Y][k][1]}" for k in ext.get(Y, {})})
    out = {"name": f"us_{Y}ytd", "label": f"United States {Y} year-to-date (built by live_query.py from the JST sheet through 2020 and the FRED bridge, "
                                           f"Shiller workbooks; {len(features)} of {len(BASE)} features)",
           "as_of": time.strftime("%Y-%m-%d", time.gmtime()), "node": "fred_data_feed/history", "features": features,
           "missing": "; ".join(missing) if missing else "", "join_rules": "history/bridge/join_rules.json", "current_year_inputs": ytd}
    dest = a.out or os.path.join(ROOT, "history", "analogs", f"us_{Y}ytd_query.json")
    json.dump(out, open(dest, "w"), indent=1)
    json.dump({"overlap_years": list(OVERLAP), "rules": rules, "built": out["as_of"]}, open(os.path.join(BRIDGE, "join_rules.json"), "w"), indent=1)
    with open(os.path.join(BRIDGE, "us_overlap_check.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["jst_column", "series", "year", "jst", "bridge_in_jst_units", "ratio"]); w.writeheader(); w.writerows(overlap_rows)
    print(f"{dest}: {len(features)}/{len(BASE)} features; missing: {missing}")
    for k, r in rules.items():
        print(f"  {k:14s} {r['rule']:6s} factor {r['factor']:.4g}  overlap {r.get('overlap_ratios') or r.get('overlap_differences')}")
    for f, d in features.items():
        print(f"  {f:22s} {d['value']:10.4f}  <- {d['source'][:110]}")


if __name__ == "__main__":
    main()
