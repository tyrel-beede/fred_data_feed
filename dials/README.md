# dials/ — sub-skill outputs for the macro-dials orchestrator

The scheduled sub-skills (`dials-voices`, `dials-gather`) write here; `/macro-dials` reads here. Nothing in this folder is state: it is dated evidence, and the orchestrator decides what it means.

```
dials/
  config.json              roster, schedules, group tolerances, queries, tickers — the one place cadence lives
  _status_<group>.json     one object per group: last_run_at, last_as_of, last_file, status, error
  voices/YYYY-MM-DD.json   N5 arguments + N6 roster positions (dials-voices)
  consensus/YYYY-MM-DD.json  N3/N4 pages (dials-voices)
  flows/YYYY-MM-DD.json    P-groups gathered that day (dials-gather)
  calendar/YYYY-MM-DD.json P8 issuance, IPO calendar, verified event dates (dials-gather)
  events/YYYY-MM-DD.json   raw date-gated hits for the event sweep (dials-gather)
```

## Output file schema (every group)

```json
{
  "group": "voices",
  "run_at": "2026-11-06T05:02:00-07:00",
  "skill": "dials-voices",
  "config_version": "2026-11-03",
  "status": "ok | partial | failed",
  "error": "",
  "items": [
    {
      "key": "dalio",
      "as_of": "2026-10-13",
      "title": "...",
      "url": "...",
      "position": "one or two sentences, in the voice's own framing",
      "sign": "bear-bonds | bull | bear | neutral | n/a",
      "numbers": [{"claim": "bills ~50% of issuance", "checkable_against": "FiscalData MSPD"}],
      "conversion": false,
      "fetched_how": "WebFetch | search-surfaced | secondary coverage"
    }
  ]
}
```

**Fixed item keys.** Every item has `kind`, `as_of`, `name`, `source`, `url`, `fetched_how`, `status` (ok / quiet / unreachable / paywalled). By kind: `voice` and `argument` add `position`, `sign`, `numbers`, `conversion`; `reading` (flow groups) adds `series`, `value`, `unit`, `period_end`; `deal` adds `issuer`, `size`, `tranches`, `spread_vs_ipt`, `book`; `ipo` adds `size`, `priced`; `event_date` adds `ticker_or_release`, `datetime`, `verified` (true only from IR / SEC / the agency); `hit` adds `headline`, `candidate_dial`, `late`. The orchestrator drops an item without `kind` and `as_of`.

Items carry their own `as_of` (publication or data date), never the run date. A page that could not be read is an item with `status: "unreachable"` rather than an omission, so the orchestrator can tell a quiet week from a failed fetch.

## Status file schema

```json
{ "group": "P4_cftc", "last_run_at": "...", "last_as_of": "2026-11-03", "last_file": "dials/flows/2026-11-07.json", "status": "ok", "error": "" }
```

## The freshness gate (applied by the orchestrator)

For each group, with `tolerance_days` from `config.json`:

- **fresh** — `last_as_of` within tolerance of the run → used as the reading
- **carried** — a good file exists but is older → used, as-of date printed, named in the run line
- **missing** — nothing good within 2 × tolerance → the orchestrator fetches it itself or labels the group unmeasured

A group that fails two scheduled runs running is reported to the user with its error string.

## Rules

1. Sub-skills write only to this folder. They never edit the memory files — only the orchestrator writes state.
2. One commit per sub-skill run: `dials: <groups> <date>`.
3. Nothing here is scored. Hits are hits; the likelihood ratios live in the orchestrator.
