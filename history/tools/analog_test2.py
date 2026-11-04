#!/usr/bin/env python3
"""Analog test, second design: does giving the method the subnet at time t and the state's flux recover the skill the
leak had borrowed? Walk-forward only (expanding-window standardization; candidates' outcome windows closed before the
query year; own episode excluded), k nearest, one episode per country.

Feature families (history/jst/features2.csv, built by features2.py):
  base      the 20 original state features (levels and changes of the country's own series)
  network   the subnet at t: cross-sectional shares, means and dispersion of the others, crises already begun
            elsewhere, the bloc and its base country
  rank      the relative growth race: percentile rank within the cross-section at t
  flux      speed of the state in z-space, band transitions, accelerations
Targets: crisis within 1..5 years (the JST label), and four measured stress events within 3 years - a 30% real equity
drawdown, a 5-pp credit contraction, a 3-pp unemployment spike, a 5% real GDP per capita fall - plus a measured
composite (3 of 5 stress conditions in one year).

Usage: python3 -I history/tools/analog_test2.py [--k 15] [--min-coverage 0.6] [--from-year 1880]
Writes history/analogs/test2.md and test2.json.
"""
import argparse, csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from analogs import GROUPS  # noqa: E402
from wf import walk_forward_neighbors, predict, auc, top_decile, build_targets  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
BASE = [f for g in GROUPS.values() for f in g]
NETWORK = ["xs_share_credit_boom", "xs_mean_d3_loans_gdp", "xs_disp_real_rate", "xs_mean_term_spread", "xs_mean_req3y",
           "xs_crises_now", "xs_crises_last2y", "bloc_crises_last2y", "base_d3_loans_gdp", "base_term_spread"]
RANK = ["rank_d3_loans_gdp", "rank_req3y", "rank_ca_gdp", "rank_rgdp_pc_growth", "rank_rhp3y", "rank_d1_unemp"]
FLUX = ["speed_1y", "speed_2y", "transitions_1y", "accel_d3_loans_gdp", "d1_term_spread", "d1_real_eq_capgain_3y",
        "d1_real_hp_growth_3y", "d1_ca_gdp", "d1_rank_d3_loans_gdp"]
FAMILIES = {"base": BASE, "network": NETWORK, "rank": RANK, "flux": FLUX,
            "base+network": BASE + NETWORK, "base+flux": BASE + FLUX, "base+rank": BASE + RANK,
            "base+network+flux": BASE + NETWORK + FLUX, "all": BASE + NETWORK + RANK + FLUX}
TARGETS3 = ["crisis_3y", "stress3_3y", "dd30_3y", "credit_contraction_3y", "unemp_spike_3y", "gdp_fall_3y"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=15); ap.add_argument("--min-coverage", type=float, default=0.6)
    ap.add_argument("--from-year", type=int, default=1880)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(os.path.join(ROOT, "history", "jst", "features2.csv"))))
    isos = [r["iso"] for r in rows]; years = [int(r["year"]) for r in rows]
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    T = build_targets(jst, isos, years)
    base_rates = {t: float(np.nanmean(T[t])) for t in T}
    rep = {"k": a.k, "min_coverage": a.min_coverage, "from_year": a.from_year, "base_rates": base_rates,
           "families": {f: {"n_features": len(v)} for f, v in FAMILIES.items()}, "results": {}, "horizon": {}, "leak_check": {}}

    def mat(cols):
        return np.array([[np.nan if r[c] in ("", None) else float(r[c]) for c in cols] for r in rows], dtype=float)

    # 1) families x 3-year targets, walk-forward
    for fam, cols in FAMILIES.items():
        X = mat(cols)
        nb = walk_forward_neighbors(X, isos, years, horizon=3, k=a.k, min_cov=a.min_coverage, from_year=a.from_year)
        res = {}
        for t in TARGETS3:
            p = predict(nb, T[t]); A, npos, nneg = auc(p, T[t]); td, base = top_decile(p, T[t])
            res[t] = {"auc": A, "n_pos": npos, "n_neg": nneg, "top_decile": td, "base": base}
        rep["results"][fam] = res
        print(fam, {t: (round(v["auc"], 3) if v["auc"] else None) for t, v in res.items()})

    # 2) crisis AUC by horizon for base and all (candidates' windows closed per horizon)
    for fam in ("base", "base+network+flux", "all"):
        X = mat(FAMILIES[fam]); curve = {}
        for h in (1, 2, 3, 4, 5):
            nb = walk_forward_neighbors(X, isos, years, horizon=h, k=a.k, min_cov=a.min_coverage, from_year=a.from_year)
            p = predict(nb, T[f"crisis_{h}y"]); A, npos, nneg = auc(p, T[f"crisis_{h}y"])
            curve[h] = {"auc": A, "n_pos": npos, "n_neg": nneg}
        rep["horizon"][fam] = curve
        print("horizon", fam, {h: round(v["auc"], 3) for h, v in curve.items() if v["auc"]})

    # 3) the leak check on this harness: base features, same-country vs block-year vs walk-forward, crisis_3y
    X = mat(BASE)
    for mode in ("same-country", "block-year", "walk-forward"):
        nb = walk_forward_neighbors(X, isos, years, horizon=3, k=a.k, min_cov=a.min_coverage, from_year=a.from_year, mode=mode)
        p = predict(nb, T["crisis_3y"]); A, _, _ = auc(p, T["crisis_3y"]); td, base = top_decile(p, T["crisis_3y"])
        rep["leak_check"][mode] = {"auc": A, "top_decile": td, "base": base}
    print("leak check", {m: round(v["auc"], 3) for m, v in rep["leak_check"].items()})

    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    json.dump(rep, open(os.path.join(ROOT, "history", "analogs", "test2.json"), "w"), indent=1)
    L = ["# Analog test 2 — the subnet at t, and flux", "",
         f"Walk-forward only: z-scores from an expanding window (rows ≤ the query year), candidates whose outcome window "
         f"closed before the query year, own country within ±5 years excluded, one episode per country within ±5 years, "
         f"k={a.k}, coverage ≥ {a.min_coverage:.0%}, queries from {a.from_year}. AUC 0.5 is no skill.", "",
         "## Walk-forward AUC by feature family and 3-year target", "",
         "| family (features) | " + " | ".join(TARGETS3) + " |", "|---|" + "---|" * len(TARGETS3)]
    for fam, res in rep["results"].items():
        L.append(f"| {fam} ({len(FAMILIES[fam])}) | " + " | ".join(
            (f"{v['auc']:.2f} (top {v['top_decile']:.0%} vs {v['base']:.0%})" if v["auc"] is not None else "—") for v in res.values()) + " |")
    L += ["", "Base rates: " + ", ".join(f"{t} {base_rates[t]:.1%}" for t in TARGETS3), "",
          "## Crisis AUC by horizon (JST label)", "", "| family | 1y | 2y | 3y | 4y | 5y |", "|---|---|---|---|---|---|"]
    for fam, curve in rep["horizon"].items():
        L.append(f"| {fam} | " + " | ".join(f"{curve[h]['auc']:.2f}" if curve[h]["auc"] else "—" for h in (1, 2, 3, 4, 5)) + " |")
    L += ["", "## Leak check on this harness (base features, crisis within 3 years)", "",
          "| exclusion | AUC | top decile vs base |", "|---|---|---|"]
    for m, v in rep["leak_check"].items():
        L.append(f"| {m} | {v['auc']:.2f} | {v['top_decile']:.0%} vs {v['base']:.0%} |")
    L += ["", "Targets: `crisis_hy` = a JST-labelled systemic banking crisis begins within h years; `stress3_3y` = in some year "
          "of the next three, at least 3 of 5 measured conditions hold (real equity ≤ −20%, real GDP/cap ≤ −2%, unemployment "
          "+1.5 pp, loans/GDP −2 pp, bank capital ratio −0.7 pp); `dd30_3y` = the real equity path falls 30% within 3 years; "
          "`credit_contraction_3y` = loans/GDP down 5 pp of GDP at some point within 3 years; `unemp_spike_3y` = unemployment "
          "+3 pp within 3 years; `gdp_fall_3y` = real GDP per capita −5% within 3 years. All censored unless the full window exists.", ""]
    open(os.path.join(ROOT, "history", "analogs", "test2.md"), "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
