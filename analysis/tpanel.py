#!/usr/bin/env python3
"""tpanel.py — technical panel for the macro-dials equity lens, computed from the data repository's daily OHLCV files.

Usage: python3 -I tpanel.py <repo>/data [TICKER ...]
Prints one row per ticker (trend regime, extension, volatility, volume character, overnight/intraday split, momentum)
and one row per relative-strength pair (ratio vs its own moving averages and 1-year percentile). Standard library only.
"""
import csv, math, os, sys, statistics as st

DEFAULT = ["SPY", "RSP", "QQQ", "IWM", "SMH", "NVDA", "MU", "SPCX", "MSFT", "GOOGL", "META", "AMZN", "CRWV", "TLT", "HYG", "GLD"]
PAIRS = [("RSP", "SPY"), ("QQQ", "SPY"), ("IWM", "SPY"), ("SMH", "QQQ"), ("NVDA", "SMH"), ("MU", "SMH"), ("SPCX", "QQQ"),
         ("XLU", "XLY"), ("IVE", "IVW"), ("HYG", "LQD")]

def load(root, t):
    p = os.path.join(root, "prices", f"{t}.csv")
    if not os.path.exists(p):
        return None
    rows = []
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                rows.append({"d": r["date"], "o": float(r["open"]), "h": float(r["high"]), "l": float(r["low"]),
                             "c": float(r["close"]), "a": float(r.get("adjclose") or r["close"]), "v": float(r["volume"] or 0)})
            except (ValueError, KeyError):
                continue
    rows.sort(key=lambda r: r["d"])
    return rows

def pct(a, b):
    return None if a is None or b is None or b == 0 else 100.0 * (a / b - 1.0)

def fmt(x, d=1, suffix=""):
    return "—" if x is None else f"{x:+.{d}f}{suffix}" if isinstance(x, float) and suffix == "%" else ("—" if x is None else f"{x:.{d}f}" if isinstance(x, float) else str(x))

def ma(c, n, end=None):
    end = len(c) if end is None else end
    if end - n < 0:
        return None
    return sum(c[end - n:end]) / n

def panel(rows):
    c = [r["c"] for r in rows]; v = [r["v"] for r in rows]; n = len(c)
    if n < 25:
        return None
    out = {"close": c[-1], "date": rows[-1]["d"], "bars": n}
    for k, name in ((1, "d1"), (5, "w1"), (21, "m1"), (63, "m3"), (126, "m6"), (252, "m12")):
        out[name] = pct(c[-1], c[-1 - k]) if n > k else None
    out["mom_12_1"] = pct(c[-22], c[-253]) if n > 253 else None
    m50, m200 = ma(c, 50), ma(c, 200)
    out["vs50"] = pct(c[-1], m50); out["vs200"] = pct(c[-1], m200)
    out["slope200"] = pct(m200, ma(c, 200, n - 20)) if m200 and n >= 220 else None
    out["slope50"] = pct(m50, ma(c, 50, n - 20)) if m50 and n >= 70 else None
    # 50/200 cross state and age
    state = None; age = None
    if m50 and m200:
        state = "golden" if m50 > m200 else "death"
        age = 0
        for end in range(n, 199, -1):
            a, b = ma(c, 50, end), ma(c, 200, end)
            if (a > b) != (m50 > m200):
                break
            age = n - end + 1
    out["cross"] = state; out["cross_age"] = age
    w = c[-252:] if n >= 252 else c
    hi, lo = max(w), min(w)
    out["from_high"] = pct(c[-1], hi); out["above_low"] = pct(c[-1], lo)
    out["since_high"] = len(w) - 1 - w.index(hi)
    # extension z: today's % vs 200d against its own trailing-year distribution
    if m200 and n >= 200 + 120:
        series = []
        for end in range(max(200, n - 252), n + 1):
            mm = ma(c, 200, end)
            series.append(100.0 * (c[end - 1] / mm - 1.0))
        sd = st.pstdev(series)
        out["ext_z"] = (series[-1] - st.mean(series)) / sd if sd else None
    else:
        out["ext_z"] = None
    rets = [math.log(c[i] / c[i - 1]) for i in range(1, n)]
    out["rv20"] = 100.0 * st.pstdev(rets[-20:]) * math.sqrt(252) if len(rets) >= 20 else None
    out["rv60"] = 100.0 * st.pstdev(rets[-60:]) * math.sqrt(252) if len(rets) >= 60 else None
    trs = [max(rows[i]["h"] - rows[i]["l"], abs(rows[i]["h"] - c[i - 1]), abs(rows[i]["l"] - c[i - 1])) for i in range(1, n)]
    out["atr14_pct"] = 100.0 * (sum(trs[-14:]) / 14) / c[-1] if len(trs) >= 14 else None
    # volume character
    v20 = sum(v[-21:-1]) / 20 if n > 21 and sum(v[-21:-1]) > 0 else None
    out["vol_vs20"] = (v[-1] / v20) if v20 else None
    dist = 0
    for i in range(max(1, n - 25), n):
        if c[i] / c[i - 1] - 1.0 <= -0.002 and v[i] > v[i - 1]:
            dist += 1
    out["dist_days25"] = dist
    up = sum(v[i] for i in range(n - 20, n) if c[i] > c[i - 1]); dn = sum(v[i] for i in range(n - 20, n) if c[i] < c[i - 1])
    out["updown_vol20"] = (up / dn) if dn else None
    # volume–return correlation over 60 sessions (negative = the heavy days are the down days)
    if n > 61 and v20:
        rr = [c[i] / c[i - 1] - 1.0 for i in range(n - 60, n)]; vv = [v[i] for i in range(n - 60, n)]
        mr, mv = st.mean(rr), st.mean(vv)
        cov = sum((a - mr) * (b - mv) for a, b in zip(rr, vv)); den = math.sqrt(sum((a - mr) ** 2 for a in rr) * sum((b - mv) ** 2 for b in vv))
        out["corr_rv60"] = cov / den if den else None
    else:
        out["corr_rv60"] = None
    # overnight vs intraday contributions (log sums, in %)
    def split(k):
        if n <= k:
            return None, None
        on = sum(math.log(rows[i]["o"] / c[i - 1]) for i in range(n - k, n) if rows[i]["o"] > 0)
        intra = sum(math.log(c[i] / rows[i]["o"]) for i in range(n - k, n) if rows[i]["o"] > 0)
        return 100.0 * on, 100.0 * intra
    out["on21"], out["id21"] = split(21)
    out["on63"], out["id63"] = split(63)
    streak = 0
    for i in range(n - 1, 0, -1):
        s = 1 if c[i] > c[i - 1] else -1 if c[i] < c[i - 1] else 0
        if streak == 0:
            streak = s
        elif s == streak // abs(streak):
            streak += s
        else:
            break
    out["streak"] = streak
    return out

def ratio_panel(a, b):
    da = {r["d"]: r["a"] for r in a}; db = {r["d"]: r["a"] for r in b}   # adjusted closes: dividends drop out of the ratio
    ds = sorted(set(da) & set(db))
    r = [da[d] / db[d] for d in ds]; n = len(r)
    if n < 25:
        return None
    out = {"date": ds[-1], "level": r[-1], "bars": n}
    out["m1"] = pct(r[-1], r[-22]) if n > 21 else None
    out["m3"] = pct(r[-1], r[-64]) if n > 63 else None
    m50, m200 = ma(r, 50), ma(r, 200)
    out["vs50"] = pct(r[-1], m50); out["vs200"] = pct(r[-1], m200)
    out["slope200"] = pct(m200, ma(r, 200, n - 20)) if m200 and n >= 220 else None
    w = r[-252:] if n >= 252 else r
    out["pct1y"] = 100.0 * sum(1 for x in w if x <= r[-1]) / len(w)
    out["from_high1y"] = pct(r[-1], max(w))
    return out

def f(x, d=1):
    return "—" if x is None else f"{x:+.{d}f}"

def g(x, d=1):
    return "—" if x is None else f"{x:.{d}f}"

def main():
    root = sys.argv[1]
    tickers = sys.argv[2:] or DEFAULT
    print(f"{'tkr':6}{'close':>9}{'1d':>7}{'1w':>7}{'1m':>7}{'3m':>7}{'12m':>7}{'12-1':>7}{'v50':>7}{'v200':>7}{'s200':>6}{'cross':>8}{'age':>4}"
          f"{'fmHi':>7}{'dHi':>4}{'extZ':>6}{'rv20':>6}{'atr%':>5}{'v/20':>5}{'dd25':>5}{'u/d':>5}{'cRV':>6}{'on21':>6}{'id21':>6}{'on63':>6}{'id63':>6}{'stk':>4}")
    for t in tickers:
        rows = load(root, t)
        if not rows:
            print(f"{t:6} (no file)"); continue
        p = panel(rows)
        if not p:
            print(f"{t:6} (too few bars)"); continue
        print(f"{t:6}{p['close']:9.2f}{f(p['d1']):>7}{f(p['w1']):>7}{f(p['m1']):>7}{f(p['m3']):>7}{f(p['m12']):>7}{f(p['mom_12_1']):>7}"
              f"{f(p['vs50']):>7}{f(p['vs200']):>7}{f(p['slope200']):>6}{(p['cross'] or '—'):>8}{(g(float(p['cross_age']),0) if p['cross_age'] is not None else '—'):>4}"
              f"{f(p['from_high']):>7}{p['since_high']:>4}{f(p['ext_z']):>6}{g(p['rv20']):>6}{g(p['atr14_pct']):>5}{g(p['vol_vs20']):>5}{p['dist_days25']:>5}"
              f"{g(p['updown_vol20']):>5}{f(p['corr_rv60'],2):>6}{f(p['on21']):>6}{f(p['id21']):>6}{f(p['on63']):>6}{f(p['id63']):>6}{p['streak']:>4}")
    print()
    print(f"{'pair':10}{'level':>9}{'1m':>7}{'3m':>7}{'v50':>7}{'v200':>7}{'s200':>6}{'pct1y':>6}{'fmHi1y':>7}  (ratio of adjusted closes)")
    for a, b in PAIRS:
        ra, rb = load(root, a), load(root, b)
        if not ra or not rb:
            print(f"{a}/{b:<5} (missing)"); continue
        q = ratio_panel(ra, rb)
        if not q:
            print(f"{a}/{b:<5} (too few bars)"); continue
        print(f"{a + '/' + b:10}{q['level']:9.4f}{f(q['m1']):>7}{f(q['m3']):>7}{f(q['vs50']):>7}{f(q['vs200']):>7}{f(q['slope200']):>6}{g(q['pct1y'],0):>6}{f(q['from_high1y']):>7}")

if __name__ == "__main__":
    main()
