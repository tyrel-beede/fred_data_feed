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

## Revision one (`history-v1`, 2026-11-06)

What stands at revision one — commit `bb2e0fc` plus this note; the `history-v1` tag is placed by the repository owner
(see `HANDOFF.md`) — so that later work has a fixed point to be compared against:

- **The record**: JST R6 (18 countries, 1870–2020) with two cited overrides and a propagated override flag; the Dalio
  corpus taken apart into templates, 48 cases, gauges and 193 graded reads; the physical layer (CO2 and energy,
  oil since 1861, CHAT technology adoption, USGS minerals, the commodity PPI, US energy from 1635, European energy
  from 1800); the network's topology from the regime columns; the corporate layer (Z.1 from 1945, BEA profits from
  1929, Shiller from 1871, home prices from 1890; Goyal–Welch from 1871 and Jacks's 42 world commodity prices from
  1850, both supplied by hand; the SEC financial-statement data sets for every quarter since 2009 and the 13F data
  sets since 2013, pulled from the owner's desktop and reduced to aggregates). 98 physical and 17 corporate files
  pulled by the workflow with hashes; the four desktop-only sources are all in, with their refresh cadence in
  `HANDOFF.md`.
- **The four parts of the foundation as artifacts**: the climatology by measured topology era (`climatology/`), the
  analog library with a full 20-feature live query and measured join rules (`analogs/`, `bridge/join_rules.json`),
  the voice ledger (`dalio/reads.csv`, 193 reads graded for falsifiability, unscored), the mechanisms (templates,
  ladders with measured conditional rates).
- **The measured numbers**: walk-forward crisis-label AUC 0.59 for the analog cone (the leaky 0.66 retired); measured
  targets 0.68–0.76 with weighted learners; the oil price the one physical feature that earns its place (GDP fall
  0.60 → 0.68 on the logit, four times its band; the drawdown's 0.73 → 0.76 on the trees sits at the edge of theirs
  and rests on the top-decile lift, 40% against 14%); diffusion, materials, the Jacks panel and topology measured
  and found not to add as features (the global-at-t families cost skill as weights and earn it as ladder rungs: a
  real commodity bust at T lifts the contraction rate 42% → 62%); the CO2 proxy calibrated against measured energy; the era split and the cadence noise band
  (`analogs/noise_band.md`: refit years shifted 0–3, mean range 0.03 for the logit, 0.025 for the trees, up to 0.07 and
  0.06 on single cells) as the reading rules for every comparison.
- **What it does not do**: forecast the dials' branches by itself; learn from the handful of eras; see the micro layer
  before 2009; bridge any country but the United States. No investment advice.

The revision-one pass closed with the SEC backfill and its quality-control check (2026-11-07): the full
financial-statement and 13F records in, the 13F reduction found wrong before 2023 and rewritten (units detected per
filer, the set's own report period, amendments handled), the financial-statement reduction split by sector and capped
for scale errors, a synthetic self-test for both, `corporate/sec_analysis.md` as the SEC layer's read over its record,
and seven SEC checks in `QC.md` — two of which fail by design until the re-reduction runs from the owner's desktop
(`HANDOFF.md`). The tag goes on the commit that closes that run.

Queued after the tag: conformal bands, mile-marker timing, the voice ledger scored against outcomes, the diffusion
panel past 2003, the bridge for other countries, a windowed climatology for young eras.

## Where things live

| to find… | open | built by |
|---|---|---|
| the measured record (18 countries, 1870–2020) and its features | `jst/jst_r6.csv`, `jst/features.csv`, `jst/data_dictionary.md` | `tools/jst_build.py` |
| the crisis chronology and the two overrides | `jst/crises_chronology.csv`, `jst/overrides.csv` | `tools/jst_build.py` |
| the climatology by era and regime | `climatology/*.csv`, `climatology/README.md` | `tools/climatology.py` |
| the network's topology (subnets, breaks) | `jst/topology.csv`, `analogs/topology_test.md` | `tools/topology.py` |
| the analog cone's skill and the learners' numbers | `analogs/learner_test_physical_era*.md`, `analogs/noise_band.md` | `tools/learner_test.py`, `tools/noise_band.py` |
| the ladders (conditional event rates after a signal) | `analogs/lag_test.md` | `tools/lag_test.py` |
| the live US query and its nearest analogs | `analogs/us_2026ytd.md`, `analogs/us_2026ytd_query.json`, `bridge/join_rules.json` | `tools/live_query.py`, `tools/analogs.py` |
| the physical layer (energy, oil, diffusion, materials, commodities) | `physical/*_features.csv`, `physical/README.md`, `physical/catalog.json` | `tools/physical_pull.py`, `physical_build.py`, `physical_build2.py` |
| the long corporate anchors (Z.1, BEA, Shiller, Goyal–Welch) | `corporate/us_corporate_annual.csv`, `corporate/README.md` | `tools/corporate_pull.py`, `corporate_build.py` |
| the SEC layer: quarterly tables and the read over its record | `corporate/sec_fsds_quarterly.csv`, `corporate/sec_13f_quarterly.csv`, `corporate/sec_analysis.md` | `tools/corporate_pull.py` (desktop), `corporate_build.py`, `sec_analysis.py` |
| the voice ledger and the Dalio encodings | `dalio/reads.csv`, `dalio/*_template.json`, `dalio/*.md` | `tools/assemble.py` |
| what runs from a desktop, and the tag | `HANDOFF.md` | — |
| the checks and their evidence | `QC.md` (mechanical), `QC_review.md` (content) | `tools/qc.py`, `tools/tests/` |
| every source, license and citation | `sources.json`, `physical/catalog.json`, `corporate/catalog.json` | — |

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
                            backtest.md / backtest.json, test2, label_test, lag_test, learner_test(_physical…),
                            topology_test
  climatology/              the unconditional distributions by topology era and regime: every base feature's percentiles,
                            the forward outcomes, the event base rates (tools/climatology.py)
  corporate/                the corporate layer: Z.1 and BEA via FRED, Shiller, Goyal-Welch (long-record US anchors) and
                            the SEC financial-statement and 13F data sets reduced to aggregates (the bridge and live
                            cone); us_corporate_annual.csv, sec_fsds_quarterly.csv, sec_13f_quarterly.csv,
                            sec_analysis.md/json (the SEC layer over its record), catalog, README
  physical/                 the physical layer: OWID extract (CO2, energy), oil prices since 1861, the CHAT technology-
                            diffusion panel, USGS mineral statistics and FRED commodity prices (raw/ pulled by the
                            workflow), the derived footprint, oil, diffusion and materials features, and the catalog
  tools/
    jst_build.py            workbook -> csv, coverage, crisis flags, units, features
    jstlib.py               shared loader (sheet + overrides + features)
    bridge_pull.py          the FRED bridge (needs FRED_API_KEY; runs in the pull workflow)
    assemble.py             merges the documentation and book encodings into the layout above
    analogs.py              the empirical cone: nearest country-years and what followed, beside climatology
    analog_backtest.py      skill of the cone by feature group under three exclusion rules
    features2.py, wf.py, analog_test2.py, label_test.py, lag_test.py, learner_test.py   test 2 (subnet, rank, flux;
                            measured targets; horizons), the tests of the crisis label, the lead-lag measurements,
                            and the weighted learners
    topology.py             the network's topology from the regime columns: subnets, tenure, moves, churn, breaks ->
                            jst/topology.csv and analogs/topology_test.md
    physical_pull.py, physical_build.py, physical_build2.py   the physical layer: the workflow's raw pulls, the
                            energy/CO2/oil features, the diffusion and materials features
    corporate_pull.py, corporate_build.py   the corporate layer: the workflow's pulls (FRED-resolved Z.1 and BEA
                            series, Shiller, Goyal-Welch) and the SEC reductions (desktop; --redo, --selftest), the US
                            annual series and the two SEC quarterly tables
    sec_analysis.py         the SEC layer over its record: annual flows and ratios, the timely read, calibration
                            against Z.1 and NIPA, the 13F concentration series -> corporate/sec_analysis.md
    tests/                  test_sec_aggregators.py: the SEC aggregators on synthetic data sets (run by qc.py)
    climatology.py          the climatology tables by measured topology era and regime -> climatology/
    noise_band.py           the cadence noise band from the shifted-refit runs -> analogs/noise_band.md
    live_query.py           the live US query vector (all 20 features) from the JST sheet, the bridge and Shiller, with
                            the join rules measured on the 2016-2020 overlap -> bridge/join_rules.json
    qc.py                   mechanical checks -> QC.md (33 at revision one)
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

`analogs/us_2026ytd.md` is the live query, built by `tools/live_query.py` from the JST sheet through 2020, the FRED
bridge from 2021 and Shiller's workbooks: all 20 features, each with the series, the months or quarters behind it
and the join factor beside its value. The join rules are measured, not remembered — `live_query.py` recomputes the
2016–2020 overlap between every bridged series and the JST column each run and writes `bridge/join_rules.json`:
rates, the fiscal flows, M2 and the dividend yield join at level (overlap ratios within 1% of one; the JST equity
series turn out to *be* Shiller's annual means, ratio 1.0000 and capital-gain differences 0.0000); the CPI (×0.744),
nominal GDP (×0.977), federal debt (×1.05), house prices (×1.37), real GDP per capita (×0.55, Maddison dollars), bank
loans (×1.39, the JST aggregate is broader than bank loans and leases), mortgages (×0.84, a drifting ratio: scope
differs) and the investment share (×1.20, real against nominal) splice by a ratio chained at 2020. The current year's
rates and indices are year-to-date means, the current account is annualized by the quarters observed, and nominal GDP
is the mean of the quarterly series until the annual prints. The 2026 reading's fifteen nearest episodes are USA 2019,
Belgium 2014, USA 1996, USA 2005, Japan 2007, Italy 1998 and their neighbours; what followed them, against the
climatology, is in the file — a record's answer to "what followed states like this one", not a forecast of the dials'
branches. `analogs/us_2025.md` is the earlier nine-feature demonstration, kept for the plumbing.

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

## A learner that can weight (`tools/learner_test.py`, `analogs/learner_test.md`)

The same 53 features (base, subnet, rank, flux, five selected leads, three mile-marker indicators with training-set
terciles) fed to learners that weight them — an L2 logit and shallow gradient-boosted trees — refit every four years
on rows whose outcome window closed before the fit year, forecasting the next four; the nearest-neighbour share on the
same features is the no-weights reference. Walk-forward AUC within three years, queries from 1900: a 30% real equity
drawdown 0.73 with the trees (k-NN 0.65; top decile 35% against a 14% base rate), a 3-pp unemployment spike 0.67
(k-NN 0.57), the crisis label 0.63 (k-NN 0.60), while the credit contraction stays at 0.68–0.69 under every learner
(its signal — the loans/GDP level three years earlier — is simple enough that weighting adds nothing) and the GDP fall
is best left to k-NN at 0.61. The heaviest weights are readable: for the drawdown, low r−g, a low real rate, a high
share of countries in a credit boom, the state's two-year speed and a low dividend yield; for the contraction, the
loans/GDP level three years back above everything else. The label's horizon curve under the logit is 0.61 / 0.58 /
0.58 / 0.54 / 0.51. Differences of ±0.02 are within noise for a few hundred events; the gaps above are larger than that.

## The physical layer (`physical/`, `tools/physical_build.py`, `tools/physical_build2.py`)

Fossil CO2 by fuel from 1750–1870 and primary energy, fossil production and consumption from 1900/1965 for the 18
countries, from Our World in Data's repositories (Global Carbon Budget, EIA, Energy Institute, Ember; licenses in the
extract's provenance file), with derived features: the **energy footprint gap** (CO2 or energy growth minus real GDP
growth over three years, and its anomaly against the country's own trailing decade), carbon intensity, fossil
production growth, fuel self-sufficiency, fuel shares. Added to the learners: the real GDP fall gains (0.61 → 0.66
under k-NN; +0.02 on the weighted learners), the financial targets do not move at their best learner, and the
footprint gap takes weight in the crisis and drawdown models without adding skill — redundant with the subnet and
credit features, not wrong. Oil prices since 1861 (fetched by the workflow, deflated into a real price with changes, a
shock flag and an exposure-signed change) then move the two targets the shock channel should move: real GDP fall
0.60 → 0.68 (logit) and the equity drawdown 0.73 → 0.76 (trees, top decile 40% against 14%) — the shadow price of the
energy constraint earns its place.

The second slice brings in the CHAT technology-adoption panel (sixteen technologies, 1870–2003: the pace of adoption,
its acceleration, the lead technology's pace, the distance to the frontier, the diffusion race) and the USGS mineral
statistics with the FRED commodity PPI (a base-metal basket's real price changes and its price against its own
history, world metal production growth and acceleration, gold, the real commodity PPI; global at t). Measured
like-for-like with an era split (`analogs/learner_test_physical_*_era.md`): **diffusion adds no skill** at three years
— within ±0.03 of the baseline wherever the panel exists, and harmful after 2003 where it is missing for every country
(the label's trees 0.62 → 0.35 on that window) — with one ladder hint, slow diffusion lifting the contraction rate
42% → 54% after the credit and equity rungs; **materials move the label** (logit 0.58 → 0.66, the largest move it has
shown) while costing the logit on the drawdown (0.60 → 0.52) and the GDP fall (0.68 → 0.62) as a linear model fits the
era from eight global columns — the trees barely move, and are the right learner for global-at-t features; the two
families together land at or below the oil run everywhere. The era split also shows that from 2004 the drawdown
and contraction AUCs are 0.8–0.9 for every learner because 2008 is one synchronized event, so skill on the full
panel is mostly pre-2004 skill. The later pulls landed the EIA series (US energy 1949– and the 1635–1945 estimates)
and the European energy series 1800–2009 (`physical/kmw_extract.csv`): the CO2 proxy is now calibrated against
measured energy — near-exact for the coal economies, 4–14 pp a year too fast for the wood-and-hydro economies in their
transition decades — and swapping measured energy into the footprint gap moves no AUC by more than 0.01
(`analogs/learner_test_physical_measured_era.md`). `physical/catalog.json` lists what is pulled and what still has
to be supplied (the Jacks commodity panel, ore grades, land).

## The climatology (`climatology/`, `tools/climatology.py`)

The fourth part of the foundation — climatology, analog library, voice ledger, mechanisms — is now an artifact rather
than a sentence. `climatology.py` takes the measured topology eras (1870–1913, 1914–31, 1932–39, 1940–72, 1973–98,
1999–2020) and the regime (`peg_type`) as the index and writes, for every cell with thirty country-years or more, the
five percentiles of each base feature, the forward outcomes the analog reports use and the event base rates. The
arrangement is a climate: the median loans/GDP ratio is 34% in the first era and 96% in the last, the median long
rate 3.9% and then 9.2% in 1973–98 and 3.4% after; real equity three years out runs +17% at the median in 1870–1913,
+8% with a −29% lower quartile between the wars, +28% in 1973–98; unemployment spikes 35% of the time in 1914–31 and
1% of the time in 1940–72. The same state vector means different things in different arrangements, which is why the
analog retrieval standardizes inside an expanding window and why the far end of a cone should relax toward the era's
climate rather than the pooled one. `climatology/README.md` carries the headline tables.

## The noise band (`tools/noise_band.py`, `analogs/noise_band.md`)

The harness refits every four years; shift those years by one, two and three and rerun, and the spread is the
run-to-run noise with nothing else changed (the trees have no other randomness at this sample size; the k-NN does not
refit and does not move). Mean range across targets: 0.031 for the logit, 0.025 for the trees, 0.016 for the ensemble;
single cells reach 0.07 (the logit on the drawdown before 2004) and 0.06 (the trees on the contraction before 2004).
Read against it: the oil price's GDP-fall gain (+0.08, logit) and the materials family's label move (+0.08, logit)
clear the band, the oil drawdown gain (+0.03, trees) sits at its edge, the Jacks panel's GDP-fall loss (−0.09 logit,
−0.05 trees) clears it the other way, and the diffusion, topology and measured-energy differences (±0.01 to ±0.06,
mostly logit) sit inside it — which is the reading the sections above already gave,
now with the band written down rather than assumed.

## The corporate layer (`corporate/`, `tools/corporate_pull.py`, `tools/corporate_build.py`)

Corporate filings were the question — 10-Ks and 13-Fs as a data source — and the answer is a layer with two depths.
Machine-readable filings begin in 1993 (structured financial statements 2009, structured 13F holdings 2013): one
era, the kind the tests here keep showing cannot be learned as a climatology. So the filings go to the bridge and
the live cone as *counted* records (self-reported, audited, a quarter stale; 13F long-only and 45 days late), where
they add two things the macro aggregates lack — the capex, buyback, dividend and cash cycle across all filers, and
the crowding of institutional holdings — and the long record comes from the compiled sector accounts instead: the
Fed's Financial Accounts for nonfinancial corporate business from 1945 (debt, equity at market value, net worth,
capital expenditures, dividends, liquid assets), BEA corporate profits from 1929, Shiller's market series from 1871,
and the Goyal–Welch predictors (net equity issuance, book-to-market, the default spread). `corporate_pull.py` fetches
them in the workflow — the FRED series resolved by exact title at run time, the SEC quarterly zips streamed and
reduced to aggregates because the files are hundreds of megabytes — and `corporate_build.py` turns the long series
into `corporate/us_corporate_annual.csv`, one row per year, every value computable at year end. These are US-only
and so stay out of the panel learners (a learner would read the missingness as the country); they belong to the US
query vector and to the corporate reads in the voice ledger. `corporate/README.md` and `corporate/catalog.json`
carry the routes, licenses and provenance notes.

The SEC side is the one place in the history layer where the record had to be reduced before it could be kept: the
quarterly zips run to hundreds of megabytes, sec.gov refuses cloud addresses, so the owner's desktop streams every
set (71 financial-statement quarters since 2009, 54 13F sets since 2013) and keeps only aggregates. The first
reduction was wrong for 13F before 2023 — the form's unit changed from thousands to dollars in 2023, and inside the
thousands-era sets a few hundred filers reported in dollars; scaling a set by its majority unit multiplied them a
thousandfold — and the quality-control pass that found it (totals of $300–480 trillion against a $50 trillion
market, trillion-dollar single positions, the median filer's concentration a thousand times too small) rewrote both
reductions: units detected per filer from the implied price of its lines, only each set's own report-period filings
counted, amendments handled, the financial-statement sums split by sector (banks' operating cash flow swings with
their trading books) and screened for scale errors, every set stamped with its aggregator version, and a synthetic
self-test under `tools/tests/`. `tools/sec_analysis.py` then reads the layer over its record — annual flows and
ratios of the December-fiscal-year filers with the latest year's percentile, the timely year-to-date read, the
calibration of the sums against Z.1 and NIPA (coverage near a quarter, growth correlation 0.4–0.5), the 13F
concentration series — and a consistency section that lays the same period's sum from every file it appears in side
by side, so a file whose values are inflated is visible rather than averaged in. What the first reduction got right
stands; what it got wrong is marked stale in the tables, in `QC.md` and in the analysis until the desktop
re-reduction replaces it (`HANDOFF.md`).

## The network's topology (`tools/topology.py`, `jst/topology.csv`, `analogs/topology_test.md`)

Nodes come and go from subnets, and the JST regime columns record it: `peg_type` (BASE, PEG, FLOAT) and `peg_base`
(GBR, USA, DEU, HYBRID) give, for every country-year, which base currency the country is tied to — one sterling bloc of
thirteen before 1914, fragmentation and hybrids between the wars, one dollar bloc of sixteen by 1960, a dollar bloc
and a mark bloc with floaters from 1973, the euro bloc from 1999. From those columns alone, with nothing dated by
hand, `topology.py` measures the node's place in the arrangement (in a peg, a base, bloc size and share, tenure in
the current state, whether it moved subnet in the last three years, churn in its bloc, a base change within five
years) and the arrangement itself (number of blocs, share pegged, panel-wide changes in three years, years since the
last break). A **break** is a year in which at least a third of the recorded countries changed state, and the data
finds four: 1914 (17 of 17), 1932 (7 of 18), 1940 (17 of 18) and 1973 (13 of 18) — the two wars, the gold standard's
collapse and the end of Bretton Woods, found without being told.

Three measurements of what the topology carries:

- **Climate by era.** Event base rates between the measured breaks differ by an order of magnitude: in 1940–72 (war,
  then one dollar bloc) the crisis label fires 0% of the time, unemployment spikes 1% and the stress composite 3%;
  in 1914–31, 23%, 35% and 24%; the 1932–39 bloc era has credit contractions 54% of the time; 1973–2020 sits in
  between (drawdown 16%, contraction 20%, label 9%). These are the unconditional rates a forecast relaxes toward at
  long lead times — the climatology the plan called for, with the arrangement as its index. The arrangement marks a
  whole institutional setting (wars, capital controls, financial repression, the euro), not a cause by itself.
- **The topology alone as a forecast.** Walk-forward, the pooled trailing event rate (the no-skill reference, varying
  only with the query year) scores 0.40–0.48 — below a coin flip, because the trailing mean lags the regime (a 1930s
  rate carried into the calm 1950s). Conditioning the rate on the node's class (peg type × bloc size × moved
  recently) lifts it to 0.54 on the contraction, 0.54 on the GDP fall and 0.55 on the label, 0.49 on the drawdown,
  and 0.37 on unemployment. So the topology by itself corrects part of the reference's drift on three targets, and
  nothing more.
- **After a break.** In the three years after a measured break the drawdown rate is 27% against 11% in all other
  years, the credit contraction 48% against 14%, the GDP fall 30% against 10% (192–213 country-years), while the
  crisis label is 4% against 10% — the label does not register the wars, as `label_test` found. The break arrives
  with the shock rather than ahead of it: it is a signature, usable as a mile marker the year it is observed (four
  observations), not a precursor.

As learner features (`analogs/learner_test_physical_topology_era.md`, twelve columns on top of the oil run): the
logit gains on the drawdown (0.60 → 0.66) and unemployment (0.55 → 0.61) while the trees lose on unemployment (0.68 →
0.59) and the label (0.63 → 0.56); the era split places the drawdown gain entirely from 2004 (0.81 → 0.94, one event,
the euro-era arrangement scored against 2008) and the pre-2004 numbers within noise or down. Four of the twelve
columns are global at t and the family's information is a handful of arrangements, so this is the materials result
again: a few eras cannot be learned as features, and the trees over-carve them. The topology's place is the
climatology and the break marker, not the feature vector.

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

1. **Calibrated bands and on-time markers**: conformal bands so coverage is 50% by construction; the gap distribution
   between successive markers so an on-schedule arrival carries a higher ratio than an early or late one; a seed and
   cadence sweep on the trees to size the noise band around each AUC.
2. **Climatology**: done in revision one (`climatology/`, indexed by the measured topology eras and the regime); a
   windowed (trailing 30-year) variant remains to be added for a young era.
3. **Voice ledger**: resolve Dalio's dated reads against the criteria recorded here and the data in `jst/` and the feed;
   the same table takes any other voice.
4. **The bridge**: done in revision one — `tools/live_query.py` measures the join rules each run and builds the full
   20-feature live vector; what remains is to carry the join to the other 17 countries' live feeds when there are any.
5. **Extend the diffusion panel past 2003** (electricity from OWID's energy data, telephones and internet users from
   the ITU, vehicles from the WDI) so the family can be retested on the window that holds the later episodes, and
   test the materials family under a learner built for global-at-t columns (the trees, or a year-demeaned logit)
   before the label's 0.66 is quoted as a finding.

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
- 2026-11-04 (physical, second slice): CHAT country names mapped to the 18 ISO codes by hand (no partial matches used);
  inception years taken from the raw series before the population join (a first build took them after it and lost the
  1870s — caught by the 1873 spot check and fixed); 108 one-year per-capita log jumps above 1.0 flagged as breaks and
  excluded from growth; the USGS parser located the real unit value (98$/t) and world production columns by header, and every
  basket workbook has both from 1900–1905 on (the Steel sheet's real unit value ends 2010 and Pig Iron's 1988, so the
  basket uses iron ore for price and adds pig iron for production only); PPIACO averaged from monthly to annual (≥ 6 months)
  and deflated by the JST US CPI; spot checks at 1873, 1893, 1920, 1929–33, 1973–80, 2008 and 2011 read as the record
  says; the baseline era run reproduced the oil run's AUCs to three decimals; the ladder re-run reproduced every earlier
  section unchanged (diff limited to the three new ladders); `tech_n` removed from the learner family after it took
  heavy weights as a calendar proxy.
- 2026-11-04 (topology): subnets read from `peg_type`/`peg_base` only; the four measured breaks (1914, 1932, 1940, 1973)
  checked against the regime columns year by year (1914: all 17 recorded countries change state; 1932: 7 leave the
  interwar pegs; 1940: 17 of 18; 1973: 13 of 18); spot checks — GBR 1913 base of a bloc of 13 with 44 years' tenure,
  GBR 1931 on a gold peg with no base country recorded and so no bloc, USA 1960 base of 16, DEU 1973 floating with 15 bloc moves in
  three years, IRL and ESP 1999 in the DEU bloc of 9 — all as the record says; the climatology test is walk-forward
  (training rows' windows closed before the query year, classes with fewer than 20 training rows left unscored).
- 2026-11-05 (EIA 1635–1945): the notes page links the table as a PDF; the parser reads its text layer, treats the
  table's "– –" (two dashes) as one not-applicable cell, drops dot leaders and the footnote letter glued to the 1945
  wood value, and checks fossil, renewable and total sums on every row — 42 rows, 42 pass, matching a reader's
  independent extraction of the same PDF value for value; the CO2-proxy calibration (correlation 0.993 with fossil
  energy growth, +4.5 pp a year against total energy growth before 1900, +0.1 pp after 1905) computed at five-year
  spans from the two files as stored.
- 2026-11-06 (KMW European energy): the Mendeley file API delivered the deposit's workbook through the workflow;
  `kmw_parse.py` finds each sheet's carrier columns by header text (the UK sheet in mtoe, converted), checks every row's
  carrier sum against the compilers' total (1,813 rows, four Spanish rows off by more than 1%, kept and flagged), and
  leaves Warde's England and Wales sheet out because GBR is the UK; the splice into the features changed only
  previously empty cells (777 country-years); the proxy calibration by country and era recomputed from the stored
  files; the measured-energy learner run reproduces the proxy run within ±0.01 everywhere.
- 2026-11-06 (Jacks): the workbook's group headers span merged cells and were carried forward by column; 42 commodities
  found with their first years as the chartbook lists them (gas, aluminum, chromium, manganese, bauxite, iron ore,
  potash, platinum, soybeans from 1900; petroleum from 1860; rubber from 1890); the equal-weight index is chained from
  mean one-year log changes over the commodities present at both ends, so entries and exits do not jump it; spot
  checks at 1917, 1920, 1932, 1974, 1986, 2008 and 2022 read as the record says; the ladder re-run reproduced every
  earlier section unchanged (diff limited to the three Jacks ladders).
- 2026-11-06 (corporate layer): the first workflow run resolved all FRED titles (the "Debt Securities" series answered
  for the debt key, so a second key for "Debt Securities and Loans" was added and the builder prefers it); the
  resolved ids, titles, units and start dates are in `corporate/raw/FRED-Z1/series_used.json`; the SEC endpoints
  returned 403 until the User-Agent carried a contact in the fair-access form; Shiller's Yale server refused the
  runner's connection and the Goyal-Welch page exposed no Drive link, so both carry fallbacks and an attach route;
  `us_corporate_annual.csv` spot-checked — NIPA profits before tax 10% of GDP in 1929, 3% in 1933; nonfinancial
  corporate equities 0.42× GDP in 1950, 1.30× in 2000, 2.1× in 2024; dividends 30% of after-tax profits in 1973,
  88% in 2000 — against the published series.
- 2026-11-07 (SEC backfill and quality control): inventory after the owner's desktop runs — 71 financial-statement
  sets 2009q1–2026q3 without a gap (2009q1–q2 header-only: no tag reaches twenty filers before the phase-in) and 53 of
  the SEC's 54 13F sets (the Jun–Aug 2026 window, published after the run, and the first 2024 window named
  `01jan2024-29feb2024` rather than the December start the name generator assumed; both fixed in the puller, which now
  tries the predictable names as well as the index's links). The rebuilt 13F table showed totals of $329 trillion
  for the 2014q4 set and $478 trillion for 2022q2 against $47 trillion for 2023q4, a Gilead convertible at $12
  trillion in a top-20 list, and the median filer's top-10 share at 0.04% before 2023 and 54% after: inside the
  thousands-era sets a few hundred filers report in dollars and the set-wide scaling multiplied them a thousandfold,
  and the per-filer heaps behind the median were never scaled. Aggregator v2 (13F) detects the unit per filer from
  the implied price of its lines against each issuer's cross-filer reference, keeps only the set's own report-period
  holdings reports (a restatement replaces its original, a new-holdings amendment adds to it, notices and late
  reports for earlier periods set aside) and records the report period; on a synthetic set the size of a real one
  (2.8 million lines, 7,500 filers, 2% in the other unit) it recovers the true total exactly and every mixed-unit
  filer, in 19 seconds. The financial-statement sums were checked across files: the same December-31 assets appear
  in the 10-K file and in later 10-Q comparatives files with sums that differ by up to 2.1× (2025: $35.5 trillion
  in the 10-K file, $74.2 trillion in the following quarter's), and all-filer operating cash flow for a single
  quarter swings threefold year to year with banks' trading books; aggregator v3 keys values by filer rather than
  submission (a 10-K/A no longer counts beside its original), splits the sums by sector, sets aside values beyond a
  per-tag plausibility cap and lists the five largest filers per key in a sidecar, so the next re-reduction can
  say which file carries the inflation. Both aggregators carry a version, `--redo` re-fetches, `--selftest` runs
  38 synthetic checks, and `qc.py` gained seven SEC checks (self-test, no gaps in either record, the unit split at
  2023q1, no stale thousands-era set, table consistency, versions in use, analysis bounds). Two fail by design until
  the desktop re-reduction lands.
- 2026-11-07 (the re-reductions, measured): the owner's desktop re-reduced the 53 13F sets with v2 in under an hour
  and the 71 financial-statement sets with v2 in ten minutes (not the two hours estimated). 13F: report periods as
  the set names imply; 70–90 filers per thousands-era set reported in dollars, carrying 1–3% of value once
  corrected; after the 2023 change 1,205 filers in the first dollar-era set still reported in thousands (18% of
  value), thinning to 361 (4%) by the May 2026 set; holdings value $19–27 trillion in 2013–2018, $27–38 trillion in
  2018–2019, $34–54 trillion in 2020–2022, $40–72 trillion since, against $300–480 trillion before; the median
  filer's top-10 share 38% in 2013 rising to 54% in 2026; the top-10 issuer share 9–25%. Six sets still carried
  option lines worth more than the market (put/call shares of 25–58% against 4–8% elsewhere) and one a $6.6
  trillion issuer line (Brookfield, June 2021), so v3 snaps a filer's unit to the nearest power of a thousand,
  sets aside single lines beyond $1 trillion and filers beyond $20 trillion after scaling, reports the total
  excluding options, and lists the ten largest managers by name as a sanity check; on the real-sized synthetic set
  it recovers the true total exactly with every mixed-unit and millionfold filer identified, in 21 seconds.
  Financial statements: with one value per filer and dimensional rows set aside, the same December-31 sum now
  agrees across the files it appears in (2024 assets $69–74 trillion in five files; 2025 $74–78 trillion in three)
  — the first reduction's 10-K-file sums were the low ones, its "first value seen" having taken segment rows —
  and the capex sum's growth correlation with the Z.1 series rose from 0.49 to 0.69 (0.75 after the phase-in),
  the dividend and profit sums' coverage holding steady; the all-filer quarterly operating cash flow still swings
  with the banks, which the v3 sector split addresses. Both v3 reductions are pending one desktop run.
