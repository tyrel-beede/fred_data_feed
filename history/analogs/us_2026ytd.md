# Analogs for United States 2026 year-to-date (built by live_query.py from the JST sheet through 2020 and the FRED bridge, Shiller workbooks; 20 of 20 features)

Features used (20 of 20 requested): loans_gdp, d3_loans_gdp, d5_loans_gdp, mort_gdp, debt_gdp, d5_debt_gdp, deficit_gdp, r_minus_g, ltrate, term_spread, real_ltrate_expost, cpi_infl, rgdp_pc_growth, unemp, d1_unemp, iy, ca_gdp, eq_dp, real_eq_capgain_3y, real_hp_growth_3y. Candidates: 2718 country-years (regime any, from 1870); the query's own country within ±5 years is excluded. Distance is the root-mean-square of robust z-score differences over the features both sides have. One episode per country within ±5 years.

## Query

| feature | value | provenance |
|---|---|---|
| loans_gdp | 0.6034 | FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED TOTLL 2026 (mean of 42 obs) x 1.388 |
| d3_loans_gdp | -0.01669 | FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED GDPA 2023 (last of 1 obs) x 0.9775; FRED TOTLL 2023 (mean of 52 obs) x 1.388; FRED TOTLL 2026 (mean of 42 obs) x 1.388 |
| d5_loans_gdp | -0.02025 | FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED GDPA 2021 (last of 1 obs) x 0.9775; FRED TOTLL 2021 (mean of 52 obs) x 1.388; FRED TOTLL 2026 (mean of 42 obs) x 1.388 |
| mort_gdp | 0.3679 | FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED HHMSDODNS 2026 (mean of 2 obs) x 0.8386 |
| debt_gdp | 1.276 | FRED GFDEGDQ188S 2026 (mean of 2 obs) x 1.047 |
| d5_debt_gdp | 0.01033 | FRED GFDEGDQ188S 2021 (mean of 4 obs) x 1.047; FRED GFDEGDQ188S 2026 (mean of 2 obs) x 1.047 |
| deficit_gdp | 0.06273 | FRED FYFR 2026 (last of 1 obs); FRED FYONET 2026 (last of 1 obs); FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775 |
| r_minus_g | -0.7523 | FRED DGS10 2026 (mean of 212 obs); FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED GDPA 2025 (last of 1 obs) x 0.9775 |
| ltrate | 4.535 | FRED DGS10 2026 (mean of 212 obs) |
| term_spread | 0.8263 | FRED DGS10 2026 (mean of 212 obs); FRED TB3MS 2026 (mean of 10 obs) |
| real_ltrate_expost | 1.468 | FRED CPIAUCSL 2025 (mean of 11 obs) x 0.7441; FRED CPIAUCSL 2026 (mean of 9 obs) x 0.7441; FRED DGS10 2026 (mean of 212 obs) |
| cpi_infl | 0.03067 | FRED CPIAUCSL 2025 (mean of 11 obs) x 0.7441; FRED CPIAUCSL 2026 (mean of 9 obs) x 0.7441 |
| rgdp_pc_growth | 0.0179 | FRED A939RX0Q048SBEA 2025 (mean of 4 obs) x 0.5504; FRED A939RX0Q048SBEA 2026 (mean of 3 obs) x 0.5504 |
| unemp | 4.23 | FRED UNRATE 2026 (mean of 10 obs) |
| d1_unemp | -0.03364 | FRED UNRATE 2025 (mean of 11 obs); FRED UNRATE 2026 (mean of 10 obs) |
| iy | 0.2296 | FRED GPDIC1/GDPC1 2026 (mean of 3 quarters) x 1.202 |
| ca_gdp | -0.03018 | FRED GDP quarterly SAAR, mean of 3 quarters of 2026 x 0.9775; FRED IEABC 2026 (sum of 2 obs) x 1.045 |
| eq_dp | 0.01107 | Shiller ie_data D/P 2026 (mean of 6 months) |
| real_eq_capgain_3y | 0.1603 | FRED CPIAUCSL 2023 (mean of 12 obs) x 0.7441; FRED CPIAUCSL 2024 (mean of 12 obs) x 0.7441; FRED CPIAUCSL 2025 (mean of 11 obs) x 0.7441; FRED CPIAUCSL 2026 (mean of 9 obs) x 0.7441; Shiller ie_data P 2024/2023 (annual means, 12 months in 2024); Shiller ie_data P 2025/2024 (annual means, 12 months in 2025); Shiller ie_data P 2026/2025 (annual means, 10 months in 2026) |
| real_hp_growth_3y | -0.0006225 | FRED CPIAUCSL 2023 (mean of 12 obs) x 0.7441; FRED CPIAUCSL 2026 (mean of 9 obs) x 0.7441; FRED CSUSHPISA 2023 (mean of 12 obs) x 1.374; FRED CSUSHPISA 2026 (mean of 8 obs) x 1.374 |

## The 15 nearest episodes

| # | country | year | distance | crisis in 1-3y | rGDP/cap next 3y | real equity next 3y | real houses next 3y | Δ long rate 3y | Δ unemp 3y |
|---|---|---|---|---|---|---|---|---|---|
| 1 | USA | 2019 | 0.54 | — | — | — | — | — | — |
| 2 | BEL | 2014 | 0.78 | no | +3.4% | +6.8% | +3.3% | -1.0 pp | -1.4 pp |
| 3 | USA | 1996 | 0.81 | no | +10.3% | +89.4% | +7.8% | -0.8 pp | -1.2 pp |
| 4 | USA | 2005 | 0.87 | yes | +1.3% | -32.5% | -6.3% | -0.6 pp | +0.7 pp |
| 5 | JPN | 2007 | 0.87 | no | -2.1% | -43.0% | -3.5% | -0.5 pp | +1.2 pp |
| 6 | ITA | 1998 | 0.87 | no | +6.4% | -2.3% | +18.2% | +0.3 pp | -2.5 pp |
| 7 | BEL | 1954 | 0.88 | no | +7.7% | -2.5% | +9.2% | +1.3 pp | -2.6 pp |
| 8 | USA | 2013 | 0.88 | no | +4.5% | +18.8% | +13.3% | -0.5 pp | -2.5 pp |
| 9 | BEL | 2005 | 0.89 | yes | +6.3% | -52.4% | +18.0% | +1.0 pp | -1.5 pp |
| 10 | ITA | 2005 | 0.90 | yes | +0.9% | -42.3% | +1.6% | +1.1 pp | -1.0 pp |
| 11 | FRA | 2014 | 0.93 | no | +3.6% | +42.7% | +0.8% | -0.9 pp | -1.3 pp |
| 12 | DNK | 1949 | 0.93 | no | +7.1% | -0.9% | -7.1% | +0.9 pp | +1.0 pp |
| 13 | BEL | 1997 | 0.94 | no | +8.7% | +27.9% | +14.8% | -0.2 pp | -2.4 pp |
| 14 | CAN | 1971 | 0.94 | no | +13.1% | — | +33.6% | +2.0 pp | -0.8 pp |
| 15 | IRL | 1939 | 0.95 | no | -6.3% | — | — | -0.7 pp | — |

## What followed: analogs vs climatology

| outcome | analogs p25 / p50 / p75 (n) | climatology p25 / p50 / p75 (n) |
|---|---|---|
| systemic crisis within 1-3 years (share) | share 21% (n=14) | share 10% (n=2615) |
| real GDP per capita, next 1 year (%) | +1.0 / +1.7 / +2.9 (n=15) | +0.1 / +2.0 / +4.0 (n=2648) |
| real GDP per capita, next 3 years cumulative (%) | +1.9 / +5.4 / +7.6 (n=14) | +1.5 / +5.8 / +10.3 (n=2612) |
| real equity total return, next 1 year (%) | +11.1 / +18.3 / +21.1 (n=13) | -5.0 / +6.2 / +17.3 (n=2258) |
| real equity total return, next 3 years cumulative (%) | -35.0 / -1.6 / +21.1 (n=12) | -5.2 / +16.8 / +41.8 (n=2224) |
| real house prices, next 3 years cumulative (%) | +0.8 / +7.8 / +14.8 (n=13) | -5.5 / +4.6 / +15.2 (n=1980) |
| long rate change, next 1 year (pp) | -0.5 / -0.1 / +0.2 (n=15) | -0.3 / -0.0 / +0.2 (n=2606) |
| long rate change, next 3 years (pp) | -0.7 / -0.3 / +1.0 (n=14) | -0.6 / -0.1 / +0.4 (n=2561) |
| unemployment change, next 3 years (pp) | -2.4 / -1.3 / -0.8 (n=13) | -1.1 / +0.0 / +1.1 (n=1868) |
| bank loans/GDP change, next 3 years (pp of GDP) | -0.1 / +3.7 / +7.5 (n=14) | -1.6 / +2.1 / +6.5 (n=2358) |

Climatology is the same outcome over every candidate country-year: the no-skill reference. Where the analog quantiles sit inside the climatology's, the state vector carried information; where they do not, it did not. Nothing here is a forecast of the dials' branches; it is the record's answer to 'what followed states like this one'.
