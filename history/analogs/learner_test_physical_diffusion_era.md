# A learner that can weight — walk-forward

**Diffusion features added (10): tech_growth_3y, tech_accel_3y, tech_max_growth_3y, tech_frontier_gap, rank_tech_growth_3y, rail_growth_3y, elec_growth_3y, car_growth_3y, phone_growth_3y, elec_per_co2_growth_3y.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 10 diffusion = 76. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.62 (top 36%) | 0.59 (top 23%) | 0.74 (top 36%) | 0.62 (top 26%) |
| credit_contraction_3y (19%) | 0.62 (top 36%) | 0.65 (top 51%) | 0.65 (top 49%) | 0.68 (top 44%) |
| gdp_fall_3y (12%) | 0.65 (top 23%) | 0.69 (top 35%) | 0.59 (top 18%) | 0.53 (top 14%) |
| unemp_spike_3y (11%) | 0.56 (top 12%) | 0.55 (top 23%) | 0.67 (top 20%) | 0.62 (top 19%) |
| crisis_3y (9%) | 0.58 (top 17%) | 0.56 (top 12%) | 0.58 (top 16%) | 0.58 (top 18%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.56 / 0.92 | 0.59 / 0.85 | 0.68 / 0.91 | 0.65 / 0.48 |
| credit_contraction_3y | 0.59 / 0.73 | 0.61 / 0.83 | 0.62 / 0.78 | 0.65 / 0.82 |
| gdp_fall_3y | 0.66 / 0.53 | 0.74 / 0.35 | 0.59 / 0.62 | 0.52 / 0.66 |
| unemp_spike_3y | 0.54 / 0.69 | 0.53 / 0.77 | 0.64 / 0.84 | 0.57 / 0.84 |
| crisis_3y | 0.64 / 0.33 | 0.57 / 0.58 | 0.62 / 0.35 | 0.59 / 0.55 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.19, co2_growth_3y -0.84, real_ltrate_expost -0.83, xs_share_credit_boom +0.72, eq_dp -0.65, oil_share_co2 -0.64, speed_2y +0.62, loans_gdp_lag3 +0.57, oil_real_price -0.48, oil_real_change_3y +0.47, elec_per_co2_growth_3y -0.47, bloc_crises_last2y -0.46
- **credit_contraction_3y**: loans_gdp_lag3 +1.59, mort_gdp -0.92, loans_gdp +0.84, d5_loans_gdp -0.62, real_eq_capgain_3y -0.52, tech_growth_3y -0.47, coal_share_co2 +0.47, real_hp_growth_3y -0.44, xs_mean_d3_loans_gdp -0.44, d1_real_eq_capgain_3y +0.43, r_minus_g +0.39, speed_1y +0.39
- **gdp_fall_3y**: fuel_self_sufficiency -1.29, oil_share_co2 -0.74, real_hp_growth_3y -0.59, base_d3_loans_gdp -0.56, energy_footprint_gap_3y -0.50, d5_loans_gdp -0.47, d3_loans_gdp +0.42, real_eq_capgain_3y_lag1 +0.41, xs_mean_d3_loans_gdp -0.39, loans_gdp +0.37, r_minus_g_lag1 -0.36, ca_gdp -0.31
- **unemp_spike_3y**: xs_mean_term_spread -0.77, loans_gdp_lag3 +0.73, oil_real_price +0.64, r_minus_g_lag1 -0.61, xs_share_credit_boom +0.60, coal_share_co2 +0.58, mort_gdp_lag3 -0.56, r_minus_g +0.54, fuel_self_sufficiency -0.52, xs_mean_d3_loans_gdp -0.49, tech_growth_3y +0.42, bloc_crises_last2y +0.41
- **crisis_3y**: co2_growth_3y -0.88, xs_mean_term_spread -0.65, xs_mean_d3_loans_gdp +0.62, energy_footprint_gap_3y +0.55, base_term_spread +0.48, mort_gdp -0.44, oil_share_co2 -0.43, gap_anom_3y +0.41, mort_gdp_lag3 +0.39, speed_1y +0.38, unemp -0.37, mk_equity_le0_T-1 +0.37

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
