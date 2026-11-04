# Analog cone backtest

Over the panel from 1880 (k=15, coverage ≥ 80%), under three exclusion rules: same-country (own episode only excluded — leaky across countries in a shared global episode), block-year (all countries within ±5 years excluded) and walk-forward (only candidates whose outcome window closed before the query year — the forecast setting, and the headline). Skill is measured against climatology: AUC 0.5 and band coverage equal to the climatology's mean no information. The same-country rows are kept to show how much of the apparent skill was leakage.

| feature set | queries | crisis AUC | crisis rate: top decile vs base | real equity 3y: ρ, band cover (analog / clim), band width (analog / clim) | rGDP/cap 3y: ρ, cover, width | Δ long rate 3y: ρ, cover, width |
|---|---|---|---|---|---|---|
| all | same-country | 2140 | 0.66 | 25% vs 10% | ρ +0.36 (n=1923), 42% / 50%, 36.2 / 47.1 | ρ +0.42 (n=2086), 46% / 52%, 6.6 / 8.7 | ρ +0.41 (n=2078), 43% / 47%, 1.0 / 1.0 |
| all | block-year | 2140 | 0.54 | 15% vs 10% | ρ +0.20 (n=1924), 39% / 50%, 36.0 / 47.1 | ρ +0.30 (n=2086), 44% / 52%, 6.7 / 8.7 | ρ +0.25 (n=2078), 39% / 47%, 0.9 / 1.0 |
| all | walk-forward | 2079 | 0.59 | 13% vs 10% | ρ +0.20 (n=1863), 31% / 49%, 30.9 / 47.1 | ρ +0.18 (n=2025), 37% / 52%, 6.2 / 8.7 | ρ +0.14 (n=2017), 29% / 46%, 0.7 / 1.0 |
| credit | same-country | 2125 | 0.54 | 15% vs 9% | ρ -0.02 (n=1860), 44% / 50%, 44.3 / 47.1 | ρ +0.21 (n=2077), 44% / 51%, 6.9 / 8.7 | ρ +0.11 (n=2058), 45% / 48%, 1.1 / 1.0 |
| credit | block-year | 2125 | 0.50 | 9% vs 9% | ρ -0.07 (n=1860), 43% / 50%, 43.7 / 47.1 | ρ +0.10 (n=2077), 41% / 51%, 6.9 / 8.7 | ρ +0.01 (n=2058), 43% / 48%, 1.1 / 1.0 |
| credit | walk-forward | 2082 | 0.51 | 7% vs 9% | ρ -0.07 (n=1829), 34% / 49%, 35.7 / 47.1 | ρ +0.08 (n=2034), 43% / 51%, 7.0 / 8.7 | ρ +0.02 (n=2015), 29% / 47%, 0.6 / 1.0 |
| debt | same-country | 2220 | 0.52 | 9% vs 10% | ρ +0.24 (n=1901), 44% / 50%, 39.7 / 47.1 | ρ +0.14 (n=2168), 44% / 52%, 7.5 / 8.7 | ρ +0.29 (n=2160), 44% / 49%, 1.0 / 1.0 |
| debt | block-year | 2220 | 0.42 | 5% vs 10% | ρ +0.17 (n=1901), 42% / 50%, 39.0 / 47.1 | ρ -0.01 (n=2168), 43% / 52%, 7.6 / 8.7 | ρ +0.21 (n=2160), 43% / 49%, 1.0 / 1.0 |
| debt | walk-forward | 2180 | 0.45 | 5% vs 10% | ρ +0.19 (n=1873), 33% / 50%, 30.2 / 47.1 | ρ +0.07 (n=2128), 42% / 52%, 7.1 / 8.7 | ρ +0.20 (n=2120), 28% / 48%, 0.6 / 1.0 |
| rates | same-country | 2372 | 0.64 | 22% vs 10% | ρ +0.26 (n=2052), 43% / 50%, 40.3 / 47.1 | ρ +0.21 (n=2308), 44% / 52%, 7.1 / 8.7 | ρ +0.31 (n=2293), 45% / 49%, 0.9 / 1.0 |
| rates | block-year | 2372 | 0.50 | 10% vs 10% | ρ +0.08 (n=2056), 42% / 50%, 40.7 / 47.1 | ρ +0.09 (n=2312), 43% / 52%, 7.4 / 8.7 | ρ +0.03 (n=2297), 38% / 49%, 0.9 / 1.0 |
| rates | walk-forward | 2312 | 0.51 | 12% vs 10% | ρ +0.06 (n=2022), 33% / 50%, 31.3 / 47.1 | ρ +0.13 (n=2258), 39% / 51%, 6.9 / 8.7 | ρ +0.00 (n=2243), 30% / 48%, 0.6 / 1.0 |
| activity | same-country | 1874 | 0.59 | 13% vs 8% | ρ +0.22 (n=1641), 42% / 48%, 41.8 / 47.1 | ρ +0.35 (n=1820), 45% / 52%, 6.7 / 8.7 | ρ +0.33 (n=1812), 46% / 44%, 1.3 / 1.0 |
| activity | block-year | 1874 | 0.48 | 7% vs 8% | ρ +0.16 (n=1641), 41% / 48%, 41.6 / 47.1 | ρ +0.25 (n=1820), 43% / 52%, 6.9 / 8.7 | ρ +0.28 (n=1812), 45% / 44%, 1.3 / 1.0 |
| activity | walk-forward | 1824 | 0.51 | 8% vs 7% | ρ +0.11 (n=1603), 36% / 47%, 36.7 / 47.1 | ρ +0.17 (n=1770), 41% / 52%, 7.0 / 8.7 | ρ +0.24 (n=1762), 34% / 42%, 0.9 / 1.0 |
| valuation | same-country | 1658 | 0.61 | 17% vs 10% | ρ +0.16 (n=1607), 44% / 50%, 40.7 / 47.1 | ρ +0.02 (n=1610), 42% / 56%, 6.7 / 8.7 | ρ +0.15 (n=1591), 44% / 46%, 1.1 / 1.0 |
| valuation | block-year | 1658 | 0.58 | 14% vs 10% | ρ +0.07 (n=1607), 42% / 50%, 41.0 / 47.1 | ρ -0.10 (n=1610), 41% / 56%, 6.7 / 8.7 | ρ +0.02 (n=1591), 41% / 46%, 1.1 / 1.0 |
| valuation | walk-forward | 1611 | 0.58 | 12% vs 9% | ρ +0.08 (n=1560), 35% / 49%, 32.4 / 47.1 | ρ -0.01 (n=1563), 42% / 55%, 6.6 / 8.7 | ρ -0.02 (n=1544), 25% / 44%, 0.6 / 1.0 |
| credit_change | same-country | 2250 | 0.54 | 16% vs 9% | ρ -0.02 (n=1938), 44% / 50%, 43.0 / 47.1 | ρ +0.09 (n=2199), 43% / 51%, 7.4 / 8.7 | ρ +0.06 (n=2179), 45% / 48%, 1.1 / 1.0 |
| credit_change | block-year | 2250 | 0.51 | 10% vs 9% | ρ -0.05 (n=1938), 43% / 50%, 42.7 / 47.1 | ρ +0.01 (n=2199), 42% / 51%, 7.4 / 8.7 | ρ -0.01 (n=2179), 44% / 48%, 1.1 / 1.0 |
| credit_change | walk-forward | 2206 | 0.51 | 7% vs 9% | ρ -0.07 (n=1910), 36% / 49%, 34.9 / 47.1 | ρ +0.03 (n=2155), 44% / 51%, 7.9 / 8.7 | ρ +0.01 (n=2135), 27% / 47%, 0.6 / 1.0 |

Reading: a crisis AUC above ~0.6 with a top-decile rate several times the base rate means the state vector sorts country-years by what followed; a band coverage near 50% with a narrower band than the climatology's is a cone that is both calibrated and informative. The comparison across feature sets is the point: it says which parts of the state carry information at this horizon, instead of assuming it.
