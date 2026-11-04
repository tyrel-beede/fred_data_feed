#!/usr/bin/env python3
"""Does the analog cone carry information? A leave-one-episode-out backtest on the JST panel.

For every country-year with enough feature coverage, find its k nearest analogs (excluding the same country within
+-5 years, i.e. its own episode), take the analogs' forward outcomes as the prediction, and score them against what
actually followed that country-year:
  - crisis within 1-3 years: AUC of the analog crisis share as a classifier, vs 0.5 for no skill; plus the realized
    crisis rate in the top decile of analog shares vs the base rate
  - continuous outcomes (real equity 3y, real GDP per capita 3y, long-rate change 3y): rank correlation between the
    analog median and the realized value, and the share of realized values inside the analogs' p25-p75 band vs the
    share inside the climatology's p25-p75 band (a calibrated cone covers ~50%)
Run per feature group as well as for all groups, so the groups' skill can be compared rather than assumed.

Usage: python3 -I history/tools/analog_backtest.py [--k 15] [--min-coverage 0.8] [--from-year 1880]
Writes history/analogs/backtest.md and backtest.json.
"""
import argparse, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_features, load_jst  # noqa: E402
from analogs import GROUPS, forward  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))


def auc(scores, labels):
    pairs = [(s, l) for s, l in zip(scores, labels) if s is not None and l is not None]
    pos = [s for s, l in pairs if l == 1]
    neg = [s for s, l in pairs if l == 0]
    if not pos or not neg:
        return None
    # rank-based AUC (ties count half)
    allv = sorted(pairs, key=lambda t: t[0])
    ranks = {}
    i = 0
    while i < len(allv):
        j = i
        while j < len(allv) and allv[j][0] == allv[i][0]:
            j += 1
        r = (i + j + 1) / 2.0
        for k in range(i, j):
            ranks[k] = r
        i = j
    rank_pos = sum(ranks[k] for k, (s, l) in enumerate(allv) if l == 1)
    return (rank_pos - len(pos) * (len(pos) + 1) / 2.0) / (len(pos) * len(neg))


def spearman(x, y):
    pairs = [(a, b) for a, b in zip(x, y) if a is not None and b is not None]
    if len(pairs) < 10:
        return None, 0
    xs = np.array([p[0] for p in pairs]); ys = np.array([p[1] for p in pairs])
    rx = xs.argsort().argsort().astype(float); ry = ys.argsort().argsort().astype(float)
    return float(np.corrcoef(rx, ry)[0, 1]), len(pairs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=15); ap.add_argument("--min-coverage", type=float, default=0.8)
    ap.add_argument("--from-year", type=int, default=1880)
    a = ap.parse_args()
    rows = [r for r in load_features() if r["year"] >= a.from_year]
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    outs = [forward(jst, r["iso"], r["year"]) for r in rows]
    isos = np.array([r["iso"] for r in rows]); years = np.array([r["year"] for r in rows])
    report = {"k": a.k, "min_coverage": a.min_coverage, "from_year": a.from_year, "groups": {}}
    sets = {"all": [f for g in GROUPS.values() for f in g]}
    sets.update(GROUPS)
    for gname, feats in sets.items():
        X = np.array([[np.nan if r.get(f) is None else r[f] for f in feats] for r in rows], dtype=float)
        # robust scale
        med = np.nanmedian(X, axis=0); mad = np.nanmedian(np.abs(X - med), axis=0) * 1.4826
        mad[mad == 0] = np.nanstd(X, axis=0)[mad == 0]; mad[mad == 0] = 1.0
        Z = (X - med) / mad
        cov = (~np.isnan(Z)).sum(axis=1) / len(feats)
        ok = cov >= a.min_coverage
        idx = np.where(ok)[0]
        preds = {"crisis": [], "req_3y": [], "rgdp_pc_3y": [], "dltrate_3y": []}
        bands = {"req_3y": [], "rgdp_pc_3y": [], "dltrate_3y": []}
        labels = {"crisis": [], "req_3y": [], "rgdp_pc_3y": [], "dltrate_3y": []}
        for qi in idx:
            zq = Z[qi]
            both = ~np.isnan(zq) & ~np.isnan(Z)  # per candidate, features both have
            n_both = both.sum(axis=1)
            d2 = np.where(both, (Z - zq) ** 2, 0.0).sum(axis=1)
            dist = np.sqrt(d2 / np.maximum(n_both, 1))
            dist[(n_both / len(feats)) < a.min_coverage] = np.inf
            same = (isos == isos[qi]) & (np.abs(years - years[qi]) <= 5)
            dist[same] = np.inf
            order = np.argsort(dist)
            picked, taken = [], []
            for ci in order:
                if not np.isfinite(dist[ci]):
                    break
                if any(isos[ci] == isos[t] and abs(years[ci] - years[t]) <= 5 for t in taken):
                    continue
                picked.append(ci); taken.append(ci)
                if len(picked) >= a.k:
                    break
            if len(picked) < a.k // 2:
                continue
            ao = [outs[ci] for ci in picked]
            cs = [o["crisis_1_3y"] for o in ao if o["crisis_1_3y"] is not None]
            preds["crisis"].append(sum(cs) / len(cs) if cs else None); labels["crisis"].append(outs[qi]["crisis_1_3y"])
            for key in ("req_3y", "rgdp_pc_3y", "dltrate_3y"):
                vs = sorted(o[key] for o in ao if o[key] is not None)
                if len(vs) >= 5:
                    preds[key].append(float(np.median(vs)))
                    bands[key].append((float(np.percentile(vs, 25)), float(np.percentile(vs, 75))))
                else:
                    preds[key].append(None); bands[key].append(None)
                labels[key].append(outs[qi][key])
        g = {"n_queries": int(len(preds["crisis"]))}
        g["crisis_auc"] = auc(preds["crisis"], labels["crisis"])
        pl = [(p, l) for p, l in zip(preds["crisis"], labels["crisis"]) if p is not None and l is not None]
        if pl:
            base = sum(l for _, l in pl) / len(pl)
            top = sorted(pl, key=lambda t: -t[0])[: max(1, len(pl) // 10)]
            g["crisis_base_rate"] = base; g["crisis_rate_top_decile"] = sum(l for _, l in top) / len(top)
        clim = {key: [o[key] for o in outs if o[key] is not None] for key in ("req_3y", "rgdp_pc_3y", "dltrate_3y")}
        for key in ("req_3y", "rgdp_pc_3y", "dltrate_3y"):
            rho, n = spearman(preds[key], labels[key])
            inside = [1 if b[0] <= l <= b[1] else 0 for b, l in zip(bands[key], labels[key]) if b is not None and l is not None]
            c25, c75 = np.percentile(clim[key], 25), np.percentile(clim[key], 75)
            cin = [1 if c25 <= l <= c75 else 0 for l in labels[key] if l is not None]
            g[key] = {"spearman": rho, "n": n, "coverage_analog_band": (sum(inside) / len(inside)) if inside else None,
                      "coverage_climatology_band": (sum(cin) / len(cin)) if cin else None,
                      "analog_band_width_median": float(np.median([b[1] - b[0] for b in bands[key] if b])) if any(bands[key]) else None,
                      "climatology_band_width": float(c75 - c25)}
        report["groups"][gname] = g
        print(gname, json.dumps(g)[:300])
    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    json.dump(report, open(os.path.join(ROOT, "history", "analogs", "backtest.json"), "w"), indent=1)
    L = ["# Analog cone backtest", "",
         f"Leave-one-episode-out over the panel from {a.from_year} (k={a.k}, own country within ±5 years excluded, "
         f"coverage ≥ {a.min_coverage:.0%}). Skill is measured against climatology: AUC 0.5 and band coverage equal to "
         f"the climatology's mean no information.", "",
         "| feature set | queries | crisis AUC | crisis rate: top decile vs base | real equity 3y: ρ, band cover (analog / clim), band width (analog / clim) | rGDP/cap 3y: ρ, cover, width | Δ long rate 3y: ρ, cover, width |",
         "|---|---|---|---|---|---|---|"]
    for gname, g in report["groups"].items():
        def f(key):
            x = g[key]
            return (f"ρ {x['spearman']:+.2f} (n={x['n']}), {x['coverage_analog_band']:.0%} / {x['coverage_climatology_band']:.0%}, "
                    f"{x['analog_band_width_median']:.1f} / {x['climatology_band_width']:.1f}") if x.get("spearman") is not None else "—"
        L.append(f"| {gname} | {g['n_queries']} | {g['crisis_auc']:.2f} | {g.get('crisis_rate_top_decile', 0):.0%} vs {g.get('crisis_base_rate', 0):.0%} | "
                 f"{f('req_3y')} | {f('rgdp_pc_3y')} | {f('dltrate_3y')} |")
    L += ["", "Reading: a crisis AUC above ~0.6 with a top-decile rate several times the base rate means the state vector "
          "sorts country-years by what followed; a band coverage near 50% with a narrower band than the climatology's is a "
          "cone that is both calibrated and informative. The comparison across feature sets is the point: it says which "
          "parts of the state carry information at this horizon, instead of assuming it.", ""]
    open(os.path.join(ROOT, "history", "analogs", "backtest.md"), "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
