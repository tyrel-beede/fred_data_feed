# The dials feed — state in the repository, runs on a schedule

*Design, 2026-11-06. Status: proposed. Nothing below is built until the steps in §7 are done; the skills keep their current behaviour until then.*

## 1. What this changes and why

Today the gatherers (`dials-gather`, `dials-voices`) write dated evidence to `dials/` on a schedule, and the scorers (`macro-dials`, `standoff-watch`, `macro-column`) run by hand and keep their state in the memory files. That split exists because the memory files have one writer at a time: two unattended sessions editing `/areas/macro-dials.md` in the same hour would collide, and the loser would have to merge blind.

The fix is not to schedule the scorers more carefully; it is to move the state they write out of memory and into the repository, where every run is a folder that is written once and never edited. Then:

- a scheduled run of `standoff-watch → macro-dials → macro-column` is one session, one writer, one commit per stage — no collision is possible;
- what the system gathered, what it read, what it projected and how each projection scored are all on disk with a commit SHA, which is the "known past" the history layer and the tree-of-cones rulings need;
- the column can be posted to the site from the same run, because the run folder is its source;
- the site can show the scoreboard — weights over time, the ledger, the Brier — built from the folders, which is the open-ecosystem loop the site was set up for.

Memory keeps what it is good for: the user's own intent — `[stated]` rulings, overrides, roster decisions — and a pointer to the latest run. Machine state (readings, ledgers, logs, registers) lives in the repo and memory never carries a copy of it again.

## 2. Layout

```
dials/
  config.json                 roster, schedules, group tolerances, queries, tickers   (exists)
  README.md                   output contract for the gatherers                       (exists)
  FEED.md                     this document
  rulings.md                  the human-edited rulings and overrides (mirrored from memory; see §5)

  voices/  consensus/  flows/  calendar/  events/  standoff/      gatherer outputs, dated   (exist)
  _status_<group>.json        per-group freshness                                      (exist)

  runs/<RUN_ID>/              one folder per scorer run; written once, never edited
    run.json                  header — see §3
    inputs.json               manifest of every input read: path, commit SHA, as_of, gate label
    readings.json             Part I as data: fields, events scored, lenses, flows, discourse, stage, games
    spec.json                 the cone spec handed to cone.py
    cone.json                 cone.py's output: medians, bands, P(conf), state label, per-item table
    forecasts.json            forks registered this run (id, p, criterion, resolves, lead_days, depth,
                              implied p|target / p|rest) and forks resolved this run (id, outcome, Brier, log score)
    report.md                 the run's Part I / Part II text as published to the user
    export.json               (standoff runs) the export block macro-dials reads

  state/                      materialized views, rebuilt from runs/ by tools/materialize.py — never hand-edited
    ledger.json               every forecast ever registered, with its resolution if any
    scoreboard.json           rolling Brier and log score by horizon and by lead-time bucket
    register.json             the fetch register: last_fetched / last_as_of / status per group
    weights.csv               run_id, run_at, kind, H2_A, H2_B, H2_C, H2_B_q25, H2_B_q75, H3_…, state, s2, s3
    fields.csv                one row per run: the field log line as columns
    lens.csv  flows.csv  discourse.csv  cone.csv  standoff.csv
    latest.json               run_id and run_at of the latest run of each kind (what a skill reads first)

  column/<RUN_ID>.md          the column as written, with its frontmatter (also pushed to the site)

  tools/
    materialize.py            rebuild state/ from runs/ (deterministic; run after every scorer commit)
    post_column.py            copy column/<RUN_ID>.md into the macrodials repo as a blog post and push
    migrate_memory.py         one-time: seed runs/ and state/ from the memory files' logs (§7, step 1)
```

`RUN_ID` is `<YYYY-MM-DD>T<HHMM>-<kind>` in America/Boise, kinds `dials`, `standoff`, `column`, with `-event` or `-lite` suffixed when not a full run — `2026-11-07T0610-dials`, `2026-11-07T0545-standoff`, `2026-11-07T0700-column`.

## 3. The run header and the two timestamps

```json
{
  "run_id": "2026-11-07T0610-dials",
  "kind": "dials", "mode": "full",
  "run_at": "2026-11-07T06:10:00-07:00",
  "skill_version": "<sha of the SKILL.md the run used, if known>",
  "repo_commit": "<SHA of main at clone time>",
  "inputs_commit": "<SHA after the gatherers' last commit>",
  "state_prev": {"run_id": "2026-11-02T1935-dials", "label": "TRANSITION"},
  "status": "ok | partial | failed", "error": ""
}
```

Every reading and every event in `readings.json` carries two times: `event_time` (when the thing happened or the observation is for) and `observed_time` (when this system first read it), plus `source_node` (the file or page it came from). That is the bitemporal record ruling (n) and the tree-of-cones proposal ask for: a late print scores late without rewriting what was known when, and the resolved ledger reads as the node's known past.

## 4. The scheduled sequence

One scheduled task, **`dials-weekly`**, Saturday 06:10 MT (after the 05:10 gather has landed), running three skills in sequence in a single session so ordering and state sanity are guaranteed by construction:

1. **`standoff-watch`** — reads `dials/standoff/` and `state/latest.json`, writes `runs/<id>-standoff/` with its `export.json`, commits.
2. **`macro-dials`** — reads every `_status_*.json` through the gate, the standoff export from step 1, `state/ledger.json` for the open forecasts, `dials/rulings.md` for the rulings; writes `runs/<id>-dials/`, runs `materialize.py`, commits.
3. **`macro-column`** — reads `runs/<id>-dials/` (report, weights, forecasts), writes `column/<id>.md` and runs `post_column.py`, which commits the post to `tyrel-beede/macrodials` under `docs/blog/posts/` (the Pages workflow builds it) and commits the column copy here.
4. One `SendUserMessage` with the run ids, the weights line, the regime pair, anything carried or missing, and the post URL.

If a stage fails, the later stages do not run on stale inputs: `macro-dials` refuses to start if the standoff export is older than the previous dials run and the standoff stage reported `failed` (it carries the last export, labeled, if the stage was merely `partial`); the column refuses to write if the dials stage failed. The task reports what stopped and why.

Hands-off version: the weekly task only; event-mode and lite runs stay manual and write the same run folders. Micromanager version: a second task midweek (Wednesday, lite mode, no column) once the weekly one has run clean for a month, and the column posted as a pull request on the site repo for review instead of straight to `main`.

**Posting the column.** Default: push to `main` on the site, with the post carrying its `run_id` and a "generated from run …" stamp in the release-stamp line, so a bad week is one revert. The alternative — a PR you merge — costs you a click every Saturday and is the right setting if the first few generated columns need editing; the choice is one line in `config.json` (`column.post_mode: "push" | "pr"`).

## 5. What memory still holds

- `/areas/macro-dials.md` and `/areas/standoff-watch.md` keep the **Overrides and rulings** sections — user intent, `[stated]` lines — and a **pointer** line: latest run id, weights, regime pair, Brier. The game positions, projection ledger, field zones and run log sections go; they are `state/` now.
- `dials/rulings.md` in the repo is the machine-readable copy of the rulings, with each ruling's id, date and text. A rule the user states in chat is written to memory *and* to `rulings.md` in the same attended turn; scheduled runs read only `rulings.md`, so they never need the memory tools. Drift between the two is caught by the attended run that reads both.
- `/areas/macro-dials-log.md` is retired once `state/*.csv` holds its lines (step 1 migrates them); the voices roster is already in `config.json`.
- `/areas/macro-column.md` keeps the column's standing editorial rules; the column log and the pig ledger move to `state/` as part of the column run folder.

## 6. What the site gets

A **Forecasts** section built at site build time from `state/` (the same pattern as the model tables: image plus a selectable text version): the weights-over-time chart with the IQR band, the regime pair over time, the open-forecast table with lead days, the resolved ledger and the rolling Brier by lead-time bucket. The column posts link to the run folder they were written from, so a reader can open the readings behind any sentence. This is the scoreboard the contribution loop needs; reader dial settings from the model page, when that interface exists, land in the same feed as another input kind.

## 7. Build order

1. `tools/migrate_memory.py` — one-time seed of `runs/` (one folder per logged run, from the run lines) and `state/` (ledger, weights, the five CSV logs, register) from the two memory files. Checked against the memory text line by line before anything is deleted from memory.
2. `tools/materialize.py` with a test that rebuilding `state/` from `runs/` reproduces the seeded files byte for byte.
3. `macro-dials` revision: step 1 reads `state/latest.json`, `state/ledger.json`, `dials/rulings.md` (memory only when attended, for `[stated]` changes); step 12 writes the run folder, runs `materialize.py`, commits; the lite/event modes write folders too. Memory write reduced to the pointer line, attended runs only.
4. `standoff-watch` revision on the same pattern; `export.json` replaces the export line.
5. `macro-column` revision: input is a run folder; output is `column/<id>.md`; `tools/post_column.py` posts it (`make_post.py` on the site already builds a post from a markdown source).
6. The `dials-weekly` scheduled task, first firing as a one-shot test on a Saturday with the column in `pr` mode.
7. The site's Forecasts section from `state/`.

Steps 1–2 are a few hours and reversible (memory is untouched until step 3 is saved). Step 3 is the one that changes behaviour; it is proposed as a skill card and saved by you. The weekly task exists only after 6.

**Status (2026-11-06).** Steps 1–2 done (commit 69cbc42: 15 run folders seeded, `state/` reproducible, Brier 0.121 n=12 reproduced). Step 3 proposed as a skill card (saved by the user). Step 4 saved. Step 5: `tools/post_column.py` built (verified against the site's strict build) and the `macro-column` card proposed; `state/pigs.json` added to the materializer. Step 6: the `dials-weekly` scheduled task exists (Sat 06:10 MT) with a precondition guard — it stops and reports, writing nothing, if `main` lacks the feed tools or any of the three skills is still the memory-writing version — so its first firing is the one-shot test. Step 7 done on the site (`tools/forecasts.py`, the Forecasts page, a Saturday 15:30 UTC rebuild after the sequence). Remaining: merge this branch; a ruleset on the site repository; retire `/areas/macro-dials-log.md` once the pointer-line model is in use.

## 8. Invariants (the rules the tools enforce)

- A run folder is written once. Corrections are new runs with `supersedes: <run_id>` in the header; nothing is edited in place.
- `state/` is derived. `materialize.py` must reproduce it from `runs/`; if it cannot, the run that broke it is the bug.
- Gatherers write only under their group folders; scorers write only under `runs/`, `state/` and `column/`; `config.json` and `rulings.md` are edited by the user or by an attended run on a `[stated]` instruction.
- Every number in a run carries `event_time`, `observed_time` and `source_node`.
- The sequence never scores on an input it cannot date; a missing gate input is fetched or labeled unmeasured, as the skills already say.
