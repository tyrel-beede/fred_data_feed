# The corporate layer

Corporate-sector records, in two parts with different depths and different jobs:

- **Long-record anchors for the history layer** (US only): the Federal Reserve's Financial Accounts (Z.1) for the
  nonfinancial corporate sector from 1945, BEA corporate profits from 1929, Shiller's stock-market series from 1871,
  and the Goyal–Welch predictor workbook (net equity issuance, book-to-market, the default spread) from 1871. These
  are compiled national aggregates: the counted side of the sector, consistent for decades, the corporate analogue of
  the JST panel's bank variables.
- **The modern micro layer for the bridge and the live cone**: the SEC's Financial Statement Data Sets (every number in
  10-K/10-Q XBRL statements, quarterly since 2009) and Form 13F Data Sets (institutional holdings, quarterly since
  2013). These are *counted* in the ledger's sense — self-reported, audited, lagged a quarter (13-F: 45 days,
  long-only, $100M+ managers) — and one era deep, so they feed the live dials' capital/capex and positioning groups,
  not the climatology. The quarterly zips run to hundreds of megabytes, so `../tools/corporate_pull.py` streams them in
  the workflow and keeps only aggregates (sums, medians and filer counts per tag; concentration and crowding
  summaries per quarter); the zips themselves are hashed in the manifest and not kept.

## What is here

- `catalog.json` — the entries, their status (pulled / planned / attach), retrieval route, license and provenance class.
- `raw/` — what the workflow fetched, with `manifest.json` (URL, size, SHA-256, time, and for the FRED series the
  resolved id, title, units and frequency in `raw/FRED-Z1/series_used.json`; the puller resolves each series by its
  exact FRED title at run time rather than trusting a remembered id).
- `sec_fsds_quarterly.csv`, `sec_13f_quarterly.csv` — the SEC aggregates reduced to two tables for the live dials (built
  by `../tools/corporate_build.py` from `raw/SEC-FSDS/` and `raw/SEC-13F/`): per sector (all filers; nonfinancial and
  financial by SIC, from aggregator v3), period end and tag, the filer count, sum, median and 90th percentile for the
  3-month, year-to-date and annual rows (10-Q cash-flow statements are year-to-date, so a single quarter's flow is
  the difference between successive rows), from the quarterly file with the most filers reporting it, with the file
  and the aggregator version that produced it; and per 13F set, the holdings date, filers, total value in dollars,
  issuers, top-10 and top-50 issuer shares, Herfindahl, the median filer's top-10 concentration, the put/call share,
  and (v2) how many filers reported in the other unit and how many filings for other periods were set aside. The
  record: 71 financial-statement quarters 2009q1–2026q3 and the 13F sets from 2013q2 (54 published; one window
  pending). First readings: 9,361 filers reporting $71 trillion for the quarter ended December 2025 and 9,711
  reporting $82 trillion for March 2026, the ten largest issuers 24% and 23% of the total, the median filer with
  54% of its value in its ten largest positions; capital expenditures of $249 billion across 2,325 filers in the
  March 2026 quarter against buybacks of $263 billion across 1,402 and operating cash flow of $407 billion across
  4,327 (all filers; the nonfinancial figures follow the v3 re-reduction).
- `sec_analysis.md`, `sec_analysis.json` — the layer read over its record by `../tools/sec_analysis.py`: the annual
  cash flows of the December-fiscal-year filers 2009–2025 and the ratios between them (capex, buybacks and dividends
  to operating cash flow, payout to net income, capex to depreciation, cash, leverage) with the latest year's
  percentile in the record; December-31 balance sheets with each year's sum checked against the 10-K file's; the
  timely read (the latest year-to-date flows against a year earlier, filer counts beside each sum); calibration of
  the capex, dividend and net-income sums against Z.1 and NIPA (coverage and growth correlation); the 13F
  concentration series with the latest reading's percentiles and each period's status (current, provisional,
  stale); and a consistency section laying the same period's sum from every file side by side.
- `raw/SEC-FSDS/<q>_meta.json` (v3) and the `aggregator_version` field in every 13F summary — what each reduction
  did: filings and amendments counted, filers by sector, values set aside beyond the plausibility caps, the five
  largest filers per large tag-period; for 13F the report period, the filings used and set aside, the set's unit and
  the filers rescaled. `../tools/tests/test_sec_aggregators.py` runs both aggregators on synthetic sets (also
  `corporate_pull.py --selftest`; `qc.py` runs it).
- `us_corporate_annual.csv` — built by `../tools/corporate_build.py`, one row per year, every value computable at year
  end (balance-sheet levels at Q4, flows as annual averages of the quarterly series, nominal GDP from FRED from 1947
  and the JST sheet before): nonfinancial corporate debt/GDP, equity market value/GDP, net worth growth over three
  years, capital expenditures/GDP, net dividends/profits after tax, liquid assets/debt, NIPA corporate profits before
  tax/GDP (1929–), and from Shiller's workbook when present the December CAPE, real earnings growth over one and
  three years, real price growth over three years and the earnings yield less the long rate; from the Goyal–Welch
  workbook when present net equity issuance, book-to-market, the default yield spread and stock variance.
  `us_corporate_annual.provenance.json` records the series behind each column and the coverage.

## What it is for

The history layer's learners run on an 18-country panel; a US-only family would let a learner identify the country
by what is missing, so these series are **not** learner features. Their place is (1) the US query vector in the bridge
— the live state the analogs are retrieved for — and (2) the Dalio-style reads about the corporate sector
(leverage, payout, cash, valuation) that the voice ledger scores, now against a counted record rather than a
narrative one. The SEC aggregates give the live dials a quarterly read of capex, buybacks, dividends and cash against
revenue and debt across all filers, and a crowding read (how concentrated institutional holdings are, which issuers
are most held) beside the CFTC, EPFR, ICI, AAII and margin series the positioning group already carries.

## Provenance notes

- Z.1 levels are market value for equities and book-ish for debt; the sector is nonfinancial corporate business,
  which leaves out banks, insurers and non-corporate business. Profits series differ in concept (before/after tax,
  with and without IVA and CCAdj): the title of the series used is recorded beside its id.
- Shiller's earnings and dividends are the S&P composite's reported aggregates (Cowles back to 1871); CAPE uses
  ten-year real earnings. The copy the Yale server still serves (`raw/SHILLER/ie_data_yale.xls`) was last updated in
  September 2023; the current workbook lives on shillerdata.com behind a page the puller cannot read a link from. A
  hand-downloaded `ie_data.xls` placed beside it takes precedence in the builder. The last resort in the puller is
  datahub.io's scripted mirror of the same workbook, flagged `MIRROR` in the manifest.
- Goyal–Welch is distributed from Amit Goyal's page as a Drive-hosted workbook that the puller may not be able to
  resolve; when it cannot, the workbook goes under `raw/GOYAL-WELCH/` by hand (`the predictor workbook (PredictorData<year>.xlsx or Data<year>.xlsx)`).
- SEC 13F `VALUE` changed unit with the filings made from January 2023 (dollars; thousands before), and filers did
  not all follow the form: inside a thousands-era set a few hundred report in dollars. The first aggregator scaled
  each set by its majority unit and so multiplied those filers a thousandfold (totals of $300–480 trillion before
  2023, trillion-dollar single positions, the median filer's concentration a thousand times too small — found in
  the quality-control pass of 2026-11-07). Aggregator v2 detects the unit per filer: every line's value over its
  shares (or principal) is an implied price; the set's unit comes from the median implied price of its share lines
  (below $1 means thousands); each issuer's reference is the median across the filers holding it; a filer whose
  lines sit a thousandfold above or below their references reports in the other unit; everything is scaled to
  dollars line by line before aggregation (`value_unit_set`, `n_filers_unit_corrected`,
  `value_share_unit_corrected`). A data set holds the filings *made* in its quarter, mostly reports for the quarter
  that ended just before it: v2 counts only the holdings reports for the set's own report period (the modal
  `REPORTCALENDARORQUARTER`), takes per filer the latest of its original and restatements plus its new-holdings
  amendments, sets notices and late reports for earlier periods aside, and records `report_period`; the quarterly
  table's `period_end` is that date (for older summaries, the quarter the set's name implies). Summaries from the
  first aggregator are version 1 and, for the thousands era, known wrong; `qc.py` fails until they are re-reduced
  (`--only 13f --all --redo` from a desktop; the zips are fetched again, nothing large is kept).
- The financial-statement sums are sensitive in two ways the first reduction did not control. The same
  December-31 figure appears in the 10-K file and again as a comparative in later 10-Q files, and the sums differ —
  by up to 2.1× for 2025 assets (`sec_analysis.md` section 7 lays them side by side); and all-filer operating cash
  flow swings with the banks' and brokers' trading books. Aggregator v3 keys values by filer (CIK) rather than
  submission, taking the latest-filed submission that carries the tag (a 10-K/A replaces its original), sets
  dimensional rows aside where the set marks them, splits every sum by sector (SIC 6000–6799 financial), sets aside
  values beyond a per-tag plausibility cap (several times the largest company's; a filer's scale error) and lists
  them with the five largest filers per large key in `<q>_meta.json`. `sec_analysis.py` reads the nonfinancial
  rows where they exist and says which sector each row is. The tag set carries both the current revenue tag
  (`RevenueFromContractWithCustomerExcludingAssessedTax`, from 2018) and the earlier ones (`SalesRevenueNet`,
  `SalesRevenueGoodsNet`); `PaymentsOfDividends` and `PaymentsOfDividendsCommonStock` are kept apart (some filers
  report both); `InterestExpense` thins out after the 2023 taxonomy and is not a series. The filer population grows
  through the XBRL phase-in (large accelerated filers from 2009, all filers from mid-2011), so ratios within a
  period are the comparable quantities, levels are not.
- SEC data: public domain, under the fair-access policy (identify the client in the User-Agent, at most ten
  requests a second). **sec.gov refuses GitHub-hosted runners** (403 to every request from cloud-provider addresses,
  with or without the fair-access User-Agent), so the two SEC pulls run from a desktop:
  `SEC_CONTACT="Your Name you@example.com" python3 history/tools/corporate_pull.py --only fsds,13f` streams the two
  latest quarterly zips and writes only the aggregates under `raw/`; commit and push them, and the builder and the
  dials pick them up. The contact goes in the User-Agent, which sec.gov requires in "Name email" form (a bot-style
  agent is refused with 403 even from a home address); it is read from the environment and never written to the
  repo. `--all` backfills every set, `--redo` re-fetches and re-reduces the sets already in `raw/` after an
  aggregator change, `--selftest` runs the synthetic checks without the network. Options lines (put/call) are
  excluded from the issuer concentration. Restated financials appear as later filings; the aggregates take, per
  filer, the latest-filed submission in the set (v3) or the first value seen per submission (v1), and restatements
  in later quarters are not propagated back.
