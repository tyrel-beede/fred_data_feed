# A learner that can weight — walk-forward

**Physical-layer features added (9): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 9 physical = 62. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.61 (top 31%) | 0.59 (top 19%) | 0.73 (top 33%) | 0.62 (top 29%) |
| credit_contraction_3y (19%) | 0.65 (top 44%) | 0.69 (top 55%) | 0.65 (top 48%) | 0.69 (top 47%) |
| gdp_fall_3y (11%) | 0.66 (top 21%) | 0.62 (top 34%) | 0.60 (top 19%) | 0.53 (top 17%) |
| unemp_spike_3y (11%) | 0.56 (top 13%) | 0.58 (top 22%) | 0.68 (top 20%) | 0.64 (top 22%) |
| crisis_3y (9%) | 0.60 (top 15%) | 0.58 (top 20%) | 0.63 (top 18%) | 0.59 (top 16%) |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.27, real_ltrate_expost -0.89, xs_share_credit_boom +0.80, oil_share_co2 -0.65, co2_growth_3y -0.61, eq_dp -0.60, speed_2y +0.60, xs_mean_term_spread -0.47, loans_gdp_lag3 +0.42, energy_footprint_gap_3y +0.41, xs_crises_now -0.40, xs_crises_last2y -0.39
- **credit_contraction_3y**: loans_gdp_lag3 +1.55, mort_gdp -0.87, loans_gdp +0.86, coal_share_co2 +0.71, d5_loans_gdp -0.61, real_eq_capgain_3y -0.48, xs_mean_d3_loans_gdp -0.48, oil_share_co2 +0.45, r_minus_g +0.42, real_hp_growth_3y -0.42, speed_1y +0.40, xs_crises_last2y +0.35
- **gdp_fall_3y**: fuel_self_sufficiency -1.33, real_hp_growth_3y -0.56, oil_share_co2 -0.53, xs_mean_d3_loans_gdp -0.48, d5_loans_gdp -0.48, base_d3_loans_gdp -0.48, loans_gdp +0.43, d3_loans_gdp +0.42, energy_footprint_gap_3y -0.39, r_minus_g_lag1 -0.39, real_eq_capgain_3y_lag1 +0.36, xs_share_credit_boom +0.32
- **unemp_spike_3y**: xs_mean_term_spread -0.69, loans_gdp_lag3 +0.62, xs_share_credit_boom +0.61, r_minus_g +0.56, ca_gdp -0.52, oil_share_co2 -0.51, r_minus_g_lag1 -0.50, ltrate +0.44, fuel_self_sufficiency -0.42, mort_gdp_lag3 -0.41, xs_crises_last2y -0.37, bloc_crises_last2y +0.37
- **crisis_3y**: co2_growth_3y -1.03, energy_footprint_gap_3y +0.78, xs_mean_term_spread -0.62, oil_share_co2 -0.59, xs_mean_d3_loans_gdp +0.55, base_term_spread +0.49, base_d3_loans_gdp -0.42, fuel_self_sufficiency -0.39, term_spread -0.39, real_eq_capgain_3y +0.39, mort_gdp_lag3 +0.38, speed_1y +0.35

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
