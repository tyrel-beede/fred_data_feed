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
  QC.md, QC_review.md       mechanical checks (tools/qc.py) and the hand-kept content review
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
    overrides.csv           corrections with their own provenance; JST values are never edited
    features.csv            derived annual features for analog matching (see below), override-flagged per row
    features2.csv           the base 20 plus the subnet-at-t, rank and flux families (tools/features2.py)
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
  analogs/                  analog queries (validation cases, the live US queries with per-value provenance) and
                            backtest.md / backtest.json
  tools/
    jst_build.py            workbook -> csv, coverage, crisis flags, units, features
    jstlib.py               shared loader (sheet + overrides + features)
    bridge_pull.py          the FRED bridge (needs FRED_API_KEY; runs in the pull workflow)
    assemble.py             merges the documentation and book encodings into the layout above
    analogs.py              the empirical cone: nearest country-years and what followed, beside climatology
    analog_backtest.py      skill of the cone by feature group under three exclusion rules
    features2.py, wf.py, analog_test2.py, label_test.py, lag_test.py   test 2 (subnet, rank, flux; measured targets;
                            horizons), the tests of the crisis label itself, and the lead-lag measurements
    qc.py                   mechanical checks -> QC.md
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
  Xiong (2021). The dataset also moves the US Great Depression flag from 1929 to 1930 and carries IRL 2008 in
  `crisisJST` with no `crisisJST_old` flag at all for Ireland; neither change is listed in the document's Section 3,
  and both are noted as open in the verification log.
- **Release 6 extended 2016–2020 from different sources than the history** (OECD, IFS, Fama-French factors, Datastream)
  and silently revised some bond returns back to 1988 for six countries; see `returns_documentation.md`.

Anomalies found while checking the data (not corrected in the files; flagged for the join rules):

| where | reading | expected | note |
|---|---|---|---|
| USA `unemp` 2019 | 2.0 | 3.7 (BLS annual) | 2018 = 3.90 and 2020 = 8.05 are right; 2019 looks like an entry error in the R6 update |
| GBR `stir` 2019–2020 | 0 | ~0.8 / ~0.3 | zero where a value is missing; treat as missing |
| FIN IRL NLD PRT `stir` 2016–2020 | identical | — | the euro-area rate used for all four; fine, but not national |
| JPN `tloans` 2018–2020, `revenue`/`expenditure` 2020, AUS fiscal 2020 | blank | — | gaps in the update window (full list in `coverage.csv`) |
| USA `narrowm` | 5,206 (2020) | — | not an anomaly: US narrow money is the monetary base (documentation pp. 193–194), so the bridge uses BOGMBASE, never M1 |

## Overrides (`jst/overrides.csv`)

A JST value is never edited. Where a value is wrong or is a placeholder, `overrides.csv` records the cell, the JST
value, the replacement, the source and its URL, the observed time and the node that made the correction, and the
reason. `jst_build.py` applies the `replace` rows in memory when it computes `features.csv`, and the affected rows
carry the overridden variable names in an `overrides` column, so every derived number can be traced to either the
sheet or a named correction. Rows with action `note` change nothing and record a basis caveat. Current overrides:
US unemployment 2019 (2.0 → 3.7, BLS), UK short rate 2019 and 2020 (0 → 0.81 and 0.30, the OECD 3-month interbank
rate as the nearest continuing instrument, flagged as a proxy), and a basis note on US narrow money at the May-2020
M1 redefinition.

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
  gives one, the reader's falsifiability flag, and a mechanical `falsifiability_grade` — *strict* needs a dated horizon
  and a criterion with a quantity or threshold, *conditional* marks claims that hang on an antecedent, *loose* is the
  reader's "yes" without both, *no* is the reader's "no", *author-scored* are the Daily Observations the book itself
  grades. Of the 116 book claims, 8 are strict, 70 loose, 8 conditional, 30 not falsifiable: the strict share, 7%, is
  the voice metric, and it says what one expects of a public voice. Each read stays `open` until a resolution is
  logged against the criterion he stated. Pages follow each source's convention, stated per row.
- **His mechanisms** are hypotheses about which game is being played (`hcgb_template.json`: the nine stages and their
  gauges, the five forces, the monetary regimes; `bdc_template.json`: the phase templates and the bubble checklist;
  `cwo_gauges.json`: the power determinants and cycle stages). They enter the dials only as prospective rules, after the
  backtest of his reads says how much weight the prior has earned.

The two Principles editions are encoded for a different reason: believability weighting, scorecards, the issues-log
incentive and timestamp-locked judgment are the closed-network version of the open scoring ledger the dials are growing
into. `principles_mechanisms.json` carries the mechanisms and a mapping, labeled as ours.

Copyright: the books' text is not reproduced; every file under `dalio/` is our own structured encoding with page
citations, and the PDFs stay out of the repository.

## Analog retrieval (`tools/analogs.py`, `analogs/`)

The first use of the layer: standardize a state vector (robust z-scores across the panel), find the nearest
country-years (one per country within ±5 years, the query's own episode excluded), and report what followed them —
crisis within 1–3 years, real GDP per capita, real equity and house-price returns, long-rate and unemployment changes
— as quantiles beside the same outcomes over the whole panel, which is the climatology and the no-skill reference.
Nothing in it assumes a branch: the analogs are paths that happened.

`tools/analog_backtest.py` asks whether the cone carries information, over the panel from 1880 (k=15), per feature
group and under three exclusion rules, because the rule decides how much apparent skill is real (`analogs/backtest.md`).
Excluding only the query's own episode leaves other countries in the same global episode in the pool — a 2007 query
"predicted" by other countries' 2007 — and that leaky setting reads crisis AUC 0.66, top decile 25% against a 10% base,
ρ +0.36 to +0.42 for the three-year outcomes. Remove the leakage and the skill is modest: block-year (every country
within ±5 years excluded) gives AUC 0.54, top decile 15% vs 10%, ρ +0.20 / +0.30 / +0.25 for three-year real equity,
real GDP per capita and the long-rate change; walk-forward (only candidates whose outcome window closed before the query
year — the forecast setting, and the headline) gives AUC 0.59, top decile 13% vs 10%, ρ +0.20 / +0.18 / +0.14, with
analog bands narrower than climatology's (31 vs 47 pp for equity) but covering only 29–37% of outcomes — the past's
dispersion under-covers what followed, which is a finding about non-stationarity, not a tuning problem. No single group
survives on its own in the forecast setting (crisis AUC 0.45–0.58; valuation is the best single group at 0.58); the
five-year change in loans/GDP alone, the literature's credit-boom signal, scores 0.51 as a nearest-neighbour feature
(it is a logit result there, not a distance result here). The honest summary: the state vector carries information
about the next three years, less than a leaky backtest suggests and more than nothing, and the number to beat is now
on the record.

`analogs/us_2025.md` and `analogs/us_2026ytd.md` are the first live queries, built from the feed with the provenance
of every value in `analogs/us_2025_query.json`; they cover 9 of the 20 features (no credit, valuation or investment
yet — those arrive with the bridge pull), so they are a demonstration of the plumbing, not a reading.

## Test 2: the subnet at t, flux, and measured targets (`tools/analog_test2.py`, `analogs/test2.md`)

The leak had been borrowing the *outcomes* of other countries in the same global episode. Their *states* at time t are
legitimate information, so `tools/features2.py` adds three families computable at t and nothing later: the subnet
(cross-sectional shares, means and dispersion of the others; crises already begun elsewhere in t−1 and t−2; the
bloc and its base currency's state, from `peg_base`), the relative growth race (percentile rank within the
cross-section), and flux (speed of the state in z-space, band transitions, accelerations). The harness is walk-forward
throughout, with expanding-window standardization, so it is stricter than the first backtest.

What moved. On the JST crisis label within three years, base features alone score AUC 0.53 (the leaky same-country
number on this harness is 0.63); the subnet alone scores 0.58 — the others' present state carries as much crisis
information as the country's own whole state vector — and everything together 0.58. Skill by horizon peaks at two to
three years (0.56–0.58) and is gone by four (0.51) and five (0.48): the cone's "day 5" is about three years.

Where the signal is. Measured targets are far more predictable than the label: a 30% real equity drawdown within three
years AUC 0.67 (top decile 35% against a 12.5% base rate), a 5-pp credit contraction 0.68 (top decile 45% vs 17%), a
5% real GDP per capita fall 0.61, a 3-pp unemployment spike 0.59.

## Lead-lag: the path into T (`tools/lag_test.py`, `analogs/lag_test.md`)

Does the path into T carry information the point at T does not? Three measurements. *Trajectory analogs*: matching on
the state at T, T−1 and T−2 (60 dimensions) makes the nearest-neighbour cone worse, not better (drawdown 0.61 → 0.55,
label 0.53 → 0.50) — stacking lagged copies dilutes an equal-weighted distance with redundant dimensions; adding only
five lagged features with proven lead keeps it level (0.665 / 0.667 on drawdown and contraction). *Lead profiles*:
for every feature and lag 0–4, the single-feature AUC for each event, with pre/post-1950 agreement. The drawdown's
information is coincident and persistent (low dividend yield, low r−g, low real rate, high inflation, all best at
lag 0, decaying slowly); the credit contraction has true leads — the *level* of loans/GDP three to four years earlier
(0.73 at k=3–4, era-consistent), equity weakness one year earlier (0.65 at k=1), house-price weakness coincident.
*Mile markers*: the event rate as markers arrive in sequence — credit contraction 17% unconditional → 30% with
loans/GDP in the top tercile at T−3 → 42% with real equity gains ≤ 0 at T−1 → 51% with real house prices ≤ 0 at T
(post-1950: 25 → 36 → 52); drawdown 12% → 23% (low dividend yield) → 31% (low r−g) → 43% (high inflation). Those
ladders are measured likelihood ratios: the lag structure is worth more as conditioning than as distance.

## Testing the target (`tools/label_test.py`, `analogs/label_test.md`)

The crisis flag is a narrative judgment, so it was tested against the measured record. Labelled crisis years do look
different in the real economy and the market — unemployment rises (AUC 0.77 as a detector), real GDP per capita falls
(0.70), real equity falls (0.71) — but not in the banking aggregates the label is nominally about: loans/GDP (0.50),
the bank capital ratio (0.53) and noncore funding (0.46) do not register a labelled crisis at all. A measured stress
event built from the data alone matches the label poorly: with three of five conditions, recall 14% and precision 27%;
with two of three real-economy conditions, 27% and 28% — and 60 measured stress episodes carry no label (the wars,
1920–21, 1930–33 outside the banking cases, 1974, 2009, 2020). Timing is noisy by a year: for the 86 labelled crises,
measured stress peaks the year before the label in 18 cases, in the label year in 30, a year after in 16, two years
after in 11, and never in 11. About one label in ten is contested by another chronology and seven were recoded between
releases. Conclusion for the framework: the label is a banking-narrative event, loosely coupled to measured stress,
dated to within ±1 year, and less predictable from the state (0.58) than the measured outcomes are (0.67–0.68). It
stays as one view; the measured targets become the primary ones, and the horizon curve is reported for each.

## What this layer is for next

1. **Feature weighting measured, not assumed**: a learner that can weight (regularized logit or boosted trees),
   walk-forward, against the measured targets and by horizon; and conformal bands so coverage is 50% by construction.
2. **Climatology**: the unconditional distribution of each feature by era and regime (`peg_type`), which is what the
   forecast relaxes toward at long lead times.
3. **Voice ledger**: resolve Dalio's dated reads against the criteria recorded here and the data in `jst/` and the feed;
   the same table takes any other voice.
4. **The bridge**: once the first workflow run writes `bridge/`, confirm the join rules and complete the live query
   vector (credit, mortgages, investment, current account, house prices, dividend yield).

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
