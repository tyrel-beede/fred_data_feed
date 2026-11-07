# A learner that can weight — walk-forward

**Jacks features added (9): jacks_real_index_1y, jacks_real_index_3y, jacks_anom, jacks_breadth_3y, jacks_dispersion_3y, jacks_energy_3y, jacks_metals_3y, jacks_grains_3y, jacks_grown_vs_ground_3y.** Compare with learner_test.md (same harness without them).


**Materials features added (8): metals_real_price_1y, metals_real_price_3y, metals_real_price_anom, world_metals_prod_3y, world_metals_prod_accel, gold_real_3y, ppi_commod_real_1y, ppi_commod_real_3y.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 8 materials + 9 jacks = 83. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.56 (top 22%) | 0.55 (top 15%) | 0.74 (top 37%) | 0.63 (top 25%) |
| credit_contraction_3y (19%) | 0.60 (top 34%) | 0.65 (top 46%) | 0.63 (top 45%) | 0.68 (top 46%) |
| gdp_fall_3y (12%) | 0.66 (top 27%) | 0.53 (top 31%) | 0.58 (top 18%) | 0.55 (top 14%) |
| unemp_spike_3y (10%) | 0.53 (top 11%) | 0.58 (top 25%) | 0.66 (top 20%) | 0.61 (top 18%) |
| crisis_3y (9%) | 0.62 (top 17%) | 0.56 (top 11%) | 0.62 (top 18%) | 0.60 (top 16%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.52 / 0.79 | 0.57 / 0.68 | 0.71 / 0.91 | 0.66 / 0.50 |
| credit_contraction_3y | 0.58 / 0.74 | 0.64 / 0.75 | 0.61 / 0.72 | 0.65 / 0.82 |
| gdp_fall_3y | 0.67 / 0.56 | 0.56 / 0.36 | 0.58 / 0.57 | 0.54 / 0.63 |
| unemp_spike_3y | 0.51 / 0.69 | 0.56 / 0.74 | 0.63 / 0.82 | 0.58 / 0.82 |
| crisis_3y | 0.60 / 0.72 | 0.52 / 0.89 | 0.60 / 0.67 | 0.60 / 0.60 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.16, oil_real_price -0.86, ppi_commod_real_3y +0.85, eq_dp -0.80, world_metals_prod_accel -0.79, oil_share_co2 -0.75, jacks_real_index_1y +0.72, jacks_dispersion_3y +0.62, jacks_real_index_3y -0.62, xs_mean_term_spread -0.62, world_metals_prod_3y +0.61, metals_real_price_1y -0.59
- **credit_contraction_3y**: loans_gdp_lag3 +1.66, mort_gdp -0.96, loans_gdp +0.75, xs_mean_d3_loans_gdp -0.64, d5_loans_gdp -0.63, coal_share_co2 +0.59, real_eq_capgain_3y -0.55, metals_real_price_1y -0.49, real_hp_growth_3y -0.47, jacks_grains_3y -0.45, speed_1y +0.44, r_minus_g +0.43
- **gdp_fall_3y**: world_metals_prod_accel -1.38, ppi_commod_real_3y +1.36, fuel_self_sufficiency -1.17, xs_mean_term_spread -0.77, real_hp_growth_3y -0.72, jacks_anom -0.70, gold_real_3y +0.64, world_metals_prod_3y +0.60, d5_loans_gdp -0.54, jacks_grains_3y -0.53, r_minus_g_lag1 -0.51, d3_loans_gdp +0.50
- **unemp_spike_3y**: xs_mean_term_spread -0.99, jacks_breadth_3y +0.98, jacks_energy_3y -0.96, ppi_commod_real_3y +0.95, gold_real_3y +0.85, loans_gdp_lag3 +0.78, world_metals_prod_3y +0.74, r_minus_g_lag1 -0.74, world_metals_prod_accel -0.74, jacks_real_index_3y -0.67, xs_crises_last2y -0.54, oil_real_price +0.54
- **crisis_3y**: jacks_real_index_3y -1.73, jacks_breadth_3y +1.09, metals_real_price_anom -1.04, ppi_commod_real_3y +0.92, co2_growth_3y -0.83, energy_footprint_gap_3y +0.78, xs_mean_req3y +0.65, unemp -0.60, xs_mean_term_spread -0.57, mort_gdp -0.56, base_term_spread +0.55, jacks_anom +0.54

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
