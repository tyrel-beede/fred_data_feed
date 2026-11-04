# bdc_cases.csv schema note

The 2018 free edition has no statistics table; each case is a fixed-template auto-summary whose numbers sit in sentence slots. Columns are named after those slots. The two halves of the compendium were encoded separately; the second half's column names were mapped onto the first half's where the slot is the same statistic:

- `debt_gdp_precrisis_peak_pct` -> `debt_gdp_peak_pct`
- `fx_debt_gdp_pct` -> `fx_debt_pct_gdp`
- `investment_inflows_avg_gdp_pct` -> `capital_inflows_bubble_pct_gdp`
- `current_account_deficit_gdp_pct` -> `current_account_bubble_pct_gdp`
- `bubble_real_growth_pct` -> `real_growth_bubble_pct`
- `gdp_gap_peak_pct` -> `gdp_gap_peak_bubble_pct`
- `bubble_equity_return_ann_pct` -> `equity_return_bubble_ann_pct`
- `real_fx_peak_pct` -> `real_fx_peak_bubble_pct`
- `debt_service_precrisis_peak_gdp_pct` -> `debt_service_peak_pct_gdp`
- `shock_trigger` -> `shock`
- `capital_inflows_fall_gdp_pct` -> `capital_inflow_fall_depression_pct_gdp`
- `equity_decline_pct` -> `equity_drawdown_pct`
- `unemployment_change_pp` -> `unemployment_increase_depression_pct`
- `peak_fiscal_deficit_gdp_pct` -> `peak_fiscal_deficit_ugly_period_pct_gdp`
- `imf_program` -> `imf_program_yes_no`
- `years_to_regain_gdp_peak` -> `years_to_regain_real_gdp_peak`
- `deleveraging_driver` -> `debt_reduction_drivers_reflation`
- `ugly_phase_vs_average` -> `bust_length_vs_average`

Columns that exist in only one half are kept as encoded (units can differ between halves for rate changes: `short_rate_rise_depression` vs `short_rate_hike_pct`; `inflation_peak_pct` vs `inflation_peak_depression_pct`). Blank cells mean the book gives no number for that slot. Provenance: DALIO-BDC-2018, Bridgewater-derived statistics; see history/sources.json.
