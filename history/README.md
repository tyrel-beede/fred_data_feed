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
                            backtest.md / backtest.json, test2, label_test, lag_test, learner_test(_physical…),
                            topology_test
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
panel is mostly pre-2004 skill. `physical/catalog.json` lists what is pulled and what still has to be supplied (US
energy 1635–, European measured energy 1800–, the Jacks commodity panel, ore grades, land).

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
2. **Climatology**: the unconditional distribution of each feature by era and regime, which is what the forecast
   relaxes toward at long lead times — the topology eras measured in `analogs/topology_test.md` are the index to use,
   with a windowed (trailing 30-year) variant as the fallback where an era is young.
3. **Voice ledger**: resolve Dalio's dated reads against the criteria recorded here and the data in `jst/` and the feed;
   the same table takes any other voice.
4. **The bridge**: once the first workflow run writes `bridge/`, confirm the join rules and complete the live query
   vector (credit, mortgages, investment, current account, house prices, dividend yield).
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
