#!/usr/bin/env python3
"""The network's topology as a feature family: nodes coming and going from subnets, measured from the JST exchange-rate
regime columns (peg, peg_type BASE/PEG/FLOAT, peg_base GBR/USA/DEU/HYBRID), nothing narrative-coded.

A subnet is the set of countries sharing a base currency at t; the topology is the whole arrangement. Everything is
computable at t from the panel's regime columns for years <= t.

Per country-year (history/jst/topology.csv):
  in_peg               1 if pegged (JST peg flag)
  is_base              1 if the country is a bloc's base (peg_type BASE)
  bloc_size            number of other countries with the same base at t (0 if floating, no base, or HYBRID)
  bloc_share           bloc_size over the number of countries with a regime recorded at t
  bloc_tenure          years in the current (peg_type, peg_base) state, counting t
  regime_change_3y     1 if the country's (peg_type, peg_base) state changed in t-2..t (the node moved subnet)
  bloc_churn_3y        members who joined or left the country's current bloc in t-2..t
  base_changed_5y      1 if the country's base changed within t-4..t (GBR -> USA -> DEU)
  n_blocs              number of bases with at least two members at t (global: fragmentation)
  panel_peg_share      share of countries pegged at t (global)
  panel_changes_3y     number of countries whose state changed in t-2..t (global churn)
  years_since_break    years since the last topology break, a break being a year in which at least a third of the
                       countries with a regime recorded changed state (measured, not dated by hand)

Tests (history/analogs/topology_test.md / .json):
  1. climatology by topology: walk-forward conditional event rate by regime class as the forecast, against the pooled
     rate (which varies only with t); the AUC above 0.5 is what the topology alone carries
  2. event rates in the three years after a topology break against all other years
  3. pooled single-feature AUCs (descriptive)
Run: python3 -I history/tools/topology.py
"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from wf import build_targets, auc  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
TARGETS = ["dd30_3y", "credit_contraction_3y", "gdp_fall_3y", "unemp_spike_3y", "crisis_3y"]
COLS = ["in_peg", "is_base", "bloc_size", "bloc_share", "bloc_tenure", "regime_change_3y", "bloc_churn_3y", "base_changed_5y",
        "n_blocs", "panel_peg_share", "panel_changes_3y", "years_since_break"]


def state(r):
    t, b = (r.get("peg_type") or ""), (r.get("peg_base") or "")
    if t == "" or b == "":
        return None
    return (t, b)


def main():
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    isos = sorted({k[0] for k in jst}); years = sorted({k[1] for k in jst})
    S = {k: state(r) for k, r in jst.items()}
    # per year: members per base, states, changes
    members = {}; recorded = {}; changes = {}
    for y in years:
        m = {}
        rec = [i for i in isos if S.get((i, y)) is not None]
        for i in rec:
            t, b = S[(i, y)]
            if t == "PEG" and b not in ("NA", "HYBRID", ""):
                m.setdefault(b, set()).add(i)
        members[y] = m; recorded[y] = rec
        changes[y] = [i for i in rec if S.get((i, y - 1)) is not None and S[(i, y - 1)] != S[(i, y)]]
    breaks = [y for y in years if recorded[y] and len(changes[y]) >= len(recorded[y]) / 3.0]
    rows = {}
    for i in isos:
        tenure = 0; prev = None
        for y in years:
            st = S.get((i, y))
            if st is None:
                rows[(i, y)] = {c: np.nan for c in COLS}; prev = None; tenure = 0; continue
            tenure = tenure + 1 if st == prev else 1
            prev = st
            t, b = st
            bloc = members[y].get(b, set()) if t in ("PEG", "BASE") else set()
            others = bloc - {i}
            if t == "BASE":  # the base's bloc is everyone pegged to it
                others = members[y].get(i, set())
            nrec = len(recorded[y])
            ch3 = sum(1 for yy in (y, y - 1, y - 2) if i in changes.get(yy, []))
            # bloc churn: members of my current bloc (by base) who joined or left in t-2..t
            base_key = i if t == "BASE" else b
            churn = 0
            for yy in (y, y - 1, y - 2):
                if yy - 1 in members:
                    churn += len(members[yy].get(base_key, set()) ^ members[yy - 1].get(base_key, set()))
            bases = [S[(i, yy)][1] for yy in range(y - 4, y + 1) if S.get((i, yy)) is not None]
            base_chg = 1.0 if len(set(bases)) > 1 and len(bases) >= 2 else 0.0
            n_blocs = sum(1 for b_, mm in members[y].items() if len(mm) >= 2)
            peg_share = sum(1 for j in recorded[y] if S[(j, y)][0] == "PEG") / nrec if nrec else np.nan
            pch3 = sum(len(changes.get(yy, [])) for yy in (y, y - 1, y - 2))
            past_breaks = [bk for bk in breaks if bk <= y]
            ysb = (y - past_breaks[-1]) if past_breaks else np.nan
            rows[(i, y)] = {"in_peg": float(jst[(i, y)].get("peg") or 0), "is_base": 1.0 if t == "BASE" else 0.0,
                            "bloc_size": float(len(others)), "bloc_share": len(others) / nrec if nrec else np.nan,
                            "bloc_tenure": float(tenure), "regime_change_3y": 1.0 if ch3 else 0.0, "bloc_churn_3y": float(churn),
                            "base_changed_5y": base_chg, "n_blocs": float(n_blocs), "panel_peg_share": peg_share,
                            "panel_changes_3y": float(pch3), "years_since_break": float(ysb) if not np.isnan(ysb) else np.nan}
    os.makedirs(os.path.join(ROOT, "history", "jst"), exist_ok=True)
    with open(os.path.join(ROOT, "history", "jst", "topology.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["iso", "year"] + COLS)
        for i in isos:
            for y in years:
                w.writerow([i, y] + ["" if (isinstance(v, float) and np.isnan(v)) else f"{v:g}" for v in (rows[(i, y)][c] for c in COLS)])
    print("topology breaks (>= 1/3 of recorded countries changed state):", [(y, len(changes[y]), len(recorded[y])) for y in breaks])

    # ------------------------------------------------------------------ tests on the features2 row set
    feats = list(csv.DictReader(open(os.path.join(ROOT, "history", "jst", "features2.csv"))))
    fi = [r["iso"] for r in feats]; fy = [int(r["year"]) for r in feats]
    T = build_targets(jst, fi, fy)
    X = {c: np.array([rows[(i, y)][c] for i, y in zip(fi, fy)], dtype=float) for c in COLS}
    yrs = np.array(fy)
    rep = {"breaks": breaks, "climatology": {}, "after_break": {}, "single_feature": {}}

    # 1. climatology by topology, walk-forward (training rows: outcome window closed before t)
    def cls_peg(n):
        st = S.get((fi[n], fy[n])); return None if st is None else st[0]
    def cls_full(n):
        st = S.get((fi[n], fy[n]))
        if st is None:
            return None
        bs = X["bloc_size"][n]; b = "solo" if bs == 0 else ("small" if bs <= 5 else "large")
        return (st[0], b, int(X["regime_change_3y"][n]))
    def cls_year(n):
        return "all"
    schemes = {"pooled (varies only with t)": cls_year, "by peg_type": cls_peg, "by peg_type x bloc size x moved recently": cls_full}
    for t in TARGETS:
        lab = T[t]; res = {}
        for name, fn in schemes.items():
            cl = [fn(n) for n in range(len(fi))]
            pred = [None] * len(fi)
            for tq in sorted(set(fy)):
                if tq < 1900:
                    continue
                tr = np.where((yrs + 3 < tq) & ~np.isnan(lab))[0]
                if len(tr) < 100:
                    continue
                rates = {}
                for n in tr:
                    rates.setdefault(cl[n], []).append(lab[n])
                rates = {k: float(np.mean(v)) for k, v in rates.items() if len(v) >= 20}
                for n in np.where(yrs == tq)[0]:
                    if cl[n] in rates:
                        pred[n] = rates[cl[n]]
            A, npos, nneg = auc(pred, lab)
            res[name] = {"auc": A, "n_pos": npos, "n_neg": nneg}
        rep["climatology"][t] = res
        print("climatology", t, {k: (round(v["auc"], 3) if v["auc"] else None) for k, v in res.items()})

    # 2. event rates in the three years after a break vs other years
    after = np.zeros(len(fi), dtype=bool)
    for bk in breaks:
        after |= (yrs >= bk) & (yrs <= bk + 2)
    for t in TARGETS:
        lab = T[t]; ok = ~np.isnan(lab)
        a, o = lab[ok & after], lab[ok & ~after]
        rep["after_break"][t] = {"rate_after": float(a.mean()) if len(a) else None, "n_after": int(len(a)),
                                 "rate_other": float(o.mean()) if len(o) else None, "n_other": int(len(o))}
    print("after break", {t: (round(v["rate_after"], 3), v["n_after"], round(v["rate_other"], 3)) for t, v in rep["after_break"].items()})

    # 4. the climate of each topology era: event base rates between measured breaks (descriptive)
    bounds = [1870] + breaks + [2021]
    rep["era_rates"] = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        m = (yrs >= a) & (yrs < b)
        rec = {"era": f"{a}-{b - 1}", "rows": int(m.sum())}
        for t in TARGETS:
            v = T[t][m]; v = v[~np.isnan(v)]
            rec[t] = float(v.mean()) if len(v) else None
        rep["era_rates"].append(rec)

    # 3. pooled single-feature AUCs (descriptive)
    for c in COLS:
        rep["single_feature"][c] = {}
        for t in TARGETS:
            A, _, _ = auc([None if np.isnan(v) else float(v) for v in X[c]], T[t])
            rep["single_feature"][c][t] = A

    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    json.dump(rep, open(os.path.join(ROOT, "history", "analogs", "topology_test.json"), "w"), indent=1)
    L = ["# Topology test — nodes coming and going from subnets", "",
         "Subnets are read from the JST regime columns (peg_type, peg_base): the countries sharing a base currency at t. "
         "Features in `jst/topology.csv` (built by `tools/topology.py`); all computable at t.", "",
         "**Topology breaks** (years in which at least a third of the countries with a regime recorded changed state): " +
         ", ".join(f"{y} ({len(changes[y])} of {len(recorded[y])})" for y in breaks) + ".", "",
         "## 1. Climatology by topology (walk-forward conditional event rate as the forecast)", "",
         "| target | " + " | ".join(schemes) + " |", "|---|" + "---|" * len(schemes)]
    for t, res in rep["climatology"].items():
        L.append(f"| {t} | " + " | ".join(f"{v['auc']:.2f}" if v["auc"] else "—" for v in res.values()) + " |")
    L += ["", "The pooled column is the no-skill reference (its rate changes only with the query year). The difference is what "
          "knowing the node's place in the topology is worth before any state variable is read.", "",
          "## 2. Event rates in the three years after a topology break", "", "| target | after a break (n) | other years (n) |", "|---|---|---|"]
    for t, v in rep["after_break"].items():
        L.append(f"| {t} | {v['rate_after']:.0%} ({v['n_after']}) | {v['rate_other']:.0%} ({v['n_other']}) |")
    L += ["", "## 3. The climate of each topology era (event base rates between measured breaks)", "",
          "| era | rows | " + " | ".join(TARGETS) + " |", "|---|---|" + "---|" * len(TARGETS)]
    for rec in rep["era_rates"]:
        L.append(f"| {rec['era']} | {rec['rows']} | " + " | ".join(f"{rec[t]:.0%}" if rec[t] is not None else "—" for t in TARGETS) + " |")
    L += ["", "These are the unconditional rates a forecast relaxes toward at long lead times, and they differ by an order of "
          "magnitude between arrangements; the arrangement is a marker of the whole institutional setting (wars, capital "
          "controls, financial repression, the euro), not a cause on its own.", "",
          "## 4. Pooled single-feature AUC (descriptive, in-sample)", "", "| feature | " + " | ".join(TARGETS) + " |", "|---|" + "---|" * len(TARGETS)]
    for c in COLS:
        L.append(f"| {c} | " + " | ".join(f"{rep['single_feature'][c][t]:.2f}" if rep["single_feature"][c][t] else "—" for t in TARGETS) + " |")
    L += ["", "Below 0.5 means the feature's high values go with fewer events (read 1 − AUC for the strength).", ""]
    open(os.path.join(ROOT, "history", "analogs", "topology_test.md"), "w").write("\n".join(L))
    print("\n".join(L[:14]))


if __name__ == "__main__":
    main()
