#!/usr/bin/env python3
"""Build the corporate-sector annual series for the US from the workflow's raw pulls (history/corporate/raw/):

  history/corporate/us_corporate_annual.csv   one row per year, every value computable at year end:
    nfcb_debt_gdp            nonfinancial corporate debt securities and loans (Q4 level) / nominal GDP (debt securities
                             alone when the loans series is absent; series_used.json says which)
    nfcb_equity_mv_gdp       corporate equities at market value (Q4 level) / nominal GDP
    nfcb_net_worth_growth_3y net worth, nominal, per year over three years
    nfcb_capex_gdp           capital expenditures (annual average of the quarterly flow) / nominal GDP
    nfcb_dividends_profits   net dividends paid / nonfinancial corporate profits after tax (annual averages)
    nfcb_liquid_assets_debt  liquid assets (Q4) / debt (Q4)
    corp_profits_gdp         BEA corporate profits with IVA and CCAdj (annual) / nominal GDP, 1929-
    cape                     Shiller's cyclically adjusted P/E, December value
    real_earnings_growth_1y, real_earnings_growth_3y   S&P composite real earnings (annual average), per year
    real_price_growth_3y     S&P composite real price (annual average), per year
    real_home_price_growth_3y   Shiller's real home price index (Figure 3.1 workbook; annual to 1952, monthly averaged after),
                             per year over three years; the whole series is in shiller_home_prices.csv
    earnings_yield_minus_long_rate   annual-average E/P (real) minus the long government rate, percentage points
    gw_ntis, gw_bm, gw_dfy, gw_svar  Goyal-Welch net equity issuance, book-to-market, default yield spread, stock
                             variance (when the workbook is present)
  Nominal GDP: FRED GDP (quarterly SAAR, annual average, billions -> millions) from 1947; the JST sheet's US nominal
  GDP (billions) before that. Units are taken from the series metadata the puller recorded (series_used.json).
Run: python3 -I history/tools/corporate_build.py
"""
import csv, json, os, re, sys, time, warnings
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jstlib import load_jst  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
CORP = os.path.join(ROOT, "history", "corporate")
RAW = os.path.join(CORP, "raw")


def read_fred(name):
    p = os.path.join(RAW, "FRED-Z1", f"{name}.csv")
    if not os.path.exists(p):
        return {}
    out = {}
    for r in csv.DictReader(open(p)):
        try:
            out[r["date"]] = float(r["value"])
        except (ValueError, KeyError):
            pass
    return out


def units_scale(meta, name):
    u = (meta.get(name, {}).get("units") or "").lower()
    if "billion" in u:
        return 1000.0  # -> millions
    if "thousand" in u:
        return 0.001
    return 1.0


def q4(series, y):
    for d in (f"{y}-10-01", f"{y}-12-01", f"{y}-12-31"):
        if d in series:
            return series[d]
    return np.nan


def annual_mean(series, y):
    v = [val for d, val in series.items() if d.startswith(str(y))]
    return float(np.mean(v)) if len(v) >= 2 else (v[0] if len(v) == 1 and not any(d.startswith(str(y)) and d[5:7] not in ("01",) for d in series) else np.nan)


def annual_value(series, y):
    v = [val for d, val in series.items() if d.startswith(str(y))]
    return v[0] if v else np.nan


def read_shiller():
    """Monthly rows from Shiller's workbook (sheet 'Data'): date, P, D, E, CPI, long rate, real P, real D, real E, CAPE."""
    d = os.path.join(RAW, "SHILLER")
    if not os.path.isdir(d):
        return {}
    files = [f for f in os.listdir(d) if f.lower().startswith("ie_data") and f.lower().endswith((".xls", ".xlsx"))]
    if not files:
        return {}
    files.sort(key=lambda f: ("yale" in f.lower(), f))  # a current workbook supplied by hand beats the stale Yale copy
    path = os.path.join(d, files[0])
    warnings.filterwarnings("ignore")
    rows = []
    try:
        if path.lower().endswith(".xlsx"):
            import openpyxl
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
            ws = wb["Data"] if "Data" in wb.sheetnames else wb.worksheets[0]
            rows = [list(r) for r in ws.iter_rows(values_only=True)]
        else:
            try:
                import xlrd
                wb = xlrd.open_workbook(path)
                ws = wb.sheet_by_name("Data") if "Data" in wb.sheet_names() else wb.sheet_by_index(0)
                rows = [ws.row_values(i) for i in range(ws.nrows)]
            except ImportError:  # no xlrd: convert the .xls with LibreOffice into a temporary folder and read that
                import subprocess, tempfile, openpyxl
                tmp = tempfile.mkdtemp(prefix="shiller_")
                subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", tmp, path], check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
                conv = os.path.join(tmp, os.path.splitext(os.path.basename(path))[0] + ".xlsx")
                wb = openpyxl.load_workbook(conv, read_only=True, data_only=True)
                ws = wb["Data"] if "Data" in wb.sheetnames else wb.worksheets[0]
                rows = [list(r) for r in ws.iter_rows(values_only=True)]
    except Exception as e:  # noqa
        print("shiller workbook unreadable:", e); return {}
    # header: the row that starts with 'Date'; columns by name
    hi = next((i for i, r in enumerate(rows) if r and str(r[0]).strip().lower() == "date"), None)
    if hi is None:
        return {}
    hdr = [str(c).strip().lower() if c is not None else "" for c in rows[hi]]
    def col(*names):
        for n in names:
            for j, h in enumerate(hdr):
                if h == n:
                    return j
        return None
    ci = {"p": col("p"), "d": col("d"), "e": col("e"), "cpi": col("cpi"), "rate": col("rate gs10", "rate"), "cape": col("cape", "p/e10")}
    out = {}
    for r in rows[hi + 1:]:
        try:
            dv = float(r[0])
        except (TypeError, ValueError):
            continue
        y = int(dv); m = int(round((dv - y) * 100))
        if m < 1 or m > 12:
            continue
        rec = {}
        for k, j in ci.items():
            if j is not None and j < len(r):
                try:
                    rec[k] = float(r[j])
                except (TypeError, ValueError):
                    rec[k] = np.nan
        out[(y, m)] = rec
    return out


def read_fig31():
    """Shiller's Figure 3.1 workbook (Data sheet): col A date (annual 1890-1952, then monthly as year.fraction), col B real
    home price index (1890 = 100), cols H/I the nominal home price index with its own date column, cols N/O the CPI.
    Returns {year: {"real_hpi": annual mean, "nominal_hpi": annual mean}} (annual rows as themselves, monthly averaged)."""
    path = os.path.join(RAW, "SHILLER", "Fig3-1_1.xls")
    if not os.path.exists(path):
        return {}
    import subprocess, tempfile, openpyxl
    warnings.filterwarnings("ignore")
    tmp = tempfile.mkdtemp(prefix="fig31_")
    subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", tmp, path], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    wb = openpyxl.load_workbook(os.path.join(tmp, "Fig3-1_1.xlsx"), read_only=True, data_only=True)
    rows = [list(r) for r in (wb["Data"] if "Data" in wb.sheetnames else wb.worksheets[0]).iter_rows(values_only=True)]
    acc = {}
    def add(key, dv, v):
        try:
            dv, v = float(dv), float(v)
        except (TypeError, ValueError):
            return
        acc.setdefault(int(dv), {}).setdefault(key, []).append(v)
    for r in rows[7:]:
        if len(r) > 1:
            add("real_hpi", r[0], r[1])
        if len(r) > 8:
            add("nominal_hpi", r[7], r[8])
    return {y: {k: float(np.mean(v)) for k, v in d.items()} for y, d in acc.items()}


def read_goyal_welch():
    d = os.path.join(RAW, "GOYAL-WELCH")
    if not os.path.isdir(d):
        return {}
    files = [f for f in os.listdir(d) if f.lower().endswith(".xlsx")]
    if not files:
        return {}
    import openpyxl
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(os.path.join(d, sorted(files)[-1]), read_only=True, data_only=True)
    ws = next((wb[s] for s in wb.sheetnames if "annual" in s.lower()), wb.worksheets[0])
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    # column names as the workbook spells them; the 2025 edition (Data2025.xlsx) writes book-to-market as "b/m"
    hdr = [str(c).strip().lower().replace("/", "") if c is not None else "" for c in rows[0]]
    out = {}
    for r in rows[1:]:
        try:
            y = int(float(r[0]))
        except (TypeError, ValueError):
            continue
        rec = {}
        for k in ("ntis", "bm", "dfy", "svar"):
            if k in hdr:
                try:
                    rec[k] = float(r[hdr.index(k)])
                except (TypeError, ValueError):
                    rec[k] = np.nan
        out[y] = rec
    return out


def build_sec_tables():
    """Reduce the SEC aggregates the puller keeps to two small tables for the live dials:
    sec_fsds_quarterly.csv  per period end (ddate): for each tag, the filer count and sum for the 3-month (qtrs=1),
                            year-to-date (qtrs=2,3) and annual (qtrs=4) rows with the most filers in any quarterly file;
                            10-Q cash-flow statements are year-to-date, so the June, September and December flows are
                            the qtrs=2/3/4 rows, and a single quarter's flow is the difference between successive ones
                            for the same filer set (not computed here)
    sec_13f_quarterly.csv   per period: filers, total value, issuers, top-10 and top-50 shares, Herfindahl, median
                            filer top-10 concentration, put/call value share"""
    d = os.path.join(RAW, "SEC-FSDS")
    best = {}
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if not fn.endswith("_aggregates.csv"):
                continue
            q = fn.replace("_aggregates.csv", "")
            mp = os.path.join(d, f"{q}_meta.json")
            ver = json.load(open(mp)).get("aggregator_version", 1) if os.path.exists(mp) else 1
            for r in csv.DictReader(open(os.path.join(d, fn))):
                sector = r.get("sector") or "all"  # aggregates before v3 are all filers
                k = (sector, r["ddate"], r["tag"], r["qtrs"])
                # for a (sector, period, tag) reported in several quarterly files (10-K originals, then 10-Q comparatives),
                # the file with the most filers; among equals, the one reduced by the newer aggregator
                if k not in best or (int(r["n_filers"]), ver) > (int(best[k]["n_filers"]), best[k]["aggregator_version"]):
                    best[k] = {**r, "sector": sector, "source_file": fn, "aggregator_version": ver}
        with open(os.path.join(CORP, "sec_fsds_quarterly.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["sector", "ddate", "tag", "qtrs", "n_filers", "sum_usd", "median_usd", "p90_usd", "source_file", "aggregator_version"])
            w.writeheader()
            for k in sorted(best):
                w.writerow({c: best[k][c] for c in w.fieldnames})
    d13 = os.path.join(RAW, "SEC-13F")
    rows = []
    if os.path.isdir(d13):
        from corporate_pull import qkey_13f, period_end_13f
        for fn in sorted((f for f in os.listdir(d13) if f.endswith("_summary.json")), key=lambda f: qkey_13f(f.replace("_summary.json", ""))):
            s_ = json.load(open(os.path.join(d13, fn)))
            name = s_.get("period") or fn.replace("_summary.json", "")
            # the holdings date: measured from the filings by aggregator v2 (report_period); for an older summary, the
            # quarter the set's name implies (a set holds the filings made in its quarter, about the quarter before)
            rows.append({"period": name, "period_end": s_.get("report_period") or period_end_13f(name),
                         "aggregator_version": s_.get("aggregator_version", 1), "n_filers": s_.get("n_filers"),
                         "total_value_usd": s_.get("total_value_reported"), "value_unit_detected": s_.get("value_unit_detected", "dollars (assumed)"),
                         "n_filers_unit_corrected": s_.get("n_filers_unit_corrected", ""), "value_share_unit_corrected": s_.get("value_share_unit_corrected", ""),
                         "n_filings_other_period": s_.get("n_filings_other_period", ""),
                         "n_issuers": s_.get("n_issuers_cusip"), "top10_issuer_share": s_.get("top10_issuer_share"),
                         "top50_issuer_share": s_.get("top50_issuer_share"), "hhi_issuers": s_.get("hhi_issuers"),
                         "median_filer_top10_share": s_.get("median_filer_top10_share"), "putcall_value_share": s_.get("putcall_value_share")})
        if rows:
            with open(os.path.join(CORP, "sec_13f_quarterly.csv"), "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"sec tables: {len(best)} fsds tag-period rows, {len(rows)} 13f periods")


def main():
    build_sec_tables()
    meta = {}
    mp = os.path.join(RAW, "FRED-Z1", "series_used.json")
    if os.path.exists(mp):
        meta = {m["key"]: m for m in json.load(open(mp))}
    S = {k: read_fred(k) for k, _ in meta.items()} if meta else {}
    for k in ("nfcb_debt", "nfcb_debt_securities_and_loans", "nfcb_equity_mv", "nfcb_net_worth", "nfcb_total_liabilities", "nfcb_capex", "nfcb_net_dividends",
              "nfcb_liquid_assets", "corp_profits_after_tax_q", "corp_profits_iva_ccadj_annual", "nfcb_profits_after_tax_q", "gdp_nominal_q"):
        S.setdefault(k, read_fred(k))
    sc = {k: units_scale(meta, k) for k in S}
    jst = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}

    def gdp_mn(y):
        g = annual_mean(S["gdp_nominal_q"], y) if S.get("gdp_nominal_q") else np.nan
        if not np.isnan(g):
            return g * sc["gdp_nominal_q"]
        r = jst.get(("USA", y))
        return float(r["gdp"]) * 1000.0 if r and r.get("gdp") not in (None, "") else np.nan  # JST: billions of dollars

    sh = read_shiller(); gw = read_goyal_welch(); hp = read_fig31()
    if hp:
        with open(os.path.join(CORP, "shiller_home_prices.csv"), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["year", "real_hpi_1890eq100", "nominal_hpi", "real_home_price_growth_1y", "real_home_price_growth_3y"])
            for y in sorted(hp):
                r0, r1, r3 = hp[y].get("real_hpi", np.nan), hp.get(y - 1, {}).get("real_hpi", np.nan), hp.get(y - 3, {}).get("real_hpi", np.nan)
                g1 = r0 / r1 - 1 if not np.isnan(r0) and not np.isnan(r1) and r1 > 0 else np.nan
                g3 = (r0 / r3) ** (1 / 3) - 1 if not np.isnan(r0) and not np.isnan(r3) and r3 > 0 else np.nan
                w.writerow([y] + ["" if np.isnan(v) else f"{v:.6g}" for v in (r0, hp[y].get("nominal_hpi", np.nan), g1, g3)])
    def sh_year(y, k, how="mean"):
        v = [sh[(y, m)].get(k, np.nan) for m in range(1, 13) if (y, m) in sh]
        v = [x for x in v if not np.isnan(x)]
        if not v:
            return np.nan
        return float(np.mean(v)) if how == "mean" else v[-1]
    def real(y, k):  # deflate an annual-average nominal by the annual-average CPI
        v, c = sh_year(y, k), sh_year(y, "cpi")
        return np.nan if np.isnan(v) or np.isnan(c) or c <= 0 else v / c

    cols = ["nfcb_debt_gdp", "nfcb_equity_mv_gdp", "nfcb_net_worth_growth_3y", "nfcb_capex_gdp", "nfcb_dividends_profits",
            "nfcb_liquid_assets_debt", "corp_profits_gdp", "cape", "real_earnings_growth_1y", "real_earnings_growth_3y",
            "real_price_growth_3y", "earnings_yield_minus_long_rate", "real_home_price_growth_3y", "gw_ntis", "gw_bm", "gw_dfy", "gw_svar"]
    out = []
    for y in range(1871, time.gmtime().tm_year + 1):
        g = gdp_mn(y)
        dkey = "nfcb_debt_securities_and_loans" if S.get("nfcb_debt_securities_and_loans") else "nfcb_debt"  # loans included when present
        debt = q4(S.get(dkey, {}), y) * sc.get(dkey, 1); eq = q4(S.get("nfcb_equity_mv", {}), y) * sc.get("nfcb_equity_mv", 1)
        nw0, nw3 = q4(S.get("nfcb_net_worth", {}), y), q4(S.get("nfcb_net_worth", {}), y - 3)
        capex = annual_mean(S.get("nfcb_capex", {}), y) * sc.get("nfcb_capex", 1)
        div = annual_mean(S.get("nfcb_net_dividends", {}), y); prof = annual_mean(S.get("nfcb_profits_after_tax_q", {}), y)
        liq = q4(S.get("nfcb_liquid_assets", {}), y) * sc.get("nfcb_liquid_assets", 1)
        cp = annual_value(S.get("corp_profits_iva_ccadj_annual", {}), y) * sc.get("corp_profits_iva_ccadj_annual", 1)
        re0, re1, re3 = real(y, "e"), real(y - 1, "e"), real(y - 3, "e")
        rp0, rp3 = real(y, "p"), real(y - 3, "p")
        ep = np.nan if np.isnan(re0) or np.isnan(rp0) or rp0 <= 0 else 100.0 * re0 / rp0
        rate = sh_year(y, "rate")
        row = {"year": y,
               "nfcb_debt_gdp": debt / g if not np.isnan(debt) and not np.isnan(g) and g > 0 else np.nan,
               "nfcb_equity_mv_gdp": eq / g if not np.isnan(eq) and not np.isnan(g) and g > 0 else np.nan,
               "nfcb_net_worth_growth_3y": (nw0 / nw3) ** (1 / 3) - 1 if not np.isnan(nw0) and not np.isnan(nw3) and nw3 > 0 else np.nan,
               "nfcb_capex_gdp": capex / g if not np.isnan(capex) and not np.isnan(g) and g > 0 else np.nan,
               "nfcb_dividends_profits": div * sc.get("nfcb_net_dividends", 1) / (prof * sc.get("nfcb_profits_after_tax_q", 1)) if not np.isnan(div) and not np.isnan(prof) and prof > 0 else np.nan,
               "nfcb_liquid_assets_debt": liq / debt if not np.isnan(liq) and not np.isnan(debt) and debt > 0 else np.nan,
               "corp_profits_gdp": cp / g if not np.isnan(cp) and not np.isnan(g) and g > 0 else np.nan,
               "cape": sh_year(y, "cape", "last"),
               "real_earnings_growth_1y": re0 / re1 - 1 if not np.isnan(re0) and not np.isnan(re1) and re1 > 0 else np.nan,
               "real_earnings_growth_3y": (re0 / re3) ** (1 / 3) - 1 if not np.isnan(re0) and not np.isnan(re3) and re3 > 0 else np.nan,
               "real_price_growth_3y": (rp0 / rp3) ** (1 / 3) - 1 if not np.isnan(rp0) and not np.isnan(rp3) and rp3 > 0 else np.nan,
               "earnings_yield_minus_long_rate": ep - rate if not np.isnan(ep) and not np.isnan(rate) else np.nan,
               "real_home_price_growth_3y": ((hp[y]["real_hpi"] / hp[y - 3]["real_hpi"]) ** (1 / 3) - 1
                                             if y in hp and (y - 3) in hp and "real_hpi" in hp[y] and "real_hpi" in hp[y - 3] else np.nan),
               "gw_ntis": gw.get(y, {}).get("ntis", np.nan), "gw_bm": gw.get(y, {}).get("bm", np.nan),
               "gw_dfy": gw.get(y, {}).get("dfy", np.nan), "gw_svar": gw.get(y, {}).get("svar", np.nan)}
        if all(isinstance(v, float) and np.isnan(v) for k, v in row.items() if k != "year"):
            continue
        out.append(row)
    with open(os.path.join(CORP, "us_corporate_annual.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["year"] + cols)
        for r in out:
            w.writerow([r["year"]] + ["" if (isinstance(r[c], float) and np.isnan(r[c])) else f"{r[c]:.6g}" for c in cols])
    cov = {c: sum(1 for r in out if not (isinstance(r[c], float) and np.isnan(r[c]))) for c in cols}
    years = {c: (min(r["year"] for r in out if not np.isnan(r[c])), max(r["year"] for r in out if not np.isnan(r[c]))) for c in cols if cov[c]}
    print(f"us_corporate_annual: {len(out)} rows; coverage {cov}; spans {years}")
    json.dump({"built_by": "history/tools/corporate_build.py", "provenance_class": "derived", "series_used": meta, "coverage": cov,
               "spans": {c: list(v) for c, v in years.items()}}, open(os.path.join(CORP, "us_corporate_annual.provenance.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
