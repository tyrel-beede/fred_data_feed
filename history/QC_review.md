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
