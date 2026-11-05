# A learner that can weight — walk-forward

**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical = 66. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.61 (top 37%) | 0.60 (top 23%) | 0.76 (top 40%) | 0.62 (top 26%) |
| credit_contraction_3y (19%) | 0.63 (top 38%) | 0.67 (top 53%) | 0.64 (top 46%) | 0.68 (top 44%) |
| gdp_fall_3y (11%) | 0.66 (top 22%) | 0.68 (top 34%) | 0.63 (top 18%) | 0.55 (top 14%) |
| unemp_spike_3y (10%) | 0.55 (top 13%) | 0.55 (top 25%) | 0.68 (top 22%) | 0.62 (top 20%) |
| crisis_3y (9%) | 0.58 (top 15%) | 0.58 (top 15%) | 0.63 (top 19%) | 0.60 (top 17%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.55 / 0.92 | 0.61 / 0.81 | 0.71 / 0.91 | 0.66 / 0.48 |
| credit_contraction_3y | 0.60 / 0.72 | 0.64 / 0.84 | 0.61 / 0.75 | 0.66 / 0.80 |
| gdp_fall_3y | 0.67 / 0.55 | 0.73 / 0.35 | 0.63 / 0.67 | 0.54 / 0.67 |
| unemp_spike_3y | 0.52 / 0.69 | 0.52 / 0.76 | 0.65 / 0.86 | 0.58 / 0.84 |
| crisis_3y | 0.64 / 0.29 | 0.59 / 0.58 | 0.63 / 0.62 | 0.60 / 0.57 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.13, real_ltrate_expost -0.83, oil_share_co2 -0.70, xs_share_credit_boom +0.68, eq_dp -0.64, speed_2y +0.58, co2_growth_3y -0.55, bloc_crises_last2y -0.53, oil_real_price -0.52, loans_gdp_lag3 +0.50, oil_real_change_3y +0.48, real_eq_capgain_3y_lag1 +0.40
- **credit_contraction_3y**: loans_gdp_lag3 +1.58, mort_gdp -0.93, loans_gdp +0.82, d5_loans_gdp -0.60, real_eq_capgain_3y -0.51, real_hp_growth_3y -0.49, xs_mean_d3_loans_gdp -0.48, coal_share_co2 +0.44, r_minus_g +0.42, d1_real_eq_capgain_3y +0.40, speed_1y +0.38, xs_crises_last2y +0.38
- **gdp_fall_3y**: fuel_self_sufficiency -1.26, oil_share_co2 -0.72, real_hp_growth_3y -0.60, base_d3_loans_gdp -0.51, d5_loans_gdp -0.49, energy_footprint_gap_3y -0.48, d3_loans_gdp +0.44, r_minus_g_lag1 -0.41, xs_mean_d3_loans_gdp -0.39, real_eq_capgain_3y_lag1 +0.39, loans_gdp +0.38, ca_gdp -0.28
- **unemp_spike_3y**: xs_mean_term_spread -0.72, xs_share_credit_boom +0.63, loans_gdp_lag3 +0.62, oil_real_price +0.60, r_minus_g +0.52, mort_gdp_lag3 -0.52, coal_share_co2 +0.46, r_minus_g_lag1 -0.43, xs_mean_d3_loans_gdp -0.43, fuel_self_sufficiency -0.42, ca_gdp -0.38, bloc_crises_last2y +0.35
- **crisis_3y**: co2_growth_3y -1.05, energy_footprint_gap_3y +0.80, xs_mean_term_spread -0.60, oil_share_co2 -0.55, base_term_spread +0.48, xs_mean_d3_loans_gdp +0.47, term_spread -0.38, fuel_self_sufficiency -0.38, mort_gdp_lag3 +0.37, speed_1y +0.37, base_d3_loans_gdp -0.37, unemp -0.35

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
