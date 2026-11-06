# Handoff — what runs from a desktop, and how to check it in

Everything in the history layer is pulled by the scheduled workflow except four sources whose hosts refuse or cannot
be reached from GitHub-hosted runners. Each is optional: revision one is complete without them, and each one lands
in a `raw/` folder the builders already read. All four scripts use only the Python standard library (plus `openpyxl`
and LibreOffice for the builders, which already run in the sandbox).

| source | what to do | where it lands | what it unlocks |
|---|---|---|---|
| SEC Financial Statement Data Sets and Form 13F Data Sets | from a clone, with Python 3: `python3 history/tools/corporate_pull.py --only fsds,13f` (sec.gov answers 403 to cloud addresses; a desktop address works; the fair-access User-Agent is set in the script). Downloads the two latest quarterly zips of each (a few hundred MB), keeps only the aggregates, discards the zips. Then `git add history/corporate/raw && git commit && git push`. | `history/corporate/raw/SEC-FSDS/<yyyyqN>_aggregates.csv`, `history/corporate/raw/SEC-13F/<period>_summary.json` and `_top20.csv`, entries in `raw/manifest.json` | the live dials' capex/buyback/dividend/cash read across all filers and the crowding read of institutional holdings (positioning group) |
| Jacks real commodity prices 1850– | `python3 history/tools/physical_pull.py --only jacks` (the author's site times out from the runner; try from a desktop). If it refuses residential addresses too: download the current workbook from the openICPSR deposit (doi 10.3886/E198401V1, free login) into the folder by hand. | `history/physical/raw/JACKS-COMMODITIES/` | a world commodity panel beside the US-centred USGS basket (the materials family's price signal) |
| Goyal–Welch predictor workbook | download `PredictorData<year>.xlsx` from Amit Goyal's page (sites.google.com/view/agoyal145) into the folder. | `history/corporate/raw/GOYAL-WELCH/` | net equity issuance, book-to-market, the default spread and stock variance from 1871 in `corporate/us_corporate_annual.csv` (read automatically by `corporate_build.py`) |
| Shiller workbooks | done 2026-11-06: `ie_data.xls` (through October 2026) and `Fig3-1_1.xls` (home prices 1890–) are in place. To refresh later, download the two from shillerdata.com and overwrite them. | `history/corporate/raw/SHILLER/` | CAPE, real earnings and prices, the dividend yield and home prices for the live query and the US annual table |

After adding files, rebuild and check (each takes seconds, from the repository root):

```
python3 -I history/tools/corporate_build.py      # us_corporate_annual.csv, shiller_home_prices.csv
python3 -I history/tools/physical_build2.py      # materials (if Jacks is to be added to the basket, that is a code change: say so)
python3 -I history/tools/live_query.py --year 2026 && python3 -I history/tools/analogs.py --query history/analogs/us_2026ytd_query.json
python3 -I history/tools/qc.py                   # 25 checks -> history/QC.md
```

Commit the raw files, the rebuilt CSVs and `QC.md` together. The workflow's commit step adds `history/corporate/raw`
and `history/physical/raw` on its own runs and never deletes a hand-supplied file (the puller writes the stale Yale
copy of Shiller's workbook under a different name, so the current one keeps precedence).

Open question for the repository owner: the repository's visibility against the "internal use only" terms on some
of the live feed's licensed sources — a judgment the tooling should not make.
