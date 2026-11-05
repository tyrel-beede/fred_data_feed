#!/usr/bin/env python3
"""The physical layer, first slice: energy and emissions as the thermodynamic footprint of activity.

Inputs (not stored in this repository; fetched as shallow clones of Our World in Data's GitHub repositories):
  owid/co2-data    owid-co2-data.csv     fossil CO2 by country, annual, from 1750 (Global Carbon Budget), with
                                         primary energy consumption (EIA international), GDP (Maddison), population
  owid/energy-data owid-energy-data.csv  primary energy consumption, fossil fuel production and consumption by fuel,
                                         electricity generation (EIA, Energy Institute, Ember)
Outputs:
  history/physical/owid_extract.csv   the 18 JST countries only, the columns used, with the source commit recorded
  history/physical/physical_features.csv  derived per country-year (provenance: derived, this script):
    co2_growth_1y, co2_growth_3y        fossil CO2 growth (annualized over 3y)
    rgdp_growth_3y                      real GDP growth (Maddison per-capita x JST population), annualized over 3y
    energy_footprint_gap_3y             co2_growth_3y - rgdp_growth_3y: the thermodynamic footprint of the boom
    co2_per_rgdp, d3_co2_intensity      carbon intensity of output and its 3-year change
    energy_growth_3y, energy_gap_3y     the same with primary energy (1965 on)
    fossil_prod_growth_3y               coal+oil+gas production growth (1900 on, where produced)
    fuel_self_sufficiency               fossil production / fossil consumption (1965 on)
    coal_share_co2, oil_share_co2       fuel mix of emissions (the coal->oil->gas transitions)
Usage: python3 -I history/tools/physical_build.py <path to owid/co2-data clone> <path to owid/energy-data clone>
"""
import csv, os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "history", "physical")
ISOS = {"AUS", "BEL", "CAN", "CHE", "DEU", "DNK", "ESP", "FIN", "FRA", "GBR", "IRL", "ITA", "JPN", "NLD", "NOR", "PRT", "SWE", "USA"}
CO2_COLS = ["co2", "coal_co2", "oil_co2", "gas_co2", "cement_co2", "flaring_co2", "primary_energy_consumption", "energy_per_gdp", "gdp", "population"]
EN_COLS = ["primary_energy_consumption", "fossil_fuel_consumption", "coal_production", "oil_production", "gas_production",
           "coal_consumption", "oil_consumption", "gas_consumption", "electricity_generation", "fossil_share_energy",
           "nuclear_share_energy", "renewables_share_energy"]


def commit(path):
    try:
        return subprocess.check_output(["git", "-C", path, "rev-parse", "HEAD"], text=True).strip()
    except Exception:  # noqa
        return "unknown"


def num(v):
    try:
        return float(v) if v not in ("", None) else np.nan
    except ValueError:
        return np.nan


def main():
    co2_dir, en_dir = sys.argv[1], sys.argv[2]
    os.makedirs(OUT, exist_ok=True)
    rows = {}
    for r in csv.DictReader(open(os.path.join(co2_dir, "owid-co2-data.csv"))):
        if r["iso_code"] in ISOS:
            k = (r["iso_code"], int(r["year"]))
            rows[k] = {f"co2ds_{c}": num(r.get(c)) for c in CO2_COLS}
    for r in csv.DictReader(open(os.path.join(en_dir, "owid-energy-data.csv"))):
        if r["iso_code"] in ISOS:
            k = (r["iso_code"], int(r["year"]))
            rows.setdefault(k, {}).update({f"en_{c}": num(r.get(c)) for c in EN_COLS})
    cols = [f"co2ds_{c}" for c in CO2_COLS] + [f"en_{c}" for c in EN_COLS]
    with open(os.path.join(OUT, "owid_extract.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["iso", "year"] + cols)
        for (i, y) in sorted(rows):
            w.writerow([i, y] + ["" if np.isnan(rows[(i, y)].get(c, np.nan)) else f"{rows[(i, y)][c]:.6g}" for c in cols])
    with open(os.path.join(OUT, "owid_extract.provenance.json"), "w") as f:
        f.write('{\n "source_repos": {"owid/co2-data": "%s", "owid/energy-data": "%s"},\n' % (commit(co2_dir), commit(en_dir)))
        f.write(' "retrieved": "2026-11-04",\n "license": "Our World in Data processing CC BY 4.0; underlying: Global Carbon Budget (CC BY 4.0), U.S. EIA international data (public domain), Energy Institute Statistical Review (free with attribution), Ember (CC BY 4.0), Maddison Project Database 2023 (CC BY 4.0)",\n'
                ' "provenance_class": "measured (compiled emissions and energy statistics; early-decade emissions are reconstructed from fuel production records)"\n}\n')

    # derived features against the JST real GDP (rgdpmad x pop)
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}

    def g(i, y, k):
        r = rows.get((i, y))
        return np.nan if r is None else r.get(k, np.nan)

    def rgdp(i, y):
        r = jst.get((i, y))
        if r is None or r.get("rgdpmad") is None or r.get("pop") is None:
            return np.nan
        return float(r["rgdpmad"]) * float(r["pop"])

    def ann_growth(fn, i, y, n):
        a, b = fn(i, y), fn(i, y - n)
        return np.nan if np.isnan(a) or np.isnan(b) or b <= 0 or a <= 0 else (a / b) ** (1.0 / n) - 1

    # oil prices since 1861 (OWID grapher CSV pulled by the workflow): current US$ per cubic metre -> per barrel,
    # deflated by the US CPI from the JST sheet (1990=100); real price and its changes are the same for every country,
    # the exposure differs (fuel self-sufficiency), which the learner can combine
    oil_nom = {}
    oil_path = os.path.join(OUT, "raw", "EI-OIL-PRICE-1861", "crude-oil-prices.csv")
    if os.path.exists(oil_path):
        rd = csv.DictReader(open(oil_path))
        vcol = [c for c in rd.fieldnames if c not in ("Entity", "Code", "Year", "entity", "code", "year")][0]
        for r in rd:
            try:
                oil_nom[int(r.get("Year") or r.get("year"))] = float(r[vcol]) / 6.2898
            except (ValueError, TypeError):
                pass
    us_cpi = {y: float(jst[("USA", y)]["cpi"]) for y in range(1870, 2021) if ("USA", y) in jst and jst[("USA", y)].get("cpi") is not None}
    oil_real = {y: oil_nom[y] / us_cpi[y] * 100 for y in oil_nom if y in us_cpi}
    def oil_chg(y, n):
        a, b = oil_real.get(y), oil_real.get(y - n)
        return np.nan if a is None or b is None or b <= 0 else a / b - 1
    FH = ["iso", "year", "co2_growth_1y", "co2_growth_3y", "rgdp_growth_3y", "energy_footprint_gap_3y", "gap_anom_3y",
          "co2_per_rgdp", "d3_co2_intensity", "energy_growth_3y", "energy_gap_3y", "fossil_prod_growth_3y",
          "fuel_self_sufficiency", "coal_share_co2", "oil_share_co2",
          "oil_real_price", "oil_real_change_1y", "oil_real_change_3y", "oil_shock_1y", "oil_change_x_exposure"]
    out = []
    gap_hist = {}  # (iso, year) -> gap, for the trailing-10-year anomaly (efficiency trends make the raw gap drift)
    for i in sorted(ISOS):
        for y in range(1870, 2021):
            co2 = lambda ii, yy: g(ii, yy, "co2ds_co2")
            en = lambda ii, yy: g(ii, yy, "co2ds_primary_energy_consumption")
            prod = lambda ii, yy: (g(ii, yy, "en_coal_production") if not np.isnan(g(ii, yy, "en_coal_production")) else 0.0) + \
                                  (g(ii, yy, "en_oil_production") if not np.isnan(g(ii, yy, "en_oil_production")) else 0.0) + \
                                  (g(ii, yy, "en_gas_production") if not np.isnan(g(ii, yy, "en_gas_production")) else 0.0) \
                                  if not all(np.isnan(g(ii, yy, c)) for c in ("en_coal_production", "en_oil_production", "en_gas_production")) else np.nan
            cg1, cg3, rg3 = ann_growth(co2, i, y, 1), ann_growth(co2, i, y, 3), ann_growth(rgdp, i, y, 3)
            inten = lambda ii, yy: (co2(ii, yy) / rgdp(ii, yy)) if not np.isnan(co2(ii, yy)) and not np.isnan(rgdp(ii, yy)) and rgdp(ii, yy) > 0 else np.nan
            eg3 = ann_growth(en, i, y, 3)
            fp = g(i, y, "en_fossil_fuel_consumption")
            pr = prod(i, y)
            c, cc, oc = co2(i, y), g(i, y, "co2ds_coal_co2"), g(i, y, "co2ds_oil_co2")
            gap = np.nan if np.isnan(cg3) or np.isnan(rg3) else cg3 - rg3
            gap_hist[(i, y)] = gap
            past = [gap_hist.get((i, yy), np.nan) for yy in range(y - 10, y)]
            past = [v for v in past if not np.isnan(v)]
            anom = np.nan if np.isnan(gap) or len(past) < 6 else gap - float(np.mean(past))
            row = [i, y, cg1, cg3, rg3, gap, anom,
                   inten(i, y),
                   np.nan if np.isnan(inten(i, y)) or np.isnan(inten(i, y - 3)) or inten(i, y - 3) == 0 else inten(i, y) / inten(i, y - 3) - 1,
                   eg3, np.nan if np.isnan(eg3) or np.isnan(rg3) else eg3 - rg3,
                   ann_growth(prod, i, y, 3),
                   np.nan if np.isnan(fp) or fp <= 0 or np.isnan(pr) else pr / fp,
                   np.nan if np.isnan(c) or c <= 0 or np.isnan(cc) else cc / c,
                   np.nan if np.isnan(c) or c <= 0 or np.isnan(oc) else oc / c,
                   oil_real.get(y, np.nan), oil_chg(y, 1), oil_chg(y, 3),
                   (np.nan if np.isnan(oil_chg(y, 1)) else (1.0 if oil_chg(y, 1) >= 0.40 else 0.0)),
                   (np.nan if np.isnan(oil_chg(y, 1)) or np.isnan(fp) or fp <= 0 or np.isnan(pr) else oil_chg(y, 1) * max(-1.0, min(1.0, 1.0 - pr / fp)))]  # importer +, exporter -, self-sufficient 0
            out.append(["" if (isinstance(v, float) and np.isnan(v)) else (f"{v:.6g}" if isinstance(v, float) else v) for v in row])
    with open(os.path.join(OUT, "physical_features.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(FH); w.writerows(out)
    print(f"extract {len(rows)} rows; features {len(out)} rows x {len(FH)}; oil price years {len(oil_real)}")


if __name__ == "__main__":
    main()
