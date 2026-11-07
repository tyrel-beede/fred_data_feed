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


# Aggregator versions, recorded beside each set's aggregates so qc.py can tell a set reduced by an older rule from a
# current one (a set is re-reduced with --redo, which fetches its zip again).
AGG_VERSION_FSDS = 3  # 2 (2026-11-07): one value per filer (CIK) per tag-period from the latest-filed submission that
#                       carries it, so a 10-K/A replaces its original instead of counting beside it; dimensional
#                       (segment) rows set aside where the set marks them; filing counts in <q>_meta.json
#                       3 (2026-11-07): rows per sector (all / nonfinancial / financial, by SIC 6000-6799), since the
#                       all-filer sums of operating cash flow swing with banks' and brokers' trading books; values
#                       beyond a per-tag plausibility cap (several times the largest company's) set aside and listed
#                       in the sidecar; the five largest filers per large tag-period listed there too, so a sum that
#                       moves can be traced to who moved it
AGG_VERSION_13F_ACCEPTED = 4  # sets reduced by this version or later are accepted: the v4 summaries carry the manager
#                       lists, so what v5 corrects at aggregation is measured at build time (corporate_build.py's audit
#                       -> sec_13f_flags.csv) and left out of the table's adjusted holdings value until the next --redo
AGG_VERSION_13F = 5   # 5 (2026-11-07): the unit chosen for a filer is checked against the manager's own history (its
#                       holdings in the other sets' manager lists): among the scalings a thousandfold apart, the one
#                       that lands within twenty times its median is used — which corrects a filer that put its shares
#                       in thousands (the implied-price test reads it as reporting in millions) and a filer that scaled
#                       both value and shares (it reads as normal), and sets aside only a filer no scaling can place;
#                       an options book beyond the cap now loses its option lines, not its holdings; a manager absent
#                       from every other set while above $200 billion is set aside only once a later set exists
#                       4 (2026-11-07): a filer whose option lines exceed $2 trillion after scaling is set aside whole
#                       (an options market maker's mis-scaled book put a quarter of all reported value into options in
#                       two sets without tripping the line or filer caps); a curated exclusions file
#                       (corporate/sec_13f_exclusions.csv: cik, set, reason) is applied at aggregation and recorded;
#                       the 200 largest managers are listed per set, so a manager whose holdings jump a thousandfold
#                       against the neighbouring sets (a filer that scaled both value and shares) can be found and
#                       excluded by name
#                       3 (2026-11-07): a filer's unit is snapped to the nearest power of a thousand (a filer a
#                       millionfold off is a scale error, not a unit, and is rescaled and counted as implausible);
#                       single lines beyond $1 trillion and filers beyond $20 trillion after scaling are set aside
#                       and counted (the first re-reduction left a $6.6 trillion issuer line and option lines worth
#                       more than the market in a handful of sets); the total excluding option lines is reported
#                       beside the reported total; the ten largest filers are listed with their names
#                       2 (2026-11-07): only the holdings reports for the set's own report period count (late filings
#                       for earlier periods and notices set aside; a restatement replaces the filer's original and a
#                       new-holdings amendment adds to it); the VALUE unit is detected per filer, from the implied
#                       price of its lines against the set, so a filer that reported in dollars inside a thousands-era
#                       set is no longer multiplied a thousandfold; the median filer's top-10 share is computed on the
#                       same scaled values as its total; the report period is recorded


def _member(z, base):
    """The zip member whose basename is base (case-insensitive): at the root in the newest sets, inside a folder
    named after the set in the older ones."""
    return next((n for n in z.namelist() if n.lower().rsplit("/", 1)[-1] == base.lower()), None)


# Plausibility caps per tag, in dollars: several times the largest company's figure (JPMorgan's assets near $4tn,
# Walmart's revenue near $700bn, Apple's net income, operating cash flow and buybacks near $100-120bn). A value beyond
# its cap is a filer's scale error (a figure reported in dollars but tagged as thousands, say); it is set aside from
# the sums and listed in the set's sidecar.
FSDS_CAPS = {"Assets": 2e13, "Liabilities": 2e13, "StockholdersEquity": 3e12, "LongTermDebt": 1.5e12, "LongTermDebtNoncurrent": 1.5e12,
             "CashAndCashEquivalentsAtCarryingValue": 1.5e12, "InventoryNet": 5e11, "Revenues": 3e12, "SalesRevenueNet": 3e12,
             "SalesRevenueGoodsNet": 3e12, "RevenueFromContractWithCustomerExcludingAssessedTax": 3e12, "NetIncomeLoss": 6e11,
             "InterestExpense": 3e11, "NetCashProvidedByUsedInOperatingActivities": 1.2e12, "PaymentsToAcquirePropertyPlantAndEquipment": 4e11,
             "PaymentsForRepurchaseOfCommonStock": 4e11, "PaymentsOfDividends": 2e11, "PaymentsOfDividendsCommonStock": 2e11,
             "DepreciationDepletionAndAmortization": 3e11}
FSDS_SECTORS = ("all", "nonfinancial", "financial")


def fsds_sector(sic):
    """SIC 6000-6799 (depository and non-depository credit, brokers, insurance, real estate including REITs) is the
    financial sector; everything else, including blank, nonfinancial."""
    try:
        s = int(sic)
    except (TypeError, ValueError):
        return "nonfinancial"
    return "financial" if 6000 <= s <= 6799 else "nonfinancial"


def _done_sets(cat, suffix, redo):
    """The set names already reduced: every one in raw/, or with redo only those the current aggregator produced
    (so a stopped --redo run picks up where it left off)."""
    d = os.path.join(RAW, cat)
    if not os.path.isdir(d):
        return set()
    names = {f[:-len(suffix)] for f in os.listdir(d) if f.endswith(suffix)}
    if not redo:
        return names
    current = AGG_VERSION_FSDS if cat == "SEC-FSDS" else AGG_VERSION_13F
    done = set()
    for n in names:
        mp = os.path.join(d, f"{n}_meta.json" if cat == "SEC-FSDS" else f"{n}_summary.json")
        try:
            if int(json.load(open(mp)).get("aggregator_version", 1)) >= current:
                done.add(n)
        except Exception:  # noqa
            pass
    return done


def aggregate_fsds(zip_bytes):
    """Per (sector, tag, qtrs, ddate): number of filers, sum, median and 90th percentile of value; 10-K/10-Q forms
    only, USD, no co-registrant rows, no dimensional (segment) rows, no values beyond the tag's plausibility cap; one
    value per filer (CIK) per tag-period, taken from the latest-filed submission that carries it (an amendment
    replaces its original rather than counting beside it). Sectors: all filers, nonfinancial (SIC outside 6000-6799),
    financial. Returns (rows, meta); meta lists the values set aside and the five largest filers per large key."""
    z = zipfile.ZipFile(io.BytesIO(zip_bytes))
    forms = {}  # adsh -> (cik, filed, form, sector)
    with z.open(_member(z, "sub.txt") or "sub.txt") as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        for r in rd:
            form = (r.get("form") or "").strip()
            if form.startswith(("10-K", "10-Q")):
                forms[r["adsh"]] = ((r.get("cik") or "").strip() or r["adsh"], (r.get("filed") or "").strip(), form, fsds_sector(r.get("sic")))
    acc = {}  # (tag, qtrs, ddate) -> cik -> (filed, adsh, value, sector)
    n_used, n_dim, capped = 0, 0, []
    with z.open(_member(z, "num.txt") or "num.txt") as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        for r in rd:
            if r["tag"] not in FSDS_TAGS or r["adsh"] not in forms or r.get("uom") != "USD" or r.get("coreg"):
                continue
            if (r.get("segments") or "").strip() or (r.get("dimh") or "").strip() not in ("", "0x00000000"):
                n_dim += 1
                continue  # a segment or member value, not the consolidated figure
            try:
                v = float(r["value"])
            except (TypeError, ValueError):
                continue
            cik, filed, form, sector = forms[r["adsh"]]
            if abs(v) > FSDS_CAPS.get(r["tag"], 2e13):
                if len(capped) < 50:
                    capped.append({"cik": cik, "adsh": r["adsh"], "form": form, "tag": r["tag"], "qtrs": r["qtrs"], "ddate": r["ddate"], "value": f"{v:.6g}"})
                continue
            n_used += 1
            d = acc.setdefault((r["tag"], r["qtrs"], r["ddate"]), {})
            cur = d.get(cik)
            if cur is None or (filed, r["adsh"]) > (cur[0], cur[1]):  # the latest-filed submission wins; within one, the first value seen
                d[cik] = (filed, r["adsh"], v, sector)
    rows, top = [], {}
    for (tag, qtrs, ddate), d in sorted(acc.items()):
        for sector in FSDS_SECTORS:
            vals = sorted(x[2] for x in d.values() if sector == "all" or x[3] == sector)
            if len(vals) < 20:
                continue
            rows.append({"sector": sector, "tag": tag, "qtrs": qtrs, "ddate": ddate, "n_filers": len(vals), "sum_usd": f"{sum(vals):.6g}",
                         "median_usd": f"{vals[len(vals) // 2]:.6g}", "p90_usd": f"{vals[int(len(vals) * 0.9)]:.6g}"})
        if len(d) >= 1000:
            big = sorted(d.items(), key=lambda kv: -abs(kv[1][2]))[:5]
            top[f"{tag}|{qtrs}|{ddate}"] = [{"cik": cik, "value": f"{x[2]:.6g}", "sector": x[3], "form": forms[x[1]][2]} for cik, x in big]
    per_cik = {}
    for cik, _, _, _ in forms.values():
        per_cik[cik] = per_cik.get(cik, 0) + 1
    meta = {"aggregator_version": AGG_VERSION_FSDS, "n_filings_10k_10q": len(forms),
            "n_filings_amendments": sum(1 for v in forms.values() if "/A" in v[2]),
            "n_filers_cik": len(per_cik), "n_filers_with_several_filings": sum(1 for n in per_cik.values() if n > 1),
            "n_filers_financial": len({v[0] for v in forms.values() if v[3] == "financial"}),
            "n_num_rows_used": n_used, "n_dimensional_rows_set_aside": n_dim, "n_values_beyond_cap": len(capped),
            "values_beyond_cap": capped, "largest_filers": top}
    return rows, meta


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


# The SEC has served the data sets from more than one path: the financial-statement sets under /files/dera/data/,
# the 13F sets under /files/structureddata/data/ and, from the Jun-Aug 2026 window, /files/datastandardsinnovation/data/.
# A predictable file name is tried under each until one answers; the index pages are read for whatever path they link.
SEC_PATHS_FSDS = ["/files/dera/data/financial-statement-data-sets/", "/files/datastandardsinnovation/data/financial-statement-data-sets/",
                  "/files/structureddata/data/financial-statement-data-sets/"]
SEC_PATHS_13F = ["/files/structureddata/data/form-13f-data-sets/", "/files/datastandardsinnovation/data/form-13f-data-sets/",
                 "/files/dera/data/form-13f-data-sets/"]


def get_sec_zip(rels, timeout):
    """Fetch the first of the candidate paths that answers; a 404 moves on to the next, any other failure is raised.
    Returns (data, url)."""
    import urllib.error
    last = None
    for rel_ in rels:
        url = "https://www.sec.gov" + rel_
        try:
            data, _ = get(url, SEC_UA, tries=2, timeout=timeout)
            return data, url
        except urllib.error.HTTPError as e:
            last = e
            if e.code != 404:
                raise
        except Exception as e:  # noqa
            last = e
            raise
    raise last if last else ValueError("no candidate path")


def pull_fsds(manifest, errors, max_quarters=2, since=None, redo=False):
    """since: a year (int) from which every quarter is a candidate (the data sets begin 2009q1); None = the recent ones.
    redo: fetch and reduce again the sets whose aggregates are already in raw/ (after an aggregator change)."""
    try:
        links = []
        try:  # the index page lists the zips; it sits behind bot protection that answers 403 to cloud addresses
            idx = "https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets"
            page, _ = get(idx, SEC_UA, tries=2)
            links = sorted(set(re.findall(r'href="(/files/[^"]+/financial-statement-data-sets/(\d{4}q[1-4])\.zip)"', page.decode("utf-8", "replace"))), reverse=True)
        except Exception as e:  # noqa
            errors.append(f"sec fsds index: {e}; trying the quarterly file names directly")
        # the predictable names (yyyyqN.zip) are tried under every known path as well as whatever the index lists
        qs = all_quarters(since) if since else recent_quarters()
        cands = {}
        for rel_, q in links:
            cands.setdefault(q, []).append(rel_)
        for y, q in qs:
            name = f"{y}q{q}"
            cands.setdefault(name, [])
            cands[name] += [p + name + ".zip" for p in SEC_PATHS_FSDS if p + name + ".zip" not in cands[name]]
        if since:
            cands = {q: v for q, v in cands.items() if int(q[:4]) >= since}
        done = _done_sets("SEC-FSDS", "_aggregates.csv", redo)
        n = 0
        for q in sorted(cands, reverse=True):
            if q in done or n >= max_quarters:
                continue
            try:
                data, url = get_sec_zip(cands[q], timeout=600)
                rows, meta = aggregate_fsds(data)
            except Exception as e:  # noqa
                errors.append(f"sec fsds {q}: {e}"); continue
            body = io.StringIO(); w = csv.DictWriter(body, fieldnames=["sector", "tag", "qtrs", "ddate", "n_filers", "sum_usd", "median_usd", "p90_usd"])
            w.writeheader(); w.writerows(rows)
            meta.update({"set": q, "source_zip_sha256": hashlib.sha256(data).hexdigest(), "source_zip_bytes": len(data), "n_rows": len(rows)})
            save("SEC-FSDS", f"{q}_aggregates.csv", body.getvalue().encode(), url, manifest,
                 note=f"aggregated from the {len(data)}-byte zip (sha256 {meta['source_zip_sha256']}): {meta['n_filings_10k_10q']} 10-K/10-Q filings "
                      f"({meta['n_filings_amendments']} amendments) from {meta['n_filers_cik']} filers, {len(rows)} tag-period rows; aggregator v{AGG_VERSION_FSDS}; the zip is not kept")
            save("SEC-FSDS", f"{q}_meta.json", json.dumps(meta, indent=1).encode(), url, manifest)
            n += 1; time.sleep(2)
    except Exception as e:  # noqa
        errors.append(f"sec fsds: {e}")


# ------------------------------------------------------------------------------------------------------- SEC Form 13F Data Sets
def _iso_date(s):
    """'30-SEP-2014', '2014-09-30', '09/30/2014' or '20140930' -> '2014-09-30'; anything else unchanged."""
    s = (s or "").strip()
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%m/%d/%Y", "%Y%m%d", "%d-%b-%y"):
        try:
            return time.strftime("%Y-%m-%d", time.strptime(s, fmt))
        except ValueError:
            continue
    return s


def _tsv_rows(z, base):
    """All rows of a small TSV member (SUBMISSION, COVERPAGE) with upper-case, stripped keys; None if the set lacks it."""
    name = _member(z, base)
    if not name:
        return None
    with z.open(name) as f:
        rd = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        return [{(k or "").strip().upper(): (v or "").strip() for k, v in r.items()} for r in rd]


def select_13f_filings(z):
    """Which filings of a 13F data set count, and for which report period. A quarterly data set holds the filings
    *made* in the quarter: mostly holdings reports for the quarter that ended just before it, plus late reports for
    earlier periods, notices (13F-NT, no table) and amendments. Returns (use, info): use maps the accession numbers to
    count onto the filer (CIK) they belong to — the latest-filed of each filer's original and restatements for the
    set's own report period, plus its new-holdings amendments — or None when the set has no submission table (then
    every accession in the information table counts, as the first aggregator did)."""
    subs = _tsv_rows(z, "SUBMISSION.tsv")
    if not subs:
        return None, {"filings_filter": "none (no SUBMISSION.tsv in the set)"}
    cover = {r.get("ACCESSION_NUMBER"): r for r in (_tsv_rows(z, "COVERPAGE.tsv") or [])}
    filings = []
    for r in subs:
        a = r.get("ACCESSION_NUMBER"); c = cover.get(a, {})
        stype = (r.get("SUBMISSIONTYPE") or "").upper()
        filings.append({"acc": a, "cik": r.get("CIK") or a, "type": stype, "filed": _iso_date(r.get("FILING_DATE")), "name": c.get("FILINGMANAGER_NAME") or "",
                        "period": _iso_date(c.get("REPORTCALENDARORQUARTER") or r.get("PERIODOFREPORT")),
                        "amend": (c.get("AMENDMENTTYPE") or "").upper(),
                        "is_amend": (c.get("ISAMENDMENT") or "").upper() in ("Y", "TRUE", "1") or stype.endswith("/A")})
    periods = {}
    for f in filings:
        if f["type"].startswith("13F-HR"):
            periods[f["period"]] = periods.get(f["period"], 0) + 1
    if not periods:
        return None, {"filings_filter": "none (no 13F-HR filings listed in SUBMISSION.tsv)"}
    modal = max(periods.items(), key=lambda kv: kv[1])[0]
    by_cik = {}
    for f in filings:
        if f["type"].startswith("13F-HR") and f["period"] == modal:
            by_cik.setdefault(f["cik"], []).append(f)
    use, n_new, n_restate, n_dup = {}, 0, 0, 0
    for cik, fs in by_cik.items():
        new = [f for f in fs if f["is_amend"] and f["amend"].startswith("NEW")]
        base = sorted((f for f in fs if f not in new), key=lambda f: (f["filed"], f["acc"]))
        if base:
            keep = base[-1]
            use[keep["acc"]] = cik
            n_restate += int(keep["is_amend"]); n_dup += len(base) - 1
        for f in new:
            use[f["acc"]] = cik; n_new += 1
    info = {"report_period": modal, "n_filings_in_set": len(filings), "n_filings_used": len(use),
            "n_filings_other_period": sum(1 for f in filings if f["type"].startswith("13F-HR") and f["period"] != modal),
            "n_notices": sum(1 for f in filings if f["type"].startswith("13F-NT")),
            "n_amendments_new_holdings": n_new, "n_restatements_replacing": n_restate, "n_superseded_duplicates": n_dup,
            "filings_filter": "13F-HR for the set's report period; per filer the latest of original and restatements, plus new-holdings amendments",
            "_names": {f["cik"]: f["name"] for f in filings if f["name"]}}
    return use, info


def _infotable(z):
    """Stream the information table: first a dict of column name (upper-cased; the case differs across sets) ->
    index, then each row as a list. Plain rows rather than dicts: the table runs to three million lines and is read
    twice."""
    name = _member(z, "INFOTABLE.tsv")
    if not name:
        raise ValueError(f"no INFOTABLE.tsv in zip: {z.namelist()[:5]}")
    with z.open(name) as f:
        rd = csv.reader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        header = [(c or "").strip().upper() for c in next(rd, [])]
        yield {c: i for i, c in enumerate(header)}
        for row in rd:
            yield row


def _reservoir(store, counts, key, item, cap, rng):
    n = counts.get(key, 0) + 1; counts[key] = n
    s = store.setdefault(key, [])
    if len(s) < cap:
        s.append(item)
    else:
        j = rng.randrange(n)
        if j < cap:
            s[j] = item


LINE_CAP_13F = 1e12    # no single reported position is worth a trillion dollars (the largest real ones are a third of that)
FILER_CAP_13F = 2e13   # no manager reports twenty trillion (the largest report five to six)
FILER_OPTIONS_CAP_13F = 2e12  # no manager's option lines are worth two trillion (the largest options books report a few hundred billion)
EXCLUSIONS_13F = os.path.join(ROOT, "history", "corporate", "sec_13f_exclusions.csv")


def load_13f_exclusions(path=EXCLUSIONS_13F):
    """Curated exclusions: rows of cik, set ('*' for every set), reason, measured. Returns {cik: {set: reason}}."""
    out = {}
    if not os.path.exists(path):
        return out
    for r in csv.DictReader(open(path)):
        cik = (r.get("cik") or "").strip().lstrip("0") or "0"
        if cik and (r.get("set") or "").strip():
            out.setdefault(cik, {})[r["set"].strip()] = r.get("reason", "")
    return out


NEIGHBOR_RATIO_13F = 20.0   # a manager's holdings do not move twenty times against its own history in the other sets
NEIGHBOR_MIN_VALUE_13F = 2e11  # the history check applies where a scaling would put the manager above $200 billion


def load_13f_managers(name):
    """The managers file of a set (its two thousand largest managers, written by aggregator v4): {cik: holdings}."""
    p = os.path.join(RAW, "SEC-13F", f"{name}_managers.csv")
    if not os.path.exists(p):
        return None
    out = {}
    for r in csv.DictReader(open(p)):
        try:
            out[(r["cik"] or "").lstrip("0") or "0"] = float(r["value"])
        except (ValueError, KeyError):
            pass
    return out


def history_13f(name):
    """Every other set's managers file that exists: {set name: {cik: holdings}}, the manager's own history."""
    out = {}
    for n in all_13f_names(2013):
        if n != name:
            m = load_13f_managers(n)
            if m:
                out[n] = m
    return out


def aggregate_13f(zip_bytes, set_name="", exclusions=None, history=None):
    """Reduce a Form 13F data set to a summary (filers, total value in dollars, issuer concentration, the median
    filer's concentration, the put/call share, the largest managers) and the twenty most-held issuers. Two passes
    over the information table: the first learns each filer's VALUE unit, the second aggregates.

    Units. VALUE is in thousands of dollars for filings made before January 2023 and in dollars from then on, but
    filers did not all follow the form: inside a thousands-era set a few hundred filers report in dollars, and for
    several years after the change hundreds still report in thousands. Scaling a whole set by the unit most filers
    used multiplies the others a thousandfold, which is what put trillion-dollar positions into the first
    aggregator's top-20 lists. So the unit is detected per filer: for every line, value / shares (or principal) is
    an implied price; the set's unit comes from the median implied price of its share lines (below $1 means
    thousands, a $50 stock reads 0.05); each issuer's reference is the median implied price across the filers
    holding it; and a filer whose lines sit a thousandfold above or below their issuers' references reports in the
    other unit — snapped to the nearest power of a thousand, so a filer a millionfold off (a scale error, not a
    unit) is rescaled too and counted as implausible. Everything is then scaled to dollars line by line, so filer
    totals, the top-10 heaps behind the median filer's concentration and issuer totals agree. After scaling, a
    single line beyond LINE_CAP_13F or a filer beyond FILER_CAP_13F is set aside and counted: the first
    re-reduction left one issuer at $6.6 trillion and option lines worth more than the market in a few sets."""
    import math, random
    z = zipfile.ZipFile(io.BytesIO(zip_bytes))
    use, info = select_13f_filings(z)
    names = info.pop("_names", {})
    exclusions = load_13f_exclusions() if exclusions is None else exclusions
    history = history or {}
    later_exists = any(qkey_13f(n) > qkey_13f(set_name) for n in history) if set_name else False
    def qdist(n):  # distance in quarters between a set and this one
        a, b = qkey_13f(n), qkey_13f(set_name)
        return abs((a[0] - b[0]) * 12 + (a[1] - b[1])) / 3.0
    hist_sets = sorted(history, key=qdist)
    hist_any = {}
    for n in hist_sets:
        for cik in history[n]:
            hist_any[cik] = True
    def curated(filer):
        rules = exclusions.get((filer or "").lstrip("0") or "0", {})
        return rules.get(set_name) or rules.get("*")
    def against_history(filer, holdings0, k):
        """holdings0: the manager's holdings at the set's own unit (k = 0). Checks managers counted at NEIGHBOR_MIN_VALUE
        or more against their own history — the median of their holdings in the four nearest sets that list them
        (nearest, because managers grow and merge over a decade). Returns (k_to_use, note, reason): k_to_use is the
        unit step whose holdings land nearest that median when within NEIGHBOR_RATIO (a filer that put its shares
        in thousands, or scaled both columns, is corrected rather than dropped); note records a change; reason, when
        no scaling a thousandfold apart lands within the ratio, or the manager is absent from every other set while a
        later set exists, is why it is set aside."""
        key = (filer or "").lstrip("0") or "0"
        counted = holdings0 / (1000.0 ** k)
        if counted < NEIGHBOR_MIN_VALUE_13F or not history:
            return k, "", ""
        near = [history[n][key] for n in hist_sets if key in history[n] and history[n][key] > 0][:4]
        if not near:
            if key not in hist_any and later_exists:
                return k, "", f"absent from every other set's two thousand largest managers while {counted:.3g} here"
            return k, "", ""
        near = sorted(near); med_h = near[len(near) // 2]
        if abs(math.log10(counted / med_h)) <= math.log10(NEIGHBOR_RATIO_13F):
            return k, "", ""
        cand = {m: holdings0 / (1000.0 ** m) for m in (-2, -1, 0, 1, 2)}
        best = min(cand, key=lambda m: abs(math.log10(cand[m] / med_h)) if cand[m] > 0 else 99)
        if abs(math.log10(cand[best] / med_h)) > math.log10(NEIGHBOR_RATIO_13F):
            return k, "", f"not persistent: {counted:.3g} here against a median of {med_h:.3g} in the {len(near)} nearest sets listing it, and no scaling a thousandfold apart lands within {NEIGHBOR_RATIO_13F:g}x"
        return best, f"unit step {k} -> {best}: {counted:.3g} against a median of {med_h:.3g} in the {len(near)} nearest sets listing it", ""
    rng = random.Random(13)
    ref, ref_n, fs, fs_n, set_sample, raw_total, raw_options, raw_big = {}, {}, {}, {}, [], {}, {}, {}
    n_seen = 0
    rows = _infotable(z)
    col = next(rows)
    def at(row, name, default=""):
        i = col.get(name)
        return row[i].strip() if i is not None and i < len(row) else default
    for r in rows:  # pass 1: implied prices and raw totals per filing
        acc = at(r, "ACCESSION_NUMBER")
        if use is not None and acc not in use:
            continue
        try:
            v = float(at(r, "VALUE") or 0); q = float(at(r, "SSHPRNAMT") or 0)
        except ValueError:
            continue
        if v <= 0:
            continue
        raw_total[acc] = raw_total.get(acc, 0.0) + v
        hb = raw_big.setdefault(acc, [])  # the filing's five largest raw lines, so lines beyond the cap can be left out of its estimate
        if len(hb) < 5:
            heapq.heappush(hb, v)
        elif v > hb[0]:
            heapq.heapreplace(hb, v)
        if at(r, "PUTCALL"):
            raw_options[acc] = raw_options.get(acc, 0.0) + v
        if q <= 0:
            continue
        n_seen += 1
        p = v / q; cusip = at(r, "CUSIP")
        _reservoir(ref, ref_n, cusip, (acc, p), 64, rng)
        _reservoir(fs, fs_n, acc, (cusip, p), 64, rng)
        if (at(r, "SSHPRNAMTTYPE") or "SH").upper() == "SH" and n_seen % 7 == 0:
            set_sample.append(p)
    def med(xs):
        xs = sorted(xs); return xs[len(xs) // 2] if xs else 0.0
    set_med = med(set_sample) if set_sample else med(p for s in ref.values() for _, p in s)
    set_scale = 1000.0 if set_med < 1.0 else 1.0
    def classify(ref_med):
        out = {}
        for acc, s in fs.items():
            lr = [math.log10(p / ref_med[c]) for c, p in s if ref_med.get(c, 0) > 0 and p > 0]
            out[acc] = int(round(med(lr) / 3.0)) if lr else 0  # 0: the set's unit; +1 / -1: the other unit; beyond: a scale error
        return out
    # each issuer's reference is the median implied price across its holders; a thinly held issuer whose few holders
    # mix units gets a wrong median, so the references are recomputed from the holders found to be in the set's own
    # unit and the filers classified again (one refinement is enough: the majority is large and consistent)
    filer_k = classify({c: med(p for _, p in s) for c, s in ref.items()})
    ref_med = {}
    for c, s in ref.items():
        own = [p for a, p in s if filer_k.get(a, 0) == 0]
        ref_med[c] = med(own) if own else med(p for _, p in s)
    filer_k = classify(ref_med)
    # the unit of a filer is checked against the manager's own history where it exists (a manager's holdings do not
    # change a thousandfold in a quarter); then filers whose total is beyond any manager's, whose option book is
    # (their option lines are set aside), or whom no scaling can place, are set aside, and so are the curated exclusions
    excluded, curated_applied, unit_overrides, options_set_aside = {}, [], [], {}
    for acc, rt in raw_total.items():
        filer = use.get(acc, acc) if use is not None else acc
        k0 = filer_k.get(acc, 0)
        big0 = sum(v for v in raw_big.get(acc, []) if v * set_scale / (1000.0 ** k0) > LINE_CAP_13F)  # lines the cap will remove
        holdings0 = (rt - raw_options.get(acc, 0.0) - big0) * set_scale  # at the set's unit
        k, note, why = against_history(filer, holdings0, k0)
        if note:
            filer_k[acc] = k
            unit_overrides.append({"cik": filer, "name": names.get(filer, ""), "note": note})
        sc = set_scale / (1000.0 ** k)
        est = (rt - sum(v for v in raw_big.get(acc, []) if v * sc > LINE_CAP_13F)) * sc  # as pass 2 will count it, lines beyond the cap left out
        opt = raw_options.get(acc, 0.0) * sc
        why = curated(filer) or ("total beyond cap" if est - opt > FILER_CAP_13F else "") or why
        if opt > FILER_OPTIONS_CAP_13F and not why:
            options_set_aside[acc] = {"cik": filer, "name": names.get(filer, ""), "options_scaled": f"{opt:.4g}"}
        if why:
            excluded[acc] = {"cik": filer, "name": names.get(filer, ""), "value_scaled": f"{est:.4g}", "options_scaled": f"{opt:.4g}",
                             "unit_steps": k, "why": why}
            if why != "total beyond cap":
                curated_applied.append({"cik": filer, "name": names.get(filer, ""), "value": f"{est - opt:.4g}", "reason": why})
    filer_scale = {acc: set_scale / (1000.0 ** k) for acc, k in filer_k.items()}
    by_cusip, by_cusip_name = {}, {}
    filer_total, filer_top, filer_putcall, filer_lines = {}, {}, {}, {}
    total, putcall_value, n_lines, corrected_value, implausible_value = 0.0, 0.0, 0, 0.0, 0.0
    n_lines_capped, value_lines_capped = 0, 0.0
    rows = _infotable(z)
    next(rows)
    for r in rows:  # pass 2: aggregate in dollars
        acc = at(r, "ACCESSION_NUMBER")
        if (use is not None and acc not in use) or acc in excluded:
            continue
        try:
            v = float(at(r, "VALUE") or 0)
        except ValueError:
            continue
        sc = filer_scale.get(acc, set_scale)
        v *= sc
        if abs(v) > LINE_CAP_13F:
            n_lines_capped += 1; value_lines_capped += v
            continue
        n_lines += 1
        total += v
        k = filer_k.get(acc, 0)
        if k != 0:
            corrected_value += v
        if abs(k) >= 2:
            implausible_value += v
        filer = use.get(acc, acc) if use is not None else acc  # an original and its new-holdings amendment are one filer
        if at(r, "PUTCALL"):
            if acc in options_set_aside:
                total -= v; n_lines -= 1
                if k != 0:
                    corrected_value -= v
                if abs(k) >= 2:
                    implausible_value -= v
                continue  # an option book beyond any manager's: its option lines are set aside, its holdings kept
            putcall_value += v
            filer_putcall[filer] = filer_putcall.get(filer, 0.0) + v
            continue  # options lines are not holdings of the issuer's shares
        cusip = at(r, "CUSIP")
        by_cusip[cusip] = by_cusip.get(cusip, 0.0) + v
        by_cusip_name.setdefault(cusip, at(r, "NAMEOFISSUER"))
        filer_total[filer] = filer_total.get(filer, 0.0) + v
        filer_lines[filer] = filer_lines.get(filer, 0) + 1
        h = filer_top.setdefault(filer, [])
        if len(h) < 10:
            heapq.heappush(h, v)
        elif v > h[0]:
            heapq.heapreplace(h, v)
    vals = sorted(by_cusip.values(), reverse=True)
    s = sum(vals) or 1.0
    top10 = sum(vals[:10]) / s; top50 = sum(vals[:50]) / s
    hhi = sum((v / s) ** 2 for v in vals)
    conc = sorted(sum(filer_top[a]) / filer_total[a] for a in filer_total if filer_total[a] > 0)
    n_corrected = sum(1 for a, k in filer_k.items() if k != 0 and a not in excluded)
    n_implausible = sum(1 for a, k in filer_k.items() if abs(k) >= 2 and a not in excluded)
    ranked = sorted(filer_total, key=lambda f: -filer_total[f])
    largest = [{"cik": f, "name": names.get(f, ""), "value_ex_options": f"{filer_total[f]:.4g}", "share_ex_options": f"{filer_total[f] / s:.4f}",
                "options_value": f"{filer_putcall.get(f, 0.0):.4g}", "top10_share": f"{sum(filer_top[f]) / filer_total[f]:.4f}"}
               for f in ranked[:10]]
    managers = [{"cik": f, "name": names.get(f, ""), "value": f"{filer_total[f]:.4g}", "options": f"{filer_putcall.get(f, 0.0):.4g}",
                 "n": filer_lines.get(f, 0), "unit_steps": filer_k.get(next((a for a in (use or {}) if use[a] == f), f), 0) if use is not None else 0}
                for f in ranked[:2000]]
    summary = {"aggregator_version": AGG_VERSION_13F, "n_filers": len(filer_total), "n_infotable_lines": n_lines,
               "total_value_reported": f"{total:.6g}", "total_value_ex_options": f"{total - putcall_value:.6g}",
               "value_unit_detected": "thousands (scaled x1000 to dollars)" if set_scale != 1.0 else "dollars",
               "value_unit_set": "thousands" if set_scale != 1.0 else "dollars", "set_median_implied_price": f"{set_med:.4g}",
               "n_filers_unit_corrected": n_corrected, "value_share_unit_corrected": f"{corrected_value / total:.4f}" if total else "",
               "n_filers_unit_implausible": n_implausible, "value_share_unit_implausible": f"{implausible_value / total:.4f}" if total else "",
               "n_lines_beyond_cap": n_lines_capped, "value_lines_beyond_cap": f"{value_lines_capped:.4g}",
               "n_filers_beyond_cap": len(excluded), "filers_beyond_cap": sorted(excluded.values(), key=lambda x: -float(x["value_scaled"]))[:10],
               "putcall_value_share": f"{putcall_value / total:.4f}" if total else "", "n_issuers_cusip": len(by_cusip),
               "top10_issuer_share": f"{top10:.4f}", "top50_issuer_share": f"{top50:.4f}", "hhi_issuers": f"{hhi:.6f}",
               "median_filer_top10_share": f"{conc[len(conc) // 2]:.4f}" if conc else "", "largest_filers": largest,
               "exclusions_applied": curated_applied, "unit_overrides_from_history": unit_overrides,
               "n_filers_options_set_aside": len(options_set_aside), "filers_options_set_aside": list(options_set_aside.values())[:10],
               "history_sets_checked": len(history), "managers_top200": managers[:200]}
    summary.update(info)
    summary["_managers"] = managers
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
    # windows from 2024: Jan-Feb 2024 (two months, after the 2023q4 set), then Mar-May, Jun-Aug, Sep-Nov, Dec-Feb
    t = time.gmtime()
    if since_year <= 2024:
        out.append("01jan2024-29feb2024_form13f")
    ey, em = 2024, 5
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


def period_end_13f(name):
    """The holdings date a data set is mostly about, from its name alone: a quarterly set (filings made in the
    quarter) reports the quarter that ended just before it — '2014q4_form13f' -> 2014-09-30 — and a three-month
    window (filings made Mar-May, Jun-Aug, Sep-Nov, Dec-Feb) reports the quarter ending in its first month —
    '01mar2024-31may2024_form13f' -> 2024-03-31. The summaries' report_period (from the filings themselves) is the
    measured value; this is the fallback for summaries written before it was recorded."""
    import calendar
    y, m = qkey_13f(name)
    if not y:
        return ""
    m -= 3 if re.match(r"\d{4}q[1-4]", name.lower()) else 2
    if m <= 0:
        y, m = y - 1, m + 12
    return "%d-%02d-%02d" % (y, m, calendar.monthrange(y, m)[1])


def pull_13f(manifest, errors, max_quarters=2, since=None, redo=False):
    """since: a year (int) from which every data set is a candidate (the sets begin 2013q2); None = the recent ones.
    redo: fetch and reduce again the sets whose summaries are already in raw/ (after an aggregator change)."""
    try:
        links = []
        try:
            idx = "https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets"
            page, _ = get(idx, SEC_UA, tries=2)
            links = re.findall(r'href="(/files/[^"]+/form-13f-data-sets/([^"]+)\.zip)"', page.decode("utf-8", "replace"))
        except Exception as e:  # noqa
            errors.append(f"sec 13f index: {e}; trying the quarterly file names directly")
        # the predictable names (yyyyqN_form13f through 2023, the windows from 2024) are tried under every known path
        # as well as whatever the index lists, so a set the page has not linked yet, or serves from a new path, is fetched
        names = all_13f_names(since) if since else recent_13f_windows()
        cands = {}
        for rel_, name in links:
            cands.setdefault(name, []).append(rel_)
        for name in names:
            cands.setdefault(name, [])
            cands[name] += [p + name + ".zip" for p in SEC_PATHS_13F if p + name + ".zip" not in cands[name]]
        if since:
            cands = {k: v for k, v in cands.items() if qkey_13f(k)[0] >= since}
        done = _done_sets("SEC-13F", "_summary.json", redo)
        n = 0
        for name in sorted(cands, key=qkey_13f, reverse=True):
            if name in done or n >= max_quarters:
                continue
            try:
                data, url = get_sec_zip(cands[name], timeout=900)
                summary, top = aggregate_13f(data, set_name=name, history=history_13f(name))
            except Exception as e:  # noqa
                errors.append(f"sec 13f {name}: {e}"); continue
            managers = summary.pop("_managers", [])
            body = io.StringIO(); w = csv.DictWriter(body, fieldnames=["cik", "name", "value", "options", "n", "unit_steps"]); w.writeheader(); w.writerows(managers)
            save("SEC-13F", f"{name}_managers.csv", body.getvalue().encode(), url, manifest, note="the two thousand largest managers (holdings excluding options, in dollars)")
            summary["source_zip_sha256"] = hashlib.sha256(data).hexdigest(); summary["source_zip_bytes"] = len(data); summary["period"] = name
            save("SEC-13F", f"{name}_summary.json", json.dumps(summary, indent=1).encode(), url, manifest,
                 note=f"aggregated from the zip (not kept) by aggregator v{AGG_VERSION_13F}; report period {summary.get('report_period', '?')}; "
                      f"set unit {summary['value_unit_set']}, {summary['n_filers_unit_corrected']} filers in the other unit rescaled; values in the summary are dollars")
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
    ap.add_argument("--redo", action="store_true", help="SEC sets: fetch and reduce again the sets in raw/ that an older aggregator produced "
                    "(each summary records its aggregator version, so a stopped run resumes). Typically --only 13f --all --redo")
    ap.add_argument("--selftest", action="store_true", help="run the SEC aggregators on synthetic data sets and exit (no network)")
    a = ap.parse_args()
    if a.selftest:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests"))
        import test_sec_aggregators
        return test_sec_aggregators.main()
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
        pull_fsds(manifest, errors, max_quarters=a.quarters, since=a.since or None, redo=a.redo)
    if not only or "13f" in only:
        pull_13f(manifest, errors, max_quarters=a.quarters, since=a.since or None, redo=a.redo)
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
