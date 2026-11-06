#!/usr/bin/env python3
"""Climatology: the unconditional distribution of every base feature and of every forward outcome, by topology era
and by regime — what a forecast relaxes toward at long lead times, and the no-skill reference every analog cone is
read against.

Eras are the measured topology breaks (tools/topology.py: 1914, 1932, 1940, 1973) plus 1999 for the euro bloc, so
the index is the network's arrangement, not a hand-dated narrative; regimes are the JST peg_type (BASE, PEG, FLOAT).
For each (era, regime) cell with at least 30 country-years: the 10th, 25th, 50th, 75th and 90th percentiles of each
base feature; the base rate of each 3-year event target; the quantiles of each forward outcome used by the analog
reports (real GDP per capita, real equity, real houses, the long rate, unemployment, loans/GDP, over 1 and 3 years).

Outputs: history/climatology/features_by_era.csv, outcomes_by_era.csv, event_rates_by_era.csv, README.md
Run: python3 -I history/tools/climatology.py
"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from analogs import GROUPS, forward  # noqa: E402
from wf import build_targets  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "history", "climatology")
BASE = [f for g in GROUPS.values() for f in g]
TARGETS = ["crisis_3y", "dd30_3y", "credit_contraction_3y", "unemp_spike_3y", "gdp_fall_3y", "stress3_3y"]
OUTCOMES = ["rgdp_pc_1y", "rgdp_pc_3y", "req_1y", "req_3y", "rhp_3y", "dltrate_1y", "dltrate_3y", "dunemp_3y", "dloans_gdp_3y"]
Q = [10, 25, 50, 75, 90]
MIN_N = 30


def era_bounds():
    p = os.path.join(ROOT, "history", "analogs", "topology_test.json")
    breaks = json.load(open(p))["breaks"] if os.path.exists(p) else [1914, 1932, 1940, 1973]
    breaks = sorted(set(breaks) | {1999})
    bounds = [1870] + breaks + [2021]
    return [(a, b - 1) for a, b in zip(bounds[:-1], bounds[1:])]


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(ROOT, "history", "jst", "features.csv"))))
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    isos = [r["iso"] for r in rows]; years = [int(r["year"]) for r in rows]
    T = build_targets(jst, isos, years)
    eras = era_bounds()
    regime = [(jst.get((i, y), {}).get("peg_type") or "NA") for i, y in zip(isos, years)]

    def cell_rows(a, b, reg):
        return [k for k, (i, y) in enumerate(zip(isos, years)) if a <= y <= b and (reg == "all" or regime[k] == reg)]

    feat_rows, out_rows, ev_rows = [], [], []
    fwd_cache = {}
    for a, b in eras:
        for reg in ("all", "BASE", "PEG", "FLOAT"):
            idx = cell_rows(a, b, reg)
            if len(idx) < MIN_N:
                continue
            era = f"{a}-{b}"
            for f in BASE:
                v = np.array([float(rows[k][f]) for k in idx if rows[k].get(f) not in ("", None)])
                if len(v) >= MIN_N:
                    feat_rows.append({"era": era, "regime": reg, "feature": f, "n": len(v),
                                      **{f"p{q}": f"{np.percentile(v, q):.6g}" for q in Q}})
            for t in TARGETS:
                v = T[t][idx]; v = v[~np.isnan(v)]
                if len(v) >= MIN_N:
                    ev_rows.append({"era": era, "regime": reg, "target": t, "n": len(v), "rate": f"{v.mean():.4f}"})
            for o in OUTCOMES:
                vals = []
                for k in idx:
                    key = (isos[k], years[k])
                    if key not in fwd_cache:
                        fwd_cache[key] = forward(jst, isos[k], years[k])
                    x = fwd_cache[key].get(o)
                    if x is not None and not (isinstance(x, float) and np.isnan(x)):
                        vals.append(float(x))
                if len(vals) >= MIN_N:
                    v = np.array(vals)
                    out_rows.append({"era": era, "regime": reg, "outcome": o, "n": len(v),
                                     **{f"p{q}": f"{np.percentile(v, q):.6g}" for q in Q}})
    for name, rr, fields in (("features_by_era.csv", feat_rows, ["era", "regime", "feature", "n"] + [f"p{q}" for q in Q]),
                             ("outcomes_by_era.csv", out_rows, ["era", "regime", "outcome", "n"] + [f"p{q}" for q in Q]),
                             ("event_rates_by_era.csv", ev_rows, ["era", "regime", "target", "n", "rate"])):
        with open(os.path.join(OUT, name), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rr)
    # README with the headline tables (all regimes)
    L = ["# Climatology", "",
         "The unconditional distributions the forecast relaxes toward at long lead times, indexed by the network's measured "
         "topology eras (`tools/topology.py`: breaks in 1914, 1932, 1940 and 1973, plus 1999 for the euro bloc) and by regime "
         "(`peg_type`). Built by `tools/climatology.py` from `jst/features.csv` and the forward outcomes of `tools/analogs.py`; "
         "cells with fewer than 30 country-years are left out. `features_by_era.csv` holds the five percentiles of every base "
         "feature per cell, `outcomes_by_era.csv` the forward outcomes, `event_rates_by_era.csv` the event base rates.", "",
         "## Event base rates by era (all regimes)", "",
         "| era | n | " + " | ".join(TARGETS) + " |", "|---|---|" + "---|" * len(TARGETS)]
    for a, b in eras:
        era = f"{a}-{b}"
        cells = {r["target"]: r for r in ev_rows if r["era"] == era and r["regime"] == "all"}
        if cells:
            n = max(int(r["n"]) for r in cells.values())
            L.append(f"| {era} | {n} | " + " | ".join(f"{float(cells[t]['rate']):.0%}" if t in cells else "—" for t in TARGETS) + " |")
    L += ["", "## Median state by era (all regimes): the climate the analogs are measured against", "",
          "| era | " + " | ".join(["loans/GDP", "Δ3y loans/GDP", "debt/GDP", "long rate", "term spread", "real rate", "inflation", "rGDP/cap growth", "unemp", "I/Y", "CA/GDP", "div. yield", "real eq. 3y", "real hp 3y"]) + " |",
          "|---|" + "---|" * 14]
    show = ["loans_gdp", "d3_loans_gdp", "debt_gdp", "ltrate", "term_spread", "real_ltrate_expost", "cpi_infl", "rgdp_pc_growth", "unemp", "iy", "ca_gdp", "eq_dp", "real_eq_capgain_3y", "real_hp_growth_3y"]
    for a, b in eras:
        era = f"{a}-{b}"
        med = {r["feature"]: float(r["p50"]) for r in feat_rows if r["era"] == era and r["regime"] == "all"}
        if med:
            def fmt(f):
                if f not in med:
                    return "—"
                v = med[f]
                return f"{v:.1%}" if f in ("loans_gdp", "d3_loans_gdp", "debt_gdp", "cpi_infl", "rgdp_pc_growth", "iy", "ca_gdp", "eq_dp", "real_eq_capgain_3y", "real_hp_growth_3y") else f"{v:.1f}"
            L.append(f"| {era} | " + " | ".join(fmt(f) for f in show) + " |")
    L += ["", "## Forward outcomes by era (all regimes): p25 / p50 / p75", "",
          "| era | rGDP/cap 3y | real equity 3y | real houses 3y | Δ long rate 3y (pp) | Δ unemp 3y (pp) | Δ loans/GDP 3y (pp) |", "|---|---|---|---|---|---|---|"]
    for a, b in eras:
        era = f"{a}-{b}"
        oc = {r["outcome"]: r for r in out_rows if r["era"] == era and r["regime"] == "all"}
        if oc:
            def trip(o, pct=True):  # forward() reports growth outcomes in percent and the rate/loan changes in points already
                if o not in oc:
                    return "—"
                r = oc[o]
                return " / ".join(f"{float(r[k]):+.1f}{'%' if pct else ''}" for k in ("p25", "p50", "p75"))
            L.append(f"| {era} | {trip('rgdp_pc_3y')} | {trip('req_3y')} | {trip('rhp_3y')} | {trip('dltrate_3y', False)} | {trip('dunemp_3y', False)} | {trip('dloans_gdp_3y', False)} |")
    L += ["", "Reading: the same state vector means different things in different arrangements — a 60% loans/GDP ratio was a "
          "boom in 1900 and the median in 2000 — which is why the analog retrieval standardizes within an expanding window and "
          "why the cone's far end should relax toward the era's climate rather than the pooled one. The eras mark whole "
          "institutional settings (wars, capital controls, the euro), not causes.", ""]
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(L))
    print(f"features {len(feat_rows)} rows, outcomes {len(out_rows)} rows, event rates {len(ev_rows)} rows -> {OUT}")
    print("\n".join(L[8:40]))


if __name__ == "__main__":
    main()
