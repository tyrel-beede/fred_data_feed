# Rulings and overrides — machine-readable mirror of the memory files (FEED.md §5)

Scheduled runs read this file; attended runs read memory and this file and reconcile. A ruling is changed only by the user, or by an attended run on a `[stated]` instruction, in both places in the same turn. Mirrored 2026-11-06 from /areas/macro-dials.md (Overrides) and /areas/standoff-watch.md (Overrides, discipline note). Text as in memory; ids added.

## macro-dials

| id | from | ruling |
|---|---|---|
| principle | 2026-11-02 | [stated] "if there is a mathematical method or scientific principle that gives us an edge in modeling the predictive outcome we should make that our guiding light"; avoid fighting reality; tease out a little reveal of the future at each reasonable opportunity in the data. [stated] 2026-11-03: treat the whole system as one measurement and forecasting device; never assume only the named branches exist; let the tool feel the branches and elevate / prune / stack / link them; the reality lens measures the near-present and records a known past at one node of the information network. |
| a | 2026-10 | D3 ±1 scored once per non-overlapping ~20-session window (next eligible after ~Nov 13, 2026). |
| b | 2026-10 | B5 +1 requires the index up over the compression window. |
| c | 2026-10 | Events missed by more than one sweep are stage notes, never scored. |
| d | 2026-10-30 | A principal's capex hold/raise applies its computed non-event LR, never the ×1.2 tier. |
| e | 2026-10 | FOMC is Dec 8–9, 2026 — H2 horizon date Dec 9. |
| f | 2026-11-02 | Zone hysteresis: two consecutive prints beyond the line (the 10/29 IG "tight" voided by the 10/30 print, no weight either way). |
| g | 2026-11-02 | FE6 "turns positive" = crossing from <0 to >0 (the Oct survey's 0.0→1.7 is not a turn). |
| h | 2026-11-02 | C1 "single-B widens following CCC" = single-B +25 bp or more over a month in which CCC is +100 bp or more (first applied 11/2 at +44 / +148). |
| i | 2026-11-02 | [stated] An event the previous sweep missed is scored at the run that finds it, flagged `late` — "run the data at the nearest opportunity". |
| j | 2026-11-02 | [stated] Numeric state label from the cone band — s2 = P(B_H2 ≥ 20), s3 = P(B_H3 ≥ 30); A when both < 0.25, B-LEANING when s2 ≥ 0.75, else TRANSITION; no hysteresis on A↔TRANSITION (flips logged with cause; flips per month = instability gauge); B stays event-driven; stage separate as the S-count 0–7; regime = state / stage. Calibration anchors: 10/30 → A (0.19/0.22); 11/2 18:55 → A (0.19/0.21); 11/2 19:35 → TRANSITION (0.46/0.52). Revisit after a few resolved weeks. |
| k | 2026-11-02 (prospective; first print CRWV Nov 10) | Penny test v2: content in line = revenue and the guide inside the published consensus range (±2% of the midpoint where none); response = reaction ratio r = close-to-close move next session ÷ options-implied move (ATM straddle mid ÷ spot, first expiry after the print, from the repo chain the session before); synchronizer candidate r ≤ −1.5 with HY or the issuer's CDS wider that day; opposite marker r ≥ +1.5; r logged for every registered print; flat ±7% only for names without a surface (Hynix, Samsung, Kioxia). Indicative lines from the 11/2 chains: CRWV E\|move\| 16.4% → −24.7%; NVDA 7.3% → −10.9%; ORCL 11.7% → −17.6% (FQ2 priced after Dec 11 by the IV term structure); MU 4.5% → −6.8%. |
| l | 2026-11-02 (prospective) | Percentile-band zones for every field the repository carries: percentile of the level in the file's trailing window (6y; BAML OAS files 3y from 2023-11, archived forward from pull.py v2.2.2 — window stated with each credit reading): <50 benign · 50–80 watch · 80–95 stress · ≥95 acute; 1y percentile beside it; transition = the level crossing a band boundary (today's level and the level 20 sessions earlier in different bands under today's boundaries), confirmed by (f); hand lines stay as event lines (IG 100 ×2, IG 115 element, real 10y 3.0 ×4 / 2.5 ×2 A, claims +20% ×4, TP 1.0 element) and reference points; claims keep +10/15/20% vs the 52-wk low; TP, CRWV yield and Dated Brent keep hand zones. |
| m | 2026-11-02 | G3 as shares: marker share = markers at their line ÷ markers evaluable (n); position 1 at share ≥ 1/3 with n ≥ 3; provisional when n < 3; position 2 stays event-driven; stated and revealed shares the same way, corner at ≥ 0.5 each. |
| n | 2026-11-03 | [stated] Lead time logged with every forecast (calendar days from registration to resolution, and depth in forks from the current node), so the Brier ledger can be read by lead-time bucket; applies from the next run to every open fork (backfill from the registration dates the ids carry). |
| roster | 2026-11-03 | [stated] Ray Dalio's Substack and other prominent economics and tech thinkers added to the N6 inputs; the roster lives in `dials/config.json`. |
| architecture | 2026-11-03 / 11-06 | [stated] Sub-skills gather on a schedule, the orchestrator scores; timings in `config.json`; outputs and state in this repository (FEED.md). |

Queued proposals (not yet rules; see /areas/macro-dials.md): tree-of-cones mechanics (branch standing as accumulated log-LR; elevate / prune / stack / link; a not-in-frame residual with a surprise index; bitemporal records); debt-cycle fields from FiscalData/MTS (bills share of net issuance, net interest ÷ receipts); fork criteria written against the LR-carrying outcome only; a concession rule for a principal's equity raise beside a wide bond deal as a channel-3 member; T-panel markers as revealed-set candidates after backtest.

## standoff-watch

| id | from | ruling |
|---|---|---|
| s-T7 | 2026-10-30 | A continuing harassment pattern with no new modality is a stage note, not a re-scored event (T7 was applied twice for the same pattern on 10/20 and 10/30); new modalities (energy infrastructure, Gulf AI/cable targets, casualties, a Gulf state engaging) still score. |
| s-O1 | 2026-10-30 | O1 zone uses ICE Brent front-month futures for continuity; Dated Brent logged under O3. Never read a level from a prediction-market ladder (the 10/30 first-pass error). |
| s-fuse | 2026-10-30 | Fuse states: untested · strained (a commitment with collateral/lease structure but no priced tranche) · hung (pricing fails or is pulled) · clean. |
| s-M7 | 2026-10-30 | M7 zone series = UKMTO weekly transit counts (the series that fetches reliably), not the Kpler commodity-carrier count. |
| s-gather | 2026-11-06 | The daily `standoff` gather group in `dials/standoff/` is read first; standoff-watch scores and is the only writer of its state. |
