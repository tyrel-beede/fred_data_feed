# Handoff — what runs from a desktop, and how to check it in

Everything in the history layer is pulled by the scheduled workflow except four sources whose hosts refuse or cannot
be reached from GitHub-hosted runners. All four are in place as of 2026-11-06; what remains is the SEC re-reduction (first row) and the refresh cadence noted in each row. Each is optional: revision one is complete without them, and each one lands in a `raw/` folder
the builders already read. All four scripts use only the Python standard library (plus `openpyxl`
and LibreOffice for the builders, which already run in the sandbox).

| source | what to do | where it lands | what it unlocks |
|---|---|---|---|
| SEC Financial Statement Data Sets and Form 13F Data Sets | **backfilled 2026-11-06 from the owner's desktop** (`corporate_pull.py --only fsds,13f --all` with `SEC_CONTACT` set to the name and address sec.gov's fair-access policy requires; cloud addresses are refused outright): 71 financial-statement sets 2009q1–2026q3 and 53 of the 54 13F sets. **To do once — the re-reduction** (2026-11-07): the quality-control pass found the first 13F reduction wrong before 2023 (filers reporting in dollars inside thousands-era sets were multiplied a thousandfold; see `corporate/README.md`) and the financial-statement sums inflated in some 10-Q comparatives files; the aggregators were rewritten (13F v2, FSDS v3) and the old summaries cannot be corrected without the zips. From the repository root, after `git pull`: `SEC_CONTACT="…" python3 history/tools/corporate_pull.py --only 13f --all --redo` (54 sets, ~4–5 GB, 1–1.5 hours; also fetches the Jun–Aug 2026 window) and, when convenient, `SEC_CONTACT="…" python3 history/tools/corporate_pull.py --only fsds --all --redo` (71 sets, ~5 GB, about 2 hours). Both resume: every summary records the aggregator version that produced it, and `--redo` skips the sets already at the current one, so a stopped run restarts where it left off (slice with `--since 2018` to do part of it). Then `python3 -I history/tools/corporate_build.py && python3 -I history/tools/sec_analysis.py && python3 -I history/tools/qc.py` (the two SEC checks that fail by design turn green), commit `history/corporate/` and push. **Each quarter after that**: the plain `--only fsds,13f` run fetches the two newest sets of each. | `history/corporate/raw/SEC-FSDS/<yyyyqN>_aggregates.csv` + `_meta.json`, `history/corporate/raw/SEC-13F/<period>_summary.json` + `_top20.csv`; reduced by `corporate_build.py` to `corporate/sec_fsds_quarterly.csv` and `sec_13f_quarterly.csv`, read by `sec_analysis.py` | the live dials' capex/buyback/dividend/cash read across all filers (by sector from v3) and the crowding read of institutional holdings (positioning group); `corporate/sec_analysis.md` |
| Jacks real commodity prices 1850– | done 2026-11-06: the February 2026 edition (42 commodities, 1850–2025) and its chartbook are in place; `physical_build2.py` reads it into `jacks_features.csv` and the learner takes `--jacks`. To refresh (yearly): the author's page or the openICPSR deposit (doi 10.3886/E198401V1, free login), overwrite the workbook. | `history/physical/raw/JACKS-COMMODITIES/` | the world commodity panel beside the US-centred USGS basket |
| Goyal–Welch predictor workbook | done 2026-11-06: `Data2025.xlsx` (to 2025:12) is in place and read by `corporate_build.py`. To refresh (yearly): the new workbook from Amit Goyal's page, same folder. | `history/corporate/raw/GOYAL-WELCH/` | net equity issuance, book-to-market, the default spread and stock variance from 1871 in `corporate/us_corporate_annual.csv` |
| Shiller workbooks | done 2026-11-06: `ie_data.xls` (through October 2026) and `Fig3-1_1.xls` (home prices 1890–) are in place. To refresh later, download the two from shillerdata.com and overwrite them. | `history/corporate/raw/SHILLER/` | CAPE, real earnings and prices, the dividend yield and home prices for the live query and the US annual table |

After adding files, rebuild and check (each takes seconds, from the repository root):

```
python3 -I history/tools/corporate_build.py      # us_corporate_annual.csv, shiller_home_prices.csv
python3 -I history/tools/physical_build2.py      # materials (if Jacks is to be added to the basket, that is a code change: say so)
python3 -I history/tools/live_query.py --year 2026 && python3 -I history/tools/analogs.py --query history/analogs/us_2026ytd_query.json
python3 -I history/tools/sec_analysis.py         # corporate/sec_analysis.md (after an SEC pull)
python3 -I history/tools/qc.py                   # 33 checks -> history/QC.md
```

Commit the raw files, the rebuilt CSVs and `QC.md` together. The workflow's commit step adds `history/corporate/raw`
and `history/physical/raw` on its own runs and never deletes a hand-supplied file (the puller writes the stale Yale
copy of Shiller's workbook under a different name, so the current one keeps precedence).

**The revision-one tag.** Tag and release writes are refused through the sandbox's proxy (branches push; tags do
not), so the tag is yours to place: on GitHub, create a release named `history-v1` from the commit that closes the
SEC re-reduction above (the one whose `QC.md` reads 33 of 33), or from a clone `git tag -a history-v1 <commit> -m
"history layer, revision one" && git push origin history-v1`. Until that run lands, the fixed point is commit
`bb2e0fc` ("revision one: the cadence noise band…", 2026-11-06) plus the SEC work after it. Later work is compared
against the tag.

Open question for the repository owner: the repository's visibility against the "internal use only" terms on some
of the live feed's licensed sources — a judgment the tooling should not make.
