"""Walk-forward nearest-neighbour scoring and forward targets, shared by analog_test2.py and label_test.py.

walk_forward(X, isos, years, horizon, k, min_cov, from_year) -> for each row, the mean target of its k nearest
candidates, where candidates are country-years whose outcome window closed before the query year (year_c + horizon
< year_q), never the query's own country within +-5 years, one per country within +-5 years, and z-scores are
computed from rows with year <= query year only (expanding window). Nothing from the query year or later is used.
"""
import numpy as np


def robust_scale(M):
    med = np.nanmedian(M, axis=0)
    mad = np.nanmedian(np.abs(M - med), axis=0) * 1.4826
    sd = np.nanstd(M, axis=0)
    mad = np.where((mad == 0) | np.isnan(mad), np.where((sd == 0) | np.isnan(sd), 1.0, sd), mad)
    return med, mad


def walk_forward_neighbors(X, isos, years, horizon=3, k=15, min_cov=0.6, from_year=1880, mode="walk-forward"):
    """Return a list (per row) of neighbour index arrays (None where no prediction)."""
    n, F = X.shape
    isos = np.asarray(isos); years = np.asarray(years)
    out = [None] * n
    order_years = sorted(set(years.tolist()))
    for t in order_years:
        if t < from_year:
            continue
        hist = years <= t
        med, mad = robust_scale(X[hist])
        Z = (X - med) / mad
        if mode == "walk-forward":
            cand_mask = (years + horizon) < t
        elif mode == "block-year":
            cand_mask = np.abs(years - t) > 5
        else:  # same-country only
            cand_mask = np.ones(n, dtype=bool)
        cand = np.where(cand_mask)[0]
        if len(cand) < k:
            continue
        Zc = Z[cand]
        for qi in np.where(years == t)[0]:
            zq = Z[qi]
            if np.sum(~np.isnan(zq)) / F < min_cov:
                continue
            both = ~np.isnan(zq) & ~np.isnan(Zc)
            n_both = both.sum(axis=1)
            d2 = np.where(both, (Zc - zq) ** 2, 0.0).sum(axis=1)
            dist = np.sqrt(d2 / np.maximum(n_both, 1))
            dist[(n_both / F) < min_cov] = np.inf
            same = (isos[cand] == isos[qi]) & (np.abs(years[cand] - t) <= 5)
            dist[same] = np.inf
            order = np.argsort(dist)
            picked, taken = [], []
            for j in order:
                if not np.isfinite(dist[j]):
                    break
                ci = cand[j]
                if any(isos[ci] == isos[tk] and abs(years[ci] - years[tk]) <= 5 for tk in taken):
                    continue
                picked.append(ci); taken.append(ci)
                if len(picked) >= k:
                    break
            if len(picked) >= k // 2:
                out[qi] = np.array(picked)
    return out


def predict(neighbors, target):
    """Mean target over neighbours (ignoring NaN); None if fewer than 5 valid."""
    preds = []
    for nb in neighbors:
        if nb is None:
            preds.append(None); continue
        v = target[nb]; v = v[~np.isnan(v)]
        preds.append(float(v.mean()) if len(v) >= 5 else None)
    return preds


def auc(scores, labels):
    pairs = [(s, l) for s, l in zip(scores, labels) if s is not None and l is not None and not np.isnan(l)]
    pos = [s for s, l in pairs if l == 1]; neg = [s for s, l in pairs if l == 0]
    if not pos or not neg:
        return None, len(pos), len(neg)
    allv = sorted(pairs, key=lambda t: t[0])
    ranks = {}; i = 0
    while i < len(allv):
        j = i
        while j < len(allv) and allv[j][0] == allv[i][0]:
            j += 1
        r = (i + j + 1) / 2.0
        for kk in range(i, j):
            ranks[kk] = r
        i = j
    rank_pos = sum(ranks[kk] for kk, (s, l) in enumerate(allv) if l == 1)
    return (rank_pos - len(pos) * (len(pos) + 1) / 2.0) / (len(pos) * len(neg)), len(pos), len(neg)


def top_decile(scores, labels):
    pl = [(s, l) for s, l in zip(scores, labels) if s is not None and l is not None and not np.isnan(l)]
    if not pl:
        return None, None
    base = sum(l for _, l in pl) / len(pl)
    top = sorted(pl, key=lambda t: -t[0])[: max(1, len(pl) // 10)]
    return sum(l for _, l in top) / len(top), base


# ----------------------------------------------------------------------------------------------- forward targets
def build_targets(jst, isos, years):
    """Targets per row, all censored (NaN) unless every year in the window exists."""
    def g(i, y, k):
        r = jst.get((i, y))
        return np.nan if r is None or r.get(k) is None else float(r[k])

    T = {}
    n = len(isos)
    for h in (1, 2, 3, 4, 5):
        T[f"crisis_{h}y"] = np.full(n, np.nan)
    for name in ("dd30_3y", "credit_contraction_3y", "unemp_spike_3y", "gdp_fall_3y", "stress3_3y"):
        T[name] = np.full(n, np.nan)
    for idx, (i, y) in enumerate(zip(isos, years)):
        cr = [g(i, y + h, "crisisJST") for h in range(1, 6)]
        for h in (1, 2, 3, 4, 5):
            if not any(np.isnan(v) for v in cr[:h]):
                T[f"crisis_{h}y"][idx] = 1.0 if any(v == 1 for v in cr[:h]) else 0.0
        # real equity drawdown >= 30% within 3y (cumulative real total return path)
        path, ok = 1.0, True; hit = False
        for h in (1, 2, 3):
            r, c0, c1 = g(i, y + h, "eq_tr"), g(i, y + h - 1, "cpi"), g(i, y + h, "cpi")
            if np.isnan(r) or np.isnan(c0) or np.isnan(c1) or c0 == 0:
                ok = False; break
            path *= (1 + r) / (c1 / c0)
            if path <= 0.70:
                hit = True
        if ok:
            T["dd30_3y"][idx] = 1.0 if hit else 0.0
        # credit contraction: loans/GDP falls >= 5 pp of GDP at any point within 3y
        l0, g0 = g(i, y, "tloans"), g(i, y, "gdp")
        if not np.isnan(l0) and not np.isnan(g0) and g0:
            vals, ok = [], True
            for h in (1, 2, 3):
                lh, gh = g(i, y + h, "tloans"), g(i, y + h, "gdp")
                if np.isnan(lh) or np.isnan(gh) or not gh:
                    ok = False; break
                vals.append(lh / gh - l0 / g0)
            if ok:
                T["credit_contraction_3y"][idx] = 1.0 if min(vals) <= -0.05 else 0.0
        # unemployment spike >= 3 pp within 3y
        u0 = g(i, y, "unemp")
        if not np.isnan(u0):
            us = [g(i, y + h, "unemp") for h in (1, 2, 3)]
            if not any(np.isnan(u) for u in us):
                T["unemp_spike_3y"][idx] = 1.0 if max(us) - u0 >= 3.0 else 0.0
        # real GDP per capita falls >= 5% cumulative within 3y
        r0 = g(i, y, "rgdpmad")
        if not np.isnan(r0) and r0:
            rs = [g(i, y + h, "rgdpmad") for h in (1, 2, 3)]
            if not any(np.isnan(x) for x in rs):
                T["gdp_fall_3y"][idx] = 1.0 if min(rs) / r0 - 1 <= -0.05 else 0.0
        # measured stress composite: in any year u of t+1..t+3, at least 3 of 5 conditions
        scores, ok = [], True
        for h in (1, 2, 3):
            u = y + h
            r, c0, c1 = g(i, u, "eq_tr"), g(i, u - 1, "cpi"), g(i, u, "cpi")
            req = np.nan if np.isnan(r) or np.isnan(c0) or np.isnan(c1) or c0 == 0 else (1 + r) / (c1 / c0) - 1
            rg0, rg1 = g(i, u - 1, "rgdpmad"), g(i, u, "rgdpmad")
            rg = np.nan if np.isnan(rg0) or np.isnan(rg1) or not rg0 else rg1 / rg0 - 1
            du = g(i, u, "unemp") - g(i, u - 1, "unemp")
            l1, g1, l0_, g0_ = g(i, u, "tloans"), g(i, u, "gdp"), g(i, u - 1, "tloans"), g(i, u - 1, "gdp")
            dl = np.nan if any(np.isnan(v) for v in (l1, g1, l0_, g0_)) or not g1 or not g0_ else l1 / g1 - l0_ / g0_
            dlev = g(i, u, "lev") - g(i, u - 1, "lev")
            conds = [(req, lambda v: v <= -0.20), (rg, lambda v: v <= -0.02), (du, lambda v: v >= 1.5),
                     (dl, lambda v: v <= -0.02), (dlev, lambda v: v <= -0.7)]
            avail = [(v, f) for v, f in conds if not np.isnan(v)]
            if len(avail) < 3:
                ok = False; break
            scores.append(sum(1 for v, f in avail if f(v)))
        if ok:
            T["stress3_3y"][idx] = 1.0 if max(scores) >= 3 else 0.0
    return T
