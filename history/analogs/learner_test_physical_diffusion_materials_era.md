# A learner that can weight — walk-forward

**Materials features added (8): metals_real_price_1y, metals_real_price_3y, metals_real_price_anom, world_metals_prod_3y, world_metals_prod_accel, gold_real_3y, ppi_commod_real_1y, ppi_commod_real_3y.** Compare with learner_test.md (same harness without them).


**Diffusion features added (10): tech_growth_3y, tech_accel_3y, tech_max_growth_3y, tech_frontier_gap, rank_tech_growth_3y, rail_growth_3y, elec_growth_3y, car_growth_3y, phone_growth_3y, elec_per_co2_growth_3y.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 10 diffusion + 8 materials = 84. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.59 (top 22%) | 0.52 (top 17%) | 0.72 (top 36%) | 0.63 (top 27%) |
| credit_contraction_3y (19%) | 0.58 (top 31%) | 0.65 (top 45%) | 0.65 (top 47%) | 0.67 (top 41%) |
| gdp_fall_3y (12%) | 0.65 (top 24%) | 0.63 (top 31%) | 0.59 (top 20%) | 0.52 (top 16%) |
| unemp_spike_3y (10%) | 0.58 (top 12%) | 0.57 (top 27%) | 0.65 (top 18%) | 0.62 (top 18%) |
| crisis_3y (9%) | 0.61 (top 14%) | 0.63 (top 15%) | 0.62 (top 16%) | 0.59 (top 19%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.54 / 0.88 | 0.54 / 0.65 | 0.67 / 0.92 | 0.66 / 0.49 |
| credit_contraction_3y | 0.56 / 0.73 | 0.62 / 0.83 | 0.63 / 0.76 | 0.64 / 0.81 |
| gdp_fall_3y | 0.66 / 0.55 | 0.67 / 0.36 | 0.59 / 0.59 | 0.51 / 0.62 |
| unemp_spike_3y | 0.56 / 0.74 | 0.56 / 0.75 | 0.62 / 0.83 | 0.59 / 0.81 |
| crisis_3y | 0.63 / 0.48 | 0.61 / 0.88 | 0.63 / 0.53 | 0.59 / 0.56 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.21, real_ltrate_expost -0.82, eq_dp -0.72, loans_gdp_lag3 +0.66, co2_growth_3y -0.63, oil_share_co2 -0.63, speed_2y +0.62, world_metals_prod_accel -0.59, xs_share_credit_boom +0.56, oil_real_price -0.52, xs_mean_term_spread -0.49, bloc_crises_last2y -0.49
- **credit_contraction_3y**: loans_gdp_lag3 +1.60, mort_gdp -0.91, loans_gdp +0.82, d5_loans_gdp -0.64, real_eq_capgain_3y -0.55, xs_mean_d3_loans_gdp -0.47, coal_share_co2 +0.45, real_hp_growth_3y -0.44, tech_growth_3y -0.43, d1_real_eq_capgain_3y +0.42, elec_growth_3y +0.38, speed_1y +0.37
- **gdp_fall_3y**: world_metals_prod_accel -1.35, fuel_self_sufficiency -1.22, ppi_commod_real_3y +1.01, real_hp_growth_3y -0.68, xs_mean_d3_loans_gdp -0.65, metals_real_price_anom -0.59, world_metals_prod_3y +0.58, gold_real_3y +0.56, xs_mean_term_spread -0.55, d5_loans_gdp -0.52, oil_share_co2 -0.51, base_d3_loans_gdp -0.47
- **unemp_spike_3y**: xs_mean_term_spread -1.00, loans_gdp_lag3 +0.84, r_minus_g_lag1 -0.82, gold_real_3y +0.79, world_metals_prod_accel -0.76, ppi_commod_real_3y +0.66, oil_real_price +0.61, fuel_self_sufficiency -0.61, mort_gdp_lag3 -0.56, r_minus_g +0.54, world_metals_prod_3y +0.52, coal_share_co2 +0.50
- **crisis_3y**: metals_real_price_anom -0.88, mort_gdp -0.78, xs_mean_term_spread -0.70, oil_real_price +0.68, co2_growth_3y -0.67, coal_share_co2 +0.65, unemp -0.64, mort_gdp_lag3 +0.62, ppi_commod_real_3y +0.61, energy_footprint_gap_3y +0.57, metals_real_price_3y +0.52, gap_anom_3y +0.44

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
