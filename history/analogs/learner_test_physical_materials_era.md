# A learner that can weight — walk-forward

**Materials features added (8): metals_real_price_1y, metals_real_price_3y, metals_real_price_anom, world_metals_prod_3y, world_metals_prod_accel, gold_real_3y, ppi_commod_real_1y, ppi_commod_real_3y.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 8 materials = 74. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.58 (top 25%) | 0.52 (top 16%) | 0.75 (top 35%) | 0.63 (top 28%) |
| credit_contraction_3y (19%) | 0.60 (top 33%) | 0.67 (top 50%) | 0.65 (top 43%) | 0.68 (top 45%) |
| gdp_fall_3y (12%) | 0.65 (top 26%) | 0.62 (top 32%) | 0.62 (top 21%) | 0.54 (top 16%) |
| unemp_spike_3y (10%) | 0.57 (top 15%) | 0.58 (top 28%) | 0.67 (top 22%) | 0.62 (top 18%) |
| crisis_3y (9%) | 0.60 (top 17%) | 0.66 (top 19%) | 0.64 (top 19%) | 0.60 (top 17%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.53 / 0.86 | 0.54 / 0.65 | 0.71 / 0.90 | 0.67 / 0.50 |
| credit_contraction_3y | 0.57 / 0.75 | 0.64 / 0.83 | 0.62 / 0.73 | 0.64 / 0.82 |
| gdp_fall_3y | 0.66 / 0.52 | 0.66 / 0.37 | 0.62 / 0.65 | 0.53 / 0.62 |
| unemp_spike_3y | 0.55 / 0.71 | 0.56 / 0.75 | 0.64 / 0.83 | 0.59 / 0.81 |
| crisis_3y | 0.63 / 0.45 | 0.63 / 0.89 | 0.62 / 0.70 | 0.60 / 0.57 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.17, real_ltrate_expost -0.82, eq_dp -0.74, oil_share_co2 -0.66, loans_gdp_lag3 +0.63, world_metals_prod_accel -0.60, ppi_commod_real_3y +0.60, speed_2y +0.59, bloc_crises_last2y -0.56, oil_real_price -0.55, xs_share_credit_boom +0.52, real_eq_capgain_3y_lag1 +0.44
- **credit_contraction_3y**: loans_gdp_lag3 +1.60, mort_gdp -0.91, loans_gdp +0.81, d5_loans_gdp -0.63, real_eq_capgain_3y -0.54, xs_mean_d3_loans_gdp -0.51, real_hp_growth_3y -0.49, coal_share_co2 +0.44, xs_crises_last2y +0.40, d1_real_eq_capgain_3y +0.39, oil_real_price -0.38, r_minus_g +0.37
- **gdp_fall_3y**: world_metals_prod_accel -1.32, fuel_self_sufficiency -1.17, ppi_commod_real_3y +1.03, real_hp_growth_3y -0.68, metals_real_price_anom -0.60, xs_mean_d3_loans_gdp -0.60, world_metals_prod_3y +0.55, d5_loans_gdp -0.54, r_minus_g_lag1 -0.48, xs_mean_term_spread -0.47, oil_share_co2 -0.46, gold_real_3y +0.45
- **unemp_spike_3y**: xs_mean_term_spread -0.94, loans_gdp_lag3 +0.80, gold_real_3y +0.79, world_metals_prod_accel -0.74, r_minus_g_lag1 -0.71, world_metals_prod_3y +0.62, ppi_commod_real_3y +0.60, oil_real_price +0.58, fuel_self_sufficiency -0.48, mort_gdp_lag3 -0.47, r_minus_g +0.46, rank_rgdp_pc_growth -0.41
- **crisis_3y**: metals_real_price_anom -0.87, co2_growth_3y -0.77, energy_footprint_gap_3y +0.76, oil_real_price +0.67, xs_mean_term_spread -0.66, mort_gdp -0.65, ppi_commod_real_3y +0.65, unemp -0.64, mort_gdp_lag3 +0.59, coal_share_co2 +0.58, metals_real_price_3y +0.51, world_metals_prod_3y -0.50

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
