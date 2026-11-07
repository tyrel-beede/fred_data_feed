#!/usr/bin/env python3
"""The physical layer, second slice: technology diffusion (the transfer function) and materials (the mining problem).

Inputs (raw files pulled by physical_pull.py in the workflow):
  history/physical/raw/CHAT/FinalCHAT_72909.csv      Comin & Hobijn, Cross-country Historical Adoption of Technology
                                                     (NBER w15319): adoption levels of >100 technologies, 150+ countries,
                                                     1750-2008; provenance: counted (units shipped, km built, kWh,
                                                     subscribers), compiled from national and league statistics
  history/physical/raw/USGS-DS140/*.xlsx             USGS Data Series 140: US production, apparent consumption, unit
                                                     value nominal and real (98$/t), world production, 1900-; provenance:
                                                     measured/counted (mine and smelter returns), prices are averages
  history/physical/raw/FRED-PHYSICAL/PPIACO.csv       all-commodity producer price index, monthly 1913- (FRED)
  history/physical/owid_extract.csv                   fossil CO2 (first slice) for the electricity/CO2 transfer ratio
  history/jst/jst_r6.csv (+overrides)                 population (per-capita), US CPI (deflator)

Outputs (all derived, this script; every value computable at year t from data dated <= t):
  history/physical/chat_extract.csv        the 18 JST countries x the technologies used (as published, no fill)
  history/physical/usgs_extract.csv        the commodity basket's real unit value and world production by year
  history/physical/diffusion_features.csv  per country-year:
    tech_growth_3y       median across technologies of the per-capita log adoption growth per year, t vs the latest
                         observation in [t-5, t-2] (post-inception only: >= 10 years after the first positive value)
    tech_accel_3y        median change of that growth against its value 3-5 years earlier (S-curve position)
    tech_max_growth_3y   the fastest-growing technology's pace (the era's lead technology)
    tech_n               number of technologies behind the medians (coverage)
    tech_frontier_gap    median over technologies of log per-capita level minus the JST-18 maximum at t (distance to
                         the frontier; 0 = the leader)
    rank_tech_growth_3y  percentile rank of tech_growth_3y among the JST 18 at t (the relative diffusion race)
    rail_growth_3y, elec_growth_3y, car_growth_3y, phone_growth_3y   the same growth for the four long lead series
    elec_per_co2_growth_3y   growth of electricity output per tonne of fossil CO2 (the transfer ratio: how much of the
                         energy flow becomes the highest-grade carrier)
  history/physical/materials_features.csv  per year (global; the same for every country at t):
    metals_real_price_1y, metals_real_price_3y   median across the base-metal basket of the log change in real unit
                         value (copper, lead, zinc, tin, nickel, aluminum, iron ore)
    metals_real_price_anom   median across the basket of log real unit value minus its own history-to-t median
                         (>= 10 years): the scarcity signal, the price the mining problem is clearing at
    world_metals_prod_3y     median across the basket (plus pig iron) of world production log growth per year over 3y
    world_metals_prod_accel  that growth minus the same three years earlier
    gold_real_3y         3-year log change of gold's real unit value
    ppi_commod_real_1y, ppi_commod_real_3y   log change of the all-commodity PPI deflated by the US CPI (1913-)
  history/physical/jacks_features.csv      per year (global): Jacks's 42 real commodity prices 1850-2025 as an equal-weight
    index (1- and 3-year log changes, the index against its own history), breadth and dispersion of 3-year changes,
    the energy, metals and grains groups, and grown-minus-in-the-ground (see build_jacks)
Usage: python3 -I history/tools/physical_build2.py
"""
import csv, json, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
PH = os.path.join(ROOT, "history", "physical")
RAW = os.path.join(PH, "raw")
ISOS = ["AUS", "BEL", "CAN", "CHE", "DEU", "DNK", "ESP", "FIN", "FRA", "GBR", "IRL", "ITA", "JPN", "NLD", "NOR", "PRT", "SWE", "USA"]
CHAT_NAMES = {"AUS": "Australia", "BEL": "Belgium", "CAN": "Canada", "CHE": "Switzerland", "DEU": "Germany", "DNK": "Denmark",
              "ESP": "Spain", "FIN": "Finland", "FRA": "France", "GBR": "United Kingdom", "IRL": "Ireland", "ITA": "Italy",
              "JPN": "Japan", "NLD": "Netherlands", "NOR": "Norway", "PRT": "Portugal", "SWE": "Sweden", "USA": "United States"}
TECHS = ["railline", "telegram", "telephone", "elecprod", "vehicle_car", "vehicle_com", "radio", "tv", "mail", "aviationpkm",
         "shipton_all", "ag_tractor", "fert_total", "cellphone", "computer", "internetuser"]
LEAD = {"rail_growth_3y": "railline", "elec_growth_3y": "elecprod", "car_growth_3y": "vehicle_car", "phone_growth_3y": "telephone"}
INCEPTION_YEARS = 10      # a technology counts only >= 10 years after its first positive value in that country
BREAK_LOGJUMP = 1.0       # a one-year per-capita log jump above this is a unit or territory break: no growth across it
# USGS basket: workbook file -> sheet title (None = first sheet)
PRICE_BASKET = {"copper": ("ds140-copper-2020.xlsx", None), "lead": ("ds140-lead-2021.xlsx", None), "zinc": ("ds140-zinc-2022.xlsx", None),
                "tin": ("ds140-tin-2021.xlsx", None), "nickel": ("ds140-nickel-2019.xlsx", "Nickel"), "aluminum": ("ds140-aluminum-2021.xlsx", None),
                "iron_ore": ("ds140-iron_ore-2021.xlsx", None)}
PROD_EXTRA = {"pig_iron": ("ds140-iron-steel-2021.xlsx", "Pig Iron")}
GOLD = ("ds140-gold-2022.xlsx", None)


def nan(v):
    try:
        return float(v) if v not in ("", None, "NA", "W", "--", "—") else np.nan
    except ValueError:
        return np.nan


# ------------------------------------------------------------------------------------------------------- CHAT
def build_diffusion(jst, co2):
    path = os.path.join(RAW, "CHAT", "FinalCHAT_72909.csv")
    if not os.path.exists(path):
        print("CHAT file missing; skipping diffusion"); return None
    name_to_iso = {v: k for k, v in CHAT_NAMES.items()}
    raw = {}  # (iso, year) -> {tech: value}
    for r in csv.DictReader(open(path)):
        iso = name_to_iso.get(r["country_name"])
        if iso is None:
            continue
        raw[(iso, int(r["year"]))] = {t: nan(r.get(t)) for t in TECHS}
    with open(os.path.join(PH, "chat_extract.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["iso", "year"] + TECHS)
        for k in sorted(raw):
            w.writerow([k[0], k[1]] + ["" if np.isnan(raw[k][t]) else f"{raw[k][t]:.6g}" for t in TECHS])

    def pop(i, y):
        r = jst.get((i, y))
        return np.nan if r is None or r.get("pop") in (None, "") else float(r["pop"])

    # per-capita log levels, observed only (no fill), with inception year and break flags
    lp = {}       # (iso, tech) -> {year: log per-capita}
    first = {}    # (iso, tech) -> first year with a positive value
    for (i, y), d in raw.items():
        for t, v in d.items():
            if np.isnan(v) or v <= 0:
                continue
            first[(i, t)] = min(first.get((i, t), y), y)  # inception from the raw series, before any population join
            p = pop(i, y)
            if np.isnan(p) or p <= 0:
                continue
            lp.setdefault((i, t), {})[y] = float(np.log(v / p))
    breaks = {}   # (iso, tech) -> set of years y where the jump from y-1 to y exceeds the threshold
    for k, s in lp.items():
        b = set()
        for y in s:
            if y - 1 in s and abs(s[y] - s[y - 1]) > BREAK_LOGJUMP:
                b.add(y)
        breaks[k] = b

    def growth(i, t, y):
        """per-year log growth from the latest observation in [y-5, y-2] to y; NaN if not post-inception or across a break."""
        s = lp.get((i, t))
        if s is None or y not in s or y - first.get((i, t), y) < INCEPTION_YEARS:
            return np.nan
        for s0 in (y - 2, y - 3, y - 4, y - 5):
            if s0 in s:
                if any(b in breaks[(i, t)] for b in range(s0 + 1, y + 1)):
                    return np.nan
                return (s[y] - s[s0]) / (y - s0)
        return np.nan

    years = range(1870, 2021)
    G = {(i, t, y): growth(i, t, y) for i in ISOS for t in TECHS for y in years}
    # frontier (JST-18 max of the log per-capita level) per tech-year
    frontier = {}
    for t in TECHS:
        for y in years:
            vals = [lp[(i, t)][y] for i in ISOS if (i, t) in lp and y in lp[(i, t)] and y - first[(i, t)] >= INCEPTION_YEARS]
            frontier[(t, y)] = (max(vals), len(vals)) if len(vals) >= 5 else (np.nan, len(vals))

    def co2v(i, y):
        return co2.get((i, y), np.nan)

    rows = {}
    for i in ISOS:
        for y in years:
            gs = {t: G[(i, t, y)] for t in TECHS if not np.isnan(G[(i, t, y)])}
            # acceleration: growth now minus growth at the latest year in [y-5, y-3] where it was defined
            acc = []
            for t in gs:
                for s0 in (y - 3, y - 4, y - 5):
                    g0 = G.get((i, t, s0), np.nan)
                    if not np.isnan(g0):
                        acc.append(gs[t] - g0); break
            gaps = []
            for t in TECHS:
                fr, n = frontier[(t, y)]
                s = lp.get((i, t))
                if not np.isnan(fr) and s is not None and y in s and y - first[(i, t)] >= INCEPTION_YEARS:
                    gaps.append(s[y] - fr)
            ratio = lambda yy: (np.nan if (i, "elecprod") not in lp or yy not in lp[(i, "elecprod")] or np.isnan(co2v(i, yy)) or co2v(i, yy) <= 0
                                else lp[(i, "elecprod")][yy] + np.log(pop(i, yy)) - np.log(co2v(i, yy)))
            r0, r3 = ratio(y), ratio(y - 3)
            rows[(i, y)] = {
                "tech_growth_3y": float(np.median(list(gs.values()))) if len(gs) >= 2 else np.nan,
                "tech_accel_3y": float(np.median(acc)) if len(acc) >= 2 else np.nan,
                "tech_max_growth_3y": max(gs.values()) if len(gs) >= 2 else np.nan,
                "tech_n": float(len(gs)),
                "tech_frontier_gap": float(np.median(gaps)) if len(gaps) >= 2 else np.nan,
                "rank_tech_growth_3y": np.nan,
                **{name: G[(i, tech, y)] for name, tech in LEAD.items()},
                "elec_per_co2_growth_3y": np.nan if np.isnan(r0) or np.isnan(r3) else (r0 - r3) / 3.0}
    for y in years:
        vals = {i: rows[(i, y)]["tech_growth_3y"] for i in ISOS if not np.isnan(rows[(i, y)]["tech_growth_3y"])}
        for i, v in vals.items():
            others = [o for j, o in vals.items() if j != i]
            if len(others) >= 5:
                rows[(i, y)]["rank_tech_growth_3y"] = sum(1 for o in others if o < v) / len(others)
    cols = ["tech_growth_3y", "tech_accel_3y", "tech_max_growth_3y", "tech_n", "tech_frontier_gap", "rank_tech_growth_3y",
            "rail_growth_3y", "elec_growth_3y", "car_growth_3y", "phone_growth_3y", "elec_per_co2_growth_3y"]
    with open(os.path.join(PH, "diffusion_features.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["iso", "year"] + cols)
        for i in ISOS:
            for y in years:
                w.writerow([i, y] + ["" if np.isnan(rows[(i, y)][c]) else f"{rows[(i, y)][c]:.6g}" for c in cols])
    nb = sum(len(b) for b in breaks.values())
    cov = {c: int(sum(1 for k in rows if not np.isnan(rows[k][c]))) for c in cols}
    print(f"diffusion: {len(rows)} rows; breaks flagged {nb}; coverage {cov}")
    return {"rows": len(rows), "breaks_flagged": nb, "coverage": cov, "techs": TECHS, "inception_years": INCEPTION_YEARS, "break_logjump": BREAK_LOGJUMP}


# ------------------------------------------------------------------------------------------------------- USGS + FRED
def parse_ds140(path, sheet=None):
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    hdr, rows = None, []
    for row in ws.iter_rows(values_only=True):
        vals = [("" if c is None else str(c).strip()) for c in row]
        if hdr is None:
            if vals and vals[0].lower() == "year":
                hdr = [re.sub(r"\s+", " ", v) for v in vals]
            continue
        if vals and re.fullmatch(r"\d{4}", vals[0]):
            rows.append(dict(zip(hdr, vals)))
    if hdr is None:
        raise ValueError(f"no Year header in {path} {sheet}")
    real = next((h for h in hdr if "98" in h and "unit value" in h.lower()), None)
    world = next((h for h in hdr if h.lower().startswith("world")), None)
    out = {}
    for r in rows:
        y = int(r["Year"])
        out[y] = (nan(r.get(real)) if real else np.nan, nan(r.get(world)) if world else np.nan)
    return out, real, world


def build_materials(jst):
    d = os.path.join(RAW, "USGS-DS140")
    if not os.path.isdir(d):
        print("USGS directory missing; skipping materials"); return None
    series, meta = {}, {}
    for name, (fn, sheet) in {**PRICE_BASKET, **PROD_EXTRA, "gold": GOLD}.items():
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            print("  missing", fn); continue
        series[name], real_col, world_col = parse_ds140(p, sheet)
        meta[name] = {"file": f"history/physical/raw/USGS-DS140/{fn}", "sheet": sheet or "first", "real_unit_value_column": real_col, "world_production_column": world_col}
    years = range(1900, 2023)
    with open(os.path.join(PH, "usgs_extract.csv"), "w", newline="") as f:
        w = csv.writer(f); names = sorted(series)
        w.writerow(["year"] + [f"{n}_real_uv_98usd_t" for n in names] + [f"{n}_world_production_t" for n in names])
        for y in years:
            w.writerow([y] + ["" if np.isnan(series[n].get(y, (np.nan, np.nan))[0]) else f"{series[n][y][0]:.6g}" for n in names]
                       + ["" if np.isnan(series[n].get(y, (np.nan, np.nan))[1]) else f"{series[n][y][1]:.6g}" for n in names])
    # FRED PPIACO monthly -> annual mean, deflated by the US CPI (JST, 1990=100)
    ppi = {}
    pp = os.path.join(RAW, "FRED-PHYSICAL", "PPIACO.csv")
    if os.path.exists(pp):
        acc = {}
        for r in csv.DictReader(open(pp)):
            try:
                acc.setdefault(int(r["date"][:4]), []).append(float(r["value"]))
            except (ValueError, KeyError):
                pass
        ppi = {y: float(np.mean(v)) for y, v in acc.items() if len(v) >= 6}
    us_cpi = {y: float(jst[("USA", y)]["cpi"]) for y in range(1870, 2021) if ("USA", y) in jst and jst[("USA", y)].get("cpi") not in (None, "")}
    ppi_real = {y: ppi[y] / us_cpi[y] for y in ppi if y in us_cpi}

    def lchg(s, y, n):
        a, b = s.get(y, np.nan), s.get(y - n, np.nan)
        return np.nan if np.isnan(a) or np.isnan(b) or a <= 0 or b <= 0 else float(np.log(a / b))

    price = {n: {y: v[0] for y, v in series[n].items()} for n in PRICE_BASKET if n in series}
    prod = {n: {y: v[1] for y, v in series[n].items()} for n in list(PRICE_BASKET) + list(PROD_EXTRA) if n in series}
    gold = {y: v[0] for y, v in series.get("gold", {}).items()}
    rows = []
    for y in years:
        p1 = [lchg(price[n], y, 1) for n in price]; p3 = [lchg(price[n], y, 3) for n in price]
        anom = []
        for n in price:
            hist = [np.log(v) for yy, v in price[n].items() if yy <= y and not np.isnan(v) and v > 0]
            cur = price[n].get(y, np.nan)
            if len(hist) >= 10 and not np.isnan(cur) and cur > 0:
                anom.append(float(np.log(cur) - np.median(hist)))
        g3 = [lchg(prod[n], y, 3) / 3.0 for n in prod]
        g3p = [lchg(prod[n], y - 3, 3) / 3.0 for n in prod]
        accel = [a - b for a, b in zip(g3, g3p) if not np.isnan(a) and not np.isnan(b)]
        def med(v, k=3):
            v = [x for x in v if not np.isnan(x)]
            return float(np.median(v)) if len(v) >= k else np.nan
        rows.append([y, med(p1), med(p3), med(anom), med(g3), med(accel), lchg(gold, y, 3), lchg(ppi_real, y, 1), lchg(ppi_real, y, 3)])
    cols = ["metals_real_price_1y", "metals_real_price_3y", "metals_real_price_anom", "world_metals_prod_3y", "world_metals_prod_accel",
            "gold_real_3y", "ppi_commod_real_1y", "ppi_commod_real_3y"]
    with open(os.path.join(PH, "materials_features.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["year"] + cols)
        for r in rows:
            w.writerow([r[0]] + ["" if np.isnan(v) else f"{v:.6g}" for v in r[1:]])
    cov = {c: int(sum(1 for r in rows if not np.isnan(r[k + 1]))) for k, c in enumerate(cols)}
    print(f"materials: {len(rows)} years; coverage {cov}")
    return {"years": len(rows), "coverage": cov, "basket": meta, "ppi_years": len(ppi_real)}


# ------------------------------------------------------------------------------------------------------- Jacks
JACKS = os.path.join(RAW, "JACKS-COMMODITIES", "Real-commodity-prices-1850-2025.xlsx")


def build_jacks():
    """Jacks's real commodity prices (42 commodities, 1850-2025, deflated by the US CPI, 1900 = 100) -> per-year global
    features in history/physical/jacks_features.csv:
      jacks_real_index_1y, jacks_real_index_3y   log change of an equal-weight index (geometric mean of the commodities
                                                 available at both ends; the index itself starts 1850, Jacks's own 1900)
      jacks_anom                                 the equal-weight index against its own history to t (log, >= 10 years)
      jacks_breadth_3y                           share of commodities whose real price is higher than three years earlier
      jacks_dispersion_3y                        cross-commodity standard deviation of the 3-year log change
      jacks_energy_3y, jacks_metals_3y, jacks_grains_3y   group equal-weight indices, 3-year log change
      jacks_grown_vs_ground_3y                   3-year log change of the grown (grains, softs, animal products) index minus
                                                 the in-the-ground (energy, metals, minerals) index: the composition of a boom
    Every value at t uses prices of years <= t."""
    if not os.path.exists(JACKS):
        print("Jacks workbook missing; skipping"); return None
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(JACKS, read_only=True, data_only=True)
    rows = list(wb["Commodities"].iter_rows(values_only=True))
    groups, names = rows[0], rows[1]
    cols, g = [], None
    for j, (grp, nm) in enumerate(zip(groups, names)):
        if grp:
            g = str(grp).strip()
        if nm and str(nm).strip().lower() != "year":
            cols.append((j, g, str(nm).strip()))
    P = {}  # year -> {commodity: real price}
    for r in rows[2:]:
        if r[0] is None or not re.fullmatch(r"\d{4}", str(r[0])):
            continue
        y = int(r[0])
        P[y] = {nm: nan(r[j]) for j, g, nm in cols}
        P[y] = {k: v for k, v in P[y].items() if not np.isnan(v) and v > 0}
    grp_of = {nm: g for j, g, nm in cols}
    GROWN = {"Grains", "Softs", "Animal products"}; GROUND = {"Energy", "Metals", "Minerals"}
    years = sorted(P)

    def lchg(y, n, members=None):
        """mean log change over n years across commodities present at both ends (equal weight)."""
        if y - n not in P:
            return np.nan, 0
        ks = [k for k in P[y] if k in P[y - n] and (members is None or k in members)]
        if len(ks) < 3:
            return np.nan, len(ks)
        return float(np.mean([np.log(P[y][k] / P[y - n][k]) for k in ks])), len(ks)

    # chained equal-weight index from 1850 (log index = cumulative mean 1-year log changes)
    idx, lv = {}, 0.0
    for y in years:
        c, n = lchg(y, 1)
        if not np.isnan(c):
            lv += c
        idx[y] = lv
    out = []
    for y in years:
        i1, _ = lchg(y, 1); i3, n3 = lchg(y, 3)
        hist = [idx[yy] for yy in years if yy <= y]
        anom = idx[y] - float(np.median(hist)) if len(hist) >= 10 else np.nan
        ks3 = [k for k in P[y] if (y - 3) in P and k in P[y - 3]]
        chg = [np.log(P[y][k] / P[y - 3][k]) for k in ks3]
        breadth = float(np.mean([c > 0 for c in chg])) if len(chg) >= 10 else np.nan
        disp = float(np.std(chg)) if len(chg) >= 10 else np.nan
        e3, _ = lchg(y, 3, {k for k in grp_of if grp_of[k] == "Energy"})
        m3, _ = lchg(y, 3, {k for k in grp_of if grp_of[k] == "Metals"})
        gr3, _ = lchg(y, 3, {k for k in grp_of if grp_of[k] == "Grains"})
        grown, _ = lchg(y, 3, {k for k in grp_of if grp_of[k] in GROWN}); ground, _ = lchg(y, 3, {k for k in grp_of if grp_of[k] in GROUND})
        out.append([y, i1, i3, anom, breadth, disp, e3, m3, gr3, (np.nan if np.isnan(grown) or np.isnan(ground) else grown - ground), n3])
    cols_out = ["jacks_real_index_1y", "jacks_real_index_3y", "jacks_anom", "jacks_breadth_3y", "jacks_dispersion_3y",
                "jacks_energy_3y", "jacks_metals_3y", "jacks_grains_3y", "jacks_grown_vs_ground_3y", "jacks_n_3y"]
    with open(os.path.join(PH, "jacks_features.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["year"] + cols_out)
        for r in out:
            w.writerow([r[0]] + ["" if (isinstance(v, float) and np.isnan(v)) else (f"{v:.6g}" if isinstance(v, float) else v) for v in r[1:]])
    cov = {c: int(sum(1 for r in out if not (isinstance(r[k + 1], float) and np.isnan(r[k + 1])))) for k, c in enumerate(cols_out)}
    print(f"jacks: {len(out)} years, {len(cols)} commodities; coverage {cov}")
    return {"years": len(out), "commodities": [(g, nm) for j, g, nm in cols], "coverage": cov, "file": "history/physical/raw/JACKS-COMMODITIES/Real-commodity-prices-1850-2025.xlsx"}


def main():
    jst = {(r["iso"], int(r["year"])): r for r in load_jst(apply_overrides=True)}
    co2 = {}
    xp = os.path.join(PH, "owid_extract.csv")
    if os.path.exists(xp):
        for r in csv.DictReader(open(xp)):
            co2[(r["iso"], int(r["year"]))] = nan(r.get("co2ds_co2"))
    prov = {"built_by": "history/tools/physical_build2.py", "provenance_class": "derived",
            "diffusion": build_diffusion(jst, co2), "materials": build_materials(jst), "jacks": build_jacks()}
    json.dump(prov, open(os.path.join(PH, "physical_build2.provenance.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
