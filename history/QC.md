# history/ — quality control

Mechanical checks run by `tools/qc.py`: **25 of 25 pass**. Re-run after any change.

| check | result | evidence |
|---|---|---|
| inventory: every expected file exists | PASS | 101 files |
| parse: every JSON parses and every CSV is rectangular | PASS | ok |
| jst_r6: 2,718 rows, 18 countries x 1870-2020, no duplicate country-year | PASS | rows 2718, countries 18 |
| jst_r6: 59 columns | PASS | 59 columns |
| data dictionary: every column has an entry | PASS | 75 entries |
| data dictionary: terms of use and citation transcribed | PASS |  |
| crises: chronology episodes equal crisisJST flags | PASS | chronology 88, flags 88, diff [] |
| crises: the seven BVX recodings appear in crisisJST_old vs crisisJST | PASS | added [('BEL', 1876), ('IRL', 2008), ('JPN', 1901), ('USA', 1930)], removed [('DEU', 1907), ('DNK', 1931), ('NLD', 1893), ('NLD', 1907), ('NLD', 1939), ('USA', 1929)] |
| overrides: every row points at a real cell, quotes the JST value correctly, and carries provenance | PASS | 4 rows |
| features: 44 country-years recomputed independently (loans/GDP, 5y change, r-g, unemp, crisis label) | PASS | all match |
| features: overrides applied and flagged, with propagation to dependent rows | PASS |  |
| field map: every variable-looking token names a real column or feature | PASS | 23 rows |
| sources.json: every local_files path exists | PASS | 30 sources |
| HCGB: nine numbered stages with names and gauges | PASS | 1 The Private Sector and Government Get De; 2 The Private Sector Suffers a Debt Crisis; 3 The Central Government Experiences a Deb; 4 The Selling of the Government's Debt Lea; 5 When There Is a Debt Crisis and Interest;  |
| HCGB: five forces of the Big Cycle recorded | PASS | ['1. The debt/credit/money/economic cycle (p. 165)', '2. The internal order and disorder cycle (p. 165)', '3. The external geopolitical order and disorder cycle (i.e., the changing world order) (p. 16 |
| reads ledger: every row has a claim and an as-of date; falsifiable flag well-formed; pages in each source's range; page convention and grade present | PASS | 193 reads; bad [] [] [] |
| BDC compendium: 48 unique cases with ordered years and 3-letter codes | PASS | 48 cases |
| BDC template: 7 deflationary and 5-6 inflationary phases, bubble checklist of 7 | PASS | defl 7, infl 6, checklist 7 |
| CWO: 8 measures of power and 18 determinants recorded | PASS | measures 8, determinants 18 |
| Principles: mechanisms and ledger mapping present from both editions | PASS | 267 mechanisms, 61 mappings |
| units: 2019 GDP in USD within 10% of World Bank for all 18 countries | PASS | ok |
| workflow: bridge step wired and the bridge script exists | PASS |  |
| license: CC BY-NC-SA 4.0 and both required citations stated | PASS |  |
| README: documents overrides, provenance classes, bitemporal fields | PASS |  |
| README: every quoted AUC-like number (0.5x-0.9x) appears in a result file | PASS | 26 quoted numbers all found |

## Content review

The content review (encodings against the source documents, design intent against the layout) is kept by hand in `QC_review.md` and included here verbatim; this script never edits it.

### Content review — 2026-11-04

**Scope.** An independent reviewer that had not seen the work checked the layer against the source PDFs and the design
intent: every checkable claim in the README; 12 data-dictionary variables (definition, units, a per-country source and
a caveat each) against the R6 documentation at the cited pages; 11 crisis episodes against the chronology document; 12
reads against the cited book pages (claim, as-of date, falsifiability, quote length); 5 compendium cases number by
number; 3 of the nine stages and 6 indicator rows against the 2025 book; a scan of every `dalio/*.md` for verbatim
passages; the tools' code; the concept against the layout; and the license and citations. A scratch rebuild from the
workbook reproduced `jst_r6.csv`, `coverage.csv`, `crises_indicator.csv`, `units.csv` and `features.csv` byte for
byte, `qc.py` passed on the copy, and `analogs.py --iso USA --year 2007` reproduced the committed output exactly.

**Verified clean.** All 12 dictionary variables; all 11 chronology episodes, including the cross-database notes; all
12 reads on their pages with correct as-of dates and no quote over 25 words; all 5 compendium rows; the sampled stages
and indicators; the license text and both required citations; no PDF under `history/`; only bibliographies, numeric
tables and tables of contents match the sources at length.

**Findings and what was done** (0 blockers, 7 should-fix, 15 minor, 4 notes):

| # | finding | fix applied |
|---|---|---|
| S1 | The backtest excluded only the query's own country, so other countries in the same global episode leaked their outcomes into the analogs; the published AUC 0.66 overstated skill by about half. | `analog_backtest.py` now runs three exclusion rules (same-country, block-year, walk-forward) for every feature set and reports all of them; the README headline is the walk-forward result (crisis AUC 0.59, ρ ≈ +0.2). |
| S2 | US `narrowm` is the monetary base, not M1 (documentation pp. 193–194); the README anomaly row, the override note, the field map and the bridge mapping to M1SL were wrong. | All four corrected; the bridge maps `narrowm` to BOGMBASE. |
| S3 | The UK short-rate override misattributed the source series (the documentation says MeasuringWorth "Ordinary Funds", not the OECD bill series). | Reason rewritten to what the documentation says; the proxy replacement and its flag kept. |
| S4 | `reads.csv` mixed page conventions (book pages for the 2025 book, PDF pages for the Daily Observations) with no column saying so. | Daily-Observation rows converted to printed Part 2 pages; a `page_convention` column added; QC checks each source's range. |
| S5 | The falsifiability flag was lenient (74% of claims passed; conditional and "nearing" claims counted as falsifiable). | A mechanical `falsifiability_grade` added (strict / loose / conditional / no / author-scored); the README's voice metric is the strict share, 7%. |
| S6 | The seven-item bubble checklist was reproduced verbatim (~100 words). | Paraphrased in both files; page cite kept. |
| S7 | Override flags did not propagate to dependent rows (USA 2020 `d1_unemp` used the overridden 2019 value, unflagged). | Flags now propagate as `variable@year` to every later row within the five-year lookback. |
| M1 | `qc.py` re-appended the content-review boilerplate on every run. | QC.md is now written whole from the mechanical results plus this file. |
| M2 | "Ireland is new in R6" was unsupported. | Reworded: IRL 2008 is in `crisisJST` with no old flag for Ireland; not listed in the document's Section 3. |
| M3 | The explanation of the credit group's weak score (levels diluting the change) was asserted, not measured. | The 5-year loan/GDP change is now run alone as a feature set (AUC 0.51 walk-forward) and the README reports the measurement. |
| M4 | Maddison GDP per capita labelled "2011 USD"; the documentation says 1990 international dollars (Maddison Project 2013). | Corrected in the field map and the bridge. |
| M5 | `sources.json` pointed to the README for the terms of use. | Points to `LICENSE-JST.md` and the dictionary. |
| M6 | README layout tree omitted several files. | Completed. |
| M7 | "Sources:" prefixes and duplicates in the chronology CSV; stale filename and count in the notes. | Cleaned; the note now says the sheet carries 90 old flags because Ireland has none. |
| M8 | Compendium notes referred to the readers' intermediate files. | Point at `bdc_cases.csv` / `bdc_cases_schema.md`. |
| M9 | 2018–2019 crisis labels were partial windows coded 0. | Censored unless all three forward years exist (also in the analog outcomes). |
| M10 | `--regime FLOAT` dropped the US's entire post-1940 record because the anchor country is coded BASE. | Regimes are now `nonpeg` (FLOAT or BASE), `peg`, `any`; the earlier FLOAT-only run removed. |
| M11 | Stale "pp. 1–100" scoping in the merged dictionary; three entries lacked cross-references. | Release block updated; `see_also` added for the returns, crisis and peg entries. |
| M12 | The RORE citation differs from the documentation's pre-publication wording. | Published form kept, documentation's wording noted beside it. |
| M13 | The ledger mapping was not labelled as the repository's own. | `_about` added to `principles_mechanisms.json`. |
| M14 | Stage-4 sub-sequence order (reserves / currency) swapped in one mechanism line. | Corrected. |
| M15 | Nothing at the repository root said it carries non-commercial, share-alike data. | One line and a link added to the root README. |
| N1–N4 | Bitemporal fields are explicit only on overrides and reads (file-level elsewhere); no per-variable counted/measured/coded attribute yet; nothing enters `dials/` yet, as intended; rebuild reproducibility confirmed. | N1 and N2 are queued: an `observed_time`/`node` column on the chronology and indicator tables when a second release or voice arrives, and a `kind` field in the dictionary. |

**Verdict (reviewer's, before fixes):** the concept is implemented as intended and the encodings are faithful at every
point checked; the shortfalls were at the method's edges — backtest leakage, two wrong provenance statements, lenient
falsifiability, mixed page conventions, one verbatim list. All seven should-fixes and the fifteen minors above are
applied; the mechanical checks were re-run afterwards (see the table above).
