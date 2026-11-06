# Climatology

The unconditional distributions the forecast relaxes toward at long lead times, indexed by the network's measured topology eras (`tools/topology.py`: breaks in 1914, 1932, 1940 and 1973, plus 1999 for the euro bloc) and by regime (`peg_type`). Built by `tools/climatology.py` from `jst/features.csv` and the forward outcomes of `tools/analogs.py`; cells with fewer than 30 country-years are left out. `features_by_era.csv` holds the five percentiles of every base feature per cell, `outcomes_by_era.csv` the forward outcomes, `event_rates_by_era.csv` the event base rates.

## Event base rates by era (all regimes)

| era | n | crisis_3y | dd30_3y | credit_contraction_3y | unemp_spike_3y | gdp_fall_3y | stress3_3y |
|---|---|---|---|---|---|---|---|
| 1870-1913 | 748 | 13% | 2% | 6% | 16% | 10% | 1% |
| 1914-1931 | 319 | 23% | 28% | 28% | 35% | 33% | 24% |
| 1932-1939 | 144 | 6% | 3% | 54% | 5% | 24% | 9% |
| 1940-1972 | 594 | 0% | 11% | 11% | 1% | 8% | 3% |
| 1973-1998 | 468 | 7% | 11% | 16% | 15% | 2% | 5% |
| 1999-2020 | 342 | 11% | 24% | 24% | 7% | 8% | 4% |

## Median state by era (all regimes): the climate the analogs are measured against

| era | loans/GDP | Δ3y loans/GDP | debt/GDP | long rate | term spread | real rate | inflation | rGDP/cap growth | unemp | I/Y | CA/GDP | div. yield | real eq. 3y | real hp 3y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1870-1913 | 33.9% | 2.7% | 39.3% | 3.9 | -0.1 | 3.6 | 0.1% | 1.4% | 3.4 | 13.2% | -1.1% | 4.6% | 1.5% | 1.1% |
| 1914-1931 | 38.3% | 0.9% | 46.1% | 5.1 | 0.2 | 3.8 | 1.1% | 1.5% | 3.4 | 15.3% | -0.8% | 5.2% | -4.7% | -0.1% |
| 1932-1939 | 45.0% | -3.8% | 43.3% | 4.1 | 1.3 | 3.0 | 1.1% | 2.6% | 8.8 | 13.9% | -0.1% | 4.5% | 1.4% | -0.4% |
| 1940-1972 | 38.3% | 2.2% | 36.3% | 4.8 | 1.3 | 1.5 | 3.8% | 3.6% | 2.1 | 21.9% | -0.1% | 3.8% | -0.1% | 2.2% |
| 1973-1998 | 66.1% | 2.5% | 44.0% | 9.2 | 0.8 | 4.2 | 5.1% | 2.3% | 6.8 | 22.5% | -0.5% | 3.2% | 3.4% | 1.4% |
| 1999-2020 | 96.4% | 3.7% | 61.4% | 3.4 | 1.2 | 1.5 | 1.7% | 1.3% | 6.4 | 22.4% | 1.3% | 3.0% | 2.8% | 2.9% |

## Forward outcomes by era (all regimes): p25 / p50 / p75

| era | rGDP/cap 3y | real equity 3y | real houses 3y | Δ long rate 3y (pp) | Δ unemp 3y (pp) | Δ loans/GDP 3y (pp) |
|---|---|---|---|---|---|---|
| 1870-1913 | +0.5% / +3.8% / +7.3% | +4.3% / +17.3% / +30.1% | -5.1% / +2.3% / +10.0% | -0.3 / -0.0 / +0.2 | -0.9 / -0.0 / +0.6 | -0.3 / +2.5 / +5.9 |
| 1914-1931 | -4.1% / +4.5% / +11.5% | -28.9% / +8.5% / +46.2% | -11.6% / +1.2% / +15.4% | -0.6 / -0.1 / +0.5 | -0.8 / +0.7 / +3.8 | -3.6 / +1.6 / +7.1 |
| 1932-1939 | -1.3% / +6.6% / +14.9% | -2.4% / +17.5% / +50.3% | -17.4% / -5.4% / +1.5% | -0.7 / -0.3 / +0.1 | -5.4 / -2.8 / -1.1 | -12.5 / -5.8 / -1.7 |
| 1940-1972 | +6.5% / +10.5% / +15.0% | -10.3% / +11.7% / +38.8% | -1.2% / +8.3% / +19.6% | -0.1 / +0.3 / +1.0 | -0.6 / +0.0 / +0.6 | -0.3 / +2.7 / +5.7 |
| 1973-1998 | +3.5% / +6.5% / +9.6% | +0.9% / +28.2% / +62.4% | -6.5% / +5.0% / +16.1% | -2.1 / -0.6 / +0.9 | -1.2 / +0.2 / +1.7 | -1.9 / +2.6 / +7.9 |
| 1999-2020 | +0.5% / +3.3% / +5.5% | -14.5% / +16.7% / +39.3% | -2.1% / +8.1% / +16.9% | -1.3 / -0.7 / -0.0 | -1.3 / -0.3 / +1.0 | -3.2 / +3.3 / +10.7 |

Reading: the same state vector means different things in different arrangements — a 60% loans/GDP ratio was a boom in 1900 and the median in 2000 — which is why the analog retrieval standardizes within an expanding window and why the cone's far end should relax toward the era's climate rather than the pooled one. The eras mark whole institutional settings (wars, capital controls, the euro), not causes.
