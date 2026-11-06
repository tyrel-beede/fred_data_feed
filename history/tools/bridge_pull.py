#!/usr/bin/env python3
"""US bridge from the JST Macrohistory Database (annual, 1870–2020) to the live FRED feed (2010–today).

The JST layer ends in 2020. The dials feed starts in late 2020. This script pulls the FRED series that carry the same
concepts as the JST columns, from 2010 so that the 2016–2020 overlap can be checked, aggregates them to calendar years,
and writes a comparison against the JST values over the overlap. Nothing is spliced automatically: the overlap check is
the evidence for how each series should be joined (ratio splice for indices, level join for rates and ratios), and the
join rules live in history/jst/field_map.csv once confirmed.

Outputs: history/bridge/us/<SERIES>.csv      raw FRED observations since 2010 (date,value)
         history/bridge/us_annual.csv        calendar-year aggregates (mean for rates/indices/levels, sum for flows)
         history/bridge/us_overlap_check.csv JST value, bridge value, ratio and difference for 2016–2020
Needs FRED_API_KEY (GitHub Actions secret). Run from the repo root: python3 history/tools/bridge_pull.py
"""
import csv, json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "history", "bridge")
START = "2010-01-01"

# FRED series -> (JST column it bridges, annual aggregation, scale to the JST unit, note)
BRIDGE = {
    "DGS10":          ("ltrate",   "mean", 1.0,    "10-year Treasury constant maturity, daily; JST ltrate is percent"),
    "TB3MS":          ("stir",     "mean", 1.0,    "3-month Treasury bill secondary market, monthly; JST stir is percent"),
    "CPIAUCSL":       ("cpi",      "mean", None,   "CPI-U all items, 1982-84=100; JST cpi has its own base -> ratio splice"),
    "UNRATE":         ("unemp",    "mean", 1.0,    "civilian unemployment rate, monthly, percent"),
    "GDPA":           ("gdp",      "last", 1.0,    "nominal GDP, annual, billions USD"),
    "GFDEGDQ188S":    ("debtgdp",  "mean", 0.01,   "federal debt / GDP, quarterly, percent -> JST ratio"),
    "FYFR":           ("revenue",  "last", 1e-3,   "federal receipts, fiscal year, millions USD -> billions"),
    "FYONET":         ("expenditure", "last", 1e-3, "federal outlays, fiscal year, millions USD -> billions"),
    "M2SL":           ("money",    "mean", 1.0,    "M2, monthly, billions USD"),
    "BOGMBASE":       ("narrowm",  "mean", 1.0,    "monetary base, monthly, billions USD as FRED reports it; JST US narrow money is the monetary base (doc pp. 193-194)"),
    "CSUSHPISA":      ("hpnom",    "mean", None,   "Case-Shiller national index, Jan 2000=100 -> ratio splice"),
    "IEABC":          ("ca",       "sum",  1e-3,   "balance on current account, quarterly, millions USD -> billions"),
    "A939RX0Q048SBEA": ("rgdpmad", "mean", None,   "real GDP per capita, chained 2017 USD -> ratio splice to Maddison 1990 international dollars"),
    "TOTLL":          ("tloans",   "mean", 1.0,    "loans and leases in bank credit, all commercial banks, billions; concept check pending"),
    "HHMSDODNS":      ("tmort",    "mean", 1e-3,   "household mortgage debt, quarterly, millions -> billions; concept check pending"),
    "GPDIC1":         (None,       "mean", None,   "real gross private domestic investment (for iy, with GDPC1)"),
    "GDPC1":          (None,       "mean", None,   "real GDP (denominator for iy)"),
}


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode()
        except Exception as e:  # noqa
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def main():
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        print("FRED_API_KEY not set; nothing pulled", file=sys.stderr)
        return 1
    os.makedirs(os.path.join(OUT, "us"), exist_ok=True)
    annual = {}  # (year) -> {series: value}
    for sid, (col, agg, scale, note) in BRIDGE.items():
        url = ("https://api.stlouisfed.org/fred/series/observations?"
               + urllib.parse.urlencode({"series_id": sid, "api_key": key, "file_type": "json",
                                         "observation_start": START}))
        obs = json.loads(get(url))["observations"]
        rows = [(o["date"], float(o["value"])) for o in obs if o["value"] not in (".", "")]
        with open(os.path.join(OUT, "us", f"{sid}.csv"), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["date", "value"]); w.writerows(rows)
        byy = {}
        for d, v in rows:
            byy.setdefault(int(d[:4]), []).append(v)
        for y, vs in byy.items():
            if agg == "mean":
                val = sum(vs) / len(vs)
            elif agg == "sum":
                val = sum(vs)
            else:
                val = vs[-1]
            annual.setdefault(y, {})[sid] = val
        time.sleep(0.25)
    years = sorted(annual)
    sids = list(BRIDGE)
    with open(os.path.join(OUT, "us_annual.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["year"] + sids)
        for y in years:
            w.writerow([y] + [f"{annual[y][s]:.6g}" if s in annual[y] else "" for s in sids])
    # overlap check against JST 2016-2020
    jst = {}
    with open(os.path.join(ROOT, "history", "jst", "jst_r6.csv")) as f:
        for r in csv.DictReader(f):
            if r["iso"] == "USA":
                jst[int(r["year"])] = r
    with open(os.path.join(OUT, "us_overlap_check.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["series", "jst_column", "year", "jst_value", "bridge_value_scaled", "ratio_jst_over_bridge", "difference", "note"])
        for sid, (col, agg, scale, note) in BRIDGE.items():
            if col is None:
                continue
            for y in range(2016, 2021):
                jv = jst.get(y, {}).get(col, "")
                bv = annual.get(y, {}).get(sid)
                if jv == "" or bv is None:
                    continue
                jv = float(jv)
                bs = bv * scale if scale else bv
                w.writerow([sid, col, y, f"{jv:.6g}", f"{bs:.6g}", f"{jv / bs:.6g}" if bs else "", f"{jv - bs:.6g}", note])
    print(f"bridge: {len(sids)} series, years {years[0]}–{years[-1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
