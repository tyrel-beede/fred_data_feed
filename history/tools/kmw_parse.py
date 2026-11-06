#!/usr/bin/env python3
"""Parse the Mendeley deposit of the European energy-consumption series (Kander, Malanima, Warde and the national
compilers, as assembled by Rubio-Varas and Munoz-Delgado, CC BY 4.0) into history/physical/kmw_extract.csv.

Workbook: history/physical/raw/KMW-EUROPE-ENERGY/Energy use and EMCI.xlsx. One sheet per country with annual energy
use by carrier in PJ (food, feed for draught animals, fuelwood, water/wind, coal, oil, natural gas, hydro and other
primary electricity, nuclear, TOTAL); the UK sheet (Fouquet) is in mtoe and converted at 41.868 PJ per mtoe.

Output columns (PJ): iso, year, food, feed, fuelwood, water_wind, coal, oil, gas, hydro_other, nuclear, total_all
(the sheet's TOTAL, all forms including muscle energy), fuel_total (fuelwood + coal + oil + gas + hydro_other +
nuclear: the fuels, the analogue of EIA's total), fossil_total (coal + oil + gas), sheet. Every row's fuel_total and
fossil_total are computed here; total_all is the compilers' own and is checked against the sum of the carriers to
within 1% (rows outside that are kept and flagged in the check column).
Run: python3 -I history/tools/kmw_parse.py
"""
import csv, os, re, sys, warnings

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
XLSX = os.path.join(ROOT, "history", "physical", "raw", "KMW-EUROPE-ENERGY", "Energy use and EMCI.xlsx")
OUT = os.path.join(ROOT, "history", "physical", "kmw_extract.csv")
SHEETS = {"SwedenFinal": "SWE", "SpainFinal": "ESP", "PortugalFinal": "PRT", "ItalyFinal": "ITA", "NetherlandsFinal": "NLD",
          "GermanyFinal": "DEU", "UK Prim Energy": "GBR", "FranceFinal": "FRA"}  # England & Wales (Warde) kept out: GBR is the UK
# header text (lower-case prefix) -> output column, for the country sheets (header row 2) and the UK sheet (row 4)
MAP = [("food", "food"), ("feed for draught", "feed"), ("fodder", "feed"), ("fuelwood", "fuelwood"), ("wood", "fuelwood"),
       ("water,wind", "water_wind"), ("coal", "coal"), ("oil", "oil"), ("petroleum", "oil"), ("natural gas", "gas"),
       ("hydro,geo", "hydro_other"), ("primary electricity", "hydro_other"), ("nuclear", "nuclear"), ("total", "total_all")]
MTOE_TO_PJ = 41.868


def num(v):
    try:
        return float(v) if v not in (None, "", " ") else None
    except (TypeError, ValueError):
        return None


def main():
    if not os.path.exists(XLSX):
        print("workbook not present:", XLSX); return 2
    warnings.filterwarnings("ignore")
    import openpyxl
    wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
    out, flagged = [], 0
    for sheet, iso in SHEETS.items():
        rows = list(wb[sheet].iter_rows(values_only=True))
        hrow = 3 if iso == "GBR" else 1
        hdr = [(str(c).strip().lower() if c is not None else "") for c in rows[hrow]]
        cols = {}
        for j, h in enumerate(hdr):
            if not h:
                continue
            for prefix, name in MAP:
                if h.startswith(prefix) and name not in cols:
                    cols[name] = j; break
            if iso == "GBR" and j > 10:  # the UK sheet's hydro/wind/nuclear detail columns sit after the primary set
                break
        scale = MTOE_TO_PJ if iso == "GBR" else 1.0
        missing = [n for n in ("fuelwood", "coal", "total_all") if n not in cols]
        if missing:
            print(f"  {sheet}: columns not found {missing}; header {hdr[:12]}"); return 1
        n0 = len(out)
        for r in rows[hrow + 1:]:
            y = r[0]
            if y is None or not re.fullmatch(r"\d{4}(\.0)?", str(y)):
                continue
            y = int(float(y))
            vals = {name: (None if j >= len(r) else num(r[j])) for name, j in cols.items()}
            if vals.get("total_all") is None:
                continue
            vals = {k: (v * scale if v is not None else None) for k, v in vals.items()}
            g = lambda k: vals.get(k) or 0.0  # noqa: E731
            fuel = g("fuelwood") + g("coal") + g("oil") + g("gas") + g("hydro_other") + g("nuclear")
            fossil = g("coal") + g("oil") + g("gas")
            allsum = fuel + g("food") + g("feed") + g("water_wind")
            check = "ok" if vals["total_all"] and abs(allsum / vals["total_all"] - 1) <= 0.01 else "total differs from carrier sum by > 1%"
            if check != "ok":
                flagged += 1
            out.append({"iso": iso, "year": y, **{k: ("" if vals.get(k) is None else f"{vals[k]:.6g}") for k in
                        ("food", "feed", "fuelwood", "water_wind", "coal", "oil", "gas", "hydro_other", "nuclear", "total_all")},
                        "fuel_total": f"{fuel:.6g}", "fossil_total": f"{fossil:.6g}", "sheet": sheet, "check": check})
        ys = [o["year"] for o in out[n0:]]
        print(f"  {sheet} -> {iso}: {len(ys)} years {min(ys)}-{max(ys)}; columns {sorted(cols)}")
    out.sort(key=lambda o: (o["iso"], o["year"]))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"{len(out)} rows -> {OUT}; rows whose total differs from the carrier sum by > 1%: {flagged}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
