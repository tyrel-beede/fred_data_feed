#!/usr/bin/env python3
"""Lead-lag: does the path into T carry information the point at T does not?

Two measurements, both walk-forward where a forecast is involved:

1. Trajectory analogs. Match on the state's path rather than its point: the base vector at T, at T and T-1, at T, T-1
   and T-2, and the point plus its 1- and 2-year differences. Walk-forward AUC on the measured 3-year targets and the
   crisis label, same harness as test 2. If the path helps, the record stores dependence across time before T.

2. Lead profiles. For each base feature x and lag k = 0..4, the AUC of x(T-k) alone as a predictor of each target
   over T+1..T+3 (oriented so the better direction scores > 0.5). The profile over k says how far ahead each feature
   leads the event - the measured lag structure that mile markers can be registered against. Reported with the sign
   agreement between the pre-1950 and post-1950 halves of the panel, so a lag that only works in one era is visible.

Usage: python3 -I history/tools/lag_test.py ; writes history/analogs/lag_test.md and lag_test.json
"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from analogs import GROUPS  # noqa: E402
from wf import walk_forward_neighbors, predict, auc, top_decile, build_targets  # noqa: E402
from analog_test2 import NETWORK  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
BASE = [f for g in GROUPS.values() for f in g]
TARGETS = ["crisis_3y", "dd30_3y", "credit_contraction_3y", "gdp_fall_3y", "unemp_spike_3y"]


def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "history", "jst", "features2.csv"))))
    isos = [r["iso"] for r in rows]; years = [int(r["year"]) for r in rows]
    idx = {(i, y): n for n, (i, y) in enumerate(zip(isos, years))}
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    T = build_targets(jst, isos, years)

    def col(name, lag=0):
        out = np.full(len(rows), np.nan)
        for n, (i, y) in enumerate(zip(isos, years)):
            j = idx.get((i, y - lag))
            if j is not None and rows[j][name] not in ("", None):
                out[n] = float(rows[j][name])
        return out

    def mat(names, lags):
        return np.column_stack([col(nm, lg) for lg in lags for nm in names])

    rep = {"trajectory": {}, "lead_profiles": {}}
    designs = {
        "point T (20)": (BASE, [0]),
        "path T, T-1 (40)": (BASE, [0, 1]),
        "path T, T-1, T-2 (60)": (BASE, [0, 1, 2]),
        "point + network (30)": (BASE + NETWORK, [0]),
        "path T, T-1 + network at T (50)": None,  # built below
    }
    X_path_net = np.column_stack([mat(BASE, [0, 1]), mat(NETWORK, [0])])
    for name, spec in designs.items():
        X = X_path_net if spec is None else mat(*spec)
        nb = walk_forward_neighbors(X, isos, years, horizon=3, k=15, min_cov=0.6, from_year=1880)
        res = {}
        for t in TARGETS:
            p = predict(nb, T[t]); A, npos, nneg = auc(p, T[t]); td, base = top_decile(p, T[t])
            res[t] = {"auc": A, "top_decile": td, "base": base, "n_pos": npos, "n_neg": nneg}
        rep["trajectory"][name] = res
        print(name, {t: round(v["auc"], 3) for t, v in res.items() if v["auc"]})
    # differences design: point + 1y and 2y differences
    X = np.column_stack([mat(BASE, [0]), mat(BASE, [0]) - mat(BASE, [1]), mat(BASE, [0]) - mat(BASE, [2])])
    nb = walk_forward_neighbors(X, isos, years, horizon=3, k=15, min_cov=0.6, from_year=1880)
    res = {}
    for t in TARGETS:
        p = predict(nb, T[t]); A, npos, nneg = auc(p, T[t]); td, base = top_decile(p, T[t])
        res[t] = {"auc": A, "top_decile": td, "base": base, "n_pos": npos, "n_neg": nneg}
    rep["trajectory"]["point + 1y and 2y differences (60)"] = res
    print("differences", {t: round(v["auc"], 3) for t, v in res.items() if v["auc"]})

    # selected leads: only the lagged features whose lead profile is strong and era-consistent
    LEADS = [("loans_gdp", 3), ("mort_gdp", 3), ("real_eq_capgain_3y", 1), ("rgdp_pc_growth", 1), ("r_minus_g", 1)]
    X = np.column_stack([mat(BASE + NETWORK, [0])] + [col(f, k) for f, k in LEADS])
    nb = walk_forward_neighbors(X, isos, years, horizon=3, k=15, min_cov=0.6, from_year=1880)
    res = {}
    for t in TARGETS:
        p = predict(nb, T[t]); A, npos, nneg = auc(p, T[t]); td, base = top_decile(p, T[t])
        res[t] = {"auc": A, "top_decile": td, "base": base, "n_pos": npos, "n_neg": nneg}
    rep["trajectory"]["point + network + 5 selected leads (35)"] = res
    print("selected leads", {t: round(v["auc"], 3) for t, v in res.items() if v["auc"]})

    # mile markers: conditional event rates as markers arrive in sequence (descriptive, with era split)
    yrs = np.array(years)
    def tercile_flag(name, lag, top=True):
        x = col(name, lag); q = np.nanpercentile(x, 67 if top else 33)
        return (x >= q) if top else (x <= q)
    # physical rung: the real oil price change at T (the shadow price of the energy constraint), if the physical layer is built
    oil = {}
    pp = os.path.join(ROOT, "history", "physical", "physical_features.csv")
    if os.path.exists(pp):
        for r in csv.DictReader(open(pp)):
            if r.get("oil_real_change_1y"):
                oil[(r["iso"], int(r["year"]))] = float(r["oil_real_change_1y"])
    oil_up = np.array([oil.get((i, y), np.nan) >= 0.25 if (i, y) in oil else np.nan for i, y in zip(isos, years)], dtype=float)
    ladders = {
        "credit_contraction_3y": [("loans/GDP high (top tercile) at T-3", tercile_flag("loans_gdp", 3, True)),
                                  ("real equity 3y gain <= 0 at T-1", col("real_eq_capgain_3y", 1) <= 0),
                                  ("real house prices 3y growth <= 0 at T", col("real_hp_growth_3y", 0) <= 0)]
                                 + ([("real oil price up >= 25% over the year at T", oil_up == 1.0)] if oil else []),
        "dd30_3y": [("dividend yield low (bottom tercile) at T", tercile_flag("eq_dp", 0, False)),
                    ("r - g low (bottom tercile) at T", tercile_flag("r_minus_g", 0, False)),
                    ("inflation high (top tercile) at T", tercile_flag("cpi_infl", 0, True))]
                   + ([("real oil price up >= 25% over the year at T", oil_up == 1.0)] if oil else []),
        "gdp_fall_3y": ([("real oil price up >= 25% over the year at T", oil_up == 1.0),
                         ("loans/GDP high (top tercile) at T-3", tercile_flag("loans_gdp", 3, True)),
                         ("real house prices 3y growth <= 0 at T", col("real_hp_growth_3y", 0) <= 0)] if oil else []),
    }
    rep["mile_markers"] = {}
    for t, steps in ladders.items():
        lab = T[t]; cond = ~np.isnan(lab)
        out = [{"stage": "unconditional", "n": int(cond.sum()), "rate": float(np.nanmean(lab[cond]))}]
        for name, flag in steps:
            cond = cond & np.nan_to_num(flag, nan=False)
            if cond.sum() > 0:
                pre = cond & (yrs < 1950); post = cond & (yrs >= 1950)
                out.append({"stage": name, "n": int(cond.sum()), "rate": float(np.nanmean(lab[cond])),
                            "rate_pre1950": float(np.nanmean(lab[pre])) if pre.sum() else None,
                            "rate_post1950": float(np.nanmean(lab[post])) if post.sum() else None})
        rep["mile_markers"][t] = out
        print("ladder", t, [(o["stage"][:28], o["n"], round(o["rate"], 2)) for o in out])

    # lead profiles: single feature at lag k vs target
    yrs = np.array(years)
    for t in ("dd30_3y", "credit_contraction_3y", "crisis_3y"):
        prof = {}
        for f in BASE:
            row = {}
            for k in range(0, 5):
                x = col(f, k)
                lab = T[t]
                m = ~np.isnan(x) & ~np.isnan(lab)
                A, npos, nneg = auc(list(x[m]), list(lab[m]))
                if A is None:
                    continue
                # orient: report max(A, 1-A) and the direction
                direction = "high" if A >= 0.5 else "low"
                A_or = max(A, 1 - A)
                # era agreement
                e1 = m & (yrs < 1950); e2 = m & (yrs >= 1950)
                A1 = auc(list(x[e1]), list(lab[e1]))[0]; A2 = auc(list(x[e2]), list(lab[e2]))[0]
                agree = (A1 is not None and A2 is not None and ((A1 >= 0.5) == (A2 >= 0.5)))
                row[k] = {"auc": A_or, "direction": direction, "pre1950": A1, "post1950": A2, "eras_agree": agree, "n_pos": npos}
            prof[f] = row
        rep["lead_profiles"][t] = prof

    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    json.dump(rep, open(os.path.join(ROOT, "history", "analogs", "lag_test.json"), "w"), indent=1)
    L = ["# Lead-lag: the path into T versus the point at T", "",
         "Walk-forward k=15 nearest-neighbour harness (expanding-window scaling, own episode excluded, one episode per "
         "country), 3-year targets. AUC 0.5 = no skill.", "",
         "## 1. Trajectory analogs", "", "| design (features) | " + " | ".join(TARGETS) + " |", "|---|" + "---|" * len(TARGETS)]
    for name, res in rep["trajectory"].items():
        L.append(f"| {name} | " + " | ".join(f"{v['auc']:.2f} (top {v['top_decile']:.0%} vs {v['base']:.0%})" if v["auc"] else "—" for v in res.values()) + " |")
    L += ["", "## 2. Lead profiles: single feature at lag k (years before T) as a predictor of the event in T+1..T+3", "",
          "AUC oriented (max of AUC and 1−AUC; 'high'/'low' says which direction of the feature predicts the event); "
          "✓ = the pre-1950 and post-1950 halves agree on the direction, ✗ = they disagree. Features sorted by their best lag.", ""]
    for t, prof in rep["lead_profiles"].items():
        L += [f"### {t}", "", "| feature | k=0 | k=1 | k=2 | k=3 | k=4 | best lag |", "|---|---|---|---|---|---|---|"]
        order = sorted(prof.items(), key=lambda kv: -max((v["auc"] for v in kv[1].values()), default=0))
        for f, row in order:
            cells = []
            for k in range(5):
                v = row.get(k)
                cells.append("—" if v is None else f"{v['auc']:.2f} {v['direction'][0]}{'✓' if v['eras_agree'] else '✗'}")
            best = max(row.items(), key=lambda kv: kv[1]["auc"]) if row else None
            L.append(f"| {f} | " + " | ".join(cells) + f" | {best[0] if best else '—'} |")
        L.append("")
    L += ["## 3. Mile markers: event rate as markers arrive in sequence", "",
          "Conditional frequency of the event given each marker in turn (all markers computable at T; terciles over the "
          "panel; descriptive, so in-sample, with the pre/post-1950 rates beside each stage).", ""]
    for t, out in rep["mile_markers"].items():
        L += [f"### {t}", "", "| stage | n | event rate | pre-1950 | post-1950 |", "|---|---|---|---|---|"]
        for o in out:
            L.append(f"| {o['stage']} | {o['n']} | {o['rate']:.0%} | {('%.0f%%' % (100 * o['rate_pre1950'])) if o.get('rate_pre1950') is not None else '—'} | "
                     f"{('%.0f%%' % (100 * o['rate_post1950'])) if o.get('rate_post1950') is not None else '—'} |")
        L.append("")
    L += ["Reading the profiles: a feature whose AUC is highest at k=0 is coincident information; one whose AUC stays high "
          "or peaks at k=1..3 leads the event by that many years, which is the lag a mile marker can be registered at. "
          "A ✗ means the relationship flipped sign between eras and should not be trusted as a 'known' lag.", ""]
    open(os.path.join(ROOT, "history", "analogs", "lag_test.md"), "w").write("\n".join(L))
    print("\n".join(L[:12]))


if __name__ == "__main__":
    main()
