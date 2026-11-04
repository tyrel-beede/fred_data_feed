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

## How it is tested

`../tools/learner_test.py --physical` adds the physical features to the walk-forward learners and writes
`../analogs/learner_test_physical.md` beside the run without them, so the layer's value is a measured difference, not
an argument. The expectation stated before the run: modest gains on the activity targets from the shock channel, larger
on the financial targets from the footprint gap if it separates booms that built from booms that priced — and no
movement toward 0.85, because the physical variables are slow and the targets are fast.

## Rebuild

```
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/co2-data    /path/owid/co2-data
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/owid/energy-data /path/owid/energy-data
python3 -I history/tools/physical_build.py /path/owid/co2-data /path/owid/energy-data
```
