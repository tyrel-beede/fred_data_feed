#!/usr/bin/env python3
"""pull.py — nightly data pull for the macro-dials dashboard.

Runs inside GitHub Actions (or anywhere with outbound internet). Writes CSV/JSON under data/ and a
status file at data/_status.json. Every source is independent: one failure never blocks the rest.
Standard library only.

Sources
  FRED (needs FRED_API_KEY)            data/fred/<SERIES>.csv           date,value
  Treasury FiscalData (no key)         data/treasury/auctions.json      auction results incl. allotments
                                       data/treasury/tga.json           daily operating cash balance
  NY Fed markets API (no key)          data/nyfed/sofr.json, pd_timeseries_list.json, pd_latest.json
  CFTC Socrata TFF (no key)            data/cftc/tff_<slug>.json        asset managers / leveraged funds / dealers
  stooq (no key, rate-limited)         data/prices/<ticker>.csv         daily OHLCV
  GDELT DOC (no key)                   data/gdelt/<slug>_timelinevol.json / _timelinetone.json
  EIA (optional, EIA_API_KEY)          data/eia/wti_brent_spot.json
"""
import csv, json, os, sys, time, datetime as dt
import urllib.request, urllib.parse, urllib.error

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
STATUS = {"run_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z", "ok": [], "failed": {}}
UA = {"User-Agent": "macro-dials-pull/1.0 (github actions)"}

def get(url, timeout=60, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", errors="replace")

def save(relpath, text):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def attempt(name, fn):
    try:
        fn()
        STATUS["ok"].append(name)
        print("ok      ", name)
    except Exception as e:  # noqa: BLE001 — every source is independent
        STATUS["failed"][name] = f"{type(e).__name__}: {e}"[:300]
        print("FAILED  ", name, "->", STATUS["failed"][name])

# ---------------------------------------------------------------- FRED
FRED_SERIES = [
    # rates, breakevens, credit
    "DGS2", "DGS5", "DGS10", "DGS20", "DGS30", "DFII5", "DFII10", "T5YIE", "T10YIE", "T5YIFR",
    "BAMLC0A0CM", "BAMLH0A0HYM2", "BAMLH0A1HYBB", "BAMLH0A2HYB", "BAMLH0A3HYC",
    # activity, inflation, labor
    "ICSA", "CCSA", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS",
    # markets
    "SP500", "NASDAQCOM", "VIXCLS", "DTWEXBGS", "DCOILWTICO", "DCOILBRENTEU", "GOLDAMGBD228NLBM",
    # Fed plumbing and demand-by-holder
    "WALCL", "RRPONTSYD", "WTREGEN", "SOFR", "IORB", "DFF", "EFFR", "WRESBAL",
    "WMTSECL1",      # marketable Treasuries held in custody for foreign official and international accounts (H.4.1)
    "WSHOMCB",       # securities held outright: MBS (context)
    "TOTCI",         # C&I loans, all commercial banks, weekly SA (H.8)
    "DRTSCILM",      # SLOOS: net % of banks tightening standards for C&I loans, large/mid firms (quarterly)
    "BUSLOANS",      # C&I loans monthly (long history)
    "TOTRESNS",      # reserves (monthly)
    "GFDEGDQ188S",   # federal debt / GDP (quarterly)
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
            out = "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows) + "\n"
            save(f"fred/{sid}.csv", out)
        attempt(f"fred:{sid}", one)
        time.sleep(0.25)

# ------------------------------------------------------- Treasury FiscalData
def pull_treasury():
    base = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    def auctions():
        url = base + "/v1/accounting/od/auctions_query?sort=-auction_date&page[size]=400"
        save("treasury/auctions.json", get(url))
    def tga():
        url = base + "/v1/accounting/dts/operating_cash_balance?sort=-record_date&page[size]=120"
        save("treasury/tga.json", get(url))
    attempt("treasury:auctions", auctions)
    attempt("treasury:tga", tga)

# ------------------------------------------------------------- NY Fed
def pull_nyfed():
    base = "https://markets.newyorkfed.org/api"
    def sofr():
        save("nyfed/sofr.json", get(base + "/rates/secured/sofr/last/60.json"))
    def pd_list():
        save("nyfed/pd_timeseries_list.json", get(base + "/pd/list/timeseries.json"))
    def pd_latest():
        save("nyfed/pd_latest.json", get(base + "/pd/latest/all.json"))
    attempt("nyfed:sofr", sofr)
    attempt("nyfed:pd_list", pd_list)      # pick the Treasury net-position series keys from this list once
    attempt("nyfed:pd_latest", pd_latest)

# --------------------------------------------------------------- CFTC TFF
# Socrata dataset gpe5-46if = Traders in Financial Futures, futures only. Column names are kept raw.
CFTC_MARKETS = {
    "es": "E-MINI S&P 500",
    "nq": "NASDAQ MINI",
    "rty": "RUSSELL E-MINI",
    "tu": "UST 2Y NOTE",
    "fv": "UST 5Y NOTE",
    "ty": "UST 10Y NOTE",
    "tn": "ULTRA UST 10Y",
    "us": "UST BOND",
    "wn": "ULTRA UST BOND",
    "vx": "VIX FUTURES",
    "gc": "GOLD",
    "cl": "CRUDE OIL, LIGHT SWEET",
}

def pull_cftc():
    base = "https://publicreporting.cftc.gov/resource/gpe5-46if.json"
    since = (dt.date.today() - dt.timedelta(days=365 * 3)).isoformat()
    for slug, name in CFTC_MARKETS.items():
        def one(slug=slug, name=name):
            where = f"upper(market_and_exchange_names) like '%{name.upper()}%' AND report_date_as_yyyy_mm_dd >= '{since}'"
            url = base + "?" + urllib.parse.urlencode({"$where": where, "$order": "report_date_as_yyyy_mm_dd DESC",
                                                      "$limit": 400})
            save(f"cftc/tff_{slug}.json", get(url))
        attempt(f"cftc:{slug}", one)
        time.sleep(0.5)

# --------------------------------------------------------------- stooq
PRICES = ["spy", "rsp", "qqq", "iwm", "smh", "xhb", "xlp", "xlu", "xly", "xli", "ive", "ivw", "hyg", "lqd", "tlt", "gld",
          "nvda", "aapl", "msft", "googl", "amzn", "meta", "avgo", "tsla",
          "mu", "gev", "vrt", "anet", "crwv", "nbis", "orcl", "spcx"]

def pull_stooq():
    for t in PRICES:
        def one(t=t):
            txt = get(f"https://stooq.com/q/d/l/?s={t}.us&i=d")
            if not txt.lower().startswith("date,") or "exceeded" in txt.lower():
                raise RuntimeError(txt.strip()[:80])
            save(f"prices/{t}.csv", txt)
        attempt(f"stooq:{t}", one)
        time.sleep(1.5)

# --------------------------------------------------------------- GDELT
GDELT_QUERIES = {
    "ai_bubble": '"AI bubble" sourcelang:english',
    "dc_capex": '"data center" capex sourcelang:english',
    "term_premium": '("term premium" OR "Treasury auction") sourcelang:english',
    "private_credit": '"private credit" (redemption OR gating) sourcelang:english',
    "hormuz": '"Strait of Hormuz" sourcelang:english',
}

def pull_gdelt():
    for slug, q in GDELT_QUERIES.items():
        for mode in ("timelinevol", "timelinetone"):
            def one(slug=slug, q=q, mode=mode):
                url = "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(
                    {"query": q, "mode": mode, "timespan": "3m", "format": "json"})
                txt = get(url)
                data = json.loads(txt)                      # raises on a non-JSON (rate-limited) reply
                if "timeline" not in data:
                    raise RuntimeError("no timeline in GDELT reply: " + txt[:80])
                save(f"gdelt/{slug}_{mode}.json", txt)      # query_details.title is kept for the run to check
            attempt(f"gdelt:{slug}:{mode}", one)
            time.sleep(6)   # GDELT rate-limits bursts

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
    groups = sys.argv[1:] or ["fred", "treasury", "nyfed", "cftc", "stooq", "gdelt", "eia"]
    for g in groups:
        {"fred": pull_fred, "treasury": pull_treasury, "nyfed": pull_nyfed, "cftc": pull_cftc,
         "stooq": pull_stooq, "gdelt": pull_gdelt, "eia": lambda: attempt("eia", pull_eia)}[g]()
    save("_status.json", json.dumps(STATUS, indent=1))
    print(json.dumps({"ok": len(STATUS["ok"]), "failed": len(STATUS["failed"])}))
