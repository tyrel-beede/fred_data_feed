# The SEC layer over its record

Built 2026-11-07 by `tools/sec_analysis.py` from `sec_fsds_quarterly.csv` (financial statements, 10-K/10-Q filers, 2009–2025) and `sec_13f_quarterly.csv` (institutional holdings). Sums are over every filer reporting the tag; the filer population changed with the XBRL phase-in (large accelerated filers in 2009–2010, all filers from mid-2011) and drifts with listings and tag usage, so the record is read through ratios and same-period comparisons, and levels carry their filer counts. Where the aggregates carry a sector split (aggregator v3) the reads use the **nonfinancial** filers (SIC outside 6000–6799); older aggregates are all filers, and the `sector` column says which each row is.

## 1. Annual cash flows of the December-fiscal-year filers ($bn, 10-K `qtrs=4` rows at December 31)

| year | sector | filers (OCF) | operating cash flow | capex | buybacks | common dividends | net income | D&A |
|---|---|---|---|---|---|---|---|---|
| 2009* | nonfinancial | 1852 | 809 | 269 | 88 | 78 | 280 | 223 |
| 2010* | nonfinancial | 2617 | 899 | 291 | 160 | 93 | 416 | 245 |
| 2011 | nonfinancial | 2664 | 998 | 349 | 253 | 99 | 490 | 260 |
| 2012 | nonfinancial | 2265 | 914 | 423 | 238 | 133 | 478 | 271 |
| 2013 | nonfinancial | 2282 | 991 | 439 | 283 | 130 | 549 | 297 |
| 2014 | nonfinancial | 1750 | 920 | 478 | 333 | 141 | 513 | 326 |
| 2015 | nonfinancial | 1547 | 870 | 442 | 325 | 140 | 300 | 361 |
| 2016 | nonfinancial | 1845 | 1,009 | 423 | 272 | 147 | 402 | 328 |
| 2017 | nonfinancial | 2321 | 1,092 | 423 | 251 | 148 | 534 | 348 |
| 2018 | nonfinancial | 2535 | 1,333 | 440 | 384 | 153 | 545 | 354 |
| 2019 | nonfinancial | 2690 | 1,426 | 449 | 302 | 175 | 539 | 382 |
| 2020 | nonfinancial | 2980 | 1,331 | 391 | 240 | 172 | 140 | 433 |
| 2021 | nonfinancial | 3030 | 1,645 | 421 | 382 | 181 | 846 | 427 |
| 2022 | nonfinancial | 3047 | 1,708 | 523 | 546 | 192 | 801 | 445 |
| 2023 | nonfinancial | 2775 | 1,825 | 573 | 445 | 196 | 866 | 467 |
| 2024 | nonfinancial | 2786 | 1,853 | 603 | 492 | 203 | 876 | 505 |
| 2025 | nonfinancial | 2724 | 2,127 | 720 | 517 | 209 | 1,020 | 536 |

\* phase-in years (large accelerated filers only). Dividends are the `PaymentsOfDividendsCommonStock` tag (408 filers in 2025); the broader `PaymentsOfDividends` tag is carried in the JSON and not added to it, since some filers report both.

## 2. The ratios, and where the latest year sits

Aggregate ratios (sum over sum) per year; the percentile is the share of years in the record at or below the latest reading (100% = the highest in the record).

| ratio | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | latest percentile |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| capital expenditures / operating cash flow | 0.33 | 0.32 | 0.35 | 0.46 | 0.44 | 0.52 | 0.51 | 0.42 | 0.39 | 0.33 | 0.31 | 0.29 | 0.26 | 0.31 | 0.31 | 0.33 | 0.34 | 59% |
| buybacks / operating cash flow | 0.11 | 0.18 | 0.25 | 0.26 | 0.29 | 0.36 | 0.37 | 0.27 | 0.23 | 0.29 | 0.21 | 0.18 | 0.23 | 0.32 | 0.24 | 0.27 | 0.24 | 41% |
| common dividends / operating cash flow | 0.10 | 0.10 | 0.10 | 0.15 | 0.13 | 0.15 | 0.16 | 0.15 | 0.14 | 0.11 | 0.12 | 0.13 | 0.11 | 0.11 | 0.11 | 0.11 | 0.10 | 12% |
| buybacks + common dividends / operating cash flow | 0.21 | 0.28 | 0.35 | 0.41 | 0.42 | 0.51 | 0.53 | 0.41 | 0.36 | 0.40 | 0.33 | 0.31 | 0.34 | 0.43 | 0.35 | 0.38 | 0.34 | 29% |
| buybacks + common dividends / net income | 0.59 | 0.61 | 0.72 | 0.78 | 0.75 | 0.92 | 1.55 | 1.04 | 0.75 | 0.98 | 0.88 | 2.95 | 0.67 | 0.92 | 0.74 | 0.79 | 0.71 | 24% |
| capital expenditures / depreciation and amortization | 1.21 | 1.19 | 1.34 | 1.56 | 1.48 | 1.47 | 1.22 | 1.29 | 1.22 | 1.24 | 1.18 | 0.90 | 0.99 | 1.18 | 1.23 | 1.19 | 1.34 | 82% |
| cash and equivalents / assets (Dec 31) | 0.07 | 0.08 | 0.07 | 0.07 | 0.07 | 0.06 | 0.06 | 0.06 | 0.07 | 0.05 | 0.06 | 0.07 | 0.07 | 0.06 | 0.07 | 0.06 | 0.06 | 41% |
| liabilities / assets (Dec 31) | 0.37 | 0.37 | 0.36 | 0.36 | 0.35 | 0.37 | 0.37 | 0.37 | 0.34 | 0.31 | 0.37 | 0.38 | 0.38 | 0.38 | 0.38 | 0.39 | 0.39 | 94% |
| inventories / assets (Dec 31) | 0.04 | 0.04 | 0.04 | 0.05 | 0.05 | 0.04 | 0.04 | 0.04 | 0.05 | 0.04 | 0.04 | 0.04 | 0.04 | 0.05 | 0.05 | 0.04 | 0.04 | 47% |
| long-term debt (noncurrent) / stockholders' equity (Dec 31) | 1.06 | 0.50 | 0.47 | 0.45 | 0.43 | 0.48 | 0.58 | 0.62 | 0.67 | 0.60 | 0.61 | 0.64 | 0.58 | 0.56 | 0.53 | 0.51 | 0.50 | 35% |

Balance-sheet ratios use the December-31 levels (`qtrs=0`); long-term debt is the `LongTermDebtNoncurrent` tag, which a minority of filers use, so that ratio is the thinnest of the set.

## 3. December-31 balance sheets ($bn)

The table takes, for each tag and date, the quarterly file with the most filers reporting it; the last two columns give the assets and equity sums in the first file that carried the date (the 10-Ks) and the ratio of the chosen sum to it. A ratio far from one means the chosen file (10-Q comparatives) carries inflated or duplicated values for that date — see section 7.

| year | filers (assets) | assets | liabilities | equity | cash | inventories | long-term debt (noncurrent; filers) | assets, 10-K file (ratio) | equity, 10-K file (ratio) |
|---|---|---|---|---|---|---|---|---|---|
| 2009 | 800 | 8,861 | 3,252 | 974 | 657 | 342 | 1,037 (415) |  | 974 (1.00) |
| 2010 | 3793 | 11,268 | 4,148 | 3,081 | 901 | 445 | 1,541 (1178) | 11,268 (1.00) | 2,996 (1.03) |
| 2011 | 4011 | 13,534 | 4,897 | 3,855 | 959 | 599 | 1,823 (1309) | 13,534 (1.00) | 3,855 (1.00) |
| 2012 | 3593 | 13,019 | 4,700 | 4,143 | 906 | 650 | 1,875 (1214) | 14,432 (0.90) | 4,143 (1.00) |
| 2013 | 3820 | 15,412 | 5,434 | 4,631 | 1,045 | 699 | 2,012 (1275) | 15,412 (1.00) | 4,631 (1.00) |
| 2014 | 3835 | 16,224 | 5,941 | 4,670 | 1,016 | 716 | 2,241 (1306) | 16,224 (1.00) | 4,670 (1.00) |
| 2015 | 3643 | 16,469 | 6,141 | 4,533 | 930 | 695 | 2,626 (1294) | 16,469 (1.00) | 4,533 (1.00) |
| 2016 | 3499 | 17,131 | 6,329 | 4,623 | 953 | 688 | 2,865 (1251) | 17,131 (1.00) | 4,623 (1.00) |
| 2017 | 3191 | 15,904 | 5,484 | 4,427 | 1,123 | 756 | 2,982 (1193) | 18,250 (0.87) | 5,113 (0.87) |
| 2018 | 3127 | 18,516 | 5,713 | 4,820 | 1,000 | 791 | 2,890 (1172) | 18,516 (1.00) | 5,231 (0.92) |
| 2019 | 3187 | 19,027 | 6,955 | 4,948 | 1,056 | 771 | 3,040 (1146) | 19,027 (1.00) | 5,377 (0.92) |
| 2020 | 3458 | 17,846 | 6,868 | 5,169 | 1,221 | 795 | 3,331 (1203) | 20,444 (0.87) | 5,478 (0.94) |
| 2021 | 3681 | 21,799 | 8,207 | 5,752 | 1,493 | 931 | 3,364 (1277) | 21,799 (1.00) | 6,300 (0.91) |
| 2022 | 3683 | 22,561 | 8,630 | 6,125 | 1,303 | 1,067 | 3,426 (1232) | 22,561 (1.00) | 6,687 (0.92) |
| 2023 | 3338 | 20,609 | 7,923 | 6,491 | 1,391 | 1,066 | 3,467 (1116) | 23,531 (0.88) | 7,230 (0.90) |
| 2024 | 3356 | 24,439 | 9,528 | 6,873 | 1,381 | 1,078 | 3,530 (1112) | 24,439 (1.00) | 7,649 (0.90) |
| 2025 | 3299 | 26,356 | 10,272 | 7,530 | 1,524 | 1,161 | 3,801 (1093) | 26,356 (1.00) | 8,403 (0.90) |

## 4. The timely read: latest year-to-date flows against a year earlier ($bn)

**Q1 (three months to March 31), 2026 vs 2025** (nonfinancial filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 486 (3029) | 399 (3090) | 21.8% |
| capital expenditures | 231 (1874) | 177 (1906) | 30.4% |
| buybacks | 155 (881) | 156 (862) | -0.7% |
| common dividends | 61 (389) | 59 (403) | 3.3% |
| net income | 397 (3247) | 313 (3296) | 26.7% |

**H1 (six months to June 30), 2026 vs 2025** (nonfinancial filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,112 (3028) | 824 (3076) | 34.9% |
| capital expenditures | 460 (1937) | 335 (1976) | 37.2% |
| buybacks | 287 (981) | 273 (976) | 5.3% |
| common dividends | 110 (394) | 105 (410) | 4.4% |
| net income | 720 (2898) | 500 (2919) | 44.0% |

**nine months to September 30, 2025 vs 2024** (nonfinancial filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,459 (3074) | 1,306 (3198) | 11.7% |
| capital expenditures | 519 (2006) | 442 (2133) | 17.6% |
| buybacks | 396 (1010) | 371 (995) | 6.8% |
| common dividends | 157 (407) | 152 (418) | 3.1% |
| net income | 745 (2936) | 617 (3028) | 20.8% |

**fiscal year to December 31, 2025 vs 2024** (nonfinancial filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 2,127 (2724) | 1,853 (2786) | 14.8% |
| capital expenditures | 720 (1879) | 603 (1973) | 19.5% |
| buybacks | 517 (1077) | 492 (1070) | 5.0% |
| common dividends | 209 (408) | 203 (420) | 3.1% |
| net income | 1,020 (2633) | 876 (2654) | 16.4% |

10-Q cash-flow statements are year-to-date, so the June and September rows are cumulative; the comparison is same period, same statement, with the filer counts beside each sum (a change in the count is part of the change in the sum).

## 5. Calibration against the compiled national series

The financial-statement sums are the listed, XBRL-filing part of the sector; the Z.1 and NIPA series are the whole nonfinancial corporate sector, compiled. Coverage is the FSDS sum over the compiled flow; the growth correlation is between year-on-year log changes of the two.

| FSDS series | compiled series | years | coverage, first → latest | growth corr. (all years) | growth corr. after the phase-in |
|---|---|---|---|---|---|
| capex | Z.1 nonfinancial corporate capital expenditures | 2009–2025 | 0.25 → 0.23 | 0.69 (n=16) | 0.75 (n=14) |
| dividends_common | Z.1 nonfinancial corporate net dividends paid | 2009–2025 | 0.21 → 0.15 | 0.23 (n=16) | 0.26 (n=14) |
| net_income | NIPA nonfinancial corporate profits after tax | 2009–2025 | 0.46 → 0.46 | 0.38 (n=16) | 0.38 (n=14) |

Coverage of a quarter or so is expected: the FSDS sum counts only the filers using the one tag (purchases of property, plant and equipment, or dividends on common stock), while the Z.1 flows cover every nonfinancial corporation, listed or not, and capital expenditures there include intellectual-property products. The ratio's stability year to year, and the growth correlation, are the measures of agreement; the level is not.

## 6. Institutional holdings (Form 13F)

53 periods reduced by the current aggregator (v5: per-filer units, the set's own report period, lines and filers beyond any real size set aside), 0 provisional (an earlier reduction: right in the main, but a few sets carry option lines worth more than the market or a trillion-dollar issuer line), 0 stale (the first reduction, thousands era, known wrong), 1 partial (the SEC's first, incomplete set, left out). Re-reduce with `corporate_pull.py --only 13f --all --redo` from a desktop. Holdings value is the total excluding option lines, less the managers the build-time history audit flags (`sec_13f_flags.csv`: a manager counted twenty times off its own holdings in the nearest sets, or absent from every other set; the count per period is the last column).

| holdings date | status | filers | holdings value ($tn) | / Z.1 NFC equities | top-10 issuer share | HHI (issuers) | median filer top-10 share | put/call share | filers rescaled | flagged |
|---|---|---|---|---|---|---|---|---|---|---|
| 2013-06-30 | current | 3,367 | 17.1 | 0.86 | 10.1% | 0.0025 | 40.9% | 4.2% | 77 |  |
| 2013-09-30 | current | 3,399 | 18.2 | 0.86 | 9.5% | 0.0024 | 40.4% | 4.3% | 67 |  |
| 2013-12-31 | current | 3,703 | 20.4 | 0.90 | 9.9% | 0.0025 | 41.8% | 4.1% | 68 |  |
| 2014-03-31 | current | 3,719 | 19.9 | 0.85 | 9.7% | 0.0024 | 41.4% | 5.2% | 79 |  |
| 2014-06-30 | current | 3,751 | 21.0 | 0.85 | 9.2% | 0.0023 | 41.1% | 5.4% | 81 |  |
| 2014-09-30 | current | 3,744 | 20.9 | 0.86 | 9.3% | 0.0024 | 41.2% | 4.6% | 71 |  |
| 2014-12-31 | current | 4,035 | 21.8 | 0.86 | 9.3% | 0.0024 | 42.9% | 4.2% | 82 |  |
| 2015-03-31 | current | 4,054 | 21.8 | 0.86 | 8.9% | 0.0024 | 43.1% | 3.8% | 78 |  |
| 2015-06-30 | current | 4,064 | 21.8 | 0.86 | 9.0% | 0.0024 | 43.2% | 4.2% | 86 |  |
| 2015-09-30 | current | 4,059 | 20.1 | 0.86 | 9.3% | 0.0024 | 44.0% | 4.3% | 76 |  |
| 2015-12-31 | current | 4,231 | 21.1 | 0.87 | 10.2% | 0.0027 | 45.2% | 4.2% | 87 |  |
| 2016-03-31 | current | 4,196 | 20.7 | 0.84 | 10.1% | 0.0027 | 45.4% | 4.0% | 88 |  |
| 2016-06-30 | current | 4,200 | 21.0 | 0.83 | 9.8% | 0.0026 | 44.7% | 4.5% | 77 |  |
| 2016-09-30 | current | 4,178 | 21.6 | 0.84 | 10.2% | 0.0026 | 45.1% | 4.9% | 80 |  |
| 2016-12-31 | current | 4,346 | 22.9 | 0.89 | 10.4% | 0.0027 | 45.6% | 4.5% | 76 |  |
| 2017-03-31 | current | 4,339 | 24.5 | 0.90 | 10.6% | 0.0027 | 45.1% | 4.2% | 75 |  |
| 2017-06-30 | current | 4,344 | 24.4 | 0.88 | 10.9% | 0.0028 | 45.6% | 4.3% | 71 |  |
| 2017-09-30 | current | 4,329 | 25.5 | 0.90 | 10.8% | 0.0028 | 46.1% | 4.7% | 70 |  |
| 2017-12-31 | current | 4,676 | 27.2 | 0.91 | 11.5% | 0.0030 | 46.6% | 5.0% | 76 |  |
| 2018-03-31 | current | 4,685 | 26.5 | 0.89 | 11.5% | 0.0030 | 46.9% | 5.1% | 86 |  |
| 2018-06-30 | current | 4,688 | 27.5 | 0.89 | 12.0% | 0.0031 | 46.2% | 4.6% | 75 |  |
| 2018-09-30 | current | 4,700 | 29.0 | 0.89 | 12.6% | 0.0034 | 46.5% | 4.8% | 69 | 1 |
| 2018-12-31 | current | 5,023 | 25.1 | 0.90 | 12.3% | 0.0034 | 48.8% | 4.5% | 72 |  |
| 2019-03-31 | current | 5,012 | 27.7 | 0.87 | 12.3% | 0.0033 | 47.7% | 4.4% | 76 |  |
| 2019-06-30 | current | 4,990 | 29.3 | 0.90 | 12.5% | 0.0034 | 47.6% | 5.2% | 74 |  |
| 2019-09-30 | current | 4,985 | 28.8 | 0.88 | 12.8% | 0.0036 | 48.0% | 4.7% | 75 |  |
| 2019-12-31 | current | 5,392 | 32.2 | 0.92 | 13.7% | 0.0038 | 48.7% | 4.7% | 81 |  |
| 2020-03-31 | current | 5,353 | 24.8 | 0.89 | 16.0% | 0.0050 | 51.3% | 5.0% | 80 |  |
| 2020-06-30 | current | 5,344 | 29.8 | 0.86 | 17.0% | 0.0055 | 49.9% | 5.2% | 71 |  |
| 2020-09-30 | current | 5,335 | 32.2 | 0.85 | 17.3% | 0.0058 | 49.6% | 6.5% | 72 |  |
| 2020-12-31 | current | 5,854 | 38.0 | 0.87 | 15.9% | 0.0049 | 49.7% | 7.5% | 79 |  |
| 2021-03-31 | current | 5,891 | 39.4 | 0.84 | 14.9% | 0.0043 | 48.4% | 6.1% | 78 | 1 |
| 2021-06-30 | current | 5,941 | 42.7 | 0.85 | 15.8% | 0.0046 | 48.4% | 6.3% | 72 |  |
| 2021-09-30 | current | 5,946 | 42.6 | 0.84 | 16.0% | 0.0047 | 48.5% | 6.9% | 68 |  |
| 2021-12-31 | current | 6,699 | 46.7 | 0.86 | 17.2% | 0.0054 | 51.6% | 5.5% | 97 | 1 |
| 2022-03-31 | current | 6,720 | 43.3 | 0.84 | 17.0% | 0.0054 | 51.6% | 6.3% | 86 |  |
| 2022-06-30 | current | 6,728 | 36.3 | 0.86 | 15.8% | 0.0049 | 52.3% | 5.8% | 74 |  |
| 2022-09-30 | current | 6,714 | 34.5 | 0.85 | 16.2% | 0.0051 | 52.9% | 5.9% | 83 |  |
| 2022-12-31 | current | 6,912 | 37.1 | 0.88 | 14.5% | 0.0045 | 52.4% | 5.9% | 1204 |  |
| 2023-03-31 | current | 6,846 | 38.5 | 0.85 | 16.0% | 0.0053 | 52.9% | 6.5% | 851 |  |
| 2023-06-30 | current | 6,906 | 41.5 | 0.85 | 18.2% | 0.0063 | 53.3% | 6.6% | 767 | 1 |
| 2023-09-30 | current | 6,940 | 40.1 | 0.85 | 18.5% | 0.0061 | 53.3% | 6.9% | 690 |  |
| 2023-12-31 | current | 7,171 | 45.2 | 0.87 | 19.0% | 0.0064 | 53.3% | 7.5% | 640 | 1 |
| 2024-03-31 | current | 7,219 | 48.7 | 0.86 | 20.2% | 0.0067 | 53.1% | 7.1% | 605 |  |
| 2024-06-30 | current | 7,278 | 50.7 | 0.87 | 22.9% | 0.0082 | 53.6% | 6.5% | 561 |  |
| 2024-09-30 | current | 7,341 | 52.6 | 0.86 | 21.5% | 0.0075 | 53.2% | 6.9% | 540 |  |
| 2024-12-31 | current | 7,940 | 54.8 | 0.87 | 23.1% | 0.0082 | 54.1% | 7.2% | 517 |  |
| 2025-03-31 | current | 7,981 | 52.2 | 0.88 | 20.7% | 0.0070 | 53.7% | 6.8% | 462 |  |
| 2025-06-30 | current | 8,033 | 58.8 | 0.90 | 22.7% | 0.0081 | 53.6% | 7.1% | 443 | 1 |
| 2025-09-30 | current | 8,017 | 64.1 | 0.91 | 24.0% | 0.0089 | 53.1% | 7.7% | 375 |  |
| 2025-12-31 | current | 8,622 | 65.3 | 0.91 | 24.6% | 0.0088 | 54.2% | 6.8% | 390 | 1 |
| 2026-03-31 | current | 8,736 | 63.3 | 0.90 | 22.3% | 0.0076 | 54.1% | 6.9% | 361 |  |
| 2026-06-30 | current | 8,855 | 75.0 | 0.90 | 23.3% | 0.0079 | 54.2% | 7.9% | 345 | 2 |

Latest (2026-06-30): the ten most-held issuers are 23.3% of reported value (percentile 96% of the usable record), the median filer holds 54.2% of its value in its ten largest positions (98%), reported value is 0.90× the Z.1 market value of nonfinancial corporate equities (91%; 13F value includes financial issuers, foreign issuers and options, so the ratio is a coverage index, not a share).

The ten largest managers in the latest set (a sanity list: the names should be the ones a reader expects, and a stranger at the top is a scale error the caps did not catch):

| manager | holdings ($bn) | share | top-10 positions' share of its own holdings |
|---|---|---|---|
| BlackRock, Inc. | 6,713 | 8.8% | 12% |
| VANGUARD CAPITAL MANAGEMENT LLC | 4,680 | 6.1% | 33% |
| STATE STREET CORP | 3,371 | 4.4% | 29% |
| FMR LLC | 2,304 | 3.0% | 24% |
| VANGUARD PORTFOLIO MANAGEMENT LLC | 2,219 | 2.9% | 22% |
| MORGAN STANLEY | 1,891 | 2.5% | 10% |
| GEODE CAPITAL MANAGEMENT, LLC | 1,875 | 2.5% | 27% |
| JPMORGAN CHASE & CO | 1,712 | 2.2% | 15% |
| BANK OF AMERICA CORP /DE/ | 1,552 | 2.0% | 10% |
| Invesco Ltd. | 1,264 | 1.7% | 24% |

## 7. The same period across files: a consistency check

A December-31 figure appears first in the 10-Ks (the following quarter's set) and again as the comparative in later 10-Qs. The sums should agree; where they do not, the difference is duplicated or mis-scaled filer values in one file, and the sidecars written by aggregator v3 (`raw/SEC-FSDS/<q>_meta.json`: the values set aside and the five largest filers per key) say which.

| tag | period | file | filers | sum ($bn) | p90 ($m) | aggregator |
|---|---|---|---|---|---|---|
| Assets | 20241231 | 2025q1 | 4566 | 73,602 | 19,374 | v3 |
| Assets | 20241231 | 2025q2 | 4379 | 69,251 | 18,684 | v3 |
| Assets | 20241231 | 2025q3 | 4363 | 69,368 | 18,684 | v3 |
| Assets | 20241231 | 2025q4 | 4358 | 69,206 | 18,661 | v3 |
| Assets | 20241231 | 2026q1 | 3968 | 69,225 | 20,814 | v3 |
| Assets | 20251231 | 2026q1 | 4636 | 78,494 | 20,712 | v3 |
| Assets | 20251231 | 2026q2 | 4447 | 74,048 | 19,389 | v3 |
| Assets | 20251231 | 2026q3 | 4433 | 74,215 | 19,465 | v3 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2025q1 | 3838 | 2,320 | 1,299 | v3 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2026q1 | 3705 | 2,343 | 1,374 | v3 |
| NetCashProvidedByUsedInOperatingActivities | 20251231 | 2026q1 | 3830 | 2,485 | 1,369 | v3 |
| NetIncomeLoss | 20241231 | 2025q1 | 3616 | 1,464 | 718 | v3 |
| NetIncomeLoss | 20241231 | 2026q1 | 3559 | 1,486 | 775 | v3 |
| NetIncomeLoss | 20251231 | 2026q1 | 3675 | 1,625 | 782 | v3 |
| StockholdersEquity | 20241231 | 2025q1 | 4201 | 12,696 | 5,158 | v3 |
| StockholdersEquity | 20241231 | 2025q2 | 4305 | 11,830 | 4,729 | v3 |
| StockholdersEquity | 20241231 | 2025q3 | 4112 | 11,653 | 4,908 | v3 |
| StockholdersEquity | 20241231 | 2025q4 | 4038 | 11,630 | 5,077 | v3 |
| StockholdersEquity | 20241231 | 2026q1 | 4018 | 12,301 | 5,158 | v3 |
| StockholdersEquity | 20241231 | 2026q2 | 3001 | 3,999 | 2,170 | v3 |
| StockholdersEquity | 20241231 | 2026q3 | 2689 | 3,827 | 2,305 | v3 |
| StockholdersEquity | 20251231 | 2026q1 | 4269 | 14,014 | 5,541 | v3 |
| StockholdersEquity | 20251231 | 2026q2 | 4373 | 13,060 | 4,975 | v3 |
| StockholdersEquity | 20251231 | 2026q3 | 4151 | 12,819 | 5,208 | v3 |

## Reading rules

- Ratios and same-period changes are the comparable quantities; levels drift with the filer population and tag usage.
- The FSDS sums are first-reported values from the latest-filed submission per filer and period (aggregator v2) or the first value seen (v1 sets); restatements in later years are not propagated back.
- 13F value includes options (put/call lines, excluded from the issuer concentration), financial and foreign issuers; it is long-only and lagged (filed within 45 days of the quarter end).
- These are the live dials' corporate-sector and positioning reads; they are not learner features (US-only, one era deep).
