#!/usr/bin/env python3
"""Is the JST crisis label a good target? Tests of the label against the measured record.

The crisisJST flag is a narrative judgment (the chronology says so: major bank failures, panics, losses, recapitalization
or government intervention, dated to the first year). A good target should (1) coincide with measurable stress in the
same data, (2) be reproducible, in most cases, from measured conditions alone, (3) be dated consistently, and (4) be at
least as predictable from the state as a measured alternative. This script measures each.

  1. Aftermath separability: how well each measured aftermath variable (real equity return, real GDP per capita,
     unemployment, loans/GDP, bank capital ratio, noncore funding) separates labelled crisis years from all other years
     - an AUC per variable, with medians for both groups.
  2. A measured stress event defined from the data alone (3 of 5 conditions in a year: real equity <= -20%, real GDP
     per capita <= -2%, unemployment +1.5 pp, loans/GDP -2 pp, bank capital ratio -0.7 pp; first year of a run), and
     its agreement with the label within +-1 year: precision, recall, and the unmatched episodes on both sides.
  3. Timing: for each labelled crisis, the year of maximum measured stress relative to the label year.
  4. Contestedness across chronologies, from the chronology document's own comparison sections.
  5. Predictability from the state, label vs measured targets, read from history/analogs/test2.json.

Usage: python3 -I history/tools/label_test.py ; writes history/analogs/label_test.md and label_test.json
"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from wf import auc  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))


def main():
    rows = load_jst(apply_overrides=True)
    jst = {(r["iso"], r["year"]): r for r in rows}
    isos = sorted({r["iso"] for r in rows})

    def g(i, y, k):
        r = jst.get((i, y))
        return np.nan if r is None or r.get(k) is None else float(r[k])

    def real_eq(i, u):
        r, c0, c1 = g(i, u, "eq_tr"), g(i, u - 1, "cpi"), g(i, u, "cpi")
        return np.nan if np.isnan(r) or np.isnan(c0) or np.isnan(c1) or c0 == 0 else (1 + r) / (c1 / c0) - 1

    def score(i, u):
        rg0, rg1 = g(i, u - 1, "rgdpmad"), g(i, u, "rgdpmad")
        rg = np.nan if np.isnan(rg0) or np.isnan(rg1) or not rg0 else rg1 / rg0 - 1
        du = g(i, u, "unemp") - g(i, u - 1, "unemp")
        l1, g1, l0, g0 = g(i, u, "tloans"), g(i, u, "gdp"), g(i, u - 1, "tloans"), g(i, u - 1, "gdp")
        dl = np.nan if any(np.isnan(v) for v in (l1, g1, l0, g0)) or not g1 or not g0 else l1 / g1 - l0 / g0
        dlev = g(i, u, "lev") - g(i, u - 1, "lev")
        conds = [(real_eq(i, u), lambda v: v <= -0.20), (rg, lambda v: v <= -0.02), (du, lambda v: v >= 1.5),
                 (dl, lambda v: v <= -0.02), (dlev, lambda v: v <= -0.7)]
        avail = [(v, f) for v, f in conds if not np.isnan(v)]
        if len(avail) < 3:
            return np.nan, len(avail)
        return sum(1 for v, f in avail if f(v)), len(avail)

    years = list(range(1871, 2021))
    rep = {}

    # ---------------------------------------------------------------- 1. aftermath separability
    labels, aft = [], {k: [] for k in ("real_eq_min_t_t1", "rgdp_pc_min_growth_t_t2", "unemp_max_rise_t_t2", "dloans_gdp_min_t_t3",
                                      "lev_min_change_t_t2", "noncore_change_t_t2", "ltrate_change_t_t1")}
    for i in isos:
        for y in years:
            if (i, y) not in jst or y > 2017:
                continue
            labels.append(1.0 if g(i, y, "crisisJST") == 1 else 0.0)
            re_ = [real_eq(i, y), real_eq(i, y + 1)]
            aft["real_eq_min_t_t1"].append(np.nan if all(np.isnan(v) for v in re_) else np.nanmin(re_))
            rg = []
            for u in (y, y + 1, y + 2):
                a, b = g(i, u - 1, "rgdpmad"), g(i, u, "rgdpmad")
                rg.append(np.nan if np.isnan(a) or np.isnan(b) or not a else b / a - 1)
            aft["rgdp_pc_min_growth_t_t2"].append(np.nan if all(np.isnan(v) for v in rg) else np.nanmin(rg))
            u0 = g(i, y - 1, "unemp"); us = [g(i, u, "unemp") - u0 for u in (y, y + 1, y + 2)]
            aft["unemp_max_rise_t_t2"].append(np.nan if all(np.isnan(v) for v in us) else np.nanmax(us))
            l0, g0 = g(i, y - 1, "tloans"), g(i, y - 1, "gdp"); dl = []
            for u in (y, y + 1, y + 2, y + 3):
                l1, g1 = g(i, u, "tloans"), g(i, u, "gdp")
                dl.append(np.nan if any(np.isnan(v) for v in (l0, g0, l1, g1)) or not g0 or not g1 else l1 / g1 - l0 / g0)
            aft["dloans_gdp_min_t_t3"].append(np.nan if all(np.isnan(v) for v in dl) else np.nanmin(dl))
            lv0 = g(i, y - 1, "lev"); lv = [g(i, u, "lev") - lv0 for u in (y, y + 1, y + 2)]
            aft["lev_min_change_t_t2"].append(np.nan if all(np.isnan(v) for v in lv) else np.nanmin(lv))
            aft["noncore_change_t_t2"].append(g(i, y + 2, "noncore") - g(i, y - 1, "noncore"))
            aft["ltrate_change_t_t1"].append(g(i, y + 1, "ltrate") - g(i, y - 1, "ltrate"))
    sep = {}
    for k, vals in aft.items():
        v = np.array(vals, dtype=float); lab = np.array(labels)
        # orient so that higher = more stress
        sign = -1.0 if k in ("real_eq_min_t_t1", "rgdp_pc_min_growth_t_t2", "dloans_gdp_min_t_t3", "lev_min_change_t_t2") else 1.0
        sc = [None if np.isnan(x) else sign * x for x in v]
        A, npos, nneg = auc(sc, [l if not np.isnan(x) else None for x, l in zip(v, lab)])
        mc = np.nanmedian(v[(lab == 1) & ~np.isnan(v)]); mn = np.nanmedian(v[(lab == 0) & ~np.isnan(v)])
        sep[k] = {"auc_as_detector": A, "median_crisis_years": float(mc), "median_other_years": float(mn), "n_crisis": npos, "n_other": nneg}
    rep["aftermath_separability"] = sep

    # ---------------------------------------------------------------- 2. measured stress events vs the label
    def score_real(i, u):
        rg0, rg1 = g(i, u - 1, "rgdpmad"), g(i, u, "rgdpmad")
        rg = np.nan if np.isnan(rg0) or np.isnan(rg1) or not rg0 else rg1 / rg0 - 1
        du = g(i, u, "unemp") - g(i, u - 1, "unemp")
        conds = [(real_eq(i, u), lambda v: v <= -0.20), (rg, lambda v: v <= -0.02), (du, lambda v: v >= 1.5)]
        avail = [(v, f) for v, f in conds if not np.isnan(v)]
        if len(avail) < 2:
            return np.nan
        return sum(1 for v, f in avail if f(v))

    lab_years = [(i, y) for i in isos for y in years if y <= 2020 and g(i, y, "crisisJST") == 1]
    lab_set = set(lab_years)
    def near(a, S):
        return any((a[0], a[1] + d) in S for d in (-1, 0, 1))
    rep["measured_events"] = {}
    for name, fn, thr, definition in (
            ("five_condition_3of5", lambda i, y: score(i, y)[0], 3,
             "first year of a run with >= 3 of 5 conditions (real equity <= -20%, real GDP/cap <= -2%, unemployment +1.5 pp, loans/GDP -2 pp, bank capital ratio -0.7 pp); years with fewer than 3 conditions observable are skipped"),
            ("real_economy_2of3", score_real, 2,
             "first year of a run with >= 2 of 3 real-economy conditions (real equity <= -20%, real GDP/cap <= -2%, unemployment +1.5 pp); years with fewer than 2 observable are skipped")):
        events = []
        for i in isos:
            prev = 0
            for y in years:
                if y > 2020:
                    continue
                sc = fn(i, y)
                cur = 1 if (not np.isnan(sc) and sc >= thr) else 0
                if cur and not prev:
                    events.append((i, y))
                prev = cur
        ev_set = set(events)
        matched_ev = [e for e in events if near(e, lab_set)]
        matched_lab = [l for l in lab_years if near(l, ev_set)]
        rep["measured_events"][name] = {
            "definition": definition, "n_events": len(events), "n_labels": len(lab_years),
            "precision_within_1y": len(matched_ev) / len(events) if events else None,
            "recall_within_1y": len(matched_lab) / len(lab_years) if lab_years else None,
            "labels_without_measured_stress": sorted(l for l in lab_years if not near(l, ev_set)),
            "measured_stress_without_label": sorted(e for e in events if not near(e, lab_set)),
        }

    # ---------------------------------------------------------------- 3. timing
    timing = {-1: 0, 0: 0, 1: 0, 2: 0, "no stress score": 0}
    for i, y in lab_years:
        sc = {d: score(i, y + d)[0] for d in (-1, 0, 1, 2)}
        sc = {d: v for d, v in sc.items() if not np.isnan(v)}
        if not sc or max(sc.values()) == 0:
            timing["no stress score"] += 1
        else:
            m = max(sc.values()); best = min(d for d, v in sc.items() if v == m)
            timing[best] += 1
    rep["timing_of_max_measured_stress_relative_to_label"] = {str(k): v for k, v in timing.items()}

    # ---------------------------------------------------------------- 4. contestedness (from the chronology document)
    rep["contestedness"] = {
        "source": "history/jst/crises_chronology_notes.md (the document's Sections 3-5)",
        "jst_episodes_absent_from_laeven_valencia_2018_post1970": 6,
        "jst_episodes_absent_from_baron_verner_xiong_2021": 9,
        "bvx_crisis_years_rejected_by_jst": 30,
        "recodings_between_jst_versions": 7,
        "note": "88 labelled episodes; roughly one in ten is contested by at least one other chronology, and the authors themselves recoded seven between releases",
    }

    # ---------------------------------------------------------------- 5. predictability from the state
    t2 = os.path.join(ROOT, "history", "analogs", "test2.json")
    if os.path.exists(t2):
        r2 = json.load(open(t2))
        rep["predictability_from_state_walk_forward_all_features"] = {t: v["auc"] for t, v in r2["results"]["all"].items()}
        rep["predictability_horizon_curve_all_features"] = {h: v["auc"] for h, v in r2["horizon"]["all"].items()}

    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    json.dump(rep, open(os.path.join(ROOT, "history", "analogs", "label_test.json"), "w"), indent=1, default=str)
    L = ["# Testing the target: is the JST crisis label a good one?", "",
         "The flag is a narrative judgment dated to the first year of an episode. Four tests against the measured record.", "",
         "## 1. Do labelled crisis years look different in the measured data?", "",
         "AUC of each aftermath variable as a detector of a labelled crisis year (oriented so that more stress scores higher; 0.5 = the label is unrelated to the variable):", "",
         "| aftermath variable (window) | AUC | median, crisis years | median, other years | n crisis / other |", "|---|---|---|---|---|"]
    for k, v in sep.items():
        L.append(f"| {k} | {v['auc_as_detector']:.2f} | {v['median_crisis_years']:+.3f} | {v['median_other_years']:+.3f} | {v['n_crisis']} / {v['n_other']} |")
    L += ["", "## 2. Can the label be reproduced from measured stress alone?", ""]
    for name, me in rep["measured_events"].items():
        L += [f"**{name}** — {me['definition']}. Events found: {me['n_events']}; labels: {me['n_labels']}.", "",
              f"- Precision (measured events with a label within ±1 year): {me['precision_within_1y']:.0%}",
              f"- Recall (labels with a measured event within ±1 year): {me['recall_within_1y']:.0%}", "",
              f"Labelled crises with no measured stress within ±1 year ({len(me['labels_without_measured_stress'])}): " +
              ", ".join(f"{i} {y}" for i, y in me["labels_without_measured_stress"]), "",
              f"Measured stress with no label within ±1 year ({len(me['measured_stress_without_label'])}): " +
              ", ".join(f"{i} {y}" for i, y in me["measured_stress_without_label"]), ""]
    L += ["## 3. Timing", "",
          "Year of maximum measured stress relative to the label year (t−1 / t / t+1 / t+2 / no stress at all): " +
          " / ".join(str(timing[k]) for k in (-1, 0, 1, 2, "no stress score")), "",
          "## 4. Contestedness across chronologies", "",
          f"From the chronology document's own comparisons: {rep['contestedness']['jst_episodes_absent_from_laeven_valencia_2018_post1970']} post-1970 JST episodes are absent from Laeven–Valencia; "
          f"{rep['contestedness']['jst_episodes_absent_from_baron_verner_xiong_2021']} JST episodes are absent from Baron–Verner–Xiong, who in turn date {rep['contestedness']['bvx_crisis_years_rejected_by_jst']} crisis years JST rejects; "
          f"the authors recoded {rep['contestedness']['recodings_between_jst_versions']} episodes between releases. {rep['contestedness']['note']}.", ""]
    if "predictability_from_state_walk_forward_all_features" in rep:
        p = rep["predictability_from_state_walk_forward_all_features"]
        L += ["## 5. Predictability from the state (walk-forward, all 45 features, from test2)", "",
              "| target | AUC |", "|---|---|"] + [f"| {t} | {v:.2f} |" for t, v in p.items()] + ["",
              "Horizon curve for the label: " + ", ".join(f"{h}y {v:.2f}" for h, v in rep["predictability_horizon_curve_all_features"].items()), ""]
    open(os.path.join(ROOT, "history", "analogs", "label_test.md"), "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
