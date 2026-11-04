<!-- Encoding written from the source document in our own words with page citations; the source text is not reproduced. Provenance class: stated (a voice's template and reads). See history/sources.json. -->

# Big Debt Crises, Part 3 (second half): Non-Domestic-Currency Debt Crises — PDF pages 363–480

Source: Ray Dalio, *Principles for Navigating Big Debt Crises* (Bridgewater, 2018), free PDF edition. Part 3 printed page = PDF page − 258. This file covers printed pages 105–221: the 26 cases from Argentina 1980 to Russia 2014 (the "Non-Domestic Currency Debt Crises (Typically Inflationary Deleveragings)" group, minus Germany 1918 which is on printed p. 99, PDF 357, outside this range), the Appendix on Macroprudential Policies, the endnotes, and the Disclosures page.

Companion CSV: `bdc_cases.csv` (64 columns, 26 rows); column list in `bdc_cases_schema.md`.

---

## 0. What the compendium template actually is in this edition (important for the analog index)

**There is no separate statistics table per case in the free PDF.** Every case occupies exactly four pages:

1. **"[Country] [years] Case Auto-Summary"** (page 1): a one-sentence classification, then three narrative sections, *The Bubble Phase* and *The Depression Phase*, with the statistics embedded in fixed template sentences; right column: three gauge charts (**Bubble & Depression Gauge**, **Tightening & Easing Gauge**, **Core Inflation (Y/Y)**) and a stacked bar, **Deleveraging Attribution: Depression Period** (legend: Real Growth, Inflation, Chg in Dom. Debt, FX Debt Chg due to FX Move, FX Debt Chg due to Other, Debt %GDP diamond marker giving the annualized change in debt as % of GDP). A footnote explains that the two gauges measure bubble/depression conditions and tightness/easiness of money and credit; distance from zero is the extent, crossing zero is entry/exit. Header note: the gauges are composed from the chart-deck statistics and are meant as rough measures.
2. **"... Case Auto-Summary (cont.)"** (page 2): *The Reflation Phase* narrative plus **Deleveraging Attribution: Reflation Period** (same legend). Some cases end with a one-paragraph political note (a populist leader the crisis helped bring to power).
3. **"... Chart Deck Appendix"** (page 3), three rows of charts:
   - *Indebtedness*: Total Debt (%GDP) with Debt Service (%GDP); FX Debt (%GDP); Chg in Debt-GDP Ratio (Ann) with Debt Growth (%GDP, Ann).
   - *Monetary and Fiscal Policy*: Nominal Short Rate; Money0 Level (%GDP); Fiscal Balance (%GDP).
   - *Economic Conditions*: Real GDP (Indexed); Real Growth (Y/Y); GDP Gap; Core Inflation (Y/Y); Nominal Long Rate with Nominal Growth; Real Short Rate.
4. **"... Chart Deck Appendix (cont.)"** (page 4):
   - *Markets*: Equity Price USD (Indexed); Nominal Long Rate with Nominal Short Rate; Yield Curve (SR-LR); Real FX vs TWI; FX Return for Foreign Investors (Indexed); Gold Price (Local FX, Indexed).
   - *External Position*: Reserves (USD, Indexed); Capital Inflows (%GDP); Imports (%GDP); Current Account (%GDP); Capital Outflows (%GDP); Exports (%GDP).
   Charts carry vertical lines at the phase boundaries; a 15-year x-axis window is used (start dates listed per case below). Charts with no data are printed as "No Data Available".

**The narrative template (the de-facto statistics table).** Paraphrased slot structure, in order of appearance; the CSV columns follow this order:

- Opening: "[Country] experienced a **classic inflationary** / **classic hyperinflationary** / **transitory inflationary** deleveraging cycle between [start] and [end]." Transitory cases add that the country is a classic example of "letting its currency go" in the face of external pressures, which produces temporary inflation but gives policy makers more flexibility on interest rates.
- Bubble phase: either "Between [y1] and [y2] ... a bubble ... driven by a self-reinforcing cycle of [drivers]" or "Unlike many other cases, [Country] didn't experience a broad-based bubble ... but it was tied to other countries/markets experiencing bubble-like conditions" / "...built up a substantial debt stock". Slots: debts rose by **X% of GDP during the bubble** to a **pre-crisis peak of X% of GDP**; **foreign-currency debt X% of GDP**; **investment inflows averaging X% of GDP**; **current account deficit X% of GDP**; **growth X%**; **GDP gap peaked at X%**; **equities averaged X% annualized returns over the bubble**; **real FX peaked at +X%**.
- Depression phase: "...a balance of payments/currency crisis, which ran from [y2] to [y3]"; **debt service at pre-crisis peak X% of GDP**; the **shock**; **capital inflows falling by X% of GDP**; **policy makers hiked short rates by X%**; **real FX fell by X%**; **GDP falling by X%**; **stock prices falling by X%**; (home prices falling by X%); **unemployment rates increased by X%**; **inflation peaking at X% during the depression phase, which is high/normal/low compared to other similar cases**; share of the classic "risk factors" for bigger inflation spirals (**most / around half / only about a quarter**) with the **biggest risk factor** named; central bank **drew down reserves by X%** before abandoning its currency defense (sometimes "the currency had fallen by X%"); **debt as % GDP went up by X% (X% annualized)** / was roughly flat / fell by X%, attributed to the currency fall and/or government borrowing, with a **peak fiscal deficit of X% of GDP**.
- Reflation phase: a fixed sentence about the key determinant being whether policy makers let the currency go and allow tightening to flow through or print money. Then either (a) "they abandoned the currency peg and, after a **relatively short / slightly shorter than average / slightly longer than average / relatively long** 'ugly' phase, allowed enough tightening to reduce imports (**current account improved by X% of GDP**)" or (b) hyperinflation branch: "the tightening wasn't enough ... spiral of declining exchange rates and hyperinflation. **Real FX bottomed at -X%** and **inflation peaked at over X%**", with the risk-factor sentence here instead of in the depression. Then: **[very aggressive / aggressive / somewhat aggressive / not aggressive]** in managing financial institutions and bad debts, **pulling N out of 9 classic policy levers**, naming nationalized banks / provided liquidity / directly purchased troubled assets; **IMF assistance program**; **structural reforms to increase labor market flexibility**; (hyperinflation cases) stopping the spiral required abandoning the hyperinflated currency and adopting a new one; **debt as % of GDP fell by X% (X% annualized)**; reduction came mostly from **nominal income rising** (driven primarily by higher real growth / higher inflation) or a balanced mix of outright debt reduction and rising income; **real FX bottoming at -X% during the "beautiful" period**; **X years before real GDP reached its prior peak**; **equity prices in USD recovered within X years**.

Where the text omits a slot, the CSV cell is blank. Where the attribution chart's diamond gives an annualized number the text does not state, I used the chart value and said so in `data_notes`.

**Grouping.** All 26 cases in this range sit in the book's second group, "Non-Domestic Currency Debt Crises (Typically Inflationary Deleveragings)". The book's own sub-classification (first sentence of each case):
- classic inflationary (8): Brazil 1977, Chile 1978, Mexico 1979, Peru 1980, Turkey 1990, Mexico 1991, Ecuador 1995, Turkey 1997;
- classic hyperinflationary (5): Argentina 1977, Peru 1986, Argentina 1987, Brazil 1987, Bulgaria 1995;
- transitory inflationary / "letting its currency go" (13): Philippines 1979, Malaysia 1981, Thailand 1993, Indonesia 1994, Korea 1994, Malaysia 1994, Philippines 1994, Russia 1996, Colombia 1995, Argentina 1998, Iceland 2005, Russia 2005, Russia 2012.

---

## 1. Case notes (26 cases)

Format: phases; bubble; depression; reflation and policy mix; the lesson as the book frames it; chart window; pages (PDF / printed).

### 1. Argentina 1977–1988 — classic hyperinflationary — PDF 363–366 / p. 105–108
- Phases: bubble 1977–1980; depression 1980–1985; reflation 1985–1988. Chart window 1975-07 to 1990-07.
- Bubble: debt peak 39% of GDP, FX debt 15%; inflows ~2% of GDP; growth 2%; GDP gap peak 8%; equities 52%/yr; real FX peak +70%.
- Depression (shock: 1980s LatAm debt crisis): inflows −9% of GDP; short rates hiked >250%; real FX −93%; GDP −14%; stocks −91%; unemployment +3; reserves −83%; debt/GDP +33% (+7% ann.); peak fiscal deficit 5%.
- Reflation: hyperinflation spiral; real FX bottom −138%; inflation peak >1,000%; around half of risk factors (biggest: low real short rates). Policy: somewhat aggressive, 3/9 levers (nationalized banks, provided liquidity); IMF program; peso ley abandoned for peso argentino (1983). Real GDP peak regained after 7 years. Chart: reflation debt change −16% ann.
- Lesson (book framing): tightening that fails to produce adjustment ends in a currency/inflation spiral; stopping it needs structural change including a new currency.

### 2. Brazil 1977–1987 — classic inflationary — PDF 367–370 / p. 109–112
- Phases: no bubble dates; depression 1980–1983; reflation 1983–1987. Window 1975-05 to 1990-05.
- Pre-crisis: no broad-based bubble; debt 158% of GDP, FX debt 70%; CA deficit 5%; inflows ~6% of GDP.
- Depression (LatAm debt crisis): inflows −5%; rates +234%; real FX −20%; GDP −6%; stocks −51%; inflation peak 124% (high); most risk factors (low real short rates); reserves −70%; debt/GDP +54% (+18% ann.); fiscal deficit 11%.
- Reflation: peg abandoned; ugly phase slightly longer than average; CA +3% of GDP; aggressive, 4/9 levers (nationalized banks, liquidity); IMF. Debt/GDP −121% (−27% ann.), mostly nominal income; real FX bottom −33%; GDP peak 4 yrs; USD equities 1.9 yrs.

### 3. Chile 1978–1995 — classic inflationary — PDF 371–374 / p. 113–116
- Phases: bubble 1978–1981; depression 1981–1985; reflation 1985–1995. Window 1976-11 to 1991-11.
- Bubble: debt +86% of GDP to 145%; FX debt 32%; inflows ~14%; CA deficit 11%; growth 7%; gap 11%; equities 36%/yr; real FX +36%.
- Depression (LatAm debt crisis): debt service 45% of GDP; inflows −40%; rates +31%; real FX −50%; GDP −14%; stocks −74%; inflation peak 33% (normal); most risk factors (long history of poorly-controlled inflation); reserves −53%; debt/GDP +73% (+19% ann.); fiscal deficit 4%.
- Reflation: peg abandoned; ugly phase slightly longer; CA +11%; aggressive, 5/9 (provided liquidity, directly purchased troubled assets); IMF; labor-market reforms. Debt/GDP −129% (−13% ann.); real FX bottom −32%; GDP peak 5 yrs; equities 9 yrs.

### 4. Mexico 1979–1991 — classic inflationary — PDF 375–378 / p. 117–120
- Phases: bubble 1979–1981; depression 1981–1987; reflation 1987–1991. Window 1976-11 to 1991-11.
- Bubble: debt peak 65%; FX 26%; inflows ~8%; CA deficit 6%; growth 9%; gap 9%; real FX +30%.
- Depression (LatAm debt crisis + falling oil): debt service 31%; inflows −17%; rates +128%; real FX −74%; GDP −7%; stocks −86%; inflation peak 151% (high); most risk factors (fiscal deficit); reserves −66%; debt/GDP +41% (+7% ann.); fiscal deficit 13%.
- Reflation: peg abandoned; relatively long ugly phase; CA +10%; not aggressive, 2/9; IMF; labor reforms. Debt/GDP −31% (−8% ann.); real FX bottom −44%; GDP peak 7 yrs; equities 6 yrs.

### 5. Peru 1980–1986 — classic inflationary — PDF 379–382 / p. 121–124
- Phases: no bubble dates; depression 1982–1985; reflation 1985–1986. Window 1976-12 to 1991-12.
- Pre-crisis: debt 107%; FX debt 106%; CA deficit 4%.
- Depression (LatAm debt crisis): GDP −13%; stocks −56%; unemployment +5; inflation peak 190% (high); most risk factors (low real short rates); reserves −44%; currency −53% by the time defense abandoned; debt/GDP +163% (+42% ann.); fiscal deficit 5%.
- Reflation: peg abandoned; ugly phase slightly longer; CA +13%; somewhat aggressive 3/9 (nationalized banks, liquidity); IMF; labor reforms. Debt/GDP −88% (−88% ann., one-year phase); real FX bottom −46%; GDP peak 4 yrs; equities 6 yrs. Political: set stage for Alan Garcia Perez.

### 6. Philippines 1979–1992 — transitory inflationary ("letting its currency go") — PDF 383–386 / p. 125–128
- Phases: bubble 1979–1982; depression 1982–1984; reflation 1984–1992. Window 1977-09 to 1992-09.
- Bubble: debt +16% to 77%; FX 56%; inflows ~9%; CA deficit 7%; growth 4%; gap 9%; real FX +18%.
- Depression (falling commodity prices + political violence): inflows −9%; rates +34%; real FX −16%; GDP −11%; stocks −71%; inflation peak 58% (normal); around half of risk factors (high foreign-denominated debts); reserves −100%; debt/GDP roughly flat (chart 0%).
- Reflation: peg abandoned; ugly phase slightly shorter; CA +7%; very aggressive 7/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −9% (−1% ann.); real FX bottom −19%; GDP peak 6 yrs; equities 5 yrs.

### 7. Malaysia 1981–1990 — transitory inflationary — PDF 387–390 / p. 129–132
- Phases: bubble 1981–1984; depression 1984–1987; reflation 1987–1990. Window 1979-06 to 1994-06.
- Bubble: debt +40% to 153%; FX 42%; inflows ~14%; CA deficit 10%; growth 7%; gap 3%; real FX +20%.
- Depression (commodity price declines hitting exports): inflows −11%; real FX −19%; stocks −56%; unemployment +2; reserves −26%; debt/GDP +43% (+17% ann.); fiscal deficit 10%. No GDP decline, rate hike or inflation peak stated.
- Reflation: peg abandoned; ugly phase slightly shorter; CA +9%; aggressive 5/9 (nationalized banks, liquidity); no IMF mentioned. Debt/GDP −74% (−21% ann.), driven by real growth; real FX bottom −12%; GDP peak 1.8 yrs; equities 6 yrs.

### 8. Peru 1986–1995 — classic hyperinflationary — PDF 391–394 / p. 133–136
- Phases: bubble 1986–1987; depression 1987–1990; reflation 1990–1995. Window 1981-12 to 1996-12.
- Bubble: debt +55% to 184%; FX 182%; CA deficit 3%; growth 5%; gap 11%; equities 124%/yr.
- Depression (leadership unwilling to cooperate with international creditors): GDP −30%; stocks −91%; debt/GDP −106% (−30% ann.) via inflation (ugly deleveraging).
- Reflation: hyperinflation spiral; real FX bottom −115%; inflation >10,000%; most risk factors (low real short rates); somewhat aggressive 3/9 (nationalized banks, liquidity); labor reforms; inti abandoned for the sol (1991). GDP peak 9 yrs. Chart: reflation −9% ann.

### 9. Argentina 1987–1993 — classic hyperinflationary — PDF 395–398 / p. 137–140
- Phases: no bubble dates; depression 1987–1990; reflation 1990–1993. Window 1982-06 to 1997-06.
- Pre-crisis: debt +15% to 70% during a leveraging-up; FX 39%; structural weaknesses.
- Depression (commodity price declines): inflows −4%; rates >250%; real FX −60%; GDP −16%; stocks −33%; unemployment +3; reserves −26%; debt/GDP −30% (−11% ann.) via inflation.
- Reflation: spiral; real FX bottom −135%; inflation >10,000%; around half of risk factors (long inflation history); somewhat aggressive 3/9; IMF; labor reforms; austral abandoned for the current peso, initially dollar-pegged. GDP peak 4 yrs; equities 2 yrs. Chart: reflation +7% ann. Political: Carlos Menem.

### 10. Brazil 1987–1995 — classic hyperinflationary — PDF 399–402 / p. 141–144
- Phases: bubble 1987–1990; depression 1990–1991; reflation 1991–1995. Window 1984-12 to 1999-12.
- Bubble: debt +69% to 177%; FX 26%; inflows ~−3%; growth 3%; gap 7%; equities 16%/yr; real FX +35%.
- Depression (collapse of price controls + inflation shock): GDP −7%; stocks −70%; unemployment +4; reserves −28%; currency −19%; debt/GDP +40% (+37% ann.); fiscal deficit 19%.
- Reflation: spiral; real FX bottom −16%; inflation >5,000%; most risk factors (long inflation history); not aggressive 2/9; IMF; labor reforms; cruzado → cruzeiro → real (1994). GDP peak 1.4 yrs; equities 3 yrs. Chart: reflation −27% ann.

### 11. Turkey 1990–1995 — classic inflationary — PDF 403–406 / p. 145–148
- Phases: no bubble dates; depression 1993–1994; reflation 1994–1995. Window 1988-11 to 2003-11.
- Pre-crisis: debt 41%; FX 26%; inflows ~2%.
- Depression (government undermining central-bank independence): inflows −8%; rates +203%; real FX −26%; GDP −12%; stocks −70%; inflation peak 117% (high); only a quarter of risk factors (long inflation history); reserves −99%; debt/GDP +9% (+17% ann.).
- Reflation: relatively short ugly phase; CA +5%; somewhat aggressive 3/9; IMF. Debt/GDP −11% (−7% ann.); real FX bottom −21%; GDP peak 1.6 yrs; equities 4 yrs.

### 12. Mexico 1991–2005 — classic inflationary — PDF 407–410 / p. 149–152
- Phases: bubble 1991–1994; depression 1994–1995; reflation 1995–2005. Window 1989-08 to 2004-08.
- Bubble: debt +10% to 85%; FX 25%; inflows ~8%; CA deficit 7%; growth 4%; gap 3%; equities 25%/yr.
- Depression (outbreak of political violence): GDP −10%; stocks −66%; unemployment +3; inflation peak 43% (normal); around half of risk factors (long inflation history); reserves −100%; currency −37%; debt/GDP roughly flat (chart 1%).
- Reflation: peg abandoned; relatively short ugly phase; CA +7%; very aggressive 6/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −41% (−4% ann.); real FX bottom −26%; GDP peak 2 yrs; equities 10 yrs.

### 13. Bulgaria 1995–2003 — classic hyperinflationary — PDF 411–414 / p. 153–156
- Phases: no bubble dates; depression 1995–1997; reflation 1997–2003. Window 1989-12 to 2004-12.
- Pre-crisis: FX debt 82%; CA deficit 4% (no total-debt peak stated).
- Depression (wave of losses at over-indebted companies/banks): inflows −6%; rates +228%; real FX −96%; GDP −13%; reserves −75%. Chart: +13% ann.
- Reflation: spiral; real FX bottom −63%; inflation >500%; most risk factors (long inflation history); aggressive 5/9 (nationalized banks, liquidity, asset purchases); IMF; lev redenominated, pegged to the Deutsche Mark and backed by FX reserves. GDP peak 8 yrs. Chart: −13% ann. Equity chart: No Data Available.

### 14. Thailand 1993–2004 — transitory inflationary — PDF 415–418 / p. 157–160
- Phases: bubble 1993–1996; depression 1996–1998; reflation 1998–2004. Window 1991-05 to 2006-05.
- Bubble: debt +44% to 183%; FX 51%; inflows ~15%; CA deficit 9%; growth 8%; gap 8%; equities 12%/yr.
- Depression (losses at over-indebted companies/banks): debt service 49%; inflows −34%; rates +11%; real FX −19%; GDP −14%; stocks −87%; inflation peak 8% (low); a quarter of risk factors (current account deficit); reserves −100%; debt/GDP +36% (+18% ann.).
- Reflation: peg abandoned; ugly phase slightly shorter; CA +21%; very aggressive 8/9 (nationalized banks, liquidity, asset purchases); IMF. Debt/GDP −88% (−15% ann.), via real growth; real FX bottom −16%; GDP peak 5 yrs; equities 23 yrs. Political: Thaksin Shinawatra, 2001.

### 15. Indonesia 1994–2012 — transitory inflationary — PDF 419–422 / p. 161–164
- Phases: bubble 1994–1997; depression 1997–1998; reflation 1998–2012. Window 1992-05 to 2007-05.
- Bubble: debt peak 104%; FX 51%; inflows ~5%; CA deficit 3%; growth 7%; gap 13%; equities 12%/yr; real FX +19%.
- Depression (1997 Asian financial crisis): inflows −13%; rates +43%; real FX −110%; GDP −14%; stocks −89%; inflation peak 59% (normal); a quarter of risk factors (high foreign-denominated debts); reserves −23%; debt/GDP +132% (+132% ann.).
- Reflation: peg abandoned; relatively short ugly phase; CA +4%; very aggressive 7/9 (nationalized banks, liquidity, asset purchases); IMF. Debt/GDP −178% (−13% ann.); real FX bottom −90%; GDP peak 5 yrs; equities 13 yrs.

### 16. Korea 1994–2001 — transitory inflationary — PDF 423–426 / p. 165–168
- Phases: bubble 1994–1997; depression 1997–1998; reflation 1998–2001. Window 1992-05 to 2007-05.
- Bubble: debt +23% to 163%; FX 27%; inflows ~8%; CA deficit 3%; growth 8%; gap 5%.
- Depression (1997 Asian crisis): debt service 42%; inflows −9%; rates +14%; real FX fell to −50%; GDP −8%; stocks −75%; home prices −13%; unemployment +6; inflation peak 7% (low); a quarter of risk factors (low central bank reserves); reserves −24%; debt/GDP +19% (+13% ann.).
- Reflation: peg abandoned; ugly phase slightly shorter; CA +7%; very aggressive 7/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −25% (−10% ann.), via real growth; real FX bottom −17%; GDP peak 1.7 yrs; equities 9 yrs.

### 17. Malaysia 1994–2001 — transitory inflationary — PDF 427–430 / p. 169–172
- Phases: bubble 1994–1997; depression 1997–1998; reflation 1998–2001. Window 1992-05 to 2007-05.
- Bubble: debt +53% to 212%; FX 39%; inflows ~6%; CA deficit 8%; growth 10%; gap 9%.
- Depression (1997 Asian crisis): debt service 45%; inflows −5%; rates +4%; real FX −24%; GDP −9%; stocks −83%; inflation peak 5% (low); a quarter of risk factors (current account deficit); reserves −27%; debt/GDP +10% (+7% ann.).
- Reflation: peg abandoned; ugly phase slightly shorter; CA +19%; very aggressive 7/9 (nationalized banks, liquidity, asset purchases); no IMF mentioned. Debt/GDP −41% (−18% ann.), via real growth; real FX bottom −9%; GDP peak 2 yrs; equities 14 yrs.

### 18. Philippines 1994–2008 — transitory inflationary — PDF 431–434 / p. 173–176
- Phases: bubble 1994–1997; depression 1997–1998; reflation 1998–2008. Window 1991-12 to 2006-12.
- Bubble: debt +12% to 95%; FX 51%; inflows ~12%; CA deficit 5%; growth 5%; gap 2%; equities 8%/yr; real FX +23%.
- Depression (1997 Asian crisis): debt service 25%; inflows −19%; rates +9%; real FX −29%; GDP −3%; stocks −79%; inflation peak 10% (low); a quarter of risk factors (low central bank reserves); reserves −60%; debt/GDP +24% (+15% ann.).
- Reflation: peg abandoned; ugly phase slightly shorter; CA +11%; somewhat aggressive 3/9; IMF; labor reforms. Debt/GDP −51% (−5% ann.); real FX bottom −24%; GDP contraction "brief" (no years figure); equities 16 yrs. Political: Joseph Estrada.

### 19. Russia 1996–2006 — transitory inflationary — PDF 435–438 / p. 177–180
- Phases: no bubble dates; depression 1997–1998; reflation 1998–2006. Window 1992-10 to 2007-10.
- Pre-crisis: debt 112% (inflow-driven); FX 38%; inflows ~5%.
- Depression (Asian-crisis ripples + falling oil): debt service 90%; inflows −5%; rates >250%; real FX −72%; GDP −10%; stocks −85%; inflation peak 91% (high); around half of risk factors (long inflation history); reserves −55%; debt/GDP +63% (+58% ann.); fiscal deficit 5%.
- Reflation: peg abandoned; relatively short ugly phase; CA +8%; very aggressive 6/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −119% (−15% ann.); real FX bottom −43%; GDP peak 1.8 yrs; equities 6 yrs.

### 20. Colombia 1995–2008 — transitory inflationary — PDF 439–442 / p. 181–184
- Phases: bubble 1995–1998; depression 1998–2003; reflation 2003–2008. Window 1993-03 to 2008-03.
- Bubble: debt +11% to 58%; FX 30%; inflows ~8%; CA deficit 5%; growth 3%; gap 5%; real FX +16%; strong housing returns.
- Depression (effects of the 1997 Asian crisis): inflows −8%; rates +20%; real FX −45%; GDP −7%; stocks −66%; unemployment +6; inflation peak 20% (low); around half of risk factors (long inflation history); reserves −37%; debt/GDP +12% (+2% ann.); fiscal deficit 5%.
- Reflation: peg abandoned; ugly phase slightly longer; CA +5%; very aggressive 6/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −16% (−3% ann.); real FX bottom −29%; GDP peak 4 yrs; equities 7 yrs.

### 21. Ecuador 1995–2009 — classic inflationary — PDF 443–446 / p. 185–188
- Phases: no bubble dates; depression 1998–2000; reflation 2000–2009. Window 1993-11 to 2008-11.
- Pre-crisis: debt 85%; FX 56%; CA deficit 4%; inflows ~3%.
- Depression (contagion from the 1997 Asian crisis): inflows −11%; real FX −60%; GDP −6%; stocks −62%; unemployment +2; inflation peak 76% (high); most risk factors (low real short rates); reserves −61%; debt/GDP +46% (+42% ann.).
- Reflation: peg abandoned; relatively short ugly phase; CA +11%; very aggressive 9/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −79% (−8% ann.); real FX bottom −55%; GDP peak 1.8 yrs; equities 5 yrs. Political: Lucio Gutierrez, 2003. (The 2000 dollarization is not named in the text; the FX-return chart goes flat from 2000.)

### 22. Turkey 1997–2003 — classic inflationary — PDF 447–450 / p. 189–192
- Phases: bubble 1997–2000; depression 2000–2001; reflation 2001–2003. Window 1995-05 to 2010-05.
- Bubble: debt +17% to 60%; FX 46%; inflows ~3%; growth 2%; gap 9%; equities 22%/yr.
- Depression (political turmoil and violence): debt service 30%; inflows −10%; rates +157%; real FX −12%; GDP −10%; stocks −78%; unemployment +3; inflation peak 62% (high); most risk factors (long inflation history); reserves −100%; debt/GDP +9% (+6% ann.); fiscal deficit 11%.
- Reflation: peg abandoned; ugly phase slightly shorter; CA +5%; very aggressive 7/9 (nationalized banks, liquidity, asset purchases); IMF; labor reforms. Debt/GDP −6% (−3% ann.); real FX bottom −18%; GDP peak 2 yrs; equities 6 yrs.

### 23. Argentina 1998–2012 — transitory inflationary — PDF 451–454 / p. 193–196
- Phases: bubble 1998–2001; depression 2001–2002; reflation 2002–2012. Window 1995-12 to 2010-12.
- Bubble: debt peak 78%; FX 47%; inflows ~11%; CA deficit 5%; growth 0%; gap 9%; real FX +39%.
- Depression (ripples from late-1990s EM crises): inflows −10%; rates +173%; real FX −77%; GDP −15%; stocks −82%; unemployment +3; inflation peak 32% (normal); around half of risk factors (long inflation history); reserves −66%; debt/GDP +118% (+62% ann.); fiscal deficit 4%.
- Reflation: peg abandoned; ugly phase slightly shorter; CA +7%; very aggressive 6/9 (nationalized banks, liquidity); IMF; labor reforms. Debt/GDP −140% (−15% ann.); real FX bottom −42%; GDP peak 5 yrs; equities 7 yrs. Political: Eduardo Duhalde.

### 24. Iceland 2005–2016 — transitory inflationary — PDF 455–458 / p. 197–200
- Phases: bubble 2005–2008; depression 2008–2010; reflation 2010–2016. Window 2002-12 to 2017-12.
- Bubble: debt +565% to 1,173%; FX 691%; inflows ~37%; CA deficit 18%; growth 7%; equities 12%/yr; strong housing returns. GDP gap: No Data Available.
- Depression (2008 global financial crisis): inflows −49%; rates +4%; real FX −29%; GDP −11%; stocks −96%; home prices −15%; unemployment +5; inflation peak 18% (low); a quarter of risk factors (high foreign-denominated debts); reserves −18%; debt/GDP +122% (+46% ann.); fiscal deficit 5%.
- Reflation: ugly phase slightly longer; CA +13%; very aggressive 6/9 (nationalized banks, liquidity); IMF. Debt/GDP −1,037% (−170% ann.), a balanced mix of outright debt reduction and rising income driven by real growth; real FX bottom −22%; GDP peak 8 yrs; USD equities not yet recovered.

### 25. Russia 2005–2011 — transitory inflationary — PDF 459–462 / p. 201–204
- Phases: bubble 2005–2008; depression 2008–2009; reflation 2009–2011. Window 2002-12 to 2017-12.
- Bubble: debt peak 66%; FX 21%; inflows ~10%; growth 8%; gap 8%; equities 46%/yr.
- Depression (2008 GFC + oil collapse): inflows −21%; rates +19%; real FX −21%; GDP −8%; stocks −71%; unemployment +3; inflation peak 15% (low); a quarter of risk factors (long inflation history); reserves −44%; debt/GDP +17% (+12% ann.).
- Reflation: ugly phase slightly shorter; aggressive 4/9; no IMF or CA figure. Debt/GDP −14% (−8% ann.); real FX bottom +11% (positive); GDP peak 3 yrs; USD equities not yet recovered.

### 26. Russia 2012–2016 — transitory inflationary — PDF 463–466 / p. 205–208
- Phases: no bubble dates; depression 2014–2016; reflation 2016–2016. Window 2009-05 to 2024-05 (data to ~2018).
- Pre-crisis: debt +19% to 89% (inflow-driven); FX 15%; inflows ~6%.
- Depression (oil price declines): debt service 32%; inflows −8%; rates +7%; real FX −30%; GDP −4%; stocks −46%; inflation peak 18% (low); a quarter of risk factors (long inflation history); reserves −26%; debt/GDP +19% (+9% ann.); fiscal deficit 4%.
- Reflation: ugly phase slightly shorter; aggressive 4/9. Debt/GDP −7% (−14% ann.), balanced mix of debt reduction and rising income; real FX bottom −17%; real GDP and USD equities not yet back to prior peaks.

### Quick cross-case table (depression-phase core numbers)

| Case | GDP decline | Equity decline (USD) | Real FX decline | Inflation peak | Debt/GDP chg (ann.) | Levers /9 | GDP peak regained (yrs) | Equities regained (yrs) |
|---|---|---|---|---|---|---|---|---|
| Argentina 1977 | 14 | 91 | 93 | >1000 (refl.) | +7 | 3 | 7 | — |
| Brazil 1977 | 6 | 51 | 20 | 124 | +18 | 4 | 4 | 1.9 |
| Chile 1978 | 14 | 74 | 50 | 33 | +19 | 5 | 5 | 9 |
| Mexico 1979 | 7 | 86 | 74 | 151 | +7 | 2 | 7 | 6 |
| Peru 1980 | 13 | 56 | (53 ccy) | 190 | +42 | 3 | 4 | 6 |
| Philippines 1979 | 11 | 71 | 16 | 58 | 0 | 7 | 6 | 5 |
| Malaysia 1981 | — | 56 | 19 | — | +17 | 5 | 1.8 | 6 |
| Peru 1986 | 30 | 91 | — | >10000 (refl.) | −30 | 3 | 9 | — |
| Argentina 1987 | 16 | 33 | 60 | >10000 (refl.) | −11 | 3 | 4 | 2 |
| Brazil 1987 | 7 | 70 | (19 ccy) | >5000 (refl.) | +37 | 2 | 1.4 | 3 |
| Turkey 1990 | 12 | 70 | 26 | 117 | +17 | 3 | 1.6 | 4 |
| Mexico 1991 | 10 | 66 | (37 ccy) | 43 | +1 | 6 | 2 | 10 |
| Bulgaria 1995 | 13 | — | 96 | >500 (refl.) | +13 | 5 | 8 | — |
| Thailand 1993 | 14 | 87 | 19 | 8 | +18 | 8 | 5 | 23 |
| Indonesia 1994 | 14 | 89 | 110 | 59 | +132 | 7 | 5 | 13 |
| Korea 1994 | 8 | 75 | to −50 | 7 | +13 | 7 | 1.7 | 9 |
| Malaysia 1994 | 9 | 83 | 24 | 5 | +7 | 7 | 2 | 14 |
| Philippines 1994 | 3 | 79 | 29 | 10 | +15 | 3 | brief | 16 |
| Russia 1996 | 10 | 85 | 72 | 91 | +58 | 6 | 1.8 | 6 |
| Colombia 1995 | 7 | 66 | 45 | 20 | +2 | 6 | 4 | 7 |
| Ecuador 1995 | 6 | 62 | 60 | 76 | +42 | 9 | 1.8 | 5 |
| Turkey 1997 | 10 | 78 | 12 | 62 | +6 | 7 | 2 | 6 |
| Argentina 1998 | 15 | 82 | 77 | 32 | +62 | 6 | 5 | 7 |
| Iceland 2005 | 11 | 96 | 29 | 18 | +46 | 6 | 8 | not yet |
| Russia 2005 | 8 | 71 | 21 | 15 | +12 | 4 | 3 | not yet |
| Russia 2012 | 4 | 46 | 30 | 18 | +9 | 4 | not yet | not yet |

---

## 2. Appendix: Macroprudential Policies — PDF 467–477 / printed 209–219

**What it is and is not.** The Part 3 appendix is a qualitative essay on macroprudential policy, built on Elliott, Feldberg and Lehnert's Fed paper. It does **not** contain archetype statistics, the method behind the compendium charts/gauges, or averages across the 48 cases. Every number it contains is transcribed below.

### 2a. Framing (p. 209, PDF 467)
- Definition (paraphrased): macroprudential policies are tools for steering credit one way or another through the central bank's regulatory authorities, as opposed to one-size-fits-all monetary policy or fiscal apportionment. Need arises because credit growth differentiates: a bubble in one area, starvation in another. Classic countercyclical example: making it easier to buy a house in a housing bust (lower credit standards / lower down payments) or harder in a housing bubble.
- They resemble fiscal policy in benefiting some at others' expense; useful complement to monetary policy during a deleveraging because QE often fuels pockets of froth (asset markets) while the broad economy is still recovering. In the Great Depression and WWII, central bankers used macroprudential measures to curb froth while keeping overall money easy.
- Not new: bread-and-butter tool for almost all of modern monetary-policy history. **The Federal Reserve has changed margin requirements for equity holdings 23 times since it was formed**, tightening in big rallies / periods of excess stock-market credit and easing in bear markets. Rarer from the early 1990s to mid-2000s (the historical exception); global central banks have since returned to macroprudential tools.
- The typical case (US history):
  - Occurred when shifting interest rates was losing effectiveness: economy needs stimulation but rates are at zero; or tightening is needed in one area but not for the whole economy.
  - Occurred when it was desirable to direct credit toward credit-starved sectors and away from frothy assets/lending.
  - Involved a combination of policies at once. **Demand-for-credit measures**: changing required loan-to-value ratios; required debt-service-to-income ratios; loan-maturity requirements; margin requirements for buying financial assets; cost of loans via interest-rate subsidies / tax policy / other regulation. **Supply-of-credit measures**: capital/reserve requirements for certain lending types; the portfolio of assets institutions may hold; accounting rules on different assets; supervisors pressuring for certain lending behaviors; interest/lending-rate ceilings and other limits (p. 210).
  - Saw coordination between the Fed, Congress, the executive branch and regulators; new institutions were set up to implement and monitor.
  - Saw mixed success: effective policies kept for long periods or expanded, unsuccessful ones ended within months, but some distortionary ones lingered for years (Regulation Q); tools changed as the financial system evolved; policies were adapted or abandoned when innovations circumvented them.

### 2b. Questions to consider (p. 210–211, PDF 468–469)
1. Where are bubbles emerging, and how confident are you they are bubbles? Examples: US policy tightened in 1935–36 partly in response to rapid stock-price gains; that proved too much for the deleveraging economy, which fell back into severe recession, and **stocks fell 60% between 1937 and 1938**. Over recent decades US policy makers took a "mopping up" approach (deal with the aftermath rather than prick bubbles), reasoning that mispricing is hard to know; hence regulators did not aggressively slow frothy mortgage lending in 2006 and earlier.
2. Which sectors are starved for credit; is differentiated credit policy needed? 1950s policy makers developed **four basic tests**: how effective general monetary policy is in balancing credit provision; how destabilizing the sector's credit growth is; how important credit is to the sector's growth; how effective selective credit controls would be to administer.
3. How comfortable are you picking winners and losers; what are the political costs?
4. Which tools: target demand for credit, supply, or both?
5. How will you measure effectiveness?
6. Second- and third-order consequences, often years later: Regulation Q (deposit-rate caps, implemented in the Depression to help smaller banks) was creating substantial distortions by the 1950s, pushing deposits into shadow banking; S&L deregulation in the early 1980s (partly to help S&Ls cope with tight money) contributed to the S&L crisis that began in the mid-1980s.
7. Coordination between legislators, executive and central bank; empowering regulators: WWII effort as the model (Congress revised laws to give the Fed authority, Roosevelt used executive orders); Volcker's Fed given room to shift policy nimbly; biggest problems came from inflexibility (rate caps not adapted). Today: UK vests much power in the BoE and its Financial Policy Committee (FPC); US spreads it across agencies plus the post-crisis Financial Stability Oversight Council (FSOC).

### 2c. Historical cases of US macroprudential policy (p. 211–218, PDF 469–476), seven categories

Source paper named: Elliott, Feldberg and Lehnert, "The History of Cyclical Macroprudential Policy in the United States."

**(i) Demand side: margin requirements** (p. 211–212)
- Fed gained the power under the Securities Exchange Act of 1934; used counter-cyclically (raise when asset prices boom and credit purchases rise; lower otherwise). Regulation T set margins for brokers, Regulation U for banks.
- Chart "USA Initial Margin Requirement US Stocks", 1930-01 to 1975-01: starts around 25–30% (mid-1930s), steps to ~55% (c. 1936), ~50% late 1930s/early 1940s, rises to 75% then **100% around 1946**, falls to ~50% (1949), 75% (1951), 50% (1953), 60–70% (mid/late 1950s), 90% (1958–59), 70% (1960), 50% (1962), 70% (1963–67), 80% (1968–69), 65% (1970), 55% (1971), 65% (1972), 50% (1974 onward).
- Since 1974 the Fed has mostly stopped using this lever because derivatives and other credit routes let investors sidestep it.

**(ii) Demand side: underwriting standards** (p. 212–213)
- Great Depression: Congress created the **Federal Home Loan Bank System in 1932** (quasi-central bank for S&Ls, also set underwriting standards and collateral restrictions). **1934: Federal Housing Administration (FHA)** created to insure home loans; eligible loans at **80% LTV and 20-year maturity** (easier terms). **Electric Home and Farm Authority (1934)**: cheap appliance loans at **<10% interest, 5% down, up to 36 months**; ended 1942. **1935**: Congress lowered LTV regulation for national banks **from 50% to 60%** and extended maximum maturity **from 5 to 10 years**. FHA insured **up to 20% of loans (up to 5-year maturity)** for residential improvements, **1934–1937**. **1938**: FHA lowered insurance standards to **90% LTV and 25-year maturity**.
- WWII: **1941** Roosevelt ordered the Fed to limit installment credit for consumer durables to steer production to defense (short quote from the executive order about liberal credit terms stimulating durable-goods demand); the Fed enforced tighter underwriting on consumer installment loans (**Regulation W**).
- Post-war: **October 1950** the Fed, worried about mortgage debt, tightened housing credit with **Regulation X** (LTV and maturity caps on residential loans, more restrictive as loan size grew); target of **reducing 1951 housing production by one-third of 1950 levels**. **1950**: at Truman's request the FHA and VA raised down-payment requirements **by 5 percent**, cut the maximum single-family FHA loan **from $16,000 to $14,000**, and set a **25-year** maximum maturity, their first restrictive actions in nearly 20 years; removed in the mid-1953 recession; **August 1954** Congress reversed them (lower down payments, higher max FHA loan).
- Late 1954 (frothy housing, Fed unwilling to tighten after recession): FHA/VA raised down payments and cut maximum maturities **from 30 to 25 years** (later tweaked/reversed); field offices told to survey local markets and restrain federal underwriting where surpluses existed; the FHLBB asked Federal Home Loan banks to curb loan commitments to thrifts and in **September 1954** imposed official lending restraints on S&Ls; the New York Fed moved to restrain mortgage warehouse lending (which had more than doubled between August 1954 and August 1955).
- **Credit Control Act of 1969**: gave the Fed power to use credit controls on specific sectors (maximum rate, maturity, minimum periodic payment, etc.); not used until the Volcker era. **1982**: Congress abolished LTV and maturity restrictions for national banks.

**(iii) Supply side: voluntary guidelines against speculative/non-productive lending** (p. 213–214)
- **1947**: Congress encouraged banks to voluntarily restrict lending and investing after the Fed's consumer-installment limits expired.
- Korean War: **Defense Production Act of 1950** gave the Fed authority for "voluntary" credit restraints (lenders to screen loans by purpose as well as creditworthiness); in place about a year.
- **1965**: cabinet-level Committee on the Balance of Payments recommended voluntary lending restraints monitored by the Fed; goal to cut net capital outflows by **over 15%** from the prior year; an initial **5% ceiling on foreign loan growth**, the first quantitative credit target; **1968** Johnson executive order allowed the Fed to make it mandatory (Fed declined, citing high voluntary participation); programs continued until **1974**.
- **1966**: Fed prompted banks to slow business loans (high business credit creation, rising inflation); non-cooperating banks had discount-window access limited; ended once the economy slowed.
- **March–July 1980**: Carter's "voluntary" Special Credit Restraint Program: banks, holding companies, finance companies and foreign branches asked to limit loan growth to **6–9%**; restrain speculative/inflationary lending (credit cards, unsecured consumer loans, speculative inventories, takeovers/mergers, commodity/precious-metal speculation) while maintaining funds for small business, farmers and home buyers; periodic lending reports required.
- Europe: national credit councils in France and Italy announced which sectors needed more credit or were over-burdened, especially post-war.

**(iv) Supply side: reserve requirements** (p. 214–215)
- States set the first reserve requirements in the 1800s; **National Bank Act of 1863** introduced the first nationwide ones; **Federal Reserve Act of 1913** eased them (Fed as lender of last resort).
- **1935**: Congress gave the Fed the power to set reserve requirements; **spring 1938** the Fed lowered them alongside Roosevelt's recovery program. **1942**: eased three times; held steady during the war; **1948**: tightened three times back to statutory caps; **1949–1951**: adjusted nine times (eased 1949, tightened 1951). Also raised during tightening periods in **1966–69, 1973 and 1979–80**.
- New instruments bypassed reserves (commercial paper, eurodollars, repos, large CDs). **1969**: new bank borrowing from overseas branches capped at **10%**, plus a **10%** limit on asset sales to overseas branches; **1970** both limits raised to **20%**; **1973** both lowered to **8%** (same as for large CDs).
- Late 1960s: FHLBB used reserve requirements to steer mortgage lending (lower when savings declined, higher when lending was high); eased in **1968–69 and 1973–74**, with "at most a limited, positive impact".
- **October 1979** (Volcker): reserve requirements on wholesale liabilities (large time deposits, eurodollar borrowings, repos with government/agency collateral, fed funds borrowings) rose to **8%**; **March 1980** increased to **10%**; a month later lowered to **5%**; eliminated in **July**.
- **1980**: unprecedented asset-based reserve requirements under the 1969 Credit Control Act: a **15% special deposit** on specific consumer credit, money-market funds subject to the same; both later lowered to **7.5%**; MMFs required to file monthly reports; by **August** all removed; by **end-1980** Congress terminated the Credit Control Act.
- Fed lowered reserve requirements in **1990 and 1992** to promote credit availability.
- Europe: France and Italy used differential reserve requirements (lenient for public banks, excluding long-term or export loans); regulators more often used caps on loans or on access to central-bank financing; France had a "rediscount ceiling" until **1972**, sometimes sector-specific (Banque de France quotas on over-producing agricultural sectors) or broad (p. 216).

**(v) Supply side: interest rate ceilings** (p. 216–217)
- Early 1900s: states limited deposit rates as part of state deposit insurance; amended **Federal Reserve Act of 1927** capped interest paid by national banks to state banks; **Banking Act of 1933** let the Fed cap time/savings deposit rates: **November 1933 Regulation Q, 3% ceiling**, lowered to **2.5%** after market rates fell, later raised back to **3%** (savings/time deposits of six months or more); Regulation Q also let the Fed set maximum rates the FDIC paid to non-member insured banks; ceilings raised in **1960 and 1961**.
- **1934–1989**: FHLBB supervised S&Ls, with informal dividend ceilings generally **25–50 bp above the Fed funds rate**.
- **Interest Rate Regulation Act of 1966**: FDIC and FHLBB could set ceilings at mutual savings banks and S&Ls; Fed could set rates for specific deposit classes, used a **5.5% limit on single-maturity CDs** and lowered time-deposit maxima; **1973** CD ceiling removed.
- **1978**: banks allowed money-market certificates with floating ceilings pegged to the six-month T-bill (relaxation of Regulation Q).
- **Depository Institutions Deregulation and Monetary Control Act, March 1980**: eliminated Regulation Q (judged unsuccessful because easily circumvented); ceilings phased out by **1986**.
- Chart "Interest Rate Ceilings on Deposits at Commercial Banks", 1926–1986: ceiling on savings deposit rate, ceiling on time deposit rate (same before 1966), average interest paid on deposits, 3-month T-bill; ceilings ~2.5–3% through the 1950s, time-deposit ceiling rising stepwise to ~5–8% by the late 1970s, T-bill peaking near 16–18% around 1980–81, savings ceiling ~5.5%.

**(vi) Supply side: supervisory guidance and "direct pressure"** (p. 217–218)
- Curtailing lending in booms: after WWI the Fed used supervisors to pressure banks toward productive uses; by mid-1927 policy makers were nervous about stock speculation (stocks up almost **100%** the prior year); **February 1929** statement that the Fed would not lend to banks extending speculative credit, largely ineffective. **November 24, 1947** supervisors urged caution on speculative real-estate, commodity and securities loans. 1990s–2000s: **1995** examiner warning on easing underwriting standards (regional real-estate risk after the S&L crisis); **1999** statement on subprime risks and higher capital; two years later agencies quantified **1.5x–3x** more capital against subprime loans; early/mid-2000s statements on frothy credit; **2005** guidance on home-equity, commercial real estate and nontraditional mortgages; **2013** Fed and OCC leveraged-loan regulation with a **6x leverage limit**.
- Credit availability in busts: **April 1938** Roosevelt asked regulators for a more liberal bank-examination policy; Treasury plus three supervisors issued a joint statement moving away from mark-to-market and distinguishing "investment" (top four rating grades) from "speculative" securities. End of the S&L crisis: **May 1990** OCC, Fed and FDIC urged banks to lend; **March 1991** report to "clarify regulatory policies" without easing standards. Clinton's post-election credit-availability initiative (joint statement, reduced "appraisal burden", better appeals for small-business lending). **2007–2009**: supervisors encouraged lending and working with distressed borrowers without weakening examination standards.

Note on the count: the text says the cases are organized into "seven categories", but only six section headings are printed (Margin Requirements; Underwriting Standards; Voluntary Guidelines; Reserve Requirements; Interest Rate Ceilings; Supervisory Guidance and "Direct Pressure"); the last is split into two bold sub-headings, "Guidance to curtail lending in booms" and "Credit availability during busts", which would make seven if counted separately.

Chart readings in this section (margin-requirement steps, deposit-ceiling levels) are approximate values read off the printed charts, not numbers stated in the text.

### 2d. Endnotes (p. 219, PDF 477)
Sixty endnotes. Sources cited: Douglas J. Elliott, Greg Feldberg and Andreas Lehnert, "The History of Cyclical Macroprudential Policy in the United States," Finance and Economics Discussion Series 2013-29, Board of Governors (May 2013) — the bulk of notes; Stanley Fischer, "Financial Sector Reform: How Far Are We?", Martin Feldstein Lecture, NBER, Speech 813 (July 2014); Dominic Wilson et al., "Beyond interest rates: Macro-prudential policies in housing markets," Goldman Sachs Global Economics Weekly no. 14/16 (April 2014); Anna Kelber and Éric Monnet, "Macroprudential policy and quantitative instruments: a European historical perspective," Financial Stability Review, Banque de France, no. 18 (April 2014): 157 (notes 28, 41–44).

### 2e. End matter
- PDF 478: blank.
- PDF 479 (printed 221): **Disclosures** — list of Bridgewater data sources (Australian Bureau of Statistics through World Economic Forum), standard disclaimers, no-copying notice, "©2018 Ray Dalio. All rights reserved."
- PDF 480: blank.

---

## 3. Exact field list of the statistics "table" (narrative slots, in template order)

Because this edition has no tabular statistics block, the "row labels" are the template's statistic slots. In order of appearance (CSV column name in parentheses):

1. Cycle type: classic inflationary / classic hyperinflationary / transitory inflationary (`deleveraging_subtype`); "letting its currency go" flag (`letting_currency_go`)
2. Bubble dates (`bubble_dates`); whether a broad-based bubble occurred (`broad_based_bubble`); drivers (`bubble_drivers`)
3. Debts rose by X% of GDP during the bubble (`debt_gdp_change_bubble_pct`)
4. Pre-crisis peak debt, % of GDP (`debt_gdp_precrisis_peak_pct`)
5. Share of debt in foreign currencies, % of GDP (`fx_debt_gdp_pct`)
6. Investment inflows, average % of GDP (`investment_inflows_avg_gdp_pct`)
7. Current account deficit, % of GDP (`current_account_deficit_gdp_pct`)
8. Growth during the bubble, % (`bubble_real_growth_pct`)
9. GDP gap peak, % (`gdp_gap_peak_pct`)
10. Equities, annualized return over the bubble, % (`bubble_equity_return_ann_pct`)
11. Real FX peak, % (`real_fx_peak_pct`)
12. Depression dates (`depression_dates`)
13. Debt service at pre-crisis peak, % of GDP (`debt_service_precrisis_peak_gdp_pct`)
14. Shock (`shock_trigger`)
15. Capital inflows fell by X% of GDP (`capital_inflows_fall_gdp_pct`)
16. Short rates hiked by X% (`short_rate_hike_pct`)
17. Real FX fell by X% (`real_fx_decline_pct`)
18. GDP fell by X% (`gdp_decline_pct`)
19. Stock prices fell by X% (`equity_decline_pct`)
20. Home prices fell by X% (`home_price_decline_pct`)
21. Unemployment increased by X% (`unemployment_change_pp`)
22. Inflation peak during the depression, % (`inflation_peak_depression_pct`) and its high/normal/low label (`inflation_peak_vs_similar_cases`)
23. Share of classic risk factors for inflation spirals (`risk_factor_share`) and the biggest one (`biggest_risk_factor`)
24. Reserves drawn down by X% (`reserves_drawdown_pct`); currency fallen by X% when defense abandoned (`currency_fall_by_end_depression_pct`)
25. Debt as % GDP change in the depression and annualized (`debt_gdp_change_depression_pct`, `debt_gdp_change_depression_ann_pct`)
26. Peak fiscal deficit, % of GDP (`peak_fiscal_deficit_gdp_pct`)
27. Reflation dates (`reflation_dates`)
28. Abandoned the currency peg (`abandoned_currency_peg`); ugly-phase length vs average (`ugly_phase_vs_average`); hyperinflation branch (`hyperinflation_spiral`, `reflation_inflation_peak_pct`)
29. Current account improved by X% of GDP (`current_account_improvement_gdp_pct`)
30. Real FX bottom, % (`real_fx_bottom_pct`)
31. Aggressiveness in managing financial institutions/bad debts (`policy_aggressiveness`); N of 9 classic policy levers (`policy_levers_pulled_of_9`); named levers (`nationalized_banks`, `provided_liquidity`, `purchased_troubled_assets`)
32. IMF assistance program (`imf_program`); structural reforms for labor-market flexibility (`structural_reforms_labor_market`); new currency (`currency_redenomination`)
33. Debt as % GDP change in the reflation and annualized (`debt_gdp_change_reflation_pct`, `debt_gdp_change_reflation_ann_pct`); driver of the reduction (`deleveraging_driver`)
34. Years before real GDP reached its prior peak (`years_to_regain_gdp_peak`)
35. Years for USD equity prices to recover (`years_to_recover_equities_usd`)
36. Political note (`populist_leader`)

Sign convention in the CSV: decline/drawdown/fall columns hold the magnitude as printed (positive number = decline of that size); debt-change columns carry an explicit sign (+ rose, − fell); real FX peak/bottom carry their printed sign. ">250" means "more than 250%" as printed.

---

## 4. Page coverage

- Read in full: PDF 261–262 (Part 3 table of contents; 262 is blank) and PDF 363–480, every page, in 20-page calls (363–382, 383–402, 403–422, 423–442, 443–462, 463–480).
- Pages I could not read: none.
- Blank pages in range: 478 and 480.
- Not in my range (for the other half's encoder): Germany 1918 (printed 99–104, PDF 357–362) is the first case of the non-domestic-currency group.

## 5. Things worth flagging

- Debt/GDP *fell* during the depression in two hyperinflation cases (Peru 1986–95: −106%, −30% ann.; Argentina 1987–93: −30%, −11% ann.) because inflation inflated away nominal income; and Argentina 1987's reflation attribution chart shows debt/GDP *rising* (+7% ann.).
- Iceland's numbers dwarf the rest: debt +565% of GDP in the bubble to 1,173% (691% FX), inflows 37% of GDP, and a −1,037% (−170% ann.) reflation deleveraging.
- Ecuador 1995–2009 is the only case pulling 9 of 9 policy levers; Mexico 1979–91 and Brazil 1987–95 the weakest at 2 of 9.
- Longest USD-equity recoveries: Thailand 23 years, Philippines 1994 16 years, Malaysia 1994 14 years, Indonesia 13 years; Iceland, Russia 2005 and Russia 2012 not recovered at the time of writing.
- Russia 2005–2011 is the only case whose "beautiful period" real FX bottom is positive (+11%).
- Indonesia 1997–98: debt/GDP +132% in one year, the largest annualized depression-phase increase in the group; Argentina 2001–02 +62% ann.; Russia 1997–98 +58% ann.
- Reserve exhaustion (−100%) in Philippines 1982–84, Mexico 1994–95, Thailand 1996–98 and Turkey 2000–01.
- The Argentina 1977–88 text places the peso argentino adoption in 1983, i.e. inside the 1980–85 depression window, though it is discussed under reflation.
- Russia 2012–2016 has a reflation phase labelled "2016–2016" and its chart window runs to 2024-05 with data stopping around 2018.
- Several template slots are structurally missing in "no broad-based bubble" cases (Brazil 1977, Peru 1980, Argentina 1987, Turkey 1990, Bulgaria, Russia 1996, Ecuador, Russia 2012): no bubble dates, growth, GDP gap, equity return or real FX peak.
- The Appendix is about macroprudential policy history, not case statistics; if the parent expected archetype averages here, they are not in this edition.
