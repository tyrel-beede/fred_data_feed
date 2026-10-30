#!/usr/bin/env python3
"""pull.py — scheduled data pull for the macro-dials dashboard (v2, after the first live run).

Runs inside GitHub Actions. Writes under data/ and a status file at data/_status.json. Every source is
independent: one failure never blocks the rest. Standard library only.

  FRED (FRED_API_KEY)          data/fred/<SERIES>.csv                 date,value (6 years)
  Treasury FiscalData          data/treasury/auctions.json            raw, newest 400 rows
                               data/treasury/auctions_results.csv     completed auctions with allotment shares
                               data/treasury/tga.json                 daily operating cash balance
  NY Fed markets API           data/nyfed/sofr.json                   SOFR, last 60
                               data/nyfed/pd_positions.csv            primary-dealer net Treasury positions by bucket
  CFTC Socrata TFF             data/cftc/tff_<slug>.json              exact contract match, 3 years
  Yahoo chart API              data/prices/<ticker>.csv               date,open,high,low,close,adjclose,volume (2 years)
  GDELT DOC                    data/gdelt/<slug>_timelinevol.json     20-second spacing; tone in a second pass
  EIA (optional)               data/eia/wti_brent_spot.json
"""
import csv, json, os, sys, time, io, datetime as dt
import urllib.request, urllib.parse, urllib.error

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
STATUS = {"run_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z", "ok": [], "failed": {}}
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) macro-dials-pull/2.0", "Accept": "*/*"}

def get(url, timeout=60, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def save(relpath, text):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

def attempt(name, fn):
    try:
        fn()
        STATUS["ok"].append(name)
        print("ok      ", name)
    except Exception as e:  # noqa: BLE001 — every source is independent
        STATUS["failed"][name] = f"{type(e).__name__}: {e}"[:300]
        print("FAILED  ", name, "->", STATUS["failed"][name])

def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None

# ---------------------------------------------------------------- FRED
FRED_SERIES = [
    "DGS2", "DGS5", "DGS10", "DGS20", "DGS30", "DFII5", "DFII10", "T5YIE", "T10YIE", "T5YIFR",
    "BAMLC0A0CM", "BAMLH0A0HYM2", "BAMLH0A1HYBB", "BAMLH0A2HYB", "BAMLH0A3HYC",
    "ICSA", "CCSA", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS",
    "SP500", "NASDAQCOM", "VIXCLS", "DTWEXBGS", "DCOILWTICO", "DCOILBRENTEU",
    "GOLDPMGBD228NLBM",   # LBMA gold PM fix (the AM series id retired)
    "WALCL", "RRPONTSYD", "WTREGEN", "SOFR", "IORB", "DFF", "EFFR", "WRESBAL",
    "WMTSECL1", "WSHOMCB", "TOTCI", "DRTSCILM", "BUSLOANS", "TOTRESNS", "GFDEGDQ188S",
]

def pull_fred():
    key = os.environ.get("FRED_API_KEY", "").strip()
    if not key:
        raise RuntimeError("FRED_API_KEY not set")
    start = (dt.date.today() - dt.timedelta(days=365 * 6)).isoformat()
    for sid in FRED_SERIES:
        def one(sid=sid):
            url = ("https://api.stlouisfed.org/fred/series/observations?"
                   + urllib.parse.urlencode({"series_id": sid, "api_key": key, "file_type": "json",
                                             "observation_start": start}))
            obs = json.loads(get(url))["observations"]
            rows = [(o["date"], o["value"]) for o in obs if o["value"] not in (".", "")]
            save(f"fred/{sid}.csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows) + "\n")
        attempt(f"fred:{sid}", one)
        time.sleep(0.25)

# ------------------------------------------------------- Treasury FiscalData
def pull_treasury():
    base = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    def auctions():
        url = base + "/v1/accounting/od/auctions_query?sort=-auction_date&page[size]=400"
        txt = get(url)
        save("treasury/auctions.json", txt)
        recs = json.loads(txt)["data"]
        out = io.StringIO(); w = csv.writer(out)
        w.writerow(["auction_date", "security_type", "security_term", "reopening", "high_yield", "bid_to_cover",
                    "comp_accepted", "indirect_pct", "direct_pct", "dealer_pct", "soma_accepted", "total_accepted", "cusip"])
        for r in recs:
            hy = num(r.get("high_yield")); comp = num(r.get("comp_accepted"))
            if hy is None or not comp or r.get("security_type") not in ("Note", "Bond", "TIPS", "FRN"):
                continue
            ind = num(r.get("indirect_bidder_accepted")) or 0.0
            dire = num(r.get("direct_bidder_accepted")) or 0.0
            deal = num(r.get("primary_dealer_accepted")) or 0.0
            w.writerow([r["auction_date"], r["security_type"], r["security_term"], r.get("reopening"), hy,
                        r.get("bid_to_cover_ratio"), int(comp), round(100 * ind / comp, 1), round(100 * dire / comp, 1),
                        round(100 * deal / comp, 1), r.get("soma_accepted"), r.get("total_accepted"), r.get("cusip")])
        save("treasury/auctions_results.csv", out.getvalue())
    def tga():
        url = base + "/v1/accounting/dts/operating_cash_balance?sort=-record_date&page[size]=120"
        save("treasury/tga.json", get(url))
    attempt("treasury:auctions", auctions)
    attempt("treasury:tga", tga)

# ------------------------------------------------------------- NY Fed
PD_KEYS = ["PDPOSGST-TOT", "PDPOSGST-TOTC", "PDPOSGS-B", "PDPOSGSC-L2", "PDPOSGSC-G2L3", "PDPOSGSC-G3L6",
           "PDPOSGSC-G6L7", "PDPOSGSC-G7L11", "PDPOSGSC-G11L21", "PDPOSGSC-G21",
           "PDSORA-UTSETTOT", "PDSIRRA-UTSETTOT"]   # repo / reverse repo on Treasuries ex-TIPS

def pull_nyfed():
    base = "https://markets.newyorkfed.org/api"
    def sofr():
        save("nyfed/sofr.json", get(base + "/rates/secured/sofr/last/60.json"))
    def pd_positions():
        rows = []
        for k in PD_KEYS:
            txt = get(f"{base}/pd/get/{k}.json")
            ts = json.loads(txt)["pd"]["timeseries"]
            for t in ts:
                rows.append((t["asofdate"], t["keyid"], t["value"]))
            time.sleep(0.3)
        rows.sort(reverse=True)
        out = "asofdate,keyid,value_mm\n" + "\n".join(f"{a},{b},{c}" for a, b, c in rows) + "\n"
        save("nyfed/pd_positions.csv", out)
    attempt("nyfed:sofr", sofr)
    attempt("nyfed:pd_positions", pd_positions)

# --------------------------------------------------------------- CFTC TFF
# Exact market names from the Socrata TFF futures-only dataset (gpe5-46if).
CFTC_MARKETS = {
    "es": "E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE",
    "nq": "NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE",
    "rty": "RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE",
    "tu": "UST 2Y NOTE - CHICAGO BOARD OF TRADE",
    "fv": "UST 5Y NOTE - CHICAGO BOARD OF TRADE",
    "ty": "UST 10Y NOTE - CHICAGO BOARD OF TRADE",
    "tn": "ULTRA UST 10Y - CHICAGO BOARD OF TRADE",
    "us": "UST BOND - CHICAGO BOARD OF TRADE",
    "wn": "ULTRA UST BOND - CHICAGO BOARD OF TRADE",
    "vx": "VIX FUTURES - CBOE FUTURES EXCHANGE",
    "gc": "GOLD - COMMODITY EXCHANGE INC.",
    "cl": "CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE",
}

def pull_cftc():
    base = "https://publicreporting.cftc.gov/resource/gpe5-46if.json"
    since = (dt.date.today() - dt.timedelta(days=365 * 3)).isoformat()
    for slug, name in CFTC_MARKETS.items():
        def one(slug=slug, name=name):
            safe = name.replace("'", "''")
            where = f"market_and_exchange_names = '{safe}' AND report_date_as_yyyy_mm_dd >= '{since}'"
            url = base + "?" + urllib.parse.urlencode({"$where": where, "$order": "report_date_as_yyyy_mm_dd DESC", "$limit": 400})
            txt = get(url)
            rows = json.loads(txt)
            if not rows:   # fall back to a contains-match but exclude micro contracts
                where = (f"upper(market_and_exchange_names) like '%{safe.split(' - ')[0].upper()}%' "
                         f"AND upper(market_and_exchange_names) not like 'MICRO%' AND report_date_as_yyyy_mm_dd >= '{since}'")
                url = base + "?" + urllib.parse.urlencode({"$where": where, "$order": "report_date_as_yyyy_mm_dd DESC", "$limit": 400})
                txt = get(url); rows = json.loads(txt)
                if not rows:
                    raise RuntimeError("no rows for " + name)
            save(f"cftc/tff_{slug}.json", txt)
        attempt(f"cftc:{slug}", one)
        time.sleep(0.5)

# ------------------------------------------------------------- prices
PRICES = ["SPY", "RSP", "QQQ", "IWM", "SMH", "XHB", "XLP", "XLU", "XLY", "XLI", "IVE", "IVW", "HYG", "LQD", "TLT", "GLD",
          "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "AVGO", "TSLA",
          "MU", "GEV", "VRT", "ANET", "CRWV", "NBIS", "ORCL", "SPCX"]

def pull_prices():
    """Yahoo's chart endpoint (no key). 2 years of daily bars; a stooq CSV is the fallback."""
    for t in PRICES:
        def one(t=t):
            url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=2y&interval=1d"
                   "&includeAdjustedClose=true")
            try:
                d = json.loads(get(url, headers={"Accept": "application/json"}))["chart"]["result"][0]
                ts = d["timestamp"]; q = d["indicators"]["quote"][0]
                adj = d["indicators"].get("adjclose", [{}])[0].get("adjclose", [None] * len(ts))
                out = io.StringIO(); w = csv.writer(out)
                w.writerow(["date", "open", "high", "low", "close", "adjclose", "volume"])
                for i, s in enumerate(ts):
                    if q["close"][i] is None:
                        continue
                    w.writerow([dt.datetime.utcfromtimestamp(s).date().isoformat(), q["open"][i], q["high"][i],
                                q["low"][i], q["close"][i], adj[i], q["volume"][i]])
                save(f"prices/{t}.csv", out.getvalue())
            except Exception as e_yahoo:
                txt = get(f"https://stooq.com/q/d/l/?s={t.lower()}.us&i=d")
                if not txt.lower().startswith("date,"):
                    raise RuntimeError(f"yahoo: {e_yahoo}; stooq: {txt.strip()[:60]}")
                save(f"prices/{t}.csv", txt)
        attempt(f"prices:{t}", one)
        time.sleep(1.0)

# --------------------------------------------------------------- GDELT
GDELT_QUERIES = {
    "ai_bubble": '"AI bubble" sourcelang:english',
    "dc_capex": '"data center" capex sourcelang:english',
    "term_premium": '("term premium" OR "Treasury auction") sourcelang:english',
    "private_credit": '"private credit" (redemption OR gating) sourcelang:english',
    "hormuz": '"Strait of Hormuz" sourcelang:english',
}

def pull_gdelt(mode="timelinevol"):
    for slug, q in GDELT_QUERIES.items():
        def one(slug=slug, q=q, mode=mode):
            url = "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(
                {"query": q, "mode": mode, "timespan": "3m", "format": "json"})
            for attempt_no in range(3):
                try:
                    txt = get(url)
                    data = json.loads(txt)
                    if "timeline" not in data:
                        raise RuntimeError("no timeline: " + txt[:80])
                    save(f"gdelt/{slug}_{mode}.json", txt)
                    return
                except urllib.error.HTTPError as e:
                    if e.code == 429 and attempt_no < 2:
                        time.sleep(45)
                        continue
                    raise
        attempt(f"gdelt:{slug}:{mode}", one)
        time.sleep(20)

# ----------------------------------------------------------------- EIA
def pull_eia():
    key = os.environ.get("EIA_API_KEY", "").strip()
    if not key:
        raise RuntimeError("EIA_API_KEY not set (optional)")
    url = ("https://api.eia.gov/v2/petroleum/pri/spt/data/?" + urllib.parse.urlencode(
        {"api_key": key, "frequency": "daily", "data[0]": "value", "sort[0][column]": "period",
         "sort[0][direction]": "desc", "length": 400}))
    save("eia/wti_brent_spot.json", get(url))

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    groups = sys.argv[1:] or ["fred", "treasury", "nyfed", "cftc", "prices", "gdelt", "gdelt_tone", "eia"]
    for g in groups:
        {"fred": pull_fred, "treasury": pull_treasury, "nyfed": pull_nyfed, "cftc": pull_cftc,
         "prices": pull_prices, "gdelt": lambda: pull_gdelt("timelinevol"),
         "gdelt_tone": lambda: pull_gdelt("timelinetone"),
         "eia": lambda: attempt("eia", pull_eia)}[g]()
    save("_status.json", json.dumps(STATUS, indent=1))
    print(json.dumps({"ok": len(STATUS["ok"]), "failed": len(STATUS["failed"])}))
