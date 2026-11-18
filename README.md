# fred_data_feed
Data from FRED

## The layers

| directory | what it is | read first |
|---|---|---|
| `data/` | the FRED, EIA and GDELT pulls the scheduled jobs refresh | `pull.py` |
| `dials/` | the macro-dials runs, gathers, state and rulings (the measurement and the cone) | `dials/README.md`, `dials/FEED.md` |
| `history/` | the history layer: 18-country macro history, the analog query, climatology, the SEC corporate tables | `history/README.md` |
| `narratives/` | the narrative ledger: the discourse as the hypothesis set, measured against the data and the record; the bull / bear / pig baseline; the bias log | `narratives/README.md`, `narratives/DESIGN.md` |
| `analysis/` | one-off analyses | — |

## Data licenses

`history/jst/` redistributes the Jordà–Schularick–Taylor Macrohistory Database (Release 6) under its own terms, Creative Commons Attribution-NonCommercial-ShareAlike 4.0, with the required citations beside the data; see `history/jst/LICENSE-JST.md`. The rest of the repository's data comes from public sources named in `history/sources.json` and the dials documentation.
