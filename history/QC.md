# history/ — quality control

Mechanical checks run by `tools/qc.py`: **24 of 24 pass**. Re-run after any change.

| check | result | evidence |
|---|---|---|
| inventory: every expected file exists | PASS | 48 files |
| parse: every JSON parses and every CSV is rectangular | PASS | ok |
| jst_r6: 2,718 rows, 18 countries x 1870-2020, no duplicate country-year | PASS | rows 2718, countries 18 |
| jst_r6: 59 columns | PASS | 59 columns |
| data dictionary: every column has an entry | PASS | 75 entries |
| data dictionary: terms of use and citation transcribed | PASS |  |
| crises: chronology episodes equal crisisJST flags | PASS | chronology 88, flags 88, diff [] |
| crises: the seven BVX recodings appear in crisisJST_old vs crisisJST | PASS | added [('BEL', 1876), ('IRL', 2008), ('JPN', 1901), ('USA', 1930)], removed [('DEU', 1907), ('DNK', 1931), ('NLD', 1893), ('NLD', 1907), ('NLD', 1939), ('USA', 1929)] |
| overrides: every row points at a real cell, quotes the JST value correctly, and carries provenance | PASS | 4 rows |
| features: 44 country-years recomputed independently (loans/GDP, 5y change, r-g, unemp, crisis label) | PASS | all match |
| features: overrides applied and flagged | PASS |  |
| field map: every variable-looking token names a real column or feature | PASS | 23 rows |
| sources.json: every local_files path exists | PASS | 16 sources |
| HCGB: nine numbered stages with names and gauges | PASS | 1 The Private Sector and Government Get De; 2 The Private Sector Suffers a Debt Crisis; 3 The Central Government Experiences a Deb; 4 The Selling of the Government's Debt Lea; 5 When There Is a Debt Crisis and Interest;  |
| HCGB: five forces of the Big Cycle recorded | PASS | ['1. The debt/credit/money/economic cycle (p. 165)', '2. The internal order and disorder cycle (p. 165)', '3. The external geopolitical order and disorder cycle (i.e., the changing world order) (p. 16 |
| reads ledger: every row has a claim and an as-of date; falsifiable flag well-formed; pages in range | PASS | 193 reads; bad [] [] |
| BDC compendium: 48 unique cases with ordered years and 3-letter codes | PASS | 48 cases |
| BDC template: 7 deflationary and 5-6 inflationary phases, bubble checklist of 7 | PASS | defl 7, infl 6, checklist 7 |
| CWO: 8 measures of power and 18 determinants recorded | PASS | measures 8, determinants 18 |
| Principles: mechanisms and ledger mapping present from both editions | PASS | 267 mechanisms, 61 mappings |
| units: 2019 GDP in USD within 10% of World Bank for all 18 countries | PASS | ok |
| workflow: bridge step wired and the bridge script exists | PASS |  |
| license: CC BY-NC-SA 4.0 and both required citations stated | PASS |  |
| README: documents overrides, provenance classes, bitemporal fields | PASS |  |

## Content review

The content review (encodings against the source documents, design intent against the layout) is recorded below by whoever ran it, with date, scope and findings. It is not mechanical and is not overwritten by this script.

The content review (encodings against the source documents, design intent against the layout) is recorded below by whoever ran it, with date, scope and findings. It is not mechanical and is not overwritten by this script.

The content review (encodings against the source documents, design intent against the layout) is recorded below by whoever ran it, with date, scope and findings. It is not mechanical and is not overwritten by this script.

The content review (encodings against the source documents, design intent against the layout) is recorded below by whoever ran it, with date, scope and findings. It is not mechanical and is not overwritten by this script.
