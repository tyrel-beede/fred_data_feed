# A learner that can weight — walk-forward

Models are refit every 4 years; a model fit at t forecasts years t..t+3 and is trained only on rows whose outcome window closed before t (training from 1880, queries from 1900); standardization and imputation from the training rows, mile-marker terciles from the training rows. Features: 20 base + 10 subnet + 6 rank + 9 flux + 5 selected leads + 3 markers = 53. AUC 0.5 is no skill.

| target (base rate) | knn (no weights) | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y (14%) | 0.65 (top 36%) | 0.61 (top 22%) | 0.73 (top 35%) | 0.64 (top 27%) |
| credit_contraction_3y (19%) | 0.68 (top 52%) | 0.68 (top 53%) | 0.65 (top 50%) | 0.69 (top 45%) |
| gdp_fall_3y (11%) | 0.61 (top 26%) | 0.60 (top 37%) | 0.58 (top 19%) | 0.52 (top 14%) |
| unemp_spike_3y (10%) | 0.57 (top 13%) | 0.61 (top 31%) | 0.67 (top 23%) | 0.64 (top 26%) |
| crisis_3y (9%) | 0.60 (top 15%) | 0.58 (top 20%) | 0.63 (top 19%) | 0.60 (top 19%) |

## Crisis label by horizon, logit

| 1y | 2y | 3y | 4y | 5y |
|---|---|---|---|---|
| 0.61 | 0.58 | 0.58 | 0.54 | 0.51 |

## Heaviest logit weights in the final (2020) fit

- **dd30_3y**: r_minus_g -1.21, real_ltrate_expost -0.84, xs_share_credit_boom +0.77, speed_2y +0.58, eq_dp -0.56, xs_mean_term_spread -0.54, rgdp_pc_growth -0.43, xs_crises_now -0.40, xs_crises_last2y -0.40, real_eq_capgain_3y_lag1 +0.37, bloc_crises_last2y -0.33, loans_gdp_lag3 +0.33
- **credit_contraction_3y**: loans_gdp_lag3 +1.59, mort_gdp -0.85, loans_gdp +0.71, d5_loans_gdp -0.62, xs_mean_d3_loans_gdp -0.53, r_minus_g +0.49, real_eq_capgain_3y -0.49, real_hp_growth_3y -0.48, speed_1y +0.47, xs_crises_last2y +0.39, d1_real_eq_capgain_3y +0.38, r_minus_g_lag1 +0.33
- **gdp_fall_3y**: loans_gdp +0.64, xs_mean_d3_loans_gdp -0.63, real_hp_growth_3y -0.62, base_d3_loans_gdp -0.50, d5_loans_gdp -0.50, xs_mean_term_spread -0.47, ltrate -0.42, d3_loans_gdp +0.42, ca_gdp -0.42, real_eq_capgain_3y_lag1 +0.37, mort_gdp_lag3 -0.34, rank_rhp3y +0.30
- **unemp_spike_3y**: loans_gdp_lag3 +1.00, xs_mean_term_spread -0.80, ca_gdp -0.69, r_minus_g +0.50, xs_share_credit_boom +0.47, r_minus_g_lag1 -0.44, mort_gdp_lag3 -0.42, d3_loans_gdp +0.42, iy -0.37, loans_gdp -0.34, xs_mean_d3_loans_gdp -0.33, real_hp_growth_3y -0.33
- **crisis_3y**: xs_mean_term_spread -0.76, mort_gdp -0.50, xs_mean_d3_loans_gdp +0.48, speed_1y +0.45, base_term_spread +0.44, mort_gdp_lag3 +0.44, base_d3_loans_gdp -0.43, real_eq_capgain_3y +0.42, iy -0.42, rank_rhp3y +0.37, mk_equity_le0_T-1 +0.36, debt_gdp +0.34

Reading: the gap between knn and the weighted learners on the same features is the value of weighting; the ensemble row says whether the learners disagree in a useful way. Walk-forward throughout, so these are the numbers a forecaster at the time could have had.
