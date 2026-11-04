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
- `catalog.json` — the catalog of long-running physical series: what is pulled, what the workflow can retrieve by URL,
  and what has to be supplied as a file (the pre-1965 European energy consumption series, the Jacks commodity panel,
  ore-grade compilations).

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

Not yet landed: the NBER data appendix for CHAT returned 504 then 503 (the workflow retries on its schedule; the file
can also be supplied), and the `EIA_API_KEY` secret is not set in the repository, so the EIA pull and the feed's own
`eia` source are skipping.

## Rebuild

```
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/co2-data    /path/owid/co2-data
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/energy-data /path/owid/energy-data
python3 -I history/tools/physical_build.py /path/owid/co2-data /path/owid/energy-data
```
