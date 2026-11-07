#!/usr/bin/env python3
"""migrate_memory.py — one-time seed of dials/runs/ from the memory files (FEED.md §7 step 1).

Every record below is a hand transcription of a line in /areas/macro-dials.md, /areas/macro-dials-log.md,
/areas/standoff-watch.md or /areas/macro-column.md as they stood on 2026-11-06, with a `source` field naming
the section and line it came from. Nothing is parsed from prose and nothing is inferred: where memory holds
only a rolled range for October, the range is recorded as a range; where a run line carries no number for a
column, the column is null. Discrepancies found while transcribing are recorded in NOTES and never corrected
silently (invariant: a run folder is the record of what was logged, not of what should have been).

Usage: python3 -I dials/tools/migrate_memory.py [--root dials]   (idempotent; refuses to overwrite a folder
whose run.json differs from what it would write)
"""
import argparse, json, os, sys, hashlib

MEM = "memory 2026-11-06"
NOTES = [
    "standoff weights method: memory applies each LR by multiplying the target branch's WEIGHT and renormalizing (10/20: E 20x2 -> 10/25/45/40 -> /120; 10/30: R+ 10x1.5, R- 20x1.5, E 35x2 -> 15/30/35/70 -> /150). Checked: this is algebraically identical to the odds-form update the skills specify (new_t = w_t*LR / (w_t*LR + 1 - w_t), others scaled by 1/(w_t*LR + 1 - w_t)), and sequential updates compose to the product of multipliers, so no method discrepancy. The only lossy step is the rounding to 5 (10/30 H2 exact 10.0/20.0/23.3/46.7 -> logged 10/20/25/45; H3 exact 9.7/19.4/19.4/51.6 -> 10/20/20/50). Recorded as logged; exact values in cone.json 'exact'.",
    "macro-dials F-20261103-ORCL-BONDS carries a Nov 3 id but was resolved in the 2026-11-02 19:35/20:30 session (the pricing was reported that evening); id kept as logged.",
    "macro-dials rolling Brier 0.121 (n=12) reproduced from the twelve resolved lines: sum 1.455 / 12 = 0.12125.",
    "October 2026 field, flow and discourse lines were rolled into min-max summaries in memory before migration; per-run point values for 10/17-18, 10/27 and 10/30 are not recoverable from memory except where a run line states them (lens levels, cone log lines, weights). Those summaries are stored under runs/2026-10-rolled/ as ranges.",
    "The macro-dials 2026-11-02 19:35 published band 'A 79 (67-85) / B 19 (12-30) / C 2' comes from the run line; the cone log line carries only the B IQR [12.2, 30.1]; the A band is kept as published text, not as a cone field.",
]

# ---------------------------------------------------------------- macro-dials: resolved and open forecasts
RESOLVED = [  # id, p, outcome, brier  — macro-dials.md 'Projection ledger > Resolved'
    ("F-20261020-SPCX", 0.80, 1, 0.04), ("F-20261021-META", 0.80, 1, 0.04), ("F-20261028-GEV", 0.75, 1, 0.0625),
    ("F-20261028-FOMC", 0.70, 1, 0.09), ("F-20261028-DISSENT", 0.55, 1, 0.2025), ("F-20261028-MSFT", 0.80, 0, 0.64),
    ("F-20261028-GOOGL", 0.85, 1, 0.0225), ("F-20261029-AMZN", 0.85, 1, 0.0225), ("F-20261030-ANY-RESTRAINT", 0.40, 0, 0.16),
    ("F-20261030-META-EQ", 0.75, 1, 0.0625), ("F-20261102-SLOOS", 0.30, 0, 0.09), ("F-20261103-ORCL-BONDS", 0.85, 1, 0.0225),
]
RESOLVED_NOTES = {"F-20261028-MSFT": "bundled criterion (capex >= guide and no restraint); scored 0 on a supply miss — the fork-criteria ruling followed",
                  "F-20261103-ORCL-BONDS": "priced inside talk, T+335 vs ~T+360 IPT; book undisclosed — scored on the pricing leg"}
# open: id, p, criterion, resolves (date or text), tier, target, element, implied (p|target, p|rest) or None, registered_run, notes
OPEN = [
    ("F-20261104-REFUND", 0.25, "coupon sizes increased or a bills shift", "2026-11-04", "x2", "C", "C", (0.48, 0.24), "2026-10-27", ""),
    ("F-20261104-OBDC", 0.60, "Q3 non-accruals at FV above Q2's", "2026-11-04", None, None, None, None, "2026-10-27", "date unverified"),
    ("F-20261110-10Y", 0.15, "10y auction tail >= 2 bp", "2026-11-10", "x2", "C", None, None, "2026-11-02", "cluster long-end; not a C element (acceptance edit)"),
    ("F-20261112-30Y", 0.20, "30y auction tail >= 2 bp", "2026-11-12", "x2", "C", "C", None, "2026-10-27", "cluster long-end"),
    ("F-20261118-20Y", 0.20, "20y auction tail >= 2 bp", "2026-11-18", "x2", "C", None, None, "2026-11-02", "cluster long-end"),
    ("F-20261110-CPI", 0.30, "Oct core CPI m/m >= 0.4", "2026-11-10T08:30-05:00", "x1.5", "B", None, (0.42, 0.28), "2026-10-27", ""),
    ("F-20261110-CRWV", 0.30, "Q3 discloses a customer-contract renegotiation, deferral or cancellation", "2026-11-10T17:00-05:00", "x2", "B", None, (0.54, 0.27), "2026-10-27", "complement P(backlog up q/q, no renegotiation)=0.65 (10/27) open; reaction ratio v2: Nov 13 straddle the session before; indicative E|move| 16.4%, line -24.7%"),
    ("F-20261117-NVDA-GUIDE", 0.25, "Q4 revenue guide below the ~$110B implied consensus", "2026-11-17 after the close", "x4", "B", "B", (0.74, 0.18), "2026-10-27", "v2: Nov 20 straddle; indicative E|move| 7.3%, line -10.9%"),
    ("F-20261117-NVDA-AR", 0.60, "AR growth > revenue growth again", "2026-11-17", "x1.2", "B", None, (0.70, 0.59), "2026-10-27", "weak tier (capped)"),
    ("F-20261120-ANTHROPIC", 0.42, "IPO delayed past Nov 30, downsized below the ~$75B reported raise, or priced below the top of the initial range", "2026-11-30", "x2", "B", None, (0.69, 0.37), "2026-10-27", "from 0.35 on the OpenAI cut (11/2); the 10/27 line P(prices by Nov 30 at >= $1.5T)=0.50 stays open"),
    ("F-20261210-ORCL", 0.09, "FQ2 capex cut, deferral or verified restraint language", "after 2026-12-11 (options term structure); Dec 14 cited; unverified", "x4", "B", "B", (0.27, 0.07), "2026-10-27", "v2 indicative E|move| 11.7%, line -17.6%"),
    ("F-20261209-FOMC", 0.15, "hike with claims 4-wk > +10% from the 189k low (LR-carrying form; P(hike) market 0.77 on 11/2)", "2026-12-09", "x2", "B", None, (0.27, 0.13), "2026-10-27", ""),
    ("F-20261209-IG100", 0.45, "IG OAS >= 100 bp on any day by Dec 9", "2026-12-09", "x2", "B", None, (0.80, 0.40), "2026-10-27", ""),
    ("F-20261209-IG115", 0.14, "IG OAS >= 115 bp on any day by Dec 9", "2026-12-09", None, "B", "B", (0.14, 0.14), "2026-10-27", "B element"),
    ("F-20261209-HORMUZ", 0.38, "signing by Dec 9", "2026-12-09", "x2", "A", None, (0.32, 0.16), "2026-10-27", "from 0.30 (11/2)"),
    ("F-20261209-OILE", 0.33, "standoff E criteria met or Brent front-month >= 120 by Dec 9", "2026-12-09", "x2", "B", None, (0.72, 0.36), "2026-10-27", "from 0.40 (11/2)"),
    ("F-20261209-B-CONF", 0.17, "B confirmed by Dec 9 (two of the five B elements)", "2026-12-09", None, None, None, None, "2026-11-02", "cone layer 2"),
    ("F-20261209-C-CONF", 0.13, "C confirmed by Dec 9", "2026-12-09", None, None, None, None, "2026-11-02", "cone layer 2"),
    ("F-20261209-REAL3", 0.09, "real 10y > 3.0 by Dec 9", "2026-12-09", None, None, None, None, "2026-11-02", ""),
    ("F-20261027-B-H2", 0.35, "B confirmed by Dec 9 (10/27 line, scored alongside)", "2026-12-09", None, None, None, None, "2026-10-27", ""),
    ("F-20261027-C-H2", 0.05, "C confirmed by Dec 9 (10/27 line)", "2026-12-09", None, None, None, None, "2026-10-27", ""),
    ("F-20261027-B-H3", 0.50, "B confirmed by Jan 20, 2027 (10/27 line)", "2027-01-20", None, None, None, None, "2026-10-27", ""),
    ("F-20270120-B-H3", 0.31, "B confirmed by Jan 20, 2027 (cone H3 median; 0.18 before the amendment)", "2027-01-20", None, None, None, None, "2026-11-02", "A 0.66, C 0.03 (+/-15)"),
    ("F-202612xx-MU", 0.15, "Micron FQ1 guide below consensus or LTA-renegotiation language", "~2026-12-16/17 (unverified)", "x2", "B", None, None, "2026-11-02", "H3-only; v2 indicative E|move| 4.5%"),
]

# ---------------------------------------------------------------- macro-dials: weights per run (as logged)
WEIGHTS = [  # run_id, run_at, kind, H2(A,B,C), H3(A,B,C), H2_IQR_B, H3_IQR_B, P_B_conf, P_C_conf, drift_B, state, s2, s3, source
    ("2026-10-18T0823-dials", "2026-10-18T08:23-06:00", "full", (70, 20, 10), None, None, None, None, None, None, None, None, None, "macro-dials.md run log: 'first runs 10/17-18 rolled earlier ... v3 weights H2 A70/B20/C10' (hand weights, pre-cone)"),
    ("2026-10-27T0817-dials", "2026-10-27T08:17-06:00", "full", (60, 35, 5), (45, 50, 5), None, None, None, None, None, None, None, None, "macro-dials.md run log 2026-10-27 (hand weights)"),
    ("2026-10-28T0000-dials-event", "2026-10-28", "event", (65, 30, 5), (50, 45, 5), None, None, None, None, None, None, None, None, "macro-dials.md run log 2026-10-28 event-mode (GEV resolution x1.2 A, old rule); also the 'Window prior (10/28)'"),
    ("2026-10-30T1445-dials", "2026-10-30T14:45-06:00", "full", (82.8, 13.2, 3.4), (72.7, 22.7, 3.8), (9.8, 19.0), None, 0.164, 0.10, 0.3, None, None, None, "macro-dials-log.md cone log 2026-10-30 14:45"),
    ("2026-10-30T1640-dials", "2026-10-30T16:40-06:00", "full", (86.4, 10.5, 2.6), (77.8, 18.5, 3.0), (7.4, 16.4), (13.4, 27.3), 0.156, 0.128, -0.2, "A", 0.19, 0.22, "macro-dials-log.md cone log 2026-10-30 16:40 (state label replayed 11/2)"),
    ("2026-11-02T1855-dials-lite", "2026-11-02T18:55-07:00", "event-lite", (86.8, 10.1, 2.7), (78.6, 17.7, 3.1), (6.8, 16.4), (12.4, 27.3), 0.163, 0.127, -0.0, "A", 0.19, 0.21, "macro-dials-log.md cone log 2026-11-02 18:55"),
    ("2026-11-02T1935-dials-lite", "2026-11-02T19:35-07:00", "event-lite", (78.5, 18.7, 2.4), (66.3, 30.7, 2.6), (12.2, 30.1), (21.1, 45.2), 0.166, 0.129, -1.0, "TRANSITION", 0.46, 0.52, "macro-dials-log.md cone log 2026-11-02 19:35 (+ C8 late-flagged x2 B; FLIP from A)"),
]
PUBLISHED_BANDS = {"2026-11-02T1935-dials-lite": "H2 A 79 (67-85) / B 19 (12-30) / C 2; H3 A 66 (52-76) / B 31 (21-45) / C 3 (+/-15); regime TRANSITION / stage score 5 of 7"}

# ---------------------------------------------------------------- macro-dials: lens levels (rebased 100 at 2026-10-16 close)
LENS_BASE = {"MU": 878.84, "GEV": 921.20, "VRT": 206.42, "ANET": 176.98, "MSFT": 529.05, "GOOGL": 340.59, "META": 709.33, "AMZN": 250.00,
             "CRWV": 61.39, "NBIS": 165.47, "ORCL": 128.23, "NVDA": 214.13, "AAPL": 343.46, "AVGO": 328.75, "TSLA": 354.72}
LENS = [  # run_id, SUP, PRIN, NEO, HYP, TOP8
    ("2026-10-18T0823-dials", 100.0, 100.0, 100.0, 100.0, None),
    ("2026-10-27T0817-dials", 98.1, 95.6, 93.6, 97.8, None),
    ("2026-10-30T1640-dials", 100.5, 90.9, 94.8, 92.3, 96.4),
    ("2026-11-02T1855-dials-lite", 97.5, 90.4, 86.7, 92.0, 95.8),
]
LENS_CLOSES_1102 = {"MU": 833.59, "GEV": 862.25, "VRT": 224.24, "ANET": 164.14, "MSFT": 507.12, "GOOGL": 278.99, "META": 606.73, "AMZN": 245.63,
                    "CRWV": 50.15, "NBIS": 141.39, "ORCL": 119.22, "NVDA": 202.06, "AAPL": 338.32, "AVGO": 322.23, "TSLA": 403.82}

# ---------------------------------------------------------------- macro-dials: the one point field row (11/02) and the October ranges
FIELD_COLS = ["DFII10", "T5YIFR", "WTI", "IG", "HY", "CCC", "ICSA_4wk", "DGS10", "DGS30", "DXY_broad", "SPX", "E1_1m", "E2_1m", "E4_1m", "E5_1m", "E6_1m", "E7_1m", "E8_1m"]
FIELD_1102 = {"DFII10": 2.60, "T5YIFR": 2.19, "WTI": 96.46, "IG": 94, "HY": 344, "CCC": 1327, "ICSA_4wk": 196.75, "DGS10": 4.94, "DGS30": 5.31,
              "DXY_broad": 121.67, "SPX": 7541, "E1_1m": 7.17, "E2_1m": -11.43, "E4_1m": -5.73, "E5_1m": -10.26, "E6_1m": -6.84, "E7_1m": -26.30, "E8_1m": 10.43}
FIELD_1102_EXTRA = {"DFII10_d1m": -0.33, "DFII10_d3m": 0.13, "T5YIFR_d1m": -0.16, "Brent": 104.77, "IG_d1m": 10, "HY_d1m": 32, "CCC_d1m": 148, "DXY_index": 101.8,
                    "SPY": 752.10, "E1_3m": 2.06, "E2_3m": -3.22, "E4_3m": -7.09, "E5_3m": -4.10, "E6_3m": -1.95, "E7_3m": -18.71, "E8_3m": -0.94, "E3_1m": -6.86,
                    "dDFII10_bp": -33, "E9_defcyc_1m": 7.60, "E9_defcyc_3m": 6.43, "E9_valgro_1m": 11.98, "E9_valgro_3m": 6.63, "E10_sigma": 9.02, "E10_range": 27.7,
                    "singleB": 360, "BB": 209, "corr_dSPX_d10y": 0.45, "VIX": 21.15, "asof_prices": "2026-11-02", "asof_fred": "2026-10-30"}
OCTOBER_RANGES = {"runs": ["10/17-18", "10/27", "10/30"], "DFII10": [2.63, 2.78], "T5YIFR": [2.21, 2.31], "WTI": [90, 103], "IG": [84, 91], "HY": [323, 338],
                  "CCC": [1278, 1356], "ICSA_4wk": [196.75, 198.5], "DGS10": [4.98, 5.10], "DGS30": [5.31, 5.43], "DXY_broad": [121.3, 121.6], "SPX": [7659, 7744],
                  "E1_1m": "-1.3 -> +5.9", "E2_1m": "-5.6 -> -9.6", "E4_1m": "-4.4 ... -4.7", "E5_1m": "+0.4 -> -10.3 -> -7.5", "E6_1m": "-11.0 -> -2.9",
                  "E7_1m": "-22.8 ... -25.2 -> -18.7", "E8_1m": "-3.7 -> +6.1",
                  "1030_extras": {"E3_1m": -5.76, "dDFII10_bp": -28, "E9_defcyc": 7.4, "E9_valgro": 10.4, "E10_sigma": 9.7, "singleB": 332, "corr_dSPX_d10y": 0.42, "netliq_B": 5745.7, "TP": "0.64 -> 0.61", "gold": "~4000 -> 3899"}}
FLOW_1102 = {"P1_eq_MA4_B": -27.7, "P1_bond_MA4_B": -3.9, "P1_MMF_ww_B": -43.3, "P4_AM_SP_pct3y": 44, "P4_AM_SP_pct26w": 27, "P4_LF_UST_pct": None, "P5_AAII_spread": -3.6,
             "P5_PC_tot9d": 0.89, "P6_margin_d3m_pct": -1.5, "P9_custody_d4w_B": -13.8, "P9_custody_ww_B": -4.2, "P9_MOF_4w": None, "P10_netliq_B": 5745.7, "P10_netliq_vs_0930_B": -37,
             "P11_SLOOS_largemid": 1.7, "P11_SLOOS_small": 5.1, "P11_CI_demand_net": -11.7, "carried": ["P1", "P2", "P5 AAII", "P5 PC", "P6", "P9 MOF"], "FE6_fired": False}
DISCOURSE_1102 = {"N1_bubble_7d": None, "N1_bubble_z": None, "N1_tone_bubble_7d": -3.32, "N1_tone_bubble_MA4": -2.22, "N1_tone_bubble_z": -1.96, "N1_tone_dccapex_7d": 0.84,
                  "N1_hormuz_vol_z": -1.69, "N1_status": "unmeasured (GDELT stale at 10/26-27; fourth run)", "N3_2027_capex_total_T": 1.2, "N3_source": "BofA/Hartnett via investinglive 11/1; FCF -180B, buybacks 14B annualized",
                  "N4_SBB_share": 90.7, "N4_status": "carried", "corner": "primed", "stated_share": "2/2", "revealed_share": "1/3", "G3_marker_share": "3/4"}
CONE_1102_1935_SPEC = {"H2_prior": [65, 30, 5], "H3_prior": [50, 45, 5], "horizon": "2026-12-09", "state_block": {"t2": 20, "t3": 30, "lo": 0.25, "hi": 0.75, "prev": "A"},
                       "applied": ["broadening convergence x1.5 A -> BROAD x1.33 A", "IG watch->tight VOIDED (q 0)", "MSFT CY26 trim as a cut x4 B at q 0.25 (judgment)", "C1 -1 single-B 316->360 following CCC x1.5 B", "C7 +1 list GPU rates up x1.2 A", "C8 -1 late-flagged OpenAI round cut x2 B (ruling i)"],
                       "nonevents": ["MSFT/GOOGL/AMZN restraint absent LR_non 0.85 each (p 0.09 x4, w_at 0.30)", "FOMC hike absent 0.92", "SLOOS >=10 absent 0.64 (p 0.30 x2, w_at 0.13)"],
                       "forks_added_1102": "CRWV Nov 10, NVDA Nov 17, 20y Nov 18; ANTHROPIC 0.42, HORMUZ 0.38, OILE 0.33, IG100 0.45, IG115 0.14", "spec_file_then": "scratchpad/cone/spec_20261102.json (not retained)"}

GAME_POSITIONS = {  # run_id -> dict (as logged under 'Game positions')
    "2026-10-27T0817-dials": {"G1": 1, "G2": 1, "G3": 1, "G4_Fed": 1, "G4_Treasury": 1, "note": "rolled 10/27-28"},
    "2026-10-30T1640-dials": {"G1": 1, "G2": 1, "G3": 2, "G3_status": "provisional", "G4_Fed": 1, "G4_Treasury": 1},
    "2026-11-02T1935-dials-lite": {"G1": 1, "G2": 1, "G2_note": "intensifying", "G3": 2, "G3_status": "provisional", "G3_marker_share": "3/4", "stated": "2/2", "revealed": "1/3", "corner": "primed", "G4_Fed": 1, "G4_Treasury": 1, "stage_score": 5},
}

RUN_LINES = {  # run_id -> verbatim run-log line (macro-dials.md 'Run log'), kept as report.md
    "2026-10-27T0817-dials": "2026-10-27/28 (rolled; first runs 10/17–18 rolled earlier: Debt +3 / Capital +1 / Business 0, \"A on state / B on stage\", v3 weights H2 A70/B20/C10) | 10/27 full: events Debt +1 (D3 tally) / Capital +1 (C2 SPCX) / Business 0; IG tight→watch 91 (×1.5 B); periphery convergence broad (10/18 ×1.5 applied, escalated ×1.33); stage capital late / debt late / business late-expansion; G1 1 · G2 1 · G3 1 · G4 1/1; weights H2 A60/B35/C5, H3 A45/B50/C5; Brier 0.04 (n=2); moved: 10y 5.15→4.99 in Meta week, IG 84→91, CCC 1,278→1,356, META −11% on a hold + $95B equity plan, LRCX −12% on a beat, Dec hike ~94→78%",
    "2026-10-28T0000-dials-event": "10/28 event-mode (Hynix, GEV, VRT): C5 +1 confirmed; S1 OP margin 80% vs 56.7% prior peak; S3 >50% of 2027–28 capacity on 5-yr LTAs; weights H2 A65/B30/C5, H3 A50/B45/C5 on the GEV resolution (×1.2 A, old rule)",
    "2026-10-30T1445-dials": "2026-10-30 14:45 MDT (full; superseded by 16:40 — kept for the tally) | events Debt 0 (5y/7y indirects 60.0/57.8 below avg; D3 +1 tally only) / Capital 0 scored (MSFT FQ1 $45.2B vs \">$50B\" on 3P delays, CY26 ~$170B, no restraint → judgment q 0.25 as a cut; GOOGL/AMZN held with 2027 up → non-events 0.85; C3 stage: MSFT $25B at 4.6x; C8: Amazon $50B into OpenAI vs $100B OpenAI backlog = S7) / Business 0 | broadening FIRED (×1.5 A); periphery 3 members present — not re-fired | G3 2 provisional (GOOGL −12.6% w/ HY +12; META −7% 10/22) | moved: SPX −1.83% d/d, SOX −7.2%, Intel −29%; 10y 5.05→4.91 post-FOMC; IG 91→89; oil +15% 1m; MMF −43B w/w",
    "2026-10-30T1640-dials": "2026-10-30 16:40 MDT (repository reconciliation; first run on repo data) | fields match the web to the bp; DFII10 Δ1m −28 bp (not −14) → broadening BROAD, ×1.33 A | filled: E2 −9.6, E9 def−cyc +7.4 and value−growth +10.4 with real yields falling (an AI-complex derating, not a rate rotation), E10 σ 9.7, dealers $426B at the 10th pct, AM 10y record long, LF 10y short 17th pct, custody Δ4w −13.8B, GDELT \"AI bubble\" tone z −1.2 | IG q 0.5 held pending the Oct 30 print | weights H2 A 86 (80–90) / B 10 (7–16) / C 3; H3 A 78 / B 18 (13–27) / C 3; P(B conf) 0.15, P(C) 0.13; drift −0.1 | Brier 0.134 (n=10)",
    "2026-10-30T1950-dials-enrich": "2026-10-30 19:50 MDT (v2.2/v2.2.1 enrichment; no re-weighting) | vol complex: SKEW 149.8 = 78th pct 1y (not 97th); VIX 19.4; no vol stress | option surfaces: index skew steep (SPY 25Δ 5.8 on 15.2 ATM; TLT call wall 85 = the record AM long in option form) while AI names near-symmetric (NVDA 5.9, MU 5.2, SPCX 4.5); NVDA Nov 18 implied ±6.6% | breadth (498): Oct 1 washout 40.8% >200d → 63.7%; 29.8% in >20% drawdowns; sector 1m medians Energy +12 … Tech +0.9, Comm −3.3 — expansion under a flat index | stage (10y files): supplier equity leg topped in June (SMH 6/22, MU 6/25, Hynix −51% since, Samsung −38%, LRCX −41%, AMAT −42%); principals' derating began 10/22–29 → suppliers-first confirmed | T panel: up/down volume QQQ 0.4, SMH 0.4 vs RSP 2.0; distribution days SMH 11, QQQ 9; GOOGL death cross 10/29 | credit tiers: BBB 110, NFCI −0.49, mortgage 7.24% (96th pct) | read unchanged",
    "2026-10-31T0000-dials-event": "2026-10-31 (event-mode: SPCX Q3 official transcript; stage notes only; full detail in [[spacex-tesla-article]]) | compute 1.7 GW at 9/30, ~2 GW Oct, 2.5–3 GW YE26, \"+10 GW incremental 2027 → ~13 GW\"; 200k GB300/month; 440k Vera Rubin cluster by end-Q2'27 | pricing: new deployments \"slightly above the $30–50 per watt range\", payback \"<1 year\"; rents \"at effectively the spot-market rate\", short contracts renewing higher — no take-or-pay by choice (S3 inverted); 50/50 internal/external goal | financing: IG, \"several debt pools\", OCF + debt + vendor/customer partnerships; self-funding from 1H27; backlog $63B ($17.5B deferred); Q4 capex $35–40B; Q1'27 revenue $33–37B; ARR $100B YE26, \"$500B–$1T\" YE27 (Musk) | Tesla–SpaceX combination under special committees | Maguire model (X 10/30–11/1; Musk \"I think we can do better\"): 10.2 GW YE27 vs Musk 13; ~$421B ARR vs $500B–1T; self-funding Q1'28 vs 1H27 — management discounted 25–50%; $40B/GW on 100% of GW conflicts with the 50/50 split | queued forks F-SPCX-GW27 / -SELFFUND / -PRICE for the Q4 call",
    "2026-11-02T1855-dials-lite": "2026-11-02 18:55 MST (event-lite; repo manual pull 00:39Z Nov 3 with Monday's bars; two agents for the sweep and the calendar) | events Debt 0 (D3 tally only; refunding Nov 4 pending) / Capital 0 net: C1 −1 single-B 316→360 following CCC (every HY tier wider on Oct 30: HY +18, B +28, BB +15, IG +5 d/d) and C7 +1 list GPU rates up (RunPod 10/12 and 11/2, Nebius 10/1); C2–C6 0 (Kioxia NAND deceleration = stage note; Oracle priced wide but done; Alphabet €6bn 2.8×; no pulled deals, no gates) / Business 0 (SLOOS +1.7, demand −11.7 weaker; ISM 55.5, prices paid 75.2; claims 194k; 5y5y 2.19) | zones: IG 94 WATCH — the 10/29 tight voided (hysteresis adopted); CCC 1,327 acute; real 10y 2.60 (−33 bp 1m); VIX 21.15 / SKEW 152.8 | convergence: periphery present at broad-level membership (CCC, single-B | E4 −5.7, E6 −6.8, E7 −26.3 | P1) and broadening present at broad (real 10y −33 w/ 5y5y anchored | E1 +7.2 w/ RSP up, E2 −11.4, E8 +10.4 | claims falling, 493 breadth, AI issuance up) — neither re-fired (once-a-month window); dual resolution measured in both at once; crunch Ch3 only — no | divergence: none; E6 3m reversal dated to September = S1 stage note | stage: capital late, debt late (TP falling, bonds hedging corr +0.45), business late-expansion | G1 1 · G2 1 intensifying · G3 2 provisional · G4 1/1 | moved: Brent 117.6→104.8 (−7.6% on Iran talk signals; Hormuz still closed), SOX −3.4%, NDX −1.4%, RSP +0.8%, A/D 343/154, 10y 4.91, gold +2%, Dec hike 80→77%, ORCL −8.8%, CRWV −8.6%, MU −5.8%, Hynix +3.8% Mon then −5.0% Tue a.m. | read: A on state / B on stage / G3 synchronizing provisional; the AI complex's own bear deepened while the 493 broadened; live judgments: MSFT-as-cut (q 0.25) and whether single-B's move is the start of transmission (IG100 fork 0.45)",
    "2026-11-02T1935-dials-lite": "19:35 amendment (ruling i): OpenAI round cut scored late, C8 −1 ×2 B → H2 A 79 (67–85) / B 19 (12–30) / C 2; H3 A 66 / B 31 (21–45) / C 3; P(B conf) 0.17; regime TRANSITION (0.46 / 0.52; first flip from A) / stage score 5 of 7 | 20:30 housekeeping: October lines rolled; rulings (k)–(m) adopted prospectively — under them tonight: HY, BB and single-B one print from a confirmed stress-band transition (×1.5 B if the 11/2 OAS prints hold; same-story cap — HY and single-B count once); G3 corner computed = primed (stated 2/2 / revealed 1/3) vs the hand-called synchronizing; CRWV/NVDA reaction lines −24.7% / −10.9% registered; Oracle's FQ2 date re-anchored after Dec 11 by the IV term structure",
}
ZONES_1102 = "IG 94 watch 77/100 (84/96/110; event lines 100, 115) · BBB 116 watch 75/100 · HY 344 stress 88/100 (302/328/379) one print pending · BB 209 stress 87/99 (182/201/237) pending · single-B 360 stress 91/99 (304/334/390) pending · CCC 1,327 acute 99.6/99 (908/967/1,076) · real 10y 2.60 acute 98/87 (1.74/2.07/2.40; event lines 2.5, 3.0) · 10y 4.94 acute 98/86 · 30y 5.31 acute 98/88 · 5y5y 2.19 benign 28/36 (2.26/2.33/2.43) · 5y BE 2.39 watch 51/54 · WTI 103.4 (10/27 FRED stale; settle 96.46 11/2) stress 94/89 · VIX 21.15 watch (1y 78th; 6y 61st; 18.0/22.9/29.7) · mortgage 7.24 acute 96/93 · DXY broad 121.67 watch 71/96 · NFCI -0.49 benign 45/91 · claims 4-wk 196.75k benign (+4.1% vs 189k low) · TP 0.61 watch falling · CRWV ~14-15.6% YTW / CDS ~1,041 acute · net liquidity 5,745.7B · SOFR 3.95 / IORB 3.90 · gold 3,971"

# ---------------------------------------------------------------- standoff-watch
STANDOFF = [  # run_id, run_at, H2 (R+,R-,F,E), H3, applied, method, source
    ("2026-10-20T0620-standoff", "2026-10-20T06:20-06:00", (10, 20, 35, 35), (10, 20, 30, 40), ["T7 -1 x2 toward E"], "odds-form (= weight-multiply and renormalize), rounded to 5; exact H2 8.3/20.8/37.5/33.3, H3 12.0/20.0/28.0/40.0",
     "standoff-watch.md projection ledger: opening H2 10/25/45/20, H3 15/25/35/25; applied 10/20 T7 -> H2 10/20/35/35, H3 10/20/30/40"),
    ("2026-10-30T1253-standoff", "2026-10-30T12:53-06:00", (10, 20, 25, 45), (10, 20, 20, 50), ["T4 +1 x1.5 toward R (R+ and R- odds x1.5)", "T7 -1 x2 toward E"], "odds-form (= weight-multiply and renormalize), rounded to 5: H2 raw 15/30/35/70 (sum 150) -> exact 10.0/20.0/23.3/46.7 -> logged 10/20/25/45; H3 raw 15/30/30/80 (sum 155) -> exact 9.7/19.4/19.4/51.6 -> logged 10/20/20/50",
     "standoff-watch.md projection ledger 2026-10-30 (corrected 13:15 MDT; the first-pass O1 zone transition from a stale Kalshi ladder was voided)"),
]
STANDOFF_OPEN = [  # id, p, criterion, resolves, note
    ("S-20261209-SIGN", 0.30, "a written US-Iran agreement announced by both governments by Dec 9", "2026-12-09", "held"),
    ("S-20261209-E", 0.40, "E criteria met by Dec 9", "2026-12-09", "from 0.35"),
    ("S-20261103-STRIKE", 0.10, "US or Israeli strikes on Iranian territory before Nov 3", "2026-11-03", ""),
    ("S-20261130-STRIKE", 0.45, "US or Israeli strikes on Iranian territory Nov 4-30", "2026-11-30", "from 0.40; press/crowd adjustment within +/-10"),
    ("S-20261109-YANBU", 0.30, "Saudi-acknowledged damage to the East-West line or Yanbu export facilities Oct 20-Nov 9", "2026-11-09", ""),
    ("S-20261209-M3", 0.15, "a Hormuz war-risk premium <= 2% of hull reported by Dec 9", "2026-12-09", ""),
    ("S-20261209-BRENT120", 0.35, "Brent front-month settles >= 120 on any day by Dec 9", "2026-12-09", "from 0.25; first-pass 0.20 void"),
    ("S-20261209-BRENT90", 0.15, "Brent front-month settles <= 90 on any day by Dec 9", "2026-12-09", "from 0.20; first-pass 0.35 void"),
    ("S-20261231-FUSE", 0.10, "any tranche of the SpaceX $40B prices by Dec 31 at an IG spread with no collateral or sweeteners reported", "2026-12-31", "from 0.20"),
    ("S-20261204-ISRAELGOV", 0.30, "a new Israeli government sworn in by Dec 4", "2026-12-04", "new 10/30"),
]
STANDOFF_EXPORT_1030 = {"run_at": "2026-10-30T12:53-06:00 (corrected 13:15)", "H2": {"R+": 10, "R-": 20, "F": 25, "E": 45}, "floor_zone": "100-120",
                        "brent": {"Jan": 113.5, "Dec_expiry": 117.6, "high_4y": 116.72, "high_date": "2026-10-23", "Dec_Jan_spread": 4.1}, "hormuz_fork_p_signing_by": {"2026-12-09": 0.30},
                        "shock_type": "supply", "fuse": "strained", "fuse_note": "SpaceX $40B restructured as an Apollo GPU finance lease Oct 26; pricing pending"}
STANDOFF_HAZARDS_1030 = {"energy_infra_strike": 12, "gulf_state_engages_iran": 7, "iran_nuclear_test": 3, "red_sea_or_pipeline_shutdown": 25, "fuse_pricing_fails_or_sweetened_by_1231": 15, "disorderly_treasury_move": 10, "choreographed_strike_then_ceasefire": 10}
STANDOFF_RUN_LINES = {
    "2026-10-20T0620-standoff": "2026-10-20 06:20 MDT (first full run) | T: T7 −1 ×2 E; T1–T6 0 | M: M1 in force · M2 ≥4 · M3 stress · M4 none · M5 FM · M7 <20 · M8 10–13 · M9 flowing-contested | O1 Brent fut ~107 / Dated 126.55 (10/14) / WTI ~97, zone 100–120; O2 Dec–Jan 2.85 (10/5) | F1 3.7/2.6 (Sep), floor month 8; F3 Oct hold ~81%, Dec hike ~85–94% | fuse untested (FT: 2027 close) | weights H2 R+10/R−20/F35/E35, H3 R+10/R−20/F30/E40 | Brier n/a | grade-mode: no",
    "2026-10-30T1253-standoff": "2026-10-30 12:53 MDT (full run, triggered by the Oct 30 selloff conversation) | T: T4 +1 ×1.5 R (Trump \"end soon\"); T7 −1 ×2 E (limpet, sinking, record month); T3 0 but strongest since July (Qatar draft revisions in Tehran, Vance letter); T1/T2/T5/T6 0 | M: M1 in force · M2 ≥4 record month · M3 stress (carried) · M4 none (US \"cleared\" claim disputed) · M5 FM to early Nov · M7 20–60 (UKMTO ~40/day) · M8 10–13 with 8.5–14 weekly swings · M9 flowing-contested (Oct 27 Houthi claim unacknowledged; Egypt authorizes Saudi support) | O1 Brent Jan ~113.5 / Dec expiry ~117.6 (10/30), zone 100–120 unchanged (first pass misread ~97 from a Kalshi ladder; corrected 13:15 MDT); O2 Dec–Jan ≈ 4.1 widening; O8 reg 4.2471 (10/28); O9 supply-type day | F1 Sep PCE 0.5/3.6 headline, 0.3/3.1 core, floor month 8–9; F3 Oct hold 10–2, Dec hike 79.6% (10/30); F4 10y 4.91 | M3 6–10% (Oct 14) | fuse strained (Apollo GPU lease, Oct 26, pricing pending) | weights H2 R+10/R−20/F25/E45, H3 R+10/R−20/F20/E50 | Brier n/a (first resolution Nov 3) | grade-mode: no",
}

# ---------------------------------------------------------------- macro-column
COLUMNS = [  # run_id, date, built_from, headline, added, graded, retired, tally(paid,cost,void), words, note
    ("2026-10-18T0000-column", "2026-10-18", "2026-10-18T0823-dials", "The Market Is Holding Up. Look Underneath, and It Isn't. / The Case That the Market Has It Right", 6, 0, 0, (0, 0, 0), None, "experimental, not a formal column"),
    ("2026-10-27T0817-column", "2026-10-27", "2026-10-27T0817-dials", "Credit Reached the Core This Week. The Economy Didn't Notice.", 6, 1, 0, (0, 1, 0), None, "spine date Nov 13; erratum 10/28 on Wilson's 'final innings'"),
    ("2026-10-30T2000-column", "2026-10-30", "2026-10-30T1640-dials", "The Spenders Kept Spending. The Market Stopped Paying Them for It.", 6, 3, 0, (0, 4, 0), 3600, "first long-form column; delivered as a doc https://claude.ai/artifact/1JgJhhJ7rpBMe5fVV1ExW4; spine date Nov 20"),
]
PIGS_OPEN = [  # id, resolves, criterion, status_1030
    ("PG-20261018-PERIPHERY-REBOUND", "2026-11-13", "equal-weight basket (IWM, XHB, E7 neoclouds) outperforms the top-8 equal-weight by > 3 pts from the Oct 16 close to Nov 13", "live; +5.1 pts above the line (10/30)"),
    ("PG-20261018-UNMOVED", "2026-12-09", "IG OAS > 100 or E6 3m < -15 by Dec 9; void if no B element", "IG 89, E6 3m -1.5, no B element; four-week limit at the next column"),
    ("PG-20261018-TAIL", "2026-11-13", "gold +5% from Oct 16 by Nov 13 together with a 30y tail >= 2 bp or custody down 4 straight weeks", "against: gold -6.9% since 10/16"),
    ("PG-20261018-DEC-HIKE", "2026-12-09", "no hike on Dec 9, or Dec-hike odds < 60% at any point before", "odds 78-80 vs dashboard 80; four-week limit at the next column"),
    ("PG-20261027-SINGLE-B", "2026-12-09", "HY OAS >= 400 on any day by Dec 9 -> paid; else cost", "HY 326, single-B 332, CCC 1,325; not killed"),
    ("PG-20261027-NVDA-LAST-NODE", "2026-11-19", "NVDA close on Nov 19 >= +/-10% from 216.00 (10/26)", "204.64 = -5.3%"),
    ("PG-20261027-CRWV-80", "2026-12-09", "CRWV 5y CDS <= 900 bp on any day by Dec 9 -> paid; else cost", "CDS ~1,138"),
    ("PG-20261027-AVGO-SPV", "2026-12-01", "AVGO close on Dec 1 >= +/-8% from 329.17 (10/26)", "326.08 = -0.9%"),
    ("PG-20261030-SHELTER", "2026-11-13", "10y close >= 5.20 on any day by Nov 13, or a 30y tail >= 2 bp on Nov 12 -> paid; else cost", "new"),
    ("PG-20261030-UNHEDGED-NAMES", "2026-11-20", "top-8 dispersion sigma >= 12 with SPX within 5% of its high -> paid; sigma < 7 or SPX > 5% down -> cost", "new"),
    ("PG-20261030-JUNE-TOP", "2026-12-09", "equal-weight (LRCX, AMAT, 000660.KS, 005930.KS) beats top-8 equal-weight by > 5 pts from Oct 30 -> paid; void if a B element fires first", "new"),
    ("PG-20261030-LAST-SUPPLIER", "2026-12-18", "MU/SMH ratio down > 10% from 1.693 (10/30) -> paid; else cost", "new"),
    ("PG-20261030-UNOWNED-OIL", "2026-12-09", "WTI front-month close outside $90-120 on any day by Dec 9 -> paid; else cost", "new"),
    ("PG-20261030-BREADTH-TREND", "2026-11-20", "paid if on Nov 20 >= 63.7% above the 200d AND the A/D line > its Oct 29 level; cost if either fails", "new"),
]
PIGS_GRADED = [  # id, grade, graded_on, basis
    ("PG-20261018-SPCX", "cost", "2026-10-27", "SPCX +7.79% on Oct 21 with capex raised vs a +/-8% line"),
    ("PG-20261018-CONVEX", "cost", "2026-10-30", "SPX -1.4% Oct 19-30 (range +1.5/-1.7%), SMH -4.7% vs +/-4% / +/-8% lines"),
    ("PG-20261027-DISSENT", "cost", "2026-10-30", "two dissents for a hike; 2y 4.67 vs 4.68 prior = 1 bp vs an 8 bp line"),
    ("PG-20261027-AMZN-TAPE", "cost", "2026-10-30", "AMZN -7% premarket, closed -1.4% vs a +/-6% line"),
]


def jdump(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n"


def write(root, rel, obj_or_text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = obj_or_text if isinstance(obj_or_text, str) else jdump(obj_or_text)
    if os.path.exists(path) and rel.endswith("run.json"):
        old = open(path, encoding="utf-8").read()
        if old != text:
            sys.exit(f"refusing to overwrite {rel}: run.json differs (run folders are written once)")
    open(path, "w", encoding="utf-8").write(text)


def header(run_id, run_at, kind, mode, source, extra=None):
    h = {"run_id": run_id, "kind": kind, "mode": mode, "run_at": run_at, "migrated_from": MEM, "source": source,
         "repo_commit": None, "inputs_commit": None, "status": "ok", "error": "", "note": "seeded by migrate_memory.py; values transcribed, not recomputed"}
    if extra: h.update(extra)
    return h


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="dials"); a = ap.parse_args()
    R = a.root
    runs = os.path.join(R, "runs")

    # ---- macro-dials runs
    w_by_id = {w[0]: w for w in WEIGHTS}
    for run_id, line in RUN_LINES.items():
        kind = "dials"; mode = "event" if "event" in run_id else ("lite" if "lite" in run_id else ("enrichment" if "enrich" in run_id else "full"))
        run_at = w_by_id[run_id][1] if run_id in w_by_id else {"2026-10-30T1950-dials-enrich": "2026-10-30T19:50-06:00", "2026-10-31T0000-dials-event": "2026-10-31"}[run_id]
        write(R, f"runs/{run_id}/run.json", header(run_id, run_at, kind, mode, "macro-dials.md run log"))
        write(R, f"runs/{run_id}/report.md", f"# {run_id}\n\nVerbatim run line from /areas/macro-dials.md (migrated {MEM}):\n\n{line}\n")
        if run_id in w_by_id:
            _, _, _, h2, h3, iqb2, iqb3, pb, pc, drift, state, s2, s3, src = w_by_id[run_id]
            cone = {"H2": list(h2), "H3": list(h3) if h3 else None, "H2_IQR_B": list(iqb2) if iqb2 else None, "H3_IQR_B": list(iqb3) if iqb3 else None,
                    "P_B_conf": pb, "P_C_conf": pc, "drift_B": drift, "state": state, "s2": s2, "s3": s3, "source": src, "published_band": PUBLISHED_BANDS.get(run_id)}
            write(R, f"runs/{run_id}/cone.json", cone)
        if run_id in GAME_POSITIONS:
            write(R, f"runs/{run_id}/readings.json", {"game_positions": GAME_POSITIONS[run_id], "source": "macro-dials.md Game positions"})
    # 10/18 run (weights only; rolled)
    write(R, "runs/2026-10-18T0823-dials/run.json", header("2026-10-18T0823-dials", "2026-10-18T08:23-06:00", "dials", "full", "macro-dials.md run log (rolled: 'first runs 10/17-18')"))
    write(R, "runs/2026-10-18T0823-dials/cone.json", {"H2": [70, 20, 10], "H3": None, "state": None, "source": WEIGHTS[0][13], "hand_weights": True})
    write(R, "runs/2026-10-18T0823-dials/report.md", "# 2026-10-18T0823-dials\n\nRolled in memory: 'first runs 10/17–18 rolled earlier: Debt +3 / Capital +1 / Business 0, \"A on state / B on stage\", v3 weights H2 A70/B20/C10'.\n")
    # 11/02 point readings into the 18:55 run; ledger snapshot into the 19:35 run
    write(R, "runs/2026-11-02T1855-dials-lite/readings.json", {"fields": FIELD_1102, "fields_extra": FIELD_1102_EXTRA, "flows": FLOW_1102, "discourse": DISCOURSE_1102,
                                                                "lens_closes": LENS_CLOSES_1102, "zones": ZONES_1102, "source": "macro-dials-log.md field/flow/discourse/lens logs 2026-11-02 18:55; macro-dials.md Field zones"})
    write(R, "runs/2026-11-02T1935-dials-lite/readings.json", {"game_positions": GAME_POSITIONS["2026-11-02T1935-dials-lite"], "source": "macro-dials.md Game positions 2026-11-02"})
    write(R, "runs/2026-11-02T1935-dials-lite/spec.json", CONE_1102_1935_SPEC)
    write(R, "runs/2026-11-02T1935-dials-lite/forecasts.json", {
        "registered": [{"id": i, "p": p, "criterion": c, "resolves": r, "tier": t, "target": tg, "element": el, "implied_p_target": (im[0] if im else None), "implied_p_rest": (im[1] if im else None), "registered_run": reg, "note": n, "lead_days": None, "depth": None}
                        for i, p, c, r, t, tg, el, im, reg, n in OPEN],
        "resolved": [{"id": i, "p": p, "outcome": o, "brier": b, "note": RESOLVED_NOTES.get(i, "")} for i, p, o, b in RESOLVED],
        "rolling_brier_as_logged": 0.121, "n_as_logged": 12,
        "source": "macro-dials.md Projection ledger (Resolved; Open forecasts) as of 2026-11-02 20:30; the open set is the state at migration, registered_run as recorded"})
    # October rolled summaries and lens points
    write(R, "runs/2026-10-rolled/run.json", header("2026-10-rolled", "2026-10", "dials", "rolled-summary", "macro-dials-log.md field/flow/discourse logs, 'October 2026 (rolled)' lines",
                                                     {"note": "min-max / sequence summaries only; per-run point values not recoverable from memory"}))
    write(R, "runs/2026-10-rolled/readings.json", {"field_ranges": OCTOBER_RANGES,
        "flow_rolled": "P1 eq MA4 -24.2B -> -24.0B -> -27.7B ex-anomaly (accel) | bond -3.1B -> -3.9B | MMF +31.8B (2wk) -> -43.3B w/w (10/30) | AM S&P 26w idx 0 (10/27) -> +923K, 3y pct 45 / 26w 27 (10/30); AM NQ 25th; LF ES -401K | LF 10y 3y pct 29 -> 17; LF 2y 92 -> 91; LF T-bond 98 -> 100 | AAII -2.9 -> -8.9 -> -3.6 | PC10 eq 0.62-0.67 / tot-9d 0.84-0.89 (34th -> 73rd) | margin -1.5% (Sep) | custody -30.0B (1wk) -> +18.5B -> d4w -13.8B | MOF -161.6B JPY (5-wk -3.43T) -> -92.6B (6th wk) | netliq +2.7B -> +31B (4w) -> -55.7B w/w",
        "discourse_rolled": "10/18 'AI bubble' GDELT share 0.0052-0.0064 (peak 0.0539 Aug 31), dc-capex 0.0084-0.0087 | 10/27 GDELT refused; N3 big-four 2027 $934.5B (Aug, stale) / Goldman $1.2T five incl. ORCL / Morgan Stanley $1.58T total AI compute (10/19); N4 principals+suppliers SB+B 90.7% | 10/30 repo tone 'AI bubble' 7d -2.54 (z -1.23), dc-capex +0.36, Hormuz volume z -1.44 | corner primed, provisional throughout"})
    for run_id, sup, prin, neo, hyp, top8 in LENS:
        write(R, f"runs/{run_id}/lens.json", {"SUP": sup, "PRIN": prin, "NEO": neo, "HYP": hyp, "TOP8": top8, "base_date": "2026-10-16", "base_closes": LENS_BASE, "source": "macro-dials-log.md lens level log"})

    # ---- standoff runs
    for run_id, run_at, h2, h3, applied, method, src in STANDOFF:
        write(R, f"runs/{run_id}/run.json", header(run_id, run_at, "standoff", "full", src))
        write(R, f"runs/{run_id}/cone.json", {"H2": {"R+": h2[0], "R-": h2[1], "F": h2[2], "E": h2[3]}, "H3": {"R+": h3[0], "R-": h3[1], "F": h3[2], "E": h3[3]}, "applied": applied, "method": method, "source": src})
        write(R, f"runs/{run_id}/report.md", f"# {run_id}\n\nVerbatim run line from /areas/standoff-watch.md (migrated {MEM}):\n\n{STANDOFF_RUN_LINES[run_id]}\n")
    write(R, "runs/2026-10-30T1253-standoff/export.json", STANDOFF_EXPORT_1030)
    write(R, "runs/2026-10-30T1253-standoff/forecasts.json", {"registered": [{"id": i, "p": p, "criterion": c, "resolves": r, "note": n} for i, p, c, r, n in STANDOFF_OPEN], "resolved": [], "hazards_per_month": STANDOFF_HAZARDS_1030,
                                                               "source": "standoff-watch.md Projection ledger (Open forecasts; Hazards) 2026-10-30"})

    # ---- column runs
    for run_id, date, built, head, added, graded, retired, tally, words, note in COLUMNS:
        write(R, f"runs/{run_id}/run.json", header(run_id, date, "column", "weekly", "macro-column.md Column log", {"built_from": built, "headline": head, "pigs_added": added, "pigs_graded": graded, "pigs_retired": retired,
                                                                                                                  "tally": {"paid": tally[0], "cost": tally[1], "void": tally[2]}, "words": words, "note": note}))
    write(R, "runs/2026-10-30T2000-column/pigs.json", {"open": [{"id": i, "resolves": r, "criterion": c, "status_1030": s} for i, r, c, s in PIGS_OPEN],
                                                       "graded": [{"id": i, "grade": g, "graded_on": d, "basis": b} for i, g, d, b in PIGS_GRADED], "tally": {"paid": 0, "cost": 4, "void": 0},
                                                       "source": "macro-column.md Pig ledger (open; graded); Running tally"})

    write(R, "runs/MIGRATION_NOTES.md", "# Migration notes (migrate_memory.py, " + MEM + ")\n\n" + "\n".join(f"- {n}" for n in NOTES) + "\n")
    print("seeded", sum(len(f) for _, _, f in os.walk(runs)), "files under", runs)


if __name__ == "__main__":
    main()
