# Analog cone backtest

Leave-one-episode-out over the panel from 1880 (k=15, own country within ±5 years excluded, coverage ≥ 80%). Skill is measured against climatology: AUC 0.5 and band coverage equal to the climatology's mean no information.

| feature set | queries | crisis AUC | crisis rate: top decile vs base | real equity 3y: ρ, band cover (analog / clim), band width (analog / clim) | rGDP/cap 3y: ρ, cover, width | Δ long rate 3y: ρ, cover, width |
|---|---|---|---|---|---|---|
| all | 2140 | 0.66 | 26% vs 9% | ρ +0.36 (n=1923), 42% / 50%, 36.2 / 47.1 | ρ +0.42 (n=2086), 46% / 52%, 6.6 / 8.7 | ρ +0.41 (n=2078), 43% / 47%, 1.0 / 1.0 |
| credit | 2125 | 0.55 | 16% vs 9% | ρ -0.02 (n=1860), 44% / 50%, 44.3 / 47.1 | ρ +0.21 (n=2077), 44% / 51%, 6.9 / 8.7 | ρ +0.11 (n=2058), 45% / 48%, 1.1 / 1.0 |
| debt | 2220 | 0.51 | 9% vs 9% | ρ +0.24 (n=1901), 44% / 50%, 39.7 / 47.1 | ρ +0.14 (n=2168), 44% / 52%, 7.5 / 8.7 | ρ +0.29 (n=2160), 44% / 49%, 1.0 / 1.0 |
| rates | 2372 | 0.65 | 21% vs 10% | ρ +0.26 (n=2052), 43% / 50%, 40.3 / 47.1 | ρ +0.21 (n=2308), 44% / 52%, 7.1 / 8.7 | ρ +0.31 (n=2293), 45% / 49%, 0.9 / 1.0 |
| activity | 1874 | 0.59 | 13% vs 8% | ρ +0.22 (n=1641), 42% / 48%, 41.8 / 47.1 | ρ +0.35 (n=1820), 45% / 52%, 6.7 / 8.7 | ρ +0.33 (n=1812), 46% / 44%, 1.3 / 1.0 |
| valuation | 1658 | 0.61 | 17% vs 9% | ρ +0.16 (n=1607), 44% / 50%, 40.7 / 47.1 | ρ +0.02 (n=1610), 42% / 56%, 6.7 / 8.7 | ρ +0.15 (n=1591), 44% / 46%, 1.1 / 1.0 |

Reading: a crisis AUC above ~0.6 with a top-decile rate several times the base rate means the state vector sorts country-years by what followed; a band coverage near 50% with a narrower band than the climatology's is a cone that is both calibrated and informative. The comparison across feature sets is the point: it says which parts of the state carry information at this horizon, instead of assuming it.
