#!/usr/bin/env python3
"""The SEC layer read over its whole record: the thirteen-to-seventeen-year view the two quarterly tables allow.

  financial statements (FSDS, 10-K/10-Q XBRL, 2009-):
    - the annual cash-flow aggregates of the December-fiscal-year filers (operating cash flow, capital expenditures,
      buybacks, dividends, net income, depreciation) and the ratios between them, year by year, with where the latest
      year sits in the record
    - the December-31 balance-sheet aggregates (assets, liabilities, equity, cash, inventories, long-term debt)
    - the timely read: the latest year-to-date flows against the same period a year earlier
    - calibration against the compiled national aggregates the history layer already carries (Z.1 nonfinancial
      corporate capital expenditures and net dividends, NIPA nonfinancial corporate profits after tax): coverage
      ratios and growth agreement
  institutional holdings (13F, 2013-):
    - total reported value against Z.1 corporate equities, issuer concentration (top-10 share, Herfindahl), the
      median filer's own concentration, the number of filers and the put/call share; percentiles of the latest reading
    - only periods reduced by the current aggregator (or, provisionally, dollar-era periods reduced by the first
      one) are used; the rest are listed as awaiting re-reduction

Everything here is a ratio or a same-period comparison: the filer population changed with the XBRL phase-in
(large accelerated filers from 2009, all filers from mid-2011) and drifts with listings and tag usage, so levels are
reported with their filer counts and never compared across years on their own.

Writes history/corporate/sec_analysis.md and sec_analysis.json. Run from the repo root: python3 -I history/tools/sec_analysis.py
"""
import csv, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from corporate_build import read_fred, annual_mean, units_scale, CORP, RAW  # noqa: E402
from corporate_pull import AGG_VERSION_13F, AGG_VERSION_13F_ACCEPTED  # noqa: E402

FSDS = os.path.join(CORP, "sec_fsds_quarterly.csv")
F13 = os.path.join(CORP, "sec_13f_quarterly.csv")
OUT_MD = os.path.join(CORP, "sec_analysis.md")
OUT_JSON = os.path.join(CORP, "sec_analysis.json")
PHASE_IN_LAST_YEAR = 2010  # XBRL for all filers from fiscal periods after June 2011; 2009-2010 annual rows are the large accelerated filers

FLOWS = {"ocf": "NetCashProvidedByUsedInOperatingActivities", "capex": "PaymentsToAcquirePropertyPlantAndEquipment",
         "buybacks": "PaymentsForRepurchaseOfCommonStock", "dividends_common": "PaymentsOfDividendsCommonStock",
         "dividends_all_tag": "PaymentsOfDividends", "net_income": "NetIncomeLoss", "depreciation": "DepreciationDepletionAndAmortization"}
LEVELS = {"assets": "Assets", "liabilities": "Liabilities", "equity": "StockholdersEquity", "cash": "CashAndCashEquivalentsAtCarryingValue",
          "inventories": "InventoryNet", "ltd_noncurrent": "LongTermDebtNoncurrent"}
RATIOS = [  # name, numerator, denominator, label
    ("capex_ocf", "capex", "ocf", "capital expenditures / operating cash flow"),
    ("buybacks_ocf", "buybacks", "ocf", "buybacks / operating cash flow"),
    ("dividends_ocf", "dividends_common", "ocf", "common dividends / operating cash flow"),
    ("payout_ocf", ("buybacks", "dividends_common"), "ocf", "buybacks + common dividends / operating cash flow"),
    ("payout_net_income", ("buybacks", "dividends_common"), "net_income", "buybacks + common dividends / net income"),
    ("capex_depreciation", "capex", "depreciation", "capital expenditures / depreciation and amortization"),
    ("cash_assets", "cash", "assets", "cash and equivalents / assets (Dec 31)"),
    ("liabilities_assets", "liabilities", "assets", "liabilities / assets (Dec 31)"),
    ("inventories_assets", "inventories", "assets", "inventories / assets (Dec 31)"),
    ("ltd_equity", "ltd_noncurrent", "equity", "long-term debt (noncurrent) / stockholders' equity (Dec 31)"),
]


SECTOR = "nonfinancial"  # the sector the reads are built on where the aggregates carry one (v3); all filers before


class Fsds:
    """The quarterly table keyed by (tag, qtrs, ddate), preferring the nonfinancial-sector rows (aggregator v3) and
    falling back to all-filer rows (older aggregates); .sector_used records which, per key."""

    def __init__(self):
        self.rows = {}
        for r in csv.DictReader(open(FSDS)):
            if r["ddate"] < "20090101":
                continue
            self.rows[(r.get("sector") or "all", r["tag"], r["qtrs"], r["ddate"])] = \
                (int(r["n_filers"]), float(r["sum_usd"]), float(r["median_usd"]), r["source_file"], int(float(r.get("aggregator_version") or 1)))
        self.sector_used = {}

    def get(self, key):
        tag, qtrs, ddate = key
        for sector in (SECTOR, "all"):
            v = self.rows.get((sector, tag, qtrs, ddate))
            if v:
                self.sector_used[key] = sector
                return v
        return None

    def keys(self):
        return {(t, q, d) for (_, t, q, d) in self.rows}


def load_fsds():
    return Fsds()


def bn(x):
    return "" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x / 1e9:,.0f}"


def pct_rank(values, x):
    """Share of the record at or below x (1.0 = the highest reading in the record)."""
    vs = [v for v in values if v is not None and not math.isnan(v)]
    return sum(1 for v in vs if v <= x) / len(vs) if vs else float("nan")


def corr(xs, ys):
    pairs = [(a, b) for a, b in zip(xs, ys) if a is not None and b is not None and not (math.isnan(a) or math.isnan(b))]
    if len(pairs) < 4:
        return float("nan"), len(pairs)
    mx = sum(a for a, _ in pairs) / len(pairs); my = sum(b for _, b in pairs) / len(pairs)
    sxy = sum((a - mx) * (b - my) for a, b in pairs); sxx = sum((a - mx) ** 2 for a, _ in pairs); syy = sum((b - my) ** 2 for _, b in pairs)
    return (sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else float("nan")), len(pairs)


def annual_fsds(idx):
    years = sorted({int(d[:4]) for (t, q, d) in idx.keys() if t == FLOWS["ocf"] and q == "4" and d.endswith("1231")})
    out = {}
    for y in years:
        row = {"year": y}
        for k, tag in FLOWS.items():
            v = idx.get((tag, "4", f"{y}1231"))
            row[k] = v[1] if v else None; row[f"n_{k}"] = v[0] if v else None
        for k, tag in LEVELS.items():
            v = idx.get((tag, "0", f"{y}1231"))
            row[k] = v[1] if v else None; row[f"n_{k}"] = v[0] if v else None
        for name, num, den, _ in RATIOS:
            n = sum((row.get(x) or 0.0) for x in num) if isinstance(num, tuple) else row.get(num)
            d = row.get(den)
            ok = (all(row.get(x) is not None for x in num) if isinstance(num, tuple) else n is not None) and d
            row[name] = (n / d) if ok else None
        row["sector"] = idx.sector_used.get((FLOWS["ocf"], "4", f"{y}1231"), "")
        out[y] = row
    return out


def ytd_read(idx):
    """The latest year-to-date (or annual) flow rows against the same period a year earlier, per flow."""
    reads = []
    for qtrs, mmdd, label in (("1", "0331", "Q1 (three months to March 31)"), ("2", "0630", "H1 (six months to June 30)"),
                              ("3", "0930", "nine months to September 30"), ("4", "1231", "fiscal year to December 31")):
        ys = sorted({int(d[:4]) for (t, q, d) in idx.keys() if t == FLOWS["ocf"] and q == qtrs and d.endswith(mmdd)})
        if not ys:
            continue
        y = ys[-1]
        block = {"period": label, "year": y, "flows": {}, "sector": ""}
        for k in ("ocf", "capex", "buybacks", "dividends_common", "net_income"):
            cur = idx.get((FLOWS[k], qtrs, f"{y}{mmdd}")); prev = idx.get((FLOWS[k], qtrs, f"{y - 1}{mmdd}"))
            if cur and prev:
                block["flows"][k] = {"sum": cur[1], "n_filers": cur[0], "sum_prev": prev[1], "n_filers_prev": prev[0],
                                     "growth": cur[1] / prev[1] - 1 if prev[1] else None}
                block["sector"] = idx.sector_used.get((FLOWS[k], qtrs, f"{y}{mmdd}"), "")
        reads.append(block)
    return reads


def calibration(annual):
    """FSDS annual aggregates against the compiled series already in the corporate layer."""
    meta = {}
    mp = os.path.join(RAW, "FRED-Z1", "series_used.json")
    if os.path.exists(mp):
        meta = {m["key"]: m for m in json.load(open(mp))}
    out = []
    for key, fsds_key, label in (("nfcb_capex", "capex", "Z.1 nonfinancial corporate capital expenditures"),
                                 ("nfcb_net_dividends", "dividends_common", "Z.1 nonfinancial corporate net dividends paid"),
                                 ("nfcb_profits_after_tax_q", "net_income", "NIPA nonfinancial corporate profits after tax")):
        s = read_fred(key)
        if not s:
            continue
        sc = units_scale(meta, key) * 1e6  # -> dollars
        rows = []
        for y in sorted(annual):
            z = annual_mean(s, y)
            f = annual[y].get(fsds_key)
            if z is None or math.isnan(z) or f is None:
                continue
            rows.append({"year": y, "fsds": f, "compiled": z * sc, "coverage": f / (z * sc) if z else None})
        g_f = [math.log(rows[i]["fsds"] / rows[i - 1]["fsds"]) if rows[i]["fsds"] > 0 and rows[i - 1]["fsds"] > 0 else None for i in range(1, len(rows))]
        g_z = [math.log(rows[i]["compiled"] / rows[i - 1]["compiled"]) if rows[i]["compiled"] > 0 and rows[i - 1]["compiled"] > 0 else None for i in range(1, len(rows))]
        post = [i for i in range(1, len(rows)) if rows[i - 1]["year"] > PHASE_IN_LAST_YEAR]
        r_all, n_all = corr(g_f, g_z)
        r_post, n_post = corr([g_f[i - 1] for i in post], [g_z[i - 1] for i in post])
        out.append({"compiled_series": key, "label": label, "fsds_series": fsds_key, "units_note": meta.get(key, {}).get("units", ""),
                    "rows": rows, "growth_corr_all": r_all, "n_all": n_all, "growth_corr_after_phase_in": r_post, "n_after_phase_in": n_post})
    return out


def load_13f():
    if not os.path.exists(F13):
        return []
    rows = list(csv.DictReader(open(F13)))
    for r in rows:
        v = int(float(r.get("aggregator_version") or 1))
        unit = (r.get("value_unit_detected") or "")
        # current: the aggregator in force; provisional: an earlier per-filer reduction (v2: right in the main, but a few
        # sets carry garbage option lines and one trillion-dollar issuer line) or a v1 dollar-era set; stale: a v1
        # thousands-era set (known wrong); partial: the SEC's first, incomplete set
        if v >= AGG_VERSION_13F_ACCEPTED:
            r["status"] = "current"
        elif v >= 2 or unit.startswith("dollars"):
            r["status"] = "provisional"
        else:
            r["status"] = "stale"
        if int(float(r.get("n_filers") or 0)) < 1000:
            r["status"] = "partial"
    return rows


def analyze_13f(rows):
    eq = read_fred("nfcb_equity_mv")
    meta = {}
    mp = os.path.join(RAW, "FRED-Z1", "series_used.json")
    if os.path.exists(mp):
        meta = {m["key"]: m for m in json.load(open(mp))}
    sc = units_scale(meta, "nfcb_equity_mv") * 1e6
    used = []
    for r in rows:
        if r["status"] in ("stale", "partial"):
            continue
        pe = r["period_end"]
        q_start = f"{pe[:4]}-{'%02d' % (((int(pe[5:7]) - 1) // 3) * 3 + 1)}-01" if len(pe) >= 7 else ""
        z = eq.get(q_start)
        tv = float(r.get("holdings_value_adjusted_usd") or r.get("total_value_ex_options_usd") or r["total_value_usd"]) \
            if (r.get("holdings_value_adjusted_usd") or r.get("total_value_ex_options_usd") or r.get("total_value_usd")) else None
        used.append({"period": r["period"], "period_end": pe, "status": r["status"], "n_filers": int(r["n_filers"] or 0), "total_value": tv,
                     "z1_nfcb_equities": z * sc if z is not None else None, "coverage": (tv / (z * sc)) if (z and tv) else None,
                     "top10_issuer_share": float(r["top10_issuer_share"] or "nan"), "top50_issuer_share": float(r["top50_issuer_share"] or "nan"),
                     "hhi_issuers": float(r["hhi_issuers"] or "nan"), "median_filer_top10_share": float(r["median_filer_top10_share"] or "nan"),
                     "putcall_value_share": float(r["putcall_value_share"] or "nan"), "n_issuers": int(r["n_issuers"] or 0),
                     "n_filers_unit_corrected": r.get("n_filers_unit_corrected") or "", "value_share_unit_corrected": r.get("value_share_unit_corrected") or "",
                     "n_managers_flagged_at_build": int(float(r.get("n_managers_flagged_at_build") or 0))})
    latest = used[-1] if used else None
    pr = {}
    if latest:
        for k in ("coverage", "top10_issuer_share", "hhi_issuers", "median_filer_top10_share", "putcall_value_share", "n_filers"):
            vals = [u[k] for u in used if u.get(k) is not None]
            pr[k] = pct_rank(vals, latest[k]) if latest.get(k) is not None else None
    largest = []
    if latest:
        sp = os.path.join(RAW, "SEC-13F", f"{latest['period']}_summary.json")
        if os.path.exists(sp):
            largest = json.load(open(sp)).get("largest_filers", [])
    return {"periods": used, "n_current": sum(1 for u in used if u["status"] == "current"), "n_provisional": sum(1 for u in used if u["status"] == "provisional"),
            "n_stale": sum(1 for r in rows if r["status"] == "stale"), "stale_periods": [r["period"] for r in rows if r["status"] == "stale"],
            "n_partial": sum(1 for r in rows if r["status"] == "partial"), "latest": latest, "latest_percentiles": pr, "largest_filers_latest": largest}


def fmt_pct(x, d=0):
    return "" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.{d}f}%"


def fmt(x, d=2):
    return "" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{d}f}"


def raw_rows(tags_qtrs, dates, sector="all", min_filers=1000):
    """Every quarterly file's row for the given (tag, qtrs) keys and dates, from raw/SEC-FSDS, with the aggregator version."""
    d = os.path.join(RAW, "SEC-FSDS")
    out = []
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith("_aggregates.csv"):
            continue
        q = fn.replace("_aggregates.csv", "")
        mp = os.path.join(d, f"{q}_meta.json")
        ver = json.load(open(mp)).get("aggregator_version", 1) if os.path.exists(mp) else 1
        for r in csv.DictReader(open(os.path.join(d, fn))):
            if (r["tag"], r["qtrs"]) in tags_qtrs and r["ddate"] in dates and (r.get("sector") or "all") == sector and int(r["n_filers"]) >= min_filers:
                out.append({"tag": r["tag"], "qtrs": r["qtrs"], "ddate": r["ddate"], "file": q, "n_filers": int(r["n_filers"]), "sum": float(r["sum_usd"]),
                            "p90": float(r["p90_usd"]), "version": ver})
    return sorted(out, key=lambda x: (x["tag"], x["ddate"], x["file"]))


def consistency_check():
    """For the two latest December-31 dates: every file's all-filer row for assets, equity, operating cash flow and net
    income, so a sum that differs between the 10-K file and a 10-Q comparatives file is visible."""
    dates = sorted({r["ddate"] for r in csv.DictReader(open(FSDS)) if r["ddate"].endswith("1231")})[-2:]
    return raw_rows({("Assets", "0"), ("StockholdersEquity", "0"), ("NetCashProvidedByUsedInOperatingActivities", "4"), ("NetIncomeLoss", "4")}, dates)


def first_file_sums(annual, sector):
    """For every year's December-31 assets and equity: the sum in the first quarterly file that carries the key with at
    least 1,000 filers (the 10-Ks, filed in the following quarter), beside the sum the table chose (the file with the
    most filers). Their ratio flags a comparatives file whose values are inflated."""
    dates = {f"{y}1231" for y in annual}
    rows = raw_rows({("Assets", "0"), ("StockholdersEquity", "0")}, dates, sector=sector)
    first = {}
    for r in rows:
        first.setdefault((r["tag"], r["ddate"]), r)  # files are read in name order, so the earliest file comes first
    return first


def write_md(annual, reads, calib, f13, consistency, first_sums, when):
    L = ["# The SEC layer over its record", "",
         f"Built {when} by `tools/sec_analysis.py` from `sec_fsds_quarterly.csv` (financial statements, 10-K/10-Q filers, "
         f"{min(annual)}–{max(annual)}) and `sec_13f_quarterly.csv` (institutional holdings). Sums are over every filer reporting the tag; "
         "the filer population changed with the XBRL phase-in (large accelerated filers in 2009–2010, all filers from mid-2011) and drifts with "
         "listings and tag usage, so the record is read through ratios and same-period comparisons, and levels carry their filer counts. "
         f"Where the aggregates carry a sector split (aggregator v3) the reads use the **{SECTOR}** filers (SIC outside 6000–6799); older aggregates "
         "are all filers, and the `sector` column says which each row is.", ""]
    # 1. annual flows
    L += ["## 1. Annual cash flows of the December-fiscal-year filers ($bn, 10-K `qtrs=4` rows at December 31)", "",
          "| year | sector | filers (OCF) | operating cash flow | capex | buybacks | common dividends | net income | D&A |", "|---|---|---|---|---|---|---|---|---|"]
    for y in sorted(annual):
        a = annual[y]
        L.append(f"| {y}{'*' if y <= PHASE_IN_LAST_YEAR else ''} | {a.get('sector', '')} | {a['n_ocf'] or ''} | {bn(a['ocf'])} | {bn(a['capex'])} | {bn(a['buybacks'])} | "
                 f"{bn(a['dividends_common'])} | {bn(a['net_income'])} | {bn(a['depreciation'])} |")
    L += ["", f"\\* phase-in years (large accelerated filers only). Dividends are the `PaymentsOfDividendsCommonStock` tag "
          f"({annual[max(annual)]['n_dividends_common'] or '?'} filers in {max(annual)}); the broader `PaymentsOfDividends` tag is carried in the JSON "
          "and not added to it, since some filers report both.", ""]
    # 2. ratios
    L += ["## 2. The ratios, and where the latest year sits", "",
          "Aggregate ratios (sum over sum) per year; the percentile is the share of years in the record at or below the latest reading "
          "(100% = the highest in the record).", "",
          "| ratio | " + " | ".join(str(y) for y in sorted(annual)) + " | latest percentile |", "|---|" + "---|" * (len(annual) + 1)]
    latest_y = max(annual)
    pr = {}
    for name, _, _, label in RATIOS:
        vals = [annual[y].get(name) for y in sorted(annual)]
        pr[name] = pct_rank(vals, annual[latest_y][name]) if annual[latest_y].get(name) is not None else None
        L.append(f"| {label} | " + " | ".join(fmt(v) for v in vals) + f" | {fmt_pct(pr[name])} |")
    L += ["", "Balance-sheet ratios use the December-31 levels (`qtrs=0`); long-term debt is the `LongTermDebtNoncurrent` tag, which a minority "
          "of filers use, so that ratio is the thinnest of the set.", ""]
    # 3. levels
    L += ["## 3. December-31 balance sheets ($bn)", "",
          "The table takes, for each tag and date, the quarterly file with the most filers reporting it; the last two columns give the assets "
          "and equity sums in the first file that carried the date (the 10-Ks) and the ratio of the chosen sum to it. A ratio far from one "
          "means the chosen file (10-Q comparatives) carries inflated or duplicated values for that date — see section 7.", "",
          "| year | filers (assets) | assets | liabilities | equity | cash | inventories | long-term debt (noncurrent; filers) | assets, 10-K file (ratio) | equity, 10-K file (ratio) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for y in sorted(annual):
        a = annual[y]
        fa = first_sums.get(("Assets", f"{y}1231")); fe = first_sums.get(("StockholdersEquity", f"{y}1231"))
        ra = f"{bn(fa['sum'])} ({a['assets'] / fa['sum']:.2f})" if fa and a.get("assets") else ""
        re_ = f"{bn(fe['sum'])} ({a['equity'] / fe['sum']:.2f})" if fe and a.get("equity") else ""
        L.append(f"| {y} | {a['n_assets'] or ''} | {bn(a['assets'])} | {bn(a['liabilities'])} | {bn(a['equity'])} | {bn(a['cash'])} | {bn(a['inventories'])} | "
                 f"{bn(a['ltd_noncurrent'])} ({a['n_ltd_noncurrent'] or ''}) | {ra} | {re_} |")
    L.append("")
    # 4. timely read
    L += ["## 4. The timely read: latest year-to-date flows against a year earlier ($bn)", ""]
    for b in reads:
        L += [f"**{b['period']}, {b['year']} vs {b['year'] - 1}** ({b.get('sector') or 'all'} filers)", "", "| flow | " + f"{b['year']} (filers) | {b['year'] - 1} (filers) | change |", "|---|---|---|---|"]
        for k, lab in (("ocf", "operating cash flow"), ("capex", "capital expenditures"), ("buybacks", "buybacks"), ("dividends_common", "common dividends"), ("net_income", "net income")):
            f = b["flows"].get(k)
            if f:
                L.append(f"| {lab} | {bn(f['sum'])} ({f['n_filers']}) | {bn(f['sum_prev'])} ({f['n_filers_prev']}) | {fmt_pct(f['growth'], 1)} |")
        L.append("")
    L += ["10-Q cash-flow statements are year-to-date, so the June and September rows are cumulative; the comparison is same period, "
          "same statement, with the filer counts beside each sum (a change in the count is part of the change in the sum).", ""]
    # 5. calibration
    L += ["## 5. Calibration against the compiled national series", "",
          "The financial-statement sums are the listed, XBRL-filing part of the sector; the Z.1 and NIPA series are the whole nonfinancial "
          "corporate sector, compiled. Coverage is the FSDS sum over the compiled flow; the growth correlation is between year-on-year log "
          "changes of the two.", "",
          "| FSDS series | compiled series | years | coverage, first → latest | growth corr. (all years) | growth corr. after the phase-in |", "|---|---|---|---|---|---|"]
    for c in calib:
        if not c["rows"]:
            continue
        r0, r1 = c["rows"][0], c["rows"][-1]
        L.append(f"| {c['fsds_series']} | {c['label']} | {r0['year']}–{r1['year']} | {fmt(r0['coverage'])} → {fmt(r1['coverage'])} | "
                 f"{fmt(c['growth_corr_all'])} (n={c['n_all']}) | {fmt(c['growth_corr_after_phase_in'])} (n={c['n_after_phase_in']}) |")
    L += ["", "Coverage of a quarter or so is expected: the FSDS sum counts only the filers using the one tag (purchases of property, plant and "
          "equipment, or dividends on common stock), while the Z.1 flows cover every nonfinancial corporation, listed or not, and capital "
          "expenditures there include intellectual-property products. The ratio's stability year to year, and the growth correlation, are the "
          "measures of agreement; the level is not.", ""]
    # 6. 13F
    L += ["## 6. Institutional holdings (Form 13F)", ""]
    if f13["periods"]:
        L += [f"{f13['n_current']} periods reduced by the current aggregator (v{AGG_VERSION_13F}: per-filer units, the set's own report period, "
              f"lines and filers beyond any real size set aside), {f13['n_provisional']} provisional (an earlier reduction: right in the main, but a few "
              f"sets carry option lines worth more than the market or a trillion-dollar issuer line), {f13['n_stale']} stale (the first reduction, "
              f"thousands era, known wrong), {f13['n_partial']} partial (the SEC's first, incomplete set, left out). Re-reduce with "
              "`corporate_pull.py --only 13f --all --redo` from a desktop. Holdings value is the total excluding option lines, less the managers the "
              "build-time history audit flags (`sec_13f_flags.csv`: a manager counted twenty times off its own holdings in the nearest sets, or absent "
              "from every other set; the count per period is the last column).", "",
              "| holdings date | status | filers | holdings value ($tn) | / Z.1 NFC equities | top-10 issuer share | HHI (issuers) | median filer top-10 share | put/call share | filers rescaled | flagged |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for u in f13["periods"]:
            L.append(f"| {u['period_end']} | {u['status']} | {u['n_filers']:,} | {fmt(u['total_value'] / 1e12 if u['total_value'] else None, 1)} | {fmt(u['coverage'])} | "
                     f"{fmt_pct(u['top10_issuer_share'], 1)} | {fmt(u['hhi_issuers'], 4)} | {fmt_pct(u['median_filer_top10_share'], 1)} | {fmt_pct(u['putcall_value_share'], 1)} | "
                     f"{u['n_filers_unit_corrected']} | {u['n_managers_flagged_at_build'] or ''} |")
        lt = f13["latest"]; pr13 = f13["latest_percentiles"]
        L += ["", f"Latest ({lt['period_end']}): the ten most-held issuers are {fmt_pct(lt['top10_issuer_share'], 1)} of reported value "
              f"(percentile {fmt_pct(pr13.get('top10_issuer_share'))} of the usable record), the median filer holds {fmt_pct(lt['median_filer_top10_share'], 1)} of its value in "
              f"its ten largest positions ({fmt_pct(pr13.get('median_filer_top10_share'))}), reported value is {fmt(lt['coverage'])}× the Z.1 market value of "
              f"nonfinancial corporate equities ({fmt_pct(pr13.get('coverage'))}; 13F value includes financial issuers, foreign issuers and options, so "
              "the ratio is a coverage index, not a share).", ""]
        if f13.get("largest_filers_latest"):
            L += ["The ten largest managers in the latest set (a sanity list: the names should be the ones a reader expects, and a stranger at the top "
                  "is a scale error the caps did not catch):", "", "| manager | holdings ($bn) | share | top-10 positions' share of its own holdings |", "|---|---|---|---|"]
            for m in f13["largest_filers_latest"]:
                L.append(f"| {m.get('name') or m.get('cik')} | {float(m['value_ex_options']) / 1e9:,.0f} | {fmt_pct(float(m['share_ex_options']), 1)} | {fmt_pct(float(m['top10_share']), 0)} |")
            L.append("")
    else:
        L += ["No usable 13F periods yet.", ""]
    L += ["## 7. The same period across files: a consistency check", "",
          "A December-31 figure appears first in the 10-Ks (the following quarter's set) and again as the comparative in later 10-Qs. The sums "
          "should agree; where they do not, the difference is duplicated or mis-scaled filer values in one file, and the sidecars written by "
          "aggregator v3 (`raw/SEC-FSDS/<q>_meta.json`: the values set aside and the five largest filers per key) say which.", "",
          "| tag | period | file | filers | sum ($bn) | p90 ($m) | aggregator |", "|---|---|---|---|---|---|---|"]
    for row in consistency:
        L.append(f"| {row['tag']} | {row['ddate']} | {row['file']} | {row['n_filers']} | {bn(row['sum'])} | {row['p90'] / 1e6:,.0f} | v{row['version']} |")
    L += ["", "## Reading rules", "",
          "- Ratios and same-period changes are the comparable quantities; levels drift with the filer population and tag usage.",
          "- The FSDS sums are first-reported values from the latest-filed submission per filer and period (aggregator v2) or the first value seen "
          "(v1 sets); restatements in later years are not propagated back.",
          "- 13F value includes options (put/call lines, excluded from the issuer concentration), financial and foreign issuers; it is long-only "
          "and lagged (filed within 45 days of the quarter end).",
          "- These are the live dials' corporate-sector and positioning reads; they are not learner features (US-only, one era deep).", ""]
    return "\n".join(L)


def main():
    idx = load_fsds()
    annual = annual_fsds(idx)
    reads = ytd_read(idx)
    calib = calibration(annual)
    f13 = analyze_13f(load_13f())
    consistency = consistency_check()
    first_sums = first_file_sums(annual, annual[max(annual)].get("sector") or "all")
    when = time.strftime("%Y-%m-%d", time.gmtime())
    md = write_md(annual, reads, calib, f13, consistency, first_sums, when)
    with open(OUT_MD, "w") as f:
        f.write(md)
    out = {"built": when, "phase_in_last_year": PHASE_IN_LAST_YEAR, "ratios": [{"name": n, "label": lab} for n, _, _, lab in RATIOS],
           "sector_preferred": SECTOR, "annual": [annual[y] for y in sorted(annual)], "ytd_reads": reads, "calibration": calib,
           "consistency_across_files": consistency, "balance_sheet_first_file_sums": [{"tag": k[0], "ddate": k[1], **v} for k, v in sorted(first_sums.items())],
           "form13f": f13}
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=1, default=lambda x: None if isinstance(x, float) and math.isnan(x) else x)
    ly = max(annual)
    print(f"sec_analysis: {len(annual)} annual years ({min(annual)}-{ly}); {len(reads)} timely reads; {len(calib)} calibrations; "
          f"13F {f13['n_current']} current + {f13['n_provisional']} provisional, {f13['n_stale']} stale -> {os.path.relpath(OUT_MD)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
