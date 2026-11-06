# A learner that can weight — walk-forward

**Measured energy:** energy_footprint_gap_3y and gap_anom_3y are taken from measured energy consumption where it exists (fgap_src = energy: OWID 1968-, EIA for the US 1952-, KMW for eight European countries 1873-) and from the CO2 proxy elsewhere. Compare with learner_test_physical_era.md (the proxy everywhere).


**Physical features added (13): energy_footprint_gap_3y, gap_anom_3y, d3_co2_intensity, co2_growth_3y, co2_growth_1y, fossil_prod_growth_3y, fuel_self_sufficiency, coal_share_co2, oil_share_co2, oil_real_price, oil_real_change_1y, oil_real_change_3y, oil_change_x_exposure.** Compare with learner_test.md (same harness without them).


Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers + 13 physical = 66. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.61 (top 35%) | 0.60 (top 23%) | 0.76 (top 41%) | 0.62 (top 27%) |
| credit_contraction_3y (19%) | 0.63 (top 37%) | 0.67 (top 53%) | 0.64 (top 47%) | 0.69 (top 44%) |
| gdp_fall_3y (11%) | 0.65 (top 22%) | 0.68 (top 35%) | 0.62 (top 19%) | 0.54 (top 14%) |
| unemp_spike_3y (10%) | 0.55 (top 13%) | 0.55 (top 25%) | 0.67 (top 23%) | 0.61 (top 20%) |
| crisis_3y (9%) | 0.57 (top 13%) | 0.57 (top 15%) | 0.63 (top 20%) | 0.59 (top 18%) |

## AUC by query era (before / from 2004)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.55 / 0.92 | 0.61 / 0.80 | 0.71 / 0.91 | 0.66 / 0.48 |
| credit_contraction_3y | 0.60 / 0.72 | 0.64 / 0.84 | 0.61 / 0.75 | 0.66 / 0.80 |
| gdp_fall_3y | 0.67 / 0.55 | 0.73 / 0.36 | 0.62 / 0.70 | 0.53 / 0.67 |
| unemp_spike_3y | 0.53 / 0.69 | 0.51 / 0.76 | 0.64 / 0.85 | 0.57 / 0.83 |
| crisis_3y | 0.64 / 0.30 | 0.58 / 0.57 | 0.63 / 0.67 | 0.60 / 0.56 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.15, real_ltrate_expost -0.79, xs_share_credit_boom +0.68, oil_share_co2 -0.68, eq_dp -0.63, speed_2y +0.57, oil_real_price -0.52, bloc_crises_last2y -0.51, loans_gdp_lag3 +0.50, oil_real_change_3y +0.48, rgdp_pc_growth -0.41, real_eq_capgain_3y_lag1 +0.39
- **credit_contraction_3y**: loans_gdp_lag3 +1.57, mort_gdp -0.92, loans_gdp +0.83, d5_loans_gdp -0.60, real_eq_capgain_3y -0.51, xs_mean_d3_loans_gdp -0.50, real_hp_growth_3y -0.49, coal_share_co2 +0.46, d1_real_eq_capgain_3y +0.40, speed_1y +0.39, r_minus_g +0.38, xs_crises_last2y +0.37
- **gdp_fall_3y**: fuel_self_sufficiency -1.26, oil_share_co2 -0.68, real_hp_growth_3y -0.58, base_d3_loans_gdp -0.51, d5_loans_gdp -0.48, d3_loans_gdp +0.43, xs_mean_d3_loans_gdp -0.41, r_minus_g_lag1 -0.40, real_eq_capgain_3y_lag1 +0.39, loans_gdp +0.39, ca_gdp -0.30, d3_co2_intensity -0.28
- **unemp_spike_3y**: xs_mean_term_spread -0.72, xs_share_credit_boom +0.61, loans_gdp_lag3 +0.61, oil_real_price +0.59, r_minus_g +0.51, mort_gdp_lag3 -0.51, coal_share_co2 +0.48, r_minus_g_lag1 -0.43, fuel_self_sufficiency -0.43, xs_mean_d3_loans_gdp -0.42, ca_gdp -0.37, bloc_crises_last2y +0.35
- **crisis_3y**: xs_mean_term_spread -0.61, oil_share_co2 -0.55, base_term_spread +0.50, xs_mean_d3_loans_gdp +0.48, fuel_self_sufficiency -0.38, base_d3_loans_gdp -0.38, speed_1y +0.37, term_spread -0.37, mort_gdp_lag3 +0.35, rank_rhp3y +0.35, mk_equity_le0_T-1 +0.35, real_eq_capgain_3y +0.35

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
