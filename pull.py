#!/usr/bin/env python3
"""pull.py — scheduled data pull for the macro-dials dashboard.

v2.2: volatility indices (^VIX, ^VIX3M, ^VIX9D, ^VVIX, ^SKEW) and index/futures/sector tickers with 10-year history for the
      core set; FRED volatility and credit additions; two new groups — `options` (CBOE delayed quotes → single-name implied-vol
      surfaces for the AI names and the index ETFs) and `breadth` (S&P 500 constituents → breadth summary and member table).
v2.1: gold/crude via the CFTC Disaggregated dataset, GDELT in its own workflow, per-workflow status files.

Runs inside GitHub Actions. Writes under data/ and a status file at data/_status_main.json (or _status_gdelt.json for the GDELT
workflow). Every source is independent: one failure never blocks the rest. Standard library only.

  FRED (FRED_API_KEY)          data/fred/<SERIES>.csv                 date,value (6 years)
  Treasury FiscalData          data/treasury/auctions.json            raw, newest 400 rows
                               data/treasury/auctions_results.csv     completed auctions with allotment shares
                               data/treasury/tga.json                 daily operating cash balance
  NY Fed markets API           data/nyfed/sofr.json                   SOFR, last 60
                               data/nyfed/pd_positions.csv            primary-dealer net Treasury positions by bucket
  CFTC Socrata TFF             data/cftc/tff_<slug>.json              exact contract match, 3 years
  CFTC Disaggregated           data/cftc/disagg_<slug>.json           gold, crude
  Yahoo chart API              data/prices/<file>.csv                 date,open,high,low,close,adjclose,volume (2y; 10y core; max SPCX)
                                                                       file name: ^VIX → IDX_VIX, ES=F → ES_F, DX-Y.NYB → DX_Y_NYB
  CBOE delayed quotes          data/options/<ticker>_surface.csv      one row per quote date: ATM / 25Δ / 10Δ implied vols at ~30/60/90 days,
                                                                       skew, put/call open interest and volume, OI walls
                               data/options/<ticker>_chain.csv        latest chain ≤ 100 days (strike, expiry, type, bid, ask, iv, delta, oi, volume)
  S&P 500 breadth (Yahoo)      data/breadth/sp500_breadth.csv         daily: advancers/decliners, % above 50d/200d, new 52w highs/lows,
                                                                       up/down volume, A/D line, equal-weight index, % in drawdown >20%
                               data/breadth/sp500_members_latest.csv  per member: sector, close, % from 52w high, MA states, 1m/3m returns
                               data/breadth/constituents.csv          cached constituent list (symbol, sector)
  GDELT DOC                    data/gdelt/<slug>_timelinevol.json     30-second spacing; tone in a second pass (own workflow)
  EIA (optional)               data/eia/wti_brent_spot.json
"""
import csv, json, os, sys, time, io, math, datetime as dt
import urllib.request, urllib.parse, urllib.error
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
STATUS = {"run_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z", "ok": [], "failed": {}}
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) macro-dials-pull/2.2", "Accept": "*/*"}

def get(url, timeout=60, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def get_retry(url, tries=3, backoff=(8, 30, 90), **kw):
    """Yahoo and CBOE answer 429 / 5xx under load; back off instead of failing the source."""
    for i in range(tries):
        try:
            return get(url, **kw)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(backoff[min(i, len(backoff) - 1)])
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if i < tries - 1:
                time.sleep(backoff[min(i, len(backoff) - 1)])
                continue
            raise

def save(relpath, text):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

def load(relpath):
    path = os.path.join(ROOT, relpath)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()

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
        v = float(x)
        return v if math.isfinite(v) else None
    except (TypeError, ValueError):
        return None

def r4(x):
    return "" if x is None else round(x, 4)

# ---------------------------------------------------------------- FRED
FRED_SERIES = [
    "DGS2", "DGS5", "DGS10", "DGS20", "DGS30", "DFII5", "DFII10", "T5YIE", "T10YIE", "T5YIFR",
    "BAMLC0A0CM", "BAMLC0A4CBBB", "BAMLH0A0HYM2", "BAMLH0A1HYBB", "BAMLH0A2HYB", "BAMLH0A3HYC",
    "ICSA", "CCSA", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS",
    "SP500", "NASDAQCOM", "VIXCLS", "VXVCLS", "VXNCLS", "OVXCLS", "GVZCLS", "DTWEXBGS", "DCOILWTICO", "DCOILBRENTEU",
    "WALCL", "RRPONTSYD", "WTREGEN", "SOFR", "IORB", "DFF", "EFFR", "WRESBAL",
    "WMTSECL1", "WSHOMCB", "TOTCI", "DRTSCILM", "BUSLOANS", "TOTRESNS", "GFDEGDQ188S",
    "NFCI", "STLFSI4", "MORTGAGE30US",
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
}
# Gold and crude are not in the TFF report; they live in the Disaggregated futures-only dataset (72hh-8ejz),
# whose classes are producer/merchant, swap dealers, managed money and other reportables.
CFTC_DISAGG = {
    "gc": "GOLD - COMMODITY EXCHANGE INC.",
    "cl": "CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE",
}

def pull_cftc_disagg():
    base = "https://publicreporting.cftc.gov/resource/72hh-8ejz.json"
    since = (dt.date.today() - dt.timedelta(days=365 * 3)).isoformat()
    for slug, name in CFTC_DISAGG.items():
        def one(slug=slug, name=name):
            safe = name.replace("'", "''")
            where = f"market_and_exchange_names = '{safe}' AND report_date_as_yyyy_mm_dd >= '{since}'"
            url = base + "?" + urllib.parse.urlencode({"$where": where, "$order": "report_date_as_yyyy_mm_dd DESC", "$limit": 400})
            txt = get(url)
            if not json.loads(txt):
                raise RuntimeError("no rows for " + name)
            save(f"cftc/disagg_{slug}.json", txt)
        attempt(f"cftc_disagg:{slug}", one)
        time.sleep(0.5)

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
PRICES = [
    # lenses and baskets (unchanged from v2)
    "SPY", "RSP", "QQQ", "IWM", "SMH", "XHB", "XLP", "XLU", "XLY", "XLI", "IVE", "IVW", "HYG", "LQD", "TLT", "GLD",
    "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "AVGO", "TSLA",
    "MU", "GEV", "VRT", "ANET", "CRWV", "NBIS", "ORCL", "SPCX",
    # v2.2 — volatility complex (P5 percentiles computed in-house, 1-year and 6-year windows)
    "^VIX", "^VIX3M", "^VIX9D", "^VVIX", "^SKEW",
    # indices and continuous futures (same-day settles for oil, gold, rates, the dollar; overnight futures for gap work)
    "^GSPC", "^NDX", "^SOX", "^RUT", "ES=F", "NQ=F", "CL=F", "BZ=F", "GC=F", "ZN=F", "DX-Y.NYB",
    # remaining sectors and factor/credit ETFs
    "XLK", "XLF", "XLE", "XLV", "XLC", "XLB", "XLRE", "MTUM", "IEF", "SHY", "TIP", "BKLN", "EMB",
    # wider AI supply chain (memory, foundry, equipment)
    "TSM", "ASML", "LRCX", "AMAT", "000660.KS", "005930.KS",
]
# Ten years for the core set (200-week averages, long percentiles, drawdown context); SPCX from its June 2026 IPO; 2 years otherwise.
LONG_HISTORY = {"SPY", "RSP", "QQQ", "IWM", "SMH", "NVDA", "MU", "TLT", "HYG", "LQD", "GLD", "XLU", "XLY", "XLP", "XLI", "IVE", "IVW",
                "XLK", "XLF", "XLE", "^VIX", "^VIX3M", "^VIX9D", "^VVIX", "^SKEW", "^GSPC", "^NDX", "^SOX", "^RUT",
                "CL=F", "BZ=F", "GC=F", "ZN=F", "DX-Y.NYB"}
RANGE_OVERRIDE = {"SPCX": "max"}

def price_file(t):
    """^VIX → IDX_VIX, ES=F → ES_F, DX-Y.NYB → DX_Y_NYB, 000660.KS → 000660_KS; plain tickers unchanged."""
    return t.replace("^", "IDX_").replace("=F", "_F").replace("-", "_").replace(".", "_")

def yahoo_bars(t, rng, interval="1d"):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(t)}?range={rng}&interval={interval}"
           "&includeAdjustedClose=true")
    d = json.loads(get_retry(url, headers={"Accept": "application/json"}))["chart"]["result"][0]
    ts = d["timestamp"]; q = d["indicators"]["quote"][0]
    adj = d["indicators"].get("adjclose", [{}])[0].get("adjclose", [None] * len(ts))
    rows = []
    for i, s in enumerate(ts):
        if q["close"][i] is None:
            continue
        rows.append((dt.datetime.utcfromtimestamp(s).date().isoformat(), q["open"][i], q["high"][i], q["low"][i],
                     q["close"][i], adj[i], q["volume"][i]))
    return rows

def pull_prices():
    """Yahoo's chart endpoint (no key); a stooq CSV is the fallback (stooq answers a bot check from most cloud IPs)."""
    for t in PRICES:
        def one(t=t):
            rng = RANGE_OVERRIDE.get(t, "10y" if t in LONG_HISTORY else "2y")
            try:
                rows = yahoo_bars(t, rng)
                out = io.StringIO(); w = csv.writer(out)
                w.writerow(["date", "open", "high", "low", "close", "adjclose", "volume"])
                for r in rows:
                    w.writerow(["" if v is None else v for v in r])
                save(f"prices/{price_file(t)}.csv", out.getvalue())
            except Exception as e_yahoo:
                txt = get(f"https://stooq.com/q/d/l/?s={t.lower()}.us&i=d")
                if not txt.lower().startswith("date,"):
                    raise RuntimeError(f"yahoo: {e_yahoo}; stooq: {txt.strip()[:60]}")
                save(f"prices/{price_file(t)}.csv", txt)
        attempt(f"prices:{t}", one)
        time.sleep(1.0)

# ------------------------------------------------------------ options
# CBOE's delayed-quotes feed (the one behind cboe.com's option-chain pages): full chain with bid/ask, implied vol and Greeks.
OPTIONS = ["SPY", "QQQ", "RSP", "IWM", "SMH", "TLT", "HYG",
           "NVDA", "MU", "SPCX", "MSFT", "GOOGL", "META", "AMZN", "AVGO", "CRWV", "ORCL"]
TENORS = (30, 60, 90)

def parse_occ(sym):
    """'NVDA251121C00200000' → ('2025-11-21', 'C', 200.0). Root may carry digits (weeklies), so parse from the right."""
    core = sym.strip().split(":")[-1]
    if len(core) < 16:
        raise ValueError("short option symbol " + sym)
    strike = int(core[-8:]) / 1000.0
    cp = core[-9].upper()
    ymd = core[-15:-9]
    exp = f"20{ymd[:2]}-{ymd[2:4]}-{ymd[4:6]}"
    if cp not in ("C", "P"):
        raise ValueError("bad put/call flag in " + sym)
    return exp, cp, strike

def pick(opts, key, target):
    """The option whose `key` is nearest `target`; None if the list is empty."""
    return min(opts, key=lambda o: abs(o[key] - target)) if opts else None

def interp_iv(opts, spot):
    """Implied vol at the spot strike by linear interpolation between the bracketing strikes (nearest strike if outside)."""
    if not opts:
        return None
    s = sorted(opts, key=lambda o: o["strike"])
    lo = [o for o in s if o["strike"] <= spot]; hi = [o for o in s if o["strike"] >= spot]
    if lo and hi:
        a, b = lo[-1], hi[0]
        if a["strike"] == b["strike"]:
            return a["iv"]
        w = (spot - a["strike"]) / (b["strike"] - a["strike"])
        return a["iv"] + w * (b["iv"] - a["iv"])
    return (hi[0] if hi else lo[-1])["iv"]

def surface_summary(t, asof, spot, chain):
    """One summary row from a parsed chain: ATM / 25Δ / 10Δ vols and skew at ~30/60/90 days, put-call OI and volume, OI walls."""
    today = dt.date.fromisoformat(asof)
    by_exp = {}
    for o in chain:
        by_exp.setdefault(o["exp"], []).append(o)
    exps = []
    for e, os_ in by_exp.items():
        dte = (dt.date.fromisoformat(e) - today).days
        calls = [o for o in os_ if o["cp"] == "C" and o["iv"] and o["delta"] is not None]
        puts = [o for o in os_ if o["cp"] == "P" and o["iv"] and o["delta"] is not None]
        if dte > 0 and len(calls) >= 6 and len(puts) >= 6:
            exps.append((e, dte, calls, puts))
    row = {"date": asof, "spot": r4(spot)}
    wall_exp = None
    for tgt in TENORS:
        cands = [x for x in exps if 0.5 * tgt <= x[1] <= 1.6 * tgt]
        best = min(cands, key=lambda x: abs(x[1] - tgt)) if cands else None
        tag = str(tgt)
        if best is None:
            row.update({f"exp{tag}": "", f"dte{tag}": "", f"atm{tag}": "", f"p25_{tag}": "", f"c25_{tag}": "",
                        f"p10_{tag}": "", f"skew25_{tag}": ""})
            continue
        e, dte, calls, puts = best
        atm_c = interp_iv(calls, spot); atm_p = interp_iv(puts, spot)
        atm = None if atm_c is None or atm_p is None else 0.5 * (atm_c + atm_p)
        p25 = pick(puts, "delta", -0.25); c25 = pick(calls, "delta", 0.25); p10 = pick(puts, "delta", -0.10)
        skew = None if not (p25 and c25) else p25["iv"] - c25["iv"]
        row.update({f"exp{tag}": e, f"dte{tag}": dte, f"atm{tag}": r4(atm), f"p25_{tag}": r4(p25["iv"] if p25 else None),
                    f"c25_{tag}": r4(c25["iv"] if c25 else None), f"p10_{tag}": r4(p10["iv"] if p10 else None),
                    f"skew25_{tag}": r4(skew)})
        if tgt == 30:
            wall_exp = best
    near = [o for o in chain if 0 < (dt.date.fromisoformat(o["exp"]) - today).days <= 100]
    oi_c = sum(o["oi"] for o in near if o["cp"] == "C"); oi_p = sum(o["oi"] for o in near if o["cp"] == "P")
    v_c = sum(o["vol"] for o in near if o["cp"] == "C"); v_p = sum(o["vol"] for o in near if o["cp"] == "P")
    row.update({"pc_oi_100d": r4(oi_p / oi_c) if oi_c else "", "pc_vol_100d": r4(v_p / v_c) if v_c else "",
                "oi_calls_100d": oi_c, "oi_puts_100d": oi_p, "vol_calls_100d": v_c, "vol_puts_100d": v_p})
    if wall_exp:
        e, dte, calls, puts = wall_exp
        cw = max(calls, key=lambda o: o["oi"]) if calls else None
        pw = max(puts, key=lambda o: o["oi"]) if puts else None
        row.update({"call_wall30": cw["strike"] if cw else "", "call_wall30_oi": cw["oi"] if cw else "",
                    "put_wall30": pw["strike"] if pw else "", "put_wall30_oi": pw["oi"] if pw else ""})
    else:
        row.update({"call_wall30": "", "call_wall30_oi": "", "put_wall30": "", "put_wall30_oi": ""})
    row["n_options"] = len(chain)
    return row

def upsert_row(relpath, row):
    """Append `row` to a CSV keyed on its `date`, replacing an existing row for the same date (two pulls a day)."""
    old = load(relpath)
    rows = []
    if old:
        rd = list(csv.DictReader(io.StringIO(old)))
        rows = [r for r in rd if r.get("date") != row["date"]]
    rows.append({k: ("" if v is None else v) for k, v in row.items()})
    fields = list(row.keys())
    for r in rows:
        for k in r:
            if k not in fields:
                fields.append(k)
    out = io.StringIO(); w = csv.DictWriter(out, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in sorted(rows, key=lambda r: r["date"]):
        w.writerow({k: r.get(k, "") for k in fields})
    save(relpath, out.getvalue())

def pull_options():
    for t in OPTIONS:
        def one(t=t):
            url = f"https://cdn.cboe.com/api/global/delayed_quotes/options/{t}.json"
            raw = json.loads(get_retry(url, headers={"Accept": "application/json"}))
            d = raw.get("data", raw)
            spot = num(d.get("current_price")) or num(d.get("close")) or num(d.get("last"))
            if spot is None:
                b, a = num(d.get("bid")), num(d.get("ask"))
                spot = 0.5 * (b + a) if b and a else None
            if not spot:
                raise RuntimeError("no underlying price in the CBOE payload")
            stamp = str(raw.get("timestamp") or d.get("timestamp") or "")[:10]
            asof = stamp if len(stamp) == 10 and stamp[4] == "-" else dt.date.today().isoformat()
            chain = []
            for o in d.get("options") or []:
                try:
                    exp, cp, strike = parse_occ(o.get("option") or o.get("symbol") or "")
                except ValueError:
                    continue
                iv = num(o.get("iv", o.get("implied_volatility")))
                bid, ask = num(o.get("bid")) or 0.0, num(o.get("ask")) or 0.0
                if not iv or iv <= 0 or (bid <= 0 and ask <= 0):
                    continue            # untraded / stale quote: no usable vol
                chain.append({"exp": exp, "cp": cp, "strike": strike, "bid": bid, "ask": ask, "iv": iv,
                              "delta": num(o.get("delta")), "oi": int(num(o.get("open_interest", o.get("oi"))) or 0),
                              "vol": int(num(o.get("volume")) or 0)})
            if len(chain) < 20:
                raise RuntimeError(f"chain too thin ({len(chain)} usable quotes)")
            upsert_row(f"options/{t}_surface.csv", surface_summary(t, asof, spot, chain))
            today = dt.date.fromisoformat(asof)
            out = io.StringIO(); w = csv.writer(out)
            w.writerow(["asof", "exp", "dte", "type", "strike", "bid", "ask", "iv", "delta", "oi", "volume"])
            for o in sorted(chain, key=lambda o: (o["exp"], o["cp"], o["strike"])):
                dte = (dt.date.fromisoformat(o["exp"]) - today).days
                if 0 < dte <= 100:
                    w.writerow([asof, o["exp"], dte, o["cp"], o["strike"], o["bid"], o["ask"], r4(o["iv"]), r4(o["delta"]),
                                o["oi"], o["vol"]])
            save(f"options/{t}_chain.csv", out.getvalue())
        attempt(f"options:{t}", one)
        time.sleep(1.5)

# ------------------------------------------------------------ breadth
class _Table(HTMLParser):
    """Rows of the first <table> whose id is `constituents` (Wikipedia's S&P 500 list)."""
    def __init__(self):
        super().__init__(); self.rows = []; self._in = False; self._row = None; self._cell = None; self._depth = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table" and a.get("id") == "constituents":
            self._in = True
        if not self._in:
            return
        if tag == "tr":
            self._row = []
        elif tag in ("td", "th"):
            self._cell = ""
    def handle_endtag(self, tag):
        if not self._in:
            return
        if tag in ("td", "th") and self._row is not None and self._cell is not None:
            self._row.append(" ".join(self._cell.split())); self._cell = None
        elif tag == "tr" and self._row is not None:
            self.rows.append(self._row); self._row = None
        elif tag == "table":
            self._in = False
    def handle_data(self, data):
        if self._in and self._cell is not None:
            self._cell += data

def constituents():
    """(symbol, sector) for the S&P 500 — GitHub datasets CSV first, Wikipedia second, the cached file third."""
    try:
        txt = get_retry("https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv")
        rd = list(csv.DictReader(io.StringIO(txt)))
        rows = [(r.get("Symbol", "").strip(), r.get("GICS Sector", "").strip()) for r in rd]
        rows = [(s, sec) for s, sec in rows if s]
        if len(rows) < 450:
            raise RuntimeError(f"only {len(rows)} constituents in the datasets CSV")
        src = "datasets"
    except Exception:
        try:
            html = get_retry("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                             headers={"Accept": "text/html"})
            p = _Table(); p.feed(html)
            rows = [(r[0], r[2]) for r in p.rows if len(r) >= 3 and r[0] and r[0] != "Symbol"]
            if len(rows) < 450:
                raise RuntimeError(f"only {len(rows)} constituents parsed from Wikipedia")
            src = "wikipedia"
        except Exception as e:
            cached = load("breadth/constituents.csv")
            if not cached:
                raise RuntimeError(f"no constituent list: {e}")
            rows = [(r["symbol"], r["sector"]) for r in csv.DictReader(io.StringIO(cached))]
            src = "cache"
    out = io.StringIO(); w = csv.writer(out); w.writerow(["symbol", "sector"])
    for s, sec in rows:
        w.writerow([s, sec])
    save("breadth/constituents.csv", out.getvalue())
    print("constituents:", len(rows), "from", src)
    return rows

def breadth_tables(bars, sectors, asof_hint=None):
    """bars: {symbol: [(date, open, high, low, close, adjclose, volume), ...]} → (daily breadth rows, member rows)."""
    series = {}
    for s, rows in bars.items():
        cl = {}; vol = {}
        for d, o, h, l, c, a, v in rows:
            if c is None:
                continue
            cl[d] = float(c); vol[d] = float(v or 0)
        if len(cl) >= 60:
            series[s] = (cl, vol)
    dates = sorted({d for s in series.values() for d in s[0]})
    # a trading day counts when at least 90% of the names printed a close (filters half-populated latest bars)
    counts = {d: sum(1 for s in series.values() if d in s[0]) for d in dates}
    need = 0.9 * len(series)
    dates = [d for d in dates if counts[d] >= need]
    if len(dates) < 260:
        raise RuntimeError(f"too few complete sessions ({len(dates)})")
    per = {}
    for s, (cl, vol) in series.items():
        c = [cl.get(d) for d in dates]
        for i in range(1, len(c)):          # forward-fill isolated gaps so moving averages stay defined
            if c[i] is None:
                c[i] = c[i - 1]
        if c[0] is None:
            continue
        ps = [0.0]                          # prefix sums → O(1) moving averages
        for x in c:
            ps.append(ps[-1] + x)
        per[s] = (c, [vol.get(d, 0.0) for d in dates], ps)
    def ma(ps, i, n):
        return (ps[i + 1] - ps[i + 1 - n]) / n
    out = []
    ad_line = 0.0; eqw = 100.0
    start = 251                         # first session with a full 252-day window
    for i in range(start, len(dates)):
        adv = dec = 0; ab50 = ab200 = 0; nh = nl = 0; upv = dnv = 0.0; rets = []; dd20 = 0; near_high = 0; n = 0
        for s, (c, v, ps) in per.items():
            if c[i] is None or c[i - 1] is None or c[i - 1] == 0:
                continue
            n += 1
            r = c[i] / c[i - 1] - 1.0
            rets.append(r)
            if r > 0:
                adv += 1; upv += v[i]
            elif r < 0:
                dec += 1; dnv += v[i]
            ab50 += c[i] > ma(ps, i, 50); ab200 += c[i] > ma(ps, i, 200)
            w252 = c[i - 251:i + 1]
            mx = max(w252); mn = min(w252)
            nh += c[i] >= mx; nl += c[i] <= mn
            dd20 += c[i] <= 0.8 * mx; near_high += c[i] >= 0.95 * mx
        if n == 0:
            continue
        ad_line += adv - dec
        mean_r = sum(rets) / len(rets)
        eqw *= 1.0 + mean_r
        srt = sorted(rets); med = srt[len(srt) // 2]
        out.append({"date": dates[i], "n": n, "advancers": adv, "decliners": dec, "ad_line": int(ad_line),
                    "pct_above_50d": round(100.0 * ab50 / n, 1), "pct_above_200d": round(100.0 * ab200 / n, 1),
                    "new_52w_highs": nh, "new_52w_lows": nl, "pct_within_5pct_of_high": round(100.0 * near_high / n, 1),
                    "pct_drawdown_gt20": round(100.0 * dd20 / n, 1), "up_volume": int(upv), "down_volume": int(dnv),
                    "eqw_index": round(eqw, 3), "mean_ret_pct": round(100 * mean_r, 3), "median_ret_pct": round(100 * med, 3)})
    members = []
    i = len(dates) - 1
    for s, (c, v, ps) in per.items():
        if c[i] is None:
            continue
        w252 = c[i - 251:i + 1]; mx = max(w252); mn = min(w252)
        ma50 = ma(ps, i, 50); ma200 = ma(ps, i, 200)
        def ret(k):
            return round(100.0 * (c[i] / c[i - k] - 1.0), 2) if i - k >= 0 and c[i - k] else ""
        v20 = sum(v[i - 20:i])
        members.append({"symbol": s, "sector": sectors.get(s, ""), "date": dates[i], "close": round(c[i], 4),
                        "pct_from_52w_high": round(100.0 * (c[i] / mx - 1.0), 2), "pct_above_52w_low": round(100.0 * (c[i] / mn - 1.0), 2),
                        "above_50d": int(c[i] > ma50), "above_200d": int(c[i] > ma200),
                        "ma200_slope_20d_pct": round(100.0 * (ma200 / ma(ps, i - 20, 200) - 1.0), 3) if i >= 219 else "",
                        "ret_1d_pct": ret(1), "ret_1m_pct": ret(21), "ret_3m_pct": ret(63), "ret_12m_pct": ret(252),
                        "vol_vs_20d": round(v[i] / (v20 / 20), 2) if v20 > 0 else ""})
    members.sort(key=lambda m: m["symbol"])
    return out, members

def pull_breadth():
    cons = constituents()
    sectors = {s: sec for s, sec in cons}
    bars = {}
    failed = []
    for s, _ in cons:
        y = s.replace(".", "-")          # BRK.B → BRK-B on Yahoo
        try:
            bars[s] = yahoo_bars(y, "2y")
        except Exception as e:  # noqa: BLE001
            failed.append(f"{s}: {type(e).__name__}")
        time.sleep(0.25)
    if len(bars) < 0.9 * len(cons):
        raise RuntimeError(f"only {len(bars)} of {len(cons)} members fetched; first failures: {failed[:5]}")
    daily, members = breadth_tables(bars, sectors)
    out = io.StringIO(); w = csv.DictWriter(out, fieldnames=list(daily[0].keys())); w.writeheader()
    for r in daily:
        w.writerow(r)
    save("breadth/sp500_breadth.csv", out.getvalue())
    out = io.StringIO(); w = csv.DictWriter(out, fieldnames=list(members[0].keys())); w.writeheader()
    for m in members:
        w.writerow(m)
    save("breadth/sp500_members_latest.csv", out.getvalue())
    if failed:
        STATUS["breadth_unfetched"] = failed
    print(f"breadth: {len(bars)} members, {len(daily)} sessions, latest {daily[-1]['date']}")

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
            for attempt_no in range(4):
                try:
                    txt = get(url)
                    data = json.loads(txt)
                    if "timeline" not in data:
                        raise RuntimeError("no timeline: " + txt[:80])
                    save(f"gdelt/{slug}_{mode}.json", txt)
                    return
                except urllib.error.HTTPError as e:
                    if e.code == 429 and attempt_no < 3:
                        time.sleep(60)
                        continue
                    raise
        attempt(f"gdelt:{slug}:{mode}", one)
        time.sleep(30)

# ----------------------------------------------------------------- EIA
def pull_eia():
    key = os.environ.get("EIA_API_KEY", "").strip()
    if not key:
        raise RuntimeError("EIA_API_KEY not set (optional)")
    url = ("https://api.eia.gov/v2/petroleum/pri/spt/data/?" + urllib.parse.urlencode(
        {"api_key": key, "frequency": "daily", "data[0]": "value", "sort[0][column]": "period",
         "sort[0][direction]": "desc", "length": 400}))
    save("eia/wti_brent_spot.json", get(url))

GROUPS = {
    "fred": pull_fred, "treasury": pull_treasury, "nyfed": pull_nyfed, "cftc": pull_cftc, "cftc_disagg": pull_cftc_disagg,
    "prices": pull_prices, "options": pull_options, "breadth": lambda: attempt("breadth", pull_breadth),
    "gdelt": lambda: pull_gdelt("timelinevol"), "gdelt_tone": lambda: pull_gdelt("timelinetone"),
    "eia": lambda: attempt("eia", pull_eia),
}

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    groups = sys.argv[1:] or ["fred", "treasury", "nyfed", "cftc", "cftc_disagg", "prices", "options", "breadth", "eia"]
    for g in groups:
        GROUPS[g]()
    tag = "gdelt" if all(g.startswith("gdelt") for g in groups) else "main"
    save(f"_status_{tag}.json", json.dumps(STATUS, indent=1))
    print(json.dumps({"ok": len(STATUS["ok"]), "failed": len(STATUS["failed"])}))
