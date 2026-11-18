# The narrative ledger

Built 2026-11-18T20:32:15Z from 3 voices sweeps (2026-11-05, 2026-11-09, 2026-11-12), the event sweeps, the consensus pages, the GDELT timelines, the scorer run `2026-11-14T0611-dials` and the history layer's live query. Matching is deterministic on the words in `map.json`; the words that matched are printed with each quote. A *holder* is a tracked voice or argument whose sign agrees with the narrative's and whose item matched its words; *opposed* counts items of the opposite sign that matched one of its strong words (a proxy for opposition, not a reading of the argument); *mentions* count every matched item. Nothing here moves a branch weight: the system's own weight is printed beside the holders as one more voice.

## At a glance

| narrative | sign | lifecycle | holders by sweep | opposed | GDELT z (series) | evidence: fields true / evaluable | forks supporting / resolved | open forks (p) | system weight H2 |
|---|---|---|---|---|---|---|---|---|---|
| The AI buildout is a debt-financed capex bubble that breaks when the m (`ai-capex-bust`) | bear | held | 4 → 5 → 1 | 0 → 0 → 0 | 1.42 (ai_bubble) | 2 / 4 | 0 / 0 | F-20261209-B-CONF (0.071), F-20270120-B-H3 (0.313) | 18.9 (B) |
| This is 2000 again: a productive bubble whose bust spares the economy  (`dotcom-echo`) | bear | held | 1 → 0 → 1 | 0 → 0 → 0 | 1.42 (ai_bubble) | 3 / 3 | 0 / 0 |  | 18.9 (B) |
| AI's financing is circular — suppliers fund their customers — so the c (`circular-financing`) | bear | held | 2 → 0 → 2 | 0 → 0 → 0 | 1.42 (ai_bubble) | 1 / 1 | 0 / 0 | F-20261117-NVDA-AR (0.6), F-20261117-NVDA-BACKSTOP (0.2) | 18.9 (B) |
| Only a third of the announced data-center pipeline is credible, and po (`credible-pipeline`) | bear | held | 4 → 2 → 1 | 0 → 0 → 0 | 0.34 (dc_capex) | 0 / 0 | 0 / 0 | F-20261210-ORCL (0.09) | 18.9 (B) |
| The selloff is a rotation inside a continuing cycle: a correction's la (`flight-to-quality`) | bull | growing | 2 → 1 → 4 | 1 → 1 → 1 | 1.42 (ai_bubble) | 3 / 3 | 0 / 0 | F-20261209-B-CONF (0.071) | 79.9 (A) |
| Demand exceeds supply through FY28 and consensus is too low: the suppl (`nvidia-supercycle`) | bull | growing | 0 → 0 → 2 | 0 → 0 → 0 |  | 0 / 1 | 0 / 0 | F-20261117-NVDA-GUIDE (0.25), F-202612xx-MU (0.15) | 79.9 (A) |
| Deficits at full employment, thinning auction demand and a rising term (`debt-crunch`) | bear-bonds | held | 4 → 1 → 2 | 0 → 0 → 0 | -0.02 (term_premium) | 2 / 2 | 0 / 0 | F-20261209-C-CONF (0.02), F-20261210-30YR (0.25), F-20261208-10YR (0.25) | 1.0 (C) |
| The Fed hikes into a slowing, lagging-data economy — the 2018 path, wi (`fed-policy-error`) | bear | held | 2 → 3 → 2 | 0 → 0 → 2 |  | 1 / 2 | 0 / 0 | F-20261209-FOMC (0.08), F-20261210-CPI (0.25) | 18.9 (B) |
| Households keep spending across income groups while saying they are mi (`consumer-resilient`) | bull | growing | 0 → 0 → 1 | 0 → 0 → 0 |  | 2 / 2 | 0 / 0 |  | 79.9 (A) |
| Prices are not reflecting fundamentals: unprofitable companies outperf (`price-discovery-broken`) | bear | held | 3 → 1 → 1 | 0 → 0 → 0 | 1.42 (ai_bubble) | 0 / 2 | 0 / 0 |  | 18.9 (B) |
| Stress is surfacing in private credit and leveraged loans: BDC marks,  (`private-credit-stress`) | bear | fading | 4 → 1 → 0 | 0 → 0 → 0 | -0.26 (private_credit) | 2 / 4 | 0 / 0 | F-20261130-CRWV-LOAN (0.2) | 18.9 (B) |
| Key-person and governance risk at Nvidia: the chief is gone, the backs (`nvidia-governance`) | bear | growing | 0 → 0 → 3 | 0 → 0 → 2 |  | 0 / 0 | 0 / 0 | F-20261117-NVDA-BACKSTOP (0.2), F-20261117-NVDA-GUIDE (0.25) | 18.9 (B) |
| The Hormuz standoff sets an oil floor that feeds headline inflation an (`oil-floor-hormuz`) | neutral | fading | 0 → 3 → 0 | 0 → 0 → 0 | -0.38 (hormuz) | 1 / 1 | 0 / 0 | F-20261209-HORMUZ (0.15), F-20261209-OILE (0.35) | standoff E 45 / F 35 / R+ 5 / R- 15 |
| SpaceX is the fastest data-center builder ever — or its revenue math i (`spacex-compute-bet`) | contested | fading | 3 → 0 → 0 | 0 → 0 → 0 |  | 0 / 0 | 0 / 0 | F-20261231-SPCX-FUSE (0.3) | 18.9 (B) |
| China holds hidden foreign-exchange assets that underpin a weak renmin (`china-hidden-fx`) | n/a | unheld (mentions only) | 0 → 0 → 0 | 0 → 0 → 0 |  | 0 / 0 | 0 / 0 |  |  |

Sell-side alignment (N4, 2026-11-09): 88.8% of 645 ratings across 14 registered tickers are buy or strong buy; median price-target upside 69%. This is the sell side's bandwidth on the bull narratives, printed beside them and never added to the holder counts.

## The AI buildout is a debt-financed capex bubble that breaks when the money runs out

`ai-capex-bust` · sign **bear** · lane capital · branch B · lifecycle **held**

As held: capex has run past cash flow and is increasingly debt-funded; the chain below the principals (neoclouds, labs, suppliers) defects first — deferrals, cancellations, shelved deals, rental prices — and the bust arrives through credit transmission rather than through anyone's guidance.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Dario Perkins, Ed Zitron, Michael Hartnett, Paul Krugman (4) | — (0) | 6 | 1 |
| 2026-11-09 (58) | Ed Zitron, Gary Marcus, Paul Kedrosky, Paul Krugman, arg: Redwood: AI revenue will not grow fast enough to support current investm (5) | — (0) | 7 | 2 |
| 2026-11-12 (56) | Ed Zitron (1) | — (0) | 3 | 1 |

**In their words** (the latest matched positions; words that matched in brackets).

- Paul Kedrosky (2026-11-06, bear) [overdetermined, capex]: Kedrosky models the data center boom as a hybrid public-private stimulus program: hyperscalers supplied capital while governments supplied depreciation, tax credits, abatements, permitting and power access, which made AI capex a material fraction of GDP growth and kept excesses less visible in equit…
- Gary Marcus (2026-11-05, bear) [bubble may finally have popped, ai bubble, bubble, neocloud]: Says the generative AI bubble may finally have popped. He had posted on X on Nov 4 that tech stocks were set to crash now that AI companies would no longer get a free ride; the first day was split (chipmakers and neoclouds such as CoreWeave down sharply, Amazon, Apple and Google up), but by Nov 5 it…
- arg: Redwood: AI revenue will not grow fast enough to support current investm (2026-11-06, bear) [capex slows, capex]: AI should lift productivity, but AI revenue is unlikely to grow fast enough to support current levels of investment; if revenue lags, AI capital spending slows and that could weigh on US growth next year.
- Ed Zitron (2026-11-10, bear) [neocloud, coreweave]: Huang's affair with Megaspeed CEO Alice Huang is a symptom of a larger scheme: Megaspeed functioned as a transshipment entity funnelling sanctioned Nvidia GPUs into China, Nvidia knew about it as far back as 2024 and interfered with Commerce's probe, and Nvidia's earnings were inflated by more than …

**Numbers the holders put on it** (59 in the window, 36 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- arg: Redwood: AI revenue will not grow f (2026-11-06): Oxford Economics expects Fed rate increases in December and March — *check against: FOMC decisions; FRED DFEDTARU*
- Ed Zitron (2026-11-10): Megaspeed subsidiary SpeedMatrix bought ~$4.8bn of Nvidia GPUs; Megaspeed balance sheet grew from $33m to $3bn in 2024 (Alibaba anchor customer) — *check against: Bloomberg/FT reporting; Singapore ACRA filings; no FRED field*
- Ed Zitron (2026-11-10): $2.4bn of Nvidia 'Bianca' boards unaccounted for at sites reported to Washington — *check against: Bloomberg reporting; Commerce/BIS*
- Ed Zitron (2026-11-10): Culper: ~20% of Nvidia FY2026 revenue (~$43.18bn) from China; Megaspeed imported 50,000 more GPUs than Nvidia told the government — *check against: Nvidia FY2026 10-K geographic revenue note; Culper_NVDA_5-13-2026 report*
- Ed Zitron (2026-11-10): 44% of Nvidia 1H FY2027 revenue from three customers; Q2 FY2027: 70% of receivables from three customers, 16% of revenue from one — *check against: Nvidia Q2 FY2027 10-Q customer concentration note*
- Ed Zitron (2026-11-10): Nvidia has deployed >$100bn in deals with customers/neoclouds (The Information); rent-backs $1.5bn Lambda, $6.3bn CoreWeave — *check against: CoreWeave 10-Q/8-K; Nvidia 10-Q; repo capex/circular-financing field*

**Other channels.** GDELT "AI bubble" sourcelang:english: 7-day volume 0.0385 against a 90-day mean of 0.0138, z 1.42 (to 20261113).

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-capex (GW deferral - supplier/lab)]: 456X (single source): Broadcom/Anthropic 700 MW TPU deployment pushed from 2027 to 2028 on construction and power permitting; Broadcom 2026-2030 custom-ASIC revenue forecast cut 11% (research)
- 2026-11-16 [C-credit (pulled deal - leveraged loan, private IT services)] late: Citigroup-led banks pull USD 400m five-year UST Global refinancing term loan (S+425-450, OID 98; commitments were due 28 Oct) after demand fell short - a pulled leveraged loan, non-hyperscaler (Briefs
- 2026-11-17 [C-capex (principal demand/guidance - no cut, no digestion)]: Nvidia Q3 FY27 (Tue 17 Nov after close): revenue USD 115.8bn (+103% y/y) vs ~109.1bn est, Data Center 107.6bn, Q4 guide USD 130bn +/-3% (14 weeks, no China DC compute) vs 125.1bn, GM 71-72%; FY28 grow
- 2026-11-17 [C-capex (sell-side/independent forecast cut - not a principa]: SemiAnalysis cuts 2028 global AI-accelerator capex forecast 28% to USD 758bn from 1.054tn (2027 -19% to 627bn, 2026 ~392bn unchanged); Nvidia compute revenue -22% 2027 / -39% 2028; Broadcom custom-ASI
- 2026-11-17 [C-capex (memory LTA - tightening, not renegotiation)] late: Maeil: Samsung and Apple 'poised to sign' a 4-5 year DRAM LTA effective H1 2027 with a minimum-supply floor and pricing set to future market conditions; Apple reportedly already has an SK hynix LTA on

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | B confirmed by Dec 9 (two of five B elements) | open, p 0.071, resolves 2026-12-09 | — |
| fork | B confirmed by Jan 20, 2027 | open, p 0.313, resolves 2027-01-20 | — |
| history | real equity total return over the next three years for states like the present one (analog quartiles) | analogs (n 12): p25 -35.0 / median -1.6 / p75 21.1; climatology median 16.8 (p25 -5.2, p75 41.8) | — |
| history_rate | share of country-years followed by a 30% real equity drawdown within three years, in the current era's climatology | 1999-2020: 24.3% of 304 country-years | — |
| field | CCC spreads in a stress or acute zone | CCC 1314.0 (acute, 98.5th pct; Δ1m 47.0, Δ3m 290.0; 2026-11-12) | yes |
| field | IG OAS through 100 (transmission) | IG 89.0 (watch, 62.1th pct; Δ1m 6.0, Δ3m 10.0; 2026-11-12) | no |
| field | neoclouds underperforming hyperscalers over the month | E7_1m -16.36 (3m -39.1; 2026-11-14): -16.4 1m / -39.1 3m: neoclouds (NBIS -37.7, CRWV -19.2, ORCL -4.0) vs hyperscalers (MSFT -1.8, GOOGL -14.9, AMZN +5.0) - the periphery inside the chain | yes |
| field | high-yield spreads in a stress or acute zone | HY 320.0 (watch, 71.7th pct; Δ1m 4.0, Δ3m 49.0; 2026-11-12) | no |

Evidence tally: 2 of 4 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share 0.5 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** The 2027 capex guides of the principals hold or rise through the Q4 prints with IG below 100, no hyperscaler deal pulled and GPU rental prices flat — the chain keeps paying one more year.

**Incentive tags** (a reader's discount, never the system's): short-sellers and bears talking their book; newsletter writers rewarded for alarm; sell-side bears rewarded for being early once.

## This is 2000 again: a productive bubble whose bust spares the economy and crushes the suppliers

`dotcom-echo` · sign **bear** · lane capital · branch B · lifecycle **held**

As held: buy-the-dip, supply bottlenecks turning into gluts and the belief that the Fed does not matter echo the dot-com peak; the resolution is dual — the cap-weighted index falls while the equal-weighted index and value rise, suppliers are crushed and the users of cheap capacity thrive.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Paul Krugman (1) | — (0) | 1 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 0 | 0 |
| 2026-11-12 (56) | Dario Perkins (1) | — (0) | 1 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Paul Krugman (2026-10-31, bear) [1990s it bubble, 1999]: In his own remarks in the conversation (recorded Oct 29), Krugman says the 1990s IT bubble is a less convincing model than he thought, but he worries about how much capital AI infrastructure absorbs for few jobs, fast chip depreciation (likened to fracking wells), and whether AI firms will capture t…
- Dario Perkins (2026-11-09, bear) [dot-com, echo the dot-com, 2000 in, nasdaq]: Today's conditions echo the dot-com peak: widespread dip-buying, tech supply bottlenecks and confidence that rate hikes would not hurt tech. In 2000 investors 'promptly decided that the Fed didn't matter anymore'; tech shortages can turn quickly into a tech glut. Buying every dip could backfire as r…

**Numbers the holders put on it** (6 in the window, 4 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Paul Krugman (2026-10-31): Total factor productivity about 10% above prior trend by around 2005, with IT-boom gains starting about 1999 — *check against: SF Fed / Fernald TFP series; BLS total factor productivity*
- Dario Perkins (2026-11-09): Fed hiked 25bp Feb 2000, 25bp Mar 2000, 50bp May 2000 to 6.5% before the tech top — *check against: FRED FEDFUNDS / DFEDTAR 2000*
- Dario Perkins (2026-11-09): Nasdaq 100 -6.5% and Nvidia -9.3% on Nov 5 (TipRanks framing) — *check against: FRED NASDAQ100; NVDA close*
- Dario Perkins (2026-11-09): Nvidia quarterly revenue +106% YoY to $96.2bn, data center $89bn; Microsoft Azure +48%, capex $45.2bn (TipRanks context, not Perkins) — *check against: NVDA / MSFT latest 10-Q*

**Other channels.** GDELT "AI bubble" sourcelang:english: 7-day volume 0.0385 against a 90-day mean of 0.0138, z 1.42 (to 20261113).

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-equity (AI complex drawdown / correction)]: Mon 16 Nov AI-complex drawdown: S&P 500 -1.92% (7,416.59), Nasdaq -2.49% (24,509.76, >10% below 6 Oct record = correction), SOX -5.3%, NVDA -4.1% to 156.10 (lowest since Jun 2025), MU -7.62%, VIX 22.9
- 2026-11-17 [C-equity (broadening drawdown - software, financials, breadt]: Tue 17 Nov US close (pre-NVDA): S&P 500 7,340.53 (-1.03%, five-month low), Nasdaq 24,328.38 (-0.74%, fourth straight loss), Dow 50,759.42 (-1.64%), RUT -1.50%, VIX 25.46 (+11.13%, fourth straight gain

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| history | real equity total return over the next three years for states like the present one | analogs (n 12): p25 -35.0 / median -1.6 / p75 21.1; climatology median 16.8 (p25 -5.2, p75 41.8) | — |
| field | equal-weight beating cap-weight over the month (the dual resolution) | E1_1m 6.26 (3m 2.11; 2026-11-14) | yes |
| field | semis underperforming the Nasdaq-100 (suppliers first) | E5_1m -7.08 (3m -10.19; 2026-11-14): SMH -7.1 1m / -10.2 3m vs QQQ: semis breaking ahead of the Nov 17 guide (leading node) | yes |
| field | the index still near its highs (a bust has not begun) | SPX 7561.67 (acute, 95.1th pct; Δ1m -157.27, Δ3m -224.09; 2026-11-13) | yes |

Evidence tally: 3 of 3 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 0 open. Support share 1.0 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** The cap-weighted index makes a new high with the equal-weight index lagging and supplier margins intact a year on — the 2000 analogy had the wrong decade.

**Incentive tags** (a reader's discount, never the system's): strategists rewarded for a memorable analogy; survivors of 2000 generalizing from one cycle.

## AI's financing is circular — suppliers fund their customers — so the chain's interdependence hides its risk

`circular-financing` · sign **bear** · lane capital · branch B · lifecycle **held**

As held: chipmakers and clouds take equity stakes in, extend backstops to and guarantee the obligations of the labs and neoclouds that buy from them, so one demand shortfall at the top becomes a balance-sheet event at every tier; receivables outgrow revenue and the lenders carry equity risk at debt returns.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Howard Marks, James Mackintosh (2) | — (0) | 2 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 0 | 0 |
| 2026-11-12 (56) | Gary Marcus, Michael Burry (2) | — (0) | 3 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- James Mackintosh (2026-11-01, bear) [circular, backstop, funding their own customers, guarantee]: Circular financing in AI, with chip suppliers funding their own customers through equity stakes, backstops and guarantees, reduces diversification because interdependent companies move together. Shareholders should demand a lower premium and consider their exposure if the AI trade falls; he draws th…
- Howard Marks (2026-10-29, bear) [lenders to ai firms, risk better suited to stockholders]: Lenders to AI firms may be taking risk better suited to stockholders, because debt returns are capped while equity shares the upside; "If you want to invest in AI, you should probably buy the stocks." He is not against all AI bonds and loans, but wants the risk matched by adequate reward.
- Michael Burry (2026-11-12, bear) [protection racket]: Free portion: Nvidia's 'protection racket' has lost its enforcer; the DOJ was already probing whether Nvidia abused dominance by bundling GPUs with other products; Huang had as many as 60 direct reports and delegated little, so CFO Kress as interim CEO cannot replace him smoothly; key-person risk at…
- Gary Marcus (2026-11-11, bear) [circular]: WSJ reports Nvidia is about to fire Huang; Nvidia may have little choice given liability and reputational risk. Huang is the 'ringmaster' of AI circular financing and 'the whole thing might collapse'; the open question is whether an acting CEO (possibly the CFO) honours the billions Nvidia reportedl…

**Numbers the holders put on it** (8 in the window, 5 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- James Mackintosh (2026-11-01): Nvidia, AMD and Broadcom took $5 billion in total as cornerstone investors in Meta's $25 billion stock sale — *check against: Meta prospectus supplement / 8-K; chipmaker filings*
- James Mackintosh (2026-11-01): Nvidia provided a $105 billion backstop for an Ohio data center being built for OpenAI by SoftBank's SB Energy — *check against: Nvidia 10-Q commitments and guarantees note; press reports*
- Michael Burry (2026-11-12): Huang had as many as 60 direct reports (per TechCrunch/Axios) — *check against: TechCrunch / Axios reports*
- Michael Burry (2026-11-12): DOJ investigating Nvidia for bundling/abuse of dominant position — *check against: DOJ filings / NVDA 10-K risk disclosures*
- Gary Marcus (2026-11-11): Nvidia committed 'billions' to Anthropic in connection with the IPO — *check against: Anthropic S-1 / Nvidia 8-K; repo circular-financing field*

**Other channels.** GDELT "AI bubble" sourcelang:english: 7-day volume 0.0385 against a 90-day mean of 0.0138, z 1.42 (to 20261113).

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | Nvidia receivables growing faster than revenue a third quarter | open, p 0.6, resolves 2026-11-17 | — |
| fork | the $250bn OpenAI backstop withdrawn or shrunk | open, p 0.2, resolves 2026-11-17 | — |
| hazard | an SPV or lease-accounting story at a hyperscaler | monthly odds 0.12 | — |
| field | suppliers underperforming principals (the market pricing the dependence) | E6_1m -3.28 (3m -19.48; 2026-11-14): -3.3 1m, -19.5 3m (price-computed; basket rule says 3m n/a until 13 weeks): suppliers (MU -14.9, GEV -14.7, VRT -9.3) losing the rent to principals (MSFT -1.8,  | yes |

Evidence tally: 1 of 1 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share 1.0 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** A year of supplier revenue converting to cash at normal ratios, receivable days flat, and no vendor-financed customer defaulting on a vendor.

**Incentive tags** (a reader's discount, never the system's): short-sellers; columnists rewarded for a clean mechanism.

## Only a third of the announced data-center pipeline is credible, and power, permits and voters cap the rest

`credible-pipeline` · sign **bear** · lane capital · branch B · lifecycle **held**

As held: 586 GW is announced and 199 GW is credible; 2027 is locked in by construction already under way but 2028 is not, and the binding constraint has moved from compute to memory to power to politics — the midterms made opposition to data centers bipartisan and the fight moved to governors and town halls.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Ben Thompson, Paul Kedrosky, Paul Krugman, arg: Politics is the binding constraint on AI buildout (4) | — (0) | 10 | 2 |
| 2026-11-09 (58) | Ed Zitron, Paul Kedrosky (2) | — (0) | 11 | 3 |
| 2026-11-12 (56) | arg: Bernstein Research (relayed by 456X, Nov 12): only ~34% (199 GW) of the  (1) | — (0) | 3 | 1 |

**In their words** (the latest matched positions; words that matched in brackets).

- Ben Thompson (2026-11-04, bear) [moratori, binding constraint, oppos, power]: Thompson argues the midterms showed voters in both parties opposing data center construction and that the binding constraint on AI has moved from compute to memory to power and now to politics, which is harder to solve; he sees the AI trade as possibly painful short term (credit tightening the main …
- Ed Zitron (2026-11-06, bear) [voters, power, midterm, governor]: Zitron argues the AI bubble rests on the assumption that the powerful always get what they want, and that the midterm results show voters can say no to data centers; he says the backlash is now bipartisan and that the election could lead to the bubble bursting, since NVIDIA's growth and the AI labs'…
- Paul Kedrosky (2026-11-06, bear) [voters, power, midterm]: Kedrosky models the data center boom as a hybrid public-private stimulus program: hyperscalers supplied capital while governments supplied depreciation, tax credits, abatements, permitting and power access, which made AI capex a material fraction of GDP growth and kept excesses less visible in equit…
- arg: Bernstein Research (relayed by 456X, Nov 12): only ~34% (199 GW) of the  (2026-11-12, bear) [credible, 586 gw, 199 gw,  gw]: Planned North American data-center capacity rose from 411 GW (July) to 586 GW (October), but Bernstein classes only 199 GW (~34%) as credible, a share that held steady as the pipeline grew; of 87 GW under construction 75 GW is credible, of 497 GW merely announced only 123 GW qualifies. Neoclouds are…

**Numbers the holders put on it** (25 in the window, 7 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Paul Krugman (2026-10-29): Announced plans imply the largest investment boom in U.S. history as a share of GDP (Van Nieuwerburgh projection, Brookings paper, Sept 2026; values in chart only) — *check against: Brookings Papers Sept 2026 (Van Nieuwerburgh); BEA NIPA private fixed investment in info processing *
- Paul Krugman (2026-10-29): Oracle's Project Jupiter (New Mexico) hit by repeated gas-pipeline permit rejections; force majeure filing reported 2026-09-24 — *check against: Oracle SEC filings; Bloomberg 2026-09-24*
- Ed Zitron (2026-11-06): Texas: 57.7GW of planned IT capacity, more than half being built by first-time developers (citing Bloomberg) — *check against: Bloomberg reporting; ERCOT large-load interconnection queue*
- Paul Kedrosky (2026-11-06): AI capex became a material fraction of GDP growth (no figure given in readable portion) — *check against: BEA NIPA: private fixed investment in information processing equipment and software, contributions t*
- arg: Bernstein Research (relayed by 456X (2026-11-12): 586 GW announced NA pipeline (Oct) vs 411 GW (Jul); 199 GW credible (~34%) — *check against: Bernstein note / repo data-center pipeline field*
- arg: Bernstein Research (relayed by 456X (2026-11-12): CBRE: 1.4% vacancy top-8 markets; 10.9 GW operational, +33.7% y/y; 80.4% of 7.48 GW under construction pre-leased — *check against: CBRE H1 2026 data-center report*

**Other channels.** GDELT "data center" capex sourcelang:english: 7-day volume 0.0173 against a 90-day mean of 0.0127, z 0.34 (to 20261114).

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-capex (principal asset recycling / sale-leaseback funding)]: Amazon/AWS sells 75% of two JVs holding 13 powered-shell data centers (~647 MW) to Blackstone's BXDC for ~USD 5bn at a 7.0% initial cap rate; 12/32-year triple-net leaseback; AWS keeps 25%; ~USD 2.5bn
- 2026-11-16 [C-capex (GW deferral - supplier/lab)]: 456X (single source): Broadcom/Anthropic 700 MW TPU deployment pushed from 2027 to 2028 on construction and power permitting; Broadcom 2026-2030 custom-ASIC revenue forecast cut 11% (research)
- 2026-11-17 [C-capex (principal demand/guidance - no cut, no digestion)]: Nvidia Q3 FY27 (Tue 17 Nov after close): revenue USD 115.8bn (+103% y/y) vs ~109.1bn est, Data Center 107.6bn, Q4 guide USD 130bn +/-3% (14 weeks, no China DC compute) vs 125.1bn, GM 71-72%; FY28 grow
- 2026-11-17 [C-capex (sell-side/independent forecast cut - not a principa]: SemiAnalysis cuts 2028 global AI-accelerator capex forecast 28% to USD 758bn from 1.054tn (2027 -19% to 627bn, 2026 ~392bn unchanged); Nvidia compute revenue -22% 2027 / -39% 2028; Broadcom custom-ASI
- 2026-11-17 [C-capex (memory LTA - tightening, not renegotiation)] late: Maeil: Samsung and Apple 'poised to sign' a 4-5 year DRAM LTA effective H1 2027 with a minimum-supply floor and pricing set to future market conditions; Apple reportedly already has an SK hynix LTA on

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| stage | supply under contract and under construction against the announced pipeline (the stage read) | late - supply under contract: Samsung/Hynix/Kioxia LTAs >50% of 2027-28; 56.7 GW under construction vs 586 GW announced (Bernstein 34% credible); pause pledges  | — |
| fork | a principal's capex cut, deferral or restraint language | open, p 0.09, resolves 2026-12-14 | — |
| hazard | rental prices falling as less capacity than announced arrives | monthly odds 0.04 | — |

Evidence tally: 0 of 0 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 1 open. Support share — (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** 2028 capacity starts tracking the announced pipeline — under-construction GW rising toward the announced total through 2027 with permits and power contracts signed.

**Incentive tags** (a reader's discount, never the system's): sell-side research rewarded for a proprietary count; political commentators generalizing one election.

## The selloff is a rotation inside a continuing cycle: a correction's last stage, semis oversold, the buildout mid-way

`flight-to-quality` · sign **bull** · lane strategist · branch A · lifecycle **growing**

As held: the clearing events (midterms, AI equity supply, liquidity) are passing; the correction that began in June is in its final stage and sets up a year-end rally; semis are oversold; the buildout is roughly mid-way and the hyperscalers' books are full — buy the dip.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Mike Wilson, arg: AI pessimism is overdone: forward multiples are reasonable (2) | Michael Hartnett (1) | 4 | 1 |
| 2026-11-09 (58) | Mike Wilson (1) | arg: Hartnett: stay risk-off until three conditions reverse tighter financial (1) | 4 | 2 |
| 2026-11-12 (56) | Azeem Azhar, Mike Wilson, arg: James Schneider (Goldman Sachs, Nov 10): semiconductor stocks are 'clear, arg: Quinlan / Hyzy (BofA Merrill CIO): the AI buildout is roughly mid-way, b (4) | Dario Perkins (1) | 5 | 2 |

**In their words** (the latest matched positions; words that matched in brackets).

- Azeem Azhar (2026-11-10, bull) [flight to quality, not a collapse]: Two chaotic weeks - Nasdaq-100's worst day since March 2020 after the Democrats' midterm win, then the Huang/Chinese-spy story - but this is a 'flight to quality', not a collapse: spending keeps rising, Democratic policy makes data centers pricier (favouring hyperscalers), Nvidia and the open-weight…
- Mike Wilson (2026-11-09, bull) [final stage, last stage, year-end rally, bottoming]: The correction is in its last stage and sets up a year-end rally; the S&P 500 may approach his 7,100-7,300 downside range before bottoming, but 'this is the place where you should be adding risk over the next two to three weeks.' From the note: rather than waiting for a perfect bottom, increase expo…
- arg: Quinlan / Hyzy (BofA Merrill CIO): the AI buildout is roughly mid-way, b (2026-11-09, bull) [mid-way, constructive]: The authors view the AI buildout as roughly mid-way; the 15 largest data-center developers are expected to spend over $1.4T in 2027 (~3.5-4% of US GDP), AI-tied firms have raised over $460B of debt YTD (more than double 2025), top-rated data-center bond yields have risen from below 5% to ~7%, and th…
- arg: James Schneider (Goldman Sachs, Nov 10): semiconductor stocks are 'clear (2026-11-10, bull) [oversold, top picks]: Schneider's top picks are Nvidia, Broadcom and AMD; he values Nvidia and Broadcom at ~12x and ~13x a 'no growth' 2028 baseline and calls semis clearly oversold. Same relay: Nvidia closed 168.89 (-5.47%) with RSI ~23, its most oversold since June 2019; Nasdaq ~11% below its Oct 6 record; Nicholas Col…

**Numbers the holders put on it** (36 in the window, 24 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- arg: Quinlan / Hyzy (BofA Merrill CIO):  (2026-11-09): AI-tied firms raised >$460B debt YTD, >2x 2025 — *check against: issuance tallies (repo issuance field)*
- arg: Quinlan / Hyzy (BofA Merrill CIO):  (2026-11-09): Highest-rated data-center bond yields ~7% vs <5% at start of year — *check against: bond pricing / FRED IG yield series*
- arg: Quinlan / Hyzy (BofA Merrill CIO):  (2026-11-09): Q3 GDP 3.4%; 10-yr 4.86% and 30-yr 5.26% at Nov 6 close; HY yield 8.21% — *check against: FRED GDPC1, DGS10, DGS30, BAMLH0A0HYM2EY*
- arg: Quinlan / Hyzy (BofA Merrill CIO):  (2026-11-09): Fed funds forecast 4.13% end-2026, 4.38% end-2027 — *check against: FRED DFEDTARU*
- arg: James Schneider (Goldman Sachs, Nov (2026-11-10): Oct CPI +0.4% m/m headline, +0.3% core (consensus +0.3/+0.2) — *check against: FRED CPIAUCSL / CPILFESL*
- arg: James Schneider (Goldman Sachs, Nov (2026-11-10): Post-CPI yields: 5-yr 4.75%, 10-yr 4.93%, 30-yr 5.29% — *check against: FRED DGS5 / DGS10 / DGS30*

**Other channels.** GDELT "AI bubble" sourcelang:english: 7-day volume 0.0385 against a 90-day mean of 0.0138, z 1.42 (to 20261113); sell side: 88.8% buy ratings, median target upside 69%.

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-equity (AI complex drawdown / correction)]: Mon 16 Nov AI-complex drawdown: S&P 500 -1.92% (7,416.59), Nasdaq -2.49% (24,509.76, >10% below 6 Oct record = correction), SOX -5.3%, NVDA -4.1% to 156.10 (lowest since Jun 2025), MU -7.62%, VIX 22.9
- 2026-11-17 [C-equity (broadening drawdown - software, financials, breadt]: Tue 17 Nov US close (pre-NVDA): S&P 500 7,340.53 (-1.03%, five-month low), Nasdaq 24,328.38 (-0.74%, fourth straight loss), Dow 50,759.42 (-1.64%), RUT -1.50%, VIX 25.46 (+11.13%, fourth straight gain

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork_nonfire | B not confirmed by Dec 9 | open, p 0.071, resolves 2026-12-09 | — |
| history | real equity total return over the next year for states like the present one | analogs (n 13): p25 11.1 / median 18.3 / p75 21.1; climatology median 6.2 (p25 -5.0, p75 17.3) | — |
| field | the index within reach of its highs | SPX 7561.67 (acute, 95.1th pct; Δ1m -157.27, Δ3m -224.09; 2026-11-13) | yes |
| field | IG spreads below the transmission line | IG 89.0 (watch, 62.1th pct; Δ1m 6.0, Δ3m 10.0; 2026-11-12) | yes |
| field | claims benign (no labour transmission) | ICSA_4wk 200.0 (benign, 7.1th pct; Δ1m 2.0, Δ3m -12.0; 2026-11-07) | yes |

Evidence tally: 3 of 3 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 1 open. Support share 1.0 (counted, not weighted).

The system's own position: branch A at 79.9 (H2) / 67.4 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** The index fails to make a new high within two quarters while credit transmits (IG through 100 and a hyperscaler deal pulled) — the correction was the first stage, not the last.

**Incentive tags** (a reader's discount, never the system's): sell-side strategists whose house is long; sell-side analysts with buy ratings on the names; fund managers marketing a dip-buying product.

## Demand exceeds supply through FY28 and consensus is too low: the supplier supercycle holds

`nvidia-supercycle` · sign **bull** · lane capital · branch A · lifecycle **growing**

As held: Nvidia's supply commitments and third-party benchmarks support 70% growth in 2027 and revenue 72% above consensus in FY28; the memory makers are sold out through 2028; 'demand continues to exceed supply'.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | — (0) | — (0) | 2 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 2 | 0 |
| 2026-11-12 (56) | arg: James Schneider (Goldman Sachs, Nov 10): semiconductor stocks are 'clear, arg: Morgan Stanley (relayed by 456X, Nov 11): reiterates a $300 Nvidia price (2) | — (0) | 4 | 4 |

**In their words** (the latest matched positions; words that matched in brackets).

- arg: James Schneider (Goldman Sachs, Nov 10): semiconductor stocks are 'clear (2026-11-10, bull) [no-growth 2028, nvidia, broadcom]: Schneider's top picks are Nvidia, Broadcom and AMD; he values Nvidia and Broadcom at ~12x and ~13x a 'no growth' 2028 baseline and calls semis clearly oversold. Same relay: Nvidia closed 168.89 (-5.47%) with RSI ~23, its most oversold since June 2019; Nasdaq ~11% below its Oct 6 record; Nicholas Col…
- arg: Morgan Stanley (relayed by 456X, Nov 11): reiterates a $300 Nvidia price (2026-11-11, bull) [$300 , 72% above consensus, supply commitments, nvidia]: Morgan Stanley holds a $300 target on Nvidia and models 70% revenue growth in 2027; its FY28 revenue forecast of $698.34B sits 72% above consensus, resting on Nvidia's supply commitments rising from $119B to $279B in one quarter (mostly 2027-28 memory procurement) and third-party benchmarks showing …

**Numbers the holders put on it** (8 in the window, 5 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- arg: James Schneider (Goldman Sachs, Nov (2026-11-10): Oct CPI +0.4% m/m headline, +0.3% core (consensus +0.3/+0.2) — *check against: FRED CPIAUCSL / CPILFESL*
- arg: James Schneider (Goldman Sachs, Nov (2026-11-10): Post-CPI yields: 5-yr 4.75%, 10-yr 4.93%, 30-yr 5.29% — *check against: FRED DGS5 / DGS10 / DGS30*
- arg: Morgan Stanley (relayed by 456X, No (2026-11-11): Nvidia supply commitments $119B -> $279B in one quarter — *check against: Nvidia 10-Q purchase obligations*
- arg: Morgan Stanley (relayed by 456X, No (2026-11-11): Vertiv Q3 backlog ~$26.5B; TTM bookings $30.1B vs NTM revenue consensus $18.4B — *check against: Vertiv 10-Q / earnings release*
- arg: Morgan Stanley (relayed by 456X, No (2026-11-11): Hyperscaler cloud backlog $1.8T at Q3, +~140% y/y (per Nov 12 relay) — *check against: AWS/Azure/GCP RPO disclosures in 10-Qs*

**Other channels.** sell side: 88.8% buy ratings, median target upside 69%.

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-capex (principal asset recycling / sale-leaseback funding)]: Amazon/AWS sells 75% of two JVs holding 13 powered-shell data centers (~647 MW) to Blackstone's BXDC for ~USD 5bn at a 7.0% initial cap rate; 12/32-year triple-net leaseback; AWS keeps 25%; ~USD 2.5bn
- 2026-11-16 [C-capex (GW deferral - supplier/lab)]: 456X (single source): Broadcom/Anthropic 700 MW TPU deployment pushed from 2027 to 2028 on construction and power permitting; Broadcom 2026-2030 custom-ASIC revenue forecast cut 11% (research)
- 2026-11-17 [C-capex (principal demand/guidance - no cut, no digestion)]: Nvidia Q3 FY27 (Tue 17 Nov after close): revenue USD 115.8bn (+103% y/y) vs ~109.1bn est, Data Center 107.6bn, Q4 guide USD 130bn +/-3% (14 weeks, no China DC compute) vs 125.1bn, GM 71-72%; FY28 grow
- 2026-11-17 [C-capex (sell-side/independent forecast cut - not a principa]: SemiAnalysis cuts 2028 global AI-accelerator capex forecast 28% to USD 758bn from 1.054tn (2027 -19% to 627bn, 2026 ~392bn unchanged); Nvidia compute revenue -22% 2027 / -39% 2028; Broadcom custom-ASI
- 2026-11-17 [C-capex (memory LTA - tightening, not renegotiation)] late: Maeil: Samsung and Apple 'poised to sign' a 4-5 year DRAM LTA effective H1 2027 with a minimum-supply floor and pricing set to future market conditions; Apple reportedly already has an SK hynix LTA on

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork_nonfire | Nvidia guides at or above consensus (the fork does not fire) | open, p 0.25, resolves 2026-11-17 | — |
| fork_nonfire | Micron guides at or above consensus with no renegotiation language | open, p 0.15, resolves 2026-12-17 | — |
| field | suppliers keeping pace with principals | E6_1m -3.28 (3m -19.48; 2026-11-14): -3.3 1m, -19.5 3m (price-computed; basket rule says 3m n/a until 13 weeks): suppliers (MU -14.9, GEV -14.7, VRT -9.3) losing the rent to principals (MSFT -1.8,  | no |

Evidence tally: 0 of 1 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share 0.0 (counted, not weighted).

The system's own position: branch A at 79.9 (H2) / 67.4 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** A guide below consensus, receivables and inventory outgrowing revenue for a third quarter, or a memory contract renegotiated — the supplier is the last node, so this is the slow falsifier.

**Incentive tags** (a reader's discount, never the system's): sell-side with buy ratings and price targets; the company's own forward statements (G1/G2 bias).

## Deficits at full employment, thinning auction demand and a rising term premium: the long end is the fault line

`debt-crunch` · sign **bear-bonds** · lane debt · branch C · lifecycle **held**

As held: divided government adds spending, the debt-limit and funding fights of 2027 push short yields up and raise doubts about Treasuries as collateral; auctions tail with the indirect bid thinning; record tech bond supply competes for the same liability-matching money; foreign official accounts are selling.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | James Mackintosh, Jim Grant, Michael Hartnett, arg: Record bond supply led by tech is repricing data center credit (4) | — (0) | 7 | 1 |
| 2026-11-09 (58) | arg: Franco: divided government adds spending, widening deficits and pushing  (1) | — (0) | 3 | 1 |
| 2026-11-12 (56) | Ray Dalio, arg: US Treasury $42B 10-year auction result (relayed by TokenPost / hererock (2) | — (0) | 3 | 1 |

**In their words** (the latest matched positions; words that matched in brackets).

- Jim Grant (2026-10-29, bear-bonds) [bond supply, yields, 30-year]: ADG records the weight of AI-related bond supply: a jumbo Microsoft deal, record year-to-date global issuance and blue-chip data center bond yields moving toward 7%. It also notes the Fed's balance sheet is growing again since December.
- arg: Franco: divided government adds spending, widening deficits and pushing  (2026-11-05, bear-bonds) [term premium, debt limit, widening deficits, treasury]: Democrats take Congress with the government still borrowing about $2 trillion a year; their leverage comes from deadlines rather than votes, divided government is more likely to add spending than cut it, and that widens deficits and pushes up the term premium while fiscal policy turns from a boost i…
- Ray Dalio (2026-11-09, bear-bonds) [debt-limit, funding expiry, safe collateral, treasury]: The election changes who handles the problems (debt, wealth/values gap, geopolitics, climate, technology), not the problems; he expects brutal fights over spending and taxes around the Dec 11 funding expiry, a March 2027 debt-limit hit and a fall-2027 point where Treasury runs out of options, pushin…
- arg: US Treasury $42B 10-year auction result (relayed by TokenPost / hererock (2026-11-10, bear-bonds) [auction, indirect, tail, treasury]: The $42B 10-year note sold at a 5.02% high yield, 1bp above the 5.01% when-issued (largest tail since February), bid-to-cover 2.46 (2.77 in October; lowest since May), indirects 61.2% (80.3% in October; lowest since October 2023), directs 29% (highest since September 2013), dealers 9.8%. Monday's $5…

**Numbers the holders put on it** (35 in the window, 21 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Ray Dalio (2026-11-09): Federal debt projected to hit its limit in March 2027 — *check against: FiscalData Debt to the Penny vs statutory limit; CBO/BPC X-date estimates*
- Ray Dalio (2026-11-09): Treasury projected to run out of funding options (X-date) in fall 2027 — *check against: CBO / Bipartisan Policy Center X-date projections; FiscalData TGA cash balance*
- arg: US Treasury $42B 10-year auction re (2026-11-10): 10-yr high yield 5.020%, WI 5.010%, tail 1.0bp — *check against: TreasuryDirect auction results / repo auction field*
- arg: US Treasury $42B 10-year auction re (2026-11-10): Bid-to-cover 2.46 vs 2.77 Oct; indirects 61.2% vs 80.3%; directs 29.0%; dealers 9.8% — *check against: TreasuryDirect auction results*
- arg: US Treasury $42B 10-year auction re (2026-11-10): 3-yr Nov 9: 4.627% high yield, b/c 2.53 — *check against: TreasuryDirect auction results*
- arg: US Treasury $42B 10-year auction re (2026-11-10): Oct CPI +0.4% m/m, core +0.3%; 2-yr yield +17bp on the day — *check against: FRED CPIAUCSL / CPILFESL / DGS2*

**Other channels.** GDELT ("term premium" OR "Treasury auction") sourcelang:english: 7-day volume 0.0059 against a 90-day mean of 0.006, z -0.02 (to 20261112).

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [B-sovereign (UST)]: UST close Mon 16 Nov: 10y 5.12% (-3bp; Tradeweb 5.115 vs 5.152 Fri), 2y 4.83% (-5bp), 30y 5.46% (-1bp), 2s10s ~29bp - first down day after a 29bp five-session rise; Dec 25bp hike fully priced, 50bp ~8
- 2026-11-16 [B-sovereign (JGB/JPY, gilts)]: JGB 10y 2.885% Mon 16 Nov (highest since 22 Oct), 30y 4.04%, 40y 4.18%; Nikkei -2.42% to 59,662 (below 60,000); Tue 17 Nov Asia: KOSPI -2.59% to 4,968, Nikkei 58,925 (-1.24%) at 02:05Z; USD/JPY ~159.4
- 2026-11-17 [B-sovereign (UST)]: UST close Tue 17 Nov: 2y 4.80% (-3bp), 10y 5.10% (-2bp), 30y 5.46% (unch); 6-week bill USD 100bn 4.055% 2.82x 'in line' (no tail for bills); DXY 103.55-103.61 highest since Apr 2025; Musalem: several 
- 2026-11-18 [B-sovereign (JGB auction tail / long end)]: JGB 20y auction Wed 18 Nov weak: JPY 525.8bn, bid-to-cover 3.64 vs 5.84 prior (12m avg 3.92), tail 0.29 yen vs 0.07 (widest in a year), avg yield 3.756%; 20y yield 3.785%, 10y eased to 2.865% on forei
- 2026-11-18 [B-sovereign (EM FX defence / rate hike)]: Bank Indonesia surprise 25bp hike to 6.00% Wed 18 Nov (22 of 38 expected hold; fourth hike since May, +125bp cumulative) after rupiah record low 18,285/USD Tue; rupiah +0.2% after; BI cuts NDF hedging

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | C confirmed by Dec 9 | open, p 0.02, resolves 2026-12-09 | — |
| fork | 30y reopening tails 2 bp or more | open, p 0.25, resolves 2026-12-10 | — |
| fork | 10y reopening tails 2 bp or more | open, p 0.25, resolves 2026-12-08 | — |
| history | change in the long rate over the next year for states like the present one | analogs (n 15): p25 -0.5 / median -0.1 / p75 0.2; climatology median -0.0 (p25 -0.3, p75 0.2) | — |
| field | the 30-year yield in a stress or acute zone | DGS30 5.43 (acute, 99.0th pct; Δ1m -0.13, Δ3m 0.22; 2026-11-12) | yes |
| field | the real 10-year in a stress or acute zone | DFII10 2.86 (acute, 99.3th pct; Δ1m -0.02, Δ3m 0.47; 2026-11-12) | yes |

Evidence tally: 2 of 2 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 3 open. Support share 1.0 (counted, not weighted).

The system's own position: branch C at 1.0 (H2) / 1.1 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Two refunding cycles with no tail above 2 bp, the term premium below 1 and the 30-year back inside its watch band while deficits stay above 6% — the buyers are still there.

**Incentive tags** (a reader's discount, never the system's): bond bears and gold holders; debt-cycle authors whose framework needs the crunch; newsletter writers rewarded for alarm.

## The Fed hikes into a slowing, lagging-data economy — the 2018 path, with 25 versus 50 the live question

`fed-policy-error` · sign **bear** · lane business · branch B · lifecycle **held**

As held: with headline inflation re-accelerating on oil and fiscal, the Fed is hiking into a boom that ignores the funds rate, so the squeeze lands on housing, autos and the periphery; the survey data it steers by are deteriorating.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Michael Hartnett, Paul Krugman (2) | — (0) | 7 | 1 |
| 2026-11-09 (58) | Michael Hartnett, arg: Franco: divided government adds spending, widening deficits and pushing , arg: Hartnett: stay risk-off until three conditions reverse tighter financial (3) | — (0) | 5 | 3 |
| 2026-11-12 (56) | Dario Perkins, Jim Grant (Almost Daily Grant's; ADG byline is Philip Grant) (2) | arg: James Schneider (Goldman Sachs, Nov 10): semiconductor stocks are 'clear, arg: Quinlan / Hyzy (BofA Merrill CIO): the AI buildout is roughly mid-way, b (2) | 6 | 2 |

**In their words** (the latest matched positions; words that matched in brackets).

- arg: Franco: divided government adds spending, widening deficits and pushing  (2026-11-05, bear-bonds) [hike, fed ]: Democrats take Congress with the government still borrowing about $2 trillion a year; their leverage comes from deadlines rather than votes, divided government is more likely to add spending than cut it, and that widens deficits and pushes up the term premium while fiscal policy turns from a boost i…
- Dario Perkins (2026-11-09, bear) [hike, 25bp, 50bp, fed ]: Today's conditions echo the dot-com peak: widespread dip-buying, tech supply bottlenecks and confidence that rate hikes would not hurt tech. In 2000 investors 'promptly decided that the Fed didn't matter anymore'; tech shortages can turn quickly into a tech glut. Buying every dip could backfire as r…
- Jim Grant (Almost Daily Grant's; ADG byline is Philip Grant) (2026-11-10, bear-bonds) [hike, 25bp, 50bp, fed ]: 'The Staples Singers': defensives rallied as tech sold off, but staples and healthcare now look expensive for safety-seekers. 'Restructural Integrity': private-credit stress is building with record defaults, and a hot CPI makes further Fed tightening more likely. Recap: stocks shrugged off CPI but T…
- Jim Grant (Almost Daily Grant's; ADG byline is Philip Grant) (2026-11-09, bear-bonds) [fed lacks clean data, response rates are collapsing, fed , cpi]: 'Further Study is Required': the Fed lacks clean data for its next move - labor-survey response rates are collapsing, the October CPI has no year-over-year print after last fall's shutdown, and rising inflation expectations strengthen the case for tighter policy. Recap: stocks rebounded hard after T…

**Numbers the holders put on it** (59 in the window, 23 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-10): KBRA: 112 private-credit borrowers in default trailing 12m through Q3 (record, +22% vs year to June); Fitch private default rate 6.3% Sept vs 6% three months earlier, 5th straight quarterly rise — *check against: KBRA / Fitch private credit default reports*
- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-10): Core October CPI +0.3% m/m; futures imply 4.16% fed funds after December vs 3.75-4.00% current; 25bp hike near certain, >10% odds of 50bp — *check against: FRED CPILFESL (Oct 2026), DFEDTARU; CME FedWatch*
- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-10): Nov 10: S&P 500 -0.4%; long bond 5.35%; 2-yr 4.73% from 4.56%; WTI just under $87; gold $4,032 (-2%); BTC <$74k (3-month low); VIX <20 — *check against: FRED SP500, DGS2, DGS30, DCOILWTICO*
- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-09): October payrolls +165k vs 74k expected; unemployment 4.1% vs 4.2% consensus — *check against: FRED PAYEMS, UNRATE (Oct 2026)*
- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-09): BLS aggregate initial response rate just below 60% vs ~80% 2014-pandemic — *check against: BLS survey response rates*
- Jim Grant (Almost Daily Grant's; ADG byl (2026-11-09): Nov 9: S&P 500 +2.4%; NVDA -4.2%; 2-yr 4.56% (+5bp); long bond 5.26%; WTI $87; gold $4,141; BTC <$75k; VIX just under 20 — *check against: FRED SP500, DGS2, DGS30, DCOILWTICO*

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | a December hike with claims more than 10% above the low | open, p 0.08, resolves 2026-12-09 | — |
| fork | November core CPI at 0.4 or more | open, p 0.25, resolves 2026-12-10 | — |
| history | the change in unemployment over the next three years for states like the present one | analogs (n 13): p25 -2.4 / median -1.3 / p75 -0.8; climatology median 0.0 (p25 -1.1, p75 1.1) | — |
| field | claims rising into a stress zone (the error showing up) | ICSA_4wk 200.0 (benign, 7.1th pct; Δ1m 2.0, Δ3m -12.0; 2026-11-07) | no |
| field | real yields acute (the hurdle binding) | DFII10 2.86 (acute, 99.3th pct; Δ1m -0.02, Δ3m 0.47; 2026-11-12) | yes |

Evidence tally: 1 of 2 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share 0.5 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Claims stay within 10% of their low through two more hikes and core inflation falls back under 0.3 a month — the hikes were absorbed.

**Incentive tags** (a reader's discount, never the system's): rates strategists whose book is long duration; commentators rewarded for calling the Fed wrong.

## Households keep spending across income groups while saying they are miserable; the economy is not the AI complex

`consumer-resilient` · sign **bull** · lane business · branch A · lifecycle **growing**

As held: weekly retail sales are strong, supported by job growth for lower-income households and by asset prices and fixed-income cash flows above them, while confidence falls across the distribution; earnings pace implies nominal growth near 10%.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | — (0) | — (0) | 3 | 1 |
| 2026-11-09 (58) | — (0) | — (0) | 5 | 2 |
| 2026-11-12 (56) | arg: Slok (Apollo Daily Spark, Nov 11): weekly retail sales remain strong acr (1) | — (0) | 2 | 1 |

**In their words** (the latest matched positions; words that matched in brackets).

- Michael Hartnett (2026-11-06, bear) [consumer, payroll]: Stay risk-off until three things reverse the tightening in financial conditions: central bank rate hikes end, the 10-year Treasury yield falls below 4.5%, and oil drops below $80; if November inflation and payrolls are weak, the December Fed/ECB/BoJ hikes could be the last and a year-end risk rally …
- arg: Hartnett: stay risk-off until three conditions reverse tighter financial (2026-11-06, bear) [consumer, payroll]: Investors should stay risk-off until the central-bank hiking cycle ends, the 10-year Treasury yield falls below 4.5% and oil falls below $80; the midterms mark a 'shift from populist capitalism to populist socialism' in which affordability policy challenges the consumer and AI capex booms, favouring…
- arg: Redwood: AI revenue will not grow fast enough to support current investm (2026-11-06, bear) [spending, payroll]: AI should lift productivity, but AI revenue is unlikely to grow fast enough to support current levels of investment; if revenue lags, AI capital spending slows and that could weigh on US growth next year.
- Torsten Slok (2026-11-11, n/a) [retail sales, same-store, what consumers are saying, consumer]: Weekly same-store retail sales remain strong, supported by job growth for lower-income households and by high asset prices and fixed-income cash flows for middle/higher-income households, while consumer confidence keeps falling across all income groups; 'a significant difference between what consume…

**Numbers the holders put on it** (2 in the window, 2 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- arg: Slok (Apollo Daily Spark, Nov 11):  (2026-11-11): Redbook weekly same-store retail sales strong (chart, no figure in text) — *check against: Redbook weekly index / FRED RSXFS proxy*
- arg: Slok (Apollo Daily Spark, Nov 11):  (2026-11-11): Consumer sentiment declining across income tiers (chart, no figure) — *check against: FRED UMCSENT / Conference Board*

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| history | real GDP per head over the next year for states like the present one | analogs (n 15): p25 1.0 / median 1.7 / p75 2.9; climatology median 2.0 (p25 0.1, p75 4.0) | — |
| field | claims benign | ICSA_4wk 200.0 (benign, 7.1th pct; Δ1m 2.0, Δ3m -12.0; 2026-11-07) | yes |
| field | homebuilders keeping pace with the index | E8_1m 11.92 (3m -3.54; 2026-11-14): XHB +9.9 1m, +11.9 vs SPY: the rate-sensitive sector rallied as mortgage rates fell 29 bp to 7.11 - the G4 squeeze eased on the month; the week's +26 bp reverse | yes |

Evidence tally: 2 of 2 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 0 open. Support share 1.0 (counted, not weighted).

The system's own position: branch A at 79.9 (H2) / 67.4 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Claims up 20% from the low and real retail sales down two quarters running.

**Incentive tags** (a reader's discount, never the system's): asset managers whose products are long the cycle; chief economists of firms that lend to the consumer.

## Prices are not reflecting fundamentals: unprofitable companies outperform and AI productivity is absent from the 493

`price-discovery-broken` · sign **bear** · lane strategist · branch B · lifecycle **held**

As held: revenue per worker and margins rise for the Mag 7 and are flat for the S&P 493; there are no signs of AI boosting productivity; unprofitable companies keep outperforming profitable ones; the benefits are concentrated in the companies selling AI.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Gary Marcus, Paul Kedrosky, Torsten Slok (3) | — (0) | 3 | 0 |
| 2026-11-09 (58) | Gary Marcus (1) | — (0) | 1 | 0 |
| 2026-11-12 (56) | Torsten Slok (1) | — (0) | 1 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Gary Marcus (2026-10-24, bear) [net detriment]: Generative AI has 'on the whole been a net detriment to society': harms (hacks, deepfakes, disinformation) are mounting while expected economic benefits, per Torsten Slok, are not materialising. He acknowledges real value mainly in coding and warns of turbulence ahead.
- Torsten Slok (2026-10-24, bear) [no signs of ai boosting productivity, s&p 493, productivity, margins]: Revenue per worker and profit margins are rising for the Mag 7 but flat for the S&P 493, and "There are still no signs of AI boosting productivity growth"; corporate America still has to turn cheap intelligence into higher revenue growth and margins, and mainstream firms are starting to treat token …
- Gary Marcus (2026-11-06, bear) [not delivering the productivity, productivity]: Says the previous day's $2.5 trillion drop was only part of the bad news, pointing also to a Bank of England study showing, once again, that AI is not delivering the productivity gains people had expected. The subtitle promises five predictions, which are behind the subscribe wall and were not read.
- Torsten Slok (2026-11-09, bear) [price discovery, unprofitable companies, fundamentals]: Price discovery is malfunctioning: unprofitable companies keep outperforming profitable ones, so prices are not reflecting fundamentals. Single chart: 'Unprofitable small caps outperforming profitable small caps' (Bloomberg, Apollo Chief Economist).

**Numbers the holders put on it** (11 in the window, 4 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Paul Kedrosky (2026-10-29): Oracle '$220 Billion' appears in item 7's title only; context paywalled — *check against: Oracle 10-Q (RPO, debt, lease commitments) — which metric is unknown*
- Torsten Slok (2026-10-24): No pickup in US productivity growth (output per hour and total factor productivity, chart from Jan 1985) — *check against: BLS productivity; FRED OPHNFB; SF Fed TFP series*
- Gary Marcus (2026-11-06): Markets dropped $2.5 trillion 'yesterday' (2026-11-05) — *check against: Nasdaq / US equity market-cap change on 2026-11-05 (exchange data; FRED NASDAQCOM, SP500 for index m*
- Torsten Slok (2026-11-09): Unprofitable small caps outperforming profitable small caps (chart only; page text gives no return figures or window - chart image not readable) — *check against: Russell 2000 profitable vs unprofitable cohort returns (Bloomberg); not a repo field*

**Other channels.** GDELT "AI bubble" sourcelang:english: 7-day volume 0.0385 against a 90-day mean of 0.0138, z 1.42 (to 20261113).

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| field | equal-weight lagging cap-weight (the 493 not catching up) | E1_1m 6.26 (3m 2.11; 2026-11-14) | no |
| field | the top eight outrunning the equal-weight index | E2_1m -9.38 (3m -0.2; 2026-11-14) | no |
| stage | supplier margins at prior-cycle peaks | late - supplier margins at prior-cycle peaks (SK hynix OP 80%, Micron GM 86.8%, NVDA GM 75%; E6 3m -19.5 says the market is pricing mean-reversion) | — |

Evidence tally: 0 of 2 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 0 open. Support share 0.0 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Two quarters of 493 earnings acceleration with margins rising outside the AI complex, or measured productivity turning up in the national accounts.

**Incentive tags** (a reader's discount, never the system's): AI skeptics with a position to defend; economists rewarded for contrarian productivity calls.

## Stress is surfacing in private credit and leveraged loans: BDC marks, non-accruals, pulled deals, force majeure

`private-credit-stress` · sign **bear** · lane credit · branch B · lifecycle **fading**

As held: BDC loan marks are dispersing, the share of leveraged loans above par is collapsing, AI-related force-majeure clauses are appearing in sponsored loans ahead of a maturity wall, and CCC stress is reaching single-B through three channels.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Dario Perkins, Howard Marks, Jim Grant, Paul Krugman (4) | — (0) | 6 | 0 |
| 2026-11-09 (58) | arg: Slok: three channels by which CCC stress reaches single-B (1) | — (0) | 8 | 1 |
| 2026-11-12 (56) | — (0) | — (0) | 0 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Howard Marks (2026-10-29, bear) [loan, lender]: Lenders to AI firms may be taking risk better suited to stockholders, because debt returns are capped while equity shares the upside; "If you want to invest in AI, you should probably buy the stocks." He is not against all AI bonds and loans, but wants the risk matched by adequate reward.
- Dario Perkins (2026-10-23, bear) [private credit]: In his wargame the AI crash scenario is "now overdetermined": US stocks fall 30%, a cyclical downturn is inevitable as capex and construction jobs fall, but the recession is not especially severe because the Fed has room to cut. Investors should stay diversified globally, not bet against tech too ea…
- Jim Grant (2026-11-02, bear) [bdc, leveraged loan, loan]: ADG tallies widening dispersion in BDC loan marks and a deteriorating leveraged loan market, with the share of loans trading above par collapsing since late September and the sub-80-cent share roughly doubling this year.
- Jim Grant (2026-10-27, bear) [private credit, force majeure, maturity wall, loan]: ADG flags an AI-related force majeure clause appearing in a private-equity-sponsored loan ahead of a heavy sub-investment-grade maturity wall with large software exposure. It also notes the NAIC backing down on scrutiny of private-credit ratings from smaller agencies.

**Numbers the holders put on it** (18 in the window, 10 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Dario Perkins (2026-10-23): Tech companies invest about $1 trillion a year; AI companies expected to issue about $700 billion of bonds in 2027, $400 billion from hyperscalers — *check against: Hyperscaler capex in 10-Qs; SIFMA / Dealogic issuance*
- Jim Grant (2026-11-02): BDC loans whose marks vary by 5 or more points rose to 12.3% from 9.3%; sub-80-cent marks rose to 5.9% from 4.2% (Frankfurt School research) — *check against: Frankfurt School study; BDC 10-Q schedules of investments*
- Jim Grant (2026-11-02): Recap 2 Nov: 2-year at 4.59%, 30-year at 5.28%, VIX near 22 — *check against: FRED DGS2, DGS30, VIXCLS*
- Jim Grant (2026-10-27): A 2024 study found private-loan ratings from three smaller firms averaged three notches above the NAIC's in-house ratings; those firms rated 86% of insurers' private credit holdings — *check against: NAIC Capital Markets Bureau reports*
- Jim Grant (2026-10-27): Recap 27 Oct: 2-year about 4.7%, 30-year about 5.3% — *check against: FRED DGS2, DGS30*
- arg: Slok: three channels by which CCC s (2026-11-05): Spread between CCC and single-B at 1000bps (chart title) — *check against: FRED BAMLH0A3HYC (ICE BofA CCC & lower OAS) minus BAMLH0A2HYB (single-B OAS)*

**Other channels.** GDELT "private credit" (redemption OR gating) sourcelang:english: 7-day volume 0.0016 against a 90-day mean of 0.0018, z -0.26 (to 20261108).

**Event-sweep hits mapped to this narrative** (dated evidence, not holders).

- 2026-11-16 [C-credit (pulled deal - leveraged loan, private IT services)] late: Citigroup-led banks pull USD 400m five-year UST Global refinancing term loan (S+425-450, OID 98; commitments were due 28 Oct) after demand fell short - a pulled leveraged loan, non-hyperscaler (Briefs

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| field | CCC in a stress or acute zone | CCC 1314.0 (acute, 98.5th pct; Δ1m 47.0, Δ3m 290.0; 2026-11-12) | yes |
| field | single-B spreads in a stress or acute zone (the loan market's own rung) | singleB 339.0 (stress, 82.1th pct; Δ1m 22.0, Δ3m 51.0; 2026-11-12) | yes |
| field | high yield in a stress or acute zone | HY 320.0 (watch, 71.7th pct; Δ1m 4.0, Δ3m 49.0; 2026-11-12) | no |
| field | transmission to IG | IG 89.0 (watch, 62.1th pct; Δ1m 6.0, Δ3m 10.0; 2026-11-12) | no |
| hazard | a neocloud or AI-credit event | monthly odds 0.07 | — |
| fork | CoreWeave's secured loan pulled, repriced or downsized | open, p 0.2, resolves 2026-11-30 | — |

Evidence tally: 2 of 4 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 1 open. Support share 0.5 (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Non-accruals flat for two quarters, the above-par share recovering and the loan market absorbing the maturity wall at unchanged spreads.

**Incentive tags** (a reader's discount, never the system's): newsletter writers rewarded for alarm; credit funds marketing distressed products.

## Key-person and governance risk at Nvidia: the chief is gone, the backstop and the China channel are in question

`nvidia-governance` · sign **bear** · lane capital · branch B · lifecycle **growing**

As held: the chief executive's departure removes the enforcer of Nvidia's commercial system and its chief salesman; an interim chief cannot replace sixty direct reports; the DOJ probe and the China-sales question outlast him, and the $250bn backstop proposal is in question.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | — (0) | — (0) | 0 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 0 | 0 |
| 2026-11-12 (56) | Ed Zitron, Gary Marcus, Michael Burry (3) | Azeem Azhar, Gavin Baker (2) | 12 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Michael Burry (2026-11-12, bear) [huang, kress, key-person, interim]: Free portion: Nvidia's 'protection racket' has lost its enforcer; the DOJ was already probing whether Nvidia abused dominance by bundling GPUs with other products; Huang had as many as 60 direct reports and delegated little, so CFO Kress as interim CEO cannot replace him smoothly; key-person risk at…
- Ed Zitron (2026-11-10, bear) [huang, megaspeed, doj, affair]: Huang's affair with Megaspeed CEO Alice Huang is a symptom of a larger scheme: Megaspeed functioned as a transshipment entity funnelling sanctioned Nvidia GPUs into China, Nvidia knew about it as far back as 2024 and interfered with Commerce's probe, and Nvidia's earnings were inflated by more than …

**Numbers the holders put on it** (14 in the window, 9 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Ed Zitron (2026-11-10): $2.4bn of Nvidia 'Bianca' boards unaccounted for at sites reported to Washington — *check against: Bloomberg reporting; Commerce/BIS*
- Ed Zitron (2026-11-10): Culper: ~20% of Nvidia FY2026 revenue (~$43.18bn) from China; Megaspeed imported 50,000 more GPUs than Nvidia told the government — *check against: Nvidia FY2026 10-K geographic revenue note; Culper_NVDA_5-13-2026 report*
- Ed Zitron (2026-11-10): 44% of Nvidia 1H FY2027 revenue from three customers; Q2 FY2027: 70% of receivables from three customers, 16% of revenue from one — *check against: Nvidia Q2 FY2027 10-Q customer concentration note*
- Ed Zitron (2026-11-10): Nvidia has deployed >$100bn in deals with customers/neoclouds (The Information); rent-backs $1.5bn Lambda, $6.3bn CoreWeave — *check against: CoreWeave 10-Q/8-K; Nvidia 10-Q; repo capex/circular-financing field*
- Gary Marcus (2026-11-11): Nvidia committed 'billions' to Anthropic in connection with the IPO — *check against: Anthropic S-1 / Nvidia 8-K; repo circular-financing field*
- Gary Marcus (2026-11-09): Nasdaq 100 futures fell >1% on initial reaction to the confession (Kobeissi Letter) — *check against: NQ futures Sun-night Nov 8/9; repo equity-lens field*

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | the backstop withdrawn or shrunk | open, p 0.2, resolves 2026-11-17 | — |
| hazard | a governance shock outside the print | monthly odds 0.12 | — |
| fork | a guide below consensus under the interim chief | open, p 0.25, resolves 2026-11-17 | — |

Evidence tally: 0 of 0 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share — (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** Two clean quarters under the new chief with the backstop intact and no DOJ action.

**Incentive tags** (a reader's discount, never the system's): short-sellers; political commentators on the China question.

## The Hormuz standoff sets an oil floor that feeds headline inflation and the Fed's path; a signing breaks it

`oil-floor-hormuz` · sign **neutral** · lane business · branch standoff · lifecycle **fading**

As held by the standoff watch and the roster: with the strait constrained, Brent carries a physical premium that passes into headline CPI and keeps the Fed in hike-into-floor mode; a written agreement would take 20% off oil and move the business cycle toward A, while escalation would do the reverse.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | — (0) | — (0) | 5 | 0 |
| 2026-11-09 (58) | Michael Hartnett, Mike Wilson, arg: Hartnett: stay risk-off until three conditions reverse tighter financial (3) | — (0) | 5 | 1 |
| 2026-11-12 (56) | — (0) | — (0) | 0 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Michael Hartnett (2026-11-06, bear) [oil, energy, barrel]: Stay risk-off until three things reverse the tightening in financial conditions: central bank rate hikes end, the 10-year Treasury yield falls below 4.5%, and oil drops below $80; if November inflation and payrolls are weak, the December Fed/ECB/BoJ hikes could be the last and a year-end risk rally …
- Mike Wilson (2026-11-06, bull) [iran]: He called Thursday's (Nov 5) index selloff "likely the final stage of this correction" but wants further confirmation from his sentiment indicator before adding risk; the 8,000 year-end S&P 500 base case stays. His team also frames financial conditions as doing the Fed's work, liquidity as a remaini…
- arg: Hartnett: stay risk-off until three conditions reverse tighter financial (2026-11-06, bear) [oil, energy, barrel]: Investors should stay risk-off until the central-bank hiking cycle ends, the 10-year Treasury yield falls below 4.5% and oil falls below $80; the midterms mark a 'shift from populist capitalism to populist socialism' in which affordability policy challenges the consumer and AI capex booms, favouring…

**Numbers the holders put on it** (33 in the window, 7 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Mike Wilson (2026-11-06): S&P 500 year-end 2026 base case 8,000, about +8.4% from Friday Nov 6 close (secondary's arithmetic) — *check against: S&P 500 close 2026-11-06 (FRED SP500)*
- Mike Wilson (2026-11-06): Nov 2 Weekly Warm-up downside tactical target for S&P 500 of 7,100-7,300 before adding risk more aggressively; S&P 500 closed 7,353.73 on Nov 5 after a 4.4% one-day decline from 7,688.62 on Nov 4 (Fou — *check against: FRED SP500 daily closes*
- arg: Hartnett: stay risk-off until three (2026-11-06): Risk-on condition: 10-year US Treasury yield below 4.5% — *check against: FRED DGS10*
- arg: Hartnett: stay risk-off until three (2026-11-06): Risk-on condition: oil below $80 a barrel — *check against: FRED DCOILWTICO / DCOILBRENTEU*
- arg: Hartnett: stay risk-off until three (2026-11-06): Week to Nov 4, 2026: money market funds +$140.4bn, equities +$89.2bn, bonds +$11.6bn, gold +$0.1bn, crypto -$1.8bn — *check against: EPFR weekly flows as reported in BofA Flow Show; ICI weekly money market fund assets*
- arg: Hartnett: stay risk-off until three (2026-11-06): If November inflation and payrolls are weak, December hikes from Fed, ECB and BoJ could be the last; year-end rally could start around Thanksgiving — *check against: FOMC/ECB/BoJ December decisions; BLS CPI and payrolls*

**Other channels.** GDELT "Strait of Hormuz" sourcelang:english: 7-day volume 0.396 against a 90-day mean of 0.4691, z -0.38 (to 20261115).

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | a written US-Iran agreement by Dec 9 | open, p 0.15, resolves 2026-12-09 | — |
| fork | the standoff's E criteria or Brent at 120 by Dec 9 | open, p 0.35, resolves 2026-12-09 | — |
| field | oil in a stress or acute zone (the floor holding) | WTI 89.62 (stress, 81.8th pct; Δ1m -5.37, Δ3m 4.65; 2026-11-11) | yes |

Evidence tally: 1 of 1 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 2 open. Support share 1.0 (counted, not weighted).

The system's own position (the standoff watch's export): H2 E 45, F 35, R+ 5, R- 15; H3 E 50, F 30, R+ 5, R- 15 — printed here as one more holder.

**Falsifier.** Brent below 80 for a month with the strait still constrained — the floor was supply elsewhere, not Hormuz.

**Incentive tags** (a reader's discount, never the system's): energy strategists; governments on both sides.

## SpaceX is the fastest data-center builder ever — or its revenue math is not remotely close

`spacex-compute-bet` · sign **contested** · lane capital · branch B · lifecycle **fading**

As held on one side: SpaceX reaches 10-13 GW in 2027, the fastest buildout in history; on the other: its revenue goal implies a 1-2x revenue-to-investment ratio against an industry at 0.3x, the chip debt is a $500bn question and the funding is a fuse.

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | Dylan Patel, Ed Zitron, Jim Chanos (3) | — (0) | 5 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 1 | 0 |
| 2026-11-12 (56) | — (0) | — (0) | 1 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Ed Zitron (2026-11-03, bear) [spacex]: Zitron argues the AI bubble collapses when the money runs out: debt markets are closing to AI infrastructure and venture capital is drying up; OpenAI's raise fell short of target, Anthropic's amended S-1 shows compute costs rising faster than revenue with enormous commitments, and hyperscaler revenu…
- Ed Zitron (2026-10-28, bear) [spacex]: Zitron argues Anthropic's S-1 describes a company that won't exist once it is public: Q2 2026 was profitable only because of discounted SpaceX compute, commitments ramp sharply from mid-2026, and the IPO and lock-up schedule let insiders sell to retail investors as 'exit liquidity' within a broader …
- Jim Chanos (2026-10-26, bear) [spacex, chip debt, musk]: After Musk confirmed SpaceX's chip debt, Chanos asked what share of the 10 GW of capacity SpaceX is building in 2027 is terrestrial, calling it "a pretty material $500B question."
- Jim Chanos (2026-10-26, bear) [spacex, not even remotely close, revenue-to-investment, musk]: Musk's revenue goal implies a 1-2x revenue-to-investment ratio while the industry is at about 0.3x, and SpaceX is "not even remotely close" even with the Google and Anthropic deals. Its Q3 annualized AI revenue per MW is well below the figures cited during the quarter.

**Numbers the holders put on it** (32 in the window, 19 naming a series or filing to check against; six shown, checkable ones first — the raw material for the narrative's own predictions).

- Ed Zitron (2026-10-28): 5-7% of Anthropic revenue (~$1.65B-$2.31B, nine months to Sep 30, 2026) from distillation / policy-violating usage — *check against: Anthropic S-1 risk factors*
- Ed Zitron (2026-10-28): Meta equity raise of ~$97.5B via at-the-market offering in 2026 — *check against: Meta 424B5 prospectus supplements / 10-Q*
- Ed Zitron (2026-10-28): Magnificent Seven capex over $1 trillion — *check against: Company 10-Ks/10-Qs, capex lines*
- Ed Zitron (2026-10-28): OpenAI and Anthropic combined obligations over $1.3T — *check against: Anthropic S-1; reported OpenAI commitments*
- Jim Chanos (2026-10-26): 10 GW of capacity being built by SpaceX in 2027 — *check against: SpaceX 10-Q / earnings materials*
- Jim Chanos (2026-10-26): SpaceX Q3 2026 AI capex was $16 billion — *check against: SpaceX Q3 2026 10-Q / earnings release*

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|
| fork | the $40bn GPU financing: no tranche priced, pulled, downsized or sweetened by Dec 31 | open, p 0.3, resolves 2026-12-31 | — |

Evidence tally: 0 of 0 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 1 open. Support share — (counted, not weighted).

The system's own position: branch B at 18.9 (H2) / 31.3 (H3) in run `2026-11-14T0611-dials` — printed here as one more holder, scored like the rest.

**Falsifier.** For the bull side: the financing fails or the GW target slips a year; for the bear side: the tranches price at or inside talk and the 2027 capacity is delivered.

**Incentive tags** (a reader's discount, never the system's): the company's own statements; short-sellers; semiconductor analysts with access to the supply chain.

## China holds hidden foreign-exchange assets that underpin a weak renminbi and its export outperformance

`china-hidden-fx` · sign **n/a** · lane debt · branch none · lifecycle **unheld (mentions only)**

As held: FX settlement purchases of $500-600bn a year against a flat PBOC balance sheet, missing reinvested interest and entrusted loans to the policy banks add up to a trillion-dollar gap; the pattern looks like backdoor intervention around a crawling peg.

*Tracked for bandwidth; no measurable prediction in the dials yet (no renminbi or reserves field).*

**Holders by sweep.**

| sweep (items) | holders | opposed | mentions | arguments |
|---|---|---|---|---|
| 2026-11-05 (76) | — (0) | — (0) | 1 | 0 |
| 2026-11-09 (58) | — (0) | — (0) | 0 | 0 |
| 2026-11-12 (56) | — (0) | — (0) | 1 | 0 |

**In their words** (the latest matched positions; words that matched in brackets).

- Brad Setser (2026-11-02, n/a) [renminbi, china, export]: The EU-China auto deal (a quota on Chinese hybrids) is a reasonable first step that stops the immediate import surge but is not a full answer: China's export surge is driven by collapsing domestic demand and massive excess capacity, Europe lacks a broad Section 301-style instrument and conditions on…
- Brad Setser (2026-11-11, n/a) [hidden foreign, hidden reserves, fx settlement, china]: The PBOC says it has no hidden reserves, but Setser argues it has hidden foreign-currency assets: FX settlement purchases of $500-600bn over the last 12 months against a ~$50bn rise in the PBOC balance sheet, a cumulative unexplained gap near $1 trillion, missing reinvested interest income (~$100bn/…

**Predictions and what the data say now.**

| kind | prediction | reading | supports? |
|---|---|---|---|

Evidence tally: 0 of 0 field conditions in the predicted direction; 0 of 0 resolved forks supporting; 0 open. Support share — (counted, not weighted).

**Falsifier.** A PBOC disclosure reconciling the gap, or the renminbi floating outside the band without intervention.

**Incentive tags** (a reader's discount, never the system's): policy analysts; trade-policy advocates.

## Reading rules

- Holders are counted, never weighted: a narrative held by five newsletter writers and one by two asset managers print as 5 and 2.
- Mentions include opposed and neutral items; the holder count is the narrative's bandwidth among the roster, the opposed count a proxy for its opposition (opposite sign, strong word).
- The sweeps differ in size (the item count is printed beside each date), so a fall in holders can be a smaller sweep; `bandwidth.csv` carries holders as a share of the sweep's items as well. The lifecycle label is computed on raw counts and is a description, not a forecast.
- GDELT z is the 7-day volume against the trailing 90 days of non-zero days; the orchestrator's N1 uses the same files (its MA4 and z3m differ in window).
- A prediction's 'supports' is a counted condition (a field zone, a resolved fork), not an inference; open forks print their registered probability, which is the orchestrator's judgment (see the bias log).
- The history legs are what followed states like the present one in the 18-country record; they are base rates, not forecasts.
- Nothing here changes a branch weight. The ledger is the stated side of G3 made explicit and scorable.
