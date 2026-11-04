# Analogs for United States 2026 year-to-date (Jan-Oct/Nov 2026, from the live feed; 9 of 20 features)

Features used (9 of 20 requested): debt_gdp, d5_debt_gdp, ltrate, term_spread, real_ltrate_expost, cpi_infl, unemp, d1_unemp, real_eq_capgain_3y. Candidates: 2718 country-years (regime any, from 1870); the query's own country within ±5 years is excluded. Distance is the root-mean-square of robust z-score differences over the features both sides have. One episode per country within ±5 years.

## Query

| feature | value | provenance |
|---|---|---|
| debt_gdp | 1.218 | FRED GFDEGDQ188S, 2 observations 2026-01-01..2026-04-01, annual mean (data/fred/GFDEGDQ188S.csv) / 100 (same series concept as JST debtgdp: 2020 FRED 128.1 vs JST 1.281) |
| d5_debt_gdp | -0.06287 | GFDEGDQ188S 2026 mean / 100 minus JST USA 2020 debtgdp 1.281 |
| ltrate | 4.532 | FRED DGS10, 210 observations 2026-01-02..2026-11-02, annual mean (data/fred/DGS10.csv) |
| term_spread | 0.8602 | DGS10 minus DFF annual means (JST stir for the US is a 3-month bill rate; the funds rate is used as the short-rate proxy, levels within ~10 bp in 2025) |
| real_ltrate_expost | 1.464 | DGS10 annual mean minus CPI-U annual-average inflation |
| cpi_infl | 0.03067 | CPIAUCSL annual mean 2026 / 2025 - 1 (9 and 11 months) |
| unemp | 4.244 | FRED UNRATE, 9 observations 2026-01-01..2026-09-01, annual mean (data/fred/UNRATE.csv) |
| d1_unemp | -0.01919 | UNRATE annual mean 2026 minus 2025 |
| real_eq_capgain_3y | 0.1607 | SP500 annual mean 2026 / 2023, deflated by CPIAUCSL annual means, annualized over 3 years (annual-average basis, as JST) |

## The 15 nearest episodes

| # | country | year | distance | crisis in 1-3y | rGDP/cap next 3y | real equity next 3y | real houses next 3y | Δ long rate 3y | Δ unemp 3y |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ITA | 2005 | 0.46 | yes | +0.9% | -42.3% | +1.6% | +1.1 pp | -1.0 pp |
| 2 | USA | 2018 | 0.59 | — | — | — | — | — | — |
| 3 | BEL | 2006 | 0.64 | yes | +0.7% | -39.6% | +6.7% | +0.1 pp | -0.3 pp |
| 4 | ITA | 1936 | 0.65 | no | +17.3% | +27.0% | — | -0.2 pp | -0.6 pp |
| 5 | DNK | 1999 | 0.66 | no | +3.7% | -24.4% | +8.6% | +0.1 pp | -0.9 pp |
| 6 | BEL | 1954 | 0.69 | no | +7.7% | -2.5% | +9.2% | +1.3 pp | -2.6 pp |
| 7 | BEL | 1997 | 0.71 | no | +8.7% | +27.9% | +14.8% | -0.2 pp | -2.4 pp |
| 8 | NLD | 1959 | 0.72 | no | +11.7% | +1.2% | +37.1% | +0.1 pp | -0.9 pp |
| 9 | JPN | 1989 | 0.73 | no | +8.3% | -49.9% | +11.5% | -0.1 pp | -0.1 pp |
| 10 | FRA | 1898 | 0.74 | no | +2.4% | +0.7% | +8.3% | +0.1 pp | +0.5 pp |
| 11 | USA | 1999 | 0.75 | no | +4.0% | -39.1% | +12.6% | -1.0 pp | +1.6 pp |
| 12 | NLD | 1911 | 0.78 | no | +0.1% | +0.7% | -1.7% | +0.2 pp | +0.1 pp |
| 13 | NLD | 1904 | 0.79 | no | +0.9% | +11.2% | -12.0% | +0.2 pp | -0.3 pp |
| 14 | USA | 1956 | 0.79 | no | +2.9% | +31.9% | -2.8% | +1.2 pp | +1.4 pp |
| 15 | USA | 2005 | 0.79 | yes | +1.3% | -32.5% | -6.3% | -0.6 pp | +0.7 pp |

## What followed: analogs vs climatology

| outcome | analogs p25 / p50 / p75 (n) | climatology p25 / p50 / p75 (n) |
|---|---|---|
| systemic crisis within 1-3 years (share) | share 21% (n=14) | share 10% (n=2615) |
| real GDP per capita, next 1 year (%) | +1.8 / +3.0 / +4.4 (n=15) | +0.1 / +2.0 / +4.0 (n=2648) |
| real GDP per capita, next 3 years cumulative (%) | +1.0 / +3.3 / +8.2 (n=14) | +1.5 / +5.8 / +10.3 (n=2612) |
| real equity total return, next 1 year (%) | -1.7 / +5.0 / +14.7 (n=15) | -5.0 / +6.2 / +17.3 (n=2258) |
| real equity total return, next 3 years cumulative (%) | -37.5 / -0.9 / +8.7 (n=14) | -5.2 / +16.8 / +41.8 (n=2224) |
| real house prices, next 3 years cumulative (%) | -1.7 / +8.3 / +11.5 (n=13) | -5.5 / +4.6 / +15.2 (n=1980) |
| long rate change, next 1 year (pp) | -0.0 / +0.2 / +0.5 (n=15) | -0.3 / -0.0 / +0.2 (n=2606) |
| long rate change, next 3 years (pp) | -0.1 / +0.1 / +0.2 (n=14) | -0.6 / -0.1 / +0.4 (n=2561) |
| unemployment change, next 3 years (pp) | -0.9 / -0.3 / +0.4 (n=14) | -1.1 / +0.0 / +1.1 (n=1868) |
| bank loans/GDP change, next 3 years (pp of GDP) | -1.0 / +4.0 / +7.5 (n=12) | -1.6 / +2.1 / +6.5 (n=2358) |

Climatology is the same outcome over every candidate country-year: the no-skill reference. Where the analog quantiles sit inside the climatology's, the state vector carried information; where they do not, it did not. Nothing here is a forecast of the dials' branches; it is the record's answer to 'what followed states like this one'.
