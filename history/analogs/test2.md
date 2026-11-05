# Analog test 2 — the subnet at t, and flux

Walk-forward only: z-scores from an expanding window (rows ≤ the query year), candidates whose outcome window closed before the query year, own country within ±5 years excluded, one episode per country within ±5 years, k=15, coverage ≥ 60%, queries from 1880. AUC 0.5 is no skill.

## Walk-forward AUC by feature family and 3-year target

| family (features) | crisis_3y | stress3_3y | dd30_3y | credit_contraction_3y | unemp_spike_3y | gdp_fall_3y |
|---|---|---|---|---|---|---|
| base (20) | 0.53 (top 13% vs 9%) | 0.56 (top 12% vs 6%) | 0.61 (top 26% vs 12%) | 0.64 (top 40% vs 17%) | 0.58 (top 19% vs 10%) | 0.59 (top 18% vs 11%) |
| network (10) | 0.58 (top 9% vs 10%) | 0.54 (top 8% vs 6%) | 0.59 (top 21% vs 13%) | 0.58 (top 24% vs 17%) | 0.56 (top 11% vs 10%) | 0.67 (top 23% vs 11%) |
| rank (6) | 0.56 (top 13% vs 9%) | 0.49 (top 7% vs 6%) | 0.51 (top 13% vs 13%) | 0.54 (top 18% vs 18%) | 0.52 (top 12% vs 11%) | 0.50 (top 15% vs 11%) |
| flux (9) | 0.52 (top 13% vs 10%) | 0.53 (top 8% vs 6%) | 0.59 (top 23% vs 12%) | 0.61 (top 31% vs 17%) | 0.53 (top 14% vs 11%) | 0.55 (top 16% vs 11%) |
| base+network (30) | 0.55 (top 13% vs 10%) | 0.55 (top 10% vs 6%) | 0.67 (top 36% vs 13%) | 0.66 (top 46% vs 17%) | 0.58 (top 14% vs 9%) | 0.60 (top 24% vs 11%) |
| base+flux (29) | 0.56 (top 12% vs 10%) | 0.55 (top 12% vs 6%) | 0.62 (top 28% vs 12%) | 0.65 (top 42% vs 17%) | 0.56 (top 14% vs 10%) | 0.57 (top 21% vs 11%) |
| base+rank (26) | 0.54 (top 15% vs 9%) | 0.55 (top 10% vs 6%) | 0.60 (top 27% vs 12%) | 0.64 (top 39% vs 18%) | 0.56 (top 14% vs 10%) | 0.59 (top 19% vs 11%) |
| base+network+flux (39) | 0.57 (top 14% vs 9%) | 0.56 (top 10% vs 6%) | 0.67 (top 35% vs 12%) | 0.67 (top 44% vs 17%) | 0.59 (top 14% vs 10%) | 0.61 (top 23% vs 11%) |
| all (45) | 0.58 (top 14% vs 10%) | 0.56 (top 10% vs 6%) | 0.67 (top 35% vs 12%) | 0.68 (top 45% vs 17%) | 0.59 (top 14% vs 10%) | 0.61 (top 25% vs 11%) |

Base rates: crisis_3y 9.8%, stress3_3y 5.8%, dd30_3y 12.5%, credit_contraction_3y 16.9%, unemp_spike_3y 11.7%, gdp_fall_3y 11.5%

## Crisis AUC by horizon (JST label)

| family | 1y | 2y | 3y | 4y | 5y |
|---|---|---|---|---|---|
| base | 0.54 | 0.55 | 0.53 | 0.49 | 0.50 |
| base+network+flux | 0.53 | 0.56 | 0.57 | 0.50 | 0.48 |
| all | 0.54 | 0.56 | 0.58 | 0.51 | 0.48 |

## Leak check on this harness (base features, crisis within 3 years)

| exclusion | AUC | top decile vs base |
|---|---|---|
| same-country | 0.63 | 19% vs 9% |
| block-year | 0.50 | 9% vs 9% |
| walk-forward | 0.53 | 13% vs 9% |

Targets: `crisis_hy` = a JST-labelled systemic banking crisis begins within h years; `stress3_3y` = in some year of the next three, at least 3 of 5 measured conditions hold (real equity ≤ −20%, real GDP/cap ≤ −2%, unemployment +1.5 pp, loans/GDP −2 pp, bank capital ratio −0.7 pp); `dd30_3y` = the real equity path falls 30% within 3 years; `credit_contraction_3y` = loans/GDP down 5 pp of GDP at some point within 3 years; `unemp_spike_3y` = unemployment +3 pp within 3 years; `gdp_fall_3y` = real GDP per capita −5% within 3 years. All censored unless the full window exists.
