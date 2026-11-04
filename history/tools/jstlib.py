"""Shared loader for the JST layer: the R6 sheet, the overrides with their provenance, and the derived features.

load_jst(apply_overrides=True) -> list of dict rows (one per country-year), values as floats where numeric.
Each row gets an 'overrides' field: comma-separated variable names whose value was replaced from overrides.csv
(provenance for the replacement is in that file; the JST value is never changed on disk).
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
JST = os.path.join(os.path.dirname(HERE), "jst")

NUMERIC_EXCEPT = {"year", "country", "iso", "ifs", "peg_type", "peg_base"}


def _num(v):
    if v in ("", None):
        return None
    try:
        return float(v)
    except ValueError:
        return v


def load_overrides():
    p = os.path.join(JST, "overrides.csv")
    if not os.path.exists(p):
        return []
    return list(csv.DictReader(open(p)))


def load_jst(apply_overrides=True):
    rows = []
    with open(os.path.join(JST, "jst_r6.csv")) as f:
        for r in csv.DictReader(f):
            row = {k: (r[k] if k in NUMERIC_EXCEPT else _num(r[k])) for k in r}
            row["year"] = int(row["year"])
            row["overrides"] = ""
            rows.append(row)
    if apply_overrides:
        by = {(r["iso"], r["year"]): r for r in rows}
        for o in load_overrides():
            if o["action"] != "replace":
                continue
            r = by.get((o["iso"], int(o["year"])))
            if r is None:
                continue
            r[o["variable"]] = float(o["override_value"])
            r["overrides"] = (r["overrides"] + "," if r["overrides"] else "") + o["variable"]
    return rows


def load_features():
    with open(os.path.join(JST, "features.csv")) as f:
        out = []
        for r in csv.DictReader(f):
            row = {k: (_num(v) if k not in ("iso", "overrides") else v) for k, v in r.items()}
            row["year"] = int(row["year"])
            out.append(row)
        return out
