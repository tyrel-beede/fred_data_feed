# A learner that can weight — walk-forward

**Topology features added (12): in_peg, is_base, bloc_size, bloc_share, bloc_tenure, regime_change_3y, bloc_churn_3y, base_changed_5y, n_blocs, panel_peg_share, panel_changes_3y, years_since_break.** Compare with learner_test.md (same harness without them).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical + 12 topology = 78. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.60 (top 33%) | 0.66 (top 27%) | 0.74 (top 44%) | 0.62 (top 25%) |
| credit_contraction_3y (19%) | 0.60 (top 41%) | 0.64 (top 41%) | 0.65 (top 47%) | 0.67 (top 43%) |
| gdp_fall_3y (12%) | 0.66 (top 19%) | 0.65 (top 34%) | 0.59 (top 18%) | 0.54 (top 15%) |
| unemp_spike_3y (10%) | 0.52 (top 11%) | 0.61 (top 27%) | 0.59 (top 17%) | 0.61 (top 17%) |
| crisis_3y (9%) | 0.57 (top 13%) | 0.59 (top 16%) | 0.56 (top 14%) | 0.60 (top 16%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.54 / 0.91 | 0.60 / 0.94 | 0.69 / 0.92 | 0.65 / 0.49 |
| credit_contraction_3y | 0.57 / 0.71 | 0.61 / 0.80 | 0.63 / 0.76 | 0.65 / 0.79 |
| gdp_fall_3y | 0.67 / 0.53 | 0.70 / 0.37 | 0.60 / 0.54 | 0.53 / 0.59 |
| unemp_spike_3y | 0.49 / 0.69 | 0.58 / 0.83 | 0.56 / 0.83 | 0.57 / 0.83 |
| crisis_3y | 0.63 / 0.31 | 0.58 / 0.63 | 0.57 / 0.46 | 0.60 / 0.58 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.17, eq_dp -0.93, oil_share_co2 -0.70, xs_crises_last2y -0.61, in_peg +0.60, years_since_break +0.58, n_blocs -0.58, real_ltrate_expost -0.58, xs_share_credit_boom +0.56, energy_footprint_gap_3y +0.51, base_changed_5y +0.51, co2_growth_3y -0.49
- **credit_contraction_3y**: loans_gdp_lag3 +1.67, mort_gdp -0.98, loans_gdp +0.76, d5_loans_gdp -0.53, coal_share_co2 +0.53, panel_peg_share -0.51, real_eq_capgain_3y -0.50, oil_share_co2 +0.44, r_minus_g +0.44, real_hp_growth_3y -0.42, oil_real_price -0.35, d1_real_eq_capgain_3y +0.34
- **gdp_fall_3y**: fuel_self_sufficiency -1.16, base_d3_loans_gdp -0.87, n_blocs -0.78, bloc_crises_last2y +0.70, real_hp_growth_3y -0.62, years_since_break -0.59, xs_crises_last2y -0.53, bloc_share -0.52, r_minus_g_lag1 -0.49, in_peg +0.42, base_changed_5y +0.42, d5_loans_gdp -0.37
- **unemp_spike_3y**: oil_real_price +1.08, n_blocs -1.02, r_minus_g_lag1 -0.90, xs_mean_term_spread -0.82, loans_gdp_lag3 +0.73, panel_peg_share +0.60, bloc_crises_last2y +0.58, in_peg +0.56, xs_mean_req3y -0.50, bloc_size -0.50, xs_crises_last2y -0.47, mort_gdp_lag3 -0.46
- **crisis_3y**: n_blocs -1.29, panel_changes_3y -0.95, xs_mean_d3_loans_gdp +0.95, co2_growth_3y -0.91, years_since_break -0.82, energy_footprint_gap_3y +0.75, bloc_size -0.61, base_d3_loans_gdp -0.60, mort_gdp -0.49, oil_real_price +0.47, oil_share_co2 -0.47, panel_peg_share +0.46

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
