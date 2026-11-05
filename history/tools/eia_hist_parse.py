#!/usr/bin/env python3
"""Parse EIA's table "Estimated primary energy consumption in the United States, selected years, 1635-1945" (the PDF
the workflow stores under history/physical/raw/EIA-HISTORICAL-1635/) into history/physical/eia_1635_1945.csv.

Columns in the PDF (quadrillion Btu): coal, natural gas, petroleum, fossil fuels total, conventional hydroelectric
power, wood (fuelwood only through 1945), renewable energy total (hydro + wood), electricity net imports, total.
Symbols: NA not available, - not applicable, (s) less than 0.5 trillion Btu.

The parser reads the text layer, keeps the lines that start with a listed year, maps the tokens onto the columns
(dashes and NA become empty) and then checks every row's arithmetic: fossil = coal + gas + petroleum, renewable =
hydro + wood, total = fossil + renewable + net imports (each to within 0.002 quad, the table's rounding). A row that
fails the check is written with check=fail and the run exits non-zero, so a layout change cannot pass silently.
Run: python3 -I history/tools/eia_hist_parse.py
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PDF = os.path.join(ROOT, "history", "physical", "raw", "EIA-HISTORICAL-1635", "U.S._Primary_Energy_Consumption_1635-1945.pdf")
OUT = os.path.join(ROOT, "history", "physical", "eia_1635_1945.csv")
COLS = ["coal", "natural_gas", "petroleum", "fossil_total", "hydro", "wood", "renewable_total", "electricity_net_imports", "total"]
TOL = 0.0021


def tokens(line):
    """Split a table line into cells: numbers, 'NA', '(s)' and the not-applicable symbol, which the table prints as a
    pair of dashes ("– –" = one cell, so dash tokens are paired up in order). Dot leaders and footnote letters glued
    to a number ("a1.261") are dropped."""
    out, dashes = [], 0
    for tok in re.split(r"\s+", line.strip()):
        if not tok or re.fullmatch(r"\.+", tok):
            continue
        if re.fullmatch(r"[-–—]+", tok):
            dashes += 1
            if dashes == 2:
                out.append("-"); dashes = 0
            continue
        if dashes:  # a lone dash before another token: treat as one cell
            out.append("-"); dashes = 0
        tok2 = re.sub(r"^[a-z](?=[0-9(])", "", tok)  # footnote marker
        if tok2.upper() == "NA":
            out.append("NA")
        elif tok2 == "(s)":
            out.append("(s)")
        elif re.fullmatch(r"[0-9]*\.?[0-9]+", tok2):
            out.append(tok2)
        else:
            return None  # a footnote or caption line
    if dashes:
        out.append("-")
    return out


def value(cell):
    if cell in ("-", "NA"):
        return None
    if cell == "(s)":
        return 0.0
    return float(cell)


def main():
    if not os.path.exists(PDF):
        print("PDF not present:", PDF); return 2
    try:
        import pdfplumber
        text = "\n".join((p.extract_text() or "") for p in pdfplumber.open(PDF).pages)
    except Exception:  # noqa
        from pypdf import PdfReader
        text = "\n".join((p.extract_text() or "") for p in PdfReader(PDF).pages)
    rows, bad = [], 0
    for line in text.splitlines():
        m = re.match(r"\s*(1[6-9]\d{2})\b(.*)", line)
        if not m:
            continue
        year, rest = int(m.group(1)), m.group(2)
        cells = tokens(rest)
        if cells is None or len(cells) < 3:
            continue
        if len(cells) != len(COLS):
            rows.append({"year": year, "check": f"fail: {len(cells)} cells", "_raw": " ".join(cells)}); bad += 1
            continue
        vals = dict(zip(COLS, (value(c) for c in cells)))
        g = lambda k: vals[k] or 0.0  # noqa: E731
        ok = (abs(g("coal") + g("natural_gas") + g("petroleum") - g("fossil_total")) <= TOL
              and abs(g("hydro") + g("wood") - g("renewable_total")) <= TOL
              and abs(g("fossil_total") + g("renewable_total") + g("electricity_net_imports") - g("total")) <= TOL)
        rec = {"year": year, **{k: ("" if vals[k] is None else f"{vals[k]:g}") for k in COLS}, "check": "ok" if ok else "fail: sums"}
        if not ok:
            bad += 1; rec["_raw"] = " ".join(cells)
        rows.append(rec)
    rows.sort(key=lambda r: r["year"])
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year"] + COLS + ["check"], extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rows -> {OUT}; failed checks: {bad}")
    for r in rows:
        if r["check"] != "ok":
            print("  ", r["year"], r["check"], r.get("_raw", ""))
    return 1 if bad or not rows else 0


if __name__ == "__main__":
    sys.exit(main())
