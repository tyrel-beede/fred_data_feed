# The narrative ledger — design, feasibility and what was built

*Written 2026-11-18 from the ask of that date: remove as many of the operator's own predictions from the model as possible, let the market's narratives supply the hypotheses, measure each narrative's bandwidth and plausibility against the data, the history and known game theory, catalogue the measured dial points, and build a bull / bear / pig baseline against which any later adjustment is a known bias.*

## 1. The ask, restated as a measurement problem

The dials system (`dials/`, the `macro-dials` skill and its two gatherers) already measures the world in five ways — event dials, fields, flows, discourse, stage — and projects a cone over three branches. The ask is not to measure more of the world; it is to change **where the hypotheses come from** and **where judgment is allowed to sit**:

1. **Hypotheses from the crowd.** Today the three branches (A grow out, B capex bust, C debt crunch), their confirmation criteria and the fork table are written by the operator. The ask is that the narratives circulating among professionals become the hypothesis set — each one written down as its holders state it, with the predictions it implies — and that the system's own branches sit beside them as three more narratives, scored the same way.
2. **Bandwidth measured, not assumed.** How many tracked voices hold a narrative, whether that number is rising, how loud the news channel is on it, whether the sell side is aligned with it — measured per sweep and kept, so growth and decay are visible.
3. **Plausibility measured against the data, the record and the games.** Each narrative's implied predictions checked against the fields the run already reads, the forks the orchestrator already registers and resolves, the history layer's base rates for states like the present one, and the incentive structure of whoever is telling it.
4. **A catalogue of the measured dial points** — the fields, zones, lenses, discourse reads and game positions as the run read them — so that there is a stated baseline, and any user-set value is a difference from it.
5. **A bull / bear / pig baseline** assembled from the above with no operator probability in it, and a **bias log** that holds every number the operator or the orchestrator set rather than measured, beside the measured alternative where one exists.

The one rule carried over unchanged from the dials: **nothing in the narrative layer carries a likelihood ratio.** The discourse was already defined as "data about the players, never data about the world"; the ledger makes that data scorable without letting it move a branch weight.

## 2. Where judgment sits in the model today (the inventory)

| component | where it is set | measured or judged | what the ledger does with it |
|---|---|---|---|
| the branch set (A/B/C) and their confirmation criteria | `macro-dials` SKILL.md, *Branches and their signatures*, *Branch weights* | judged (the author's hypothesis set) | each branch becomes a narrative in `map.json` beside the crowd's own, with the same holder count and evidence tally; the rulings file's own principle ("never assume only the named branches exist") is the warrant |
| event lines (IG 100 / 115, real 10-yr 3.0 / 2.5, claims +20%, term premium 1.0) | rulings.md ruling l; SKILL.md | judged (anchored on precedents a six-year window does not contain) | logged in the bias log beside the percentile-band zone of the same field, which is the measured alternative the rulings already define |
| likelihood-ratio tiers ×4 / ×2 / ×1.5 / ×1.2 with σ | SKILL.md, *Likelihood-ratio tiers* | judged; "revised only by the calibration record" | logged; the measured alternative does not exist yet (the skill's own queued item: Beta-binomial posterior per tier on the periphery-first episode table); the history layer's ladder rungs are the nearest measured conditional rates |
| fork probabilities (each `F-…` registration) | each run's `forecasts.json` | judged by the orchestrator, "adjustable ±10 on discourse" | logged with the orchestrator's note and read against its own calibration record by probability bucket (21 resolved forks: <0.2 → 0 of 2 fired; 0.2–0.4 → 1 of 6; 0.4–0.6 → 2 of 3; ≥0.6 → 8 of 10; mean Brier 0.139) |
| hazard monthly odds | each run's `forecasts.json` | judged ("rough per-month odds, revisited each run") | logged; no measured alternative yet |
| state-label thresholds (B ≥ 20 / 30; 0.25 / 0.75) | rulings.md ruling j | judged (a two-point calibration to two hand reads) | logged |
| the fields, zones, lenses, event scores, flows, convergence | the run | **measured** (percentile bands, hysteresis, fixed queries) | the baseline every narrative is checked against; printed in `baseline.md` as the measured dial points |
| the discourse reads N1–N6 | the gatherers and the run | **measured** (fixed instrument, date gate) | the ledger's inputs; N1 and N4 are printed beside each narrative as channels |
| the resolved-fork record | `dials/state/ledger.json`, `scoreboard.json` | **measured** | the calibration record above; the only measured check on the orchestrator's judgment so far |

So the judgment in the model is concentrated in five places — the branch set, the event lines, the LR tiers, the fork and hazard probabilities, and the state thresholds — and everything else is already mechanical. That is a smaller surface than the ask implies, and it is why the design below is a layer beside the dials rather than a rewrite of them.

## 3. The design

Five objects, one loop, three rules.

**Objects** (all under `narratives/`):

- `map.json` — the narrative map: each narrative with its id, sign (bull / bear / bear-bonds / neutral / contested / n/a), lane, the branch it feeds, a one-paragraph statement *as its holders state it*, strong and weak keywords for matching, its predictions (typed: a fork id, a fork that should *not* fire, a field condition, a history leg, a base rate, a stage line, a hazard), a falsifier, incentive tags, the GDELT series that proxies it, and the date it entered. The map is the only hand-written object, and it is written *before* the data are read: it is the pre-registration.
- `ledger.json` / `ledger.md` — built from the map and the repository: holders per sweep (verbatim positions kept, with the words that matched), opposed items, mentions, arguments, the numbers the holders put on the narrative (each with what it is checkable against), GDELT bandwidth, sell-side alignment, event-sweep hits mapped by dial code, each prediction's current reading, the evidence tally, the lifecycle label, and the system's own weight printed as one more holder.
- `bandwidth.csv` — narrative × sweep: items in the sweep, holders, holder share, opposed, mentions, arguments. The time series the growth question is asked of.
- `baseline.md` — the bull case, the bear case and the pig case assembled from the ledger with no probability assigned; the measured dial points (fields, zones, lenses, discourse, games); the entry rule; how to record a bias against it.
- `bias_log.json` / `bias_log.md` — the catalogue of judgment in §2, item by item, each beside its measured alternative or "none yet", so that a result can be split into what the data said and what the operator added.

**The loop** (deterministic, re-runnable, `python3 -I narratives/tools/narratives.py`):

gather (the existing gatherers; nothing new is fetched) → match (keywords from the map, case-insensitive, word-boundary, one strong or two weak) → bandwidth (holders / opposed / mentions per sweep; GDELT 7-day vs 90-day z; N4 ratings share) → test (field conditions against `fields_detail` and the lenses; forks against every run's `forecasts.json`; history legs against `history/analogs/us_2026ytd.json` and `history/climatology/event_rates_by_era.csv`) → baseline (rank by distinct holders in the window; entry rule two holders; pig = asymmetry between bandwidth and evidence with at least two evaluable checks) → bias overlay (the log, with the calibration record read from `dials/state/`).

**Rules:**

1. Holders are counted, never weighted. The ledger prints *who*, so a reader can weight; the system does not.
2. Nothing in the layer moves a branch weight. The system's weight is printed beside the holders as one more voice and is scored like the rest.
3. Every narrative needs a falsifier and at least one typed prediction before it enters the map (the `--check` self-test enforces both, and that every narrative matched at least one item somewhere — a narrative that matches nothing is a map error, not a finding).

## 4. Feasibility, component by component

| component | verdict | what the build found |
|---|---|---|
| narrative extraction from the sweeps | **feasible now, by map + keywords** | three sweeps (76, 58, 56 items) yield 15 narratives; 11 are held in the latest sweep; 22–32 items per sweep match nothing (housekeeping posts, paywalled teasers, off-topic pieces) and are listed by the diagnostic as the unassigned bin, which is where new narratives are found. A fully automatic extraction (clustering the positions) is not needed yet: the map is 15 entries and the gatherer already tags lane and sign. |
| bandwidth over time | **feasible, thin** | three sweeps spanning seven days is a time series of length three; the sweeps differ in size (the item count is printed beside every count and a holder share is in the CSV). GDELT gives 90 days for five proxies, but one series (`ai_bubble`) proxies six narratives at once. Growth claims need four to six more sweeps before a "growing" label is more than a description. |
| plausibility against the fields and lenses | **feasible now** | 25 field conditions evaluate against the Nov 14 run (aliases map `SPX`/`ICSA_4wk`/`WTI` to the run's names; `E6_1m`-style refs read the lenses block). The direction of each condition is fixed at mapping time, before the reading is seen. |
| plausibility against the forks | **feasible, waiting on resolutions** | 19 fork references (16 distinct forks) are open; none has resolved since the map was written. The resolved record (21 forks) is used for the calibration buckets instead. |
| base rates from the history layer | **feasible now for the outcomes the history layer carries** | real equity returns at 1 y / 3 y, the long rate, crisis incidence, drawdown rates by era — the live query's analog quartiles against climatology. Narratives about auction tails, GPU rents or capex guides have no 18-country base rate; they are checked by forks and fields instead. |
| expert alignment (Dalio, Druckenmiller, Gundlach, Soros, …) | **alignment now; calibration later** | the roster already carries Dalio, Grant, Marks, Grantham, Chanos, Hartnett, Wilson, Perkins and 20 others, each with a dated position; the ledger shows which narrative each holds. Druckenmiller, Gundlach and Soros publish rarely and through interviews and 13F filings — adding them to the roster is a `dials/config.json` edit for the voices gatherer, and their 13F positions are already in the history layer's SEC tables as a *revealed* side. Scoring an expert's record (did Dalio's debt-crunch call pay) needs their stated positions resolved against dated outcomes, which is Action Ledger item 9 (voice scorecards). |
| game-theory vetting | **feasible as tags and as the games panel; not as a score** | each narrative carries incentive tags (who is rewarded for telling it) printed as a reader's discount; the run's G1–G4 reads are printed with the dial points. Turning "the teller has an incentive" into a number would be a judgment, so it is not done. |
| the bull / bear / pig baseline | **feasible now; computed per run** | ranked by distinct holders over the window; the pig case is a counted rule with three settings (entry rule 2 holders, cut-offs 0.34 / 0.66) that are themselves listed in the bias log; it found two asymmetries on this data (see §6). |
| the measured dial-point catalogue | **feasible now** | 26 fields with level, zone, window and 1-y percentiles, Δ1m/Δ3m; eight relative-return lenses with the run's notes; the N1–N6 and G1–G4 reads. |
| the bias log and overlay | **the log now; the overlay later** | 68 items catalogued (including the layer's own three settings); applying a user's alternative values and re-running the cone is an orchestrator change (§7). |
| a public interface where users set the dials | **later; the data model is ready** | the bias log is exactly the list of settings a public reader could change, each with its baseline. Serving it is a page over `ledger.json` + `bias_log.json`; collecting users' settings is a database behind that page. The data licences (Action Ledger item 2, now on hold) decide what such a page may show. |

Overall verdict: **feasible, and most of it is a reading of data the repository already gathers.** The two things that cannot be had yet are time (bandwidth needs more sweeps; calibration needs more resolved forks) and the overlay step inside the orchestrator.

## 5. Improvements found while building it

In rough priority:

1. **Score the system's branches as narratives** (done). The A/B/C weights are printed beside the crowd's holders with the same evidence tally. On the first read this is the most informative row in the ledger: the debt-crunch narrative has the widest holder base in the window (seven distinct holders, every field check true) while the system weights C at 1.0 at H2 — the confirmation criteria (consecutive 30-y tails, a positive stock–bond correlation with the dollar down, term premium above 1 and rising, a refunding shift) are what separate "widely held with the long end at acute levels" from "confirmed". The gap is the measurement; it is not a verdict on either.
2. **Separate the narrative from its predictions** (done). A narrative is a story; a prediction is a fork, a field condition or a base rate. The ledger scores the predictions and leaves the story as data, which is what keeps judgment out.
3. **Harvest the holders' own numbers** (done, as a list; not yet as predictions). The voices items carry 455 number claims in the window, each with what it is checkable against. The next step is to promote a holder's number into a typed prediction when it maps to a series the repository carries (Dalio's X-date → FiscalData; a strategist's index target → `SP500`) — then the narrative tests against *its own* claims, which is the strongest form of "let the narratives supply the hypotheses".
4. **Channel-normalised bandwidth, saturation and half-life.** Holder share per sweep is in the CSV; with ten or more sweeps, a narrative's half-life (sweeps from peak to half the peak holders) and a saturation flag (the share of the roster holding it) become measurable, and both are G3 variables in the Abreu–Brunnermeier sense.
5. **A lead–lag test of bandwidth against prices and flows.** Whether a narrative's holder count leads the lens it names (does `ai-capex-bust` bandwidth lead E7?) is a cross-correlation on two short series; it is the first thing to run once the series are long enough, because it would tell whether the discourse is a leading or lagging node, which the skill currently asserts ("opinion is the most lagging … node") rather than measures.
6. **Incentive tags as a reader's discount** (done). Kept out of the score on purpose.
7. **The two-holder entry rule with an emerging bin** (done). Single-voice claims are listed and marked; they are not in the baseline.
8. **A required falsifier** (done, enforced by `--check`).
9. **Baseline mode for the cone.** The deepest change: run the cone twice per run, once with the judgment set (today's tiers, fork p's, lines) and once with measured-only inputs (base-rate fork probabilities from the calibration buckets or the history ladders; zone transitions instead of event lines; a single default LR), and publish the difference as the operator's contribution. This is an orchestrator change (§7) and it is where "any further adjustment is known user bias" becomes literal.
10. **Opposition measured as a reading, not a sign.** The ledger's "opposed" count is a proxy (opposite-sign items that hit a strong word). A better measure needs the gatherer to tag each item with the narrative it argues *against*, which is a one-line addition to the voices skill's item schema.

## 6. The first read (2026-11-18, descriptive)

From `baseline.md` as built on sweeps 11-05 / 11-09 / 11-12 and run `2026-11-14T0611-dials`:

- The bear side is wider and older than the bull side in the window: nine bear narratives with two or more distinct holders against two bull ones. The widest are the debt crunch (7 distinct holders) and the AI capex bust (7), then the Fed policy error (6) and the credible-pipeline critique (6).
- The bull side's widest narrative is the rotation-inside-a-cycle read (5 distinct holders, 4 in the latest sweep, rising across the three sweeps); all three of its field checks are true (index within reach of its highs, IG below the transmission line, claims benign), and the one open fork it rests on is B-not-confirmed by Dec 9, which the system has at 0.93.
- The pig table found two asymmetries by the counted rule: the broken-price-discovery narrative is held by three distinct voices with neither of its two lens checks true (the equal-weight 493 are rising, E1 +6.3, and the top-8 are falling, E2 −9.4 — the opposite of "unprofitable companies outperform"); the resilient-consumer narrative is held by one voice with both its checks true (claims benign, housebuilders up on the month).
- The sell side is 88.8% buy or strong buy across the 14 registered tickers with a median target upside of 69% — the bull side's bandwidth in a channel the roster does not cover.
- The system's own position in the window: A 79.9 / B 18.9 / C 1.0 at H2. Printed beside the holders, it is the least bearish voice in the ledger. Whether that is the cone being right or the cone being slow is what the resolving forks will say; the ledger's job is to make the comparison visible every run.

None of the above is a recommendation; it is what the counts say on a seven-day window, and the window is the caveat.

## 7. Integration path

- **Phase 0 (this turn).** The layer exists beside the dials and reads their outputs. No change to the orchestrator, the gatherers or the state files.
- **Phase 1 (next runs).** Run the builder after each voices sweep (a one-line addition to the scheduled gather, or a hand run) so `bandwidth.csv` grows; add a narratives row to the QC; promote holders' numbers into typed predictions where the series exists; extend the roster with the rarely publishing experts.
- **Phase 2 (orchestrator, one edit).** The `macro-dials` skill reads `narratives/ledger.json` as an N7 line in the discourse panel — the narrative with the most holders, the fastest growing, and the largest asymmetry — under the same rule as N1–N6: never a likelihood ratio. Its fork registrations write a `baseline_p` beside `p` (the calibration-bucket rate or the history ladder rung), so the bias log stops being reconstructed after the fact.
- **Phase 3 (the overlay).** Baseline mode in `cone.py`: the cone computed twice, judgment set and measured set, the difference published. A user's own settings become a third set.
- **Phase 4 (public).** A page over the ledger and the bias log where a reader can move a setting and see the cone move; their settings collected as data. Gated on the licence question (Action Ledger item 2).

Guardrails that do not change in any phase: no likelihood ratio from a narrative; verbatim positions with name, date and link, never paraphrase as fact; deterministic matching with the matched words printed; the searcher-contamination rule (fixed instrument, date gate) inherited from the gatherers; a rule changed prospectively, never to re-score a logged window.

## 8. Open questions for the operator

1. Should the rarely publishing experts (Druckenmiller, Gundlach, Soros) enter the roster through interviews and 13F filings, accepting that their items will be months old — or stay out, with their 13F positions read on the revealed side only?
2. Is the two-holder entry rule the right bar for the baseline, or should an argument from a bank's research desk count as one holder or as none (today it counts as one)?
3. When a holder's number maps to a repository series, should it become a prediction automatically (phase 1) or only after a hand review of the mapping?
4. For the public phase, the bias log is the settings list. Which of its 68 items should a reader be able to move — the fork probabilities and hazard odds (the orchestrator's) or also the tiers and lines (the model's)?
