# history/ — the long record under the dials

The dials forecast starts in late 2020, which is where the live feed starts. A forecast with no climatology has nothing
to be better than and nothing to relax toward, so this layer anchors it to the long record: 150 years of measured
macro-financial history for 18 economies, a dated crisis chronology, and the best-known attempt to turn that history
into a template (Dalio's), kept apart from the data it rests on.

Three kinds of record live here, and every file says which it is:

| provenance class | meaning | where |
|---|---|---|
| **measured** | compiled from national sources; reconstructed and spliced in early decades; subject to revision between releases | `jst/jst_r6.csv` and the documentation that explains every splice |
| **derived** | arithmetic on measured numbers, computed by a script in `tools/` and reproducible from it | `jst/features.csv`, `jst/coverage.csv`, `bridge/` |
| **stated** | a voice's template, gauges, cases and reads, encoded in our own words with page citations | `dalio/` |

Every dated record carries, or can carry, the three bitemporal fields the dials use: the **event time** (when the thing
happened), the **observed time** (when the record was made — the release date for JST, the publication date for a book),
and the **node** (who recorded it). A revision is a new observed time for the same event time, never an overwrite.

## Layout

```
history/
  README.md                 this file
  sources.json              bibliography; every file names one of these ids
  jst/
    JSTdatasetR6.xlsx       the Release 6 workbook as distributed (CC BY-NC-SA 4.0; see LICENSE-JST.md)
    jst_r6.csv              the sheet as CSV, values untouched (18 countries x 151 years x 59 columns)
    data_dictionary.md|json every variable: definition, units, construction, per-country sources, breaks, caveats
    crises_chronology.csv   88 systemic banking crises, dated, with the narrative and sources for each
    crises_chronology_notes.md   the crisis definition, dating rules, and every deviation from other chronologies
    crises_indicator.csv    the crisisJST / crisisJST_old flags as an event table (cross-checks the chronology)
    returns_documentation.md, returns_variables.json   how the bill, bond, equity and housing returns are built
    house_prices_documentation.md   how each country's house-price index was spliced (and how weak the early parts are)
    coverage.csv            per country x variable: first year, last year, observations, gaps
    units.csv               the nominal-currency unit per country (euro members are in legacy currency)
    features.csv            derived annual features for analog matching (see below)
    field_map.csv           dials field -> long-history proxy, join rule, caveat
    LICENSE-JST.md          the license and required citations
  dalio/
    hcgb/part1..4.md, hcgb_template.json   How Countries Go Broke (2025): concepts, mechanisms, equations, the nine
                            stages with their gauges, the Big Cycle forces, the monetary regimes, cases, Japan numbers,
                            the 3% solution, scenarios, red-dot principles
    hcgb_indicators.csv     his indicator dashboards with the March-2025 readings and thresholds
    hcgb_timeline.csv       the dated events of Part III (US 1865-2025, China, Japan) with the stage he assigns
    bdc/*.md, bdc_template.json   Big Debt Crises (2018): the deflationary and inflationary phase templates, the
                            deleveraging levers, the bubble checklist, the three detailed cases
    bdc_cases.csv, bdc_cases_schema.md   the 48-case compendium as an analog index (one row per case; the book's
                            template-sentence statistics as columns)
    cwo_gauges.json, cwo_charts_catalogue.md   the Changing World Order companion charts: determinants of power,
                            cycle stages, reserve-currency stages, the country power index components
    principles_mechanisms.json, principles_2011.md, principles_2017.md   the mechanism-design content of the two
                            Principles editions (believability, scoring, governance), with a labeled mapping onto an
                            open forecasting ledger
    reads.csv               every dated read by the voice across the books, one ledger (status open until resolved)
  bridge/                   written by tools/bridge_pull.py in Actions: FRED series since 2010 that carry the JST
                            concepts for the US, annual aggregates, and the 2016-2020 overlap check
  tools/
    jst_build.py            workbook -> csv, coverage, crisis flags, units, features
    bridge_pull.py          the FRED bridge (needs FRED_API_KEY; runs in the pull workflow)
    assemble.py             merges the documentation and book encodings into the layout above
```

## The JST dataset

Jordà, Schularick and Taylor's Macrohistory Database, Release 6 (July 2022): 18 advanced economies (AUS BEL CAN CHE
DEU DNK ESP FIN FRA GBR IRL ITA JPN NLD NOR PRT SWE USA), annual, 1870–2020, 59 columns — output, prices, money, rates,
trade, the fiscal accounts, bank credit by borrower, bank balance-sheet ratios, exchange-rate regimes, the crisis
indicator, and total returns on bills, bonds, equities and housing. License CC BY-NC-SA 4.0 with a required citation;
both are in `jst/LICENSE-JST.md`, and this layer shares the files under the same terms for non-commercial use.

Conventions that matter when reading it:

- **Units differ by country.** Nominal local-currency columns (gdp, revenue, expenditure, loans, money, trade, current
  account) are in millions for some countries, billions for others and trillions of yen for Japan; euro members are in
  their legacy currency at the fixed conversion rate (Germany in DM, France in francs, Italy in lire). `units.csv` gives
  the unit per country, inferred from 2019 GDP against World Bank USD GDP and consistent with the documentation. Ratios
  within a country are unit-free; cross-country levels are not.
- **Returns are decimal annual rates** (0.0816 = 8.16%) and, for the US at least, are computed on annual-average index
  levels (Shiller's data), so a calendar-year S&P total return will not match `eq_tr` for the same year (2019: 8.2% on
  averages vs 31.5% December-to-December). Compare like with like.
- **The crisis flag marks the first year of an episode only;** no end years are coded. The chronology document gives the
  narrative and sources for each of the 88 episodes, and lists every change from the previous coding (`crisisJST_old`):
  two added (BEL 1876, JPN 1901), five removed (DEU 1907, DNK 1931, NLD 1893, 1907, 1939), following Baron, Verner and
  Xiong (2021). The dataset also moves the US Great Depression flag from 1929 to 1930 and adds IRL 2008 (Ireland is new
  in R6); those two are not discussed in the chronology document and are noted as open in the verification log.
- **Release 6 extended 2016–2020 from different sources than the history** (OECD, IFS, Fama-French factors, Datastream)
  and silently revised some bond returns back to 1988 for six countries; see `returns_documentation.md`.

Anomalies found while checking the data (not corrected in the files; flagged for the join rules):

| where | reading | expected | note |
|---|---|---|---|
| USA `unemp` 2019 | 2.0 | 3.7 (BLS annual) | 2018 = 3.90 and 2020 = 8.05 are right; 2019 looks like an entry error in the R6 update |
| GBR `stir` 2019–2020 | 0 | ~0.8 / ~0.3 | zero where a value is missing; treat as missing |
| FIN IRL NLD PRT `stir` 2016–2020 | identical | — | the euro-area rate used for all four; fine, but not national |
| JPN `tloans` 2018–2020, `revenue`/`expenditure` 2020, AUS fiscal 2020 | blank | — | gaps in the update window (full list in `coverage.csv`) |
| USA `narrowm` 2020 | 5,206 | M1 was redefined May 2020 | the series is on a pre-redefinition basis; do not splice to M1SL without a ratio |

## Features for analog matching (`jst/features.csv`)

Derived per country-year by `tools/jst_build.py`, all unit-free, each chosen because the literature built on this panel
found it carries information about what follows:

- credit: `loans_gdp`, its 3- and 5-year changes (Schularick–Taylor 2012: the 5-year change in bank loans/GDP is the
  strongest single crisis predictor in the panel), `mort_gdp` and its 5-year change (the Great Mortgaging)
- public debt: `debt_gdp`, its 5-year change, `deficit_gdp`, `interest_burden_proxy` (long rate x debt/GDP),
  `r_minus_g` (long rate minus nominal growth — the sustainability gap Dalio calls the single most important variable)
- rates and prices: `ltrate`, `stir`, `term_spread`, `real_ltrate_expost`, `cpi_infl`, `xr_depreciation`
- money: `money_growth`, `narrowm_growth`, `money_gdp`
- activity: `ngdp_growth`, `rgdp_pc_growth`, `iy` (investment/GDP — the capex cycle) and its 3-year change, `unemp` and
  its 1-year change, `ca_gdp`
- valuation and asset prices: `eq_dp` (the only valuation measure with 150 years of coverage), `real_eq_capgain_3y`,
  `real_hp_growth_3y`
- banks: `lev`, `ltd`, `noncore`
- labels: `crisis_now`, `crisis_next_1_3y` (a systemic crisis within the next three years)

`field_map.csv` says which dials field each proxies, how it joins the live feed, and what it cannot stand in for (there
are no corporate spreads, no breakevens, no volatility and no commodity prices anywhere in the history).

## The bridge to the live feed

JST ends in 2020; the feed holds six years of daily data from late 2020. `tools/bridge_pull.py` pulls the FRED series
that carry the same concepts for the US from 2010, aggregates them to calendar years, and writes a 2016–2020 overlap
check against the JST values. The overlap is the evidence for each join rule (level join for rates and ratios, ratio
splice for indices); nothing is spliced automatically. The pull needs the FRED key and runs in the workflow; its first
run populates `bridge/`, and the join rules in `field_map.csv` get confirmed or corrected from that output.

## Dalio, taken apart

A book like his is three different records with three provenances, and the encoding keeps them apart:

- **His data** (the historical figures in the cases) is a known past with secondary provenance: event time the
  historical date, observed time the publication date, node Dalio/Bridgewater. Where the primary series exist they are
  in `jst/`; his 48 cases (`bdc_cases.csv`) index into them rather than replace them.
- **His reads** are forecasts with issue dates (`dalio/reads.csv`): claim, as-of date, horizon, probability where he
  gives one, and whether the claim is falsifiable as written. Most public claims fail that last test; the share that pass
  is itself a voice metric. Each read stays `open` until a resolution is logged against the criterion he stated.
- **His mechanisms** are hypotheses about which game is being played (`hcgb_template.json`: the nine stages and their
  gauges, the five forces, the monetary regimes; `bdc_template.json`: the phase templates and the bubble checklist;
  `cwo_gauges.json`: the power determinants and cycle stages). They enter the dials only as prospective rules, after the
  backtest of his reads says how much weight the prior has earned.

The two Principles editions are encoded for a different reason: believability weighting, scorecards, the issues-log
incentive and timestamp-locked judgment are the closed-network version of the open scoring ledger the dials are growing
into. `principles_mechanisms.json` carries the mechanisms and a mapping, labeled as ours.

Copyright: the books' text is not reproduced; every file under `dalio/` is our own structured encoding with page
citations, and the PDFs stay out of the repository.

## What this layer is for next

1. **Analog retrieval**: standardize today's feature vector against the panel and return the nearest country-years and
   what followed them — the empirical cone, run unscored beside the hypothesis cone.
2. **Climatology**: the unconditional distribution of each feature by era and regime (`peg_type`), which is what the
   forecast relaxes toward at long lead times.
3. **Voice ledger**: resolve Dalio's dated reads against the criteria recorded here and the data in `jst/` and the feed;
   the same table takes any other voice.

## Verification log

- 2026-11-04: workbook inventoried (2,718 rows, 59 columns, 18 x 151 years); 88 `crisisJST` episodes match the
  chronology document's 88 by country; the seven BVX-prompted recodings match the `crisisJST_old` differences in the
  data; two further differences (USA 1929→1930, IRL 2008) are not explained in the chronology document — open.
  Units inferred and consistent with the documentation's per-country unit notes. US 2020 spot checks: nominal GDP
  20,893.7 bn, federal receipts 3,421 bn and outlays 6,550 bn, M2 17,677 bn, 10-year 0.894%, bill 0.37%, debt/GDP 1.281,
  unemployment 8.05 — all match the official figures; equity capital gain 2019 = 6.1% matches the annual-average basis.
  Anomalies listed above. Documentation and book encodings produced by page-by-page readers and spot-checked against
  the PDFs' text layers (the readers' own cross-checks are described in each file). Second pass the same day: the
  88 chronology episodes equal the 88 indicator flags by country and year exactly; nine page citations re-checked
  against the PDF text (the debt-dynamics identity at HCGB p. 70, "single most important variable" p. 74, the 100%
  long-term government risk reading p. 330, the 65%/80% restructuring-or-monetization probabilities p. 365, the BDC
  bubble checklist p. 20 and bubble statistics p. 19, the CWO determinants p. 11, the chronology's first-year rule
  p. 4) — all present where cited. The reads ledger holds 193 dated claims (116 from the 2025 book, 77 Bridgewater
  Daily Observations from the 2007–2011 case); 86 are marked falsifiable as written, 30 not, 77 (the Daily
  Observations) carry the author's own outcome note instead.
