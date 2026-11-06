#!/usr/bin/env python3
"""test_materialize.py — the invariant in FEED.md §8: state/ must be reproducible from runs/ byte for byte.

Rebuilds state/ into a temporary folder from the committed runs/ and compares every file with the committed
state/. Also checks that the dials scoreboard reproduces the Brier memory logged (0.121, n=12) and that no
logged Brier disagrees with (p - outcome)^2.

Usage: python3 -I dials/tools/test_materialize.py [--root dials]      exit 0 = pass
"""
import argparse, filecmp, json, os, subprocess, sys, tempfile


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="dials"); a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    fails = []
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run([sys.executable, "-I", os.path.join(here, "materialize.py"), "--root", a.root, "--out", tmp], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout, r.stderr); return 2
        committed = os.path.join(a.root, "state")
        names = sorted(set(os.listdir(tmp)) | set(os.listdir(committed)))
        for n in names:
            p1, p2 = os.path.join(tmp, n), os.path.join(committed, n)
            if not (os.path.exists(p1) and os.path.exists(p2)):
                fails.append(f"{n}: present in only one of rebuilt / committed")
            elif not filecmp.cmp(p1, p2, shallow=False):
                fails.append(f"{n}: rebuilt state differs from committed state")
        sb = json.load(open(os.path.join(tmp, "scoreboard.json")))
    d = sb["all"].get("dials", {})
    if d.get("n") != 12 or round(d.get("brier_mean", -1), 3) != 0.121:
        fails.append(f"dials scoreboard {d} does not reproduce the logged Brier 0.121 (n=12)")
    if sb["brier_logged_vs_recomputed_mismatches"]:
        fails.append(f"logged vs recomputed Brier mismatches: {sb['brier_logged_vs_recomputed_mismatches']}")
    if fails:
        print("FAIL"); [print(" -", f) for f in fails]; return 1
    print(f"PASS: state/ reproducible ({len(names)} files); dials Brier {d['brier_mean']:.5f} n={d['n']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
