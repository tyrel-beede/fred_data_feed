# Lead-lag: the path into T versus the point at T

Walk-forward k=15 nearest-neighbour harness (expanding-window scaling, own episode excluded, one episode per country), 3-year targets. AUC 0.5 = no skill.

## 1. Trajectory analogs

| design (features) | crisis_3y | dd30_3y | credit_contraction_3y | gdp_fall_3y | unemp_spike_3y |
|---|---|---|---|---|---|
| point T (20) | 0.53 (top 13% vs 9%) | 0.61 (top 26% vs 12%) | 0.64 (top 40% vs 17%) | 0.59 (top 18% vs 11%) | 0.58 (top 19% vs 10%) |
| path T, T-1 (40) | 0.50 (top 8% vs 9%) | 0.58 (top 21% vs 12%) | 0.64 (top 37% vs 17%) | 0.61 (top 23% vs 11%) | 0.53 (top 13% vs 10%) |
| path T, T-1, T-2 (60) | 0.51 (top 8% vs 9%) | 0.55 (top 19% vs 12%) | 0.62 (top 36% vs 17%) | 0.61 (top 22% vs 11%) | 0.53 (top 10% vs 10%) |
| point + network (30) | 0.55 (top 13% vs 10%) | 0.67 (top 36% vs 13%) | 0.66 (top 46% vs 17%) | 0.60 (top 24% vs 11%) | 0.58 (top 14% vs 9%) |
| path T, T-1 + network at T (50) | 0.52 (top 13% vs 10%) | 0.63 (top 32% vs 12%) | 0.66 (top 40% vs 17%) | 0.62 (top 21% vs 11%) | 0.56 (top 17% vs 10%) |
| point + 1y and 2y differences (60) | 0.53 (top 10% vs 9%) | 0.57 (top 17% vs 12%) | 0.64 (top 42% vs 17%) | 0.57 (top 18% vs 11%) | 0.55 (top 13% vs 10%) |
| point + network + 5 selected leads (35) | 0.56 (top 13% vs 9%) | 0.66 (top 35% vs 12%) | 0.67 (top 47% vs 17%) | 0.60 (top 25% vs 11%) | 0.57 (top 13% vs 10%) |

## 2. Lead profiles: single feature at lag k (years before T) as a predictor of the event in T+1..T+3

AUC oriented (max of AUC and 1−AUC; 'high'/'low' says which direction of the feature predicts the event); ✓ = the pre-1950 and post-1950 halves agree on the direction, ✗ = they disagree. Features sorted by their best lag.

### dd30_3y

| feature | k=0 | k=1 | k=2 | k=3 | k=4 | best lag |
|---|---|---|---|---|---|---|
| r_minus_g | 0.70 l✓ | 0.66 l✓ | 0.61 l✓ | 0.59 l✓ | 0.55 l✗ | 0 |
| eq_dp | 0.70 l✓ | 0.67 l✓ | 0.64 l✓ | 0.63 l✓ | 0.63 l✓ | 0 |
| cpi_infl | 0.68 h✓ | 0.64 h✓ | 0.61 h✗ | 0.60 h✗ | 0.58 h✗ | 0 |
| real_ltrate_expost | 0.68 l✓ | 0.64 l✓ | 0.62 l✓ | 0.59 l✗ | 0.57 l✗ | 0 |
| iy | 0.61 h✓ | 0.58 h✓ | 0.56 h✓ | 0.55 h✓ | 0.56 h✓ | 0 |
| real_eq_capgain_3y | 0.55 h✗ | 0.58 h✗ | 0.53 h✗ | 0.51 l✗ | 0.51 l✗ | 1 |
| d1_unemp | 0.58 l✓ | 0.56 l✓ | 0.52 l✓ | 0.51 l✓ | 0.51 l✗ | 0 |
| ltrate | 0.57 h✗ | 0.54 h✗ | 0.54 h✗ | 0.55 h✗ | 0.55 h✓ | 0 |
| d5_debt_gdp | 0.57 l✓ | 0.53 l✗ | 0.51 l✗ | 0.51 h✓ | 0.51 h✓ | 0 |
| deficit_gdp | 0.51 h✗ | 0.52 h✗ | 0.54 h✗ | 0.56 h✗ | 0.56 h✓ | 4 |
| loans_gdp | 0.54 h✗ | 0.54 h✗ | 0.54 h✗ | 0.55 h✓ | 0.55 h✓ | 4 |
| term_spread | 0.52 h✗ | 0.55 h✓ | 0.54 h✓ | 0.54 h✓ | 0.54 h✓ | 1 |
| ca_gdp | 0.50 h✗ | 0.54 h✓ | 0.54 h✗ | 0.55 h✗ | 0.55 h✗ | 3 |
| unemp | 0.55 l✓ | 0.52 l✗ | 0.51 l✗ | 0.50 l✗ | 0.50 h✗ | 0 |
| d5_loans_gdp | 0.50 h✗ | 0.52 l✗ | 0.54 l✗ | 0.53 l✗ | 0.52 l✗ | 2 |
| rgdp_pc_growth | 0.53 h✗ | 0.54 h✗ | 0.53 h✗ | 0.52 h✗ | 0.50 h✓ | 1 |
| d3_loans_gdp | 0.53 h✗ | 0.50 l✗ | 0.53 l✗ | 0.54 l✗ | 0.54 l✗ | 3 |
| real_hp_growth_3y | 0.54 h✗ | 0.50 l✗ | 0.53 l✗ | 0.54 l✗ | 0.51 l✗ | 0 |
| debt_gdp | 0.51 l✓ | 0.51 h✓ | 0.52 h✓ | 0.53 h✓ | 0.53 h✓ | 4 |
| mort_gdp | 0.51 h✗ | 0.52 h✗ | 0.52 h✗ | 0.52 h✓ | 0.53 h✓ | 4 |

### credit_contraction_3y

| feature | k=0 | k=1 | k=2 | k=3 | k=4 | best lag |
|---|---|---|---|---|---|---|
| loans_gdp | 0.70 h✓ | 0.71 h✓ | 0.72 h✓ | 0.73 h✓ | 0.73 h✓ | 3 |
| real_hp_growth_3y | 0.67 l✓ | 0.63 l✓ | 0.59 l✓ | 0.55 l✓ | 0.53 l✗ | 0 |
| deficit_gdp | 0.67 h✓ | 0.61 h✓ | 0.57 h✓ | 0.55 h✓ | 0.53 h✓ | 0 |
| mort_gdp | 0.63 h✓ | 0.64 h✓ | 0.65 h✓ | 0.65 h✓ | 0.65 h✓ | 3 |
| real_eq_capgain_3y | 0.63 l✓ | 0.65 l✓ | 0.61 l✓ | 0.56 l✓ | 0.51 l✓ | 1 |
| unemp | 0.65 h✓ | 0.64 h✓ | 0.62 h✓ | 0.60 h✓ | 0.58 h✓ | 0 |
| d5_debt_gdp | 0.64 h✓ | 0.60 h✓ | 0.58 h✓ | 0.58 h✓ | 0.56 h✗ | 0 |
| d3_loans_gdp | 0.62 l✓ | 0.57 l✓ | 0.52 l✗ | 0.50 h✗ | 0.54 h✗ | 0 |
| d5_loans_gdp | 0.59 l✓ | 0.54 l✗ | 0.51 h✗ | 0.53 h✗ | 0.55 h✗ | 0 |
| rgdp_pc_growth | 0.58 l✓ | 0.59 l✓ | 0.59 l✓ | 0.56 l✓ | 0.56 l✓ | 1 |
| r_minus_g | 0.55 h✗ | 0.58 h✓ | 0.56 h✓ | 0.55 h✓ | 0.54 h✓ | 1 |
| d1_unemp | 0.55 h✗ | 0.56 h✓ | 0.55 h✓ | 0.53 h✓ | 0.52 h✓ | 1 |
| iy | 0.54 l✗ | 0.52 l✗ | 0.50 l✗ | 0.51 h✓ | 0.52 h✓ | 0 |
| debt_gdp | 0.53 h✗ | 0.50 h✗ | 0.52 l✗ | 0.53 l✗ | 0.54 l✗ | 4 |
| term_spread | 0.54 h✓ | 0.52 h✗ | 0.50 h✗ | 0.50 h✗ | 0.51 l✗ | 0 |
| ca_gdp | 0.50 h✓ | 0.52 l✗ | 0.54 l✓ | 0.53 l✓ | 0.52 l✗ | 2 |
| ltrate | 0.53 l✗ | 0.53 l✗ | 0.52 l✓ | 0.52 l✓ | 0.53 l✗ | 0 |
| cpi_infl | 0.50 l✗ | 0.52 l✓ | 0.51 l✗ | 0.51 l✗ | 0.52 l✗ | 4 |
| eq_dp | 0.52 h✗ | 0.52 h✗ | 0.52 h✗ | 0.51 h✗ | 0.51 h✗ | 1 |
| real_ltrate_expost | 0.51 l✓ | 0.51 h✓ | 0.50 h✗ | 0.51 l✗ | 0.50 h✗ | 0 |

### crisis_3y

| feature | k=0 | k=1 | k=2 | k=3 | k=4 | best lag |
|---|---|---|---|---|---|---|
| d3_loans_gdp | 0.65 h✓ | 0.62 h✓ | 0.57 h✓ | 0.53 h✓ | 0.50 h✓ | 0 |
| term_spread | 0.64 l✓ | 0.60 l✓ | 0.58 l✗ | 0.58 l✗ | 0.61 l✓ | 0 |
| d5_loans_gdp | 0.63 h✓ | 0.58 h✓ | 0.55 h✓ | 0.53 h✓ | 0.52 h✓ | 0 |
| real_hp_growth_3y | 0.61 h✓ | 0.61 h✓ | 0.57 h✓ | 0.56 h✓ | 0.57 h✓ | 0 |
| d5_debt_gdp | 0.57 l✓ | 0.58 l✓ | 0.59 l✓ | 0.59 l✓ | 0.60 l✓ | 4 |
| ca_gdp | 0.60 l✓ | 0.57 l✓ | 0.54 l✗ | 0.51 l✗ | 0.51 l✗ | 0 |
| iy | 0.55 l✓ | 0.57 l✓ | 0.58 l✓ | 0.59 l✓ | 0.58 l✗ | 3 |
| d1_unemp | 0.53 l✗ | 0.51 h✗ | 0.56 h✓ | 0.57 h✓ | 0.52 h✓ | 3 |
| deficit_gdp | 0.57 l✓ | 0.55 l✓ | 0.53 l✓ | 0.53 l✓ | 0.54 l✓ | 0 |
| real_eq_capgain_3y | 0.55 h✓ | 0.56 h✓ | 0.53 h✓ | 0.52 l✗ | 0.52 l✗ | 1 |
| rgdp_pc_growth | 0.52 l✗ | 0.51 l✓ | 0.55 l✓ | 0.53 l✗ | 0.55 l✗ | 2 |
| eq_dp | 0.55 h✗ | 0.55 h✗ | 0.54 h✗ | 0.53 h✗ | 0.53 h✓ | 0 |
| unemp | 0.53 l✗ | 0.52 l✗ | 0.52 l✗ | 0.53 l✗ | 0.55 l✗ | 4 |
| r_minus_g | 0.52 h✓ | 0.50 l✗ | 0.51 h✗ | 0.53 h✗ | 0.54 h✗ | 4 |
| ltrate | 0.51 h✗ | 0.50 h✗ | 0.50 h✗ | 0.52 h✗ | 0.54 h✓ | 4 |
| mort_gdp | 0.52 l✗ | 0.53 l✗ | 0.53 l✗ | 0.53 l✗ | 0.53 l✗ | 4 |
| real_ltrate_expost | 0.53 h✓ | 0.52 h✓ | 0.51 h✗ | 0.52 h✗ | 0.52 h✓ | 0 |
| cpi_infl | 0.53 l✗ | 0.52 l✗ | 0.51 l✗ | 0.52 l✗ | 0.51 l✓ | 0 |
| loans_gdp | 0.50 l✗ | 0.51 l✗ | 0.52 l✗ | 0.52 l✗ | 0.53 l✗ | 4 |
| debt_gdp | 0.51 l✗ | 0.51 l✗ | 0.51 l✗ | 0.51 l✗ | 0.50 l✗ | 0 |

## 3. Mile markers: event rate as markers arrive in sequence

Conditional frequency of the event given each marker in turn (all markers computable at T; terciles over the panel; descriptive, so in-sample, with the pre/post-1950 rates beside each stage).

### credit_contraction_3y

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2355 | 17% | — | — |
| loans/GDP high (top tercile) at T-3 | 732 | 30% | 42% | 25% |
| real equity 3y gain <= 0 at T-1 | 275 | 42% | 56% | 36% |
| real house prices 3y growth <= 0 at T | 140 | 51% | 51% | 52% |
| real oil price up >= 25% over the year at T | 35 | 60% | 40% | 68% |

### dd30_3y

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2224 | 12% | — | — |
| dividend yield low (bottom tercile) at T | 683 | 23% | 29% | 21% |
| r - g low (bottom tercile) at T | 216 | 31% | 37% | 29% |
| inflation high (top tercile) at T | 121 | 43% | 47% | 40% |
| real oil price up >= 25% over the year at T | 11 | 64% | 60% | 67% |

### gdp_fall_3y

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2612 | 11% | — | — |
| real oil price up >= 25% over the year at T | 369 | 15% | 20% | 8% |
| loans/GDP high (top tercile) at T-3 | 143 | 15% | 30% | 11% |
| real house prices 3y growth <= 0 at T | 55 | 24% | 38% | 18% |

### credit_contraction_3y (diffusion rung)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2355 | 17% | — | — |
| loans/GDP high (top tercile) at T-3 | 732 | 30% | 42% | 25% |
| real equity 3y gain <= 0 at T-1 | 275 | 42% | 56% | 36% |
| technology diffusion slow (bottom tercile of tech_growth_3y) at T | 69 | 54% | 58% | 50% |

### gdp_fall_3y (Jacks rungs)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2612 | 11% | — | — |
| broad real commodity boom at T (Jacks breadth >= 2/3 of 42 commodities up over 3y) | 423 | 16% | 20% | 12% |
| loans/GDP high (top tercile) at T-3 | 173 | 18% | 29% | 15% |
| real house prices 3y growth <= 0 at T | 63 | 22% | 47% | 11% |

### credit_contraction_3y (Jacks rungs)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2355 | 17% | — | — |
| loans/GDP high (top tercile) at T-3 | 732 | 30% | 42% | 25% |
| real equity 3y gain <= 0 at T-1 | 275 | 42% | 56% | 36% |
| real commodity bust at T (Jacks equal-weight index down >= 15% over 3y) | 53 | 62% | 69% | 60% |

### dd30_3y (Jacks rungs)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2224 | 12% | — | — |
| broad real commodity boom at T (Jacks breadth >= 2/3) | 362 | 26% | 16% | 36% |
| r - g low (bottom tercile) at T | 136 | 38% | 24% | 62% |
| dividend yield low (bottom tercile) at T | 25 | 84% | 67% | 89% |

### dd30_3y (materials rungs)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2224 | 12% | — | — |
| metals real price above its own history (top tercile anomaly) at T | 576 | 20% | 44% | 18% |
| real commodity PPI 3y change high (top tercile) at T | 304 | 28% | 44% | 25% |
| r - g low (bottom tercile) at T | 144 | 37% | 42% | 35% |

### gdp_fall_3y (materials rungs)

| stage | n | event rate | pre-1950 | post-1950 |
|---|---|---|---|---|
| unconditional | 2612 | 11% | — | — |
| real commodity PPI 3y change high (top tercile) at T | 626 | 16% | 25% | 8% |
| world metals production decelerating at T | 250 | 20% | 33% | 10% |
| loans/GDP high (top tercile) at T-3 | 72 | 28% | 40% | 23% |

Reading the profiles: a feature whose AUC is highest at k=0 is coincident information; one whose AUC stays high or peaks at k=1..3 leads the event by that many years, which is the lag a mile marker can be registered at. A ✗ means the relationship flipped sign between eras and should not be trusted as a 'known' lag.
