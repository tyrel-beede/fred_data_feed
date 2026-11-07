#!/usr/bin/env python3
"""Pull the corporate-sector catalogs (runs in the GitHub Actions workflow; the sandbox cannot reach these hosts).
Raw files land under history/corporate/raw/<id>/ with a manifest (URL, size, SHA-256, time). Nothing here transforms
the long-record series; corporate_build.py reads them. The two SEC data sets are the exception: their quarterly zips
run to hundreds of megabytes, so the puller streams them in the runner and keeps only small aggregates.

  FRED-Z1          Financial Accounts of the United States (Z.1), nonfinancial corporate business, quarterly 1945-:
                   debt securities and loans, corporate equities (market value), net worth, total liabilities, capital
                   expenditures, net dividends; plus BEA corporate profits (annual 1929-, quarterly 1947-). Series are
                   resolved by exact FRED title at run time and the id used is recorded (needs FRED_API_KEY)
  SHILLER          Robert Shiller's long-record US stock market data (S&P composite price, dividends, earnings, CPI,
                   long rate, CAPE), monthly 1871-; the xls as served from his Yale page
  GOYAL-WELCH      the Goyal-Welch equity-premium predictor workbook (annual 1871-), linked from Amit Goyal's page
  SEC-FSDS         SEC Financial Statement Data Sets (XBRL financial data from 10-K/10-Q filings, quarterly 2009-):
                   per quarter, sums and filer counts of a fixed tag list (assets, debt, cash, revenue, net income,
                   capex, buybacks, dividends, operating cash flow, inventories, interest), 10-K/10-Q forms only
  SEC-13F          SEC Form 13F Data Sets (institutional holdings, quarterly 2013-): per quarter, number of filers,
                   total value, distinct issuers, top-10/top-50 issuer shares, Herfindahl across issuers, median
                   filer concentration, and the twenty most-held issuers

Usage: python3 history/tools/corporate_pull.py            (environment: FRED_API_KEY)
       SEC_CONTACT="Your Name you@example.com" python3 history/tools/corporate_pull.py --only fsds,13f   (desktop SEC run)
"""
import csv, hashlib, heapq, html, io, json, os, re, sys, tempfile, time, urllib.parse, urllib.request, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "history", "corporate", "raw")
UA = {"User-Agent": "fred_data_feed history layer (github.com/tyrel-beede/fred_data_feed)", "Accept-Encoding": "gzip, deflate"}
# SEC's fair-access policy wants a person or company and a contact e-mail in the User-Agent ("Name email@domain"); a
# bot-style agent is refused with 403 even from a residential address (tested 2026-11-06). Set SEC_CONTACT to your own
# "Name email@domain" for desktop runs; the default is the workflow's bot identity, which sec.gov does not accept
SEC_UA = {"User-Agent": os.environ.get("SEC_CONTACT", "").strip() or "fred_data_feed/1.0 (macro-dials-bot@users.noreply.github.com)",
          "Accept": "*/*", "Accept-Encoding": "gzip, deflate"}


def get(url, headers=None, tries=4, timeout=300):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers or UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    data = gzip.decompress(data)
                return data, dict(r.headers)
        except Exception as e:  # noqa
            if i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def save(cat, name, data, url, manifest, note=None):
    d = os.path.join(RAW, cat); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "wb") as f:
        f.write(data)
    rec = {"catalog": cat, "file": f"history/corporate/raw/{cat}/{name}", "url": url, "bytes": len(data),
           "sha256": hashlib.sha256(data).hexdigest(), "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if note:
        rec["note"] = note
    manifest.append(rec)
    print(f"  {cat}/{name}: {len(data)} bytes")


# ------------------------------------------------------------------------------------------------------- FRED Z.1 / BEA
FRED_SERIES = [  # key, candidate ids (tried first), exact title to search for if none of them answers
    ("nfcb_debt", ["NCBDBIQ027S"], "Nonfinancial Corporate Business; Debt Securities; Liability, Level"),
    ("nfcb_debt_securities_and_loans", ["BCNSDODNS"], "Nonfinancial Corporate Business; Debt Securities and Loans; Liability, Level"),
    ("nfcb_equity_mv", ["NCBEILQ027S"], "Nonfinancial Corporate Business; Corporate Equities; Liability, Level"),
    ("nfcb_net_worth", ["TNWMVBSNNCB"], "Nonfinancial Corporate Business; Net Worth, Level"),
    ("nfcb_total_liabilities", ["TLBSNNCB"], "Nonfinancial Corporate Business; Total Liabilities, Level"),
    ("nfcb_capex", ["BOGZ1FA105050005Q"], "Nonfinancial Corporate Business; Capital Expenditures, Transactions"),
    ("nfcb_net_dividends", ["BOGZ1FA106121075Q"], "Nonfinancial Corporate Business; Net Dividends Paid, Transactions"),
    ("nfcb_liquid_assets", ["NCBLLAQ027S"], "Nonfinancial Corporate Business; Liquid Assets (Broad Measure), Level"),
    ("corp_profits_after_tax_q", ["CP"], "Corporate Profits After Tax (without IVA and CCAdj)"),
    ("corp_profits_iva_ccadj_annual", ["A053RC1A027NBEA"], "National income: Corporate profits with inventory valuation and capital consumption adjustments"),
    ("nfcb_profits_after_tax_q", ["NFCPATAX"], "Nonfinancial Corporate Business: Profits After Tax (without IVA and CCAdj)"),
    ("gdp_nominal_q", ["GDP"], "Gross Domestic Product"),
]


def fred_observations(sid, key):
    url = ("https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(
        {"series_id": sid, "api_key": key, "file_type": "json", "observation_start": "1900-01-01"}))
    data, _ = get(url)
    js = json.loads(data)
    if "observations" not in js:
        raise ValueError(js.get("error_message", "no observations"))
    meta, _ = get("https://api.stlouisfed.org/fred/series?" + urllib.parse.urlencode({"series_id": sid, "api_key": key, "file_type": "json"}))
    m = json.loads(meta)["seriess"][0]
    return js["observations"], m


def fred_search(title, key):
    url = "https://api.stlouisfed.org/fred/series/search?" + urllib.parse.urlencode(
        {"search_text": title, "api_key": key, "file_type": "json", "limit": 20})
    data, _ = get(url)
    hits = json.loads(data).get("seriess", [])
    exact = [h for h in hits if h["title"].strip().lower() == title.strip().lower()]
    pool = exact or hits
    # prefer quarterly, then the longest record
    pool.sort(key=lambda h: (h.get("frequency_short") != "Q", h.get("observation_start", "9999")))
    return pool[0]["id"] if pool else None


def pull_fred(manifest, errors):
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        errors.append("fred: FRED_API_KEY not set"); return
    used = []
    for name, cands, title in FRED_SERIES:
        got = None
        for sid in cands:
            try:
                obs, meta = fred_observations(sid, key); got = (sid, obs, meta); break
            except Exception as e:  # noqa
                last = str(e)
        if got is None:
            try:
                sid = fred_search(title, key)
                if sid:
                    obs, meta = fred_observations(sid, key); got = (sid, obs, meta)
            except Exception as e:  # noqa
                last = str(e)
        if got is None:
            errors.append(f"fred {name}: no series found ({title}): {last}"); continue
        sid, obs, meta = got
        body = "date,value\n" + "\n".join(f"{o['date']},{o['value']}" for o in obs if o["value"] not in (".", "")) + "\n"
        save("FRED-Z1", f"{name}.csv", body.encode(), f"FRED {sid}", manifest,
             note=f"{meta.get('title')} | units: {meta.get('units')} | frequency: {meta.get('frequency')} | from {meta.get('observation_start')}")
        used.append({"key": name, "id": sid, "title": meta.get("title"), "units": meta.get("units"), "frequency": meta.get("frequency"),
                     "observation_start": meta.get("observation_start"), "seasonal_adjustment": meta.get("seasonal_adjustment")})
        time.sleep(0.3)
    save("FRED-Z1", "series_used.json", json.dumps(used, indent=1).encode(), "FRED series metadata", manifest)


# ------------------------------------------------------------------------------------------------------- Shiller, Goyal-Welch
def pull_shiller(manifest, errors):
    """Shiller's ie_data.xls: shillerdata.com first (the workbook has been updated there since late 2023; any href
    that names an xls, with or without a query string), then the Yale address (https, then http; the copy there
    stopped in September 2023), then datahub.io's CSV mirror of the same workbook, flagged as a mirror."""
    def yale():
        for url in ("https://www.econ.yale.edu/~shiller/data/ie_data.xls", "http://www.econ.yale.edu/~shiller/data/ie_data.xls"):
            try:
                data, _ = get(url, tries=2, timeout=120)
                if data[:4] == b"\xd0\xcf\x11\xe0" or data[:2] == b"PK":
                    save("SHILLER", "ie_data_yale.xls" if data[:2] != b"PK" else "ie_data_yale.xlsx", data, url, manifest,
                         note="the Yale copy: last updated September 2023; the current workbook is on shillerdata.com (a hand-supplied ie_data.xls beside it takes precedence)"); return True
            except Exception as e:  # noqa
                errors.append(f"shiller ({url}): {e}")
        return False
    try:
        url = "https://shillerdata.com/"
        page, _ = get(url)
        links = sorted(set(html.unescape(l) for l in re.findall(r'href="([^"]*xls[^"]*)"', page.decode("utf-8", "replace"), re.I)))
        if not links:
            raise ValueError("no xls link on shillerdata.com")
        for l in links[:3]:
            furl = urllib.parse.urljoin(url, l)
            data, _ = get(furl)
            if data[:4] == b"\xd0\xcf\x11\xe0" or data[:2] == b"PK":
                name = re.sub(r"[^A-Za-z0-9_.-]", "_", os.path.basename(urllib.parse.urlparse(furl).path)) or "ie_data.xls"
                save("SHILLER", name, data, furl, manifest); return
        raise ValueError("links found but none served a workbook")
    except Exception as e:  # noqa
        errors.append(f"shiller (shillerdata.com): {e}")
    if yale():
        return
    try:  # last resort: the datahub.io core dataset, a scripted mirror of ie_data.xls (monthly, 1871-)
        url = "https://datahub.io/core/s-and-p-500/_r/-/data/data.csv"
        data, _ = get(url)
        if b"Date" in data[:200]:
            save("SHILLER", "datahub_s-and-p-500_monthly.csv", data, url, manifest,
                 note="MIRROR: datahub.io core/s-and-p-500, scripted from Shiller's ie_data.xls; replace with the workbook when the Yale server answers")
        else:
            raise ValueError("unexpected content")
    except Exception as e:  # noqa
        errors.append(f"shiller (datahub mirror): {e}")


def pull_goyal_welch(manifest, errors):
    d = os.path.join(RAW, "GOYAL-WELCH")
    if os.path.isdir(d) and any(f.lower().endswith(".xlsx") for f in os.listdir(d)):
        print("  GOYAL-WELCH: workbook already supplied by hand; the page is not scraped (delete the file to re-pull)"); return
    try:
        url = "https://sites.google.com/view/agoyal145"
        page, _ = get(url)
        txt = page.decode("utf-8", "replace")
        ids = sorted(set(re.findall(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?[^\"']*id=)([A-Za-z0-9_-]{20,})", txt)))
        got = 0
        for fid in ids[:8]:
            try:
                data, hdr = get(f"https://drive.google.com/uc?export=download&id={fid}")
                cd = hdr.get("Content-Disposition", "") or hdr.get("content-disposition", "")
                m = re.search(r'filename="?([^";]+)', cd)
                name = m.group(1) if m else f"{fid}.bin"
                if data[:2] == b"PK" and re.search(r"predictor", name, re.I):
                    save("GOYAL-WELCH", name, data, f"https://drive.google.com/uc?export=download&id={fid}", manifest); got += 1
            except Exception:  # noqa
                pass
            time.sleep(1)
        if not got:
            errors.append("goyal-welch: no predictor workbook found among the page's Drive links (attach PredictorData<year>.xlsx under history/corporate/raw/GOYAL-WELCH/)")
    except Exception as e:  # noqa
        errors.append(f"goyal-welch: {e}")


# ------------------------------------------------------------------------------------------------------- SEC Financial Statement Data Sets
FSDS_TAGS = {"SalesRevenueNet", "SalesRevenueGoodsNet",  # the pre-2018 revenue tags, for continuity across the ASC 606 change
             "Assets", "Liabilities", "StockholdersEquity", "LongTermDebt", "LongTermDebtNoncurrent", "CashAndCashEquivalentsAtCarryingValue",
             "InventoryNet", "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "NetIncomeLoss", "InterestExpense",
             "NetCashProvidedByUsedInOperatingActivities", "PaymentsToAcquirePropertyPlantAndEquipment",
             "PaymentsForRepurchaseOfCommonStock", "PaymentsOfDividends", "PaymentsOfDividendsCommonStock", "DepreciationDepletionAndAmortization"}


def aggregate_fsds(zip_bytes):
    """Per (tag, qtrs, ddate): number of filers, sum and median of value, 10-K/10-Q filers only, USD, no co-registrant."""
    z = zipfile.ZipFile(io.BytesIO(zip_bytes))
    forms = {}
    with z.open("sub.txt") as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        for r in rd:
            if r.get("form", "").startswith(("10-K", "10-Q")):
                forms[r["adsh"]] = (r.get("form"), r.get("fy"), r.get("fp"), r.get("sic"))
    acc = {}
    with z.open("num.txt") as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        for r in rd:
            if r["tag"] not in FSDS_TAGS or r["adsh"] not in forms or r.get("uom") != "USD" or r.get("coreg"):
                continue
            try:
                v = float(r["value"])
            except (TypeError, ValueError):
                continue
            k = (r["tag"], r["qtrs"], r["ddate"])
            acc.setdefault(k, {}).setdefault(r["adsh"], v)  # one value per filer per key (the first seen)
    rows = []
    for (tag, qtrs, ddate), d in sorted(acc.items()):
        vals = sorted(d.values())
        if len(vals) < 20:
            continue
        rows.append({"tag": tag, "qtrs": qtrs, "ddate": ddate, "n_filers": len(vals), "sum_usd": f"{sum(vals):.6g}",
                     "median_usd": f"{vals[len(vals) // 2]:.6g}", "p90_usd": f"{vals[int(len(vals) * 0.9)]:.6g}"})
    return rows, len(forms)


def recent_quarters(n=5):
    """The last n completed calendar quarters as (year, q), newest first."""
    t = time.gmtime(); y, q = t.tm_year, (t.tm_mon - 1) // 3 + 1
    out = []
    for _ in range(n):
        q -= 1
        if q == 0:
            y, q = y - 1, 4
        out.append((y, q))
    return out


def all_quarters(since_year=2009):
    """Every calendar quarter from since_year q1 to the last completed one, newest first."""
    out = []
    y0, q0 = recent_quarters(1)[0]
    y, q = since_year, 1
    while (y, q) <= (y0, q0):
        out.append((y, q))
        q += 1
        if q == 5:
            y, q = y + 1, 1
    return out[::-1]


def pull_fsds(manifest, errors, max_quarters=2, since=None):
    """since: a year (int) from which every quarter is a candidate (the data sets begin 2009q1); None = the recent ones."""
    try:
        links = []
        try:  # the index page lists the zips; it sits behind bot protection that answers 403 to cloud addresses
            idx = "https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets"
            page, _ = get(idx, SEC_UA, tries=2)
            links = sorted(set(re.findall(r'href="(/files/dera/data/financial-statement-data-sets/(\d{4}q[1-4])\.zip)"', page.decode("utf-8", "replace"))), reverse=True)
        except Exception as e:  # noqa
            errors.append(f"sec fsds index: {e}; trying the quarterly file names directly")
        if not links:  # the file names are predictable: yyyyqN.zip
            qs = all_quarters(since) if since else recent_quarters()
            links = [(f"/files/dera/data/financial-statement-data-sets/{y}q{q}.zip", f"{y}q{q}") for y, q in qs]
        if since:
            links = [(rel_, q) for rel_, q in links if int(q[:4]) >= since]
        done = set(os.listdir(os.path.join(RAW, "SEC-FSDS"))) if os.path.isdir(os.path.join(RAW, "SEC-FSDS")) else set()
        n = 0
        for rel_, q in links:
            if f"{q}_aggregates.csv" in done or n >= max_quarters:
                continue
            url = "https://www.sec.gov" + rel_
            try:
                data, _ = get(url, SEC_UA, tries=2, timeout=600)
            except Exception as e:  # noqa
                errors.append(f"sec fsds {q}: {e}"); continue
            rows, nf = aggregate_fsds(data)
            body = io.StringIO(); w = csv.DictWriter(body, fieldnames=["tag", "qtrs", "ddate", "n_filers", "sum_usd", "median_usd", "p90_usd"])
            w.writeheader(); w.writerows(rows)
            save("SEC-FSDS", f"{q}_aggregates.csv", body.getvalue().encode(), url, manifest,
                 note=f"aggregated in the workflow from the {len(data)}-byte zip (sha256 {hashlib.sha256(data).hexdigest()}): {nf} 10-K/10-Q filings, {len(rows)} tag-period rows; the zip is not kept")
            n += 1; time.sleep(2)
    except Exception as e:  # noqa
        errors.append(f"sec fsds: {e}")


# ------------------------------------------------------------------------------------------------------- SEC Form 13F Data Sets
def aggregate_13f(zip_bytes):
    z = zipfile.ZipFile(io.BytesIO(zip_bytes))
    names = {n.lower(): n for n in z.namelist()}
    info = names.get("infotable.tsv")
    if not info:
        raise ValueError(f"no INFOTABLE.tsv in zip: {z.namelist()[:5]}")
    by_cusip, by_cusip_name = {}, {}
    filer_total, filer_top = {}, {}
    total, putcall_value, n_lines = 0.0, 0.0, 0
    line_values = []
    with z.open(info) as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        for r in rd:
            try:
                v = float(r.get("VALUE") or 0)
            except ValueError:
                continue
            n_lines += 1
            if v > 0 and n_lines % 7 == 0:  # a sample of positive line values for the unit check
                line_values.append(v)
            acc = r.get("ACCESSION_NUMBER"); cusip = (r.get("CUSIP") or "").strip()
            total += v
            if (r.get("PUTCALL") or "").strip():
                putcall_value += v
                continue  # options lines are not holdings of the issuer's shares
            by_cusip[cusip] = by_cusip.get(cusip, 0.0) + v
            by_cusip_name.setdefault(cusip, (r.get("NAMEOFISSUER") or "").strip())
            filer_total[acc] = filer_total.get(acc, 0.0) + v
            h = filer_top.setdefault(acc, [])
            if len(h) < 10:
                heapq.heappush(h, v)
            elif v > h[0]:
                heapq.heapreplace(h, v)
    # VALUE is in dollars for filings made from January 2023 and in thousands before; detect the unit from the median line
    # (a typical position is millions of dollars, thousands of thousands) and normalize everything to dollars
    scale = 1.0
    if line_values:
        line_values.sort()
        if line_values[len(line_values) // 2] < 1e5:
            scale = 1000.0
    if scale != 1.0:
        by_cusip = {k: v * scale for k, v in by_cusip.items()}
        filer_total = {k: v * scale for k, v in filer_total.items()}
        total *= scale; putcall_value *= scale
    vals = sorted(by_cusip.values(), reverse=True)
    s = sum(vals) or 1.0
    top10 = sum(vals[:10]) / s; top50 = sum(vals[:50]) / s
    hhi = sum((v / s) ** 2 for v in vals)
    conc = sorted(sum(filer_top[a]) / filer_total[a] for a in filer_total if filer_total[a] > 0)
    summary = {"n_filers": len(filer_total), "n_infotable_lines": n_lines, "total_value_reported": f"{total:.6g}",
               "value_unit_detected": "thousands (scaled x1000 to dollars)" if scale != 1.0 else "dollars",
               "putcall_value_share": f"{putcall_value / total:.4f}" if total else "", "n_issuers_cusip": len(by_cusip),
               "top10_issuer_share": f"{top10:.4f}", "top50_issuer_share": f"{top50:.4f}", "hhi_issuers": f"{hhi:.6f}",
               "median_filer_top10_share": f"{conc[len(conc) // 2]:.4f}" if conc else ""}
    top = [{"rank": k + 1, "cusip": c, "issuer": by_cusip_name.get(c, ""), "value": f"{v:.6g}", "share": f"{v / s:.4f}"}
           for k, (c, v) in enumerate(sorted(by_cusip.items(), key=lambda kv: -kv[1])[:20])]
    return summary, top


def recent_13f_windows(n=5):
    """The last n completed three-month 13F windows (Mar-May, Jun-Aug, Sep-Nov, Dec-Feb) as SEC file stems, newest
    first; a window counts as completed once its last month has ended."""
    import calendar
    mon = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    t = time.gmtime(); y, m = t.tm_year, t.tm_mon
    # the newest window whose end month (Feb, May, Aug, Nov) is strictly before the current month
    ends = [2, 5, 8, 11]
    ey = y; em = max([e for e in ends if e < m], default=None)
    if em is None:
        ey, em = y - 1, 11
    out = []
    for _ in range(n):
        sm = em - 2; sy = ey
        if sm <= 0:
            sm += 12; sy -= 1
        out.append(f"01{mon[sm - 1]}{sy}-{calendar.monthrange(ey, em)[1]}{mon[em - 1]}{ey}_form13f")
        em -= 3
        if em <= 0:
            em += 12; ey -= 1
    return out


def all_13f_names(since_year=2013):
    """Every 13F data-set file stem from since_year on: calendar quarters yyyyqN_form13f through 2023 (the sets begin
    2013q2), then the three-month windows the SEC switched to in 2024; newest first."""
    import calendar
    mon = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    out = []
    for y in range(max(since_year, 2013), 2024):
        for q in (1, 2, 3, 4):
            if (y, q) >= (2013, 2):
                out.append(f"{y}q{q}_form13f")
    # windows from March 2024: Mar-May, Jun-Aug, Sep-Nov, Dec-Feb
    t = time.gmtime()
    ey, em = 2024, 2  # the first window ends February 2024 (the Dec 2023-Feb 2024 filings)
    while (ey, em) < (t.tm_year, t.tm_mon):  # a window counts once its end month has ended
        sm = em - 2; sy = ey
        if sm <= 0:
            sm += 12; sy -= 1
        if sy >= since_year:
            out.append(f"01{mon[sm - 1]}{sy}-{calendar.monthrange(ey, em)[1]}{mon[em - 1]}{ey}_form13f")
        em += 3
        if em > 12:
            em -= 12; ey += 1
    return out[::-1]


def qkey_13f(name):
    """Sort key for either naming style: '2019q3_form13f' -> (2019, 9); '01jul2025-30sep2025_form13f' -> (2025, 9)."""
    m = re.match(r"(\d{4})q([1-4])", name.lower())
    if m:
        return (int(m.group(1)), 3 * int(m.group(2)))
    m = re.search(r"-(\d{2})([a-z]{3})(\d{4})", name.lower())
    months = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
    return (int(m.group(3)), months.get(m.group(2), 0)) if m else (0, 0)


def pull_13f(manifest, errors, max_quarters=2, since=None):
    """since: a year (int) from which every data set is a candidate (the sets begin 2013q2); None = the recent ones."""
    try:
        links = []
        try:
            idx = "https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets"
            page, _ = get(idx, SEC_UA, tries=2)
            links = re.findall(r'href="(/files/structureddata/data/form-13f-data-sets/([^"]+)\.zip)"', page.decode("utf-8", "replace"))
        except Exception as e:  # noqa
            errors.append(f"sec 13f index: {e}; trying the quarterly file names directly")
        if not links:  # predictable names: yyyyqN_form13f.zip through 2023, three-month windows from March 2024
            names = all_13f_names(since) if since else recent_13f_windows()
            links = [(f"/files/structureddata/data/form-13f-data-sets/{n}.zip", n) for n in names]
        if since:
            links = [(rel_, name) for rel_, name in links if qkey_13f(name)[0] >= since]
        links = sorted(set(links), key=lambda t: qkey_13f(t[1]), reverse=True)
        done = set(os.listdir(os.path.join(RAW, "SEC-13F"))) if os.path.isdir(os.path.join(RAW, "SEC-13F")) else set()
        n = 0
        for rel_, name in links:
            if f"{name}_summary.json" in done or n >= max_quarters:
                continue
            url = "https://www.sec.gov" + rel_
            try:
                data, _ = get(url, SEC_UA, tries=2, timeout=900)
            except Exception as e:  # noqa
                errors.append(f"sec 13f {name}: {e}"); continue
            summary, top = aggregate_13f(data)
            summary["source_zip_sha256"] = hashlib.sha256(data).hexdigest(); summary["source_zip_bytes"] = len(data); summary["period"] = name
            save("SEC-13F", f"{name}_summary.json", json.dumps(summary, indent=1).encode(), url, manifest,
                 note=f"aggregated from the zip (not kept); VALUE unit detected: {summary['value_unit_detected']}; values in the summary are dollars")
            body = io.StringIO(); w = csv.DictWriter(body, fieldnames=["rank", "cusip", "issuer", "value", "share"]); w.writeheader(); w.writerows(top)
            save("SEC-13F", f"{name}_top20.csv", body.getvalue().encode(), url, manifest)
            n += 1; time.sleep(2)
    except Exception as e:  # noqa
        errors.append(f"sec 13f: {e}")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma list of pulls to run: fred, shiller, goyal, fsds, 13f (default: all). "
                    "sec.gov answers 403 to cloud-provider addresses, so fsds and 13f are meant to be run from a desktop: "
                    "python3 history/tools/corporate_pull.py --only fsds,13f, then commit history/corporate/raw/")
    ap.add_argument("--quarters", type=int, default=2, help="how many SEC data sets to fetch per run, per set (default 2; the run is resumable: sets already in raw/ are skipped)")
    ap.add_argument("--since", type=int, default=0, help="backfill: consider every SEC data set from this year on (FSDS begin 2009, 13F 2013)")
    ap.add_argument("--all", action="store_true", help="backfill everything: --since 2009 --quarters 200")
    a = ap.parse_args()
    if a.all:
        a.since, a.quarters = 2009, 200
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    manifest, errors = [], []
    os.makedirs(RAW, exist_ok=True)
    if not only or "fred" in only:
        pull_fred(manifest, errors)
    if not only or "shiller" in only:
        pull_shiller(manifest, errors)
    if not only or "goyal" in only:
        pull_goyal_welch(manifest, errors)
    if not only or "fsds" in only:
        pull_fsds(manifest, errors, max_quarters=a.quarters, since=a.since or None)
    if not only or "13f" in only:
        pull_13f(manifest, errors, max_quarters=a.quarters, since=a.since or None)
    out = {"manifest": manifest, "errors": errors, "pulls_run": sorted(only) if only else "all"}
    prev = os.path.join(RAW, "manifest.json")
    if os.path.exists(prev):
        try:
            old = json.load(open(prev)).get("manifest", [])
            seen = {m["file"] for m in manifest}
            out["manifest"] = manifest + [m for m in old if m["file"] not in seen]
        except Exception:  # noqa
            pass
    json.dump(out, open(prev, "w"), indent=1)
    print(json.dumps({"files": len(manifest), "errors": errors}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
