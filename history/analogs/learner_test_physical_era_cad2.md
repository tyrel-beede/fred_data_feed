# A learner that can weight — walk-forward

**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical = 66. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.61 (top 37%) | 0.59 (top 24%) | 0.77 (top 46%) | 0.64 (top 29%) |
| credit_contraction_3y (19%) | 0.63 (top 38%) | 0.70 (top 55%) | 0.67 (top 49%) | 0.69 (top 45%) |
| gdp_fall_3y (11%) | 0.66 (top 22%) | 0.65 (top 33%) | 0.61 (top 21%) | 0.53 (top 15%) |
| unemp_spike_3y (10%) | 0.55 (top 13%) | 0.60 (top 25%) | 0.66 (top 21%) | 0.63 (top 23%) |
| crisis_3y (9%) | 0.58 (top 15%) | 0.59 (top 18%) | 0.63 (top 17%) | 0.60 (top 17%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.55 / 0.92 | 0.60 / 0.75 | 0.74 / 0.93 | 0.67 / 0.49 |
| credit_contraction_3y | 0.60 / 0.72 | 0.66 / 0.84 | 0.64 / 0.76 | 0.66 / 0.81 |
| gdp_fall_3y | 0.67 / 0.55 | 0.70 / 0.34 | 0.61 / 0.68 | 0.51 / 0.67 |
| unemp_spike_3y | 0.52 / 0.69 | 0.57 / 0.75 | 0.62 / 0.85 | 0.60 / 0.84 |
| crisis_3y | 0.64 / 0.29 | 0.61 / 0.50 | 0.64 / 0.52 | 0.60 / 0.57 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.12, real_ltrate_expost -0.83, oil_share_co2 -0.72, xs_share_credit_boom +0.70, eq_dp -0.64, speed_2y +0.58, loans_gdp_lag3 +0.56, co2_growth_3y -0.55, bloc_crises_last2y -0.52, oil_real_price -0.49, oil_real_change_3y +0.46, coal_share_co2 -0.43
- **credit_contraction_3y**: loans_gdp_lag3 +1.52, mort_gdp -0.89, loans_gdp +0.77, xs_mean_d3_loans_gdp -0.57, d5_loans_gdp -0.57, real_eq_capgain_3y -0.53, coal_share_co2 +0.52, real_hp_growth_3y -0.50, d1_real_eq_capgain_3y +0.42, r_minus_g +0.41, d3_loans_gdp +0.39, xs_crises_last2y +0.39
- **gdp_fall_3y**: fuel_self_sufficiency -1.24, oil_share_co2 -0.76, real_hp_growth_3y -0.57, d5_loans_gdp -0.50, base_d3_loans_gdp -0.49, xs_mean_d3_loans_gdp -0.48, energy_footprint_gap_3y -0.46, d3_loans_gdp +0.44, r_minus_g_lag1 -0.41, real_eq_capgain_3y_lag1 +0.39, loans_gdp +0.37, xs_share_credit_boom +0.30
- **unemp_spike_3y**: xs_mean_term_spread -0.75, xs_share_credit_boom +0.64, loans_gdp_lag3 +0.61, oil_real_price +0.61, r_minus_g +0.52, mort_gdp_lag3 -0.51, xs_mean_d3_loans_gdp -0.47, r_minus_g_lag1 -0.44, coal_share_co2 +0.41, fuel_self_sufficiency -0.39, ca_gdp -0.37, bloc_crises_last2y +0.35
- **crisis_3y**: co2_growth_3y -1.05, energy_footprint_gap_3y +0.81, xs_mean_term_spread -0.61, oil_share_co2 -0.57, base_term_spread +0.49, xs_mean_d3_loans_gdp +0.43, mort_gdp_lag3 +0.38, term_spread -0.38, speed_1y +0.38, fuel_self_sufficiency -0.35, real_eq_capgain_3y +0.35, base_d3_loans_gdp -0.35

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
