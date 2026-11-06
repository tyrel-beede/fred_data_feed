#!/usr/bin/env python3
"""One more turn: a learner that can weight, walk-forward, on the measured targets.

Nearest neighbours cannot weight features, so redundant dimensions dilute the few that matter. Here the same features
feed two learners refit every year on data whose outcome window closed before that year:
  logit      L2-regularized logistic regression on standardized, median-imputed features (training-set statistics only)
  gbt        histogram gradient boosting (shallow trees; handles missing values natively)
  knn        the walk-forward nearest-neighbour share from test 2, as the no-weights reference
  ensemble   mean of the three learners' within-year percentile ranks
Feature set: base 20 + subnet 10 + rank 6 + flux 9 + five selected leads + three mile-marker indicators
(loans/GDP top tercile at T-3, real equity 3y gain <= 0 at T-1, real house prices 3y growth <= 0 at T; terciles from
training data only). Targets: the four measured events and the crisis label, within 3 years. Reports walk-forward
AUC and top-decile rate per learner and target, a horizon curve for the best learner, and the heaviest logit weights
in the final fit.

Usage: python3 -I history/tools/learner_test.py ; writes history/analogs/learner_test.md and learner_test.json
"""
import argparse, csv, json, os, sys, warnings
import numpy as np

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402
from analogs import GROUPS  # noqa: E402
from wf import walk_forward_neighbors, predict, auc, top_decile, build_targets  # noqa: E402
from analog_test2 import NETWORK, RANK, FLUX  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.ensemble import HistGradientBoostingClassifier  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
BASE = [f for g in GROUPS.values() for f in g]
LEADS = [("loans_gdp", 3), ("mort_gdp", 3), ("real_eq_capgain_3y", 1), ("rgdp_pc_growth", 1), ("r_minus_g", 1)]
TARGETS = ["dd30_3y", "credit_contraction_3y", "gdp_fall_3y", "unemp_spike_3y", "crisis_3y"]


PHYSICAL = ["energy_footprint_gap_3y", "gap_anom_3y", "d3_co2_intensity", "co2_growth_3y", "co2_growth_1y",
            "fossil_prod_growth_3y", "fuel_self_sufficiency", "coal_share_co2", "oil_share_co2",
            "oil_real_price", "oil_real_change_1y", "oil_real_change_3y", "oil_change_x_exposure"]
# second physical slice (physical_build2.py): technology diffusion per country-year, materials per year (global at t)
DIFFUSION = ["tech_growth_3y", "tech_accel_3y", "tech_max_growth_3y", "tech_frontier_gap", "rank_tech_growth_3y",
             "rail_growth_3y", "elec_growth_3y", "car_growth_3y", "phone_growth_3y", "elec_per_co2_growth_3y"]
# tech_n (how many technologies the medians rest on) stays in the CSV as a coverage column but out of the learner: it
# grows with the calendar and drops to zero after 2003, so a learner would read it as a clock
MATERIALS = ["metals_real_price_1y", "metals_real_price_3y", "metals_real_price_anom", "world_metals_prod_3y",
             "world_metals_prod_accel", "gold_real_3y", "ppi_commod_real_1y", "ppi_commod_real_3y"]
# the network's topology (topology.py): the node's subnet, its tenure and moves, the panel's fragmentation and churn
TOPOLOGY = ["in_peg", "is_base", "bloc_size", "bloc_share", "bloc_tenure", "regime_change_3y", "bloc_churn_3y", "base_changed_5y",
            "n_blocs", "panel_peg_share", "panel_changes_3y", "years_since_break"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--physical", action="store_true", help="add the physical-layer features (history/physical/physical_features.csv)")
    ap.add_argument("--diffusion", action="store_true", help="add the technology-diffusion features (history/physical/diffusion_features.csv)")
    ap.add_argument("--materials", action="store_true", help="add the materials features, global at t (history/physical/materials_features.csv)")
    ap.add_argument("--topology", action="store_true", help="add the network-topology features (history/jst/topology.csv)")
    ap.add_argument("--measured-energy", action="store_true",
                    help="with --physical: use the footprint gap from measured energy where it exists (fgap_merged_3y, fgap_anom_merged_3y) instead of the CO2 proxy")
    ap.add_argument("--no-horizon", action="store_true"); ap.add_argument("--tag", default="")
    ap.add_argument("--era-split", type=int, default=0, help="also report AUC for query years before and from this year")
    ap.add_argument("--cadence-offset", type=int, default=0, help="shift the refit years (1900, 1904, ...) by this many years: the cadence noise band")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(os.path.join(ROOT, "history", "jst", "features2.csv"))))
    if a.physical:
        ph = {(r["iso"], int(r["year"])): r for r in csv.DictReader(open(os.path.join(ROOT, "history", "physical", "physical_features.csv")))}
        swap = {"energy_footprint_gap_3y": "fgap_merged_3y", "gap_anom_3y": "fgap_anom_merged_3y"} if a.measured_energy else {}
        for r in rows:
            p = ph.get((r["iso"], int(r["year"])), {})
            for c in PHYSICAL:
                r[c] = p.get(swap.get(c, c), "")
    if a.diffusion:
        df = {(r["iso"], int(r["year"])): r for r in csv.DictReader(open(os.path.join(ROOT, "history", "physical", "diffusion_features.csv")))}
        for r in rows:
            p = df.get((r["iso"], int(r["year"])), {})
            for c in DIFFUSION:
                r[c] = p.get(c, "")
    if a.materials:
        mt = {int(r["year"]): r for r in csv.DictReader(open(os.path.join(ROOT, "history", "physical", "materials_features.csv")))}
        for r in rows:
            p = mt.get(int(r["year"]), {})
            for c in MATERIALS:
                r[c] = p.get(c, "")
    if a.topology:
        tp = {(r["iso"], int(r["year"])): r for r in csv.DictReader(open(os.path.join(ROOT, "history", "jst", "topology.csv")))}
        for r in rows:
            p = tp.get((r["iso"], int(r["year"])), {})
            for c in TOPOLOGY:
                r[c] = p.get(c, "")
    isos = [r["iso"] for r in rows]; years = np.array([int(r["year"]) for r in rows])
    idx = {(i, y): n for n, (i, y) in enumerate(zip(isos, years))}
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
    T = build_targets(jst, isos, list(years))

    def col(name, lag=0):
        out = np.full(len(rows), np.nan)
        for n, (i, y) in enumerate(zip(isos, years)):
            j = idx.get((i, y - lag))
            if j is not None and rows[j][name] not in ("", None):
                out[n] = float(rows[j][name])
        return out

    extra = (PHYSICAL if a.physical else []) + (DIFFUSION if a.diffusion else []) + (MATERIALS if a.materials else []) + (TOPOLOGY if a.topology else [])
    added = [(n, f) for n, f, on in (("physical", PHYSICAL, a.physical), ("diffusion", DIFFUSION, a.diffusion), ("materials", MATERIALS, a.materials),
                                     ("topology", TOPOLOGY, a.topology)) if on]
    names = BASE + NETWORK + RANK + FLUX + [f"{f}_lag{k}" for f, k in LEADS] + extra
    X = np.column_stack([col(f) for f in BASE + NETWORK + RANK + FLUX] + [col(f, k) for f, k in LEADS] + [col(f) for f in extra])
    lg3, eq1, hp0 = col("loans_gdp", 3), col("real_eq_capgain_3y", 1), col("real_hp_growth_3y", 0)
    nF = X.shape[1]
    rep = {"features": names + ["mk_loans_top_tercile_T-3", "mk_equity_le0_T-1", "mk_houses_le0_T"], "cadence_offset": a.cadence_offset,
           "results": {}, "horizon": {}, "weights": {}}

    def fit_predict(Xtr, ytr, Xte, learner):
        keep = (~np.isnan(Xtr)).sum(axis=0) >= 50  # a column unobserved in the training era cannot be used (or binned)
        Xtr, Xte = Xtr[:, keep], Xte[:, keep]
        if learner == "logit":
            med = np.nanmedian(Xtr, axis=0); med = np.where(np.isnan(med), 0.0, med)
            A = np.where(np.isnan(Xtr), med, Xtr); B = np.where(np.isnan(Xte), med, Xte)
            mu, sd = A.mean(axis=0), A.std(axis=0); sd[sd == 0] = 1.0
            A = (A - mu) / sd; B = (B - mu) / sd
            m = LogisticRegression(C=0.3, max_iter=2000, class_weight="balanced")
            m.fit(A, ytr)
            coef = np.full(len(keep), np.nan); coef[keep] = m.coef_[0]
            return m.predict_proba(B)[:, 1], coef
        m = HistGradientBoostingClassifier(max_iter=120, max_depth=3, learning_rate=0.06, min_samples_leaf=25,
                                           l2_regularization=1.0, class_weight="balanced", random_state=0)
        m.fit(Xtr, ytr)
        return m.predict_proba(Xte)[:, 1], None

    def run(target, horizon=3, learners=("logit", "gbt"), from_year=1900, step=4):
        y = T[target]
        preds = {l: [None] * len(rows) for l in learners}
        last_coef = None
        for t in range(from_year, 2021, step):
            te = np.where((years >= t) & (years < t + step))[0]  # the model fitted at t forecasts the next `step` years
            if len(te) == 0:
                continue
            tr = np.where((years + horizon < t) & (years >= 1880) & ~np.isnan(y))[0]
            if len(tr) < 200 or y[tr].sum() < 15:
                continue
            # markers with training-set terciles
            q = np.nanpercentile(lg3[tr], 67)
            def mk(ix):
                return np.column_stack([np.where(np.isnan(lg3[ix]), np.nan, (lg3[ix] >= q).astype(float)),
                                        np.where(np.isnan(eq1[ix]), np.nan, (eq1[ix] <= 0).astype(float)),
                                        np.where(np.isnan(hp0[ix]), np.nan, (hp0[ix] <= 0).astype(float))])
            Xtr = np.column_stack([X[tr], mk(tr)]); Xte = np.column_stack([X[te], mk(te)])
            # require the test rows to have at least 60% of features
            ok = (~np.isnan(Xte)).sum(axis=1) / Xte.shape[1] >= 0.6
            for l in learners:
                p, coef = fit_predict(Xtr, y[tr], Xte, l)
                for j, n in enumerate(te):
                    if ok[j]:
                        preds[l][n] = float(p[j])
                if l == "logit":
                    last_coef = coef
        return preds, last_coef

    # knn reference (test-2 harness) on the same feature matrix
    knn_nb = walk_forward_neighbors(X, isos, list(years), horizon=3, k=15, min_cov=0.6, from_year=1900)
    for target in TARGETS:
        preds, coef = run(target, from_year=1900 + a.cadence_offset)
        preds["knn"] = predict(knn_nb, T[target])
        # ensemble: mean of within-year percentile ranks
        ens = [None] * len(rows)
        for t in sorted(set(years.tolist())):
            te = np.where(years == t)[0]
            ranks = {}
            for l in ("logit", "gbt", "knn"):
                vals = [(n, preds[l][n]) for n in te if preds[l][n] is not None]
                if len(vals) < 3:
                    continue
                order = sorted(vals, key=lambda v: v[1])
                for r_, (n, _) in enumerate(order):
                    ranks.setdefault(n, []).append(r_ / (len(order) - 1))
            for n, rs in ranks.items():
                if len(rs) == 3:
                    ens[n] = float(np.mean(rs))
        preds["ensemble"] = ens
        res = {}
        for l in ("knn", "logit", "gbt", "ensemble"):
            A, npos, nneg = auc(preds[l], T[target]); td, base = top_decile(preds[l], T[target])
            res[l] = {"auc": A, "top_decile": td, "base": base, "n_pos": npos, "n_neg": nneg}
            if a.era_split:
                for era, m in (("before", years < a.era_split), ("from", years >= a.era_split)):
                    pe = [p_ if ok_ else None for p_, ok_ in zip(preds[l], m)]
                    Ae, npe, nne = auc(pe, T[target])
                    res[l][f"auc_{era}_{a.era_split}"] = Ae; res[l][f"n_pos_{era}_{a.era_split}"] = npe
        rep["results"][target] = res
        if coef is not None:
            coef = np.where(np.isnan(coef), 0.0, coef)
            order = np.argsort(-np.abs(coef))[:12]
            rep["weights"][target] = [(rep["features"][i], float(coef[i])) for i in order]
        print(target, {l: round(v["auc"], 3) for l, v in res.items() if v["auc"]})

    # horizon curve (logit) on the label
    for target in (() if a.no_horizon else ("crisis_3y",)):
        base_name = target.replace("_3y", "")
        curve = {}
        for h in (1, 2, 3, 4, 5):
            tname = f"{base_name}_{h}y" if base_name == "crisis" else None
            if tname is None:
                continue
            preds, _ = run(tname, horizon=h, learners=("logit",))
            A, npos, nneg = auc(preds["logit"], T[tname])
            curve[h] = A
        if curve:
            rep["horizon"][target] = curve
            print("horizon logit", target, {h: round(v, 3) for h, v in curve.items() if v})

    os.makedirs(os.path.join(ROOT, "history", "analogs"), exist_ok=True)
    suffix = ("_physical" if a.physical else "") + ("_measured" if a.measured_energy else "") + ("_diffusion" if a.diffusion else "") + ("_materials" if a.materials else "") + ("_topology" if a.topology else "") + a.tag
    json.dump(rep, open(os.path.join(ROOT, "history", "analogs", f"learner_test{suffix}.json"), "w"), indent=1)
    L = ["# A learner that can weight — walk-forward", "",
         "Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries "
         "from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. "
         f"Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers{''.join(' + ' + str(len(f)) + ' ' + n for n, f in added)} = {len(names) + 3}. AUC 0.5 is no skill.", "",
         "| target (base rate) | knn (no weights) | logit | gbt | ensemble |", "|---|---|---|---|---|"]
    for target, res in rep["results"].items():
        base = next((v["base"] for v in res.values() if v["base"] is not None), 0)
        L.append(f"| {target} ({base:.0%}) | " + " | ".join(
            f"{v['auc']:.2f} (top {v['top_decile']:.0%})" if v["auc"] else "—" for v in res.values()) + " |")
    if a.era_split:
        L += ["", f"## AUC by query era (before / from {a.era_split})", "", "| target | knn | logit | gbt | ensemble |", "|---|---|---|---|---|"]
        for target, res in rep["results"].items():
            cells = []
            for l in ("knn", "logit", "gbt", "ensemble"):
                b, f_ = res[l].get(f"auc_before_{a.era_split}"), res[l].get(f"auc_from_{a.era_split}")
                cells.append((f"{b:.2f}" if b else "—") + " / " + (f"{f_:.2f}" if f_ else "—"))
            L.append(f"| {target} | " + " | ".join(cells) + " |")
    if rep["horizon"]:
        L += ["", "## Crisis label by horizon, logit", "", "| 1y | 2y | 3y | 4y | 5y |", "|---|---|---|---|---|"]
        for target, curve in rep["horizon"].items():
            L.append("| " + " | ".join(f"{curve.get(h):.2f}" if curve.get(h) else "—" for h in (1, 2, 3, 4, 5)) + " |")
    L += ["", "## Heaviest logit weights in the final (2020) fit", ""]
    for target, w in rep["weights"].items():
        L.append(f"- **{target}**: " + ", ".join(f"{f} {c:+.2f}" for f, c in w))
    L += ["", "Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the "
          "ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the "
          "numbers a forecaster at the time could have had.", ""]
    for n, f in added:
        L.insert(1, f"\n**{n.capitalize()} features added ({len(f)}): {', '.join(f)}.** Compare with learner_test.md (same harness without them).\n")
    if a.measured_energy:
        L.insert(1, "\n**Measured energy:** energy_footprint_gap_3y and gap_anom_3y are taken from measured energy consumption where it "
                    "exists (fgap_src = energy: OWID 1968-, EIA for the US 1952-, KMW for eight European countries 1873-) and from the CO2 "
                    "proxy elsewhere. Compare with learner_test_physical_era.md (the proxy everywhere).\n")
    open(os.path.join(ROOT, "history", "analogs", f"learner_test{suffix}.md"), "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
