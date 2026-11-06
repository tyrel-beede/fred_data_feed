#!/usr/bin/env python3
"""The cadence noise band: the same harness (base + physical, era split) rerun with the refit years shifted by 0, 1, 2
and 3 years (learner_test.py --cadence-offset). The spread across the four runs is the band every like-for-like
comparison in the READMEs has to clear before it is read as a difference. The tree model has no other randomness
here (no subsampling, no early stopping at this sample size), so the cadence is the whole of its run-to-run noise;
the logit's band also carries the standardization window that moves with the cadence.

Reads history/analogs/learner_test_physical_era.json (offset 0) and learner_test_physical_era_cad{1,2,3}.json.
Writes history/analogs/noise_band.md and .json.
Run: python3 -I history/tools/noise_band.py
"""
import json, os
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = os.path.join(ROOT, "history", "analogs")
FILES = {0: "learner_test_physical_era.json", 1: "learner_test_physical_era_cad1.json", 2: "learner_test_physical_era_cad2.json", 3: "learner_test_physical_era_cad3.json"}
LEARNERS = ["knn", "logit", "gbt", "ensemble"]


def main():
    runs = {k: json.load(open(os.path.join(A, f))) for k, f in FILES.items() if os.path.exists(os.path.join(A, f))}
    if len(runs) < 2:
        print("need at least two runs"); return
    targets = list(next(iter(runs.values()))["results"].keys())
    rep = {"offsets": sorted(runs), "band": {}}
    L = ["# The cadence noise band", "",
         f"Base + physical features, era split, refit years shifted by {', '.join(str(k) for k in sorted(runs))} years "
         f"({len(runs)} runs). Each cell: min–max across the runs (range). A like-for-like difference smaller than the range in its "
         "column is inside the noise.", "",
         "| target | " + " | ".join(LEARNERS) + " |", "|---|" + "---|" * len(LEARNERS)]
    for t in targets:
        cells = []
        rep["band"][t] = {}
        for l in LEARNERS:
            v = [runs[k]["results"][t][l]["auc"] for k in sorted(runs) if runs[k]["results"][t][l].get("auc") is not None]
            if v:
                rep["band"][t][l] = {"values": v, "min": min(v), "max": max(v), "range": max(v) - min(v), "mean": float(np.mean(v))}
                cells.append(f"{min(v):.2f}–{max(v):.2f} ({max(v) - min(v):.2f})")
            else:
                cells.append("—")
        L.append(f"| {t} | " + " | ".join(cells) + " |")
    # the pre-2004 bands too, since the READMEs read that window
    L += ["", "## Before 2004 (the window most skill rests on)", "", "| target | " + " | ".join(LEARNERS) + " |", "|---|" + "---|" * len(LEARNERS)]
    rep["band_before_2004"] = {}
    for t in targets:
        cells = []; rep["band_before_2004"][t] = {}
        for l in LEARNERS:
            v = [runs[k]["results"][t][l].get("auc_before_2004") for k in sorted(runs)]
            v = [x for x in v if x is not None]
            if v:
                rep["band_before_2004"][t][l] = {"min": min(v), "max": max(v), "range": max(v) - min(v)}
                cells.append(f"{min(v):.2f}–{max(v):.2f} ({max(v) - min(v):.2f})")
            else:
                cells.append("—")
        L.append(f"| {t} | " + " | ".join(cells) + " |")
    rng = {l: float(np.mean([rep["band"][t][l]["range"] for t in targets if l in rep["band"][t]])) for l in LEARNERS}
    rep["mean_range_by_learner"] = rng
    L += ["", "Mean range by learner: " + ", ".join(f"{l} {r:.3f}" for l, r in rng.items()) + ".", "",
          "Reading: a comparison between two feature sets is a finding only where it exceeds the band of the learner it was made "
          "with; the trees' band is the tighter one, and the logit's cadence sensitivity is a reason to prefer the trees for "
          "any claim about a family's contribution.", ""]
    json.dump(rep, open(os.path.join(A, "noise_band.json"), "w"), indent=1)
    open(os.path.join(A, "noise_band.md"), "w").write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
