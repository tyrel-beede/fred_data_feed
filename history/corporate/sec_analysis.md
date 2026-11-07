# The SEC layer over its record

Built 2026-11-07 by `tools/sec_analysis.py` from `sec_fsds_quarterly.csv` (financial statements, 10-K/10-Q filers, 2009–2025) and `sec_13f_quarterly.csv` (institutional holdings). Sums are over every filer reporting the tag; the filer population changed with the XBRL phase-in (large accelerated filers in 2009–2010, all filers from mid-2011) and drifts with listings and tag usage, so the record is read through ratios and same-period comparisons, and levels carry their filer counts. Where the aggregates carry a sector split (aggregator v3) the reads use the **nonfinancial** filers (SIC outside 6000–6799); older aggregates are all filers, and the `sector` column says which each row is.

## 1. Annual cash flows of the December-fiscal-year filers ($bn, 10-K `qtrs=4` rows at December 31)

| year | sector | filers (OCF) | operating cash flow | capex | buybacks | common dividends | net income | D&A |
|---|---|---|---|---|---|---|---|---|
| 2009* | all | 2710 | 1,139 | 298 | 109 | 101 | 247 | 244 |
| 2010* | all | 3803 | 1,301 | 322 | 207 | 117 | 561 | 266 |
| 2011 | all | 3894 | 1,479 | 388 | 314 | 127 | 659 | 283 |
| 2012 | all | 3216 | 1,412 | 465 | 314 | 171 | 710 | 300 |
| 2013 | all | 3248 | 1,547 | 483 | 367 | 176 | 933 | 330 |
| 2014 | all | 2467 | 1,197 | 528 | 443 | 194 | 811 | 362 |
| 2015 | all | 2216 | 1,170 | 484 | 459 | 199 | 596 | 394 |
| 2016 | all | 2677 | 1,358 | 463 | 409 | 210 | 708 | 363 |
| 2017 | all | 3321 | 1,447 | 463 | 443 | 218 | 842 | 384 |
| 2018 | all | 3591 | 1,856 | 488 | 603 | 223 | 877 | 394 |
| 2019 | all | 3746 | 1,987 | 502 | 545 | 262 | 1,002 | 424 |
| 2020 | all | 4029 | 1,624 | 437 | 389 | 254 | 451 | 473 |
| 2021 | all | 4387 | 2,385 | 468 | 626 | 272 | 1,474 | 469 |
| 2022 | all | 4310 | 2,625 | 577 | 770 | 301 | 1,162 | 491 |
| 2023 | all | 3790 | 2,456 | 630 | 666 | 299 | 1,369 | 523 |
| 2024 | all | 3838 | 2,320 | 660 | 753 | 297 | 1,464 | 564 |
| 2025 | all | 3830 | 2,485 | 785 | 844 | 313 | 1,625 | 596 |

\* phase-in years (large accelerated filers only). Dividends are the `PaymentsOfDividendsCommonStock` tag (823 filers in 2025); the broader `PaymentsOfDividends` tag is carried in the JSON and not added to it, since some filers report both.

## 2. The ratios, and where the latest year sits

Aggregate ratios (sum over sum) per year; the percentile is the share of years in the record at or below the latest reading (100% = the highest in the record).

| ratio | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | latest percentile |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| capital expenditures / operating cash flow | 0.26 | 0.25 | 0.26 | 0.33 | 0.31 | 0.44 | 0.41 | 0.34 | 0.32 | 0.26 | 0.25 | 0.27 | 0.20 | 0.22 | 0.26 | 0.28 | 0.32 | 71% |
| buybacks / operating cash flow | 0.10 | 0.16 | 0.21 | 0.22 | 0.24 | 0.37 | 0.39 | 0.30 | 0.31 | 0.32 | 0.27 | 0.24 | 0.26 | 0.29 | 0.27 | 0.32 | 0.34 | 88% |
| common dividends / operating cash flow | 0.09 | 0.09 | 0.09 | 0.12 | 0.11 | 0.16 | 0.17 | 0.15 | 0.15 | 0.12 | 0.13 | 0.16 | 0.11 | 0.11 | 0.12 | 0.13 | 0.13 | 59% |
| buybacks + common dividends / operating cash flow | 0.18 | 0.25 | 0.30 | 0.34 | 0.35 | 0.53 | 0.56 | 0.46 | 0.46 | 0.44 | 0.41 | 0.40 | 0.38 | 0.41 | 0.39 | 0.45 | 0.47 | 88% |
| buybacks + common dividends / net income | 0.85 | 0.58 | 0.67 | 0.68 | 0.58 | 0.79 | 1.11 | 0.87 | 0.78 | 0.94 | 0.81 | 1.43 | 0.61 | 0.92 | 0.71 | 0.72 | 0.71 | 41% |
| capital expenditures / depreciation and amortization | 1.22 | 1.21 | 1.37 | 1.55 | 1.47 | 1.46 | 1.23 | 1.28 | 1.21 | 1.24 | 1.19 | 0.92 | 1.00 | 1.18 | 1.21 | 1.17 | 1.32 | 76% |
| cash and equivalents / assets (Dec 31) | 0.05 | 0.03 | 0.04 | 0.04 | 0.04 | 0.04 | 0.03 | 0.03 | 0.04 | 0.04 | 0.03 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03 | 0.03 | 12% |
| liabilities / assets (Dec 31) | 0.72 | 0.76 | 0.73 | 0.73 | 0.71 | 0.71 | 0.71 | 0.71 | 0.71 | 0.68 | 0.70 | 0.74 | 0.69 | 0.72 | 0.74 | 0.72 | 0.71 | 47% |
| inventories / assets (Dec 31) | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 | 0.02 | 0.02 | 88% |
| long-term debt (noncurrent) / stockholders' equity (Dec 31) | 0.45 | 0.28 | 0.28 | 0.28 | 0.27 | 0.29 | 0.35 | 0.37 | 0.38 | 0.35 | 0.36 | 0.38 | 0.35 | 0.35 | 0.34 | 0.33 | 0.32 | 35% |

Balance-sheet ratios use the December-31 levels (`qtrs=0`); long-term debt is the `LongTermDebtNoncurrent` tag, which a minority of filers use, so that ratio is the thinnest of the set.

## 3. December-31 balance sheets ($bn)

The table takes, for each tag and date, the quarterly file with the most filers reporting it; the last two columns give the assets and equity sums in the first file that carried the date (the 10-Ks) and the ratio of the chosen sum to it. A ratio far from one means the chosen file (10-Q comparatives) carries inflated or duplicated values for that date — see section 7.

| year | filers (assets) | assets | liabilities | equity | cash | inventories | long-term debt (noncurrent; filers) | assets, 10-K file (ratio) | equity, 10-K file (ratio) |
|---|---|---|---|---|---|---|---|---|---|
| 2009 | 1067 | 27,589 | 19,821 | 2,450 | 1,275 | 348 | 1,112 (440) | 27,436 (1.01) | 2,450 (1.00) |
| 2010 | 5337 | 46,551 | 35,610 | 5,797 | 1,602 | 453 | 1,649 (1223) | 32,457 (1.43) | 5,315 (1.09) |
| 2011 | 5624 | 45,438 | 33,230 | 6,822 | 1,772 | 610 | 1,937 (1362) | 45,438 (1.00) | 6,822 (1.00) |
| 2012 | 5034 | 44,107 | 32,300 | 7,245 | 1,574 | 661 | 2,020 (1271) | 42,492 (1.04) | 7,245 (1.00) |
| 2013 | 5281 | 47,612 | 33,870 | 7,888 | 1,761 | 711 | 2,156 (1325) | 47,612 (1.00) | 7,888 (1.00) |
| 2014 | 5280 | 49,937 | 35,536 | 8,210 | 1,756 | 728 | 2,395 (1366) | 49,937 (1.00) | 8,210 (1.00) |
| 2015 | 5039 | 49,433 | 35,095 | 8,013 | 1,707 | 709 | 2,793 (1355) | 49,433 (1.00) | 8,013 (1.00) |
| 2016 | 4817 | 51,386 | 36,443 | 8,319 | 1,752 | 706 | 3,045 (1315) | 51,386 (1.00) | 8,319 (1.00) |
| 2017 | 4460 | 51,776 | 36,971 | 8,309 | 1,951 | 774 | 3,156 (1256) | 54,115 (0.96) | 8,995 (0.92) |
| 2018 | 4351 | 55,002 | 37,298 | 8,685 | 2,295 | 814 | 3,074 (1238) | 55,002 (1.00) | 9,125 (0.95) |
| 2019 | 4418 | 54,963 | 38,363 | 9,112 | 1,785 | 795 | 3,246 (1211) | 54,963 (1.00) | 9,379 (0.97) |
| 2020 | 4902 | 60,244 | 44,305 | 9,346 | 2,098 | 818 | 3,548 (1264) | 63,378 (0.95) | 9,992 (0.94) |
| 2021 | 5273 | 67,772 | 46,509 | 10,389 | 2,587 | 959 | 3,600 (1347) | 67,772 (1.00) | 11,029 (0.94) |
| 2022 | 5084 | 68,788 | 49,393 | 10,387 | 2,209 | 1,100 | 3,682 (1305) | 68,788 (1.00) | 11,010 (0.94) |
| 2023 | 4552 | 68,318 | 50,341 | 11,108 | 2,057 | 1,098 | 3,747 (1184) | 71,787 (0.95) | 11,938 (0.93) |
| 2024 | 4566 | 73,602 | 52,820 | 11,830 | 2,252 | 1,110 | 3,871 (1184) | 73,602 (1.00) | 12,696 (0.93) |
| 2025 | 4636 | 78,494 | 55,865 | 13,060 | 2,371 | 1,194 | 4,151 (1169) | 78,494 (1.00) | 14,014 (0.93) |

## 4. The timely read: latest year-to-date flows against a year earlier ($bn)

**Q1 (three months to March 31), 2026 vs 2025** (all filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 407 (4313) | 134 (4254) | 202.6% |
| capital expenditures | 249 (2310) | 190 (2352) | 30.9% |
| buybacks | 263 (1388) | 233 (1348) | 12.9% |
| common dividends | 97 (790) | 89 (813) | 9.1% |
| net income | 513 (4552) | 422 (4432) | 21.7% |

**H1 (six months to June 30), 2026 vs 2025** (all filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,224 (4323) | 702 (4275) | 74.3% |
| capital expenditures | 497 (2386) | 364 (2432) | 36.6% |
| buybacks | 495 (1542) | 421 (1512) | 17.7% |
| common dividends | 172 (792) | 161 (829) | 6.9% |
| net income | 985 (4139) | 776 (4024) | 26.9% |

**nine months to September 30, 2025 vs 2024** (all filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,512 (4281) | 1,376 (4346) | 9.9% |
| capital expenditures | 565 (2464) | 483 (2607) | 17.0% |
| buybacks | 626 (1550) | 564 (1529) | 10.9% |
| common dividends | 239 (826) | 227 (844) | 5.3% |
| net income | 1,211 (4048) | 1,036 (4079) | 16.9% |

**fiscal year to December 31, 2025 vs 2024** (all filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 2,485 (3830) | 2,320 (3838) | 7.1% |
| capital expenditures | 785 (2326) | 660 (2434) | 18.9% |
| buybacks | 844 (1661) | 753 (1653) | 12.0% |
| common dividends | 313 (823) | 297 (846) | 5.5% |
| net income | 1,625 (3675) | 1,464 (3616) | 11.0% |

10-Q cash-flow statements are year-to-date, so the June and September rows are cumulative; the comparison is same period, same statement, with the filer counts beside each sum (a change in the count is part of the change in the sum).

## 5. Calibration against the compiled national series

The financial-statement sums are the listed, XBRL-filing part of the sector; the Z.1 and NIPA series are the whole nonfinancial corporate sector, compiled. Coverage is the FSDS sum over the compiled flow; the growth correlation is between year-on-year log changes of the two.

| FSDS series | compiled series | years | coverage, first → latest | growth corr. (all years) | growth corr. after the phase-in |
|---|---|---|---|---|---|
| capex | Z.1 nonfinancial corporate capital expenditures | 2009–2025 | 0.27 → 0.26 | 0.69 (n=16) | 0.75 (n=14) |
| dividends_common | Z.1 nonfinancial corporate net dividends paid | 2009–2025 | 0.27 → 0.22 | 0.31 (n=16) | 0.33 (n=14) |
| net_income | NIPA nonfinancial corporate profits after tax | 2009–2025 | 0.41 → 0.73 | 0.52 (n=16) | 0.41 (n=14) |

Coverage of a quarter or so is expected: the FSDS sum counts only the filers using the one tag (purchases of property, plant and equipment, or dividends on common stock), while the Z.1 flows cover every nonfinancial corporation, listed or not, and capital expenditures there include intellectual-property products. The ratio's stability year to year, and the growth correlation, are the measures of agreement; the level is not.

## 6. Institutional holdings (Form 13F)

0 periods reduced by the current aggregator (v3: per-filer units, the set's own report period, lines and filers beyond any real size set aside), 52 provisional (an earlier reduction: right in the main, but a few sets carry option lines worth more than the market or a trillion-dollar issuer line), 0 stale (the first reduction, thousands era, known wrong), 1 partial (the SEC's first, incomplete set, left out). Re-reduce with `corporate_pull.py --only 13f --all --redo` from a desktop. Value is the total excluding option lines where the summary carries it.

| holdings date | status | filers | holdings value ($tn) | / Z.1 NFC equities | top-10 issuer share | HHI (issuers) | median filer top-10 share | put/call share | filers rescaled |
|---|---|---|---|---|---|---|---|---|---|
| 2013-06-30 | provisional | 3,369 | 19.0 | 0.95 | 14.4% | 0.0054 | 41.0% | 3.9% | 77 |
| 2013-09-30 | provisional | 3,400 | 22.4 | 1.06 | 12.2% | 0.0032 | 40.4% | 3.7% | 69 |
| 2013-12-31 | provisional | 3,703 | 21.2 | 0.94 | 9.9% | 0.0025 | 41.8% | 4.1% | 68 |
| 2014-03-31 | provisional | 3,719 | 21.0 | 0.90 | 9.7% | 0.0024 | 41.4% | 5.2% | 79 |
| 2014-06-30 | provisional | 3,751 | 22.2 | 0.91 | 9.2% | 0.0023 | 41.1% | 5.4% | 81 |
| 2014-09-30 | provisional | 3,744 | 21.9 | 0.90 | 9.3% | 0.0024 | 41.2% | 4.6% | 71 |
| 2014-12-31 | provisional | 4,036 | 23.3 | 0.92 | 9.1% | 0.0024 | 42.9% | 4.1% | 83 |
| 2015-03-31 | provisional | 4,054 | 22.7 | 0.89 | 8.9% | 0.0024 | 43.1% | 3.8% | 78 |
| 2015-06-30 | provisional | 4,066 | 26.2 | 1.04 | 8.8% | 0.0023 | 43.2% | 5.2% | 88 |
| 2015-09-30 | provisional | 4,059 | 21.0 | 0.90 | 9.3% | 0.0024 | 44.0% | 4.3% | 76 |
| 2015-12-31 | provisional | 4,232 | 22.7 | 0.93 | 10.0% | 0.0026 | 45.2% | 4.1% | 87 |
| 2016-03-31 | provisional | 4,196 | 21.6 | 0.87 | 10.1% | 0.0027 | 45.4% | 4.0% | 88 |
| 2016-06-30 | provisional | 4,202 | 23.4 | 0.93 | 9.7% | 0.0025 | 44.6% | 4.3% | 77 |
| 2016-09-30 | provisional | 4,178 | 22.7 | 0.88 | 10.2% | 0.0026 | 45.1% | 4.9% | 80 |
| 2016-12-31 | provisional | 4,346 | 24.0 | 0.93 | 10.4% | 0.0027 | 45.6% | 4.5% | 76 |
| 2017-03-31 | provisional | 4,339 | 25.6 | 0.94 | 10.6% | 0.0027 | 45.1% | 4.2% | 75 |
| 2017-06-30 | provisional | 4,344 | 25.5 | 0.92 | 10.9% | 0.0028 | 45.6% | 4.3% | 71 |
| 2017-09-30 | provisional | 4,329 | 26.7 | 0.94 | 10.8% | 0.0028 | 46.1% | 4.7% | 70 |
| 2017-12-31 | provisional | 4,676 | 28.6 | 0.95 | 11.5% | 0.0030 | 46.6% | 5.0% | 76 |
| 2018-03-31 | provisional | 4,685 | 27.9 | 0.94 | 11.5% | 0.0030 | 46.9% | 5.1% | 86 |
| 2018-06-30 | provisional | 4,689 | 40.6 | 1.32 | 11.5% | 0.0029 | 46.2% | 28.8% | 76 |
| 2018-09-30 | provisional | 4,700 | 31.0 | 0.95 | 12.5% | 0.0033 | 46.5% | 4.8% | 69 |
| 2018-12-31 | provisional | 5,024 | 26.9 | 0.96 | 13.8% | 0.0038 | 48.8% | 4.5% | 73 |
| 2019-03-31 | provisional | 5,013 | 38.0 | 1.19 | 12.0% | 0.0032 | 47.7% | 24.9% | 77 |
| 2019-06-30 | provisional | 4,990 | 31.0 | 0.95 | 12.5% | 0.0034 | 47.6% | 5.2% | 74 |
| 2019-09-30 | provisional | 4,986 | 36.8 | 1.12 | 11.7% | 0.0036 | 48.0% | 3.9% | 75 |
| 2019-12-31 | provisional | 5,392 | 33.8 | 0.96 | 13.7% | 0.0038 | 48.7% | 4.8% | 81 |
| 2020-03-31 | provisional | 5,353 | 26.2 | 0.93 | 16.0% | 0.0050 | 51.3% | 5.1% | 80 |
| 2020-06-30 | provisional | 5,345 | 53.2 | 1.54 | 16.1% | 0.0050 | 49.9% | 40.7% | 72 |
| 2020-09-30 | provisional | 5,335 | 34.5 | 0.91 | 17.3% | 0.0058 | 49.6% | 6.5% | 72 |
| 2020-12-31 | provisional | 5,856 | 99.8 | 2.28 | 14.6% | 0.0042 | 49.7% | 57.6% | 81 |
| 2021-03-31 | provisional | 5,891 | 44.0 | 0.94 | 16.8% | 0.0049 | 48.4% | 6.0% | 79 |
| 2021-06-30 | provisional | 5,942 | 53.5 | 1.06 | 25.9% | 0.0206 | 48.4% | 5.5% | 72 |
| 2021-09-30 | provisional | 5,946 | 45.9 | 0.91 | 16.0% | 0.0047 | 48.5% | 6.9% | 68 |
| 2021-12-31 | provisional | 6,701 | 53.5 | 0.99 | 17.8% | 0.0055 | 51.6% | 10.0% | 97 |
| 2022-03-31 | provisional | 6,720 | 46.3 | 0.90 | 17.0% | 0.0054 | 51.6% | 6.4% | 86 |
| 2022-06-30 | provisional | 6,728 | 38.6 | 0.91 | 15.8% | 0.0049 | 52.3% | 5.8% | 74 |
| 2022-09-30 | provisional | 6,714 | 36.7 | 0.91 | 16.2% | 0.0050 | 52.9% | 6.0% | 83 |
| 2022-12-31 | provisional | 6,913 | 39.8 | 0.95 | 14.5% | 0.0045 | 52.4% | 5.9% | 1205 |
| 2023-03-31 | provisional | 6,846 | 41.2 | 0.91 | 16.0% | 0.0053 | 52.9% | 6.5% | 851 |
| 2023-06-30 | provisional | 6,907 | 44.6 | 0.91 | 18.2% | 0.0063 | 53.3% | 6.6% | 768 |
| 2023-09-30 | provisional | 6,941 | 44.2 | 0.94 | 18.9% | 0.0065 | 53.3% | 6.8% | 691 |
| 2023-12-31 | provisional | 7,171 | 49.2 | 0.95 | 19.0% | 0.0064 | 53.3% | 7.5% | 640 |
| 2024-03-31 | provisional | 7,219 | 52.4 | 0.93 | 20.2% | 0.0067 | 53.1% | 7.1% | 605 |
| 2024-06-30 | provisional | 7,278 | 54.2 | 0.93 | 22.9% | 0.0082 | 53.6% | 6.5% | 561 |
| 2024-09-30 | provisional | 7,341 | 56.5 | 0.92 | 21.5% | 0.0075 | 53.2% | 6.9% | 540 |
| 2024-12-31 | provisional | 7,940 | 59.0 | 0.94 | 23.1% | 0.0082 | 54.1% | 7.2% | 517 |
| 2025-03-31 | provisional | 7,981 | 56.0 | 0.94 | 20.7% | 0.0070 | 53.7% | 6.8% | 462 |
| 2025-06-30 | provisional | 8,033 | 63.5 | 0.97 | 22.7% | 0.0081 | 53.6% | 7.1% | 443 |
| 2025-09-30 | provisional | 8,017 | 69.4 | 0.99 | 24.0% | 0.0089 | 53.1% | 7.7% | 375 |
| 2025-12-31 | provisional | 8,623 | 71.5 | 0.99 | 24.7% | 0.0088 | 54.2% | 6.7% | 391 |
| 2026-03-31 | provisional | 8,736 | 68.0 | 0.97 | 22.3% | 0.0076 | 54.1% | 6.9% | 361 |

Latest (2026-03-31): the ten most-held issuers are 22.3% of reported value (percentile 88% of the usable record), the median filer holds 54.1% of its value in its ten largest positions (96%), reported value is 0.97× the Z.1 market value of nonfinancial corporate equities (77%; 13F value includes financial issuers, foreign issuers and options, so the ratio is a coverage index, not a share).

## 7. The same period across files: a consistency check

A December-31 figure appears first in the 10-Ks (the following quarter's set) and again as the comparative in later 10-Qs. The sums should agree; where they do not, the difference is duplicated or mis-scaled filer values in one file, and the sidecars written by aggregator v3 (`raw/SEC-FSDS/<q>_meta.json`: the values set aside and the five largest filers per key) say which.

| tag | period | file | filers | sum ($bn) | p90 ($m) | aggregator |
|---|---|---|---|---|---|---|
| Assets | 20241231 | 2025q1 | 4566 | 73,602 | 19,374 | v2 |
| Assets | 20241231 | 2025q2 | 4379 | 69,251 | 18,684 | v2 |
| Assets | 20241231 | 2025q3 | 4363 | 69,368 | 18,684 | v2 |
| Assets | 20241231 | 2025q4 | 4358 | 69,206 | 18,661 | v2 |
| Assets | 20241231 | 2026q1 | 3968 | 69,225 | 20,814 | v2 |
| Assets | 20251231 | 2026q1 | 4636 | 78,494 | 20,712 | v2 |
| Assets | 20251231 | 2026q2 | 4447 | 74,048 | 19,389 | v2 |
| Assets | 20251231 | 2026q3 | 4433 | 74,215 | 19,465 | v2 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2025q1 | 3838 | 2,320 | 1,299 | v2 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2026q1 | 3705 | 2,343 | 1,374 | v2 |
| NetCashProvidedByUsedInOperatingActivities | 20251231 | 2026q1 | 3830 | 2,485 | 1,369 | v2 |
| NetIncomeLoss | 20241231 | 2025q1 | 3616 | 1,464 | 718 | v2 |
| NetIncomeLoss | 20241231 | 2026q1 | 3559 | 1,486 | 775 | v2 |
| NetIncomeLoss | 20251231 | 2026q1 | 3675 | 1,625 | 782 | v2 |
| StockholdersEquity | 20241231 | 2025q1 | 4201 | 12,696 | 5,158 | v2 |
| StockholdersEquity | 20241231 | 2025q2 | 4305 | 11,830 | 4,729 | v2 |
| StockholdersEquity | 20241231 | 2025q3 | 4112 | 11,653 | 4,908 | v2 |
| StockholdersEquity | 20241231 | 2025q4 | 4038 | 11,630 | 5,077 | v2 |
| StockholdersEquity | 20241231 | 2026q1 | 4018 | 12,301 | 5,158 | v2 |
| StockholdersEquity | 20241231 | 2026q2 | 3001 | 3,999 | 2,170 | v2 |
| StockholdersEquity | 20241231 | 2026q3 | 2689 | 3,827 | 2,305 | v2 |
| StockholdersEquity | 20251231 | 2026q1 | 4269 | 14,014 | 5,541 | v2 |
| StockholdersEquity | 20251231 | 2026q2 | 4373 | 13,060 | 4,975 | v2 |
| StockholdersEquity | 20251231 | 2026q3 | 4151 | 12,819 | 5,208 | v2 |

## Reading rules

- Ratios and same-period changes are the comparable quantities; levels drift with the filer population and tag usage.
- The FSDS sums are first-reported values from the latest-filed submission per filer and period (aggregator v2) or the first value seen (v1 sets); restatements in later years are not propagated back.
- 13F value includes options (put/call lines, excluded from the issuer concentration), financial and foreign issuers; it is long-only and lagged (filed within 45 days of the quarter end).
- These are the live dials' corporate-sector and positioning reads; they are not learner features (US-only, one era deep).
