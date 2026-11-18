# narratives/ — the narrative ledger

The layer that treats the professional discourse as the hypothesis set: each narrative circulating among the tracked voices is written down as its holders state it, its holders are counted sweep by sweep, its implied predictions are checked against the fields, forks and history the repository already carries, and the result is assembled into a bull / bear / pig baseline with no operator probability in it. Every number the model sets by judgment is catalogued beside the measured alternative in the bias log. Nothing here carries a likelihood ratio or moves a branch weight.

Read `DESIGN.md` for the reasoning, the feasibility verdicts and the integration path.

## Where things live

| path | what | written by |
|---|---|---|
| `map.json` | the narrative map: 15 narratives with sign, lane, branch, statement as held, keywords, typed predictions, falsifier, incentive tags, GDELT proxy; `dial_map` (event-sweep dial codes → narratives); `gdelt_series` | by hand (the pre-registration) |
| `tools/narratives.py` | the builder; `--check` runs its self-test; `--unassigned` prints the latest sweep's unmatched items; `--run <RUN_ID>` pins a scorer run | — |
| `ledger.json`, `ledger.md` | every narrative: holders per sweep with verbatim positions and matched words, opposed items, mentions, the holders' own number claims, GDELT and sell-side channels, event-sweep hits, each prediction's current reading, evidence tally, lifecycle, the system's weight beside the holders | the builder |
| `bandwidth.csv` | narrative × sweep: items in the sweep, holders, holder share, opposed, mentions, arguments | the builder |
| `baseline.md` | the bull, bear and pig cases; the measured dial points (fields, zones, lenses, discourse, games) | the builder |
| `bias_log.json`, `bias_log.md` | the catalogue of judgment in the model, item by item, beside the measured alternative or "none yet"; includes the orchestrator's calibration record | the builder |

## Inputs (nothing new is fetched)

`dials/voices/*.json` (the N5/N6 sweeps), `dials/consensus/*.json` (N4), `dials/events/*.json` (the event sweep), `data/gdelt/*_timelinevol.json` (N1), `dials/runs/<id>-dials/{readings,forecasts,cone}.json` (the latest scorer run) and every run's `forecasts.json`, `dials/state/{ledger,scoreboard}.json` (the resolved-fork record), `history/analogs/us_2026ytd.json` and `history/climatology/event_rates_by_era.csv` (the history layer's base rates).

## Running it

```
python3 -I narratives/tools/narratives.py --check
```

Run it after each voices sweep (or each scorer run) so `bandwidth.csv` grows. The self-test fails if a narrative has no falsifier, no typed prediction (signed narratives), or matched nothing in any sweep — the last is a map error, not a finding.

## Rules

- Holders are counted, never weighted; the ledger prints who, so a reader can weight.
- Matching is deterministic (case-insensitive, word-boundary keywords from the map; one strong or two weak); the words that matched are printed with each quote.
- A holder is a matched item whose sign agrees with the narrative's; *opposed* is a proxy (opposite sign, a strong word), not a reading of the argument.
- A prediction's "supports?" is a counted condition (a field zone, a lens sign, a resolved fork), with its direction fixed in the map before the reading is seen. Open forks print the orchestrator's registered probability, which is judgment and is in the bias log.
- The history legs are base rates for states like the present one, not forecasts.
- A narrative enters the baseline at two distinct holders in the window; the pig cut-offs are support shares of 0.34 and 0.66. These three settings are the layer's own and are listed in the bias log.
- A rule is changed prospectively, never to re-score a window already built.

## Adding a narrative

Add an entry to `map.json` with every field the others have — the statement *as its holders state it*, at least one typed prediction with its direction, a falsifier a stranger could score, and keywords that find its holders and not everyone else — then run `--check`. New narratives come from the unassigned bin: items in the latest sweep that match no narrative (`--unassigned` prints them).
