# A learner that can weight — walk-forward

**Jacks features added (9): jacks_real_index_1y, jacks_real_index_3y, jacks_anom, jacks_breadth_3y, jacks_dispersion_3y, jacks_energy_3y, jacks_metals_3y, jacks_grains_3y, jacks_grown_vs_ground_3y.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 9 jacks = 75. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.59 (top 26%) | 0.62 (top 24%) | 0.75 (top 39%) | 0.62 (top 27%) |
| credit_contraction_3y (19%) | 0.62 (top 34%) | 0.65 (top 51%) | 0.64 (top 47%) | 0.68 (top 46%) |
| gdp_fall_3y (12%) | 0.67 (top 24%) | 0.59 (top 36%) | 0.58 (top 20%) | 0.55 (top 16%) |
| unemp_spike_3y (10%) | 0.52 (top 9%) | 0.56 (top 22%) | 0.67 (top 22%) | 0.60 (top 18%) |
| crisis_3y (9%) | 0.60 (top 16%) | 0.55 (top 13%) | 0.60 (top 17%) | 0.59 (top 19%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.53 / 0.89 | 0.63 / 0.80 | 0.70 / 0.91 | 0.65 / 0.48 |
| credit_contraction_3y | 0.60 / 0.74 | 0.63 / 0.75 | 0.60 / 0.76 | 0.65 / 0.81 |
| gdp_fall_3y | 0.68 / 0.58 | 0.63 / 0.37 | 0.59 / 0.59 | 0.54 / 0.61 |
| unemp_spike_3y | 0.50 / 0.70 | 0.52 / 0.78 | 0.64 / 0.87 | 0.55 / 0.85 |
| crisis_3y | 0.61 / 0.56 | 0.52 / 0.81 | 0.58 / 0.69 | 0.59 / 0.56 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.01, oil_real_price -0.72, oil_share_co2 -0.71, eq_dp -0.68, real_ltrate_expost -0.65, xs_crises_last2y -0.61, jacks_dispersion_3y +0.57, xs_mean_term_spread -0.55, speed_2y +0.54, xs_share_credit_boom +0.45, xs_mean_req3y +0.42, rgdp_pc_growth -0.41
- **credit_contraction_3y**: loans_gdp_lag3 +1.62, mort_gdp -1.02, loans_gdp +0.81, d5_loans_gdp -0.57, xs_mean_d3_loans_gdp -0.56, coal_share_co2 +0.55, real_hp_growth_3y -0.49, real_eq_capgain_3y -0.48, r_minus_g +0.45, speed_1y +0.45, oil_real_change_3y +0.40, jacks_breadth_3y -0.38
- **gdp_fall_3y**: jacks_real_index_3y +1.31, fuel_self_sufficiency -1.27, jacks_breadth_3y -0.79, jacks_anom -0.79, real_hp_growth_3y -0.77, xs_mean_term_spread -0.60, d5_loans_gdp -0.59, coal_share_co2 +0.59, xs_mean_req3y -0.59, xs_mean_d3_loans_gdp -0.52, jacks_energy_3y -0.51, oil_share_co2 -0.50
- **unemp_spike_3y**: jacks_metals_3y -1.09, jacks_real_index_3y +0.99, jacks_energy_3y -0.96, xs_mean_term_spread -0.90, oil_real_price +0.74, xs_crises_last2y -0.57, loans_gdp_lag3 +0.57, coal_share_co2 +0.53, jacks_grown_vs_ground_3y -0.52, fuel_self_sufficiency -0.51, jacks_breadth_3y +0.46, r_minus_g_lag1 -0.43
- **crisis_3y**: co2_growth_3y -0.99, jacks_breadth_3y +0.94, energy_footprint_gap_3y +0.87, xs_mean_term_spread -0.83, base_term_spread +0.66, jacks_dispersion_3y +0.61, jacks_real_index_3y -0.59, xs_mean_d3_loans_gdp +0.59, xs_crises_last2y -0.57, coal_share_co2 +0.55, unemp -0.52, oil_real_change_3y -0.49

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
