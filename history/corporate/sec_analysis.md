# The SEC layer over its record

Built 2026-11-07 by `tools/sec_analysis.py` from `sec_fsds_quarterly.csv` (financial statements, 10-K/10-Q filers, 2009–2025) and `sec_13f_quarterly.csv` (institutional holdings). Sums are over every filer reporting the tag; the filer population changed with the XBRL phase-in (large accelerated filers in 2009–2010, all filers from mid-2011) and drifts with listings and tag usage, so the record is read through ratios and same-period comparisons, and levels carry their filer counts. Where the aggregates carry a sector split (aggregator v3) the reads use the **nonfinancial** filers (SIC outside 6000–6799); older aggregates are all filers, and the `sector` column says which each row is.

## 1. Annual cash flows of the December-fiscal-year filers ($bn, 10-K `qtrs=4` rows at December 31)

| year | sector | filers (OCF) | operating cash flow | capex | buybacks | common dividends | net income | D&A |
|---|---|---|---|---|---|---|---|---|
| 2009* | all | 2763 | 1,128 | 259 | 111 | 97 | 176 | 160 |
| 2010* | all | 3857 | 1,294 | 289 | 208 | 117 | 481 | 175 |
| 2011 | all | 3955 | 1,501 | 338 | 309 | 125 | 543 | 213 |
| 2012 | all | 3279 | 1,219 | 377 | 310 | 172 | 524 | 205 |
| 2013 | all | 3305 | 1,449 | 397 | 359 | 164 | 530 | 210 |
| 2014 | all | 2508 | 1,176 | 421 | 421 | 188 | 536 | 255 |
| 2015 | all | 2249 | 1,109 | 376 | 434 | 182 | 350 | 263 |
| 2016 | all | 2735 | 1,092 | 335 | 388 | 191 | 449 | 216 |
| 2017 | all | 3362 | 1,215 | 333 | 382 | 207 | 683 | 255 |
| 2018 | all | 3620 | 1,176 | 320 | 559 | 207 | 686 | 236 |
| 2019 | all | 3774 | 1,796 | 414 | 517 | 260 | 821 | 277 |
| 2020 | all | 4059 | 1,611 | 361 | 373 | 250 | 276 | 318 |
| 2021 | all | 4415 | 2,145 | 386 | 621 | 269 | 1,200 | 345 |
| 2022 | all | 4335 | 2,406 | 495 | 745 | 300 | 867 | 331 |
| 2023 | all | 3821 | 2,350 | 615 | 654 | 303 | 1,125 | 442 |
| 2024 | all | 3863 | 2,104 | 651 | 739 | 296 | 1,051 | 467 |
| 2025 | all | 3857 | 2,638 | 777 | 831 | 310 | 1,314 | 477 |

\* phase-in years (large accelerated filers only). Dividends are the `PaymentsOfDividendsCommonStock` tag (831 filers in 2025); the broader `PaymentsOfDividends` tag is carried in the JSON and not added to it, since some filers report both.

## 2. The ratios, and where the latest year sits

Aggregate ratios (sum over sum) per year; the percentile is the share of years in the record at or below the latest reading (100% = the highest in the record).

| ratio | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | latest percentile |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| capital expenditures / operating cash flow | 0.23 | 0.22 | 0.22 | 0.31 | 0.27 | 0.36 | 0.34 | 0.31 | 0.27 | 0.27 | 0.23 | 0.22 | 0.18 | 0.21 | 0.26 | 0.31 | 0.29 | 71% |
| buybacks / operating cash flow | 0.10 | 0.16 | 0.21 | 0.25 | 0.25 | 0.36 | 0.39 | 0.36 | 0.31 | 0.48 | 0.29 | 0.23 | 0.29 | 0.31 | 0.28 | 0.35 | 0.31 | 71% |
| common dividends / operating cash flow | 0.09 | 0.09 | 0.08 | 0.14 | 0.11 | 0.16 | 0.16 | 0.17 | 0.17 | 0.18 | 0.14 | 0.16 | 0.13 | 0.12 | 0.13 | 0.14 | 0.12 | 29% |
| buybacks + common dividends / operating cash flow | 0.18 | 0.25 | 0.29 | 0.39 | 0.36 | 0.52 | 0.56 | 0.53 | 0.49 | 0.65 | 0.43 | 0.39 | 0.42 | 0.43 | 0.41 | 0.49 | 0.43 | 59% |
| buybacks + common dividends / net income | 1.18 | 0.68 | 0.80 | 0.92 | 0.99 | 1.14 | 1.76 | 1.29 | 0.86 | 1.12 | 0.95 | 2.26 | 0.74 | 1.21 | 0.85 | 0.99 | 0.87 | 35% |
| capital expenditures / depreciation and amortization | 1.62 | 1.65 | 1.59 | 1.84 | 1.89 | 1.65 | 1.43 | 1.55 | 1.30 | 1.36 | 1.49 | 1.14 | 1.12 | 1.49 | 1.39 | 1.39 | 1.63 | 76% |
| cash and equivalents / assets (Dec 31) | 0.07 | 0.04 | 0.05 | 0.05 | 0.05 | 0.05 | 0.04 | 0.05 | 0.06 | 0.04 | 0.05 | 0.06 | 0.06 | 0.05 | 0.05 | 0.04 | 0.03 | 6% |
| liabilities / assets (Dec 31) | 0.89 | 0.86 | 0.75 | 0.97 | 0.86 | 0.90 | 0.87 | 0.86 | 0.92 | 0.91 | 0.71 | 1.02 | 0.88 | 0.93 | 0.92 | 0.79 | 0.72 | 12% |
| inventories / assets (Dec 31) | 0.02 | 0.01 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 12% |
| long-term debt (noncurrent) / stockholders' equity (Dec 31) | 0.97 | 0.31 | 0.37 | 0.29 | 0.32 | 0.35 | 0.52 | 0.48 | 0.61 | 0.43 | 0.46 | 0.66 | 0.49 | 0.52 | 0.50 | 0.43 | 0.28 | 6% |

Balance-sheet ratios use the December-31 levels (`qtrs=0`); long-term debt is the `LongTermDebtNoncurrent` tag, which a minority of filers use, so that ratio is the thinnest of the set.

## 3. December-31 balance sheets ($bn)

The table takes, for each tag and date, the quarterly file with the most filers reporting it; the last two columns give the assets and equity sums in the first file that carried the date (the 10-Ks) and the ratio of the chosen sum to it. A ratio far from one means the chosen file (10-Q comparatives) carries inflated or duplicated values for that date — see section 7.

| year | filers (assets) | assets | liabilities | equity | cash | inventories | long-term debt (noncurrent; filers) | assets, 10-K file (ratio) | equity, 10-K file (ratio) |
|---|---|---|---|---|---|---|---|---|---|
| 2009 | 1090 | 18,193 | 16,165 | 1,173 | 1,267 | 353 | 1,133 (458) | 18,193 (1.00) | 1,173 (1.00) |
| 2010 | 5433 | 34,050 | 29,299 | 4,992 | 1,296 | 464 | 1,554 (1253) | 20,186 (1.69) | 4,293 (1.16) |
| 2011 | 6126 | 31,790 | 23,820 | 4,680 | 1,462 | 605 | 1,735 (1389) | 28,933 (1.10) | 4,870 (0.96) |
| 2012 | 6106 | 28,700 | 27,797 | 5,898 | 1,331 | 561 | 1,732 (1292) | 21,969 (1.31) | 5,513 (1.07) |
| 2013 | 5781 | 28,786 | 24,641 | 5,695 | 1,488 | 683 | 1,804 (1345) | 22,260 (1.29) | 5,625 (1.01) |
| 2014 | 5618 | 28,989 | 26,030 | 5,611 | 1,414 | 698 | 1,984 (1389) | 22,724 (1.28) | 5,661 (0.99) |
| 2015 | 5289 | 29,625 | 25,890 | 4,639 | 1,332 | 643 | 2,427 (1373) | 26,837 (1.10) | 5,365 (0.86) |
| 2016 | 5067 | 29,016 | 24,857 | 4,730 | 1,439 | 577 | 2,260 (1334) | 26,676 (1.09) | 3,405 (1.39) |
| 2017 | 5180 | 31,226 | 28,822 | 3,837 | 1,845 | 516 | 2,353 (1273) | 26,964 (1.16) | 4,894 (0.78) |
| 2018 | 5056 | 30,196 | 27,344 | 5,448 | 1,310 | 599 | 2,339 (1252) | 24,168 (1.25) | 5,486 (0.99) |
| 2019 | 4594 | 34,011 | 24,060 | 5,457 | 1,541 | 684 | 2,512 (1221) | 28,725 (1.18) | 5,165 (1.06) |
| 2020 | 5345 | 28,632 | 29,327 | 5,915 | 1,759 | 782 | 3,877 (1276) | 26,340 (1.09) | 6,015 (0.98) |
| 2021 | 5894 | 31,798 | 28,078 | 6,382 | 2,007 | 760 | 3,152 (1365) | 28,475 (1.12) | 6,688 (0.95) |
| 2022 | 5553 | 31,430 | 29,351 | 5,965 | 1,626 | 865 | 3,119 (1317) | 35,491 (0.89) | 6,662 (0.90) |
| 2023 | 5350 | 34,320 | 31,562 | 6,414 | 1,823 | 882 | 3,203 (1203) | 31,133 (1.10) | 8,034 (0.80) |
| 2024 | 4791 | 41,793 | 33,074 | 7,875 | 1,626 | 1,015 | 3,405 (1208) | 35,762 (1.17) | 8,396 (0.94) |
| 2025 | 4810 | 74,172 | 53,761 | 13,087 | 2,138 | 1,148 | 3,629 (1193) | 35,505 (2.09) | 8,808 (1.49) |

## 4. The timely read: latest year-to-date flows against a year earlier ($bn)

**Q1 (three months to March 31), 2026 vs 2025** (all filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 407 (4327) | 134 (4266) | 203.9% |
| capital expenditures | 249 (2325) | 190 (2363) | 31.2% |
| buybacks | 263 (1402) | 234 (1364) | 12.5% |
| common dividends | 97 (798) | 89 (820) | 9.0% |
| net income | 516 (4577) | 330 (4452) | 56.5% |

**H1 (six months to June 30), 2026 vs 2025** (all filers)

| flow | 2026 (filers) | 2025 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,224 (4342) | 697 (4292) | 75.7% |
| capital expenditures | 498 (2399) | 360 (2445) | 38.2% |
| buybacks | 496 (1559) | 423 (1530) | 17.5% |
| common dividends | 172 (799) | 161 (833) | 6.9% |
| net income | 986 (4171) | 644 (4052) | 53.1% |

**nine months to September 30, 2025 vs 2024** (all filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 1,514 (4298) | 1,370 (4366) | 10.6% |
| capital expenditures | 569 (2477) | 480 (2623) | 18.5% |
| buybacks | 626 (1563) | 555 (1542) | 12.8% |
| common dividends | 240 (832) | 227 (847) | 5.6% |
| net income | 1,219 (4073) | 781 (4104) | 56.0% |

**fiscal year to December 31, 2025 vs 2024** (all filers)

| flow | 2025 (filers) | 2024 (filers) | change |
|---|---|---|---|
| operating cash flow | 2,638 (3857) | 2,104 (3863) | 25.4% |
| capital expenditures | 777 (2349) | 651 (2460) | 19.3% |
| buybacks | 831 (1692) | 739 (1679) | 12.5% |
| common dividends | 310 (831) | 296 (856) | 4.7% |
| net income | 1,314 (3715) | 1,051 (3646) | 25.1% |

10-Q cash-flow statements are year-to-date, so the June and September rows are cumulative; the comparison is same period, same statement, with the filer counts beside each sum (a change in the count is part of the change in the sum).

## 5. Calibration against the compiled national series

The financial-statement sums are the listed, XBRL-filing part of the sector; the Z.1 and NIPA series are the whole nonfinancial corporate sector, compiled. Coverage is the FSDS sum over the compiled flow; the growth correlation is between year-on-year log changes of the two.

| FSDS series | compiled series | years | coverage, first → latest | growth corr. (all years) | growth corr. after the phase-in |
|---|---|---|---|---|---|
| capex | Z.1 nonfinancial corporate capital expenditures | 2009–2025 | 0.24 → 0.25 | 0.49 (n=16) | 0.50 (n=14) |
| dividends_common | Z.1 nonfinancial corporate net dividends paid | 2009–2025 | 0.26 → 0.22 | 0.37 (n=16) | 0.40 (n=14) |
| net_income | NIPA nonfinancial corporate profits after tax | 2009–2025 | 0.29 → 0.59 | 0.47 (n=16) | 0.35 (n=14) |

Coverage above one for capital expenditures is expected: the Z.1 series is net of sales of existing assets and excludes some intangibles, and the 10-K population includes foreign private issuers and financial companies filing 10-Ks. The ratio's stability year to year, and the growth correlation, are the measures of agreement; the level is not.

## 6. Institutional holdings (Form 13F)

0 periods reduced by the current aggregator (per-filer units, the set's own report period), 14 dollar-era periods still carried from the first aggregator (provisional: late and amended filings not yet separated), 39 thousands-era periods awaiting re-reduction (`corporate_pull.py --only 13f --all --redo` from a desktop): 2013q2_form13f, 2013q3_form13f, 2013q4_form13f … 2022q4_form13f.

| holdings date | status | filers | total value ($tn) | / Z.1 NFC equities | top-10 issuer share | HHI (issuers) | median filer top-10 share | put/call share | filers rescaled |
|---|---|---|---|---|---|---|---|---|---|
| 2022-12-31 | provisional | 7,504 | 35.5 | 0.85 | 14.2% | 0.0044 | 52.4% | 5.3% |  |
| 2023-03-31 | provisional | 7,399 | 44.6 | 0.98 | 15.7% | 0.0052 | 54.3% | 5.8% |  |
| 2023-06-30 | provisional | 7,406 | 47.8 | 0.98 | 18.5% | 0.0065 | 54.2% | 6.4% |  |
| 2023-09-30 | provisional | 7,500 | 47.4 | 1.01 | 19.0% | 0.0065 | 53.8% | 6.8% |  |
| 2023-12-31 | provisional | 7,743 | 46.5 | 0.90 | 19.0% | 0.0065 | 52.9% | 7.4% |  |
| 2024-03-31 | provisional | 8,126 | 58.5 | 1.03 | 20.2% | 0.0068 | 53.6% | 7.1% |  |
| 2024-06-30 | provisional | 8,119 | 58.7 | 1.01 | 22.1% | 0.0077 | 54.1% | 5.9% |  |
| 2024-09-30 | provisional | 8,116 | 62.5 | 1.02 | 20.8% | 0.0071 | 53.8% | 6.3% |  |
| 2024-12-31 | provisional | 8,713 | 68.6 | 1.09 | 21.9% | 0.0076 | 54.4% | 6.2% |  |
| 2025-03-31 | provisional | 8,892 | 62.0 | 1.04 | 20.7% | 0.0071 | 54.7% | 6.4% |  |
| 2025-06-30 | provisional | 8,805 | 63.4 | 0.97 | 22.5% | 0.0080 | 54.2% | 7.3% |  |
| 2025-09-30 | provisional | 8,562 | 70.2 | 1.00 | 24.0% | 0.0088 | 53.4% | 7.5% |  |
| 2025-12-31 | provisional | 9,361 | 71.1 | 0.99 | 24.3% | 0.0086 | 54.3% | 8.0% |  |
| 2026-03-31 | provisional | 9,711 | 81.5 | 1.16 | 23.1% | 0.0081 | 54.1% | 8.1% |  |

Latest (2026-03-31): the ten most-held issuers are 23.1% of reported value (percentile 86% of the usable record), the median filer holds 54.1% of its value in its ten largest positions (57%), reported value is 1.16× the Z.1 market value of nonfinancial corporate equities (100%; 13F value includes financial issuers, foreign issuers and options, so the ratio is a coverage index, not a share).

## 7. The same period across files: a consistency check

A December-31 figure appears first in the 10-Ks (the following quarter's set) and again as the comparative in later 10-Qs. The sums should agree; where they do not, the difference is duplicated or mis-scaled filer values in one file, and the sidecars written by aggregator v3 (`raw/SEC-FSDS/<q>_meta.json`: the values set aside and the five largest filers per key) say which.

| tag | period | file | filers | sum ($bn) | p90 ($m) | aggregator |
|---|---|---|---|---|---|---|
| Assets | 20241231 | 2025q1 | 4601 | 35,762 | 11,336 | v1 |
| Assets | 20241231 | 2025q2 | 4791 | 41,793 | 12,768 | v1 |
| Assets | 20241231 | 2025q3 | 4503 | 35,186 | 12,204 | v1 |
| Assets | 20241231 | 2025q4 | 4472 | 69,362 | 18,010 | v1 |
| Assets | 20241231 | 2026q1 | 4054 | 30,233 | 12,947 | v1 |
| Assets | 20251231 | 2026q1 | 4676 | 35,505 | 11,770 | v1 |
| Assets | 20251231 | 2026q2 | 4810 | 74,172 | 17,186 | v1 |
| Assets | 20251231 | 2026q3 | 4536 | 74,250 | 18,711 | v1 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2025q1 | 3863 | 2,104 | 1,158 | v1 |
| NetCashProvidedByUsedInOperatingActivities | 20241231 | 2026q1 | 3735 | 2,262 | 1,263 | v1 |
| NetCashProvidedByUsedInOperatingActivities | 20251231 | 2026q1 | 3857 | 2,638 | 1,251 | v1 |
| NetIncomeLoss | 20241231 | 2025q1 | 3646 | 1,051 | 576 | v1 |
| NetIncomeLoss | 20241231 | 2026q1 | 3603 | 1,311 | 646 | v1 |
| NetIncomeLoss | 20251231 | 2026q1 | 3715 | 1,314 | 640 | v1 |
| StockholdersEquity | 20241231 | 2025q1 | 4237 | 8,396 | 3,382 | v1 |
| StockholdersEquity | 20241231 | 2025q2 | 4712 | 7,875 | 2,756 | v1 |
| StockholdersEquity | 20241231 | 2025q3 | 4264 | 7,480 | 3,119 | v1 |
| StockholdersEquity | 20241231 | 2025q4 | 4152 | 11,649 | 4,906 | v1 |
| StockholdersEquity | 20241231 | 2026q1 | 4111 | 8,485 | 3,380 | v1 |
| StockholdersEquity | 20241231 | 2026q2 | 3477 | 4,006 | 1,842 | v1 |
| StockholdersEquity | 20241231 | 2026q3 | 2932 | 3,821 | 2,103 | v1 |
| StockholdersEquity | 20251231 | 2026q1 | 4306 | 8,808 | 3,634 | v1 |
| StockholdersEquity | 20251231 | 2026q2 | 4742 | 13,087 | 4,473 | v1 |
| StockholdersEquity | 20251231 | 2026q3 | 4266 | 12,835 | 5,032 | v1 |

## Reading rules

- Ratios and same-period changes are the comparable quantities; levels drift with the filer population and tag usage.
- The FSDS sums are first-reported values from the latest-filed submission per filer and period (aggregator v2) or the first value seen (v1 sets); restatements in later years are not propagated back.
- 13F value includes options (put/call lines, excluded from the issuer concentration), financial and foreign issuers; it is long-only and lagged (filed within 45 days of the quarter end).
- These are the live dials' corporate-sector and positioning reads; they are not learner features (US-only, one era deep).
