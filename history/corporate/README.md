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
- SEC data: public domain, under the fair-access policy (identify the client in the User-Agent, at most ten
  requests a second). **sec.gov refuses GitHub-hosted runners** (403 to every request from cloud-provider addresses,
  with or without the fair-access User-Agent), so the two SEC pulls run from a desktop:
  `python3 history/tools/corporate_pull.py --only fsds,13f` streams the two latest quarterly zips and writes only the
  aggregates under `raw/`; commit and push them, and the builder and the dials pick them up. 13F `VALUE` is in dollars from 2023 and in thousands before. Options lines (put/call) are
  excluded from the issuer concentration. Restated financials appear as later filings; the aggregates take the
  first value a filer reports for a tag and period.
