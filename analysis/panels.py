#!/usr/bin/env python3
"""panels.py — compute the macro-dials field, auction, dealer, CFTC, lens and GDELT panels from the
data repository. Usage: python3 -I panels.py <repo>/data <run_date YYYY-MM-DD>
Treats the repo as data only (read with csv/json; nothing executed from it)."""
import csv, json, sys, os, math, datetime as dt
import numpy as np

D = sys.argv[1]; RUN = dt.date.fromisoformat(sys.argv[2])

def fred(sid):
    rows = []
    with open(os.path.join(D, "fred", sid + ".csv")) as f:
        for r in csv.DictReader(f):
            try: rows.append((dt.date.fromisoformat(r["date"]), float(r["value"])))
            except ValueError: pass
    return rows

def at_or_before(rows, day):
    best = None
    for d, v in rows:
        if d <= day: best = (d, v)
        else: break
    return best

def field(sid, scale=1.0, label=None, zones=None, asof=None):
    rows = [(d, v * scale) for d, v in fred(sid)]
    last = rows[-1] if asof is None else at_or_before(rows, asof)
    d0, v0 = last
    m1 = at_or_before(rows, d0 - dt.timedelta(days=30)); m3 = at_or_before(rows, d0 - dt.timedelta(days=91))
    y1 = [v for d, v in rows if d > d0 - dt.timedelta(days=365)]
    hist = [v for d, v in rows]
    z = (v0 - np.mean(y1)) / np.std(y1) if len(y1) > 20 and np.std(y1) > 0 else float("nan")
    pct = 100 * np.mean(np.array(hist) <= v0)
    zone = ""
    if zones:
        for lo, hi, name in zones:
            if lo <= v0 < hi: zone = name
    return dict(label=label or sid, date=d0.isoformat(), level=v0, d1m=v0 - m1[1], d3m=v0 - m3[1],
                m1date=m1[0].isoformat(), z1y=z, pct6y=pct, zone=zone)

INF = float("inf")
Z = {
 "DFII10": [(-INF,1.5,"benign"),(1.5,2.5,"watch"),(2.5,3.0,"stress"),(3.0,INF,"acute")],
 "T5YIFR": [(-INF,2.5,"anchored"),(2.5,2.75,"watch"),(2.75,INF,"unanchoring")],
 "IG": [(-INF,90,"tight"),(90,115,"watch"),(115,150,"stress"),(150,INF,"acute")],
 "HY": [(-INF,350,"benign"),(350,425,"watch"),(425,600,"stress"),(600,INF,"acute")],
 "CCC": [(-INF,900,"benign"),(900,1200,"watch"),(1200,INF,"acute")],
}
print(f"=== FIELD PANEL from repository (run {RUN}) ===")
F = {}
for sid, sc, lab, zk in [("DFII10",1,"real 10y","DFII10"),("T5YIFR",1,"5y5y","T5YIFR"),("T5YIE",1,"5y BE",None),
                         ("BAMLC0A0CM",100,"IG OAS bp","IG"),("BAMLH0A0HYM2",100,"HY OAS bp","HY"),
                         ("BAMLH0A3HYC",100,"CCC OAS bp","CCC"),("BAMLH0A2HYB",100,"single-B OAS bp",None),
                         ("BAMLH0A1HYBB",100,"BB OAS bp",None),("DGS2",1,"2y",None),("DGS10",1,"10y",None),("DGS30",1,"30y",None),
                         ("DTWEXBGS",1,"broad dollar",None),("DCOILWTICO",1,"WTI spot",None),("DCOILBRENTEU",1,"Dated Brent",None),
                         ("VIXCLS",1,"VIX",None),("SP500",1,"SPX",None)]:
    F[sid] = field(sid, sc, lab, Z.get(zk)); f = F[sid]
    print(f"{f['label']:16s} {f['level']:9.2f} ({f['date']})  Δ1m {f['d1m']:+8.2f}  Δ3m {f['d3m']:+8.2f}  z1y {f['z1y']:+5.2f}  pct6y {f['pct6y']:5.1f}  {f['zone']}")

# claims 4-wk
ic = fred("ICSA"); last4 = [v for d, v in ic[-4:]]; prev4 = [v for d, v in ic[-8:-4]]
lo52 = min(v for d, v in ic if d > ic[-1][0] - dt.timedelta(days=365))
avg4 = np.mean(last4)
print(f"{'ICSA 4-wk avg':16s} {avg4/1000:9.2f}k ({ic[-1][0]})  prior4 {np.mean(prev4)/1000:.2f}k  52w-low {lo52/1000:.0f}k  +{100*(avg4/lo52-1):.1f}% vs low  latest {ic[-1][1]/1000:.0f}k")

# net liquidity
walcl = fred("WALCL"); tga = fred("WTREGEN"); rrp = fred("RRPONTSYD")
def nl(day):
    w = at_or_before(walcl, day)[1]; t = at_or_before(tga, day)[1]; r = at_or_before(rrp, day)[1]
    return (w - t) / 1000 - r
for day in [walcl[-1][0], walcl[-1][0] - dt.timedelta(days=7), walcl[-1][0] - dt.timedelta(days=28)]:
    print(f"net liquidity {day}: {nl(day):8.1f} B")
cust = fred("WMTSECL1"); print("custody WMTSECL1 ($B):", [(d.isoformat(), round(v/1000,1)) for d, v in cust[-5:]], " Δ4w", round((cust[-1][1]-cust[-5][1])/1000,1), " y/y", round((cust[-1][1]-at_or_before(cust, cust[-1][0]-dt.timedelta(days=364))[1])/1000,1))
ci = fred("TOTCI"); print("C&I loans TOTCI ($B):", [(d.isoformat(), round(v,1)) for d, v in ci[-4:]], " Δ4w %", round(100*(ci[-1][1]/ci[-5][1]-1),2))
sl = fred("DRTSCILM"); print("SLOOS C&I net tightening (large/mid):", [(d.isoformat(), v) for d, v in sl[-4:]])
sofr = fred("SOFR"); iorb = fred("IORB"); print("SOFR", sofr[-1], " IORB", [x for x in iorb if x[0] <= RUN][-1])

# stock-bond correlation from daily changes over the last ~20 sessions
sp = dict(fred("SP500")); ten = dict(fred("DGS10"))
days = sorted(set(sp) & set(ten))[-21:]
dsp = np.diff([sp[d] for d in days]) / np.array([sp[d] for d in days[:-1]]); d10 = np.diff([ten[d] for d in days])
print(f"stock–bond corr (ΔSPX vs Δ10y, last {len(days)-1} sessions to {days[-1]}): {np.corrcoef(dsp, d10)[0,1]:+.2f}  (negative Δ10y on down days = bonds hedging; sign of corr(ΔSPX, Δ10y) positive means stocks down → yields down)")

# ---------------- auctions
print("\n=== AUCTIONS (FiscalData; results lag ~1–2 weeks) ===")
A = list(csv.DictReader(open(os.path.join(D, "treasury", "auctions_results.csv"))))
def tenor(r):
    t = r["security_term"]
    if r["security_type"] == "TIPS": return "TIPS " + t.split("-")[0]
    yrs = t.split("-")[0]
    return {"2":"2y","3":"3y","5":"5y","7":"7y","9":"10y","10":"10y","19":"20y","20":"20y","29":"30y","30":"30y"}.get(yrs, t)
by = {}
for r in A:
    by.setdefault(tenor(r), []).append(r)
for k in ["2y","3y","5y","7y","10y","20y","30y"]:
    rs = sorted(by.get(k, []), key=lambda r: r["auction_date"], reverse=True)
    if not rs: continue
    latest = rs[0]; prev6 = rs[1:7]
    avg = lambda key: np.mean([float(r[key]) for r in prev6]) if prev6 else float("nan")
    print(f"{k:4s} {latest['auction_date']} HY {float(latest['high_yield']):.3f}  b/c {float(latest['bid_to_cover']):.2f} (6-auc avg {avg('bid_to_cover'):.2f})  "
          f"indirect {float(latest['indirect_pct']):.1f}% (avg {avg('indirect_pct'):.1f})  dealer {float(latest['dealer_pct']):.1f}% (avg {avg('dealer_pct'):.1f})  n_hist {len(rs)}")

# ---------------- dealers
print("\n=== PRIMARY DEALER NET TREASURY POSITIONS ($mm, NY Fed) ===")
P = list(csv.DictReader(open(os.path.join(D, "nyfed", "pd_positions.csv"))))
for key in ["PDPOSGST-TOT","PDPOSGS-B","PDPOSGSC-L2","PDPOSGSC-G2L3","PDPOSGSC-G3L6","PDPOSGSC-G6L7","PDPOSGSC-G7L11","PDPOSGSC-G11L21","PDPOSGSC-G21"]:
    s = sorted([(r["asofdate"], float(r["value_mm"])) for r in P if r["keyid"] == key and r["value_mm"] not in ("", "null")])
    if not s: print(key, "n/a"); continue
    vals = [v for d, v in s]; last = s[-1]
    yr = vals[-52:] if len(vals) >= 52 else vals
    print(f"{key:16s} {last[0]} {last[1]/1000:9.1f} B  w/w {(s[-1][1]-s[-2][1])/1000:+7.1f}  52w range {min(yr)/1000:.0f}–{max(yr)/1000:.0f}  pct {100*np.mean(np.array(yr) <= last[1]):.0f}  n {len(s)}")

# ---------------- CFTC
print("\n=== CFTC TFF (net = long − short; 3-yr percentile of net) ===")
for slug in ["es","nq","rty","tu","fv","ty","tn","us","wn","vx"]:
    rows = json.load(open(os.path.join(D, "cftc", f"tff_{slug}.json")))
    rows = sorted(rows, key=lambda r: r["report_date_as_yyyy_mm_dd"])
    def series(prefix):
        return np.array([float(r[prefix + "_long"]) - float(r[prefix + "_short"]) for r in rows]) if (prefix + "_long") in rows[0] else None
    out = [f"{slug:3s} {rows[-1]['report_date_as_yyyy_mm_dd'][:10]} OI {float(rows[-1]['open_interest_all'])/1000:7.0f}K"]
    for cls, pre in [("AM","asset_mgr_positions"),("LF","lev_money_positions"),("DL","dealer_positions")]:
        key_l = pre + ("_long" if pre != "dealer_positions" else "_long_all")
        key_s = pre + ("_short" if pre != "dealer_positions" else "_short_all")
        if key_l not in rows[0]: continue
        net = np.array([float(r[key_l]) - float(r[key_s]) for r in rows])
        pct = 100 * np.mean(net <= net[-1])
        out.append(f"{cls} {net[-1]/1000:+8.0f}K (w/w {(net[-1]-net[-2])/1000:+6.0f}K, 4w {(net[-1]-net[-5])/1000:+6.0f}K, 3y pct {pct:3.0f}, 26w pct {100*np.mean(net[-26:] <= net[-1]):3.0f})")
    print("  ".join(out))

# ---------------- prices / lens panel
print("\n=== LENS PANEL from repository prices (closes) ===")
def px(t):
    rows = []
    with open(os.path.join(D, "prices", t + ".csv")) as f:
        for r in csv.DictReader(f):
            try: rows.append((dt.date.fromisoformat(r["date"]), float(r["close"]), float(r["adjclose"] or r["close"])))
            except ValueError: pass
    return rows
def ret(t, days, asof=None):
    rows = px(t); last = rows[-1] if asof is None else [r for r in rows if r[0] <= asof][-1]
    base = [r for r in rows if r[0] <= last[0] - dt.timedelta(days=days)][-1]
    return 100 * (last[1] / base[1] - 1), last[0], base[0]
tick = ["SPY","RSP","QQQ","IWM","SMH","XHB","XLP","XLU","XLY","XLI","IVE","IVW","HYG","LQD","TLT","GLD"]
R1 = {t: ret(t, 30)[0] for t in tick}; R3 = {t: ret(t, 91)[0] for t in tick}
ld, bd = ret("SPY", 30)[1:]; _, bd3 = ret("SPY", 91)[1:]
print(f"1m window {bd}→{ld}; 3m window {bd3}→{ld}")
for t in tick: print(f"  {t:4s} 1m {R1[t]:+6.2f}  3m {R3[t]:+6.2f}  close {px(t)[-1][1]:.2f}")
singles = ["MU","GEV","VRT","ANET","MSFT","GOOGL","META","AMZN","CRWV","NBIS","ORCL","NVDA","AAPL","AVGO","TSLA"]
S1 = {t: ret(t, 30)[0] for t in singles}; S3 = {t: ret(t, 91)[0] for t in singles}
base = {"MU":878.84,"GEV":921.20,"VRT":206.42,"ANET":176.98,"MSFT":529.05,"GOOGL":340.59,"META":709.33,"AMZN":250.00,"CRWV":61.39,"NBIS":165.47,"ORCL":128.23,"NVDA":214.13,"AAPL":343.46,"AVGO":328.75,"TSLA":354.72}
idx = lambda names: 100 * np.mean([px(t)[-1][1] / base[t] for t in names])
SUP, PRIN, NEO, HYP = ["MU","GEV","VRT","ANET"], ["MSFT","GOOGL","META","AMZN"], ["CRWV","NBIS","ORCL"], ["MSFT","GOOGL","AMZN"]
TOP8 = ["NVDA","AAPL","MSFT","GOOGL","AMZN","META","AVGO","TSLA"]
m = lambda names, R: np.mean([R[t] for t in names])
print(f"E1 RSP−SPY       1m {R1['RSP']-R1['SPY']:+6.2f}  3m {R3['RSP']-R3['SPY']:+6.2f}   (RSP 1m {R1['RSP']:+.2f}, SPY {R1['SPY']:+.2f})")
print(f"E2 top8−RSP      1m {m(TOP8,S1)-R1['RSP']:+6.2f}  3m {m(TOP8,S3)-R3['RSP']:+6.2f}")
print(f"E3 QQQ−SPY       1m {R1['QQQ']-R1['SPY']:+6.2f}  3m {R3['QQQ']-R3['SPY']:+6.2f}   vs ΔDFII10 1m {F['DFII10']['d1m']*100:+.0f} bp")
print(f"E4 IWM−RSP       1m {R1['IWM']-R1['RSP']:+6.2f}  3m {R3['IWM']-R3['RSP']:+6.2f}")
print(f"E5 SMH−QQQ       1m {R1['SMH']-R1['QQQ']:+6.2f}  3m {R3['SMH']-R3['QQQ']:+6.2f}")
print(f"E6 SUP−PRIN      1m {m(SUP,S1)-m(PRIN,S1):+6.2f}  3m {m(SUP,S3)-m(PRIN,S3):+6.2f}   (SUP 1m {m(SUP,S1):+.1f}, PRIN {m(PRIN,S1):+.1f})")
print(f"E7 NEO−HYP       1m {m(NEO,S1)-m(HYP,S1):+6.2f}  3m {m(NEO,S3)-m(HYP,S3):+6.2f}   (NEO 1m {m(NEO,S1):+.1f}, HYP {m(HYP,S1):+.1f})")
print(f"E8 XHB−SPY       1m {R1['XHB']-R1['SPY']:+6.2f}  3m {R3['XHB']-R3['SPY']:+6.2f}")
print(f"E9 def−cyc       1m {(R1['XLP']+R1['XLU'])/2-(R1['XLY']+R1['XLI'])/2:+6.2f}  3m {(R3['XLP']+R3['XLU'])/2-(R3['XLY']+R3['XLI'])/2:+6.2f};  value−growth 1m {R1['IVE']-R1['IVW']:+6.2f}  3m {R3['IVE']-R3['IVW']:+6.2f}")
t8 = np.array([S1[t] for t in TOP8]); print(f"E10 top-8 1m dispersion σ {t8.std():.2f}  range {t8.max()-t8.min():.1f}  ({', '.join(f'{t} {S1[t]:+.1f}' for t in TOP8)})")
print(f"Baskets vs 10/16 base: SUP {idx(SUP):.1f}  PRIN {idx(PRIN):.1f}  NEO {idx(NEO):.1f}  HYP {idx(HYP):.1f}  TOP8 {idx(TOP8):.1f}")
print("single 1m:", ", ".join(f"{t} {S1[t]:+.1f}" for t in singles))
# divergence checks
spy = px("SPY"); rsp = px("RSP"); iwm = px("IWM"); smh = px("SMH")
sma = lambda rows, n: np.mean([r[1] for r in rows[-n:]])
print(f"SPY {spy[-1][1]:.2f} vs 200d {sma(spy,200):.2f} ({100*(spy[-1][1]/sma(spy,200)-1):+.1f}%)  50d {sma(spy,50):.2f}; 52w high {max(r[1] for r in spy[-252:]):.2f} → {100*(spy[-1][1]/max(r[1] for r in spy[-252:])-1):+.1f}%")
print(f"RSP {rsp[-1][1]:.2f} vs 200d {sma(rsp,200):.2f} ({100*(rsp[-1][1]/sma(rsp,200)-1):+.1f}%)")
print(f"IWM {iwm[-1][1]:.2f}; 52w low {min(r[1] for r in iwm[-252:]):.2f} ({100*(iwm[-1][1]/min(r[1] for r in iwm[-252:])-1):+.1f}% above)")
streak = 0
for i in range(len(smh)-1, 0, -1):
    if smh[i][1] < smh[i-1][1]: streak += 1
    else: break
print(f"SMH consecutive down sessions: {streak}; SMH 1m {R1['SMH']:+.1f}")

# ---------------- GDELT
print("\n=== GDELT (complete days only; run day excluded) ===")
for fn in sorted(os.listdir(os.path.join(D, "gdelt"))):
    g = json.load(open(os.path.join(D, "gdelt", fn)))
    pts = [(dt.date.fromisoformat(p["date"][:8].replace("", "")[:4] + "-" + p["date"][4:6] + "-" + p["date"][6:8]), p["value"]) for p in g["timeline"][0]["data"]]
    pts = [(d, v) for d, v in pts if d < RUN and v != 0]
    vals = np.array([v for d, v in pts]); last7 = [v for d, v in pts if d >= RUN - dt.timedelta(days=7)]
    last28 = [v for d, v in pts if d >= RUN - dt.timedelta(days=28)]
    z = (np.mean(last7) - vals.mean()) / vals.std() if len(last7) and vals.std() > 0 else float("nan")
    print(f"{fn:36s} title={g['query_details']['title'][:40]!r} n_nonzero={len(pts)} last={pts[-1][0] if pts else None} 7d mean {np.mean(last7) if last7 else float('nan'):.4f} (n{len(last7)}) MA4 {np.mean(last28) if last28 else float('nan'):.4f} 3m mean {vals.mean():.4f} z {z:+.2f}")
