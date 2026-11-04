#!/usr/bin/env python3
"""Second feature family for the analog tests: the subnet at time t, and flux.

Everything here is computable at time t from the panel's own cross-section and past - nothing from any later year.

  network (the subnet as a feature)
    xs_share_credit_boom   share of other countries with a 3-year loans/GDP change above +5 pp of GDP this year
    xs_mean_d3_loans_gdp   cross-sectional mean of the 3-year loans/GDP change (others)
    xs_disp_real_rate      cross-sectional std of the ex-post real long rate (others)
    xs_mean_term_spread    cross-sectional mean term spread (others)
    xs_mean_req3y          cross-sectional mean 3-year real equity capital gain (others)
    xs_crises_now          number of other countries with a crisis beginning this year (observable within the year)
    xs_crises_last2y       number of other-country crises that began in t-1 or t-2 (strictly known)
    bloc_crises_last2y     the same, within the country's peg_base bloc (same base currency), t-1..t-2
    base_d3_loans_gdp      the bloc's base country's 3-year loans/GDP change (own value for the base itself or NA)
    base_term_spread       the base country's term spread
    xs_n                   number of other countries with data this year (coverage of the cross-section)
  rank (the relative growth race, percentile rank within the cross-section at t, 0..1)
    rank_d3_loans_gdp, rank_req3y, rank_ca_gdp, rank_rgdp_pc_growth, rank_rhp3y, rank_d1_unemp
  flux (rate of change of the state)
    z-scores use an expanding window: the median and MAD of each base feature over all country-years <= t
    speed_1y, speed_2y     root-mean-square change of the base z-vector over 1 and 2 years
    transitions_1y         number of base features whose |z| crossed 1.0 (either direction) since last year
    accel_d3_loans_gdp     one-year change of the 3-year loans/GDP change (credit acceleration)
    d1_term_spread, d1_real_eq_capgain_3y, d1_real_hp_growth_3y, d1_ca_gdp, d1_rank_d3_loans_gdp

Output: history/jst/features2.csv (iso, year, the base 20, then the families above).
Run: python3 -I history/tools/features2.py
"""
import csv, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_features, load_jst  # noqa: E402
from analogs import GROUPS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
BASE = [f for g in GROUPS.values() for f in g]


def nan(v):
    return np.nan if v in (None, "") else float(v)


def main():
    feats = load_features()
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    isos = sorted({r["iso"] for r in feats})
    years = sorted({r["year"] for r in feats})
    F = {(r["iso"], r["year"]): r for r in feats}
    # base matrix per (iso, year)
    X = {k: np.array([nan(r.get(f)) for f in BASE]) for k, r in F.items()}

    # expanding-window z-scores: scale at year t uses all rows with year <= t
    stacked = {}  # year -> matrix of all rows with year <= t (cumulative)
    rows_by_year = {y: [X[(i, y)] for i in isos if (i, y) in X] for y in years}
    Z = {}
    cum = []
    for y in years:
        cum += rows_by_year[y]
        M = np.vstack(cum)
        med = np.nanmedian(M, axis=0)
        mad = np.nanmedian(np.abs(M - med), axis=0) * 1.4826
        sd = np.nanstd(M, axis=0)
        mad = np.where((mad == 0) | np.isnan(mad), np.where((sd == 0) | np.isnan(sd), 1.0, sd), mad)
        for i in isos:
            if (i, y) in X:
                Z[(i, y)] = (X[(i, y)] - med) / mad

    out = []
    hdr = ["iso", "year"] + BASE + [
        "xs_share_credit_boom", "xs_mean_d3_loans_gdp", "xs_disp_real_rate", "xs_mean_term_spread", "xs_mean_req3y",
        "xs_crises_now", "xs_crises_last2y", "bloc_crises_last2y", "base_d3_loans_gdp", "base_term_spread", "xs_n",
        "rank_d3_loans_gdp", "rank_req3y", "rank_ca_gdp", "rank_rgdp_pc_growth", "rank_rhp3y", "rank_d1_unemp",
        "speed_1y", "speed_2y", "transitions_1y", "accel_d3_loans_gdp", "d1_term_spread", "d1_real_eq_capgain_3y",
        "d1_real_hp_growth_3y", "d1_ca_gdp", "d1_rank_d3_loans_gdp"]
    bi = {f: i for i, f in enumerate(BASE)}

    def val(i, y, f):
        r = F.get((i, y))
        return np.nan if r is None else nan(r.get(f))

    def rank_in_xs(i, y, f):
        v = val(i, y, f)
        others = [val(j, y, f) for j in isos if j != i]
        others = [o for o in others if not np.isnan(o)]
        if np.isnan(v) or len(others) < 5:
            return np.nan
        return sum(1 for o in others if o < v) / len(others)

    ranks = {}
    for y in years:
        for i in isos:
            if (i, y) in F:
                ranks[(i, y)] = rank_in_xs(i, y, "d3_loans_gdp")

    for y in years:
        for i in isos:
            if (i, y) not in F:
                continue
            others = [j for j in isos if j != i and (j, y) in F]
            def xs(f, fn):
                vals = [val(j, y, f) for j in others]
                vals = [v for v in vals if not np.isnan(v)]
                return fn(vals) if len(vals) >= 5 else np.nan
            share_boom = xs("d3_loans_gdp", lambda v: sum(1 for x in v if x > 0.05) / len(v))
            mean_d3 = xs("d3_loans_gdp", lambda v: float(np.mean(v)))
            disp_rr = xs("real_ltrate_expost", lambda v: float(np.std(v)))
            mean_ts = xs("term_spread", lambda v: float(np.mean(v)))
            mean_req = xs("real_eq_capgain_3y", lambda v: float(np.mean(v)))
            crises_now = sum(1 for j in others if jst.get((j, y), {}).get("crisisJST") == 1)
            crises_l2 = sum(1 for j in others for yy in (y - 1, y - 2) if jst.get((j, yy), {}).get("crisisJST") == 1)
            base = jst.get((i, y), {}).get("peg_base")
            bloc = [j for j in others if jst.get((j, y), {}).get("peg_base") == base and base not in (None, "", "NA", "HYBRID")]
            bloc_l2 = sum(1 for j in bloc for yy in (y - 1, y - 2) if jst.get((j, yy), {}).get("crisisJST") == 1) if bloc else np.nan
            base_d3 = val(base, y, "d3_loans_gdp") if base in isos else np.nan
            base_ts = val(base, y, "term_spread") if base in isos else np.nan
            # flux
            z0, z1, z2 = Z.get((i, y)), Z.get((i, y - 1)), Z.get((i, y - 2))
            def speed(a, b):
                if a is None or b is None:
                    return np.nan
                d = a - b
                d = d[~np.isnan(d)]
                return float(np.sqrt(np.mean(d ** 2))) if len(d) >= 10 else np.nan
            sp1, sp2 = speed(z0, z1), speed(z0, z2)
            if z0 is not None and z1 is not None:
                m = ~np.isnan(z0) & ~np.isnan(z1)
                trans = int(np.sum((np.abs(z0[m]) >= 1.0) != (np.abs(z1[m]) >= 1.0))) if m.sum() >= 10 else np.nan
            else:
                trans = np.nan
            def d1(f):
                a, b = val(i, y, f), val(i, y - 1, f)
                return np.nan if np.isnan(a) or np.isnan(b) else a - b
            rk = ranks.get((i, y), np.nan); rk1 = ranks.get((i, y - 1), np.nan)
            row = [i, y] + [val(i, y, f) for f in BASE] + [
                share_boom, mean_d3, disp_rr, mean_ts, mean_req, crises_now, crises_l2, bloc_l2, base_d3, base_ts, len(others),
                rk, rank_in_xs(i, y, "real_eq_capgain_3y"), rank_in_xs(i, y, "ca_gdp"), rank_in_xs(i, y, "rgdp_pc_growth"),
                rank_in_xs(i, y, "real_hp_growth_3y"), rank_in_xs(i, y, "d1_unemp"),
                sp1, sp2, trans, d1("d3_loans_gdp"), d1("term_spread"), d1("real_eq_capgain_3y"), d1("real_hp_growth_3y"),
                d1("ca_gdp"), (np.nan if np.isnan(rk) or np.isnan(rk1) else rk - rk1)]
            out.append(["" if (isinstance(v, float) and np.isnan(v)) else (f"{v:.6g}" if isinstance(v, float) else v) for v in row])
    with open(os.path.join(ROOT, "history", "jst", "features2.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(hdr); w.writerows(out)
    print(f"features2: {len(out)} rows x {len(hdr)} columns")


if __name__ == "__main__":
    main()
