# history/physical — the physical layer under the economic record

Booms run on a physical input — ore, coal, oil, land, track-miles, fibre, now megawatts — and credit carries them past
the point where the marginal physical return supports the debt that financed them. This directory holds the
long-running physical catalogs that let the history layer see that, in the same provenance discipline as `jst/`.

Physics enters the system in two roles, and only one of them shows up as backtest skill:

- **Floors in the forward model** — the scenario is refused if it needs energy or capacity that does not exist (the
  Bull Case 2.0 workbook's gigawatts, chips per gigawatt and power delivered). Floors prune impossible branches
  forward; they cannot raise a historical AUC, because the record only contains paths that respected them.
- **Features in the backtest** — the supply-shock channel (energy prices, about a one-year lead on activity), the
  marginal-cost channel (ore grades, well depth, energy return on investment: slow variables for the long cycle), the
  diffusion channel (where the era's lead technology sits on its S-curve, and capex against revenue in that sector),
  and the one gauge that applies to every boom in the panel: the **thermodynamic footprint** — energy (or, before
  1965, fossil CO2) growth minus real GDP growth over three years. A boom with a footprint built something; a boom
  without one priced something.

## What is here now

- `owid_extract.csv` — the 18 JST countries from Our World in Data's `co2-data` and `energy-data` repositories (source
  commits in `owid_extract.provenance.json`): fossil CO2 by fuel from 1750–1870, primary energy consumption from 1965,
  fossil production and consumption by fuel from 1900, electricity generation. Provenance class: measured (compiled
  statistics; early-decade emissions are reconstructed from fuel production records). Licenses: OWID CC BY 4.0;
  Global Carbon Budget CC BY 4.0; EIA public domain; Energy Institute free with attribution; Ember CC BY 4.0.
- `physical_features.csv` — derived per country-year by `../tools/physical_build.py`: CO2 growth (1y, 3y), real GDP
  growth (Maddison per capita × JST population), the **energy footprint gap** and its anomaly against the country's own
  trailing ten years (efficiency and decarbonization trends drift the raw gap), carbon intensity and its 3-year change,
  primary-energy growth and gap (1965 on), fossil production growth (1900 on), fuel self-sufficiency (production over
  consumption, 1965 on — the sign of a commodity shock for exporters versus importers), and the coal and oil shares of
  emissions (the fuel transitions).
- `raw/` — what the pull workflow (`../tools/physical_pull.py`) fetched, with `manifest.json` recording URL, size,
  SHA-256 and retrieval time per file: crude oil prices since 1861, the CHAT data appendix, 85 USGS DS140 commodity
  workbooks, the FRED physical price series. Raw files are never edited.
- `chat_extract.csv`, `usgs_extract.csv` — the 18 countries × 16 technologies as published (no fill), and the
  commodity basket's real unit values and world production by year, parsed from the workbooks named in
  `physical_build2.provenance.json`.
- `diffusion_features.csv`, `materials_features.csv` — derived by `../tools/physical_build2.py` (the second slice,
  below): technology diffusion per country-year, materials per year.
- `eia_extract.csv` — the EIA Total Energy series the workflow pulls with the `EIA_API_KEY` secret: US primary energy
  consumption by source 1949– (total, coal, petroleum, gas, nuclear, renewables, quadrillion Btu) with the fossil
  share and growth. `physical_build.py` uses it to carry the US energy growth and gap back from 1965 to 1952 where
  OWID has no value, both endpoints from the same source, with `energy_src` saying which (eia for 16 US years, owid
  otherwise). Nothing in the learner changed: the energy growth columns are not in its feature list.
- `eia_1635_1945.csv` — EIA's estimated US primary energy consumption for 42 selected years, 1635–1945 (wood every
  ten years from 1635; coal, gas, petroleum, hydro, wood and net electricity imports every five years from 1850;
  quadrillion Btu), parsed from the PDF's text layer by `../tools/eia_hist_parse.py` with every row's three sums
  checked (fossil, renewable, total; all 42 pass). Provenance class: stated/estimated — historical reconstructions
  (Schurr and Netschert's *Energy in the American Economy*; USDA fuelwood estimates in cords per decade), not
  measurements. What it is for: it calibrates the CO2 proxy. At five-year spans 1850–1945, OWID's US CO2 growth tracks
  the table's fossil energy growth almost exactly (correlation 0.99, mean gap 0.3 pp a year — the early CO2 series is
  itself built from fuel records), but overstates **total** energy growth by 4.5 pp a year before 1900, while wood fell
  from 91% of US energy in 1850 to 22% in 1900 (4% by 1945); after 1905 the gap is 0.1 pp. So before about 1900 the raw
  footprint gap (CO2 growth − GDP growth) carries the wood-to-coal substitution as a spurious boom for every country,
  with its own timing, and only the trailing-decade anomaly `gap_anom_3y` is the feature to trust there.
- `kmw_extract.csv` — the European energy-consumption series of Kander, Malanima, Warde and the national compilers
  (Fouquet's UK series 1500–2010; Sweden, Netherlands, Germany, France 1800–2009; Spain 1850–, Portugal 1856–, Italy
  1861–), annual PJ by carrier — food, feed for draught animals, fuelwood, water and wind, coal, oil, gas, hydro and
  other primary electricity, nuclear — from the Mendeley deposit by Rubio-Varas and Muñoz-Delgado (CC BY 4.0), parsed
  by `../tools/kmw_parse.py` (the UK sheet converted at 41.868 PJ per mtoe; every row's carrier sum checked against the
  compilers' total, four Spanish rows more than 1% off and flagged). `fuel_total` leaves out food and feed, so it is
  the analogue of EIA's total. Provenance class: stated/estimated. `physical_build.py` carries the energy growth and
  gap for these eight countries back to 1873 from it (777 country-years, `energy_src` = kmw, both endpoints from the
  same source), and builds `fgap_merged_3y` / `fgap_anom_merged_3y` — the footprint gap from measured energy where it
  exists (`fgap_src` = energy: 1,723 rows) and from the CO2 proxy elsewhere (887 rows).
- `jacks_features.csv` — Jacks's 42 real commodity prices 1850–2025 (`raw/JACKS-COMMODITIES/`, supplied by hand) as
  global-at-t features: the equal-weight index's changes and anomaly, breadth and dispersion, the energy, metals and
  grains groups, grown-minus-in-the-ground (`physical_build2.py`, `build_jacks`; results below).
- `catalog.json` — the catalog of long-running physical series: what is pulled, what the workflow can retrieve by URL,
  and what has to be supplied as a file (ore-grade compilations; the Jacks panel arrived by hand on 2026-11-06).

## How it is tested, and what the first slice did

`../tools/learner_test.py --physical` adds the physical features to the walk-forward learners and writes
`../analogs/learner_test_physical.md` beside a like-for-like baseline (`learner_test_rerun.md`, same code, same day).
The expectation stated before the run: modest gains on the activity targets from the shock channel, larger on the
financial targets from the footprint gap if it separates booms that built from booms that priced — and no movement
toward 0.85.

Result, 2026-11-04 (walk-forward AUC within 3 years, baseline → with physical): real GDP per capita fall **0.61 →
0.66** under k-NN, 0.60 → 0.62 logit, 0.58 → 0.60 trees — the activity target gained as predicted, and the heaviest
new weight is fuel self-sufficiency (exporters fall less, importers more: the shock-exposure channel, 1965 on). The
financial targets did not move at their best learner (drawdown 0.734 → 0.731, contraction 0.69 → 0.69, crisis label
0.633 → 0.634), and the unweighted k-NN got worse on the drawdown (0.65 → 0.61: nine more dimensions diluting a
plain distance, the same lesson as the lagged copies). The footprint gap and CO2 growth took heavy weights in the
crisis and drawdown logits without moving their AUC, which means they carry information the subnet and credit
features already carried. So the first slice earns its place on the activity target and is redundant, not wrong, on
the financial ones.

**Oil, the shadow price of the constraint (second run, same day).** The workflow fetched crude oil prices 1861–2025
(Energy Institute / S&P Global Platts via Our World in Data; `raw/EI-OIL-PRICE-1861/`, manifest with URL and hash).
`physical_build.py` deflates them by the US CPI from the JST sheet into a real price (1990 dollars per barrel), its
1- and 3-year changes, a shock flag (real price +40% in a year: 1876, 1895, 1899, 1916, 1932, 1934, 1947, 1974, 1979,
2000) and the change signed by each country's fuel self-sufficiency (importers +, exporters −). Added to the learners
(`../analogs/learner_test_physical_oil.md`): the real GDP per capita fall **0.60 → 0.68** under the logit (0.58 →
0.63 trees, 0.61 → 0.66 k-NN) — the largest single gain of any feature family on that target, the supply-shock channel
exactly as the frame predicted — and the equity drawdown **0.73 → 0.76** under the trees (top decile 35% → 40%
against a 14% base rate), with the real oil level and its 3-year change among the heaviest drawdown weights. The credit
contraction, unemployment spike and crisis label did not move. On the mile-marker ladders a ≥25% real oil rise as a
fourth rung lifts the contraction ladder 51% → 60% and the drawdown ladder 43% → 64%, on 35 and 11 country-years —
hints at that depth, not findings.

**The second slice: diffusion and materials (third run, 2026-11-04).** The workflow's next pass landed the three
catalogs that were still outstanding: the NBER data appendix of **CHAT** (Comin and Hobijn's Cross-country Historical
Adoption of Technology panel, `raw/CHAT/`), the **USGS Data Series 140** historical mineral statistics (85 commodity
workbooks, `raw/USGS-DS140/`) and the **FRED** long physical price series (`raw/FRED-PHYSICAL/`: the all-commodity PPI
from 1913, WTI from 1946, IMF copper and iron ore from 1990). `../tools/physical_build2.py` turns them into two
feature families, every value computable at year t from data dated t or earlier:

- `diffusion_features.csv` (per country-year, the transfer function): for sixteen technologies — rail km, telegrams,
  telephones, electricity, cars, commercial vehicles, radios, TVs, mail, aviation passenger-km, ship tonnage,
  tractors, fertilizer, cellphones, computers, internet users — the per-capita log level against JST population,
  its growth per year from the latest observation in [t−5, t−2] (post-inception only: ten years after the first
  positive value, and never across a one-year log jump above 1.0, which marks the 108 unit or territory breaks the
  CHAT note warns about), and from those the median pace of adoption (`tech_growth_3y`), its change against three
  to five years earlier (`tech_accel_3y`, the S-curve position), the fastest technology's pace (`tech_max_growth_3y`,
  the era's lead technology), the median distance to the JST-18 frontier (`tech_frontier_gap`, 0 for the leader),
  the percentile rank of the pace in the cross-section (`rank_tech_growth_3y`, the relative diffusion race), the four
  long lead series on their own (rail, electricity, cars, telephones) and electricity per tonne of fossil CO2
  (`elec_per_co2_growth_3y`: how much of the energy flow becomes the highest-grade carrier). `tech_n` records how many
  technologies the medians rest on and is kept out of the learner, because it grows with the calendar and falls to
  zero after 2003 — a clock, not a state. The panel thins out after 1993 and ends in 2003; nothing is filled.
- `materials_features.csv` (per year, global at t, the mining problem): across a base-metal basket — copper, lead,
  zinc, tin, nickel, aluminum, iron ore — the median log change of the real unit value (USGS's 1998-dollar series)
  over one and three years, the median of the real price against its own history to t (`metals_real_price_anom`,
  the scarcity signal: the price the mining problem is clearing at), the median world-production growth (basket plus
  pig iron) and its three-year acceleration, gold's real three-year change, and the all-commodity PPI deflated by the
  JST US CPI over one and three years. `usgs_extract.csv` holds the basket series as parsed; the workbook, sheet and
  column each came from are in `physical_build2.provenance.json`.

The features read correctly at the known episodes: US per-capita rail growth 8.9%/yr in 1872, 5.2% in 1873, 0.3% by
1875, and 5.8% in 1883 down to 0.4% in 1893; Germany 6.9%/yr in 1873; US car growth 32%/yr in 1915, 18% in 1920, 5.6%
in 1929, −5.5% in 1932; Japan the fastest diffuser in the cross-section in 1960 (rank 1.0) with its frontier gap
closing from −2.9 (1900) to −1.2 (1989); the metals basket 58% below its three-years-earlier real price in 1920 and 42%
below its own history, world metal production −15%/yr through 1932, the basket 40% above its history in 1974 and 2007
and 60% above in 2011; gold's real price +85% over 1970–73 and +111% over 1977–80.

Added to the walk-forward learners like-for-like (`../analogs/learner_test_physical_*_era.md`; the comparison row is
the oil run, 66 features, reproduced exactly by `learner_test_physical_era.md`), with a new era split in the report
(AUC for queries before 2004 and from 2004, because the later window is dominated by one synchronized episode):

| within 3 years (AUC, best learner) | energy + oil | + diffusion (10) | + materials (8) | + both |
|---|---|---|---|---|
| real equity drawdown ≥ 30% | **0.76** trees | 0.74 | 0.75 | 0.72 |
| credit contraction ≥ 5 pp of GDP | **0.68** ensemble | 0.68 | 0.68 | 0.67 |
| real GDP per capita fall ≥ 5% | **0.68** logit | 0.69 | 0.62 (0.65 k-NN) | 0.63 (0.65 k-NN) |
| unemployment spike ≥ 3 pp | **0.68** trees | 0.67 | 0.67 | 0.65 |
| JST crisis label | 0.63 trees | 0.58 | **0.66** logit (0.64 trees; 0.63 before 2004) | 0.63 |

Reading, family by family:

- **Diffusion adds no skill at this horizon.** Where the panel exists (queries before 2004) every target is within
  ±0.03 of the baseline at its best learner, mostly a little down; on the label the trees fall from 0.63 to 0.58
  overall, and the era split shows why — 0.63 → 0.62 before 2004 but 0.62 → 0.35 from 2004, when every diffusion
  column is missing for every country and the trees route those rows down branches they learned from early-era and
  small-country gaps. The family is neutral where it exists and harmful where it does not, which is a data-coverage
  result, not a mechanism result: the S-curve story (lead-technology capacity outrunning demand near the inflection)
  is not visible to a learner at three years from aggregate adoption rates. The one hint is on the mile-marker ladder:
  after a high loans/GDP at T−3 and a flat-or-falling real equity market at T−1, slow diffusion at T lifts the
  contraction rate from 42% to 54% (n = 69), the same reading before and after 1950. The pooled single-feature
  screen also says rail growth per capita separates labelled crises (0.66) — the railway manias — but the learner
  already has the credit variables that financed them.
- **Materials move the crisis label — mostly through one call — and cost the logit elsewhere.** The label's logit
  goes 0.58 → 0.66 (k-NN 0.58 → 0.61, trees 0.63 → 0.64), the largest move the label has shown in any test here, with
  the metals anomaly, the real oil price and the real commodity PPI change among the heaviest weights. The era split
  decomposes it: 0.59 → 0.63 on queries before 2004, and 0.58 → 0.89 from 2004 — the 2006–07 commodity boom (metals
  40% above their history, the real commodity PPI up 7% over three years, real oil at its highest since 1981) made the model score 2005–07 as
  pre-crisis years across the panel, and the 2007–08 wave then supplied all 39 of that window's positive country-years. That was a legitimate
  walk-forward call with information available at the time, but it is one event, and the +0.04 before 2004 is the
  part that rests on many. Elsewhere the drawdown logit falls 0.60 → 0.52 and the GDP-fall logit 0.68 → 0.62 while the
  trees barely move (0.76 → 0.75, 0.63 → 0.62), and the weights show the cause: the materials columns are the same for
  every country in a year, so a linear model with eight of them can fit the era — world production acceleration
  −1.3 and the commodity PPI +1.0 on the GDP fall, collinear with each other and with the metals anomaly — and that
  fit does not carry forward. A global-at-t family has in effect about 120 independent observations, not 2,600, so its
  skill estimates are noisier and its risk of learning the calendar higher. On the ladders the materials rungs do
  what the shock channel predicts: the drawdown rate climbs 12% → 20% → 28% → 37% as the metals anomaly, the real
  commodity PPI change and a low r−g arrive (n = 144), and the GDP fall 11% → 16% → 20% → 28% as a commodity-price
  boom, a world production deceleration and a high loans/GDP line up (n = 72) — both ladders steeper before 1950
  than after.
- **Together they do not stack.** All three families (84 features) land at or below the oil run on every target:
  the dilution that the k-NN showed on the first slice now shows on the weighted learners too.

The era split carries a warning for every number measured on the last window: from 2004 the drawdown AUC is 0.8–0.9 and
the contraction 0.7–0.8 for every learner except the within-year rank ensemble (which by construction cannot see a year
that is bad everywhere), because the 2008 wave hit nearly every country at once with one credit-boom
signature — 41 drawdowns and 73 contractions that are one event, not 41 and 73 — while the GDP-fall logit is 0.35 on
that window, anti-predicting 2009 and 2020, which were shocks from outside the state vector. Skill measured on the
full panel is mostly pre-2004 skill, and that is the honest number.

Read against the cadence noise band (`../analogs/noise_band.md`: mean range 0.031 for the logit and 0.025 for the trees,
single cells up to 0.07): the oil price's GDP-fall gain (+0.08, logit) clears it, its drawdown gain (+0.03, trees) sits
at the band's edge and rests on the top-decile lift (40% against 14%), the materials label move (+0.08, logit) clears
it but is the 2008 call, and every diffusion and measured-energy difference sits inside it.

**Jacks's world commodity panel (fifth run, 2026-11-06).** The February 2026 edition arrived by hand: 42 real commodity
prices, 1850–2025 (deflated by the US CPI, 1900 = 100), in seven groups from animal products to precious metals.
`physical_build2.py` turns it into `jacks_features.csv`: an equal-weight index chained from 1850 (log changes over
one and three years, and the index against its own history), the breadth and dispersion of three-year changes
across the 42, the energy, metals and grains groups, and grown-minus-in-the-ground. It reads the record as the
record is: breadth 71% and the index +29% into 1917, −42% by 1920 with metals −64%; breadth 95% and energy +67% into
1974; −27% by 1986; +43% into 2008 with metals +52%; energy +82% into 2022 and −81% by 2025.

As nine learner columns (`../analogs/learner_test_physical_jacks_era.md`) it does what the USGS basket did, more
strongly: the GDP-fall logit drops 0.68 → 0.59 (0.73 → 0.63 before 2004) and the trees 0.63 → 0.58, both beyond the
band; the label logit 0.58 → 0.55 overall while reaching 0.81 from 2004 — the 2008 call once more; the drawdown,
contraction and unemployment scores stay inside the band. With the USGS basket as well (17 global columns) the
GDP-fall logit is at 0.53. The weights show the mechanism: the index's three-year change takes +1.3 on the GDP fall
and −1.7 on the label beside breadth at +1.1, collinear columns with opposite signs — a linear learner reading the
calendar off a global series. Three global-at-t families have now given the same answer.

On the mile-marker ladders the panel earns its place: after a high loans/GDP at T−3 and a flat equity market at
T−1, a **real commodity bust at T** (the equal-weight index down 15% or more over three years) lifts the credit
contraction rate from 42% to 62% (n = 53; 69% before 1950, 60% after); a **broad commodity boom at T** (two-thirds of
the 42 up over three years) lifts the drawdown rate from 12% to 26%, to 38% with a low r−g and to 84% with a low
dividend yield beside it (n = 25, 89% after 1950); and the boom rung reads 16% → 18% → 22% on the GDP fall with the
credit and house rungs (47% before 1950). A measured conditional rate on a global signal is the form that survives;
nine weights on it are not.

What the second slice settles: the oil price stays the physical feature that earns its place; materials add a view
of the label and of the shock channel at the cost of a linear learner's stability (the trees are the right learner
for global features); diffusion, as aggregate adoption rates, is not a three-year forecasting feature and would need
the panel extended past 2003 (electricity from OWID's energy data, telephones and internet from the ITU, vehicles
from the WDI) before it could be retested on the only window with the later episodes. With the `EIA_API_KEY`
secret set, the next workflow run landed the EIA Total Energy series and the feed's own `eia` spot-price source, and
the manifest's error list is empty; the run after landed the EIA 1635–1945 table (parsed and cataloged above: the CO2 proxy's pre-1900 bias is now
measured), and the run after that the European series from Mendeley (below). The Jacks commodity panel timed out
from the Actions runner on every run (the author's site does not answer cloud addresses), so the scheduled pull now
leaves it out — a yearly dataset is not worth a daily timeout — and it runs from a desktop once:
`python3 history/tools/physical_pull.py --only jacks`, or the openICPSR deposit (free login) attached by hand. The
same pass put the slow annual catalogs (CHAT, USGS, KMW, the EIA 1635–1945 table) on a 30-day refresh, which takes
about ten minutes off each scheduled run.

**The European series and the proxy (fourth run, 2026-11-06).** With measured energy for eight countries from 1800,
the CO2 proxy can be calibrated country by country at three-year spans — and it is a different proxy in different
places:

| 3-year growth, CO2 (OWID) against the KMW fuels total | 1873–99 | 1900–39 | 1946–64 |
|---|---|---|---|
| GBR, DEU, FRA (coal economies): correlation / bias, pp a year | 0.53–0.98 / −0.2 to +0.8 | 0.90–0.99 / +0.1 to +0.2 | 0.73–0.95 / −0.4 to +1.9 |
| SWE, NLD, ITA, ESP, PRT (wood, hydro, late coal): correlation / bias | 0.11–0.87 / +1.4 to +17 | 0.67–0.93 / +0.5 to +1.6 | 0.23–0.98 / +0.1 to +14 |

Against fossil energy alone the proxy is near-exact almost everywhere (correlation 0.9–1.0, bias within ±0.3 pp except
post-war Italy and pre-1900 Portugal, where the fossil series starts from almost nothing). The bias against total
fuels is the share of energy the proxy cannot see: wood and hydro. Sweden's CO2 growth overstates its energy growth
by 4.5 pp a year before 1900 and 6.8 pp in 1946–64 (hydro); Italy's by 4.9 pp before 1900 and 13.6 pp in 1946–64 (the
miracle years ran on hydro and imported oil from a low base); Portugal's pre-1900 figure (17 pp, correlation 0.16) says
the CO2 series there is too small to carry a growth rate at all. For the coal economies the proxy was always fine.

Swapped into the learners like-for-like (`../analogs/learner_test_physical_measured_era.md`: the footprint gap and
its anomaly from measured energy on 1,723 rows, the proxy on the rest), **nothing moves**: every target, every learner
and both eras are within ±0.01 of the proxy-everywhere run (drawdown 0.76, contraction 0.69, GDP fall 0.68,
unemployment 0.67, label 0.63 at their best learners). The gap pair is not where the physical signal lives — the oil
price, fuel self-sufficiency and the fuel shares are the physical weights in both fits — and the anomaly form had
already taken out the proxy's slow bias. So the measured series change the ledger's numbers, not the forecast: the
right value now sits in the record for 1,723 country-years, with its source beside it, and the proxy's error is a
measured quantity rather than an assumption.

## Rebuild

```
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/co2-data    /path/owid/co2-data
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/energy-data /path/owid/energy-data
python3 -I history/tools/physical_build.py /path/owid/co2-data /path/owid/energy-data
python3 -I history/tools/physical_build2.py          # CHAT, USGS DS140 and FRED PPIACO from raw/ (pulled by the workflow)
python3 -I history/tools/learner_test.py --physical --diffusion --materials --no-horizon --era-split 2004 --tag _era
```
