# A learner that can weight — walk-forward

**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical = 66. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.61 (top 37%) | 0.55 (top 19%) | 0.76 (top 47%) | 0.62 (top 26%) |
| credit_contraction_3y (19%) | 0.63 (top 38%) | 0.69 (top 57%) | 0.65 (top 48%) | 0.69 (top 45%) |
| gdp_fall_3y (11%) | 0.66 (top 22%) | 0.67 (top 37%) | 0.61 (top 22%) | 0.55 (top 17%) |
| unemp_spike_3y (10%) | 0.55 (top 13%) | 0.56 (top 20%) | 0.66 (top 20%) | 0.63 (top 18%) |
| crisis_3y (9%) | 0.58 (top 15%) | 0.58 (top 12%) | 0.63 (top 17%) | 0.59 (top 17%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.55 / 0.92 | 0.54 / 0.82 | 0.71 / 0.95 | 0.66 / 0.48 |
| credit_contraction_3y | 0.60 / 0.72 | 0.66 / 0.84 | 0.62 / 0.77 | 0.66 / 0.81 |
| gdp_fall_3y | 0.67 / 0.55 | 0.71 / 0.42 | 0.61 / 0.69 | 0.53 / 0.66 |
| unemp_spike_3y | 0.52 / 0.69 | 0.52 / 0.76 | 0.63 / 0.86 | 0.58 / 0.85 |
| crisis_3y | 0.64 / 0.29 | 0.60 / 0.48 | 0.64 / 0.57 | 0.60 / 0.57 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.12, real_ltrate_expost -0.83, oil_share_co2 -0.72, xs_share_credit_boom +0.71, eq_dp -0.64, speed_2y +0.59, loans_gdp_lag3 +0.56, co2_growth_3y -0.54, bloc_crises_last2y -0.52, oil_real_change_3y +0.45, oil_real_price -0.45, coal_share_co2 -0.43
- **credit_contraction_3y**: loans_gdp_lag3 +1.56, mort_gdp -0.91, loans_gdp +0.81, d5_loans_gdp -0.58, xs_mean_d3_loans_gdp -0.57, real_eq_capgain_3y -0.53, coal_share_co2 +0.52, real_hp_growth_3y -0.49, r_minus_g +0.44, d1_real_eq_capgain_3y +0.42, xs_crises_last2y +0.39, d3_loans_gdp +0.38
- **gdp_fall_3y**: fuel_self_sufficiency -1.21, oil_share_co2 -0.73, real_hp_growth_3y -0.56, d5_loans_gdp -0.54, xs_mean_d3_loans_gdp -0.53, base_d3_loans_gdp -0.48, d3_loans_gdp +0.47, energy_footprint_gap_3y -0.45, r_minus_g_lag1 -0.40, real_eq_capgain_3y_lag1 +0.39, loans_gdp +0.34, xs_share_credit_boom +0.33
- **unemp_spike_3y**: xs_mean_term_spread -0.75, xs_share_credit_boom +0.66, oil_real_price +0.61, loans_gdp_lag3 +0.60, r_minus_g +0.52, mort_gdp_lag3 -0.51, xs_mean_d3_loans_gdp -0.50, r_minus_g_lag1 -0.44, coal_share_co2 +0.41, fuel_self_sufficiency -0.37, ca_gdp -0.36, bloc_crises_last2y +0.35
- **crisis_3y**: co2_growth_3y -1.04, energy_footprint_gap_3y +0.80, xs_mean_term_spread -0.62, oil_share_co2 -0.57, base_term_spread +0.49, xs_mean_d3_loans_gdp +0.39, mort_gdp_lag3 +0.39, speed_1y +0.38, term_spread -0.38, fuel_self_sufficiency -0.35, real_eq_capgain_3y +0.35, unemp -0.35

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
