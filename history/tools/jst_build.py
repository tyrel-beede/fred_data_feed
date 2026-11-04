#!/usr/bin/env python3
"""Build the JST layer of history/ from the Jordà–Schularick–Taylor Macrohistory Database workbook.

Inputs  : history/jst/JSTdatasetR6.xlsx  (the release-6 workbook as distributed at macrohistory.net)
Outputs : history/jst/jst_r6.csv          the sheet as CSV, values untouched (counted/measured numbers, provenance JST R6)
          history/jst/coverage.csv        per country x variable: first year, last year, observations, gaps inside the span
          history/jst/crises_indicator.csv the crisisJST / crisisJST_old flags as a dated event table
          history/jst/features.csv        derived annual features used for analog matching (provenance: derived, this script)
          history/jst/units.csv           the nominal-currency unit per country (inferred from 2019 GDP vs World Bank USD GDP;
                                          confirm against the documentation before quoting absolute levels)

Everything derived is labeled derived. Nothing here changes a JST value.
Run: python3 -I history/tools/jst_build.py
"""
import csv, math, os, sys
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JST = os.path.join(ROOT, "history", "jst")
SRC = os.path.join(JST, "JSTdatasetR6.xlsx")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jstlib import load_overrides  # noqa: E402

# Unit of the nominal local-currency variables (gdp, revenue, expenditure, tloans, tmort, thh, tbus, money, narrowm, ca,
# imports, exports, bdebt): multiplier that turns the stored number into billions of national currency.
# Inferred 2026-11-04 from gdp(2019)/xrusd(2019) against World Bank 2019 USD GDP; euro members are in legacy national
# currency at the fixed conversion rate (DEU in DM, FRA in FRF, ITA in ITL, ...). Confirm per variable in the documentation.
UNIT_TO_BN = {"AUS": 1e-3, "BEL": 1e-3, "CAN": 1.0, "CHE": 1e-3, "DEU": 1.0, "DNK": 1.0, "ESP": 1e-3, "FIN": 1e-3,
              "FRA": 1.0, "GBR": 1.0, "IRL": 1e-3, "ITA": 1.0, "JPN": 1e3, "NLD": 1e-3, "NOR": 1e-3, "PRT": 1e-3,
              "SWE": 1e-3, "USA": 1.0}
UNIT_NAME = {"AUS": "millions AUD", "BEL": "millions BEF (legacy, fixed EUR rate 40.3399)", "CAN": "billions CAD",
             "CHE": "millions CHF", "DEU": "billions DEM (legacy, 1.95583/EUR)", "DNK": "billions DKK",
             "ESP": "millions ESP (legacy, 166.386/EUR)", "FIN": "millions FIM (legacy, 5.94573/EUR)",
             "FRA": "billions FRF (legacy, 6.55957/EUR)", "GBR": "billions GBP", "IRL": "millions IEP (legacy, 0.787564/EUR)",
             "ITA": "billions ITL (legacy, 1936.27/EUR)", "JPN": "trillions JPY", "NLD": "millions NLG (legacy, 2.20371/EUR)",
             "NOR": "millions NOK", "PRT": "millions PTE (legacy, 200.482/EUR)", "SWE": "millions SEK", "USA": "billions USD"}


def fnum(v):
    return None if v in (None, "") else float(v)


def load():
    wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    data = [dict(zip(hdr, r)) for r in rows[1:]]
    return hdr, data


def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    hdr, data = load()
    # 1) the sheet as CSV, values untouched
    write_csv(os.path.join(JST, "jst_r6.csv"), hdr,
              [["" if r[h] is None else (repr(r[h]) if isinstance(r[h], float) else r[h]) for h in hdr] for r in data])
    isos = sorted({r["iso"] for r in data})
    by = {(r["iso"], r["year"]): r for r in data}

    # 2) coverage
    cov = []
    for iso in isos:
        rr = [r for r in data if r["iso"] == iso]
        for h in hdr[4:]:
            ys = [r["year"] for r in rr if r[h] is not None]
            if ys:
                cov.append([iso, h, min(ys), max(ys), len(ys), max(ys) - min(ys) + 1 - len(ys)])
            else:
                cov.append([iso, h, "", "", 0, ""])
    write_csv(os.path.join(JST, "coverage.csv"), ["iso", "variable", "first_year", "last_year", "n_obs", "gaps_inside_span"], cov)

    # 3) crisis indicator as an event table
    ev = []
    for r in data:
        if r["crisisJST"] == 1 or r["crisisJST_old"] == 1:
            ev.append([r["iso"], r["country"], r["year"], int(r["crisisJST"] or 0), int(r["crisisJST_old"] or 0),
                       "systemic financial crisis (JST indicator)", "JST R6 crisisJST / crisisJST_old; see crises_chronology.csv"])
    write_csv(os.path.join(JST, "crises_indicator.csv"),
              ["iso", "country", "year", "crisisJST", "crisisJST_old", "event", "provenance"], ev)

    # 4) units
    write_csv(os.path.join(JST, "units.csv"), ["iso", "nominal_unit", "to_billions_multiplier", "note"],
              [[iso, UNIT_NAME[iso], UNIT_TO_BN[iso], "inferred from 2019 GDP vs World Bank USD GDP; confirm in documentation"]
               for iso in isos])

    # 5) derived features (annual; per country; all ratios are unit-free). Features are computed on the overridden
    #    view: replacements from overrides.csv are applied in memory (the JST values on disk are untouched) and the
    #    affected rows carry the overridden variable names in the 'overrides' column.
    applied = {}
    for o in load_overrides():
        if o["action"] == "replace":
            r = by.get((o["iso"], int(o["year"])))
            if r is not None:
                r[o["variable"]] = float(o["override_value"])
                applied.setdefault((o["iso"], int(o["year"])), []).append(o["variable"])

    def g(iso, y, k):
        r = by.get((iso, y))
        return None if r is None else fnum(r.get(k))

    def ratio(a, b):
        return None if a is None or b in (None, 0) else a / b

    def growth(iso, y, k, n=1):
        a, b = g(iso, y, k), g(iso, y - n, k)
        return None if a is None or b in (None, 0) else (a / b) ** (1.0 / n) - 1.0

    def diff(iso, y, f, n):
        a, b = f(iso, y), f(iso, y - n)
        return None if a is None or b is None else a - b

    def loans_gdp(iso, y):
        return ratio(g(iso, y, "tloans"), g(iso, y, "gdp"))

    def mort_gdp(iso, y):
        return ratio(g(iso, y, "tmort"), g(iso, y, "gdp"))

    def debt_gdp(iso, y):
        return g(iso, y, "debtgdp")

    def iy(iso, y):
        return g(iso, y, "iy")

    def real_hp(iso, y):
        return ratio(g(iso, y, "hpnom"), g(iso, y, "cpi"))

    def real_hp_growth(iso, y, n):
        a, b = real_hp(iso, y), real_hp(iso, y - n)
        return None if a is None or b in (None, 0) else (a / b) ** (1.0 / n) - 1.0

    def real_eq_capgain(iso, y, n):
        # compounded real equity capital gain over n years from eq_capgain and CPI inflation
        tot = 1.0
        for k in range(n):
            cg, infl = g(iso, y - k, "eq_capgain"), growth(iso, y - k, "cpi")
            if cg is None or infl is None:
                return None
            tot *= (1 + cg) / (1 + infl)
        return tot ** (1.0 / n) - 1.0

    feats = []
    FH = ["iso", "year", "loans_gdp", "d3_loans_gdp", "d5_loans_gdp", "mort_gdp", "d5_mort_gdp", "debt_gdp", "d5_debt_gdp",
          "deficit_gdp", "ngdp_growth", "rgdp_pc_growth", "cpi_infl", "ltrate", "stir", "term_spread", "real_ltrate_expost",
          "r_minus_g", "interest_burden_proxy", "money_growth", "narrowm_growth", "money_gdp", "iy", "d3_iy", "eq_dp",
          "real_eq_capgain_3y", "real_hp_growth_3y", "ca_gdp", "lev", "ltd", "noncore", "unemp", "d1_unemp", "xr_depreciation",
          "crisis_now", "crisis_next_1_3y", "overrides"]
    for iso in isos:
        years = sorted(r["year"] for r in data if r["iso"] == iso)
        for y in years:
            ng = growth(iso, y, "gdp")
            lt, st = g(iso, y, "ltrate"), g(iso, y, "stir")
            infl = growth(iso, y, "cpi")
            dg = debt_gdp(iso, y)
            nxt = [g(iso, y + k, "crisisJST") for k in (1, 2, 3)]
            row = [iso, y,
                   loans_gdp(iso, y), diff(iso, y, loans_gdp, 3), diff(iso, y, loans_gdp, 5),
                   mort_gdp(iso, y), diff(iso, y, mort_gdp, 5),
                   dg, diff(iso, y, debt_gdp, 5),
                   ratio(None if g(iso, y, "expenditure") is None or g(iso, y, "revenue") is None
                         else g(iso, y, "expenditure") - g(iso, y, "revenue"), g(iso, y, "gdp")),
                   ng, growth(iso, y, "rgdpmad"), infl, lt, st,
                   None if lt is None or st is None else lt - st,
                   None if lt is None or infl is None else lt - 100 * infl,
                   None if lt is None or ng is None else lt - 100 * ng,
                   None if lt is None or dg is None else lt / 100 * dg,
                   growth(iso, y, "money"), growth(iso, y, "narrowm"), ratio(g(iso, y, "money"), g(iso, y, "gdp")),
                   iy(iso, y), diff(iso, y, iy, 3), g(iso, y, "eq_dp"),
                   real_eq_capgain(iso, y, 3), real_hp_growth(iso, y, 3),
                   ratio(g(iso, y, "ca"), g(iso, y, "gdp")), g(iso, y, "lev"), g(iso, y, "ltd"), g(iso, y, "noncore"),
                   g(iso, y, "unemp"), diff(iso, y, lambda i, yy: g(i, yy, "unemp"), 1), growth(iso, y, "xrusd"),
                   g(iso, y, "crisisJST"),
                   None if all(v is None for v in nxt) else (1.0 if any(v == 1 for v in nxt) else 0.0),
                   ",".join(applied.get((iso, y), []))]
            feats.append(["" if v is None else (f"{v:.6g}" if isinstance(v, float) else v) for v in row])
    write_csv(os.path.join(JST, "features.csv"), FH, feats)
    print(f"rows {len(data)}, countries {len(isos)}, features {len(feats)} x {len(FH)}")


if __name__ == "__main__":
    main()
