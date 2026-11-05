# Topology test — nodes coming and going from subnets

Subnets are read from the JST regime columns (peg_type, peg_base): the countries sharing a base currency at t. Features in `jst/topology.csv` (built by `tools/topology.py`); all computable at t.

**Topology breaks** (years in which at least a third of the countries with a regime recorded changed state): 1914 (17 of 17), 1932 (7 of 18), 1940 (17 of 18), 1973 (13 of 18).

## 1. Climatology by topology (walk-forward conditional event rate as the forecast)

| target | pooled (varies only with t) | by peg_type | by peg_type x bloc size x moved recently |
|---|---|---|---|
| dd30_3y | 0.42 | 0.45 | 0.49 |
| credit_contraction_3y | 0.40 | 0.49 | 0.54 |
| gdp_fall_3y | 0.42 | 0.49 | 0.54 |
| unemp_spike_3y | 0.48 | 0.40 | 0.37 |
| crisis_3y | 0.45 | 0.49 | 0.55 |

The pooled column is the no-skill reference (its rate changes only with the query year). The difference is what knowing the node's place in the topology is worth before any state variable is read.

## 2. Event rates in the three years after a topology break

| target | after a break (n) | other years (n) |
|---|---|---|
| dd30_3y | 27% (192) | 11% (2032) |
| credit_contraction_3y | 48% (183) | 14% (2172) |
| gdp_fall_3y | 30% (213) | 10% (2399) |
| unemp_spike_3y | 12% (154) | 12% (1714) |
| crisis_3y | 4% (213) | 10% (2402) |

## 3. The climate of each topology era (event base rates between measured breaks)

| era | rows | dd30_3y | credit_contraction_3y | gdp_fall_3y | unemp_spike_3y | crisis_3y |
|---|---|---|---|---|---|---|
| 1870-1913 | 792 | 2% | 6% | 10% | 16% | 13% |
| 1914-1931 | 324 | 28% | 28% | 33% | 35% | 23% |
| 1932-1939 | 144 | 3% | 54% | 24% | 5% | 6% |
| 1940-1972 | 594 | 11% | 11% | 8% | 1% | 0% |
| 1973-2020 | 864 | 16% | 20% | 5% | 11% | 9% |

These are the unconditional rates a forecast relaxes toward at long lead times, and they differ by an order of magnitude between arrangements; the arrangement is a marker of the whole institutional setting (wars, capital controls, financial repression, the euro), not a cause on its own.

## 4. Pooled single-feature AUC (descriptive, in-sample)

| feature | dd30_3y | credit_contraction_3y | gdp_fall_3y | unemp_spike_3y | crisis_3y |
|---|---|---|---|---|---|
| in_peg | 0.45 | 0.45 | 0.43 | 0.54 | 0.47 |
| is_base | 0.49 | 0.48 | 0.48 | 0.51 | 0.49 |
| bloc_size | 0.42 | 0.38 | 0.36 | 0.41 | 0.44 |
| bloc_share | 0.42 | 0.38 | 0.36 | 0.41 | 0.44 |
| bloc_tenure | 0.42 | 0.47 | 0.38 | 0.44 | 0.49 |
| regime_change_3y | 0.56 | 0.56 | 0.57 | 0.51 | 0.47 |
| bloc_churn_3y | 0.48 | 0.47 | 0.41 | 0.43 | 0.34 |
| base_changed_5y | 0.59 | 0.55 | 0.60 | 0.50 | 0.48 |
| n_blocs | 0.48 | 0.42 | 0.37 | 0.42 | 0.38 |
| panel_peg_share | 0.43 | 0.31 | 0.39 | 0.51 | 0.50 |
| panel_changes_3y | 0.52 | 0.59 | 0.59 | 0.54 | 0.37 |
| years_since_break | 0.45 | 0.40 | 0.30 | 0.39 | 0.51 |

Below 0.5 means the feature's high values go with fewer events (read 1 − AUC for the strength).
