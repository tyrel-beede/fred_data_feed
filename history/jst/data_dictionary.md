# JST Macrohistory Database R6 — documentation, as encoded for this repository

<!-- Written from the R6 documentation PDF in our own words; source citations and the terms of use are transcribed verbatim because they are references. -->

# Jordà–Schularick–Taylor Macrohistory Database — Release 6 documentation: extraction of PDF pages 1–100

Source file: `JST_documentationR6.pdf` (201 pages). This part covers PDF pages 1–100: front matter (title, terms of use, acknowledgements, Stata label table, table of contents) and the country chapters for Australia, Belgium, Canada, Denmark, Finland, France, Germany, and the first four pages of Ireland (the Ireland chapter continues on pp. 101–105, outside this range). PDF page numbers equal the printed page numbers (the title page is p. 1).

Conventions in this document: text in quotation marks is transcribed from the PDF; "Note:" lines inside source lists are my observations (gaps, overlaps, apparent typos) unless they say "the document notes". Year ranges use the document's own ranges even where they overlap or leave gaps; I flag those rather than silently repairing them.

---

## (a) Front matter

**Title (p. 1):** "JORDÀ-SCHULARICK-TAYLOR MACROHISTORY DATABASE" — URL `http://www.macrohistory.net/data` — dataset name "JSTDatasetR6" — "Release 6" — "July 2022".

**Authors:** Òscar Jordà, Moritz Schularick, and Alan M. Taylor (named in the required citation; the asset-return data additionally credit Katharina Knoll and Dmitry Kuvshinov). No author list or affiliation block appears on the title page.

**DOI:** none is printed anywhere in pp. 1–100; the only locator is the URL above. The page-2 text has hyperlinks ("here", "Detailed terms of licence.") whose targets are not printed.

**Funders (p. 2):** Institute for New Economic Thinking; Volkswagen Foundation; German Federal Ministry of Education Research (sic); European Research Council.

### Terms of use (p. 2) — verbatim

> **TERMS OF USE FOR THIS DATASET**
>
> This dataset was developed over many years with the generous financial support of the Institute for New Economic Thinking, the Volkswagen Foundation, and the German Federal Ministry of Education Research, and the European Research Council. We also thank our home institutions where we have conducted our research. Consistent with the terms of the support we have received from all of these organizations, our dataset is being made freely available in this noncommercial form.
>
> We grant every user at no cost a license (see below) to use and/or share the licensed material, in whole or in part, provided that it is for non-commercial (e.g., academic) purposes, provided that our dataset is properly attributed and cited to credit the authors, and provided that it may only be shared under identical license terms. Commercial data providers are thus strictly forbidden to integrate all or parts of the dataset into their services and/or resell the data.
>
> **LICENCE TERMS**
>
> [CC BY-NC-SA icons]
>
> All users of this work agree to the terms of a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. The detailed terms of this license can be found here.
>
> To comply with the attribution requirement in the license, whenever it is used the dataset must be cited as follows:
>
> "Òscar Jordà, Moritz Schularick, and Alan M. Taylor. 2017. Macrofinancial History and the New Business Cycle Facts. in *NBER Macroeconomics Annual 2016*, volume 31, edited by Martin Eichenbaum and Jonathan A. Parker. Chicago: University of Chicago Press."
>
> However, those using any data pertaining to asset prices or rates of return should cite Òscar Jordà, Katharina Knoll, Dmitry Kuvshinov, Moritz Schularick, and Alan M. Taylor. 2019. "The Rate of Return on Everything, 1870–2015." *Quarterly Journal of Economics.* Forthcoming.
>
> We advise making explicit reference to the date when the database was consulted, as statistics are subject to revisions.
>
> Detailed terms of licence.

Required citation, in one line: **Jordà, Schularick & Taylor (2017), "Macrofinancial History and the New Business Cycle Facts", NBER Macroeconomics Annual 2016, vol. 31** — plus **Jordà, Knoll, Kuvshinov, Schularick & Taylor (2019), "The Rate of Return on Everything, 1870–2015", QJE** for any asset-price or rate-of-return data. License: CC BY-NC-SA 4.0; non-commercial use only; share-alike; commercial data providers explicitly forbidden to integrate or resell.

### Acknowledgements (pp. 3–5)

The database "would not have come into being without the dedication of doctoral students, research assistants, the generosity of many colleagues at universities, central banks, and historical archives"; Felix Ward (Bonn Graduate School of Economics) and Niklas Flamang (Berkeley) are thanked for coordinating work at various stages. Acknowledged by country:

- **Australia:** Tim Hatton (ANU), Peter Tulip (Reserve Bank of Australia), Philipp Hofflin (Lazard Asset Management), Christoph Trebesch (Kiel Institute for the World Economy).
- **Belgium:** Willy Bieseman (NBB), René Brion (BNP Paribas), Frans Buelens (Univ. of Antwerp), Erik Buyst (Univ. of Leuven), Els Demuynck (Vlaamse Overheid), Daisy Dillens (NBB), Guy Lambrechts (Vlaamse Overheid), Ivo Maes (NBB), Jean-Louis Moreau (BNP Paribas), Viviane De Pré (NBB), Erik Vloeberghs (Statistics Belgium), Paul de Wael (STADIM), Christopher Warisse (NBB), Stijn Van Nieuwerburgh (NYU Stern).
- **Canada:** Debra Conner (Canadian Housing Information Centre), Gregory Klump (CREA), Marvin McInnis (Queens University).
- **Denmark:** Kim P. Abildgren, Rune Egstrup, ina Saaby Hvolbøl (all Danmarks Nationalbank), Finn Østrup (Copenhagen Business School), Kevin O'Rourke (Univ. of Oxford).
- **Finland:** Soile Hakonen (Library of the Bank of Finland), Risto Herrala (Bank of Finland), Riita Hjerppe (Univ. of Helsinki), Vappu Ikonen (Bank of Finland), Petri Kettunen (Statistics Finland), Antti Kuusterä (Bank of Finland), Kari Leväinen (Helsinki Univ. of Technology), Susanna Lindström (Bank of Finland), Marketta Lukkari (Statistics Finland), Tiina Skogberg (Library of the Bank of Finland), Essi Tamminen (Bank of Finland), Anja Törmä (Statistics Finland, Information Service of the Library of Statistics), Hannele Turunen (Bank of Finland), Juhani Väänänen (National Land Survey of Finland), Mika Vaihekoski (Univ. of Turku).
- **France:** Patrice Baubeau (Université Paris Ouest Nanterre), Sabine Effosse (Université François Rabelais Tours), Jacques Friggit (CGEDD), Frederik Grélard (Banque de France), Pierre-Cyrille Hautcoeur (EHESS), David Le Bris (Toulouse Business School), Eric Monnet (Banque de France).
- **Germany:** Carsten Burhop (Univ. of Bonn), Jens Conrad (Bundesbank), Karin Fitzner (Bundesbank), Peter Gleber (Bundesverband der Deutschen Volksbanken und Raiffeisenbanken), Petra Hauck (Statistisches Bundesamt), Carl-Ludwig Holtfrerich (FU Berlin), Alexander Nützenadel (HU Berlin), Andrea Papadia (LSE), Albrecht Ritschl (LSE), Ulrich Ronge (Knoesel & Ronge), Thorsten Weber (Sparkassenhistorisches Dokumentationszentrum), Ulrich Weber (Hochschule Anhalt), Nikolaus Wolf (HU Berlin).
- **Italy:** Riccardo De Bonis, Sergio Cardarelli, Massimo Caruso, Giuseppe Conte, Silvia Giacinti, Alfredo Gigliobianco, Andrea Mercatanti, Roberto Violi (all Banca d'Italia), Stefano Battilossi (Universidad Carlos III de Madrid), Giovanni Pellegrino (Univ. of Verona).
- **Ireland:** Ronan Lyons (Trinity College Dublin), Tom Gillespie (NUI Galway).
- **Japan:** John James (Univ. of Virginia), Makoto Kasuya (Univ. of Tokyo), Ryoji Koike (Bank of Japan), Magdalena Korb (KfW), Yuzuru Kumon (UC Davis), Masato Shizume (Bank of Japan).
- **Netherlands:** Piet Eichholtz (Maastricht Univ.), Ferry Lapré (Statistics Netherlands), Wouter Leenders (Oxford Univ.), Alfred Moest (Library Statistics Netherlands), Marjan Peppelmann (BDB), Tijmen Swank (Dutch National Bank), Joost Jonker (Universiteit van Amsterdam), Roger Otten (Maastricht Univ.).
- **Norway:** Roger Bjornstad (Samfunnsøkonomisk Analyse), Ola Gruyyen and Jan Tore Klovland (Norwegian School of Economics), Anders Kvernberg and Lars Tingelstad (Oslo Nasjonalbiblioteket), Einar Thorsrud Lømo, Kari Pedersen and Trond Amund Steinset (Statistics Norway).
- **Portugal:** Rui Alpalhão (ISCTE Business School), Jaime Reis (Univ. of Lisbon), Nuno Valério (Technical Univ. of Lisbon), Jose Rodrigues da Costa (Lisbon Stock Exchange and New Univ. of Lisbon), Maria Eugénia Mata (Nova School of Business).
- **Spain:** Pablo Martin Acena (Univ. of Alcana), Stefano Battilossi (Universidad Carlos III de Madrid), Clara Martinez Toledano-Toledano (Paris School of Economics), Leandro Prados de la Escosura.
- **Sweden:** Johannes Andersson, Birgitta Magnusson Wärmark and Jonas Zeed (Statistics Sweden), Daniel Waldenström (Uppsala Univ.), Olle Krantz (Umeå Universitet).
- **Switzerland:** Christoph Enzler (Bundesamt für Wohnungswesen), Joel Floris (Univ. of Zurich), Franz Murbach (Bundesamt für Statistik), Rebekka Schefer (UBS AG), Iso Schmid (Agristat), Annika Steiner and Robert Weinert (Wüest und Partner), Peter Steiner (Eidgenössische Finanzverwaltung), Martin Zehnder (Swiss National Bank).
- **United Kingdom:** Amanda Bell (ONS), Colin Beattie, Defra Krieghoff and Niels Krieghoff (LSE), Richard Grossman (Wesleyan Univ.), Peter Mayer (Land Registry), Joshua Miller (RICS), Neil Monnery (Ashridge Strategic Management Centre), Ryland Thomas (Bank of England), John Turner (Queen's University Belfast).
- **United States:** Mark Carlsson (Federal Reserve), Kris Mitchener (Santa Clara), Jonathan D. Rose (Board of Governors), Kenneth Snowden (UNC Greensboro), Matthew Rognli (Northwestern).
- **Various countries:** Matthew Baron (Cornell), Michael Bordo (Rutgers), Lars Jonung (Lund), Josefin Meyer (Kiel Institute), Lyndon Moore (Univ. of Melbourne).
- **Doctoral students and postdocs:** Francisco Amaral, Ricardo Duque Gabriel, Chi Hyun Kim, Katharina Knoll, Dmitry Kuvshinov, Björn Richter, Kaspar Zimmermann.
- **Research assistants:** João Azevedo, Felipe Benguria, Xiaoting Chen, Sven Eis, Sherifa Elsherbiny, Stephanie Feser, Larissa Fuchs, Nina Furbach, Dimitrios Kanelis, Corinna Kohl, Sarah Leitner, Sandra Matuschke, Manuel Peter, Laura Puglisi, Karthik Reddy, Felix Rhiel, Mario Richarz, Thomas Schwarz, Mandy Skierlo, Lucie Stoppok, Maira Talha, Yevhenii Usenko, Dominik Robert Wehr, Marco Wyzietzki, Elin Al Zaim.

### "VARIABLE NAMES AND DESCRIPTIVE LABELS IN STATA" (pp. 5–7) — verbatim table

| Variable | Label |
|---|---|
| year | Year |
| country | Country |
| iso | ISO 3-letter code |
| ifs | IFS 3-number country-code |
| pop | Population |
| rgdpmad | Real GDP per capita (PPP, 1990 Int$, Maddison) |
| rgdpbarro | Real GDP per capita (index, 2005=100) |
| rconsbarro | Real consumption per capita (index, 2006=100) |
| gdp | GDP (nominal, local currency) |
| iy | Investment-to-GDP ratio |
| cpi | Consumer prices (index, 1990=100) |
| ca | Current account (nominal, local currency) |
| imports | Imports (nominal, local currency) |
| exports | Exports (nominal, local currency) |
| narrowm | Narrow money (nominal, local currency) |
| money | Broad money (nominal, local currency) |
| stir | Short-term interest rate (nominal, percent per year) |
| ltrate | Long-term interest rate (nominal, percent per year) |
| hpnom | House prices (nominal index, 1990=100) |
| unemp | Unemployment rate (percent) |
| wage | Wages (index, 1990= 100) |
| debtgdp | Public debt-to-GDP ratio |
| revenue | Government revenues (nominal, local currency) |
| expenditure | Government expenditure (nominal, local currency) |
| xrusd | USD exchange rate (local currency/USD) |
| peg | Peg dummy |
| peg_strict | Strict peg dummy |
| crisisJST | Systemic financial crises (0-1 dummy); included since R5 |
| crisisJST_old | Systemic financial crises (0-1 dummy); as coded in all prior releases (R1 – R4) |
| JSTtrilemmaIV | JST trilemma instrument (raw base rate changes) |
| tloans | Total loans to non-financial private sector (nominal, local currency) |
| tmort | Mortgage loans to non-financial private sector (nominal, local currency) |
| thh | Total loans to households (nominal, local currency) |
| tbus | Total loans to business (nominal, local currency) |
| bdebt | Corporate debt (nominal, local currency) |
| peg_type | Peg type (BASE, PEG, FLOAT) |
| peg_base | Peg base (GBR, USA, DEU, HYBRID, NA) |
| eq_tr | Equity total return, nominal. r[t] = [[p[t] + d[t]] / p[t-1] ] - 1 |
| housing_tr | Housing total return, nominal. r[t] = [[p[t] + d[t]] / p[t-1] ] - 1 |
| bond_tr | Government bond total return, nominal. r[t] = [[p[t] + coupon[t]] / p[t-1] ] - 1 |
| bill_rate | Bill rate, nominal. r[t] = coupon[t] / p[t-1] |
| rent_ipolated | 1 if housing rental yields interpolated e.g. wartime |
| housing_capgain_ipolated | 1 if housing capital gains and total returns interpolated e.g. wartime |
| housing_capgain | Housing capital gain, nominal. cg[t] = [ p[t] / p[t-1] ] - 1 |
| housing_rent_rtn | Housing rental return. dp_rtn[t] = rent[t]/p[t-1] |
| housing_rent_yd | Housing rental yield. dp[t] = rent[t]/p[t] |
| eq_capgain | Equity capital gain, nominal. cg[t] = [ p[t] / p[t-1] ] - 1 |
| eq_dp | Equity dividend yield. dp[t] = dividend[t]/p[t] |
| eq_capgain_interp | 1 if equity cap. gain interpolated to cover exchange closure |
| eq_tr_interp | 1 if equity total return interpolated to cover exchange closure |
| eq_dp_interp | 1 if equity dividend interpolated or assumed zero to cover exchange closure |
| bond_rate | Gov. bond rate, rate[t] = coupon[t] / p[t-1], or yield to maturity at t |
| eq_div_rtn | Equity dividend return. dp_rtn[t] = dividend[t]/p[t-1] |
| capital_tr | Tot. rtn. on wealth, nominal. Wtd. avg. of housing, equity, bonds and bills |
| risky_tr | Tot. rtn. on risky assets, nominal. Wtd. avg. of housing and equity |
| safe_tr | Tot. rtn. on safe assets, nominal. Equally wtd. avg. of bonds and bills |
| lev | Banks, capital ratio (in %) |
| ltd | Banks, loans-to-deposits ratio (in %) |
| noncore | Banks, noncore funding ratio (in %) |

All 59 columns of the R6 data sheet appear in this table and nowhere else in the front matter; the table gives no units beyond what is in the label, no year coverage, and no sources. There is no glossary, no methodological chapter, no crisis chronology and no returns-construction chapter in the document's table of contents — the body of the document (pp. 21–201) consists solely of country chapters.

### Table of contents (pp. 8–20)

The TOC lists one chapter per country, each with the same three blocks — *Macro Data* (Population … Wages), *Credit Data* (Total loans … Corporate debt) and *Bank balance sheet ratios* (Capital ratio, Loans-to-Deposits ratio, Noncore ratio) — at these printed pages: Australia 21; Belgium 31; Canada 42; Denmark 53; Finland 62; France 71; Germany 84; Ireland 97; Italy 104; Japan 113; Netherlands 124; Norway 134; Portugal 143; Spain 154; Sweden 164; Switzerland 172; United Kingdom 182; United States of America 192 (ending at p. 201 with "Noncore ratios"). The unit stated in each chapter heading is: millions AUD; (converted to) millions BEF; billions CAD; billions DKK; (converted to) millions FIM (New Markaa); (converted to) billions FRF (new francs); (converted to) billions DM; (converted to) millions IEP; (converted to) billions ITL; trillions JPY; (converted to) millions NLG; millions NOK; (converted) millions to PTE; (converted to) millions ESP; millions SEK; millions CHF; billions GBP; billions USD.

Chapter-specific TOC entries worth knowing: Australia has "Mortgage Loans to Households" and "Total Other Loans to Households"; Canada has "Total Other Loans", "Mortgage Loans to Households", "Total Other Loans to Households"; Germany has "Total Other Loans to Business"; Netherlands has "Mortgage Loans to Business"; Norway and the US have "Loans to Households Secured by Real Estate" (US credit items are labelled "(All Depository Institutions)"); Ireland has no Unemployment/Wages entries, lists "Peg variables" as one item, has no bank balance-sheet block, and is the only chapter with a **"Capital returns"** block (Government p. 104, Equity p. 104, Housing p. 105). Every chapter has an "Exogenous monetary policy shocks" item, which is the documentation for `JSTtrilemmaIV`.

---

## (b) General construction principles (as evidenced by the country chapters, pp. 21–100)

The document never states its methodology in one place; the following principles are what the per-variable source lists consistently show.

1. **Organisation.** For every country and every variable the documentation is a chronological list of source segments, "YYYY – YYYY from <source>", optionally followed by a treatment word: *Level(s)* (values taken as published), *Chainlinked / Chain-linked* (new segment linked to the previous one at the splice so that the level of the earlier/anchor segment is preserved and the new source contributes growth), *growth rate(s) calculated from* or *continuation of previous series with growth rates* (same idea, stated from the other side), *residual of A and B* (A minus B, both from the JST database itself), *sum of A and B*, *geometric interpolation* (Belgium revenue 1983–84), *linear interpolation* (Germany mortgage loans 1927), and *interpolated capital ratios* (Finland 1990/91). "Formerly:" marks a superseded source that is still listed (Belgium investment ratio).

2. **Units and currency.** All nominal series are in the chapter's local-currency unit (see the TOC list above). Euro-area members are expressed in the legacy currency throughout; euro-era data are "converted to" legacy units at the fixed conversion rates, which the chapters state explicitly where used: BEF 40.3399, FIM 5.94573 (misprinted as "Belgian franc-euro" in the Finland chapter), FRF 6.55957, DM 1.95583 per euro. Finland's old markka values are divided by 100 to obtain new markka. Where a source is in another currency (IMF IFS current accounts in USD for Canada and Germany; parts of Finland's current account), the series is redenominated with the JST `xrusd` series.

3. **Index bases.** `cpi`, `hpnom` and `wage` are rebased to 1990=100; `rgdpbarro` to 2005=100; `rconsbarro` to 2006=100. `rgdpmad` is in 1990 international (Maddison) dollars.

4. **Timing.** Most recent-period monetary, credit and balance-sheet segments are December / end-of-period values (often stated: "Dec values", "December values", "end of period"); several historical sources are annual averages (Metcalf money stock "year average of monthly data"; France total loans 1980–2013 "year average of monthly values"); interest rates are mostly annual averages, with some December values (Morawietz Tagesgeld; Investor's Monthly Manual bond yields). House prices are "year average values". Australian government finance uses June (fiscal-year) values. Canada's 2020 balance-sheet values use September.

5. **Ratios.** `iy` is nominal gross fixed capital formation (IMF IFS "Gross Fixed Capital Formation, Nominal") divided by JST nominal GDP after WWII; earlier segments use whatever the historical source provides (capital formation over NNP for Germany pre-1960; GFCF plus change in inventories for Belgium; Kamps' 1995-price ratio for Australia 1960–2001). `debtgdp` is gross public debt over GDP; where a source gives only a ratio it is multiplied by JST GDP to obtain a nominal debt series (Belgium), and where only nominal debt is given it is divided by JST GDP (Canada 2011–2020). Current accounts are often rebuilt as "% of GDP × nominal GDP from JST dataset". Bank ratios (`lev`, `ltd`, `noncore`) are computed from component series that are themselves documented segment by segment.

6. **"Credit."** `tloans` ("Total loans to non-financial private sector") is the stock of loans by banks to domestic households and non-financial business. Institutional coverage follows the national data: banks only in most countries; Denmark explicitly includes mortgage-credit institutes; Belgium's 1961–79 segment covers monetary institutions, savings banks, mortgage and capitalisation companies, life/accident insurers and pension funds; Germany's 1883–1940 segment "includes interbank exposures"; Australia's APRA segments include loans to financial corporations, government, NPIs and intra-group for consistency. `tmort` is loans secured by real estate or housing loans. `thh` and `tbus` split `tloans` by borrower; one of the two is frequently the residual of `tloans` minus the other. `bdebt` ("Corporate debt") is a broader concept — bank loans plus capital-market debt (BIS "Credit to the non-financial sector") or "total non-equity liabilities of the private non-financial business sector" (OECD / Eurostat financial accounts) — with bank-loan proxies before financial accounts exist.

7. **Bank balance-sheet ratios.** Identical formulas in every chapter: Capital ratio = Capital / Total Assets; Loans-to-Deposits ratio = Loans / Deposits; Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital); "Ratios in %, underlying data in <local unit>". When a source reports only a capital ratio (OECD Bank Profitability, APRA Tier 1, ECB Consolidated Banking Data tangible equity, Finnish interpolations), the ratio is chainlinked and multiplied by Total Assets to produce Capital.

8. **Exchange-rate regime dummies.** `peg` = 1 for Obstfeld–Taylor (2003) gold-standard adherence 1870–1939, then the unpublished revised Ilzetzki–Reinhart–Rogoff (2004) coarse classification 1940–2007 "(1=1-2, all 3-6=0); broad peg category including crawling pegs", extended 2008–2020 with the IRR (2008) scheme. `peg_strict` uses "(1=1, all 2-6=0); strict peg category excluding crawling pegs". Germany is set to 0 from 2000 ("deviation from Ilzetzki, Reinhart & Rogoff classification, where Germany, as a member of the Eurozone is categorized as a 1").

9. **Monetary-policy instrument.** Every chapter's "Exogenous monetary policy shocks" item is the same sentence: exogenous variation in the short-term interest rate from Jordà, Schularick, Taylor & Ward (2019, IMF Economic Review 67(1), 109–150), using the local-projection-IV identification of Jordà, Schularick & Taylor (2020, Journal of Monetary Economics 112, 22–40). This is the only documentation of `JSTtrilemmaIV` in these pages; no year coverage is given.

10. **Crisis indicator.** Nothing in pp. 1–100 defines `crisisJST` beyond the label "Systemic financial crises (0-1 dummy); included since R5" and `crisisJST_old` "as coded in all prior releases (R1 – R4)". No crisis dates appear in these pages, and the TOC shows no crisis chapter anywhere in the document.

11. **Returns.** The label table gives the formulas (total return = (p[t] + d[t])/p[t−1] − 1, etc.) and interpolation flags; `capital_tr`/`risky_tr` are weighted averages (weights not stated here) and `safe_tr` an equally weighted average of bonds and bills. Sources appear only in the Ireland "Capital returns" block (pp. 103–105), outside this range.

12. **Common cross-country source families.** Population: Maddison (2008) + IMF WEO growth rates. `rgdpmad`: Maddison-Project 2013 + IMF WEO PPP. `rgdpbarro`/`rconsbarro`: Barro–Ursúa (2010) + World Bank. `cpi`: Taylor (2002) + IMF WEO. `hpnom`: Knoll et al. (2014) + OECD. `ca`: Jones & Obstfeld (1997), Mitchell, IMF IFS/WEO. Trade: Mitchell + IMF IFS archive M10 2021. Interest rates: Neal–Weidenmier, Bordo et al. (2001), Homer & Sylla, League of Nations, Clemens–Williamson/Bank of England consols, Schmelzing (2020), IMF IFS, OECD. `xrusd`: Denzel (2010), Bordo et al. (2001), Officer/MeasuringWorth, Bordo–Jonung (1996), Reinhart–Rogoff (2010) black-market rates, IMF IFS. Debt: Abbas et al. (2010), Mauro et al. (2013), UN (1948), AMECO. Credit: national banking statistics, Müller (2018), BIS totcredit, OECD/Eurostat financial accounts. Unemployment: Mitchell, Maddison (1982), Galenson–Zellner (1957), ILOSTAT. Wages: Mitchell, Scholliers–Zamagni (1995), IMF IFS, OECD.

---
## (c) Variable dictionary

Labels are quoted verbatim from the Stata label table (PDF pp. 6–7). Definition/construction are summarised from the per-country sections (pp. 21–100); the full per-country source lists with year ranges are in section (d). Variables marked *label-table only* have no construction detail in pp. 1–100.

### `year` — Year

- **Units:** calendar year
- **Definition:** Observation year (annual data, 1870-2020).
- **Construction:** Identifier column.
- **Caveats / breaks:** —
- **PDF pages:** 6, 7

### `country` — Country

- **Units:** text
- **Definition:** Country name (18 countries in R6).
- **Construction:** Identifier column.
- **Caveats / breaks:** —
- **PDF pages:** 6, 7

### `iso` — ISO 3-letter code

- **Units:** text
- **Definition:** ISO 3166-1 alpha-3 country code.
- **Construction:** Identifier column.
- **Caveats / breaks:** —
- **PDF pages:** 6, 7

### `ifs` — IFS 3-number country-code

- **Units:** integer
- **Definition:** IMF International Financial Statistics numeric country code.
- **Construction:** Identifier column.
- **Caveats / breaks:** —
- **PDF pages:** 6, 7

### `pop` — Population

- **Units:** persons (thousands in most underlying sources; see country sections)
- **Definition:** Total population, annual.
- **Construction:** Typically Angus Maddison Database (2008) levels through 2008, extended with IMF World Economic Outlook population growth rates (Aug 2019 and Oct 2021 vintages). Finland uses Statistics Finland throughout; Belgium uses NBB 1953-2011; Germany switches to Maddison Project Database 2018 for 1991-2008 (reunification); Ireland uses Maddison Project (Bolt et al. 2018) 1921-1949 then CSO.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Growth-rate extensions mean recent levels are Maddison-based, not official. Some printed year ranges skip a year (e.g. Australia 2018). Ireland starts 1921. Per-country notes (pp. 21-100): Australia: As printed, the year ranges skip 2018 (2009–2017 then 2019–2020); presumably a typo in the document. | Germany: Switch to Maddison Project Database 2018 from 1991 (reunification). | Ireland: Ireland data start in 1921/1922 (independence), not 1870.
- **PDF pages:** 6, 7, 21, 31, 32, 42, 53, 62, 71, 85, 97

### `rgdpmad` — Real GDP per capita (PPP, 1990 Int$, Maddison)

- **Units:** 1990 international (Geary-Khamis) dollars per capita
- **Definition:** Real GDP per capita in PPP terms, Maddison concept.
- **Construction:** The Maddison-Project 2013 version levels 1870-2010, chain-linked forward with IMF WEO 'GDP based on PPP per capita' 2011-2020. Ireland instead uses IMF WEO 1980-2020 back-cast to 1922 with the growth rates of the CSO/Gerlach-Stuart real GDP per capita series and converted to 1990 Int$ with the US CPI.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Post-2010 values are IMF WEO PPP growth rates grafted on Maddison levels. Per-country notes (pp. 21-100): Ireland: Not Maddison-sourced for Ireland: IMF WEO PPP per capita, back-cast to 1922 with rgdpbarro growth rates and deflated to 1990 Int$ with the US CPI.
- **PDF pages:** 6, 7, 21, 32, 43, 53, 62, 63, 71, 85, 98

### `rgdpbarro` — Real GDP per capita (index, 2005=100)

- **Units:** index, 2005=100
- **Definition:** Real GDP per capita index from the Barro-Ursua macroeconomic data set.
- **Construction:** Barro & Ursua (2010) 1870-2004; extended 2005-2020 with growth rates of World Bank 'GDP per capita (constant 2010 US$)' (NY.GDP.PCAP.KD). Ireland: Gerlach & Stuart (2015) 1922-1969, CSO historical national accounts 1970-1994 (chainlinked), CSO National Income and Expenditure 1995-2020.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Belgium code CPCINXBE noted. Ireland not Barro-Ursua based and its 'GDP' tables are GNI-based (see gdp). Per-country notes (pp. 21-100): Ireland: Not Barro–Ursúa-sourced for Ireland.
- **PDF pages:** 6, 7, 21, 32, 43, 54, 63, 72, 86, 98

### `rconsbarro` — Real consumption per capita (index, 2006=100)

- **Units:** index, 2006=100
- **Definition:** Real per-capita consumption index.
- **Construction:** Barro & Ursua (2010) through 2009 (Australia: Vamplew ed. Australians Historical Statistics 1870-1900 chain-linked assuming 1901 consumption growth = real GDP per capita growth), then World Bank household final consumption expenditure per capita (constant 2010 US$) chain-linked 2010-2020. Ireland: Fitzgerald & Kenny (2019) 1938-1946, CSO publications thereafter, all chainlinked.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Start dates differ: Belgium 1913, Canada 1871, Ireland 1938. Per-country notes (pp. 21-100): Belgium: Series starts only in 1913 for Belgium. | Canada: Starts 1871. | Ireland: Starts 1938.
- **PDF pages:** 6, 7, 21, 22, 32, 43, 54, 63, 72, 86, 98, 99

### `gdp` — GDP (nominal, local currency)

- **Units:** nominal local currency; unit per country (millions AUD, millions BEF, billions CAD, billions DKK, millions FIM (new markka), billions FRF (new francs), billions DM, millions IEP)
- **Definition:** Nominal gross domestic product in local currency (legacy currency for euro members, converted at the fixed conversion rate).
- **Construction:** Historical national accounts (MeasuringWorth for Australia; GGDC HNA for Belgium; Dincecco-Prado for Canada; Mitchell IHS for Denmark and France; Hjerppe for Finland; growth rates from Burhop-Wolff NNP, Ritschl-Spoerer GNP and Sensch for Germany; Gerlach-Stuart and CSO for Ireland) spliced with IMF IFS nominal GDP for the post-war period; wartime gaps filled from Bordo, Eichengreen, Klingebiel & Martinez-Peria (2001).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Germany pre-1970 is built backwards from IFS by growth rates (NNP growth 1870-1912; real GNP reflated with JST CPI 1913-1924; 1945 missing). Ireland from 1970 is expenditure on Gross National Income (excluding FISIM), not GDP. Belgium 1914-1919 and 1940-1947 and France 1914-1919 and 1939-1949 from Bordo et al. Per-country notes (pp. 21-100): Germany: German nominal GDP is built backwards from 1970 IFS levels by growth rates; 1870–1912 uses NNP growth; 1913–1924 uses real GNP reflated with the JST CPI; 1945 missing. | Ireland: From 1970 the Irish "GDP" series is actually Gross National Income (expenditure on GNI, excluding FISIM) at current market prices, per the cited CSO tables.
- **PDF pages:** 6, 7, 21, 32, 42, 43, 53, 62, 71, 85, 98

### `iy` — Investment-to-GDP ratio

- **Units:** ratio (share of GDP)
- **Definition:** Gross (fixed) capital formation divided by nominal GDP.
- **Construction:** Mitchell International Historical Statistics or national yearbooks pre-WWII; IMF IFS 'Gross Fixed Capital Formation, Nominal' divided by JST nominal GDP post-war; Kamps (OECD capital-stock database) for Australia 1960-2001; van Meerten (2003) for Belgium 1900-1952 (GFCF + change in stocks over GDP); NBB national accounts for Belgium 1980-2020 ([GFCF + change in inventories]/NGDP).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Germany pre-1960 is capital formation over net national product, and Mitchell's 1873 values are shifted one column. The document cites van Meerten's 'Capital formation in Belgium' for Canada 1946-47, France 1920-24 and Germany 1920-49 - apparently a copy-paste error. Belgium lists overlapping IFS (1953-2014) and NBB (1980-2020) sources with a 'Formerly' NBB 1953-1979 source. Ireland has no source listed for 1970-1994. Many wartime gaps. Per-country notes (pp. 21-100): Australia: Gap 1947–1948 as printed. | Belgium: Starts 1900; no data 1914–1919 and 1940, 1942, 1944, 1945. The text lists both "1953–2014 IFS" and "1980–2020 NBB" entries (overlapping 1980–2014) with the NBB 1953–1979 entry marked "Formerly"; the document does not say which source wins in the overlap. | Canada: The 1946–1947 citation (van Meerten, Capital formation in Belgium) appears to be a copy-paste error in the document for a Canadian series; starts 1871. | France: The 1920–1924 van Meerten (Belgium) citation for a French series appears to be a copy-paste error in the document; 1919 and 1945 missing. | Germany: Pre-1960 ratio is capital formation over NNP, not GDP; gaps 1914–1919, 1940–1947. The repeated van Meerten (Belgium) citations for German interwar years look like a copy-paste error in the document. | Ireland: Starts 1944; no source listed for 1970–1994 as printed.
- **PDF pages:** 6, 7, 22, 32, 33, 43, 54, 63, 72, 86, 99

### `cpi` — Consumer prices (index, 1990=100)

- **Units:** index, 1990=100
- **Definition:** Consumer price index, annual average, rebased to 1990=100.
- **Construction:** A. Taylor (2002) 'A Century of Purchasing-Power Parity' 1870-1996 chainlinked with IMF WEO 'Inflation, average consumer prices' 1997-2020 for most countries. Belgium: NBB CPI 1870-2007 with wartime gaps (1915-19, 1940-45) filled by an implicit CPI backed out of Annaert et al. (2011) nominal vs real Brussels all-share indices. France: Mitchell IHS 1870-1965 then IMF IFS CPI. Ireland: CSO CPM02 1922-2020.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Belgian wartime CPI is a stock-index-implied deflator. Per-country notes (pp. 21-100): Belgium: Wartime CPI (1915–1919, 1940–1945) is an implicit deflator backed out of nominal vs real stock indices, not a true consumer price survey. | France: France is an exception to the usual Taylor (2002) CPI source.
- **PDF pages:** 6, 7, 22, 33, 43, 54, 63, 72, 86, 99

### `ca` — Current account (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Current account balance of the balance of payments.
- **Construction:** Jones & Obstfeld (1997) historical current accounts pre-1945 (Australia: CA excl. gold + net gold exports + change in monetary gold; Finland: % of GDP x NGDP, old markka /100), Mitchell IHS 'overall current balance' for the early post-war decades, IMF IFS current account balance, and IMF WEO current account % of GDP multiplied by nominal GDP for recent decades. Belgium pre-1947 uses the trade balance as a proxy. Ireland: Fitzgerald & Kenny (2019) 1938-2017 then CSO.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Where sourced in USD (Canada 1948-2020, Germany 1975-2020, parts of Finland 1946-1979) values are redenominated with the JST exchange rate. Wartime gaps for most countries. Per-country notes (pp. 21-100): Belgium: Pre-1947 (and 1949, 1952, 1953) "current account" is actually the merchandise trade balance. | Canada: Gap 1946–1947; the 1948–2020 IFS source is in US dollars (conversion to CAD is implied but not described). | Denmark: Starts 1874; gap 1915–1920. | France: Missing for both World Wars and 1946–1947. | Germany: Starts 1872; gaps 1914–1924 and 1939–1947. | Ireland: Starts 1938.
- **PDF pages:** 6, 7, 24, 35, 45, 55, 65, 74, 88, 89, 100

### `imports` — Imports (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Value of merchandise imports (goods, c.i.f.) - except Ireland, where from 1947 national-accounts imports of goods and services are used.
- **Construction:** Mitchell International Historical Statistics (or national sources: Horlings 2002 for Belgium, Hjerppe/Finnish Customs for Finland, Sensch GESIS for Germany 1872-1913) through 1947/1953, then IMF IFS archive M10 2021 'External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency' 1948-2020.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Belgium 1950-1997 covers Belgium-Luxembourg. Germany 1920-1923 excluded as inconsistent with hyperinflation. Denmark lists overlapping 1870-1953 and 1948-2020 sources. Per-country notes (pp. 21-100): Australia: 1914 not covered as printed. | Belgium: 1950–1997 figures cover the Belgium–Luxembourg Economic Union, not Belgium alone. Gaps 1914–1918 and 1940–1945. | Denmark: Ranges overlap 1948–1953 as printed. | Germany: Starts 1872; gaps 1914–1923 and 1944–1947. | Ireland: Starts 1937; from 1947 these are national-accounts exports/imports of goods and services, not customs merchandise trade.
- **PDF pages:** 6, 7, 24, 35, 45, 55, 65, 74, 89, 100

### `exports` — Exports (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Value of merchandise exports (goods, f.o.b.) - except Ireland, where from 1947 national-accounts exports of goods and services (excluding factor income flows) are used.
- **Construction:** Same sources as imports: Mitchell IHS / national sources, then IMF IFS archive M10 2021 'External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency' 1948-2020.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** See imports. Per-country notes (pp. 21-100): Australia: 1914 not covered as printed. | Belgium: 1950–1997 figures cover the Belgium–Luxembourg Economic Union, not Belgium alone. Gaps 1914–1918 and 1940–1945. | Denmark: Ranges overlap 1948–1953 as printed. | Germany: Starts 1872; gaps 1914–1923 and 1944–1947. | Ireland: Starts 1937; from 1947 these are national-accounts exports/imports of goods and services, not customs merchandise trade.
- **PDF pages:** 6, 7, 24, 35, 45, 55, 65, 74, 89, 100

### `narrowm` — Narrow money (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Narrow money stock (M1 or currency + demand/commercial-bank deposits).
- **Construction:** Historical monetary statistics (Pope 1986 for Australia; Delbeke 1988 for Belgium; Metcalf et al. 1996 for Canada; Johansen for Denmark; Mitchell IHS for Finland/Germany; Saint Marc 1983 for France; Gerlach & Stuart 2015 for Ireland) spliced via levels or growth rates with IMF IFS M1 and then national central bank M1 (euro members: national contribution to euro-area M1, redenominated into legacy currency).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Concepts vary (year-average vs December; M1 vs M1+ gross for Canada). Belgium starts 1877 with gaps 1914-1919 and 1941-1946; Germany gaps 1914-1922 and 1939-1947; Denmark gap 1946-1949. Per-country notes (pp. 21-100): Belgium: Starts 1877; gaps 1914–1919 and 1941–1946 as printed. | Canada: Starts 1871; concept shifts from year-average M1 to December M1+ (gross) in 2005. | Denmark: Gap 1946–1949. | France: Gap 1914–1919. | Germany: Gaps 1914–1922 and 1939–1947.
- **PDF pages:** 6, 7, 22, 33, 34, 44, 54, 63, 72, 87, 99

### `money` — Broad money (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Broad money stock (M2 or M3 depending on country/period).
- **Construction:** Historical sources (Pope; Metcalf et al./Bordo et al. 2001 'monagglc'; Abildgren chart & data book for Denmark 1870-2020; Bank of Finland email series and Mitchell; Saint Marc M1 + savings-bank deposits for France; Weber 2000 / Bordo et al. / GESIS files for Germany; Gerlach & Stuart for Ireland), then IMF IFS M2/M3 and national central-bank aggregates (euro members: national contribution to euro-area M2/M3).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Belgium broad money starts only in 1979. Germany mixes M2, M1 (1948-54) and M3 segments with gaps 1923-24 and 1939-47. Belgium 2002-2020 is M3 excluding currency in circulation. Per-country notes (pp. 21-100): Belgium: Broad money for Belgium starts only in 1979 as documented. | France: Gap 1914–1919. | Germany: Gaps 1923–1924 and 1939–1947; 1948–1954 segment is M1 (chainlinked), later M3.
- **PDF pages:** 6, 7, 22, 23, 34, 44, 54, 64, 73, 87, 99

### `stir` — Short-term interest rate (nominal, percent per year)

- **Units:** percent per year
- **Definition:** Short-term nominal interest rate (money-market, treasury-bill, discount or deposit rate depending on country/period).
- **Construction:** National historical rate series (Pope/Butlin savings-deposit rates for Australia; Drappier/NBB discount and 3-month Treasury certificate rates for Belgium; Autio for Finland; Abildgren for Denmark; Neal-Weidenmier open-market rates; Bordo et al. 2001; Homer & Sylla; League of Nations) spliced with IMF IFS treasury-bill / money-market rates and recent central-bank or OECD series.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Instrument changes across splices (e.g. Australia savings-deposit rates to 1944, T-bill 1969-2001, money market 2002-19, cash-rate target 2019-20). Canada starts 1934; Denmark 1875; gaps in wars/hyperinflation (Germany 1923, 1945-49; Belgium 1915-19; France 1915-21). Belgium lists overlapping Drappier 1920-2014 and Belgostat 1991-2020 sources. Per-country notes (pp. 21-100): Australia: Gap 1945–1947 as printed. Series mixes savings-deposit rates (pre-1945), short bonds, T-bill and money-market rates. | Belgium: As printed, the Drappier (1920–2014) and Belgostat (1991–2020) entries overlap for 1991–2014. | Canada: Documented Canadian short-term rate starts only in 1934. | Denmark: Starts 1875. | France: Gap 1915–1921. | Germany: Gaps 1923 (hyperinflation) and 1945–1949.
- **PDF pages:** 6, 7, 23, 34, 44, 55, 64, 73, 87, 88, 99, 100

### `ltrate` — Long-term interest rate (nominal, percent per year)

- **Units:** percent per year
- **Definition:** Long-term government bond yield (typically 10-year or consol/perpetual yields).
- **Construction:** Pre-1914 consol-based yields (Bank of England consol yield plus Clemens-Williamson 2004 spreads for Australia/Canada; Flandreau-Zumer for Germany; Autio for Finland; Drappier perpetual 2.5% debt for Belgium; Schmelzing 2020 for France and interwar Germany), interwar League of Nations / Homer & Sylla / Investor's Monthly Manual bond yields, IMF IFS 'Government Bonds' post-1948, OECD long-term rates for recent years. Germany 1948-55 uses 5% DM-Pfandbrief prices converted to yield as (100+5-value)/value.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Gaps: Belgium 1913-19, Finland 1939-47, Germany 1922-23 and 1944-47. Per-country notes (pp. 21-100): Finland: Gap 1939–1947 as printed. | Germany: Gaps 1922–1923 and 1944–1947; 1948–1955 is a Pfandbrief (mortgage bond) yield proxy computed from prices.
- **PDF pages:** 6, 7, 23, 24, 34, 35, 44, 45, 55, 64, 65, 73, 74, 88, 100

### `hpnom` — House prices (nominal index, 1990=100)

- **Units:** nominal index, 1990=100
- **Definition:** Nominal house price index, year-average values.
- **Construction:** Knoll, Schularick & Steger (2014) 'No price like home' through 2012, chain-linked with the OECD housing (analytical house price) nominal index 2013-2020.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Start years and gaps vary: Belgium 1878 (gap 1914-18), Canada 1921 (gap 1950-55), Denmark 1875, Finland 1905, Germany gaps 1923 and 1939-61. Ireland house prices fall outside pp. 1-100 (p. 102). Per-country notes (pp. 21-100): Belgium: Starts 1878; gap 1914–1918. | Canada: Starts 1921; gap 1950–1955. | Denmark: Starts 1875. | Finland: Starts 1905. | Germany: Gaps 1923 and 1939–1961.
- **PDF pages:** 6, 7, 26, 37, 47, 57, 67, 76, 91

### `unemp` — Unemployment rate (percent)

- **Units:** percent of labour force
- **Definition:** Unemployment rate.
- **Construction:** Mitchell IHS, Maddison (1982) 'Phases of Capitalist Development' Table 6, Galenson & Zellner (1957), Abildgren (Denmark), OECD ALFS (Finland 1980-90), chainlinked with ILOSTAT LFS-based unemployment rates for recent decades.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Coverage starts late and has wartime gaps (e.g. Belgium 1921; Canada 1916; France 1895 with gaps; Finland 1920; Germany 1887). France 1921-39 is wage/salary earners in manufacturing, mining and construction only. Per-country notes (pp. 21-100): Belgium: Starts 1921; gap 1940–1944. | Canada: Starts 1916. The 1938–1954 citation is to the "Europe" volume of Mitchell as printed. | Denmark: Starts 1874. | Finland: Starts 1920; gap 1939–1949. | France: Starts 1895; gaps 1914–1920 and 1940–1949. | Germany: Starts 1887; gap 1940–1945.
- **PDF pages:** 6, 7, 26, 37, 38, 47, 58, 67, 76, 92

### `wage` — Wages (index, 1990= 100)

- **Units:** index, 1990=100
- **Definition:** Nominal wage index.
- **Construction:** Historical wage series (MeasuringWorth average weekly earnings for Australia; Mitchell IHS money wages in industry; Scholliers & Zamagni 1995; Williamson 1995 real wages reflated with Taylor CPI for Canada 1870-1900; Meltz/Statistics Canada; Abildgren real hourly earnings reflated; Hjerppe for Finland; ILO yearbooks; Sommariva & Tullio for Germany), IMF IFS wage-rate indices 1948-1989, OECD average annual wages (current prices, levels) 1990-2020, all chainlinked; Germany 1951-2020 is Bundesbank compensation of employees per employee.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Wage concept changes across splices (hourly, daily, weekly, annual; industry vs all sectors). Gaps: Belgium 1942-46, France 1898-1911, Germany 1923. Per-country notes (pp. 21-100): Belgium: Gap 1942–1946 as printed; concepts switch between average annual, daily, hourly and annual wages across splices. | France: Gap 1898–1911. | Germany: 1923 missing (hyperinflation); from 1951 the series is compensation of employees per employee (Bundesbank), not a wage-rate index.
- **PDF pages:** 6, 7, 26, 38, 48, 58, 67, 76, 77, 92

### `debtgdp` — Public debt-to-GDP ratio

- **Units:** ratio (debt / GDP)
- **Definition:** Gross public debt relative to nominal GDP.
- **Construction:** IMF historical public debt databases (Abbas et al. 2010; Mauro et al. 2013), United Nations (1948) Public Debt 1914-1946, national sources (Belgostat ratios multiplied by JST GDP; Rahlf GESIS Schuldenquote for Germany 1871-1991; INSEE; Statistics Finland), then IMF WEO or EU AMECO 'Gross Public Debt (linked series) (UDGGL), % of GDP (EDP)' or Statistics Denmark EDP tables for recent decades. Canada 2011-2020: WEO general government gross debt nominal divided by JST GDP.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Government level differs across periods (France 1880-1979 central government only; Belgium Treasury debt; Germany territory changes). Gaps: Belgium 1914-19 and 1940-45; Denmark 1947-52, 1957-59, 1997; Finland starts 1914; Germany 1914-26 and 1944-49; France 1914-19 and 1939-48. Per-country notes (pp. 21-100): Denmark: Starts 1880; gaps 1947–1952, 1957–1959, 1997. | Finland: Starts 1914 for Finland. | France: "Note: Data for 1880 – 1979 is for central government debt only." | France: Starts 1880; gaps 1914–1919, 1939–1948; central government only before 1980, general government (EDP) from 1980. | Germany: Starts 1871; gaps 1914–1926, 1944–1949; territory changes (Reich / West Germany / unified Germany).
- **PDF pages:** 6, 7, 25, 36, 46, 56, 66, 75, 90

### `revenue` — Government revenues (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Government (mostly central/federal) revenue.
- **Construction:** Historical statistics (Liesner 1989; Mitchell IHS 'Government revenue and main tax yield'; Statistics Canada yearbooks; Johansen; Statistisches Jahrbuch; Ritschl 2002; McCarthy et al. 1952 and CSO for Ireland), national statistical offices, then OECD General Government accounts Table 12 (sector GS1311 central government for Canada, Denmark, France; general government total for Belgium) in levels.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany, Ireland (see section (d)).
- **Caveats / breaks:** Australia starts 1902 (Commonwealth only). Denmark 1972-94 is total taxes and duties; gap 1936-53. Germany 1960 value scaled x1.33 for a 9-month fiscal year; gaps 1916-24 and 1939-49. Belgium 1983-84 geometrically interpolated. Ireland entry continues on p. 101. Per-country notes (pp. 21-100): Australia: Starts 1902 (Federation); Commonwealth (federal) government only. | Belgium: Pre-1985 figures are central government (Mitchell); from 1985 general government (OECD). | Canada: Central government throughout (OECD sector GS1311 = central government). | Denmark: Gap 1936–1953 as printed; 1972–1994 is total taxes and duties rather than total revenue. | Finland: Starts 1882; central government. | France: Central government throughout. | Germany: Starts 1873; gaps 1916–1924, 1939–1949; federal (Bund/Reich) level; 1960 fiscal-year change adjusted x1.33. | Ireland: Entry continues on PDF page 101 (outside the assigned range: 1970 onward not captured here).
- **PDF pages:** 6, 7, 24, 35, 45, 56, 65, 74, 89, 100

### `expenditure` — Government expenditure (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Government (mostly central/federal) expenditure.
- **Construction:** Same families of sources as revenue: Liesner, Mitchell IHS 'Total central government expenditure', Flora (1983), national yearbooks, Ritschl 2002, Statistisches Bundesamt Fachserie 14, then OECD General Government accounts Table 12 series GTE in levels.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Denmark 1972-94 cites a taxation table (apparently a copy-paste error) and 1936 is missing. Germany gaps 1914-24 and 1939-49. Ireland expenditure is on p. 101 (outside range). Per-country notes (pp. 21-100): Denmark: 1936 missing as printed; the 1972–1994 entry cites a taxation table (probably a copy-paste error in the document). | Finland: Starts 1882; central government. | Germany: Starts 1873; gaps 1914–1924, 1939–1949.
- **PDF pages:** 6, 7, 24, 25, 36, 45, 46, 56, 66, 74, 89, 90

### `xrusd` — USD exchange rate (local currency/USD)

- **Units:** local currency units per US dollar (end of period in IFS segments)
- **Definition:** Nominal exchange rate against the US dollar.
- **Construction:** Denzel (2010) Handbook of World Exchange Rates (via GBP cross rates) or national sources pre-1914; Bordo et al. (2001); Officer/MeasuringWorth 'Exchange Rates Between the US Dollar and Forty-one Currencies' for the interwar years; Bordo & Jonung (1996) for WWII; Reinhart & Rogoff (2010) black-market rates for early post-war years; IMF IFS end-of-period national currency per USD thereafter. Euro-era rates translated into legacy currency at the fixed conversion rates (BEF 40.3399, FIM 5.94573, FRF 6.55957, DM 1.95583).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Early post-war values are black-market rates (Belgium 1946-53, Canada 1947-50, Denmark 1946-56, Finland 1946-60, France 1946-58). The Finland note misprints 'Belgian franc-euro' for the markka rate 5.94573. Germany 1945 missing. Per-country notes (pp. 21-100): Belgium: "We assume a Belgian franc-euro exchange rate of 40.3399 where necessary." 1946–1953 values are black-market rates. | Finland: "We assume a Belgian franc-euro exchange rate of 5.94573 where necessary." (sic — 5.94573 is the Finnish markka–euro conversion rate; the word "Belgian" is a copy-paste error in the document.) | France: "We assume a French franc-euro exchange rate of 6.55957 where necessary." | Germany: "We assume a German mark-euro exchange rate of 1.95583 where necessary." 1945 missing.
- **PDF pages:** 6, 7, 25, 36, 46, 56, 57, 66, 75, 90, 91

### `peg` — Peg dummy

- **Units:** 0/1 dummy
- **Definition:** 1 if the currency is pegged (broad definition including crawling pegs), 0 otherwise.
- **Construction:** Obstfeld & Taylor (2003) gold-standard adherence 1870-1939; unpublished revised Ilzetzki, Reinhart & Rogoff (2004) coarse classification 1940-2007 coded 1 if IRR category 1-2, 0 if 3-6; extended 2008-2020 with the IRR (2008) coarse classification scheme. Germany 2000-2020 set to 0 by JST, deviating from IRR which codes Germany (euro member) as pegged.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Germany's euro-era override makes it the base rather than a pegger. Ireland peg variables are on p. 102 (outside range). Per-country notes (pp. 21-100): Germany: Germany is coded as NOT pegged from 2000 (euro anchor country), deliberately deviating from IRR.
- **PDF pages:** 6, 7, 25, 37, 46, 47, 57, 66, 75, 76, 91

### `peg_strict` — Strict peg dummy

- **Units:** 0/1 dummy
- **Definition:** 1 if the currency is strictly pegged (IRR category 1 only, excluding crawling pegs), 0 otherwise.
- **Construction:** Obstfeld & Taylor (2003) 1870-1939; unpublished revised IRR (2004) 1940-2007 coded 1 if IRR category 1, 0 if 2-6; IRR (2008) extension 2008-2020. Germany 2000-2020 set to 0.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** France entry printed as '1940-2020' for the IRR 2004 source (presumably 1940-2007).
- **PDF pages:** 6, 7, 25, 26, 37, 47, 57, 66, 67, 76, 91

### `peg_type` — Peg type (BASE, PEG, FLOAT) — *label-table only in pp. 1–100*

- **Units:** categorical
- **Definition:** Exchange-rate regime type: BASE (anchor country), PEG, or FLOAT.
- **Construction:** Not documented in pp. 1-100 beyond the label table.
- **Caveats / breaks:** No construction detail in this page range.
- **PDF pages:** 6, 7

### `peg_base` — Peg base (GBR, USA, DEU, HYBRID, NA) — *label-table only in pp. 1–100*

- **Units:** categorical
- **Definition:** Base/anchor currency of the peg.
- **Construction:** Not documented in pp. 1-100 beyond the label table.
- **Caveats / breaks:** No construction detail in this page range.
- **PDF pages:** 6, 7

### `crisisJST` — Systemic financial crises (0-1 dummy); included since R5 — *label-table only in pp. 1–100*

- **Units:** 0/1 dummy
- **Definition:** Systemic financial crisis indicator (1 in crisis years), as recoded from Release 5 onward.
- **Construction:** Not documented in pp. 1-100 beyond the label table; no crisis chronology or definition appears in these pages (and none is listed in the table of contents).
- **Caveats / breaks:** Definition and dates not in this page range.
- **PDF pages:** 6, 7

### `crisisJST_old` — Systemic financial crises (0-1 dummy); as coded in all prior releases (R1 – R4) — *label-table only in pp. 1–100*

- **Units:** 0/1 dummy
- **Definition:** Systemic financial crisis indicator as coded in releases R1-R4.
- **Construction:** Not documented in pp. 1-100 beyond the label table.
- **Caveats / breaks:** Definition and dates not in this page range.
- **PDF pages:** 6, 7

### `JSTtrilemmaIV` — JST trilemma instrument (raw base rate changes)

- **Units:** percentage points (interest-rate changes)
- **Definition:** Instrument for exogenous monetary policy: the raw change in the base-country policy/short rate transmitted to pegging countries ('Exogenous monetary policy shocks' in the country sections).
- **Construction:** Per the identical text in every country section: exogenous variation in the short-term interest rate from Jorda, Schularick, Taylor and Ward (2019) 'Global financial cycles and risk premiums', IMF Economic Review 67(1), 109-150, using the local-projection IV identification of Jorda, Schularick and Taylor (2020) 'The effects of quasi-random monetary experiments', Journal of Monetary Economics 112: 22-40.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** The country sections give no year coverage; the heading is 'Exogenous monetary policy shocks' rather than the column name.
- **PDF pages:** 6, 7, 26, 37, 47, 57, 67, 76, 91

### `tloans` — Total loans to non-financial private sector (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Outstanding loans by banks (and in some countries other financial intermediaries) to the domestic non-financial private sector (households plus non-financial business).
- **Construction:** Historical banking statistics (Butlin-Hall-White; Annuaire Statistique / NBB Revue Economique; Urquhart Historical Statistics of Canada; Johansen and Abildgren; Bank of Finland; Saint Marc, Patat-Lutfalla, Monnet, Conseil National du Credit annual reports; Bundesbank 1976 and BBK01.PQA350) spliced in levels or growth rates with IMF IFS 'claims on private sector', central-bank loan statistics, and for recent years the sum of (or growth rate of) loans to households and loans to business. Denmark includes mortgage-credit institutes; Belgium 1961-79 covers a broad set of intermediaries; Germany 1883-1940 includes interbank exposures.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Institutional coverage changes across splices; wartime gaps in most countries (Belgium 1914-19 and 1941-49; France 1939-45; Germany 1941-45). France 1980-2013 year-average of monthly values vs end-of-period elsewhere. Per-country notes (pp. 21-100): Australia: Gap 1946–1947 as printed. | Belgium: Starts 1885; gaps 1914–1919 and 1941–1949. Early segments are growth-rate splices from narrow institutional coverage (credit unions, bank current-account debtors); 1961–1979 covers a broad set of financial intermediaries (monetary institutions, savings banks, mortgage and capitalisation companies, life/accident insurers, pension funds). | Finland: "Bank of Finland (2012), ibid." refers to the series sent by email by Essi Tamminen (see Narrow/Broad Money). | France: Starts 1900; gap 1939–1945. 1958–1962 = credits financed by monetary resources + credits financed by public funds or other resources; 1963–1979 = bank credits in metropolitan France (banks + Banque de France); 1980–2013 year averages of monthly values vs end-of-period from 2014. | Germany: Gap 1941–1945; 1883–1940 includes interbank exposures; territorial changes (Reich → West Germany → unified Germany).
- **PDF pages:** 6, 7, 26, 38, 39, 48, 49, 58, 59, 67, 68, 77, 78, 79, 92

### `tmort` — Mortgage loans to non-financial private sector (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Outstanding loans secured by real estate / housing loans to the non-financial private sector.
- **Construction:** Savings-bank and mortgage-institution balance sheets historically (Butlin-Hall-White Table 53(i); Schultze 1918 and Peters-Goosens-Buyst for Belgium; Canada Statistical Yearbooks and Urquhart; Abildgren mortgage-credit institutes; Finnish yearbook loans by security; Credit Foncier / Banque Hypothecaire archives and CNC 'credits au logement' for France; Bundesbank Hypothekenbanken and Prussian Sparkassen), then central-bank or national-accounts mortgage/housing-loan series; in Australia 1952-2020 equal to mortgage loans to households, in Canada tracked by the same series as mortgage loans to households, in France 1977-1999 the sum of household mortgages and business loans secured by real estate.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Canada 2011 IFRS break handled by extending 1990-2010 with growth of an IFRS-unaffected aggregate. Germany 1927 linearly interpolated. Finland changes from loans secured by real estate to household housing loans in 1979. Belgium from 2003 covers individuals only. Per-country notes (pp. 21-100): Belgium: Gaps 1914–1919 and 1940–1949. From 2003 the series covers mortgage loans of individuals (households) only. | Canada: Starts 1874. Known break: 2011 IFRS conversion brought securitized mortgages back onto bank balance sheets; JST avoids the jump by extending 1990–2010 with growth rates of an IFRS-unaffected aggregate. | Denmark: Starts 1875. Danish "mortgage loans" = lending by mortgage-credit institutes (to households and non-financial corporations), not bank mortgages. | Finland: Starts 1927; gap 1932–1933. Concept changes from loans secured by real estate (all borrowers, 1934–1978) to housing loans to households (1979 on). | France: Gaps 1934–1945. Pre-1934 series track mortgage lending of the Crédit Foncier / Banque Hypothécaire only; 1946–1976 is housing credit ("crédits au logement"). | Germany: Starts 1883; gaps 1920–1923, 1941–1948; 1927 linearly interpolated; pre-1920 covers mortgage banks + Prussian savings banks only.
- **PDF pages:** 6, 7, 27, 39, 49, 59, 68, 79, 80, 93

### `thh` — Total loans to households (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Outstanding bank loans to households.
- **Construction:** Sum of mortgage and other loans to households (Australia, Canada), national financial accounts (Belgium long-term loans of individuals; Finland households AF4 loans), Abildgren 'private lending' (Denmark 1951-2005) then residual of total loans minus business loans (Denmark 2006-2020, Germany 1950-2020, Finland 1948-69, France 1958-76), CNC 'credit aux menages', INSEE and Banque de France for France.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Starts only post-war: Australia 1952, Belgium 1950 (back-cast 1950-91 with mortgage growth), Canada 1956, Denmark 1951, Finland 1948, France 1958, Germany 1950. Per-country notes (pp. 21-100): Belgium: Starts 1950; 1950–1991 is extrapolated backward from mortgage-loan growth rates; 1992 onward covers long-term (over one year) loans only. | Denmark: Starts 1951. | Finland: Starts 1948. | France: Starts 1958 for France.
- **PDF pages:** 6, 7, 27, 39, 40, 50, 59, 68, 80, 81, 93

### `tbus` — Total loans to business (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Outstanding bank loans to (non-financial) business.
- **Construction:** Residual of total loans minus household loans in early post-war decades (Australia 1952-88, Belgium 1950-96, France 1980-2020, Finland 1970-2020), national financial accounts bank loans to non-financial corporations (Belgium 1997-), RBA/APRA commercial loans (Australia), Statistics Canada chartered-bank non-mortgage loans, Abildgren 'commercial lending' and Statistics Denmark MFI lending growth rates, Finnish yearbook loans by borrower group (base 1970), CNC 'credit aux entreprises industrielles et commerciales' (France 1958-79), Bundesbank BBK01.PQ3001 (Germany 1950-2020).
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Australia 2013 break: APRA series gross of bad-debt provisions and includes loans to financial corporations, government, NPIs and intra-group. Germany includes self-employed persons. Canada starts 1961. Per-country notes (pp. 21-100): Australia: Break in 2013: APRA series is gross of bad-debt provisions (RBA 1989–2012 series was net) and includes loans to financial corporations, general government, NPIs and intra-group loans. | Canada: Starts 1961. | Denmark: Starts 1951. | Finland: Starts 1948. | France: Starts 1958. | Germany: Bundesbank "Unternehmen und wirtschaftlich selbstständige Privatpersonen" includes self-employed persons in business loans.
- **PDF pages:** 6, 7, 28, 40, 50, 59, 68, 69, 81, 82, 93

### `bdebt` — Corporate debt (nominal, local currency)

- **Units:** nominal local currency (country unit)
- **Definition:** Total debt of the private non-financial business sector: bank loans plus capital-market debt (broader than tbus).
- **Construction:** Early post-war proxies (Muller 2018 'Credit Markets around the World'; residual of total loans minus household loans; chartered-bank lending; Abildgren commercial lending; Finnish yearbook loans; CNC credit to enterprises; Bundesbank loans and discounts of Großbanken/credit cooperatives; Bundesbank financial accounts), then BIS 'Credit to the non-financial sector' (bank loans + capital-market debt), OECD financial accounts total non-equity liabilities of the private non-financial business sector, Eurostat financial accounts, and BIS again for the latest years.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Concept shifts between bank-loan proxies, total non-equity liabilities and BIS credit across splices. Start dates: Australia 1948, Belgium 1950, Canada 1880, Denmark 1875, Finland 1948 (ends 2019 as documented), France 1902 (gap 1934-57), Germany 1885. Per-country notes (pp. 21-100): Canada: Starts 1880. | Denmark: Starts 1875. | Finland: Starts 1948; documented only to 2019. | France: Starts 1902; gap 1934–1957. | Germany: Starts 1885; gaps 1921–1923, 1945–1948.
- **PDF pages:** 6, 7, 28, 40, 50, 59, 60, 69, 82, 93, 94

### `lev` — Banks, capital ratio (in %)

- **Units:** percent
- **Definition:** Capital ratio = Capital / Total Assets of the banking sector, in percent.
- **Construction:** Computed from two documented components, Total Assets and Capital (see component entries). Where a source gives only a capital ratio (e.g. OECD Bank Profitability, APRA Tier 1 ratios, ECB tangible equity % of assets, Finnish interpolated 1990/91 ratios), the ratio is chainlinked and multiplied by the Total Assets series to obtain Capital.
- **Caveats / breaks:** Coverage differs by country and period (Australia trading + savings banks; Belgium major credit institutions from 1920; Canada chartered banks; Denmark commercial + savings banks; Finland commercial banks/MFIs; France from 1890 via Mazbouri et al. then Commission de controle des banques, OECD, ECB; Germany Aktienbanken + Hypothekenbanken + Sparkassen then all banks). Capital definitions change (shareholder funds, Tier 1, tangible equity). Per-country notes (pp. 21-100): Australia: Built from two components, Total Assets and Capital, documented separately below. Where only a capital ratio is available from a source, the ratio is chainlinked and multiplied by the Total Assets series to compute Capital. | Belgium: Built from Total assets and Capital components below. | Canada: Built from Total Assets and Capital components below; chartered banks only. | Denmark: Built from Total Assets and Capital components below (commercial banks + savings banks). | Finland: Built from Total Assets and Capital components below; starts 1873. | France: Built from Total Assets and Capital components below; starts 1890. | Germany: Built from Total Assets and Capital components below. Pre-1924 coverage is a sum of Aktien-Kreditbanken, Hypothekenbanken and Sparkassen (Prussia before 1900, Reich after), with early years chainlinked to Burhop (2004) Kreditbanken data; gaps 1921–1923 and 1941–1949.
- **PDF pages:** 6, 7, 28, 29, 30, 40, 41, 51, 52, 60, 61, 69, 70, 82, 83, 94, 95, 96

### `ltd` — Banks, loans-to-deposits ratio (in %)

- **Units:** percent
- **Definition:** Loans-to-Deposits ratio = Loans / Deposits of the banking sector, in percent.
- **Construction:** Computed from the documented Loans and Deposits components (see component entries); segments are levels or chainlinked.
- **Caveats / breaks:** France ratio starts 1946; Belgium 1920; others 1870/1873. Deposit and loan definitions change across splices (e.g. RBA D3 monetary-aggregate deposit codes from 2013; Bundesbank sums of series OU5664 and OUA175). Per-country notes (pp. 21-100): Australia: Built from Deposits and Loans components documented below. | Belgium: Built from Deposits and Loans components below. | Canada: Built from Deposits and Loans components below. | Denmark: Built from Deposits and Loans components below. | Finland: Built from Deposits and Loans components below. | France: Built from Deposits and Loans components below; starts 1946 for France. | Germany: Built from Deposits and Loans components below.
- **PDF pages:** 6, 7, 30, 31, 41, 42, 52, 53, 61, 62, 70, 83, 84, 96, 97

### `noncore` — Banks, noncore funding ratio (in %)

- **Units:** percent
- **Definition:** Noncore ratio = (Total Assets - Capital - Deposits) / (Total Assets - Capital), in percent: the share of bank liabilities (excluding capital) that is not customer deposits.
- **Construction:** Formula applied to the Total Assets, Capital and Deposits components documented under the capital and loans-to-deposits ratios; every country section gives only the formula.
- **Caveats / breaks:** Inherits the coverage and definition breaks of its components. Per-country notes (pp. 21-100): Australia: Formula only; computed from the Total Assets, Capital and Deposits components above. | Belgium: Formula only. | Canada: Formula only. | Denmark: Formula only. | Finland: Formula only. | France: Formula only. | Germany: Formula only.
- **PDF pages:** 6, 7, 31, 42, 53, 62, 71, 84, 97

### `eq_tr` — Equity total return, nominal. r[t] = [[p[t] + d[t]] / p[t-1] ] - 1 — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on equity: (price + dividend)/lagged price - 1.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `housing_tr` — Housing total return, nominal. r[t] = [[p[t] + d[t]] / p[t-1] ] - 1 — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on housing: (price + rent)/lagged price - 1.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `bond_tr` — Government bond total return, nominal. r[t] = [[p[t] + coupon[t]] / p[t-1] ] - 1 — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on government bonds: (price + coupon)/lagged price - 1.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `bill_rate` — Bill rate, nominal. r[t] = coupon[t] / p[t-1] — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal bill (short-term government paper) rate.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `rent_ipolated` — 1 if housing rental yields interpolated e.g. wartime — *label-table only in pp. 1–100*

- **Units:** 0/1 flag
- **Definition:** Flag: housing rental yield interpolated (e.g. wartime).
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `housing_capgain_ipolated` — 1 if housing capital gains and total returns interpolated e.g. wartime — *label-table only in pp. 1–100*

- **Units:** 0/1 flag
- **Definition:** Flag: housing capital gain and total return interpolated (e.g. wartime).
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `housing_capgain` — Housing capital gain, nominal. cg[t] = [ p[t] / p[t-1] ] - 1 — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal housing capital gain: price/lagged price - 1.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `housing_rent_rtn` — Housing rental return. dp_rtn[t] = rent[t]/p[t-1] — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Housing rental return: rent over lagged price.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `housing_rent_yd` — Housing rental yield. dp[t] = rent[t]/p[t] — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Housing rental yield: rent over current price.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_capgain` — Equity capital gain, nominal. cg[t] = [ p[t] / p[t-1] ] - 1 — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal equity capital gain: price/lagged price - 1.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_dp` — Equity dividend yield. dp[t] = dividend[t]/p[t] — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Equity dividend yield: dividend over current price.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_capgain_interp` — 1 if equity cap. gain interpolated to cover exchange closure — *label-table only in pp. 1–100*

- **Units:** 0/1 flag
- **Definition:** Flag: equity capital gain interpolated to cover a stock-exchange closure.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_tr_interp` — 1 if equity total return interpolated to cover exchange closure — *label-table only in pp. 1–100*

- **Units:** 0/1 flag
- **Definition:** Flag: equity total return interpolated to cover a stock-exchange closure.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_dp_interp` — 1 if equity dividend interpolated or assumed zero to cover exchange closure — *label-table only in pp. 1–100*

- **Units:** 0/1 flag
- **Definition:** Flag: equity dividend interpolated or assumed zero to cover a stock-exchange closure.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `bond_rate` — Gov. bond rate, rate[t] = coupon[t] / p[t-1], or yield to maturity at t — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Government bond rate: coupon over lagged price, or yield to maturity.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `eq_div_rtn` — Equity dividend return. dp_rtn[t] = dividend[t]/p[t-1] — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Equity dividend return: dividend over lagged price.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `capital_tr` — Tot. rtn. on wealth, nominal. Wtd. avg. of housing, equity, bonds and bills — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on wealth: weighted average of housing, equity, bonds and bills.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `risky_tr` — Tot. rtn. on risky assets, nominal. Wtd. avg. of housing and equity — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on risky assets: weighted average of housing and equity.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### `safe_tr` — Tot. rtn. on safe assets, nominal. Equally wtd. avg. of bonds and bills — *label-table only in pp. 1–100*

- **Units:** decimal rate (annual)
- **Definition:** Nominal total return on safe assets: equally weighted average of bonds and bills.
- **Construction:** Not documented in pp. 1-100 beyond the formula in the label table (pp. 6-7). The table of contents shows 'Capital returns' subsections (Government, Equity, Housing) only for Ireland (pp. 103-105), outside this range. The terms of use direct users of asset-price/return data to cite Jorda, Knoll, Kuvshinov, Schularick & Taylor (2019), 'The Rate of Return on Everything, 1870-2015', QJE.
- **Caveats / breaks:** Rates in the labels are written as decimals (r[t] = ... - 1); weights for capital_tr/risky_tr are not given in this range.
- **PDF pages:** 6, 7

### *(no column; component)* — Total Assets (bank balance-sheet component)

- **Units:** nominal local currency (country unit)
- **Definition:** Total assets (or total liabilities) of the banking sector; denominator of lev and used in noncore.
- **Construction:** Per-country balance-sheet aggregates, levels or chainlinked; see sources.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Per-country notes (pp. 21-100): Belgium: Bank balance-sheet data for Belgium start only in 1920; 1934 missing as printed.
- **PDF pages:** 29, 40, 41, 51, 60, 69, 82, 83, 94, 95

### *(no column; component)* — Capital (bank balance-sheet component)

- **Units:** nominal local currency (country unit)
- **Definition:** Bank capital (share capital + reserves, shareholders' funds, Tier 1 or tangible equity depending on period); numerator of lev and used in noncore.
- **Construction:** Levels where available; otherwise a capital ratio chainlinked and multiplied by Total Assets.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** Per-country notes (pp. 21-100): Australia: Gap 1946–1950 as printed. | Finland: 1990/1991 capital ratios are interpolated because of a regulatory change allowing transfer of 90% of loan-loss reserves to reserve funds in 1990.
- **PDF pages:** 29, 30, 41, 51, 52, 60, 61, 69, 70, 83, 95, 96

### *(no column; component)* — Deposits (bank balance-sheet component)

- **Units:** nominal local currency (country unit)
- **Definition:** Customer/non-bank deposits of the banking sector; denominator of ltd and used in noncore.
- **Construction:** Per-country balance-sheet aggregates, levels or chainlinked.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** —
- **PDF pages:** 30, 41, 52, 61, 70, 83, 84, 96

### *(no column; component)* — Loans (bank balance-sheet component)

- **Units:** nominal local currency (country unit)
- **Definition:** Loans/advances of the banking sector; numerator of ltd.
- **Construction:** Per-country balance-sheet aggregates, levels or chainlinked.
- **Per-country sources in this range:** Australia, Belgium, Canada, Denmark, Finland, France, Germany (see section (d)).
- **Caveats / breaks:** —
- **PDF pages:** 30, 31, 41, 42, 52, 53, 61, 62, 70, 84, 96, 97

### *(no column; component)* — Mortgage Loans to Households (household-credit component)

- **Units:** nominal local currency (country unit)
- **Definition:** Housing/mortgage loans to households; component of thh (Australia, Canada) and equal to tmort in Australia from 1952.
- **Construction:** See sources.
- **Per-country sources in this range:** Australia, Canada (see section (d)).
- **Caveats / breaks:** —
- **PDF pages:** 27, 50

### *(no column; component)* — Total Other Loans to Households (household-credit component)

- **Units:** nominal local currency (country unit)
- **Definition:** Non-mortgage (personal/consumer) loans to households; component of thh (Australia, Canada).
- **Construction:** See sources.
- **Per-country sources in this range:** Australia, Canada (see section (d)).
- **Caveats / breaks:** Per-country notes (pp. 21-100): Canada: Starts 1956, so thh for Canada starts 1956.
- **PDF pages:** 27, 50

### *(no column; component)* — Total Other Loans (Canada; residual)

- **Units:** nominal local currency (billions CAD)
- **Definition:** Residual of total loans to the non-financial private sector minus mortgage loans (Canada).
- **Construction:** Residual.
- **Per-country sources in this range:** Canada (see section (d)).
- **Caveats / breaks:** —
- **PDF pages:** 49

### *(no column; component)* — Total Other Loans to Business (Germany; residual)

- **Units:** nominal local currency (billions DM)
- **Definition:** Residual of mortgage loans to the non-financial private sector minus mortgage loans to households (Germany), i.e. mortgage loans to business, as printed.
- **Construction:** Residual.
- **Per-country sources in this range:** Germany (see section (d)).
- **Caveats / breaks:** Per-country notes (pp. 21-100): Germany: As printed (heading "Total Other Loans to Business" defined as mortgage loans total minus mortgage loans to households, i.e. mortgage loans to business).
- **PDF pages:** 93
## (d) Per-country sources by variable (PDF pp. 21–100)

Each bullet is `years — source` as the document gives it (abbreviated only where a run of identical annual citations repeats, which is flagged with 'Same series'). Two cosmetic normalisations were applied throughout: the document's recurring misspellings 'Pallgrave MacMillen' and '21st Centry' are written 'Palgrave Macmillan' and '21st Century', and 'Karsten Muller ( ¨ 2018)' is written 'Karsten Müller (2018)'; everything else, including the document's own typos and inconsistencies, is left as printed. *Note* lines are my observations (gaps, overlaps, apparent typos) unless they quote the document. The bold heading reproduces the document's section heading (which carries the unit), followed by the dataset column name (or *component* for sub-series that have no column of their own).

### Australia (AUS) — "Data in millions AUD" — PDF pp. 21–31

**Population** — `pop` — pp. 21

- 1870–2008 — Angus Maddison Database (2008), Historical statistics of the world economy: 1–2008 AD. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.rug.nl/research/ggdc/data/maddison-historical-statistics).
- 2009–2017 — growth rates from International Monetary Fund (Aug, 2019), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at http://www.imf.org/external/data.htm).
- 2019–2020 — growth rates from International Monetary Fund (Oct, 2021), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at http://www.imf.org/external/data.htm).
- *Note:* As printed, the year ranges skip 2018 (2009–2017 then 2019–2020); presumably a typo in the document.

**GDP (millions AUD)** — `gdp` — pp. 21

- 1870–2020 — Diane Hutchinson and Florian Ploeckl, "What Was the Australian GDP or CPI Then?" MeasuringWorth, 2021. URL: http://www.measuringworth.com/australiadata/. Level.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 21

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund, World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 21

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator/NY.GDP.PCAP.KD).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 21, 22

- 1870–1900 — Australians Historical Statistics, 2007. Vamplew, W (Editor). Chapter 12: Prices and Consumption. Table 182-183: Social Accounting Indicators of Living Standards, Constant Prices, Australia 1818-1982. Chain linked (assuming the 1901 per capita consumption growth rate equalled the per capita real GDP growth rate in order to link the 1870–1900 and the 1900–2009 series).
- 1901–2009 — Robert C. Barro and José F. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.

**Investment-to-GDP ratio** — `iy` — pp. 22

- 1870–1946 — Pre-WWII data: Mitchell, Brian (2007), International Historical Statistics: Africa, Asia & Oceania, 1750–2005, Palgrave Macmillan, London.
- 1949–1959 — International Monetary Fund (2013), International Financial Statistics. Data Report "Economic indicators", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- 1960–2001 — Kamps, Christophe. Database on Capital Stocks in OECD countries. Series: Gross total fixed capital formation (1995 prices) divided by GDP (1995 prices). Underlying source: OECD analytical database. https://www.ifw-kiel.de/academy/databases/netcap_e
- 2002–2020 — International Monetary Fund, International Financial Statistics. Data Report "Economic indicators", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- *Note:* Gap 1947–1948 as printed.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 22

- 1870–1996 — A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
- 1997–2020 — International Monetary Fund World Economic Outlook (April 2019). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.

**Narrow Money (millions AUD)** — `narrowm` — pp. 22

- 1870–1983 — "PF 57–71" from David Pope, Australian Money and Banking Statistics, Canberra, Australian National University, 1986.
- 1984–2002 — continuation of previous series with growth rates calculated from International Monetary Fund, International Financial Statistics. M1, seasonally adjusted (available at IMF CD-ROM 2014: Economic Concept View – Financial Indicators – Monetary Aggregates).
- 2003–2020 — continuation of previous series with growth rates calculated from Reserve Bank of Australia, Statistical Tables, Money and credit statistics, monetary aggregates, M1: seasonally adjusted, December values.

**Broad Money (millions AUD)** — `money` — pp. 22, 23

- 1870–1978 — "PF 57–71" from David Pope, Australian Money and Banking Statistics, Canberra, Australian National University, 1986.
- 1979–2013 — International Monetary Fund, eLibrary. International Financial Statistics. Monetary Aggregates - M3.
- 2013–2020 — Reserve Bank of Australia, Statistical Tables, Money and credit statistics, monetary aggregates, M3: original, December values.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 23

- 1870–1914 — Pope, D. 1986. Australian Money and Banking Statistics. Table 7: Interest Rates, Savings Banks Deposits. Online: www.se.anu.edu.au
- 1915–1928 — Butlin, S. (1971). Australian banking and monetary statistics 1817-1945. P.535 Table 63(ii). Savings Banks maximum interest rates and limits on deposits earning interest 1901-1945. Average of seven rates.
- 1929–1944 — League of Nations, International Statistical Yearbook (various issues), League of Nations, Geneva. Average annual rate.
- 1948–1968 — International Monetary Fund (2016), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – Government Securities – Bonds short term" (accessible online at http://data.imf.org/).
- 1969–2001 — International Monetary Fund (2018), IFS. Section "Economic indicators", Series "Interest Rates – Government Securities – Treasury Bill Rate" (accessible online at http://data.imf.org/).
- 2002–2019 — International Monetary Fund (2021), IFS. Section "Economic indicators", Series "Interest Rates – Money Market Rate percent per anum" (accessible online at http://data.imf.org/).
- 2019–2020 — Reserve Bank of Australia, Interest rates, F1.1 INTEREST RATES AND YIELDS – MONEY MARKET, average of cash rate target (accessible online at: https://www.rba.gov.au/statistics/tables/).
- *Note:* Gap 1945–1947 as printed. Series mixes savings-deposit rates (pre-1945), short bonds, T-bill and money-market rates.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 23, 24

- 1870–1914 — sum of "Yield on consols" (from Bank of England, Three centuries of macroeconomic data, Series: Yield on consols) and "Spread on consols" (from Clemens, M. A. and Williamson, J. G. (2004). Wealth bias in the first global capital market boom, 1870–1913. The Economic Journal.)
- 1915–1925 — Lamberton, D. M. L. (1958). Some statistics of security prices and yields in the Sydney market, 1875-1933. Table III. Average annual rate.
- 1926–1934 — League of Nations, International Statistical Yearbook (various issues), League of Nations, Geneva.
- 1935–1947 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. Average annual rate.
- 1948–2016 — International Monetary Fund International Financial Statistics (IFS). Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds, percent per anum" (accessible online at https://data.imf.org).
- 2017–2020 — OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en, average of monthly values.

**Current Account (millions AUD)** — `ca` — pp. 24

- 1870–1945 — M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA (accessible online at http://www.nber.org/databases/jones-obstfeld/). Sum of CA excl. gold flows + net exports gold + change in monetary gold stock (see paper for derivation of this equation). Level.
- 1946–1979 — B. Mitchell (2013) International Historical Statistics. National Accounts - Balance of payments - overall current balance. Level.
- 1980–2020 — International Monetary Fund, World Economic Outlook. % of GDP * nominal GDP from JST dataset = Current Account (accessible online: http://www.imf.org/external).

**Imports & Exports (millions AUD)** — `imports,exports` — pp. 24

- 1870–1913 — B. Mitchell (2007), International Historical Statistics: Africa, Asia & Oceania 1750–2005, Palgrave Macmillan, London.
- 1915–1947 — B. Mitchell (2007), International Historical Statistics: Africa, Asia & Oceania 1750–2005, Palgrave Macmillan, London.
- 1948–2020 — International Monetary Fund, International Financial Statistics: archive, M10 2021, External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency; External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency.
- *Note:* 1914 not covered as printed.

**Government Revenues (millions AUD)** — `revenue` — pp. 24

- 1902–1948 — Liesner, T. (1989). One hundred years of economic statistics. Table A9 Public Finance. Series: Total receipts.
- 1949–1996 — Australian Bureau of Statistics: Statistical Yearbook of Australia, various issues.
- 1997–2013 — Reserve Bank of Australia (2013), Discontinued data – Government finance - "E1 Australian Government Budget", Total revenues (accessible online at http://www.rba.gov.au/statistics/tables/). June values (fiscal year).
- 2014–2020 — Australian Bureau of Statistics. 5512.0 Government Finance Statistics. Commonwealth Government. GFS Revenue.
- *Note:* Starts 1902 (Federation); Commonwealth (federal) government only.

**Government Expenditure (millions AUD)** — `expenditure` — pp. 24, 25

- 1902–1948 — Liesner, T. (1989). One hundred years of economic statistics. Table A9 Public Finance. Series: Total expenditure.
- 1949–1996 — Australian Bureau of Statistics: Statistical Yearbook of Australia, various issues. (For early years, expenditure is the combined expenditure of the Commonwealth Revenue Fund and the Loan Fund.)
- 1997–2013 — Reserve Bank of Australia, File "E1 Australian Government Budget", Total expenses (accessible online at http://www.rba.gov.au/statistics/tables/).
- 2014–2020 — Australian Bureau of Statistics. 5512.0 Government Finance Statistics. Commonwealth Government. GFS Expenses.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 25

- 1870–1994 — Mauro, Paolo, Rafael Romeu, Ari Binder, Asad Zaman (2013), "A Modern History of Fiscal Prudence and Profligacy", IMF Working Paper No. 13/5.
- 1995–2020 — IMF. World Economic Outlook. 2021. Series: Public Debt % of GDP.

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 25

- 1870–1879 — Australian Historical Statistics. Editor: Vamplew, W. Fairfax, Syme & Weldon Associates. Pp. 243-244. Inverse of GBP/AUD exchange rate multiplied with GBP/USD exchange rate (see USD exchange rate sources for the U.K.).
- 1880–1938 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1939–1947 — Australian Historical Statistics. Editor: Vamplew, W. Fairfax, Syme & Weldon Associates. Pp. 243-244. Inverse of GBP/AUD exchange rate multiplied with GBP/USD exchange rate (see USD exchange rate sources for the U.K.).
- 1948–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy** — `peg` — pp. 25

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 25, 26

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 26

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 26

- 1870–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** — `unemp` — pp. 26

- 1901–1980 — Mitchell, Brian (2013), International Historical Statistics Africa, Asia, Oceania, 1750–2010, Table B2 Oceania Unemployment, Palgrave Macmillan, London.
- 1981–2020 — ILOSTAT (2021), Table "Unemployment rate by sex and age" based on the Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/.

**Wages (index, 1990=100)** — `wage` — pp. 26

- 1870–2020 — Diane Hutchinson and Florian Ploeckl, "Weekly Wages, Average Compensation and Minimum Wage for Australia from 1861-Present" MeasuringWorth, 2021. Average weekly earnings, all employees (pounds and dollars). Levels. Accessible online at https://www.measuringworth.com/datasets/auswages/

**Total loans to non-financial private sector (Credit Data, millions AUD)** — `tloans` — pp. 26

- 1870–1945 — calculated from S.J. Butlin, A.R. Hall, & R.C. White (1971), Australian Banking and Monetary Statistics 1817–1945, Reserve Bank of Australia, Sydney. Calculated by adding Table 1 "Total assets within Australia and total advances in Australia" and Table 53(i) "Savings banks, aggregate balance sheet", Series "Mortgage loans".
- 1948–1952 — growth rate calculated from International Monetary Fund, International Financial Statistics, series 32d "Claims on private sector".
- 1953–1988 — Reserve Bank of Australia (2012), Australian Economic Statistics 1949–1950 to 1996–1997, Reserve Bank of Australia. Table 3.2 "Lending and credit aggregates", Series "Loans and advances by financial intermediaries – banks" (accessible online at http://www.rba.gov.au/statistics/frequency/occ–paper–8.html#section_3).
- 1989–2020 — sum of Total Loans to Households and Total Loans to Business.
- *Note:* Gap 1946–1947 as printed.

**Mortgage loans to non-financial private sector** — `tmort` — pp. 27

- 1870–1945 — calculated from S.J. Butlin, A.R. Hall, & R.C. White (1971), ibid. Table 53(i) "Savings banks, aggregate balance sheet".
- 1952–2020 — equal to Mortgage Loans to Households.

**Total Loans to Households** — `thh` — pp. 27

- 1952–2020 — sum of Mortgage Loans to Households and Total Other Loans to Households.

**Mortgage Loans to Households (component of thh/tmort)** — *component* — pp. 27

- 1952–1975 — growth rate calculated from Australian Bureau of Statistics (various), Statistical Yearbook (various issues). Series "Housing loans from savings bank"; and Reserve Bank of Australia (2012), ibid. Table 3.7.b "All banks: assets", Series "Loans, advances and bills held (b) of which: housing loans".
- 1976–2012 — Reserve Bank of Australia; Table: Banks – On-balance Sheet Assets, Liabilities and Off-balance Sheet Business – B2; Series: BBARALAP "Resident Assets – Loans & Advances – Residential" (accessible online at http://www.rba.gov.au/statistics/tables/index.html#historical).
- 2013–2018 — Monthly Authorised Deposit-taking Institution Statistics; Monthly Banking Statistics June 2019 back series: Table 1 Sum of "Loans to households: Housing: Owner-occupied" and "Loans to households: Housing: Investment" (TOTAL end of period values) (accessible online at https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics).
- 2019–2020 — Monthly Authorised Deposit-taking Institution Statistics; Monthly Banking Statistics back-series March 2019 – February 2022: Table 1 Sum of "Loans to households: Housing: Owner-occupied" and "Loans to households: Housing: Investment" (TOTAL end of period values) (accessible online at https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics).

**Total Other Loans to Households (component of thh)** — *component* — pp. 27

- 1952–1975 — Australian Bureau of Statistics, Statistical Yearbook (various). "Advances for persons excluding housing – trading banks only" (accessible online at http://www.abs.gov.au/).
- 1976–2012 — Reserve Bank of Australia; Table: Banks – On-balance Sheet Assets, Liabilities and Off-balance Sheet Business – B2; Series: BBARALAP "Resident Assets – Loans & Advances – Personal" (accessible online at http://www.rba.gov.au/statistics/tables/index.html#historical).
- 2013–2020 — Australian Prudential Regulation Authority; Monthly Banking Statistics: Table 2 Loans and advances on Australian books of individual banks – Households: sum of "Credit cards" and "Other" (TOTAL) (accessible online at http://www.apra.gov.au/adi/Publications/Pages/monthly–banking–statistics.aspx).

**Total Loans to Business** — `tbus` — pp. 28

- 1952–1988 — residual of Total loans to non-financial private sector and Total Loans to Households.
- 1989–2012 — Reserve Bank of Australia; Table: Banks – On-balance Sheet Assets, Liabilities and Off-balance Sheet Business – B2; Series: BBARALAP "Resident Assets – Loans & Advances – Commercial" (accessible online at http://www.rba.gov.au/statistics/tables/index.html#historical).
- 2013–2017 — Australian Prudential Regulation Authority; Monthly Banking Statistics: Table 1 Monthly banking statistics back series sum of Loans to: "Non-financial corporations", "Financial corporations", "General government", "Community service organisations and NPI" and "Intra-group loans and advances" (TOTAL end of period values) (accessible online at https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics). Note: this sum is gross of specific and general provisions for bad debts, while the 1989–2012 RBA series was a net value. The inclusion of loans other than to non-financial corporations is for reasons of series consistency across time.
- 2018–2020 — Australian Prudential Regulation Authority; Monthly authorised deposit-taking institutions statistics back series: Table 1 sum of Loans to "Non-financial business", "Financial institutions", "General government", "Community services organisation" and "Intra-group loans and finance advances" (TOTAL end of period values) (accessible online at https://www.apra.gov.au/monthly-authorised-deposit-taking-institution-statistics).
- *Note:* Break in 2013: APRA series is gross of bad-debt provisions (RBA 1989–2012 series was net) and includes loans to financial corporations, general government, NPIs and intra-group loans.

**Corporate debt** — `bdebt` — pp. 28

- 1948–1954 — lending to non-financial corporate business from Karsten Müller (2018) "Credit Markets around the World, 1910–2014", from SSRN (accessible online at https://ssrn.com/abstract=3259636).
- 1955–1976 — residual of total bank loans to non-financial private sector and total bank loans to households (both from JST MacroHistory Database).
- 1977–1988 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- 1989–2013 — total non-equity liabilities of the private non-financial business sector from OECD financial accounts data.
- 2014–2020 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).

**Capital ratio = Capital / Total Assets (Bank balance sheet ratio; ratios in %, underlying data in millions AUD)** — `lev` — pp. 28, 29, 30

- *Note:* Built from two components, Total Assets and Capital, documented separately below. Where only a capital ratio is available from a source, the ratio is chainlinked and multiplied by the Total Assets series to compute Capital.

**Total Assets (component of lev/ltd/noncore; millions AUD)** — *component* — pp. 29

- 1870–1945 — Butlin, Hall and White, Australian banking and monetary statistics, 1817-1945, Reserve Bank of Australia (1971), Part B, Table 2(i) and 2(ii) Aggregate Trading Banks, Series "Total Capital and Liabilities" (chainlinked with Table 1, series "Assets in Australia" for years 1870-1876) + Table 53 (i) Aggregate Saving Banks, Series "Total Assets". June or December values depending on availability. Levels.
- 1950–1953 — Reserve Bank of Australia, Discontinued Data, "Table 3.8 Trading Banks: Deposit Liabilities and Selected Assets (a)", series "Total Assets" + Table 3.9 "Saving Banks: Deposit Liabilities and Selected Assets (a)", series "Total Assets" (1950-1952 chainlinked with Series "Public Sector Securities" growth rates), accessible online (http://www.rba.gov.au/statistics/discontinued-data.html). Chainlinked.
- 1954–1996 — Reserve Bank of Australia, Discontinued Data, "Table 3.4a Total Assets of Financial Institutions", series "Total - Banks other than Reserve Bank", accessible online (http://www.rba.gov.au/statistics/discontinued-data.html). June values. Chainlinked.
- 1997–2020 — Reserve Bank of Australia, Statistical Tables, "Table B1- Assets of Financial Institutions", Series "Assets; Banks", series key BAFITADI, June values. Levels.

**Capital (component of lev; millions AUD)** — *component* — pp. 29, 30

- 1870–1945 — Butlin, Hall and White, Australian banking and monetary statistics, 1817-1945, Reserve Bank of Australia (1971), Part B, Table 2(i) and 2(ii) Aggregate Trading Banks, series "Shareholder's equity" + Table 53(i) Aggregate Savings Banks, series "Reserves and Undivided Profits". June or December values. Levels.
- 1951–1962 — White, R.C., Australian Banking and Monetary Statistics 1945–1970, (1973), Occasional Papers 4B, series "Capital"+"Reserves" divided by "Total liabilities" for Trading Banks. Savings Banks capital ratio chainlinked from 1963 value with trading banks capital ratio changes. Chainlinked as capital ratio. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- 1963–1980 — Australian Statistical Yearbooks, various issues, All Trading Banks (Cheque Paying Banks Grand Total or Private Trading Banks), series "Total Shareholder Funds" divided by "Total Liabilities" + Total Savings Banks, series "Shareholder's Funds" divided by "Total Liabilities". Chainlinked as capital ratio. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- 1981–1988 — OECD, Bank Profitability, Statistical Supplement, Financial Statements of Banks, capital ratio computed as "Capital and Reserves" divided by "Total Assets" end of year values. Chainlinked as capital ratio. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- 1989 — Reserve Bank of Australia, Capital ratio from Table B6 – Consolidated Group Capital of Banks "Tier 1 Ratio", Chainlinked capital ratio. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- 1990–2003 — OECD, Bank Profitability, Statistical Supplement, Financial Statements of Banks, capital ratio computed as ("Tier 1 Capital" less "Supervisory Reductions") divided by "Total Assets" from OECD series, end of year values. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- 2004–2020 — Australian Prudential Regulation Authority, Quarterly ADI Performance Statistics "Eligible Tier 1 Capital" (Basel II) or "Total Tier 1 Capital" (Basel III) divided by "Total Assets", Series for Major banks (sheet 4b and 4c) + Other domestic banks (sheet 5b and 5c), December values. Resulting capital ratio multiplied with Total Assets series to compute Capital.
- *Note:* Gap 1946–1950 as printed.

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 30, 31

- *Note:* Built from Deposits and Loans components documented below.

**Deposits (component of ltd/noncore; millions AUD)** — *component* — pp. 30

- 1870–1945 — Butlin, Hall and White, Australian banking and monetary statistics, 1817-1945, Reserve Bank of Australia (1971), Part B, Table 1 Aggregate Trading Banks, Series "Total Deposits" + Table 53 (i) Aggregate Saving Banks, Series "Deposits". Levels.
- 1950–1996 — Reserve Bank of Australia, Discontinued Data, "Table 3.1", Series "Total Bank Deposits". Chainlinked.
- 1997–2012 — Reserve Bank of Australia, Statistical Tables, Discontinued Data, Table "Banks – On-balance Sheet Assets, Liabilities and Off-balance Sheet Business – B2", Series Resident Liabilities Deposits, http://www.rba.gov.au/statistics/tables/. Levels.
- 2013–2017 — Reserve Bank of Australia, Statistical Tables, Table D3 Monetary Aggregates, "Current deposits with banks + Certificates of deposit issued by banks + Term deposits with banks + Other deposits with banks + Deposits with non-bank ADIs" (DMACDB+ DMAODCD+ DMAODTEC+ DMAODO+ DMADNA), http://www.rba.gov.au/statistics/tables/. Chainlinked.
- 2018–2020 — Reserve Bank of Australia, Statistical Tables, Table D3 Monetary Aggregates, "Transaction Deposits with ADIs + Certificates of deposit issued by ADIs + Non-Transaction Deposits with ADIs" (DMATD+ DMAODCD+ DMANTD), http://www.rba.gov.au/statistics/tables/. Chainlinked.

**Loans (component of ltd; millions AUD)** — *component* — pp. 30, 31

- 1870–1945 — Butlin, Hall and White, Australian banking and monetary statistics, 1817-1945, Reserve Bank of Australia (1971), Part B, Table 1 Aggregate Trading Banks, Series "Advances and other assets" + Table 53 (i) Aggregate Saving Banks, Series "Mortgage Loans". June or December values depending on availability, levels.
- 1950–1974 — Reserve Bank of Australia, Discontinued Data, "Table 3.8" Trading Banks: Deposit Liabilities and Selected Assets (a), Series "Loans, Advances and bills discounted" + Reserve Bank of Australia, Discontinued Data, "Table 3.9" Saving Banks; series "Loans, Advances and bills discounted – Total (estimated based on growth rate of other asset items between 1950 and 1955)", chainlinked.
- 1975–1996 — Reserve Bank of Australia, Discontinued Data, "Table 3.7a", accessible online (http://www.rba.gov.au/statistics/discontinued-data.html), chainlinked.
- 1997–2012 — Reserve Bank of Australia, Statistical Tables, Discontinued Data, Table "Banks – On-balance Sheet Assets, Liabilities and Off-balance Sheet Business – B2", assetsb02, Loans and advances, series "Residential"+"Personal"+"Commercial", levels.
- 2013–2020 — Reserve Bank of Australia, Statistical Tables, Table D2 Lending and credit Aggregates, "Loans and advances; AFIs – Excludes securitisations – For series breaks see Series Breaks", http://www.rba.gov.au/statistics/tables/, chainlinked.

**Noncore ratio = (Total Assets – Capital - Deposits) / (Total Assets - Capital)** — `noncore` — pp. 31

- *Note:* Formula only; computed from the Total Assets, Capital and Deposits components above.

### Belgium (BEL) — "Data in millions BEF" — PDF pp. 31–42

**Population** — `pop` — pp. 31, 32

- 1870–1952 — Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls).
- 1953–2011 — Bank of Belgium (2012). Table "Total population (thousands, end of year)", Series "Total" (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- 2012–2017 — growth rates from International Monetary Fund (Aug 2019), World Economic Outlook. Subject "People – population" (base year: 2011) (accessible at www.imf.org).
- 2018–2020 — growth rates from International Monetary Fund (Oct 2021), World Economic Outlook. Subject "People – population" (base year: 2011) (accessible at www.imf.org).

**GDP (converted to millions BEF)** — `gdp` — pp. 32

- 1870–1952 — Groningen Growth and Development Centre (2009), Historical National Accounts Database, University of Groningen, Groningen. Table "Belgium, value added at market prices in current price", Series "Total GDP" (accessible online at http://www.ggdc.nl/databases/hna/2009/data/hna_bel_09.xls). Gaps: 1914-1919 & 1940-1947.
- 1914–1919 & 1940–1947 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1953–2020 — International Financial Statistics. Data Report "Economic indicators", Series "Gross domestic product (in millions) – GDP nominal" (accessible online at http://data.imf.org/).

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 32

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 32

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (code: CPCINXBE) (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator/NY.GDP.PCAP.KD).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 32

- 1913–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data–sets/.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.
- *Note:* Series starts only in 1913 for Belgium.

**Investment-to-GDP ratio** — `iy` — pp. 32, 33

- 1900–1913 — calculated from van Meerten, Michelangelo (2003), Capital Formation in Belgium 1900–1990, Leuven University Press. Series "Gross Fixed Asset Formation" (private sector, incl. dwellings) (p.383) Table: Annex C.1. Column 22, and series "Value of the Physical Change in Stocks" (private sector) Table: Annex E.1. Column 20, divided by nominal GDP series from JST dataset.
- 1920–1952 — van Meerten, Michelangelo (2003), ibid. Series "Investment ratio" (note: no data for 1940, 1942, 1944, and 1945).
- 1953–2014 — International Monetary Fund (2015), International Financial Statistics. Data Report "Economic indicators", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- Formerly 1953–1979 — National Bank of Belgium (2012), Belgostat. Table "Comptabilité nationale, système traditionnel – Revenu national et dépenses de la nation (estimations à prix courants)", closed series "National Accounts, Système traditionnel – source INS (1953–1991), Estimations à Prix Courants, Comptabilité Nationale, Optique Répartition, Comptes Nationaux, Compte 1–Revenu national et dépenses de la nation"; calculation: [Gross fixed capital formation (total) + Change in inventories] / NGDP (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- 1980–2020 — National Bank of Belgium, Belgostat. Table "Main categories of expenditure, estimates at current prices", closed series "National Accounts, Quarterly Data and Annual Accounts, ESA95, Gross Data, GDP Identity from the Expenditure Side, Main Categories of Expenditures, Current Prices"; Calculation: [Gross fixed capital formation (total) + Change in inventories] / NGDP (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- *Note:* Starts 1900; no data 1914–1919 and 1940, 1942, 1944, 1945. The text lists both "1953–2014 IFS" and "1980–2020 NBB" entries (overlapping 1980–2014) with the NBB 1953–1979 entry marked "Formerly"; the document does not say which source wins in the overlap.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 33

- 1870–2007 — National Bank of Belgium Services Statistiques Financières et Économiques (2012), Table "Indice des prix à la Consommation en Belgique", received from Daisy Dillens (National Bank of Belgium). (Note: gaps for 1915-1919; 1940–1945)
- 1915–1919 and 1940–1945 — Jan Annaert, Frans Buelens, Ludo Cuyvers, Marc De Ceuster, Marc Deloof and Ann De Schepper (2011). Are blue chip stock market indices good proxies for all-shares market indices? The case of the Brussels Stock Exchange 1833–2005. Financial History Review, 18, pp. 277-308 doi:10.1017/S0968565011000187. Implicit CPI calculated from nominal and real all shares indices from Table 1: All shares index, Capital gain (CG). Chainlinked.
- 2008–2020 — International Monetary Fund World Economic Outlook (April 2019). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.
- *Note:* Wartime CPI (1915–1919, 1940–1945) is an implicit deflator backed out of nominal vs real stock indices, not a true consumer price survey.

**Narrow Money (converted to millions BEF)** — `narrowm` — pp. 33, 34

- 1877–1940 — Delbeke, Jos (1988), Geld en bankkrediet in België, 1877–1983, AWLSK, Brussels. Table 1.3. (Note: no data for 1914–1919)
- 1947–1978 — growth rate calculated from Delbeke, Jos (1988), ibid. Table 1.2.
- 1979–1995 — growth rate calculated from National Bank of Belgium (2012), Belgostat. Table "Monetary aggregates (millions of Euros 1979–1998)", series M1 (see Data Source folder for excel file).
- 1996–2001 — National Bank of Belgium (2012), Belgostat. Table "Belgian contribution to the monetary aggregates of the Eurozone (until December 2001)", Series "Overnight deposits" (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- 2002–2020 — National Bank of Belgium (2021), Belgostat. Table "other financial statistics, Monetary aggregates, M1, overnight deposits (belgian contribution to monetary aggregates of the euro area)".
- *Note:* Starts 1877; gaps 1914–1919 and 1941–1946 as printed.

**Broad Money (converted to millions BEF)** — `money` — pp. 34

- 1979–1995 — National Bank of Belgium (2012), Belgostat Online. Table "Monetary aggregates (1979–1998)", Series "M3" (Series "M1" + Series "Other assets at up to one year with credit institutions") (see Data Source folder for excel file).
- 1996–2001 — National Bank of Belgium (2012), Belgostat Online. Table "Belgian contribution to the monetary aggregates of the Eurozone (until December 2001)" (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- 2002–2020 — National Bank of Belgium (2019), Belgostat. Table "other financial statistics, Monetary aggregates, M3 excluding currency in circulation (belgian contribution to monetary aggregates of the euro area)."
- *Note:* Broad money for Belgium starts only in 1979 as documented.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 34

- 1870–1912 — series from J.M. Drappier publication received from Willy Biesemann (Data shop, National Bank of Belgium) (2012). The short-term interest rate is defined as the discount rate of Société Générale up to 1850, discount rate of the National Bank from 1851 to 1964, and the interest rate on three-month Treasury certificates after that.
- 1913–1914 — Neal, Larry D., and Marc D. Weidenmier. "Crises in the global economy from tulips to today." Globalization in historical perspective. University Of Chicago Press, 2003. 473-514. Open Market Rate, Monthly, End of Year Value (accessible online at http://ebutts05.tripod.com/nealweidenmiergsd/).
- 1920–2014 — series from J.M. Drappier publication received from Willy Biesemann (Data shop, National Bank of Belgium) (2012); same definition (National Bank discount rate 1851–1964, three-month Treasury certificate rate after that). (Note: no data for 1915–1919)
- 1991–2020 — Belgostat, Financial markets - Interest rates – Treasury certificates – 3 months – annual frequency (https://stat.nbb.be/Index.aspx).
- *Note:* As printed, the Drappier (1920–2014) and Belgostat (1991–2020) entries overlap for 1991–2014.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 34, 35

- 1870–1985 — series from J.M. Drappier publication received from Willy Biesemann (Data shop, National Bank of Belgium) (2012). The long-term interest rate is defined as the yield rate of the active debt (perpetual-maturity government bond) of 2.5 p.c. until 1912, and the yield on the government debt at six years and over from 1920 onwards. (Note: no data for 1913–1919)
- 1986–2016 — International Monetary Fund (2019). International financial statistics. Interest Rates, Government bond yield. 10-year government bond yield.
- 2017–2020 — OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en, average of monthly values.

**Current Account (converted to millions BEF)** — `ca` — pp. 35

- 1870–1946, 1949, 1952 & 1953 — B. Mitchell (1980), European Historical Statistics 1750–1975 (second revised edition), Facts on File, New York. Table F1 "External trade aggregate current value", p507. The current account balance is set equal to the trade balance for all of the above values (see Import & Export for respective years). (Note: no data for 1914–1918)
- 1947–1979 — National Bank of Belgium (various), Annual Reports (various issues), Series relating to total balance of payments – name may vary between reports (accessible online at http://www.nbb.be/pub/06_00_00_00_00/06_02_00_00_00/06_02_06_00_00.htm?l=en).
- 1980–1996 — International Monetary Fund (2015), World Economic Outlook Database April 2012. Series "Balance of payments: Current account balance % of GDP, multiplied with GDP from JST dataset" (accessible online at http://www.imf.org/external/pubs/ft/weo/2012/01/weodata/index.aspx).
- 1997–2020 — National Bank of Belgium, Belgostat Online. Table "Balance of payments: Current account of Belgium: detailed presentation – net", Series "Total of the current account" (accessible online at http://www.nbb.be/pub/stats/stats.htm?l=en&tab=Figures).
- *Note:* Pre-1947 (and 1949, 1952, 1953) "current account" is actually the merchandise trade balance.

**Import & Export (converted to millions BEF)** — `imports,exports` — pp. 35

- 1870–1913, 1919–1939 & 1946–1949 — Horlings (2002), "The International Trade of a Small and Open Economy. Revised Estimates of the Imports and Exports of Belgium, 1835-1990", NEHA-Jaarboek 65, 110-142.
- 1950–1997 — International Monetary Fund, International Financial Statistics. Series "Goods, values of imports" and Series "Goods, values of exports" for Belgium & Luxembourg (accessible online at http://data.imf.org/).
- 1998–2020 — International Monetary Fund, International Financial Statistics. Archive, 2021 M10, External trade, imports, goods, value, cost, insurance freight, Domestic Currency; External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency (accessible online at https://data.imf.org/).
- *Note:* 1950–1997 figures cover the Belgium–Luxembourg Economic Union, not Belgium alone. Gaps 1914–1918 and 1940–1945.

**Government Revenues (converted to millions BEF)** — `revenue` — pp. 35

- 1870–1982 — B. Mitchell (1980), ibid. Table H5 "Government revenue and main tax yield", p. 745. Level. (Note: no data for 1913-1919).
- 1983–1984 — geometric interpolation.
- 1985–2009 — OECD Statistics. Annual national accounts SNA93. General Government accounts SNA93. Table 12: Government deficit/surplus, revenue, expenditure and main aggregates - Total government revenue (accessible online at http://stats.oecd.org). Level.
- 2010–2020 — OECD Statistics. Annual national accounts. General Government accounts. Table 12: Government deficit/surplus, revenue, expenditure and main aggregates. Level.
- *Note:* Pre-1985 figures are central government (Mitchell); from 1985 general government (OECD).

**Government Expenditure (converted to millions BEF)** — `expenditure` — pp. 36

- 1870–1985 — B. Mitchell (1980), ibid. Table H4 "Total central government expenditure (in millions)", p. 734 (Note: no data available for 1940). Level. (Note: no data for 1913-1919).
- 1986–2020 — OECD Statistics. Annual national accounts SNA93. General Government accounts SNA93. Table 12: Government deficit/surplus, revenue, expenditure and main aggregates - Total government expenditure (accessible online at http://stats.oecd.org). Level.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 36

- 1870–1913 — Belgostat, 2012, "Official debt and net financial balance of the Treasury, total" (series sent by email, contact person is Willy Biesemann). Note: The data series provided stated only a debt-to-GDP ratio; this ratio has been multiplied with the nominal GDP series of this dataset to yield a value for the nominal public debt series.
- 1920–1968 — Belgostat, 2012, "Official debt and net financial balance of the Treasury, total" (series sent by email, contact person is Willy Biesemann). Note: The original data series expressed a debt-to-GDP ratio only; this ratio has been multiplied with the nominal GDP series of this dataset to yield a value for the nominal public debt series. (Note: no data for 1940–1945)
- 1969–2020 — European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt. 18.2 – Based on ESA 2010 and former definitions. Gross Public Debt (linked series) (UDGGL). Percentage of GDP at market prices (excessive deficit procedure) (data accessible online at http://ec.europa.eu/economy_finance/ameco/user/serie/SelectSerie.cfm).

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 36

- 1870–1880 — Denzel M. A. & Schwarzer, O. (1991). Währungen der Welt I. Europäische und Nordamerikanische Devisenkurse, 1777-1914. Teilband II. P.237: Belgische Bankplätze, lange Sicht. Old franc/100 belgian francs*100*New French Franc / US Dollar.
- 1881–1919 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1920–1939 — Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015. http://www.measuringworth.com/exchangeglobal/
- 1940–1945 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1946–1953 — Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1954–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- *Note:* "We assume a Belgian franc-euro exchange rate of 40.3399 where necessary." 1946–1953 values are black-market rates.

**Peg dummy** — `peg` — pp. 37

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 37

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold? Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 37

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 37

- 1878–1913 & 1919–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012 (1990=100). Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.
- *Note:* Starts 1878; gap 1914–1918.

**Unemployment rate (percent)** — `unemp` — pp. 37, 38

- 1921–1938 and 1950–1978 — Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press. Chainlinked.
- 1939 and 1945–1949 — Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter International Comparison of Unemployment Rates, Table 1 "Unemployment Rates, Nine Countries, 1900-1950 (per cent)". Chainlinked.
- 1979–1982 — Mitchell, Brian (2013), International Historical Statistics Europe, 1750–2010, Table B2 Europe Unemployment, Palgrave Macmillan, London. Chainlinked.
- 1983–2020 — ILOSTAT (2020), Table "Unemployment rate by sex and age" based on the EU Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/.
- *Note:* Starts 1921; gap 1940–1944.

**Wages (index, 1990=100)** — `wage` — pp. 38

- 1870–1912 — International Historical Statistics. Europe Labour force – Money/Wages in industry. Average wages in 5 industries. Chainlinked.
- 1913–1919 — Scholliers & Zamagni (1995) "Labour's Reward: Real wages and economic change in 19th- and 20th-century Europe". Average annual wages in the mining sector. Chainlinked.
- 1920–1937 — International Historical Statistics. Europe Labour force – Money/Wages in industry. Daily wages of males in industry and transport. Chainlinked.
- 1938–1941 and 1947 — Monthly Bulletin of Statistics (United Nations) January 1951. Hourly nominal earnings (including construction and transportation). Chainlinked.
- 1948–1989 — International Monetary Fund International Financial Statistics database (IFS). Labor Markets, Wage Rates, Index. Accessible online at http://data.imf.org/. Chainlinked.
- 1990–2020 — OECD. OECD statistics. Average annual wages. Current prices. Levels. Accessible online at http://stats.oecd.org/.
- *Note:* Gap 1942–1946 as printed; concepts switch between average annual, daily, hourly and annual wages across splices.

**Total loans to non-financial private sector (Credit Data, converted to millions BEF)** — `tloans` — pp. 38, 39

- 1885–1911 — growth rate calculated from Institut National de Statistique et Ministère des Affaires Économique (various), Annuaire Statistique de la Belgique (various issues). Table "Bilan d'Unions de Credit", series "Loans (current accounts + portfolio)."
- 1912–1913 — National Bank of Belgium (1931), Revue Économique Bulletin (1931.09.25). Table "Situation des établissements de credit belges au 31 décembre de chaque année", Series "Comptes courants débiteurs" + series "Immeuble mobilier etc" (accessible online at http://www.nbb.be/pub/06_00_00_00_00/06_03_00_00_00/06_03_03_00_00/economic_review_archive.htm?l=fr).
- 1920–1933 — Statistisches Reichsamt of Germany (1936), "Statistisches Handbuch der Weltwirtschaft," Berlin: Verein für Socialpolitik, Wirtschaft und Statistik.
- 1934–1937 — growth rate calculated from National Bank of Belgium (1939), Revue Économique (1939.01.01). Table "Situation trimestrielles des banques belges – Situations globales des banques, comptes courants débiteurs", Series "Comptes courants débiteurs" (accessible online at see above).
- 1938–1940 — growth rate calculated from National Bank of Belgium (various), Revue Économique (various). Columns "Reports et avances sur titres + débiteurs par acceptations + débiteurs divers" (accessible online at see above).
- 1950–1960 — growth rate calculated from Total Financial Assets.
- 1961–1979 — National Bank of Belgium (various), Revue Économique (various issues). Table 12 "Créances de dettes dans l'économie belge – 1b Encours des créances et des dettes". Series "Intermédiaires financiers: Organisms monétaires + caisses d'épargne + sociétés hypothécaires et de capitalization + organisms d'assurance vie et accidents de travail, fonds de pension" (accessible online at http://www.nbb.be/pub/06_00_00_00_00/06_03_00_00_00/06_03_03_00_00/economic_review_archive.htm?l=fr).
- 1980–1991 — National Bank of Belgium (2012), Bank Lending to non–financial sector. Series "Lending to households and non–financial corporations" (note: series sent by email, contact person Viviane De Pré, NBB, data shop).
- 1992–1996 — International Monetary Fund (2012), International Financial Statistics. Data "Total claims on private sector" (accessible online at https://data.imf.org/).
- 1997–2020 — sum of Total Loans to Households and Total Loans to Business.
- *Note:* Starts 1885; gaps 1914–1919 and 1941–1949. Early segments are growth-rate splices from narrow institutional coverage (credit unions, bank current-account debtors); 1961–1979 covers a broad set of financial intermediaries (monetary institutions, savings banks, mortgage and capitalisation companies, life/accident insurers, pension funds).

**Mortgage loans to non-financial private sector** — `tmort` — pp. 39

- 1885–1913 — Fritz Schultze (1918), Die Belgischen Bodenkreditinstitute, Duncker & Humblot, Leipzig/München. Series "Hypotheken".
- 1920–1939 — Peters, Stef; Goosens, Martine, & Buyst, Erik (2005), Belgian National Income During the Interwar Period, Leuven University Press. Reconstruction of the Database. Table 67, column 3 "Outstanding mortgage debt with private individuals".
- 1950 — National Bank of Belgium (1960), Monthly Bulletin (1960.10.01). Table "Evolution de la dette hypothécaire par catégorie de créanciers", p240, Series "Total" (accessible online at http://www.nbb.be/doc/ts/publications/economicreview/1960/1960.10.01–BULL.pdf). Chain-linked.
- 1951–1959 — growth rate calculated from Institut National de Statistique et Ministère des Affaires Économique (1971), ibid. Table "Dette hypothécaire", series "Total", p447.
- 1960–2002 — National Bank of Belgium (2012), data shop, contact person: Viviane de Pré. Series "Evolution de la Dette Hypothécaire par Créanciers". (According to de Pré this series is no longer available)
- 2003–2020 — National Bank of Belgium, Belgostat. Financial account of Belgium, Table "Financial assets and liabilities of individuals and non-financial corporations", Account: financial wealth, Institutional sector: Individuals, Financial Instrument: Mortgage loans (accessible online at https://stat.nbb.be/Index.aspx).
- *Note:* Gaps 1914–1919 and 1940–1949. From 2003 the series covers mortgage loans of individuals (households) only.

**Total Loans to Households** — `thh` — pp. 39, 40

- 1950–1991 — growth rate calculated from Mortgage loans to non-financial private sector.
- 1992–1997 — National Bank of Belgium (2012), Belgostat. Table "Financial liabilities of individuals", series "Loans at over one year – Total" (accessible online at http://www.nbb.be/belgostat/).
- 1998–2020 — National Bank of Belgium, Belgostat. Financial account of Belgium, Table "Financial liabilities of individuals and non-financial cooperations", Account: Financial wealth, Institutional sector: Individuals, Frequency: Annual, Financial Instrument: Financial liabilities, Long-term loans (accessible online at //www.nbb.be/belgostat/PublicatieSelectieLinker?LinkID=788000082|910000082&Lang=E).
- *Note:* Starts 1950; 1950–1991 is extrapolated backward from mortgage-loan growth rates; 1992 onward covers long-term (over one year) loans only.

**Total Loans to Business** — `tbus` — pp. 40

- 1950–1996 — residual of Total loans to non-financial private sector and Total Loans to Households.
- 1997–2020 — National Bank of Belgium, Belgostat. Financial account of Belgium, Table "Financial liabilities of individuals and non-financial cooperations", Account: Financial wealth, Institutional sector: non-financial cooperations, Frequency: Annual, sum of series "short term loans – Bank loans" and "Long term loans – Bank loans" http://www.nbb.be/belgostat/PublicatieSelectieLinker?LinkID=788000084|910000082&Lang=E (note: 1997 corrected for break in data series) (accessible online at http://www.nbb.be/belgostat/).

**Corporate Debt** — `bdebt` — pp. 40

- 1950–1979 — residual of total loans to non-financial private sector and total loans to households (both from JST MacroHistory Database).
- 1980–1993 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- 1994–2013 — OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2020 — eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.

**Capital ratio = Capital / Total assets (Bank balance sheet ratios; ratios in %, underlying data in millions BEF)** — `lev` — pp. 40, 41

- *Note:* Built from Total assets and Capital components below.

**Total assets (component of lev/ltd/noncore; converted to millions BEF)** — *component* — pp. 40, 41

- 1920–1932 — Banque Nationale Belge, Economic Bulletins, issue (1933-09-25), Table "Situation des etablissements de credit belges". Series: "Total de l'Actif". Levels.
- 1933 — Banque Nationale Belge, Statistiques Economique Belge (issue 1929-1940), Table "Situation des etablissements de credit belges". Series: "Total de l'Actif". Levels.
- 1935–1991 — Banque Nationale Belge, Statistiques Economiques Belge (issues 1929-1940, 1940-1950, 1950-1960, 1960-1970, 1970-1980, 1980-1990) Table "Situation globale des banques" - "Total actif". Chainlinked.
- 1992–2020 — NBB online statistics; Major credit institutions governed by Belgian law; December values. Series "Total Assets", http://stat.nbb.be/Index.aspx?DataSetCode=CREDINSCORP#. Levels.
- *Note:* Bank balance-sheet data for Belgium start only in 1920; 1934 missing as printed.

**Capital (component of lev; converted to millions BEF)** — *component* — pp. 41

- 1920–1932 — Banque Nationale Belge, Economic Bulletins, issue (1933-09-25), Table "Situation des etablissements de credit belges". Series: "Capital verse"+"Reserves". Chainlinked capital ratio.
- 1933 — Banque Nationale Belge, Statistiques Economique Belge (issue 1929-1940), Table "Situation des etablissements de credit belges". Series: "Capital-actions verse"+"Reserves diverses".
- 1935–1991 — Banque Nationale Belge, Statistiques Economiques Belge (issues 1929-1940, 1940-1950, 1950-1960, 1960-1970, 1970-1980, 1980-1990) Table "Situation globale des banques" – "Total passive non-exigible". Chainlinked capital ratio.
- 1992–2020 — NBB online statistics; Credit institutions on a corporate basis; Major credit institutions governed by Belgian law; December values. Series "Own ressources", http://stat.nbb.be/Index.aspx?DataSetCode=CREDINSCORP#. Levels.

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 41, 42

- *Note:* Built from Deposits and Loans components below.

**Deposits (component of ltd/noncore; converted to millions BEF)** — *component* — pp. 41

- 1920–1932 — Economic Bulletins, BNB, issue (1933-09-25), Table "Situation des etablissements de credit belges". Series: "Engagements immediates ou indetermines".
- 1933 — Banque Nationale Belge, Statistiques Economique Belge (issue 1929-1940), Table "Situation des etablissements de credit belges". Series: "Engagements immediates ou indetermines".
- 1935–1991 — Banque Nationale Belge, Statistiques Economiques Belge (issues 1929-1940, 1940-1950, 1950-1960, 1960-1970, 1970-1980, 1980-1990) Table "Situation globale des banques" – "Depots et comptes courants" as sum of "Depots et comptes courants a vue et a moins de 30 jours" and "Depots et comptes courants a plus de 30 jours". Chainlinked as share in total debt.
- 1992–2020 — NBB online statistics; Credit institutions on a corporate basis; Major credit institutions governed by Belgian law; December values. Series "Deposits". Levels.

**Loans (component of ltd; converted to millions BEF)** — *component* — pp. 41, 42

- 1920–1932 — based on Economic Bulletins, BNB, issue (1933-09-25), Table "Situation des etablissements de credit belges". Series: "Comptes courants debiteurs"+"Prets"+"Immeubles, mobilier, etc."+"Portefeuille Effets de Commerce".
- 1933 — based on Banque Nationale Belge, Statistiques Economique Belge 10 years, Table "Situation des etablissements de credit belges". Series: "Comptes courants debiteurs"+"Prets"+"Immeubles, mobilier, etc."+"Portefeuille Effets de Commerce".
- 1935–1991 — Banque Nationale Belge, Statistiques Economiques Belge (issues 1929-1940, 1940-1950, 1950-1960, 1960-1970, 1970-1980, 1980-1990) - Table "Situation globale des banques" – sum of "Portefeuille Effets Commerciaux" (1935–1941; chainlinked with Total Portefeuille Effets) + "Comptes courants debiteurs" + "Reports et avances sur titres" + "Debiteurs par acceptations" + "Debiteurs divers".
- 1992–2020 — NBB online statistics; Credit institutions on a corporate basis; Major credit institutions governed by Belgian law; December values. Series "Claims on clients", http://stat.nbb.be/Index.aspx?DataSetCode=CREDINSCORP#. Levels.

**Noncore ratio = (Total Assets - Capital - Deposits) / (Total Assets - Capital)** — `noncore` — pp. 42

- *Note:* Formula only.

### Canada (CAN) — "Data in billions CAD" — PDF pp. 42–53

**Population** — `pop` — pp. 42

- 1870–2008 — Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls).
- 2009–2016 — growth rates from International Monetary Fund (Aug, 2019), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).
- 2017–2020 — growth rates from International Monetary Fund (Oct, 2021), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).

**GDP (billions CAD)** — `gdp` — pp. 42, 43

- 1870–1947 — Mark Dincecco and Mauricio Prado (2013), "Nominal GDP Series, 1870-2000". Online: http://gpih.ucdavis.edu/GDP.htm. Levels.
- 1948–2020 — International Monetary Fund (2021), International Financial Statistics. Series "Gross domestic product" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx).

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 43

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 43

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator/NY.GDP.PCAP.KD).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 43

- 1871–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data–sets/.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.
- *Note:* Starts 1871.

**Investment-to-GDP ratio** — `iy` — pp. 43

- 1871–1945 — Mitchell, Brian (2007) International Historical Statistics: The Americas 1750–2005, Palgrave Macmillan, London.
- 1946–1947 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1948–2020 — Post–WWII data from International Monetary Fund, International Financial Statistics. Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- *Note:* The 1946–1947 citation (van Meerten, Capital formation in Belgium) appears to be a copy-paste error in the document for a Canadian series; starts 1871.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 43

- 1870–1996 — A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
- 1997–2020 — International Monetary Fund World Economic Outlook (April 2021). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.

**Narrow Money (billions CAD)** — `narrowm` — pp. 44

- 1871–1948 — Metcalf et al. 1996 "New estimates of the Canadian money stock: 1871-1967." Discussion paper No.: 96-17. Series M1. Year average of monthly data. Level.
- 1949–2004 — Mitchell, B. (2013). International Historical Statistics. Series: M1. Level.
- 2005–2020 — Bank of Canada, Series: Selected monetary aggregates and their components (formerly E1), M1+ (gross) (Seasonally adjusted), Dec values.
- *Note:* Starts 1871; concept shifts from year-average M1 to December M1+ (gross) in 2005.

**Broad Money (billions CAD)** — `money` — pp. 44

- 1871–1879 — Metcalf et al. 1996 "New estimates of the Canadian money stock: 1871-1967." Discussion paper No.: 96-17. Series M2. Year average of monthly data. Level.
- 1880–1967 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75. Series "monagglc" = M2 according to documentation. Level.
- 1968–2001 — International Monetary Fund, eLibrary. International Financial Statistics, series M2, Alternate Definition 2, National Currency.
- 2002–2020 — Bank of Canada, Series: Selected Monetary Aggregates and their components (formerly E1), M2+ (gross) (Unadjusted), Dec values.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 44

- 1934–1947 — Statistics Canada. Historical Statistics of Canada. Table J471-480. Series: 3-month treasury bill yield. Average annual rate.
- 1948–2016 — International Monetary Fund (2019), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – treasury bill rate" (accessible online at https://data.imf.org/).
- 2017–2020 — Bank of Canada, Treasury bill auction - average yields - 3 month – average.
- *Note:* Documented Canadian short-term rate starts only in 1934.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 44, 45

- 1870–1873 — Investor's Monthly Manual. Current yield of Canadian Dominion 5% bond. Final redemption: 1885. December values.
- 1874–1895 — sum of "Yield on consols" (from Bank of England, Three centuries of macroeconomic data, Series: Yield on consols) and "Spread on consols" (from Clemens, M. A. and Williamson, J. G. (2004). Wealth bias in the first global capital market boom, 1870–1913. The Economic Journal.)
- 1896–1939 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1940–1947 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance.
- 1948–2016 — International Monetary Fund (2019), International Financial Statistics (IFS). Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds, percent per Anum".
- 2017–2020 — Bank of Canada, average of: Government of Canada marketable bonds - average yield - over 10 years.

**Current Account (billions CAD)** — `ca` — pp. 45

- 1870–1945 — M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA (accessible online at http://www.nber.org/databases/jones–obstfeld/).
- 1948–2020 — International Monetary Fund (2020), International Financial Statistics. Supplementary Items, Current Account, Net (excluding exceptional financing), US Dollars (accessible online https://data.imf.org).
- *Note:* Gap 1946–1947; the 1948–2020 IFS source is in US dollars (conversion to CAD is implied but not described).

**Imports & Exports (billions CAD)** — `imports,exports` — pp. 45

- 1870–1947 — B. Mitchell (2007), International Historical Statistics: The Americas 1750–2005, Palgrave Macmillan, London.
- 1948–2020 — International Monetary Fund, International Financial Statistics: Archive, 2021 M10, External trade, imports, goods, value, cost, insurance freight, Domestic Currency; External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency (accessible online at https://data.imf.org/).

**Government Revenues (billions CAD)** — `revenue` — pp. 45

- 1870–1962 — Statistics Canada (various), Canada Statistical Yearbook (various issues) (accessible online at http://www66.statcan.gc.ca/acyb_000–eng.htm).
- 1963–1980 — Mitchell, B. (2013). International Historical Statistics. Revenues - Total. Level.
- 1981–2020 — OECD, OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "National currency, current prices," Series GTR "Total general government revenue" (accessible online at http://www.oecd–ilibrary.org/statistics). Level.
- *Note:* Central government throughout (OECD sector GS1311 = central government).

**Government Expenditure (billions CAD)** — `expenditure` — pp. 45, 46

- 1870–1959 — Statistics Canada (various), Canada Statistical Yearbook (various issues) (accessible online at http://www66.statcan.gc.ca/acyb_000–eng.htm).
- 1960–1980 — Mitchell, B. (2013). International Historical Statistics. Central Government Expenditure. Level.
- 1981–2020 — OECD (2021), OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "National currency, current prices," Series GTE "Total general government expenditure" (accessible online at http://www.oecd–ilibrary.org/statistics). Level.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 46

- 1870–2010 — Abbas, S.M. Ali, Nazim Belhocine, Asmaa El-Ganainy and Mark Horton (2010) "A Historical Public Debt Database", IMF Working Paper WP/10/245, Washington, DC.
- 2011–2020 — International Monetary Fund, World Economic Outlook Database, General Government Gross Debt, nominal (data accessible at http://www.imf.org/external/pubs/ft/weo/2013/01/weodata/weoselco.aspx?g=110&sg=All+countries+%2f+Advanced+economies). Divided by JST GDP after having updated.

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 46

- 1870–1899 — Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. Canadian Dollar / pound * pound / US Dollar (contained in this dataset).
- 1900–1908 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1909–1914 — Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. Canadian Dollar / pound * pound / US Dollar (contained in this dataset).
- 1915–1939 — Banking and Monetary Statistics, 1914-1941. International Financial Statistics. Table 173. https://fraser.stlouisfed.org/scribd/?toc_id=334474&filepath=/docs/publications/bms/1914-1941/BMS14-41_complete.pdf&start_page=555
- 1940–1941 — Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015. http://www.measuringworth.com/exchangeglobal/
- 1942–1946 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1947–1950 — Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1951–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy** — `peg` — pp. 46, 47

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 47

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 47

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 47

- 1921–1949 & 1956–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD Statistics. Prices and Purchasing Power Parities, House prices and related indicators, Analytical house price indicators, Nominal house price indices, s.a. Chain-linked.
- *Note:* Starts 1921; gap 1950–1955.

**Unemployment rate (percent)** — `unemp` — pp. 47

- 1916–1920 — Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter International Comparison of Unemployment Rates, Table 1 "Unemployment Rates, Nine Countries, 1900-1950 (per cent)". Chainlinked.
- 1921–1937 and 1955–1975 — Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press. Chainlinked.
- 1938–1954 — Mitchell, Brian (2013), International Historical Statistics Europe, 1750–2010, Table B2 Europe Unemployment, Palgrave Macmillan, London. Chainlinked.
- 1976–2020 — ILOSTAT (2020), Table "Unemployment rate by sex and age" based on the Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/.
- *Note:* Starts 1916. The 1938–1954 citation is to the "Europe" volume of Mitchell as printed.

**Wages (index, 1990=100)** — `wage` — pp. 48

- 1870–1900 — Williamson (1995) "The evolution of global labor markets since 1830 background evidence and hypotheses". Real wages inflated using consumer price index from A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150. Chainlinked.
- 1901–1971 — Meltz, N. M. (1983). Section E Wages and Working Conditions. Statistics Canada, Historical Statistics of Canada, 101-3. General index of average wage rates for selected main industries. Accessible online at https://www150.statcan.gc.ca/n1/pub/11-516-x/sectione/4147438-eng.htm#7. Chainlinked.
- 1972–1989 — International Monetary Fund International Financial Statistics database (IFS). Labor Markets, Manufacturing Wage Rates, Index. Accessible online at http://data.imf.org/. Chainlinked.
- 1990–2020 — OECD. OECD statistics. Average annual wages. Current prices. Levels. Accessible online at http://stats.oecd.org/.

**Total loans to non-financial private sector (Credit Data, billions CAD)** — `tloans` — pp. 48, 49

- 1870–1873 — M.C. Urquhart (1965), Historical Statistics of Canada, Cambridge UP, Toronto. Series H219, H220.
- 1874–1890 — Urquhart, ibid. Series H206, H208, H219, H220. and Statistics Canada (various), Canada Statistical Yearbooks (various). 1900: Series "Current loans secured on real estate", p348; 1903: Series "Loans secured by mortgage", p441.
- 1891–1899 — Urquhart, ibid. Series H191; and Statistics Canada (various), ibid. 1900: Series "Current loans secured on real estate", p348; 1903: Series "Loans secured by mortgage", p441.
- 1900–1913 — M.C. Urquhart (1965), ibid. Series H172; and Statistics Canada (various), ibid. 1903: p441 "Loans secured by mortgage"; 1908: p428 "Current loans secured on real estate"; 1913: p560 "Current loans secured on real estate"; 1914: p591 "Current loans secured on real estate".
- 1914–1960 — M.C. Urquhart (1965), ibid. Series H151, H127, H103, H74. and Statistics Canada (various), ibid. 1930: p870; 1936: p911; 1938: p922; 1941: p819; 1945: p1009, p1023, p1024; 1948: p1039; 1951: p1043; 1952–53: p1108; 1955: p1204; 1956: p1115; 1957–58: p1147.
- 1961–1989 — Statistics Canada. Table 378–0059 (terminated 2011) "Chartered banks and quasi–banks: Consumer credit, loans and mortgages".
- 1990–2010 — Statistics Canada. Table 378–0121; Chartered banks and quasi–banks – Loans – Sum of Consumer credit, non–mortgage loans and mortgages" (accessible online at http://www5.statcan.gc.ca/cansim/).
- 2011–2020 — Statistics Canada. Table: 36-10-0580-01 (formerly CANSIM 378-0121); Chartered banks and quasi–banks – Total assets - Loans – Sum of "Consumer credit", "Non–mortgage loans", and "Mortgages". Chain-Linked to the previous values (1990-2010). (accessible online at https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610058001)

**Mortgage loans to non-financial private sector** — `tmort` — pp. 49

- 1874–1914 — Canada Statistical Yearbooks. 1900: p348 "Current loans secured on real estate"; 1903: p441 "Loans secured by mortgage"; 1908: p428 "Current loans secured on real estate"; 1913: p560 "Current loans secured on real estate"; 1914: p591 "Current loans secured on real estate".
- 1915–1947 — Canada Statistical Yearbooks. 1930: p870 "Loan companies chartered by the dominion government, assets: Lent on mortgages and hypothèques"; 1936: p911; 1938: p922; 1941: p819; 1945: p1009, p1023 "Loan companies chartered by the dominion government, assets: Lent on mortgages and hypothèques", p1024; 1948: p. 1039; 1951: p1043; 1952–53: p1108; 1955: p1204; 1956: p1115; 1957–58: p. 1147.
- 1948–1953 — M.C. Urquhart (1965) ibid. Series H492; and Canada Statistical Yearbooks. 1930: p870; 1936: p911; 1938: p922; 1941: p819; 1945: p1009, p1023, p1024; 1948: p1039; 1951: p1043; 1952–53: p1108; 1955: p1204; 1956: p1115; 1957–58: p1147.
- 1954–1989 — Statistics Canada. Table 378–0059 (terminated 2011) "Chartered banks and quasi–Banks: Mortgages".
- 1990–2010 — Statistics Canada. Table 378–0121; Chartered banks and quasi–banks – Loans – Sum of Consumer credit, non–mortgage loans and mortgages". Jump in 2011 mortgages due to: "Over the course of 2011 data in this table were affected by conversion to International Financial Reporting Standards (IFRS)" further: "Under the outgoing CGAAP, through the process of securitization and due to the subsequent sale of the corresponding debt or ABS, the originators of ABS do not report the securitized receivables and the corresponding securities on their own balance sheets. Under the incoming IFRS, these ABS and receivables will now be reported on the balance sheets of the companies themselves, as the originators of the ABS. This is an important change in financial reporting. As mentioned, currently the transfers of receivables off balance sheet are reported as sale transactions, but this will not be the case under IFRS. The consolidation on the originators' balance sheets will be the biggest change with respect to the Financial Flow Accounts and the National Balance Sheet Accounts. It is important to note that at the economy–wide level, neither lending via credit markets nor credit market debt will change; only the sectoral composition or distribution of the credit market assets and liabilities will be affected."
- 2011–2020 — update 1990–2010 series with growth rate of: On–balance sheet mortgages and securitization: Loan mortgages + Debt Securities + Other Short Term Paper + Other Accounts Receivable (unaffected by IFRS changes in 2011) all from Statistics Canada. Table 378–0121; National balance sheet accounts.
- *Note:* Starts 1874. Known break: 2011 IFRS conversion brought securitized mortgages back onto bank balance sheets; JST avoids the jump by extending 1990–2010 with growth rates of an IFRS-unaffected aggregate.

**Total Other Loans (Canada; residual)** — *component* — pp. 49

- all — Residual of Total loans to non-financial private sector and Mortgage loans to non-financial private sector.

**Total Loans to Households** — `thh` — pp. 50

- all — Sum of Mortgage Loans to Households and Total Other Loans to Households.

**Mortgage Loans to Households (component of thh)** — *component* — pp. 50

- all — See Mortgage loans to non-financial private sector.

**Total Other Loans to Households (component of thh)** — *component* — pp. 50

- 1956–1960 — growth rate calculated from Statistics Canada (2012). Table 176–0027 "Consumer credit, outstanding balances of selected holders" (accessible online at http://www5.statcan.gc.ca/cansim/a01?lang=eng).
- 1961–1989 — Statistics Canada. Table 378–0059 (terminated 2011) "National balance sheet, total chartered banks and quasi–banks: Canada book value consumer credit (book value, as market value data goes only back to 1970, though both series are identical)".
- 1990–2020 — Statistics Canada. Table: 36-10-0580-01 (formerly CANSIM 378-0121); Chartered banks and quasi–banks – Loans – consumer credit".
- *Note:* Starts 1956, so thh for Canada starts 1956.

**Total Loans to Business** — `tbus` — pp. 50

- 1961–1989 — Statistics Canada, Table 378–0059 (terminated 2011) "Chartered banks and quasi–Banks: Loans" (accessible online at http://www5.statcan.gc.ca/cansim/pick–choisir?lang=eng&p2=33&id=3780059).
- 1990–2020 — Statistics Canada. Table: 36-10-0580-01 (formerly CANSIM 378-0121); Sector: Chartered banks and quasi–banks; Category: Total Financial assets: Loans – non–mortgage loans, q4 market values (accessible online at https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610058001).
- *Note:* Starts 1961.

**Corporate Debt** — `bdebt` — pp. 50

- 1880–1941 — lending of chartered banks recorded in Urquhart, M. C., and Buckley, K. A. H., Historical Statistics of Canada, "Banking and Finance," Series H87-179 and Canada Statistical Yearbooks (various).
- 1942–1960 — lending to non-financial corporate business from Karsten Müller (2018) "Credit Markets around the World, 1910–2014", from SSRN (accessible online at https://ssrn.com/abstract=3259636).
- 1961–1969 — total non-equity liabilities of the private non-financial business sector from Statistics Canada, Series J568-875, Table J596-607 (accessible online at https://www150.statcan.gc.ca/n1/pub/11-516-x/sectionj/4147440-eng.htm#6).
- 1970–2013 — OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2020 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- *Note:* Starts 1880.

**Capital ratio = Capital / Total Assets (Bank balance sheet ratios; ratios in %, underlying data in billions CAD)** — `lev` — pp. 51, 52

- *Note:* Built from Total Assets and Capital components below; chartered banks only.

**Total Assets (component of lev/ltd/noncore; billions CAD)** — *component* — pp. 51

- 1870–1882 — Urquhart, M.C. and Buckley K.A.H., Historical Statistics of Canada, Chartered Banks, Total Assets, series H225, Levels.
- 1883–1912 — Urquhart, M.C. and Buckley K.A.H., Historical Statistics of Canada, Chartered Banks, Total Liabilities, series H242. Levels.
- 1913–1922 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), available online (https://www150.statcan.gc.ca/n1/pub/11-516-x/sectionj/4147440-eng.htm#3 sheet), "Assets 1913-1922", series "Total Assets". Levels.
- 1923–1933 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1923-1933", series "Total Assets". Levels.
- 1934–1944 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1934-1944", series "Total Liabilities". Levels.
- 1945–1977 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1945-1977", series "Total Liabilities". Levels.
- 1978–2020 — Statistics Canada, CanSim, vector v36883, coordinate 1.1. "Chartered banks, assets and liabilities, at month-end, Bank of Canada", Total assets, Levels. December values. (For 2020 September value was used).

**Capital (component of lev; billions CAD)** — *component* — pp. 51, 52

- 1870–1882 — Urquhart, M.C. and Buckley K.A.H. Historical Statistics of Canada, Chartered Banks, difference between "Total Assets" (H225) and "Total Liabilities" (H242), Levels.
- 1883–1977 — Urquhart, M.C. and Buckley K.A.H. Historical Statistics of Canada, Chartered Banks, series H240, "Capital and Rest Fund". Levels.
- 1978–2020 — Statistics Canada, CanSim, "Chartered banks, assets and liabilities, at month-end, Bank of Canada", Canadian dollar shareholders' equity, vector v36970, coordinate 1.79. Levels. December values. (For 2020 September value was used)

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 52, 53

- *Note:* Built from Deposits and Loans components below.

**Deposits (component of ltd/noncore; billions CAD)** — *component* — pp. 52

- 1870–1977 — Urquhart, M.C. and Buckley K.A.H. Historical Statistics of Canada, Chartered Banks, Total Canadian Deposits, series H234. Levels.
- 1978–2020 — Statistics Canada, CanSim, "Chartered banks, assets and liabilities, at month-end, Bank of Canada", Canadian Dollar Total Deposits, vector v36939, coordinate 1.57. Levels. December values. (For 2020 September value was used)

**Loans (component of ltd; billions CAD)** — *component* — pp. 52, 53

- 1870–1912 — Urquhart, M.C. and Buckley K.A.H. Historical Statistics of Canada, Chartered Banks, series H221, "Total Loans", Levels.
- 1913–1922 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1913-1922", series H171, "Total Loans in Canada". Levels.
- 1923–1933 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1923-1933", series 147 "Total Loans in Canada". Levels.
- 1934–1944 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1934-1944", series 123 "Total Loans in Canada". Levels.
- 1945–1976 — Statistics Canada, Historical Statistics of Canada, Chartered Banking (Series J75-272), "Assets 1945-1977", series 94 "Total Loans". Levels.
- 1977–1980 — Statistics Canada, Table 176-0015 Chartered banks, Canadian dollar loans, general loans (personal and business loans). Chainlinked.
- 1981–2008 — Statistics Canada, Table 176-0015 Chartered banks, Loans in Canadian Dollar total, vector v36923. Levels.
- 2009–2020 — Statistics Canada, Table: 10-10-0110-01, "Chartered banks, assets and liabilities, at month-end, Bank of Canada", Canadian Dollar Total Loans, vector v53006714. Levels. December values. (For 2020 September value was used)

**Noncore ratio = (Total Assets - Capital - Deposits) / (Total Assets - Capital)** — `noncore` — pp. 53

- *Note:* Formula only.

### Denmark (DNK) — "Data in billions DKK" — PDF pp. 53–62

**Population** — `pop` — pp. 53

- 1870–2008 — Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.rug.nl/research/ggdc).
- 2009–2017 — growth rates from International Monetary Fund (Aug, 2019), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org/external).
- 2018–2020 — growth rates from International Monetary Fund (Oct, 2021), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org/external). [printed as "20018 – 2020", a typo]

**GDP (billions DKK)** — `gdp` — pp. 53

- 1870–1949 — Mitchell, Brian (1992), International Historical Statistics: Europe 1750–1988, Palgrave Macmillan, London.
- 1950–2002 — International Monetary Fund (2014), International Financial Statistics. Data Report "Economic indicators", Series "Gross domestic product (in billions) – GDP nominal" (accessible online at https://data.imf.org/).
- 2003–2020 — International Monetary Fund (2021), International Financial Statistics. Data Report "Economic indicators", Series "Gross domestic product (in millions) – GDP nominal" (accessible online at http://data.imf.org/).

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 53

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 54

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 54

- 1870–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.

**Investment-to-GDP ratio** — `iy` — pp. 54

- 1870–1951 — (WW1 gap) data from Mitchell, Brian (2013), International Historical Statistics: Europe 1750–2010, Palgrave Macmillan, London. (note: no data for 1915-1921).
- 1952–2020 — Post–WWII data from International Monetary Fund, International Financial Statistics. Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).

**Consumer prices (index, 1990=100)** — `cpi` — pp. 54

- 1870–1996 — A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
- 1997–2020 — International Monetary Fund World Economic Outlook (April 2021). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.

**Narrow Money (billions DKK)** — `narrowm` — pp. 54

- 1870–1945 — Hans Chr. Johansen, Dansk Historisk Statistik, tables 6.2, 6.6, 6.8 (available at http://www.dst.dk/da/Statistik/Publikationer).
- 1950–2012 — International Monetary Fund, International Financial Statistics, series M1 (Economic Concept View – Monetary Data (SRFs) – Monetary Aggregates).
- 2013–2020 — Danmarks Nationalbank, BANKING AND MORTGAGE LENDING, DNMNOGL: Key figures for MFI-sector by key figures and sector, Monetary aggregate M1 (DKK million).
- *Note:* Gap 1946–1949.

**Broad Money (billions DKK)** — `money` — pp. 54

- 1870–2020 — Abildgren, Kim. A Chart & Data Book on the Monetary and Financial History of Denmark, Working Paper, 30 May 2017. Series: Broad Money, M2. https://sites.google.com/view/kim-abildgren/historical-statistics

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 55

- 1875–2003 — Abildgren, K. (2005). A historical perspective on interest rates in Denmark 1875-2003. Money market rates.
- 2004–2020 — International Monetary Fund. International Financial Statistics. Interest Rates – Money Market Rates.
- *Note:* Starts 1875.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 55

- 1870–1874 — Danmarks Statistik, Publikationer, Kreditmarkedsstatistisk. Available at: http://www.dst.dk/da/Statistik/Publikationer
- 1875–1880 — Abildgren, K. (2005). A historical perspective on interest rates in Denmark 1875-2003. Government Bond Rates (long-term).
- 1880–1947 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1948–2020 — International Monetary Fund. International Financial Statistics. Monetary and Financial Accounts, Interest Rates, Securities Markets, Government Debt Securities, Government Bonds, Percent per Annum.

**Current Account (billions DKK)** — `ca` — pp. 55

- 1874–1914 — M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA (accessible online at http://www.nber.org/databases/jones–obstfeld/).
- 1921–1945 — M. Jones & M. Obstfeld (1997), same source.
- 1946–1974 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London.
- 1975–2007 — International Monetary Fund (2010), International Financial Statistics. Table "Balance of payments", Series "Balances – current account balance" (accessible online https://data.imf.org/).
- 2008–2020 — International Monetary Fund, World Economic Outlook. % of GDP * nominal GDP = Current Account (available at www.imf.org/external).
- *Note:* Starts 1874; gap 1915–1920.

**Imports & Exports (billions DKK)** — `imports,exports` — pp. 55

- 1870–1953 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London.
- 1948–2020 — International Monetary Fund, International Financial Statistics: archive, M10 2021, External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency; External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency.
- *Note:* Ranges overlap 1948–1953 as printed.

**Government Revenues (billions DKK)** — `revenue` — pp. 56

- 1870–1935 — H. Johansen (1985), Dansk økonomisk statistik 1814–1980, Gyldendal, Kopenhagen.
- 1954–1971 — H. Johansen (1985), ibid.
- 1972–1994 — Statistics Denmark (2012), Statbank. Subject "National accounts and government finances – Taxes & duties", Table SKAT "Taxation total, divided into rates and dues by type (1947–2011)", Type "Total taxes and duties" (accessible online at http://www.statbank.dk).
- 1995–2020 — OECD, OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "National currency, current prices," Series GTR "Total general government revenue" (accessible online at http://www.oecd–ilibrary.org/statistics). Level.
- *Note:* Gap 1936–1953 as printed; 1972–1994 is total taxes and duties rather than total revenue.

**Government Expenditure (billions DKK)** — `expenditure` — pp. 56

- 1870–1935 — H. Johansen (1985), Dansk økonomisk statistik 1814–1980, Gyldendal, Kopenhagen.
- 1937–1971 — P. Flora, 1983. State, Economy and society in Western Europe, 1815-1975. Denmark Public Expenditures, Central government.
- 1972–1994 — Statistics Denmark (2012), Statbank. Subject "National accounts and government finances – Taxes & duties", Table SKAT "Taxation total, divided into rates and dues by type (1947–2011)", Type "Total taxes and duties" (accessible online at http://www.statbank.dk). [as printed — the same tax table is cited for expenditure]
- 1995–2020 — OECD, OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "National currency, current prices," Series GTR "Total general government expenditure" (accessible online at http://www.oecd–ilibrary.org/statistics). Level.
- *Note:* 1936 missing as printed; the 1972–1994 entry cites a taxation table (probably a copy-paste error in the document).

**Public debt-to-GDP ratio** — `debtgdp` — pp. 56

- 1880–2009 — Abbas, S.M. Ali, Nazim Belhocine, Asmaa El-Ganainy and Mark Horton (2010) "A Historical Public Debt Database", IMF Working Paper WP/10/245, Washington, DC. (Note: no data for 1947-1952, 1957-1959, 1997).
- 2010–2020 — Statistics Denmark, Economy, general government economy, EMU debt and EMU balance, Tables in Stat Bank, EDP1: Government deficit and debt in the EU-countries by country, function and unit, in % of GDP.
- *Note:* Starts 1880; gaps 1947–1952, 1957–1959, 1997.

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 56, 57

- 1870–1912 — Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. DKK/GBP multiplied with GBP/USD exchange rate (see USD exchange rate for U.K.).
- 1913–1940 — Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015. http://www.measuringworth.com/exchangeglobal/
- 1941–1945 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1946–1956 — Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1957–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy** — `peg` — pp. 57

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 57

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 57

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 57

- 1875–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.
- *Note:* Starts 1875.

**Unemployment rate (percent)** — `unemp` — pp. 58

- 1874–1899 — Abildgren, Kim. 2009. Monetary Regimes and the Endogeneity of Labour Market Structures – Empirical Evidence from Denmark 1875-2007, European Review of Economic History, Vol. 13(2), pp. 199-218. Series: Unemployment rate; percent of labor force. Chainlinked.
- 1900–1972 — Abildgren, Kim. 2019. A Chart & Data Book on the Monetary and Financial History of Denmark. Series: Unemployment rate; percent of labor force. Chainlinked.
- 1973–2020 — ILOSTAT (2021), Table: "Unemployment rate by sex and age (%) - Annual" based on the EU Labour force survey accessible online at: https://ilostat.ilo.org/data/.
- *Note:* Starts 1874.

**Wages (index, 1990=100)** — `wage` — pp. 58

- 1870–1913 — International Historical Statistics. Europe's Labour Force – Money/Wages in Industry. Hourly wages of males. Chainlinked.
- 1914–1937 — Abildgren, Kim. 2009. Monetary Regimes and the Endogeneity of Labour Market Structures – Empirical Evidence from Denmark 1875-2007, European Review of Economic History, Vol. 13(2), pp. 199-218. Series Real hourly earnings in industry 1875-2007, before tax, 1875=100. Adjusted to nominal by using the CPI series also from Abildgren, Kim. A Chart & Data Book on the Monetary and Financial History of Denmark, Working Paper, 30 May 2017 (accessible online at https://sites.google.com/view/kim-abildgren/historical-statistics). Chainlinked.
- 1938–1989 — International Historical Statistics. Europe's Labour Force – Money/Wages in Industry. Hourly wages in manufacturing. Chainlinked.
- 1990–2020 — OECD. OECD statistics. Average annual wages. Current prices. Levels. Accessible online at http://stats.oecd.org/.

**Total loans to non-financial private sector (Credit Data, billions DKK)** — `tloans` — pp. 58, 59

- 1870–1951 — H.C. Johansen (1985), Dansk Historisk Statistik 1814–1980. Table 6.6, Series 2 "Domestic bills of exchange"; Series 4 "Other loans". and K. Abildgren (2006), Monetary Trends and Business Series in Denmark 1875–2005, Danmarks Nationalbank. Working Papers 43/2006. Appendix B, Table A.2 and Table A.3, Series "Loans".
- 1951–2005 — K. Abildgren (2007), Financial Liberalization and Credit Dynamics in Denmark in the Post–World War II Period, Danmarks Nationalbank, Working Papers 47/2007. Appendix B, Table B.1 and B.2, Series "Commercial lending" and Series "Private lending".
- 2006–2013 — growth rate from Statistics Denmark (2013), "DNSEKT3: The MFI–sectors domestic lending and deposits by balance post item, sector, data type and currency" (accessible at http://www.statbank.dk/).
- 2014–2020 — growth rate from Statistics Denmark (2021), "DNMUDL: Loans in total from banks and mortgage banks to households and non-financial cor by currency, data type, reporting institution, sector and time". Sum of Loans for "Non-financial corporations and households in total" for Banks and Mortgage banks at December of each year. All currency converted in Danish Krona (accessible at http://www.statbank.dk/).

**Mortgage loans to non-financial private sector** — `tmort` — pp. 59

- 1875–1980 — K. Abildgren (2006), Monetary Trends and Business Cycles in Denmark 1875–2005, Danmarks Nationalbank Working Papers 2006 43, Danmarks Nationalbank, Copenhagen. Appendix C "Data", Table A.3 "Financial balance sheet, mortgage–credit institutes, end–of–year 1875–2005, million kroner", series "Financial assets – loans", pp81 (accessible online at http://www.nationalbanken.dk/).
- 1981–1992 — Danmarks Nationalbank (June 2011), Udlån 1981–2010, provided by Mar. Egstrup of Danmarks Nationalbank. RI, series "Husholdninger", series "Øvrige".
- 1993–2013 — Statistics Denmark, "DNSEKT2: Mortgage–credit institutes domestic lending by sector and currency" (accessible online at http://www.statbank.dk/).
- 2014–2020 — growth rate from Statistics Denmark (2021), "DNMUDL: Loans in total from banks and mortgage banks to households and non-financial cor by currency, data type, reporting institution, sector and time". Mortgage banks. "Non-financial corporations and households in total" at December of each year. All currency converted in Danish Krona (accessible at http://www.statbank.dk/).
- *Note:* Starts 1875. Danish "mortgage loans" = lending by mortgage-credit institutes (to households and non-financial corporations), not bank mortgages.

**Total Loans to Households** — `thh` — pp. 59

- 1951–2005 — Abildgren (2007), ibid. Appendix B, Table B.1 and B.2, series "Private lending".
- 2006–2020 — Residual of Total loans to non-financial private sector and Total Loans to Business.
- *Note:* Starts 1951.

**Total Loans to Business** — `tbus` — pp. 59

- 1951–2005 — Abildgren (2007), ibid. Appendix B, Table B.1 and B.2, Series "Commercial lending".
- 2006–2013 — growth rate from Statistics Denmark, "DNSEKT3: The MFI–sectors domestic lending and deposits by balance post item, sector, data type and currency" (accessible online at http://www.statbank.dk/).
- 2014–2020 — growth rate from Statistics Denmark (2021), "DNMUDL: Loans in total from banks and mortgage banks to households and non-financial cor by currency, data type, reporting institution, sector and time". Sum of loans for "Non-financial corporations" for Banks and Mortgage banks at December for each year. All currency converted in Danish Krona.
- *Note:* Starts 1951.

**Corporate Debt** — `bdebt` — pp. 59, 60

- 1875–1950 — business loans of banks proxied by lending and domestic bills of exchange from commercial banks from Hans Christian Johannsen (1985) "Dansk Historisk Statistik 1814–1980", Table 6.6.
- 1951–1993 — Kim Abildgren (2007) "Financial Liberalization and Credit Dynamics in Denmark in the Post–World War II Period", Danmarks Nationalbank, Working Papers 47/2007, Appendix B, Table B.1 and B.2, Series "Commercial lending".
- 1994–2013 — OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2018 — eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2019–2020 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- *Note:* Starts 1875.

**Capital ratio = Capital / Total Assets (Bank balance sheet ratios; ratios in %, underlying data in billions DKK)** — `lev` — pp. 60, 61

- *Note:* Built from Total Assets and Capital components below (commercial banks + savings banks).

**Total Assets (component of lev/ltd/noncore; billions DKK)** — *component* — pp. 60

- 1870–1920 — Statistike Undersøgelser, Nr. 24 Kreditmarkedsstatistik, Danmarks Statistik, København 1969. Tilsammen. Aggregated bank-level data from end-financial year balance sheets of commercial banks published over the year. Chainlinked.
- 1921–1989 — Danmarks Statistik, Statistisk Årbog (various issues). Tilsammen/Total Assets/Total Liabilities of commercial banks + Tilsammen/Total Assets/Total Liabilities of savings banks.
- 1990–2015 — Danmarks Statistik, Statistisk Årbog (various issues). All banks. Total Assets. Levels.
- 2016–2020 — Danmarks Nationalbank, StatBank Denmark, Series: "DNBALD: Balance sheet items of the MFI sector, excl. Danmarks Nationalbank by disaggregated balance sheet items, data type and reporting institution", Total Assets, Outstanding amounts, Banks, December values. Chainlinked.

**Capital (component of lev; billions DKK)** — *component* — pp. 60, 61

- 1870–1920 — Statistike Undersøgelser, Nr. 24 Kreditmarkedsstatistik, Danmarks Statistik, København 1969. "Share capital" + "Reservefonds". Aggregated bank-level data from end-financial year balance sheets of commercial banks published over the year. Chainlinked with difference in capital ratio in 1920.
- 1921–1989 — Danmarks Statistik, Statistisk Årbog (various issues). "Capital social" + "Reserve legal" + "Autres reserves" or "Share capital" + "Reserves" of commercial banks and "Gavefonds" + "Kursreguleringsfond" + "Egentlige reservefonds" or "Share capital" + "Reserves" of savings banks.
- 1990–2015 — Danmarks Statistik, Statistisk Årbog (various issues). "Share capital" + "Reserves". All banks. Levels.
- 2016–2020 — Danmarks Nationalbank, StatBank Denmark, Series: "DNBALD: Balance sheet items of the MFI sector, excl. Danmarks Nationalbank by disaggregated balance sheet items, data type and reporting institution", Capital and reserves, Outstanding amounts, Banks, December values. Chainlinked.

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 61, 62

- *Note:* Built from Deposits and Loans components below.

**Deposits (component of ltd/noncore; billions DKK)** — *component* — pp. 61

- 1870–1920 — Statistike Undersøgelser, Nr. 24 Kreditmarkedsstatistik, Danmarks Statistik, København 1969. "Folio, indlan, kontokurant og sparekasse-indskud". Aggregated bank-level data from end-financial year balance sheets of commercial banks published over the year. Chainlinked.
- 1921–1974 — Danmarks Statistik, Statistisk Årbog (various issues). Commercial banks, sum of items "Folio Konto/Sight Deposits"+"Comptes Courants" +"Depots/Deposits" +"Deposits on bank books" +"Deposits one month or longer" (labels change over time) + savings banks "Depositor's Balances".
- 1975–1989 — Danmarks Statistik, Statistisk Årbog (various issues). Commercial banks and savings banks. "Deposits" or "Deposits (at call or less than one month's notice) + Deposits (at one month's or longer notice)".
- 1990–2015 — Danmarks Statistik, Statistisk Årbog (various issues). All banks. "Deposits" or "Deposits (at call or less than one month's notice) + Deposits (at one month's or longer notice)".
- 2016–2020 — Danmarks Nationalbank, StatBank Denmark, Series: "DNBALD: Balance sheet items of the MFI sector, excl. Danmarks Nationalbank by disaggregated balance sheet items, data type and reporting institution", Deposits, Outstanding amounts, Banks, December values. Chainlinked.

**Loans (component of ltd; billions DKK)** — *component* — pp. 61, 62

- 1870–1920 — Statistike Undersøgelser, Nr. 24 Kreditmarkedsstatistik, Danmarks Statistik, København 1969. Aggregated bank-level data from end-financial year balance sheets of commercial banks published over the year. Loans. Chainlinked.
- 1921–1974 — Abildgren, Kim. A Chart & Data Book on the Monetary and Financial History of Denmark, Working Paper. Series S007A "Total domestic non-bank credit extended by resident deposit banks". Chainlinked.
- 1975–1989 — Danmarks Statistik, Statistisk Årbog (various issues). Savings and commercial banks. Sum of "Overdraft facilities", "Bills of exchange", "Construction loans", "Mortgage Loans" and "Other Loans".
- 1990–2015 — Danmarks Statistik, Statistisk Årbog (various issues). All banks. "Loans".
- 2016–2020 — Danmarks Nationalbank, StatBank Denmark, Series: "DNBALD: Balance sheet items of the MFI sector, excl. Danmarks Nationalbank by disaggregated balance sheet items, data type and reporting institution", Loans, Outstanding amounts, Banks, December values. Chainlinked.

**Noncore ratio = (Total Assets – Capital - Deposits)/(Total Assets - Capital)** — `noncore` — pp. 62

- *Note:* Formula only.

### Finland (FIN) — "Data in millions FIM (New Markka)" — PDF pp. 62–71

**Population** — `pop` — pp. 62

- 1870–2020 — Statistics Finland (2021). Table "Population according to age (5-year) and sex in the whole country 1865 - 2020" (accessible online at http://pxnet2.stat.fi/PXWeb/pxweb/en/StatFin/StatFin__vrm__vaerak/).

**GDP (converted to millions FIM (New Markka))** — `gdp` — pp. 62

- 1870–1974 — Hjerppe (1994). Finland's Historical National Accounts. Table: 2B. Gross domestic product (accessible online at http://www.suomenpankki.fi). Levels.
- 1975–2020 — Statistics Finland. Annual national accounts. (in Euros, converted into FIM with official conversion rate) http://www.stat.fi/til/vtp/. Levels.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 62, 63

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 63

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 63

- 1870–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data-sets/.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.

**Investment-to-GDP ratio** — `iy` — pp. 63

- 1870–1950 — National Statistical Office of Finland (2007), Statistical Yearbook (accessible online at http://pxweb2.stat.fi/sahkoiset_julkaisut/vuosikirja2007/alku.htm).
- 1951–2020 — International Monetary Fund, International Financial Statistics. Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" divided by GDP from JST dataset (accessible online at https://data.imf.org/).

**Consumer prices (index, 1990=100)** — `cpi` — pp. 63

- 1870–1996 — A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, 84(1), pp. 139–150.
- 1997–2020 — International Monetary Fund World Economic Outlook (April 2019). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.

**Narrow Money (converted to millions FIM (New Markka))** — `narrowm` — pp. 63

- 1870–1987 — Mitchell, B. (2013). International Historical Statistics. Series: Sum of Currency in circulation + commercial bank deposits. Level.
- 1988–2004 — Bank of Finland (2012). Series sent by email, contact person Essi Tamminen from Bank of Finland – essi.tamminen@bof.fi. (see excel file in Data Sources) Series: M1. Level.
- 2005–2020 — Bank of Finland. Statistics. MFI balance sheet (loans and deposits) and interest rates, tables, Finnish contribution to euro area monetary aggregates and their main counterparts. M1: Contribution to euro area M1 = Overnight deposits. Redenominated from € into FIM. Level.

**Broad Money (converted to millions FIM (New Markka))** — `money` — pp. 64

- 1870–1899 — Bank of Finland (2012). Series sent by email, contact person Essi Tamminen from Bank of Finland – essi.tamminen@bof.fi. (see excel file in Data Sources) Series: M2 (historical series). Redenominated from old FIM into new FIM. Level.
- 1900–1916 — Bank of Finland (2012). Series sent by email, contact person Essi Tamminen (see excel file in Data Sources) Series: M2 (not historical). Redenominated from old FIM into new FIM. Level.
- 1917–1987 — Mitchell, B. (2013). International Historical Statistics. Series: Sum of Currency in circulation + commercial bank deposits + savings banks deposits (sum of all available). Level.
- 1988–2020 — Bank of Finland. Statistics. Statistics, MFI balance sheet (loans and deposits) and interest rates, tables, Finnish contribution to euro area monetary aggregates and their main counterparts: Contribution to euro area M2 (accessible online at http://www.suomenpankki.fi/). Redenominated from € into FIM. Level.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 64

- 1870–1952 — Autio, Jaakko. Korot Suomessa 1862-1952. Suomen Pankki, 1996.
- 1953–1977 — Post–WWII data from International Monetary Fund (2014), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – Discount Rate" (accessible online at http://elibrary–data.imf.org/).
- 1978–1986 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1987–2013 — Federal Reserve Bank of St. Louis; 3-Month or 90-day Rates and Yields: Interbank Rates for Finland; IR3TIB01FIA156N; End of period rates (First date of the year used as last date of previous year).
- 2014–2017 — International Monetary Fund (2019). International Financial Statistics. Interest Rates – Money Market Rates.
- 2018–2020 — OECD Short-term interest rates, Total, % per annum.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 64, 65

- 1870–1913 — Autio, Jaakko. Korot Suomessa 1862-1952. Suomen Pankki, 1996.
- 1914–1920 — Investor's Monthly Manual. Current yield of 4.5% Finland Government Railway Bond. Final redemption: 1965. December values.
- 1921–1938 — Autio, Jaakko. Korot Suomessa 1862-1952. Suomen Pankki, 1996.
- 1948–1986 — Alhonsuo, Sampo. Joukkovelkakirjalainojen tuotto Suomessa 1948-1986. Helsinki: Bank of Finland, Discussion paper 10/89.
- 1987 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1988–2014 — International Monetary Fund (2019). International Financial Statistics (IFS). Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds." (accessible online https://data.imf.org/)
- 2015–2020 — OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en, average of monthly values.
- *Note:* Gap 1939–1947 as printed.

**Current Account (converted to millions FIM (New Markka))** — `ca` — pp. 65

- 1870–1945 — calculated (percentage multiplied by NGDP) from Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data. In: G. Calvo, R. Dornbusch & M. Obstfeld (eds.) (2000), Money, Capital Mobility, and Trade: Essays in Honor of Robert A. Mundell, MIT Press, Cambridge. Series: current account (including gold flows). Note: series in old Finnish Markka; divide by 100 to get to new FIM. Level.
- 1946–1979 — Mitchell, B. (2013). International Historical Statistics. National Accounts – Balance of Payments – Overall current balance. Partly in USD -> redenominated in to new Finnish Markka with the exchange rate from JST dataset. Note: partly series in old Finnish Markka. Divide by 100 to redenominate into new FIM. Level.
- 1980–2020 — IMF World Economic Outlook Database. Path "Advanced Economies, Euro Area, Finland, Current Account Balance (% of GDP)" (accessible online at http://www.imf.org/external). Series multiplied with nominal GDP series (also from WEO). Level.

**Imports & Exports (converted to millions FIM (New Markka))** — `imports,exports` — pp. 65

- 1870–1883 — growth rate calculated from R. Hjerppe (1996), Finnish National Accounts, 1860–1994, Bank of Finland, Helsinki. Table 10a "Foreign Trade 1860 – 1985", Series "Exports" and Series "Imports", p259.
- 1884–2012 — Tull Customs (2013), Finnish Customs. Section "Foreign trade statistics", Subsection "Tables – Time Series", Table "Imports, exports and trade balance in 1884–2012" (accessible online at http://tulli.fi/en/statistics/time-series).
- 2013–2020 — Tull Customs, International Trade, Imports, Exports and trade balance, 1884 - 2020 (accessible online https://tulli.fi/en/statistics/time-series).

**Government Revenues (converted to millions FIM (New Markka))** — `revenue` — pp. 65

- 1882–1974 — Mitchell, Brian (2013), Table "Government revenue and main tax yield". Levels.
- 1975–2020 — Statistics Finland (2021), Sector Accounts 1975–2012, S1311 Central Government, TOTREV Total Revenue (accessible online at http://www.stat.fi/tup/suoluk/suoluk_valtiontalous_en.html). Levels.
- *Note:* Starts 1882; central government.

**Government Expenditure (converted to millions FIM (New Markka))** — `expenditure` — pp. 66

- 1882–1974 — Mitchell, Brian (2013), Table "Total Central Government Expenditure". Levels.
- 1975–2020 — Statistics Finland (2021), Sector Accounts 1975–2012, S1311 Central Government, TOTEXP Total Expenditure (accessible online at http://www.stat.fi/tup/suoluk/suoluk_valtiontalous_en.html). Levels.
- *Note:* Starts 1882; central government.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 66

- 1914–1946 — United Nations (1948). Public Debt. p.60 Table I. Column: Public Debt (at end of fiscal year) Total Debt - Amount outstanding.
- 1947–1969 — Statistics Finland, Statistical Yearbook of Finland, various issues.
- 1970–2020 — European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt. 18.2 – Based on ESA 2010 and former definitions. Gross Public Debt (linked series) (UDGGL). Percentage of GDP at market prices (excessive deficit procedure) (data accessible online at http://ec.europa.eu/economy_finance/db_indicators).
- *Note:* Starts 1914 for Finland.

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 66

- 1870–1945 — Autio, Jaakko. "Suomen Pankin Keskustelualoitteita: Valuuttakurssit Suomessa 1864-1991, Katsaus ja tilastosarjat" (1992), 1-246. FIM/GBP multiplied with GBP/USD exchange rate (see USD exchange rate of the U.K.)
- 1946–1960 — Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1961–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- *Note:* "We assume a Belgian franc-euro exchange rate of 5.94573 where necessary." (sic — 5.94573 is the Finnish markka–euro conversion rate; the word "Belgian" is a copy-paste error in the document.)

**Peg dummy** — `peg` — pp. 66

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 66, 67

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 67

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 67

- 1905–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.
- *Note:* Starts 1905.

**Unemployment rate (percent)** — `unemp` — pp. 67

- 1920–1938 and 1950–1979 — Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press. Chainlinked.
- 1980–1990 — OECD (2015), OECD.Stat. Database "Labour", "Labour Force Statistics", Dataset "ALFS summary tables", "Annual labour force statistics" (accessible online http//stats.oecd.org/).
- 1991–2020 — ILOSTAT (2021), Table "Unemployment rate by sex and age" based on the EU Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/.
- *Note:* Starts 1920; gap 1939–1949.

**Wages (index, 1990=100)** — `wage` — pp. 67

- 1870–1947 — Riitta Hjerppe (1989) "The Finnish Economy, 1860-1985. Growth and structural change." Page 274, table 12A, Manufacturing wages. Chainlinked. [printed as "11870 - 1947", a typo]
- 1948–1989 — International Monetary Fund International Financial Statistics database (IFS). Labor Markets, Manufacturing Wage Rates, Index. online at http://data.imf.org/. Chainlinked.
- 1990–2020 — OECD. OECD statistics. Average annual wages. Current prices. Levels. Accessible online at http://stats.oecd.org/.

**Total loans to non-financial private sector (Credit Data, converted to millions FIM (New Markka))** — `tloans` — pp. 67, 68

- 1870–2013 — Bank of Finland (2012), ibid. Series "Total loans".
- 2014–2020 — Bank of Finland (2021). Statistics. Tables. Finnish MFI euro-denominated loans within euro area, by sector. Sum of annual total outstanding loans of "Non-financial corporations" and "Households".
- *Note:* "Bank of Finland (2012), ibid." refers to the series sent by email by Essi Tamminen (see Narrow/Broad Money).

**Mortgage loans to non-financial private sector** — `tmort` — pp. 68

- 1927–1931 — Bank of Finland (1933), The Volume of Credits in Finland, in Bank of Finland (1934), Monthly Bulletin 07/1933, p.27–31. Table "The volume of credits in Finland at the end of 1927–1931, by nature of credit, real estate credit", p. 30.
- 1934–1978 — Statistics Finland (various), Statistical Yearbook of Finland (various issues). Table "Rahalaitosten yleisölle antamat lainat vakuuden mukaan vuosien [years] päättyessä." – "Prêts consentis par les établissements bancaires selon leur garantie à la fin des années", later translated into English as "Loans accorded to the public by banking establishments according to securities at 31 December". Addition of mortgage lending of each respective group of banks (commercial banks, savings banks, mortgage banks, post office savings bank, and cooperative credit societies).
- 1979–2002 — Statistics Finland (2012), Housing Loans to Households (incl. state and insurance company loans), provided by Essi Tamminen from the Bank of Finland essi.tamminen@bof.fi, +358 10 831 2395.
- 2003–2013 — Bank of Finland (2019), Finnish MFI euro–denominated loans to euro area households, by purpose, housing loans (accessible online at http://www.suomenpankki.fi/en/tilastot/pages/default.aspx).
- 2014–2020 — Bank of Finland (2021), Finnish MFIs' euro-denominated deposits and loans of euro area residents: stock, Loans, To Households, Housing Loans (accessible online at https://www.suomenpankki.fi/en/).
- *Note:* Starts 1927; gap 1932–1933. Concept changes from loans secured by real estate (all borrowers, 1934–1978) to housing loans to households (1979 on).

**Total Loans to Households** — `thh` — pp. 68

- 1948–1969 — residual of Total loans to non-financial private sector and Total Loans to Business.
- 1970–1994 — Statistics Finland, Financial Accounts Stocks 1970–1994. Sector "Households", Data "Liabilities", Instrument "AF4 loans" (accessible online at http://193.166.171.75/Database/StatFin/kan/rtp/rtp_en.asp).
- 1995–2010 — Statistics Finland. National Accounts 2018. Financial Accounts 2017. Appendix table 2. "Financial liabilities Households, million EUR" (converted to Finnish markka). Loans. (Accessible online at https://www.stat.fi/til/rtp/index_en.html).
- 2011–2020 — Statistics Finland. National Accounts 2021. Appendix table 2. "Financial liabilities Households, million EUR" (converted to Finnish markka). Loans. (Accessible online at https://www.stat.fi/til/rtp/tie_en.html).
- *Note:* Starts 1948.

**Total Loans to Business** — `tbus` — pp. 68, 69

- 1948–1969 — calculated from Statistics Finland (various), Statistical Yearbook (various issues). Table "Loans by the credit institutions by groups of borrowers on 31 December", Series "Total w/o municipalities and parishes". Base is 1970 value.
- 1970–2020 — residual of Total loans to non-financial private sector and Total Loans to Households.
- *Note:* Starts 1948.

**Corporate Debt** — `bdebt` — pp. 69

- 1948–1969 — calculated from Statistics Finland (various), Statistical Yearbook (various issues). Table "Loans by the credit institutions by groups of borrowers on 31 December", Series "Total w/o municipalities and parishes". Base is 1970 value.
- 1970–1994 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- 1995–2013 — financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2019 — eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- *Note:* Starts 1948; documented only to 2019.

**Capital ratio = Capital / Total Assets (Bank balance sheet ratios; ratios in %, underlying data in millions FIM (New Markka))** — `lev` — pp. 69, 70

- *Note:* Built from Total Assets and Capital components below; starts 1873.

**Total Assets (component of lev/ltd/noncore; converted to millions FIM (New Markka))** — *component* — pp. 69

- 1873–1903 — Bank of Finland, Historical Monetary Financial Institutions Time Series, sum of liability items of commercial banks (Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Chainlinked.
- 1904–2013 — Bank of Finland, Historical Monetary Financial Institutions Time Series, Sum of liability items. See Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Levels.
- 2014–2020 — Bank of Finland, Aggregated balance sheet of Finnish MFIs excluding Bank of Finland. Total.

**Capital (component of lev; converted to millions FIM (New Markka))** — *component* — pp. 69, 70

- 1873–1903 — Bank of Finland, Historical Monetary Financial Institutions Time Series, Capital of commercial banks (Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Chainlinked with difference in capital ratio.
- 1904–2013 — Bank of Finland, Historical Monetary Financial Institutions Time Series, Capital (Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Levels. 1990/1991 data are interpolated capital ratios. Banks could transfer 90% of loan loss reserves to reserve fund accounts in 1990. After 1991 new rules in place (Vihriälä, Vesa (1997), Banks and the Finnish credit cycle 1986-1995, Appendix 1, Bank of Finland monographs).
- 2014–2020 — Bank of Finland, Aggregated balance sheet of Finnish MFIs excluding Bank of Finland. Capital and reserves.
- *Note:* 1990/1991 capital ratios are interpolated because of a regulatory change allowing transfer of 90% of loan-loss reserves to reserve funds in 1990.

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 70

- *Note:* Built from Deposits and Loans components below.

**Deposits (component of ltd/noncore; converted to millions FIM (New Markka))** — *component* — pp. 70

- 1873–1903 — Bank of Finland, Historical Monetary Financial Institutions Time Series (Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Commercial banks, "Deposits to non-MFIs", Chainlinked.
- 1904–2013 — Bank of Finland, Historical Monetary Financial Institutions Time Series, Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). "Deposits to non-MFIs", Levels.
- 2014–2020 — Bank of Finland Aggregated balance sheet of Finnish MFIs excluding Bank of Finland. Deposits of Euro Area residents. Chainlinked.

**Loans (component of ltd; converted to millions FIM (New Markka))** — *component* — pp. 70

- 1873–1903 — Bank of Finland, Historical Monetary Financial Institutions Time Series (Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22). Commercial banks, "Loans to non-MFIs", Chainlinked.
- 1904–2013 — Bank of Finland, Historical Monetary Financial Institutions Time Series, Risto Herrala (1999) Banking Crises vs Depositor Crises: the Era of the Finnish Markka, Scandinavian Economic History Review vol 47, No 2, 5-22. "Loans to non-MFIs", Levels.
- 2014–2020 — Bank of Finland Aggregated balance sheet of Finnish MFIs excluding Bank of Finland. Loans to Euro Area residents. Chainlinked.

**Noncore ratio = (Total Assets – Capital - Deposits) / (Total Assets - Capital)** — `noncore` — pp. 71

- *Note:* Formula only.

### France (FRA) — "Data in billions FRF (new francs)" — PDF pp. 71–84

**Population** — `pop` — pp. 71

- 1870–2008 — Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls).
- 2009–2016 — growth rates from International Monetary Fund (Aug, 2019), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).
- 2017–2020 — growth rates from International Monetary Fund, World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).

**GDP (converted to billions FRF (new francs))** — `gdp` — pp. 71

- 1870–1938 — Mitchell, Brian (2013), International Historical Statistics: Europe 1750–2010, Palgrave Macmillan, London. No data for 1914–1919.
- 1914–1919 & 1939–1949 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1950–2020 — International Monetary Fund (2021), International Financial Statistics. Data Report "Economic indicators", Series "Gross domestic product (in millions) – GDP nominal" (accessible online at https://data.imf.org/).

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 71

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 72

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 72

- 1870–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data–sets/.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.

**Investment-to-GDP ratio** — `iy` — pp. 72

- 1870–1918 — Mitchell, Brian (2007), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London.
- 1920–1924 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1925–1950 — Mitchell, Brian (2007), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London. (Note: no data for 1945).
- 1950–2020 — International Monetary Fund, International Financial Statistics. Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- *Note:* The 1920–1924 van Meerten (Belgium) citation for a French series appears to be a copy-paste error in the document; 1919 and 1945 missing.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 72

- 1870–1965 — Mitchell, B. (2013) International Historical Statistics: Europe 1750-2005. Palgrave Macmillan, London. CPI.
- 1966–2020 — International Monetary Fund International Financial Statistics (2021). Prices, Consumer Price Index, All items, Index. Rebased: 1990=100 (accessible online at https://data.imf.org/).
- *Note:* France is an exception to the usual Taylor (2002) CPI source.

**Narrow Money (converted to billions FRF (new francs))** — `narrowm` — pp. 72

- 1870–1913 & 1920–1949 — M. Saint Marc (1983). Histoire monétaire de la France 1800-1918. pp. 37-38. Series M1. Level.
- 1950–1977 — Mitchell, B. (2013). International Historical Statistics. Series M1. Level.
- 1978–2020 — Banque de France. Monthly monetary statistics. M1. Average of monthly values. Online: http://webstat.banque-france.fr/en/home.do. Level.
- *Note:* Gap 1914–1919.

**Broad Money (converted to billions FRF (new francs))** — `money` — pp. 73

- 1870–1913 & 1920–1949 — M. Saint Marc (1983). Histoire monétaire de la France 1800-1918. Sum of series M1 (pp.37-38) + Savings ("Caisses d'epargne Solde des deposants", pp. 55-57). Level.
- 1950–1979 — Mitchell, B. (2013). International Historical Statistics. Series M2. Level.
- 1980–2020 — Banque de France. Monthly monetary statistics. M2 France. Dec values. Online: http://webstat.banque-france.fr/en/home.do. Level.
- *Note:* Gap 1914–1919.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 73

- 1870–1879 — Neal, Larry D., and Marc D. Weidenmier. "Crises in the global economy from tulips to today." Globalization in historical perspective. University Of Chicago Press, 2003. 473-514. Open Market Rate, Monthly, End of Year Value. (accessible online at http://ebutts05.tripod.com/nealweidenmiergsd/)
- 1880–1914 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1922–1924 — Statistisches Handbuch der Weltwirtschaft 1936. p.95 Series: Privatdiskont.
- 1925–1939 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1939–1947 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. Table 63 - Short-term French Interest Rates: Twentieth century. Private discount rate until 1939, money market rate thereafter. Levels.
- 1948–1998 — International Monetary Fund (2012), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – money market rate" (accessible online at http://elibrary–data.imf.org/). Levels
- 1999–2016 — International Monetary Fund (2019), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – treasury bill rate" (accessible online at http://data.imf.org/).
- 2017–2020 — Banque de France. French government debt indicative rates, 3 month, average of daily rates.
- *Note:* Gap 1915–1921.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 73, 74

- 1870–1947 — Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. Bank of England Staff Working Paper No. 845.
- 1948–2014 — International Monetary Fund (2019). International Financial Statistics (IFS). Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds" (accessible online at http://data.imf.org/). Levels
- 2015–2020 — OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en, average of monthly values.

**Current Account (converted to billions FRF (new francs))** — `ca` — pp. 74

- 1870–1945 — M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA. France – Current account original. (accessible online at http://www.nber.org/databases). (data missing for 1st and 2nd World Wars). Level
- 1948–1974 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2010, Palgrave Macmillan, London. Level
- 1975–1979 — International Monetary Fund (2010), International Financial Statistics. Table "Balance of payments", Series "Balances – current account balance" (accessible online http://elibrary–data.imf.org/). Level
- 1980–2020 — International Monetary Fund, World Economic Outlook. % of GDP * nominal GDP = Current Account (available at www.imf.org/external). Level
- *Note:* Missing for both World Wars and 1946–1947.

**Imports & Exports (converted to billions FRF (new francs))** — `imports,exports` — pp. 74

- 1870–1947 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London.
- 1948–2020 — International Monetary Fund, International Financial Statistics: archive, M10 2021, External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency; External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency.

**Government Revenues (converted to billions FRF (new francs))** — `revenue` — pp. 74

- 1870–1977 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2010, Palgrave Macmillan, London. Central Government revenue and main tax yields. Levels.
- 1978–2020 — OECD (2021), OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "Euros, current prices," Series GTR "Total general government revenue" (accessible online at http://www.oecd–ilibrary.org/statistics). Levels.
- *Note:* Central government throughout.

**Government Expenditure (converted to billions FRF (new francs))** — `expenditure` — pp. 74

- 1870–1977 — B. Mitchell (2007), International Historical Statistics: Europe 1750–2010, Palgrave Macmillan, London. Total Central Government expenditure. Levels.
- 1978–2020 — OECD (2021), OECD.Stat. Database "OECD national accounts statistics," Dataset "General government accounts," Table 12 "Government deficit/surplus, revenue, expenditure, and main aggregates," Sector GS1311 "Central government," Measure "Euros, current prices," Series GTE "Total general government expenditure" (accessible online at http://www.oecd–ilibrary.org/statistics). Levels.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 75

- 1880–1913 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1920–1938 — United Nations (1948). Public Debt, 1914–1946. Department of Economic Affairs, Lake Success, NY.
- 1949–1977 — Abbas et al. (2010). A Historical Public Debt Database. IMF working paper. www.imf.org. Levels.
- 1978–1979 — INSEE: "Annuaire Rétrospectif de la France, Séries Longues, 1948–1988." Publication is accessible at http://gallica.bnf.fr/
- 1980–2020 — European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt. 18.2 – Based on ESA 2010 and former definitions. Gross Public Debt (linked series) (UDGGL). Percentage of GDP at market prices (excessive deficit procedure) (data accessible online at http://ec.europa.eu/economy_finance/). Levels
- *Note:* "Note: Data for 1880 – 1979 is for central government debt only."
- *Note:* Starts 1880; gaps 1914–1919, 1939–1948; central government only before 1980, general government (EDP) from 1980.

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 75

- 1870–1912 — Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. FRF/GBP exchange rate multiplied with GBP/USD exchange rate (see USD exchange rate of the U.K.)
- 1913–1940 — Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015. http://www.measuringworth.com/exchangeglobal/
- 1941–1945 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1946–1958 — Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1959–2020 — International Financial Statistics. IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- *Note:* "We assume a French franc-euro exchange rate of 6.55957 where necessary."

**Peg dummy** — `peg` — pp. 75, 76

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.

**Strict peg dummy** — `peg_strict` — pp. 76

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2020 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs. [printed as 1940–2020, presumably 1940–2007]
- 2008–2020 — extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1, all 2-6=0); strict peg category excluding crawling pegs.

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 76

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 76

- 1870–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** — `unemp` — pp. 76

- 1895–1913 — Mitchell, Brian (2013), International Historical Statistics Europe, 1750–2010, Table B2 Europe Unemployment, Palgrave Macmillan, London.
- 1921–1939 — Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter International Comparison of Unemployment Rates, Table E-8 "Estimated Unemployment Rate among Wage and Salary earners in Manufacturing, Mining, and Construction, France, 1921-1939".
- 1950–1979 — Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press. Chainlinked.
- 1980–2020 — ILOSTAT (2021), Table "Unemployment rate by sex and age" based on the EU Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/
- *Note:* Starts 1895; gaps 1914–1920 and 1940–1949.

**Wages (index, 1990=100)** — `wage` — pp. 76, 77

- 1870–1897 and 1912–1938 — Scholliers & Zamagni (1995). "Labour's Reward: Real wages and economic change in 19th- and 20th-century Europe". Nominal Wages France. Chainlinked.
- 1939–1946 — International Labour Organization. ILO statistical yearbooks. Hourly earnings for industrial workers in the region of Paris. Chainlinked.
- 1947 — International Historical Statistics. Europe's Labour Force – Money/Wages in Industry. Weighted mean of hourly wages in all sectors in Paris and in the provinces. Chainlinked.
- 1948–1989 — International Monetary Fund International Financial Statistics database (IFS). Labor Markets, Wage Rates, Index. Accessible online at http://data.imf.org/. Chainlinked.
- 1990–2020 — OECD. OECD statistics. Average annual wages. Current prices. Levels. Accessible online at http://stats.oecd.org/.
- *Note:* Gap 1898–1911.

**Total loans to non-financial private sector (Credit Data, converted to billions FRF (new francs))** — `tloans` — pp. 77, 78, 79

- 1900–1910 — M. Saint Marc (1983), Histoire Monétaire de la France, 1880–1980, Presses Universitaires de France, Paris. p.64 Series 8 "Crédit accordés par toutes les banques commerciales".
- 1911–1938 — J.P. Patat, and M. Lutfalla (1986), Histoire Monétaire de la France au XXE Siècle, Economica, Paris. p244–281, Series "Séries corrigées des variations saisonnières – Créances sur l'économie".
- 1946–1957 — Eric Monnet (2013). Financing a planned economy. Credit Allocation, institutions and growth during French Golden Age. Berkeley economic history working paper. (data sent by Eric Monnet). Chainlinked backwards.
- 1958 — Conseil National du Crédit (1959), Annual Report, appendix. Page 54. Crédits financés par des ressources monétaires + crédits financés par des fonds publics ou des ressources diverses. Available at www.gallica.bnf.fr. Levels.
- 1959 — Conseil National du Crédit (1960), Annual Report, appendix. Page 52. Crédits financés par des ressources monétaires + crédits financés par des fonds publics ou des ressources diverses. Available at www.gallica.bnf.fr. Levels.
- 1960 — Conseil National du Crédit (1961), Annual Report, appendix. Page 54. Same series. Levels.
- 1961 — Conseil National du Crédit (1962), Annual Report, appendix. Page 66. Same series. Levels.
- 1962 — Conseil National du Crédit (1963), Annual Report, appendix. Page 82. Same series. Levels.
- 1963 — Conseil National du Crédit (1964), Annual Report. Page 166. Crédits bancaires en france (banques+banque de France) métropolitaine. Available at www.gallica.bnf.fr. Levels.
- 1964 — Conseil National du Crédit (1965), Annual Report. Page 166. Crédits bancaires en france (banques+banque de France) métropolitaine. Levels.
- 1965 — Conseil National du Crédit (1966), Annual Report. Page 175. Same series. Levels.
- 1966 — Conseil National du Crédit (1967), Annual Report. Page 108. Same series. Levels.
- 1967 — Conseil National du Crédit (1968), Annual Report. Page 103. Same series. Levels.
- 1968 — Conseil National du Crédit (1969), Annual Report, appendix. Page 92. Same series. Levels.
- 1969 — Conseil National du Crédit (1970), Annual Report, appendix. Page 97. Same series. Levels.
- 1970 — Conseil National du Crédit (1971), Annual Report, appendix. Page 101. Same series. Levels.
- 1971 — Conseil National du Crédit (1972), Annual Report, appendix. Page 99. Same series. Levels.
- 1972 — Conseil National du Crédit (1973), Annual Report, appendix. Page 119. Same series. Levels.
- 1973 — Conseil National du Crédit (1974), Annual Report, appendix. Page 126. Same series. Levels.
- 1974 — Conseil National du Crédit (1975), Annual Report, appendix. Page 137. Same series. Levels.
- 1975–1976 — Conseil National du Crédit (1977), Annual Report, appendix. Page 174. Same series. Levels.
- 1977–1979 — Conseil National du Crédit (1980), Annual Report, appendix. Page 185. Same series. Levels.
- 1980–2013 — Banque de France, France Crédits Secteur Privé Residents, Serie: « Crédits des non-IFM hors APU résidentes auprès des IFM, administrations centrales et banques postales, encours. Paris. (available at webstat.banque-france.fr). Year average of monthly values.
- 2014–2020 — Banque de France, Series Title: « Loans (adjusted for loan sales and securitisation) granted to domestic non MFIs except General Government stocks. (available at webstat.banque-france.fr). End of period values.
- *Note:* Starts 1900; gap 1939–1945. 1958–1962 = credits financed by monetary resources + credits financed by public funds or other resources; 1963–1979 = bank credits in metropolitan France (banks + Banque de France); 1980–2013 year averages of monthly values vs end-of-period from 2014.

**Mortgage loans to non-financial private sector** — `tmort` — pp. 79, 80

- 1870–1898 — growth rate calculated from Crédits Foncier, Prêts Hypothécaires, Archive du Monde du Travail, Time Series Code 2003 065 440–441.
- 1870–1898 — Crédits Foncier and Banque Hypothécaire, Prêts Hypothécaires, Archive du Monde du Travail, Time Series Code 2003 065 440–441. [both 1870–1898 entries appear as printed]
- 1899–1919 — growth rate calculated from Banque Hypothécaire, Prêts Hypothécaires, Archive du Monde du Travail. Time Series Code 2003 065 440–441.
- 1920–1928 — Banque Hypothécaire, Prêts Hypothécaires, Archive du Monde du Travail. Time Series Code 2003 065 440–441 and Statistisches Reichsamt of Germany (1936), "Statistisches Handbuch der Weltwirtschaft," Berlin: Verein für Socialpolitik, Wirtschaft und Statistik, series "Crédit Fonciers de France, Hypotheken".
- 1929–1933 — growth rate calculated from Statistisches Reichsamt of Germany (1936), "Statistisches Handbuch der Weltwirtschaft," Berlin: Verein für Socialpolitik, Wirtschaft und Statistik, series "Crédit Fonciers de France, Hypotheken".
- 1946–1957 — Conseil National de Crédit, Crédit à l'Habitat, Banque de France Archives Historiques, Paris. And growth rate calculated from Crédits Foncier and Banque Hypothécaire, Prêts Hypothécaires, Archive du Monde du Travail. Time Series Code 2003 065 440–441.
- 1958 — Conseil National du Crédit (1959), Annual Report. Page 135. Series: Les crédits au logement. Available at www.gallica.bnf.fr. Levels.
- 1959 — Conseil National du Crédit (1960), Annual Report. Page 134. Series: Les crédits au logement. Levels.
- 1960 — Conseil National du Crédit (1961), Annual Report. Page 126. Series: Les crédits au logement. Levels.
- 1961 — Conseil National du Crédit (1962), Annual Report. Page 131. Series: Les crédits au logement. Levels.
- 1962 — Conseil National du Crédit (1963), Annual Report. Page 148. Series: Les crédits au logement. Levels.
- 1963 — Conseil National du Crédit (1964), Annual Report. Page 181. Series: Les crédits au logement. Levels.
- 1964 — Conseil National du Crédit (1965), Annual Report. Page 180. Series: Les crédits au logement. Levels.
- 1965 — Conseil National du Crédit (1966), Annual Report, Page 190. Series: Les crédits au logement. Levels.
- 1966 — Conseil National du Crédit (1967), Annual Report, Page 115. Series: Les crédits au logement. Levels.
- 1967 — Conseil National du Crédit (1968), Annual Report, Page 110. Series: Les crédits au logement. Levels.
- 1968 — Conseil National du Crédit (1969), Annual Report, Page 100. Series: Les crédits au logement. Levels.
- 1969 — Conseil National du Crédit (1970), Annual Report, Page 107. Series: Les crédits au logement. Levels.
- 1970 — Conseil National du Crédit (1971), Annual Report, Page 112. Series: Les crédits au logement. Levels.
- 1971 — Conseil National du Crédit (1972), Annual Report, Page 114. Series: Les crédits au logement. Levels.
- 1972 — Conseil National du Crédit (1973), Annual Report, Page 136. Series: Les crédits au logement. Levels.
- 1973 — Conseil National du Crédit (1974), Annual Report, Page 139. Series: Les crédits au logement. Levels.
- 1974 — Conseil National du Crédit (1975), Annual Report, Page 156. Series: Les crédits au logement. Levels.
- 1975–1976 — Conseil National du Crédit (1974), Annual Report, Page 192. Series: Les crédits au logement. Available at www.gallica.bnf.fr. Levels. [year of report printed as 1974]
- 1977–1999 — sum of Mortgage Loans to Households and Total loans to business secured by real estate.
- 2000–2020 — Banque de France Series title: « Housing loans (adjusted for sales and securitisation) granted to domestic non-financial customers stocks », Series key: « BSI1.M.FR.N.A.A220Z.A.1.U6.2310FR.Z01.E », End of period Values.
- *Note:* Gaps 1934–1945. Pre-1934 series track mortgage lending of the Crédit Foncier / Banque Hypothécaire only; 1946–1976 is housing credit ("crédits au logement").

**Total Loans to Households** — `thh` — pp. 80, 81

- 1958–1976 — residual of Total loans to non-financial private sector and Total Loans to Business.
- 1977 — Conseil National du Crédit (1980), Annual Report. Page 193. Crédit aux ménages. Available at www.gallica.bnf.fr. Levels.
- 1978–1985 — Conseil National du Crédit (1987), Annual Report. Page 127. Crédit aux ménages. Available at www.gallica.bnf.fr. Levels.
- 1986–1987 — Conseil National du Crédit (1988), Annual Report. Page 90. Crédit aux ménages. Available at www.gallica.bnf.fr. Levels.
- 1988–1992 — Banque de France Archives Historiques (1994), Bulletin de la Banque de France Statistiques Monétaires et Financières Annuelles 1994 (Hors Séries), Paris. Time Series Code 1417201201/2.
- 1993–2017 — Institute National de la Statistique et des Etudes Economiques, Series: « d de crédit implantés en France à des résidents français en 2016, Crédits aux ménages» (available at https://www.insee.fr/fr/statistiques/2569408?sommaire=2587886&q=Crédits+des+établissements. Thémes – Economie – Monnaie-Marché financières - Crédits des établissements de crédit implantés en France à des résidents français en 2013, Crédits aux ménages)
- 2018–2020 — Webstat Banque de France, Loans granted to domestic households and NPISHs stocks, end of period values, December values (available http://webstat.banque-france.fr/en/#/home . Loans – Loans to Households – Total loans – Loans granted to domestic households and NPISHs stocks).
- *Note:* Starts 1958 for France.

**Total Loans to Business** — `tbus` — pp. 81, 82

- 1958 — Conseil National du Crédit (1959), Annual Report, Page 129. Crédit aux entreprises industrielles et comercielles. Series: Total. Available at www.gallica.bnf.fr. Chainlinked.
- 1959 — Conseil National du Crédit (1960), Annual Report. Page 128. Crédit aux entreprises industrielles et comercielles. Series: Total. Chainlinked.
- 1960 — Conseil National du Crédit (1961), Annual Report. Page 121. Same series. Chainlinked.
- 1961 — Conseil National du Crédit (1962), Annual Report. Page 126. Same series. Chainlinked.
- 1962 — Conseil National du Crédit (1963), Annual Report. Page 142. Same series. Chainlinked.
- 1963 — Conseil National du Crédit (1964), Annual Report, Page 172. Same series. Chainlinked.
- 1964 — Conseil National du Crédit (1965), Annual Report, Page 171. Same series. Chainlinked.
- 1965–1966 — Conseil National du Crédit (1966), Annual Report, Page 180. Same series. Chainlinked.
- 1967 — Conseil National du Crédit (1968), Annual Report. Page 104. Same series. Chainlinked.
- 1968 — Conseil National du Crédit (1969), Annual Report, Page 94. Same series. Chainlinked.
- 1969 — Conseil National du Crédit (1970), Annual Report. Page 99. Same series. Chainlinked.
- 1970 — Conseil National du Crédit (1974), Annual Report, Page 129. Same series. Chainlinked.
- 1971 — Conseil National du Crédit (1975), Annual Report, Page 140. Same series. Chainlinked.
- 1972–1976 — Conseil National du Crédit (1976), Annual Report, Page 178. Same series. Chainlinked.
- 1977 — Conseil National du Crédit (1983), Annual Report, Appendix. Page 129. Crédit aux entreprises industrielles et comercielles. Series: Total. Levels.
- 1978–1979 — Conseil National du Crédit (1987), Annual Report, Appendix. Page 129. Same series. Levels.
- 1980–2020 — residual of Total loans to non-financial private sector and Total Loans to Households.
- *Note:* Starts 1958.

**Corporate Debt** — `bdebt` — pp. 82

- 1902–1933 — residual of total bank credit from JST database (from Saint Marc, Patat and Lutfalla) less real estate lending from Crédit Foncier.
- 1958–1976 — Annual Reports of the Conseil National du Credit, published between 1959 and 1976: Credit aux entreprises industrielles et comercielles, total series. Available at www.gallica.bnf.fr.
- 1977–1994 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- 1995–2012 — OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2013–2018 — eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2019–2020 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- *Note:* Starts 1902; gap 1934–1957.

**Capital ratio = Capital / Total Assets (Bank balance sheet ratios; ratios in %, underlying data in billions FRF (new francs))** — `lev` — pp. 82, 83

- *Note:* Built from Total Assets and Capital components below; starts 1890.

**Total Assets (component of lev/ltd/noncore; billions FRF (new francs))** — *component* — pp. 82, 83

- 1890–1945 — Mazbouri, Malik, Sebastian Guex, and Rodrigo Lopez. 2017. Swiss Data Bank of International Bank Data (1890–1970). University of Lausanne. (http://www.unil.ch/hist/placefinanciere), series "Total bilan". Chainlinked.
- 1946–1969 — Commission de controle des banques, Rapport annuel, Tableau No. 2, Metropolitaine, series "Total". Chainlinked.
- 1970–1979 — Commission de controle des banques, Rapport annuel, Tableau No. 1, Metropolitaine, series "Total". Chainlinked.
- 1980–1987 — Banque de France, "IFM Hors BDF", sum of all reported liability items. Chainlinked.
- 1988–1996 — OECD Banking Statistics. All banks, Total Assets – end of year. Chainlinked.
- 1997–2020 — Banque de France, series "Total assets of domestic MFIs except NCB, stocks", series key BSI1.M.FR.N.A.T00.A.1.Z5.0000.Z01.E. Levels.

**Capital (component of lev; billions FRF (new francs))** — *component* — pp. 83

- 1890–1945 — Mazbouri, Malik, Sebastian Guex, and Rodrigo Lopez. 2017. Swiss Data Bank of International Bank Data (1890–1970). University of Lausanne. (http://www.unil.ch/hist/placefinanciere), series "Fonds propres". Chainlinked capital ratio (difference).
- 1946–1969 — Rapport annuel, Commission de controle des banques, Tableau No. 2, Metropolitaine, series "Capital"+"Reserves"+"Benefices Reports". Capital ratio in levels multiplied with Total Assets.
- 1970–1981 — Rapport annuel, Commission de controle des banques, Tableau No. 1, Metropolitaine, series "Capital"+"Reserves"+"Benefices Reports". Capital ratio in levels multiplied with Total Assets.
- 1982–1989 — Banque de France, series "IFM Hors BDF – Capital", series key MI.M.FR.N.A.L60.X.1.Z5.0000.Z01.M.E.B.X. Chainlinked.
- 1990–2008 — OECD Banking Statistics. All banks, "Capital and Reserves" divided by "Total Assets". Resulting capital ratio multiplied with Total Assets (see above).
- 2009–2020 — ECB Consolidated Banking Data, series "Full sample (All banking groups / stand-alone banks irrespective of their accounting / supervisory reporting framework), Tangible equity [% of total assets] (CBD2.Q.FR.W0.11._Z._Z.A.F.I3309._Z._Z._Z._Z._Z._Z.PC), Percent (PC)". Chainlinked.

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 83, 84

- *Note:* Built from Deposits and Loans components below; starts 1946 for France.

**Deposits (component of ltd/noncore; billions FRF (new francs))** — *component* — pp. 83, 84

- 1946–1969 — Rapport annuel, Commission de controle des banques, Tableau No. 2, Metropolitaine, sum of series "Comptes de cheques" and "Comptes courants". Chainlinked.
- 1970–1983 — Rapport annuel, Commission de controle des banques, Tableau No. 1, Metropolitaine, sum of "Comptes d'entreprises et divers" and "Comptes de particuliers" or sum of "Comptes crediteurs de la clientele" and "Comptes d'epargne a regime special". Chainlinked.
- 1984–1987 — Banque de France, series "IFM Hors BDF-Passif-Residents-Depots Autres Secteurs", series key MI.M.FR.N.A.L20.A.1.U6.2300.Z01.M.E.B.X. Chainlinked.
- 1988–1996 — OECD Banking Statistics. All banks, Customer deposits. Chainlinked.
- 1997–2020 — Banque de France, series "Deposits placed by domestic Non-MFIs excluding central government, stocks", series key BSI1.M.FR.N.A.L20.A.1.U6.2300.Z01.E. Levels.

**Loans (component of ltd; billions FRF (new francs))** — *component* — pp. 84

- 1946–1969 — Rapport annuel, Commission de controle des banques, Tableau No. 2, Metropolitaine, sum of series "Comptes courants et avances garanties" and "Autres effets". Chainlinked.
- 1970–1983 — Rapport annuel, Commission de controle des banques, Tableau No. 1, Metropolitaine, sum of "Credits a la Clientele - Portfeuille" and "Credits a la Clientele - Comptes Debiteurs". Chainlinked.
- 1984–1987 — Banque de France, series "IFM Hors BDF-Actif-Residents-Credits Secteur Prive", series key MI.M.FR.N.A.A20.A.1.U6.2200.Z01.M.E.B.X. Chainlinked.
- 1988–1996 — OECD Banking Statistics. All banks, Loans. Chainlinked.
- 1997–2020 — Banque de France, series "Loans granted to domestic non MFIs except General Government by domestic MFIs, stocks", series key BSI1.M.FR.N.A.A20.A.1.U6.2200.Z01.E. Chainlinked.

**Noncore ratio = (Total Assets – Capital - Deposits) / (Total Assets - Capital)** — `noncore` — pp. 84

- *Note:* Formula only.

### Germany (DEU) — "Data in billions DM" — PDF pp. 84–97

**Population** — `pop` — pp. 85

- 1870–1990 — Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (accessible online at http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls).
- 1991–2008 — Maddison Project Database (2018), ibid. Table "Population, mid-years (thousands)" (accessible online at www.ggdc.net/maddison).
- 2009–2017 — growth rates from International Monetary Fund (Aug, 2019), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).
- 2018–2020 — growth rates from International Monetary Fund (Oct, 2021), World Economic Outlook. Subject "People – population" (base year: 2008) (accessible at www.imf.org).
- *Note:* Switch to Maddison Project Database 2018 from 1991 (reunification).

**GDP (converted to billions DM)** — `gdp` — pp. 85

- 1870–1912 — growth rates from Burhop, C./Wolff, G., 2005: A Compromise Estimate of German Net National Product, 1851-1913, and its Implications for Growth and Business Cycles, in: The Journal of Economic History, Volume 65, September 2005, No. 3, S. 613-657. - Net National Product.
- 1913–1924 — growth rates from Ritschl, Albrecht; Spoerer, Mark, (1997 [2011]) Das Bruttosozialprodukt in Deutschland nach den amtlichen Volkseinkommens- und Sozialproduktstatistiken 1901-1995. GESIS Köln, Deutschland ZA8137 Datenfile Version 1.2.0. - BSP zu Marktpreisen, real (reflated with CPI series from JST dataset).
- 1925–1949 — (1945 missing) growth rates from Ritschl, Albrecht; Spoerer, Mark, (1997 [2011]) Das Bruttosozialprodukt in Deutschland nach den amtlichen Volkseinkommens- und Sozialproduktstatistiken 1901-1995. GESIS Köln, Deutschland ZA8137 Datenfile Version 1.2.0. - Bruttosozialprodukt.
- 1950–1969 — growth rates from Sensch, Jürgen, (1997, 2012 [2013]) Ausgewählte Daten zur Wirtschaftentwicklung der Bundesrepublik Deutschland seit 1948. GESIS Köln, Deutschland ZA8528 Datenfile Version 1.0.0 - BIP in jeweiligen Preisen.
- 1970–2020 — IMF eLibrary. International Financial Statistics. Series "Gross domestic product (in billions) – GDP nominal" (accessible online at https://data.imf.org/).
- *Note:* German nominal GDP is built backwards from 1970 IFS levels by growth rates; 1870–1912 uses NNP growth; 1913–1924 uses real GNP reflated with the JST CPI; 1945 missing.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 85

- 1870–2010 — The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level.
- 2011–2020 — International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 86

- 1870–2004 — R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data).
- 2005–2020 — growth rate calculated from World Bank (2021), Category "Economic policy and external debt," Series "GDP per capita (constant 2010 US$)" (accessible online at http://data.worldbank.org/indicator/NY.GDP.PCAP.KD).

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 86

- 1870–2009 — Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data–sets/.
- 2010–2020 — World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked.

**Investment-to-GDP ratio** — `iy` — pp. 86

- 1870–1913 — Mitchell, Brian (2013), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London. Capital formation (CF) / Net national product (NNP). (note that the 1873 values in Mitchell are accidentally shifted one column to the right!)
- 1920–1924 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1925–1938 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1939 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1948–1949 — van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003.
- 1950–1959 — Mitchell, Brian (2013), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London. Capital formation (CF) / Net national product (NNP).
- 1960–2020 — International Monetary Fund, International Financial Statistics. Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" (accessible online at https://data.imf.org/).
- *Note:* Pre-1960 ratio is capital formation over NNP, not GDP; gaps 1914–1919, 1940–1947. The repeated van Meerten (Belgium) citations for German interwar years look like a copy-paste error in the document.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 86

- 1870–1996 — A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
- 1997–2020 — International Monetary Fund World Economic Outlook (April 2021). Series "Inflation, average consumer prices" (accessible online at https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx). Chainlinked.

**Narrow Money (converted to billions DM)** — `narrowm` — pp. 87

- 1870–1998 — Mitchell, B. (2013). International Historical Statistics. Sum of series: Banknote circulation + Commercial bank deposits. (gaps 1914-1922 & 1939-1947).
- 1999–2020 — Sum of series Deutsche Bundesbank, Statistiken, Zeitreihen-Datenbanken, Suche in Datenbanken, type: Einlagen / täglich fällig / Deutscher Beitrag / Bestand am Monatsende and in english site type: "Banknotes in Circulation" https://www.bundesbank.de/dynamic/action/de/statistiken/zeitreihen-datenbanken/zeitreihen-datenbank/723444/723444?openNodeId=1255115&treeAnchor=EURORAUM
- *Note:* Gaps 1914–1922 and 1939–1947.

**Broad Money (converted to billions DM)** — `money` — pp. 87

- 1870–1875 — Mitchell, B. (2013). International Historical Statistics. Sum of series: Banknote circulation + Commercial bank deposits + Savings bank deposits. Chainlinked.
- 1876–1922 — Weber, Warren E. 2000. International Data. 1810-1995. Research Department, Federal Reserve Bank of Minneapolis. Series: M2. http://cdm16030.contentdm.oclc.org/cdm/singleitem/collection/p16030coll4/id/8/rec/5
- 1925–1938 — Bordo, Michael, et al. "Is the crisis problem growing more severe?." Economic policy 16.32 (2001): 51-82. M2. Note: Gap from 1914 – 1924 [as printed; gap is 1923–1924 given the Weber range].
- 1948–1954 — Sprenger, Bernd, ([2006]) Änderungen der Geldmenge in Deutschland seit 1835. GESIS Köln, Deutschland ZA8231 Datenfile Version 1.0.0. M1. www.gesis.org. Chainlinked.
- 1955–1973 — Deutsche Bundesbank, (1998 [005.]) 50 Jahre Deutsche Mark. Monetäre Statistiken von 1948 bis 1997. GESIS Köln, Deutschland ZA8186 Datenfile Version 1.0.0. M3. www.gesis.org
- 1974–1998 — International Monetary Fund (2012), eLibrary, International Financial Statistics, series M3 alternate definition. (accessible online at http://data.imf.org/).
- 1999–2020 — Deutsche Bundesbank, Statistics, search databases, type: Monetary aggregate M3 (from January 2002, excluding currency in circulation; from June 2010, excluding repos with central counterparties) / German contribution / Index / Seasonally adjusted, december value.
- *Note:* Gaps 1923–1924 and 1939–1947; 1948–1954 segment is M1 (chainlinked), later M3.

**Short-term interest rate (nominal, percent per year)** — `stir` — pp. 87, 88

- 1870–1874 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. Levels. Annual average rate.
- 1875–1879 — Neal, Larry D., and Marc D. Weidenmier. "Crises in the global economy from tulips to today." Globalization in historical perspective. University Of Chicago Press, 2003. 473-514. Open Market Rate, Monthly, End of Year Value. (accessible online at http://ebutts05.tripod.com/nealweidenmiergsd/)
- 1880–1913 — Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic policy: A European Forum 32: 51–75.
- 1914–1922 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. Levels. Annual average rate.
- 1924–1940 — Morawietz, Markus, (1994 [2009]) Rentabilität und Risiko deutscher Aktien- und Rentenanlagen 1870 – 1992. GESIS Köln, Deutschland ZA8384 Datenfile Version 1.0.0. Series: Tagesgeldsatz (interbank money market rate). December values.
- 1941–1944 — Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. Levels. Annual average rate.
- 1950–2012 — Post–WWII data from International Monetary Fund (2015), International Financial Statistics database (IFS). Section "Economic indicators", Series "Interest Rates – Money Market Rate" (accessible online at http://elibrary–data.imf.org/).
- 2012–2020 — Bundesbank. Table: "BundesbankTime series BBK01.SU0304: Money market rates / EONIA / Monthly average". 12-month average. (accessible online: http://www.bundesbank.de/Navigation/EN/Statistics/Time_series_databases/Macro_economic_time_series/its_details_value_node.html?tsId=BBK01.SU0304)
- *Note:* Gaps 1923 (hyperinflation) and 1945–1949.

**Long-term interest rate (nominal, percent per year)** — `ltrate` — pp. 88

- 1870–1879 — Clemens, Michael A., and Jeffrey G. Williamson. "Wealth bias in the first global capital market boom, 1870–1913*." The Economic Journal 114.495 (2004): 304-337.
- 1880–1913 — Flandreau and Zumer, 2004, The Making of Global Finance, Paris: OECD Development Centre.
- 1914–1921 — Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. Bank of England Staff Working Paper No. 845.
- 1924–1943 — Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. Bank of England Staff Working Paper No. 845.
- 1948–1955 — Wirtschaft und Statistik, Statistische Monatszahlen: 5% DM-Pfandbriefe per hundred parts of nominal value; calculate: (100+5-value)/value to get ltrate.
- 1956–2011 — International Monetary Fund (2019), International Financial Statistics (IFS). Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds".
- 2012–2020 — OECD (2021). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en, average of monthly values.
- *Note:* Gaps 1922–1923 and 1944–1947; 1948–1955 is a Pfandbrief (mortgage bond) yield proxy computed from prices.

**Current Account (converted to billions DM)** — `ca` — pp. 88, 89

- 1872–1938 — M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA (accessible online at http://www.nber.org/databases/jones–obstfeld/). Note: Gaps between 1914 – 1924.
- 1948–1974 — B. Mitchell (2013), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London. Series: Overall current balance (OCB).
- 1975–2020 — International Monetary Fund (2019), International Financial Statistics. Series: Supplementary Items, Current Account, Net (excluding exceptional financing), USD. (accessible online https://data.imf.org). Redenominated into DM with exchange rate from JST dataset.
- *Note:* Starts 1872; gaps 1914–1924 and 1939–1947.

**Imports & Exports (converted to billions DM)** — `imports,exports` — pp. 89

- 1872–1913 — Sensch, Jürgen, (1949-2007 [2009]) histat-Datenkompilation online: Der Außenhandel Deutschlands. Basisdaten für den Zeitraum 1830 bis 2000. GESIS Köln, Deutschland ZA8358 Datenfile Version 1.0.0. Series: "Ausfuhr insgesamt" and "Einfuhr insgesamt".
- 1924–1943 — B. Mitchell (2013), International Historical Statistics. Palgrave Macmillan, London. (Note: years 1920-1923 not taken from Mitchell, as the table says they are nominal values, but the numbers are inconsistent with high inflation in Germany.)
- 1948–2020 — International Monetary Fund, International Financial Statistics: archive, M10 2021, External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency; External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency.
- *Note:* Starts 1872; gaps 1914–1923 and 1944–1947.

**Government Revenues (converted to billions DM)** — `revenue` — pp. 89

- 1873–1915 — Statistisches Bundesamt (various), Statistische Jahrbücher für das Deutsch Reich (various issues) (accessible online at https://www.destatis.de/DE/Publikationen/StatistischesJahrbuch/StatistischesJahrbuch_AeltereAusgaben.html).
- 1925–1938 — Ritschl, Albrecht (2002), Deutschlands Krise und Konjunktur 1924–1934. Binnenkonjunktur, Auslandsverschuldung und Reparationsproblem zwischen Dawes–Plan und Transfersperre, Akademie Verlag, Berlin.
- 1950–1961 — Statistisches Bundesamt (various), Statistische Jahrbücher für die Bundesrepublik Deutschland (various issues) (accessible online at https://www.destatis.de/DE/Publikationen/StatistischesJahrbuch/StatistischesJahrbuch_AeltereAusgaben.html). Note: 1960 value originally for 9 months, value has been adjusted to reflect 12 months i.e. x1.33.
- 1962–2008 — Statistisches Bundesamt (2012), Finanzen und Steuern Rechnungsergebnisse des Öffentlichen Gesamthaushalts, Fachserie 14, Reihe 3.1. Table I "Entwicklung der Ausgaben und Einnahmen der öffentlichen Haushalte nach Arten", Serie "Bereinigte Einnahmen – Bund". (accessible online at https://www.destatis.de/DE/Publikationen/Thematisch/FinanzenSteuern/OeffentlicheHaushalte/AusgabenEinnahmen/RechnungsergebnisOeffentlicherHaushalt2140310097004.pdf?__blob=publicationFile)
- 2009–2020 — Statistisches Bundesamt (2021), Statistisches Jahrbuch 2018, Kapitel 9 Finanzen und Steuern, Tabelle 9.1.1 "Einnahmen, Ausgaben, Finanzierungssaldo und Schulden", Serie Einnahmen des Öffentlichen Gesamthaushalts – Bund.
- *Note:* Starts 1873; gaps 1916–1924, 1939–1949; federal (Bund/Reich) level; 1960 fiscal-year change adjusted x1.33.

**Government Expenditure (converted to billions DM)** — `expenditure` — pp. 89, 90

- 1873–1913 — P. Flora (1983), State Economy and Society in Western Europe 1815–1975, A Data Handbook, Vol I: The Growth of Mass Democracies and Welfare States, St James Press, Chicago.
- 1925–1938 — A. Ritschl (2002), Deutschlands Krise und Konjunktur 1924-1934. Binnenkonjunktur, Auslandsverschuldung und Reparationsproblem zwischen Dawes-Plan und Transfersperre, Akademie Verlag, Berlin.
- 1950–1961 — Statistisches Bundesamt (various), Statistische Jahrbücher für die Bundesrepublik Deutschland (various issues) (accessible online at https://www.destatis.de/DE/Publikationen/StatistischesJahrbuch/StatistischesJahrbuch_AeltereAusgaben.html). Note: 1960 value originally for 9 months, value has been adjusted to reflect 12 months i.e. x1.33.
- 1962–2008 — Statistisches Bundesamt (2012), Finanzen und Steuern Rechnungsergebnisse des Öffentlichen Gesamthaushalts, Fachserie 14, Reihe 3.1. Table I "Entwicklung der Ausgaben und Einnahmen der öffentlichen Haushalte nach Arten", Serie "Bereinigte Ausgaben – Bund". (accessible online at https://www.destatis.de/DE/Publikationen/Thematisch/FinanzenSteuern/OeffentlicheHaushalte/AusgabenEinnahmen/RechnungsergebnisOeffentlicherHaushalt2140310097004.pdf?__blob=publicationFile)
- 2009–2018 — Statistisches Bundesamt (2019), Statistisches Jahrbuch 2018, Kapitel 9 Finanzen und Steuern, Tabelle 9.1.1 "Einnahmen, Ausgaben, Finanzierungssaldo und Schulden", Serie Ausgaben des Öffentlichen Gesamthaushalts – Bund.
- 2019–2020 — Statistisches Bundesamt, Startseite. Themen. Staat. Öffentliche Finanzen. Ausgaben und Einnahmen. Tabellen. Ausgaben und Einnahmen des Öffentlichen Gesamthaushalts.
- *Note:* Starts 1873; gaps 1914–1924, 1939–1949.

**Public debt-to-GDP ratio** — `debtgdp` — pp. 90

- 1871–1991 — Rahlf, Thomas, (2015 [2015]) Zeitreihendatensatz für Deutschland, 1834-2012 GESIS Köln, Deutschland ZA8603 Datenfile. Schuldenquote (gesamte öff. Schuld / BIP), A: Zollverein/Deutsches Reich (1834-1945); B: Bundesrepublik Deutschland / alte Bundesländer; D: Deutschland seit der Wiedervereinigung. Gaps: 1914-1926; 1944-1949.
- 1992–2020 — European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt. 18.2 – Based on ESA 2010 and former definitions. Gross Public Debt (linked series) (UDGGL). Percentage of GDP at market prices (excessive deficit procedure) (data accessible online at http://ec.europa.eu/economy_finance/ameco/user/serie/SelectSerie.cfm).
- *Note:* Starts 1871; gaps 1914–1926, 1944–1949; territory changes (Reich / West Germany / unified Germany).

**USD exchange rate (local currency/USD)** — `xrusd` — pp. 90, 91

- 1870–1886 — Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. Mark / GBP*GBP / USD (contained in this dataset).
- 1887–1913 — Statistisches Jahrbuch für das dt. Reich. (various issues)
- 1914–1923 — Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1924–1940 — League of Nations. Yearbooks (various issues).
- 1941–1944 — Klovland, J. T., Chapter 7 - Historical exchange rate data 1819-2003. (December values).
- 1946–1949 — Reinhart exchange rates (official and parallel) dataset, accessible at http://www.carmenreinhart.com/data/browse-by-topic/topics/10/
- 1950–2020 — IMF eLibrary. International Financial Statistics. Exchange Rate (note Euro/USD exchange rate since 1999 translated into DM/USD rate).
- *Note:* "We assume a German mark-euro exchange rate of 1.95583 where necessary." 1945 missing.

**Peg dummy** — `peg` — pp. 91

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–1999 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 2000–2020 — set to 0 (note: deviation from Ilzetzki, Reinhart & Rogoff classification, where Germany, as a member of the Eurozone is categorized as a 1).
- *Note:* Germany is coded as NOT pegged from 2000 (euro anchor country), deliberately deviating from IRR.

**Strict peg dummy** — `peg_strict` — pp. 91

- 1870–1939 — M. Obstfeld & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
- 1940–2007 — unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1, all 2-6=0); strict peg category excluding crawling pegs. [as printed; superseded by the 2000–2020 override below]
- 2000–2020 — set to 0 (note: deviation from Ilzetzki, Reinhart & Rogoff classification, where Germany, as a member of the Eurozone is categorized as a 1).

**Exogenous monetary policy shocks** — `JSTtrilemmaIV` — pp. 91

- all — Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.

**House prices (nominal index, 1990=100)** — `hpnom` — pp. 91

- 1870–1922 & 1924–1938 & 1962–2012 — Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2013–2020 — OECD housing prices database. Nominal series. Chain-linked.
- *Note:* Gaps 1923 and 1939–1961.

**Unemployment rate (percent)** — `unemp` — pp. 92

- 1887–1919 and 1980–1982 — Mitchell, Brian (2013), International Historical Statistics Europe, 1750–2010, Table B2 Europe Unemployment, Palgrave Macmillan, London. Chainlinked (1980–1982).
- 1920–1938 and 1950–1979 — Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press.
- 1939 and 1946–1949 — Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter International Comparison of Unemployment Rates, Table 1 "Unemployment Rates, Nine Countries, 1900-1950 (per cent)". Chainlinked.
- 1983–2020 — ILOSTAT (2021), Table "Unemployment rate by sex and age" based on the EU Labour force survey (LFS) accessible online at https://ilostat.ilo.org/data/.
- *Note:* Starts 1887; gap 1940–1945.

**Wages (index, 1990=100)** — `wage` — pp. 92

- 1870–1879 and 1924–1938 — Scholliers & Zamagni (1995). "Labour's Reward: Real wages and economic change in 19th- and 20th-century Europe". Average annual wages in all sectors (including Industry, handicraft, Agriculture, forests, fishing and excluding the military). Chainlinked.
- 1880–1923 and 1939–1950 — A. Sommariva, G. Tullio (1987). "German Macroeconomic History, 1880-1979". Appendix 2, Table Wages, employment and population. Average annual wages. There's a gap for the year of 1923 due to the hyperinflation. Chainlinked.
- 1951–2020 — Bundesbank Statistik (2021). Zeitreihen-Datenbank Deutschland / Gesamtwirtschaftliche Übersicht / Arbeitnehmerentgelt (Lohnkosten) je Arbeitnehmer 1) 2) 3); BBNZ1.A.DE.N.G.0018.L. Accessible online at https://www.bundesbank.de/
- *Note:* 1923 missing (hyperinflation); from 1951 the series is compensation of employees per employee (Bundesbank), not a wage-rate index.

**Total loans to non-financial private sector (Credit Data, converted to billions DM)** — `tloans` — pp. 92

- 1870–1882 — German Time Series Database, 1834-2012. Chapter 15.2: Money and Credit - Banks, Series: Loans of all banks to non-banks. Note: loan sum refers to Zollverein/Deutsches Reich (1834-1945) territory. Chainlinked.
- 1883–1940 — Deutsche Bundesbank (1976), Deutsches Geld– und Bankwesen in Zahlen 1876–1975, Fritz Knapp GmbH, Frankfurt am Main. Table B1, Series 1.05 "Total loans of Aktienbanken, Sparkassen, Hypothekenbanken und Genossenschaftsbanken" + Table D1, Series 1.08 "Loans of Gewerbliche Kreditgenossenschaften". Includes interbank exposures.
- 1946–1947 — Statistical Annex: Report of the Military Governor, 1948, Table 2, Total - Loans and Advances - Due from other debtors - Total (including Reichsbank and Länderbanks).
- 1948–2020 — Deutsche Bundesbank (2021), Zeitreihe BBK01.PQA350: Kredite an inländische Unternehmen und Privatpersonen / insgesamt / Alle Bankengruppen. (accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.PQA350).
- *Note:* Gap 1941–1945; 1883–1940 includes interbank exposures; territorial changes (Reich → West Germany → unified Germany).

**Mortgage loans to non-financial private sector** — `tmort` — pp. 93

- 1883–1919 — calculated from Deutsche Bundesbank (1976), ibid. Table 1.02 "Hypothekenbanken", Series "Hypotheken", p60, and Table 1.05 "Sparkassen in Preußen", Series "Vom Vermögen sind zinsbar angelegt, in Hypotheken, auf städtische Grundstücke", Series "Vom Vermögen sind zinsbar angelegt, in Hypotheken, auf ländliche Grundstücke" p64.
- 1924–1940 — Deutsche Bundesbank (1976), ibid. Table 1.01 "Aktiva & passive alle Banken", Series "Langfirstige Ausleihungen, Hypothekenforderungen", p75. Note: value for 1927 is a linear interpolation.
- 1949–1967 — Deutsche Bundesbank, Monatsbericht der Deutschen Bundesbank. Table "Summe Hypothekar Kredite". December 1967, p55. https://www.bundesbank.de/Redaktion/DE/Downloads/Veroeffentlichungen/Monatsberichte/1967/1967_12_monatsbericht.pdf?__blob=publicationFile
- 1968–2020 — Deutsche Bundesbank (2021), Zeitreihe BBK01.PQ3013: Hypothekarkredite an inländische Unternehmen und Privatpersonen / insgesamt / Alle Bankengruppen. Path: Banken und andere finanzielle Institute – Banken – Aktiva und Passiva der Banken in Deutschland (ohne Deutsche Bundesbank und Geldmarktfonds) – Kredite der Banken (MFIs) an inländische Unternehmen und Privatpersonen – Kredite an inländische Unternehmen und Privatpersonen – Wohnungsbaukredite (nach Bankengruppen) – Hypothekarkredite insgesamt (accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.PQA350)
- *Note:* Starts 1883; gaps 1920–1923, 1941–1948; 1927 linearly interpolated; pre-1920 covers mortgage banks + Prussian savings banks only.

**Total Loans to Households** — `thh` — pp. 93

- 1950–2020 — Residual of Total loans to non-financial private sector and Total Loans to Business.

**Total Loans to Business** — `tbus` — pp. 93

- 1950–2020 — Deutsche Bundesbank (2021), Zeitreihe BBK01.PQ3001: Kredite an inländische Unternehmen und wirtschaftlich selbstständige Privatpersonen / insgesamt / Alle Bankengruppen. (Available online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.PQ3001)
- *Note:* Bundesbank "Unternehmen und wirtschaftlich selbstständige Privatpersonen" includes self-employed persons in business loans.

**Total Other Loans to Business (Germany; residual)** — *component* — pp. 93

- all — Residual of Mortgage loans to non-financial private sector and Mortgage Loans to Households.
- *Note:* As printed (heading "Total Other Loans to Business" defined as mortgage loans total minus mortgage loans to households, i.e. mortgage loans to business).

**Corporate Debt** — `bdebt` — pp. 93, 94

- 1885–1920 — Bundesbank (1976): loans and discounts of joint-stock banks (Aktienkreditbanken) and commercial credit unions (Genossenschaftsbanken) to non-banks proxying lending to business.
- 1924–1944 — Bundesbank (1976): loans and discounts of Großbanken and Kreditgenossenschaften.
- 1949–1990 — Deutsche Bundesbank (1983) "Revidierte Ergebnisse der gesamtwirtschaftlichen Finanzierungs- und Geldvermögensrechnung für die Jahre 1950-1959", and Deutsche Bundesbank (1994) "Ergebnisse der gesamtwirtschaftlichen Finanzierungsrechnung für Westdeutschland 1960-1992. Total private non-financial business sector liabilities less equity.
- 1991–2012 — OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2013–2018 — eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2019–2020 — bank loans to business and capital market debt from "Credit to the non-financial sector" database of the Bank of International Settlements (accessible online at https://www.bis.org/statistics/totcredit.htm).
- *Note:* Starts 1885; gaps 1921–1923, 1945–1948.

**Capital ratio = Capital / Total Assets (Bank balance sheet ratios; ratios in %, underlying data in billions DM)** — `lev` — pp. 94, 95, 96

- *Note:* Built from Total Assets and Capital components below. Pre-1924 coverage is a sum of Aktien-Kreditbanken, Hypothekenbanken and Sparkassen (Prussia before 1900, Reich after), with early years chainlinked to Burhop (2004) Kreditbanken data; gaps 1921–1923 and 1941–1949.

**Total Assets (component of lev/ltd/noncore; converted to billions DM)** — *component* — pp. 94, 95

- 1870–1878 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975, Fritz Knapp GmbH, Frankfurt am Main. Chapter D I. Table 1.02 Hypothekenbanken, series "Langfristige Ausleihungen" + Table 1.04 Sparkassen in Preußen, series "Aktivvermögen" chainlinked with Sparkassen + Aktienbanken assets chainlinked with Carsten Burhop (2004), Die Kreditbanken in der Gründerzeit, Tabelle 3, "Die Bilanzsumme der Kreditbanken".
- 1879–1880 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Aktienbanken and Hypothekenbanken chainlinked with Table 1.02 Hypothekenbanken, series "Langfristige Ausleihungen"+ Table 1.04 Sparkassen in Preußen, series "Aktivvermögen" chainlinked with Savings bank data.
- 1881–1882 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Aktienbanken "Bilanzsumme" chainlinked with series Chapter D I., Table 1.02 Hypothekenbanken "Bilanzsumme"+ Chapter D I., Table 1.02 Hypothekenbanken, series "Bilanzsumme" + Table 1.04 Sparkassen in Preußen, series "Aktivvermögen" chainlinked with Savings bank data.
- 1883–1899 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Bilanzsumme"+ Table 1.02 Hypothekenbanken, series "Bilanzsumme"+ Table 1.04 Sparkassen in Preußen, series "Aktivvermögen" chainlinked with Sparkassen im Deutschen Reich, series "Aktivvermögen".
- 1900–1920 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Bilanzsumme"+ Table 1.02 Hypothekenbanken, series "Bilanzsumme" + Table 1.04 Sparkassen im Deutschen Reich, series "Aktivvermögen". Levels.
- 1924–1940 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D II., Table 1.01 Aktiva und Passiva, Alle Banken, series "Bilanzsumme". Levels.
- 1950–2020 — Deutsche Bundesbank, Zeitreihe BBK01.OU0308: accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.OU0308). Levels.

**Capital (component of lev; converted to billions DM)** — *component* — pp. 95, 96

- 1870–1878 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I. Table 1.02 Hypothekenbanken, series "Kapital" + Table 1.04 Sparkassen in Preußen, series "Reservefonds" + Aktienbanken Capital from Carsten Burhop (2004), "Die Kreditbanken in der Gründerzeit", Tabelle 4, "Eigenkapital der Kreditbanken". Chainlinked.
- 1879–1880 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Aktienbanken capital ratio from 1883. Chapter D I., Table 1.02 Hypothekenbanken, series "Kapital". + Table 1.04 Sparkassen in Preußen, series "Reservefonds". Chainlinked.
- 1881–1882 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Aktienbanken capital ratio from 1883 + Chapter D I., Table 1.02 Hypothekenbanken, series "Kapital"+"Reserven" + Table 1.04 Sparkassen in Preußen, series "Reservefonds". Chainlinked.
- 1883–1899 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Kapital" and "Reserven"+ Table 1.02 Hypothekenbanken, series "Kapital" and "Reserven"+ Table 1.04 Sparkassen in Preußen, series "Reservefonds". Chainlinked.
- 1900–1920 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Kapital" and "Reserven"+ Table 1.02 Hypothekenbanken, series "Kapital" and "Reserven"+ Table 1.04 Sparkassen im deutschen Reich, series "Rücklagen". Levels.
- 1924–1940 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D II., Table 1.01 Aktiva und Passiva, Alle Banken, series "Grund- bzw. Geschäftskapital"+"Reserven".
- 1950–2020 — Deutsche Bundesbank, Zeitreihe BBK01.OU0322: accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.OU0322).

**Loans-to-Deposits ratio = Loans / Deposits** — `ltd` — pp. 96, 97

- *Note:* Built from Deposits and Loans components below.

**Deposits (component of ltd/noncore; converted to billions DM)** — *component* — pp. 96

- 1870–1878 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I. Table 1.02 Hypothekenbanken, series "Depositen und Kreditoren" chainlinked with growth rate of Bilanzsumme + Sparkassen in Preußen "Spareinlagen", chainlinked + Aktienbanken from Carsten Burhop (2004), "Die Kreditbanken in der Gründerzeit", Tabelle 5, "Depositen und Kontokorrenteinlagen der Kreditbanken". Chainlinked.
- 1879–1882 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Depositen und Kreditoren" (Berliner Großbanken + Provinzbanken) chainlinked with growth rate of "Bilanzsumme"+ Table 1.02 Hypothekenbanken, series "Depositen und Kreditoren" chainlinked with growth rate of Bilanzsumme + Sparkassen in Preußen "Spareinlagen", chainlinked.
- 1883–1920 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Depositen und Kreditoren" (Berliner Großbanken + Provinzbanken) + Table 1.02 Hypothekenbanken, series "Depositen und Kreditoren"+ Sparkassen im deutschen Reich "Spareinlagen" (before 1900 chainlinked with Sparkassen in Preußen). Levels.
- 1924–1940 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D II., Table 1.01 Aktiva und Passiva, Alle Banken, series "Einlagen – Nichtbanken und Auslandsbanken". Levels.
- 1950–2020 — Deutsche Bundesbank, sum of series BBK01.OU5664 and BBK01.OUA175: accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.OU5664).

**Loans (component of ltd; converted to billions DM)** — *component* — pp. 96, 97

- 1870–1878 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I. Table 1.02 Hypothekenbanken, chainlinked with "Bilanzsumme" + Aktienbanken chainlinked with Carsten Burhop (2004), "Die Kreditbanken in der Gründerzeit", Tabelle 6, "Kontokorrentkredite der Kreditbanken" + Sparkassen in Preußen "Aktivvermögen", chainlinked.
- 1879–1882 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, chainlinked with total assets + Table 1.02 Hypothekenbanken, series "Debitoren insgesamt" + Sparkassen in Preußen "Aktivvermögen", chainlinked.
- 1883–1899 — Deutsche Bundesbank (1975), Deutsches Geld– und Bankwesen in Zahlen 1876–1975. Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Debitoren insgesamt"+ "Wechsel"+ Table 1.02 Hypothekenbanken, series "Debitoren insgesamt" + Sparkassen in Preußen "Aktivvermögen", chainlinked.
- 1900–1920 — Deutsche Bundesbank (1975), Chapter D I., Table 1.01 Aktien-Kreditbanken, series "Debitoren insgesamt"+ "Wechsel"+ Table 1.02 Hypothekenbanken, series "Debitoren insgesamt" + Sparkassen im deutschen Reich "Aktivvermögen". Levels.
- 1924–1940 — Deutsche Bundesbank (1975), Chapter D II., Table 1.01 Aktiva und Passiva, Alle Banken, series "Langfristige Ausleihungen insgesamt"+"Debitoren und sonstige kürzerfristige Forderungen – Nichtbanken zusammen".
- 1950–2020 — Deutsche Bundesbank. Zeitreihe BBK01.PQA350: Kredite an inländische Unternehmen und Privatpersonen / insgesamt / Alle Bankengruppen. (accessible online at http://www.bundesbank.de/Navigation/DE/Statistiken/Zeitreihen_Datenbanken/Makrooekonomische_Zeitreihen/its_details_value_node.html?tsId=BBK01.PQA350).

**Noncore ratio = (Total Assets-Capital - Deposits ) / (Total Assets - Capital)** — `noncore` — pp. 97

- *Note:* Formula only.

### Ireland (IRL) — "Data in millions IEP" — PDF pp. 97–104 (section continues beyond p. 100)

**Population** — `pop` — pp. 97

- 1921–1949 — Bolt, J., Inklaar, R., de Jong, H., & Van Zanden, J. L. (2018), Rebasing 'Maddison': new income comparisons and the shape of long-run economic development, Maddison Project Working Paper 10.
- 1950–2020 — Central Statistics Office (2021), Table PEA01, "Population Estimates".
- *Note:* Ireland data start in 1921/1922 (independence), not 1870.

**GDP (converted to millions IEP)** — `gdp` — pp. 98

- 1922–1969 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1).
- 1970–1994 — Central Statistics Office (2019), Historical National Income & Expenditure accounts. Table NAH05 T05, Expenditure on Gross National Income (excluding FSIM) at Current Market Prices. Chainlinked.
- 1995–2020 — Central Statistics Office (2021), National Income and Expenditure Annual Results 2021, Table N1805 T05.
- *Note:* From 1970 the Irish "GDP" series is actually Gross National Income (expenditure on GNI, excluding FISIM) at current market prices, per the cited CSO tables.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — `rgdpmad` — pp. 98

- 1980–2020 — International Monetary Fund (2021). World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Note: The series is projected backwards to 1922 using the growth-rates of the real GDP per capita series described in the following subsection. Converted to 1990 Int$ using the US Consumer Price Index described in the relevant chapter.
- *Note:* Not Maddison-sourced for Ireland: IMF WEO PPP per capita, back-cast to 1922 with rgdpbarro growth rates and deflated to 1990 Int$ with the US CPI.

**Real GDP per capita (index, 2005=100)** — `rgdpbarro` — pp. 98

- 1922–1969 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1).
- 1970–1994 — Central Statistics Office (2019), Historical National Income & Expenditure accounts (NAH05 T05). Chainlinked.
- 1995–2020 — Central Statistics Office (2021), National Income and Expenditure Annual Results 2018, Table N1805 T05.
- *Note:* Not Barro–Ursúa-sourced for Ireland.

**Real consumption per capita (index, 2006=100)** — `rconsbarro` — pp. 98, 99

- 1938–1946 — Fitzgerald & Kenny (2019), 'Managing a Century of Debt', Journal of Statistical & Social Inquiry Society of Ireland, Vol.48, pp. 1-40. Chainlinked.
- 1947–1957 — Central Statistics Office (1973), "National Income and Expenditure, 1969". Chainlinked.
- 1958–1969 — Central Statistics Office (1979), "National Income and Expenditure, 1977". Table B.12. Chainlinked.
- 1970–1994 — Central Statistics Office (2019), Historical National Accounts, Table NAH06 T06, "Expenditure on Gross National Income (excluding FISIM) at Constant Market Prices". Chainlinked.
- 1995–2020 — Central Statistics Office (2021), National Income and Expenditure Annual Results 2018, Table N1806 T06, "Expenditure on Gross National Income at Constant Market Prices". Chainlinked.
- *Note:* Starts 1938.

**Investment-to-GDP ratio** — `iy` — pp. 99

- 1944–1946 — McCarthy et al (1952), 'Symposium on national income and social accounts', Journal of the Statistical and Social Inquiry Society of Ireland, 28(5), pp. 473-514. Chainlinked.
- 1947–1959 — Central Statistics Office (1964), "National Income and Expenditure", Tables A.3, A.6, B.3 and B.6.
- 1960–1969 — Central Statistics Office (1975), "National Income and Expenditure", Tables B.5 and B.9.
- 1995–2020 — Central Statistics Office, T11. Savings and Capital Formation, Gross total available for investment in domestic capital formation - ESA code (P.5), yearly.
- *Note:* Starts 1944; no source listed for 1970–1994 as printed.

**Consumer prices (index, 1990=100)** — `cpi` — pp. 99

- 1922–2020 — Central Statistics Office (2021), Table CPM02, "Consumer Price Index". Rebased to 1990 = 100.

**Narrow Money (converted to millions IEP)** — `narrowm` — pp. 99

- 1922–2002 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1). Chainlinked.
- 2003–2020 — Central Bank of Ireland, Table A.3 Money Supply - Irish Contribution to Euro Area, outstanding amount, M1 end of year value.

**Broad Money (converted to millions IEP)** — `money` — pp. 99

- 1922–2002 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1). Chainlinked.
- 2003–2020 — Central Bank of Ireland, Table A.3 Money Supply - Irish Contribution to Euro Area, outstanding amount, M2 end of year value.

**Short-term interest rates (nominal, percent per year)** — `stir` — pp. 99, 100

- 1920–1984 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1). Series uses the updated dataset of this publication extending short-term interest rates to 1920 – 1922.
- 1985–2020 — OECD (2021). OECD iLibrary. Short-term interest rates doi: 10.1787/2cc37d77-en

**Long-term interest rates (nominal, percent per year)** — `ltrate` — pp. 100

- 1922–1923 — Gerlach & Stuart (2015), 'Money, Interest Rates and Prices in Ireland, 1933-2012', Irish Economic and Social History, 42(1).
- 1924–1970 — Fitzgerald & Kenny (2019), 'Managing a Century of Debt', Journal of Statistical & Social Inquiry Society of Ireland, Vol.48, pp. 1-40.
- 1971–2020 — OECD (2021). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en

**Current Account (converted to millions IEP)** — `ca` — pp. 100

- 1938–2017 — Fitzgerald & Kenny (2019), 'Managing a Century of Debt', Journal of Statistical & Social Inquiry Society of Ireland, Vol.48, pp. 1-40.
- 2018–2020 — Central Statistics Office (2021). Irish Statistical Survey. Table 9, Net balance on current account.
- *Note:* Starts 1938.

**Imports & Exports (converted to millions IEP)** — `imports,exports` — pp. 100

- 1937–1946 — Central Statistics Office (1955). Irish Statistical Survey. Table 9.
- 1947–1958 — Central Statistics Office (1973), "National Income and Expenditure, 1969". Chainlinked.
- 1958–1969 — Central Statistics Office (1979), "National Income and Expenditure, 1977". Table B.12. Chainlinked.
- 1970–1994 — Central Statistics Office (2020), Historical National Accounts, Table NAH05 T05. Expenditure on Gross National Income. Chainlinked.
- 1995–2020 — Central Statistics Office (2021), N2005, T05 Expenditure on Gross and Net National Income at Current Market Prices, Exports of goods and services (excluding factor income flows).
- *Note:* Starts 1937; from 1947 these are national-accounts exports/imports of goods and services, not customs merchandise trade.

**Government Revenues (converted to millions IEP)** — `revenue` — pp. 100

- 1938 and 1944–1946 — McCarthy et al (1952), 'Symposium on national income and social accounts', Journal of the Statistical and Social Inquiry Society of Ireland, 28(5), pp. 473-514.
- 1947–1959 — Central Statistics Office (1964), "National Income and Expenditure", Tables A.3, A.6, B.3 and B.6.
- 1960–1969 — Central Statistics Office (1975), "National Income and Expenditure", Tables B.5 and B.9.
- *Note:* Entry continues on PDF page 101 (outside the assigned range: 1970 onward not captured here).

---

## (e) Release-6 changes (what is new vs R5)

Not covered in pp. 1–100. The only release-related statements in this range are:

- the title page: "JSTDatasetR6 / Release 6 / July 2022" (p. 1), with every series documented through 2020;
- the label table: `crisisJST` — "included since R5"; `crisisJST_old` — "as coded in all prior releases (R1 – R4)" (p. 6);
- the terms of use still cite "The Rate of Return on Everything, 1870–2015" as "Forthcoming" (p. 2).

There is no changelog, no "what's new" section, and the table of contents (pp. 8–20) lists no such section anywhere in the 201 pages. Whether Ireland (which has its own chapter with a "Capital returns" block and data starting 1921/22) or any other feature is new in R6 is not stated in these pages.

## (f) Pages in range that could not be read, or that are figures only

None were unreadable. All 100 pages rendered legibly as text. Pages without variable content:

- p. 1 — title page only.
- p. 2 — terms of use and licence (contains the three CC licence icons; otherwise text).
- pp. 3–5 — acknowledgements (p. 5 is mostly blank; its last line is the heading "VARIABLE NAMES AND DESCRIPTIVE LABELS IN STATA").
- pp. 6–7 — the Stata label table (p. 7 is two-thirds blank).
- pp. 8–20 — table of contents.

No page in the range is a chart or figure.

## (g) Document quirks and apparent errors noticed (for the user's check against the PDF)

These are things the document itself says, or evident slips, that affect how a data dictionary should read them:

1. **Copy-paste citations.** "van Meerten, Michelangelo. Capital formation in Belgium, 1900-1995. Leuven University Press, 2003" is cited for the investment ratio of **Canada** (1946–47), **France** (1920–24) and **Germany** (1920–24, 1925–38, 1939, 1948–49) — a Belgian source for non-Belgian series (pp. 43, 72, 86). The Finland exchange-rate note reads "We assume a Belgian franc-euro exchange rate of 5.94573" (p. 66); 5.94573 is the markka rate. Denmark's government **expenditure** 1972–94 cites the Statbank **taxation** table SKAT (p. 56). Canada's unemployment 1938–54 cites Mitchell's *Europe* volume (p. 47).
2. **Typos in year ranges.** Denmark population "20018 – 2020" (p. 53); Finland wages "11870 - 1947" (p. 67); France strict peg "1940 – 2020" for the IRR-2004 source, with a separate 2008–2020 line (p. 76); Australia population 2009–2017 then 2019–2020 (2018 skipped, p. 21); France mortgage loans lists 1870–1898 twice (p. 79) and the 1975–76 CNC report is dated "(1974)" (p. 80).
3. **Overlapping source ranges left unresolved.** Belgium investment ratio: IFS 1953–2014 and NBB 1980–2020 both listed (p. 33); Belgium short rate: Drappier 1920–2014 and Belgostat 1991–2020 (p. 34); Denmark trade: Mitchell 1870–1953 and IFS 1948–2020 (p. 55); Australia broad money 1979–2013 and 2013–2020 (pp. 22–23); Germany short rate 1950–2012 and 2012–2020 (p. 88).
4. **Deliberate deviations and definitions.** Germany `peg`/`peg_strict` set to 0 for 2000–2020 against IRR (p. 91). France `debtgdp` "Data for 1880 – 1979 is for central government debt only" (p. 75). Belgium `ca` pre-1947 "is set equal to the trade balance" (p. 35). Belgium wartime CPI is an implicit deflator from stock indices (p. 33). Australia `tbus` from 2013 is gross of bad-debt provisions and includes non-private borrowers "for reasons of series consistency across time" (p. 28). Canada mortgage loans: 2011 IFRS consolidation break avoided by extending 1990–2010 with the growth of an IFRS-unaffected aggregate (p. 49). Finland capital 1990/91 interpolated because banks could transfer 90% of loan-loss reserves to reserve funds in 1990 (p. 70). Germany 1960 revenue/expenditure ×1.33 for a nine-month fiscal year (pp. 89–90); Mitchell's 1873 German capital-formation values "accidentally shifted one column to the right" (p. 86); German trade 1920–23 excluded as inconsistent with hyperinflation (p. 89).
5. **Ireland is different.** Data begin 1921/1922, `rgdpmad` is IMF WEO PPP GDP per capita back-cast with Irish real-GDP growth and deflated with the US CPI (p. 98), `gdp` from 1970 is expenditure on Gross National Income (excl. FISIM) (p. 98), trade from 1947 is national-accounts goods and services (p. 100), and the chapter has no `unemp`/`wage` items and no bank-ratio block (TOC p. 13).
6. **Column-name mapping gaps.** The country chapters use descriptive headings, not column names; the mapping to `JSTtrilemmaIV` ("Exogenous monetary policy shocks"), `lev`/`ltd`/`noncore` ("Capital ratio", "Loans-to-Deposits ratio", "Noncore ratio") and `bdebt` ("Corporate debt") is by the label table. Nothing in pp. 1–100 documents `crisisJST`, `crisisJST_old`, `peg_type`, `peg_base` or any of the 19 return variables beyond their labels.

## Range boundary

This part ends at the bottom of PDF p. 100, inside the Ireland chapter's "Government Revenues (converted to millions IEP)" item (segments through 1960–1969 captured; the 1970–2020 segment, Government Expenditure, Public debt, USD exchange rate, Peg variables, House prices, Credit data and Capital returns for Ireland are on pp. 101–105, in the next part).


# JST Macrohistory Database, Release 6 — Documentation extraction, PDF pages 101–201

Source: `JST_documentationR6.pdf` (Jordà–Schularick–Taylor Macrohistory Database, release 6 documentation), pages 101–201 of 201. All page numbers below are the printed PDF page numbers (which coincide with the PDF page index in this file).

**Where this range starts:** mid-section. Page 101 opens inside the **IRELAND** chapter, in the middle of the "Government Revenues" source list (the entry for 1970–1975 is the first line on the page; the earlier Ireland revenue entries, and all Ireland macro/money/interest-rate sections, are on pages before 101 and are not in this range). The Ireland chapter continues through page 103 (Corporate Debt). Ireland has **no** "Bank balance sheet ratios" block in this range — the chapter ends at Corporate Debt and ITALY begins at the top of page 104.

**Where this range ends:** page 201 is the final page of the document; it holds only the USA "Noncore ratios" heading and formula. There is **no bibliography / reference list** in pages 101–201 and **no release-notes / "changes in Release 6" section** in this range — the document ends with the per-country source appendix. The references list in section (e) below is therefore a consolidated list of the citations that appear within these pages (they are transcribed as they appear in the source entries), not a transcription of a bibliography section.

Countries covered in this range (chapter start page): Ireland (continued, 101–103), Italy (104–113), Japan (113–124), Netherlands (124–134), Norway (134–143), Portugal (143–154), Spain (154–164), Sweden (164–172), Switzerland (172–182), United Kingdom (182–192), United States of America (192–201).

---

## (a) General construction principles and variable definitions appearing in this range

The per-country chapters in this range all follow the same template; the following definitional statements are given repeatedly (once per country) and are transcribed here once.

1. **Chapter unit statements.** Each chapter opens with a unit line: Italy "(Data in billions ITL)"; Japan "(Data in trillions JPY)"; Netherlands "(Data in millions NLG)"; Norway "(Data in millions NOK)"; Portugal "(Data in millions PTE)"; Spain "(Data in millions ESP)"; Sweden "(Data in millions SEK)"; Switzerland "(Data in millions CHF)"; United Kingdom "(Data in billions GBP)"; United States "(Data in billions USD)". Ireland's credit data block says "(converted to millions IEP)". Nominal level series (GDP, money, current account, imports/exports, government revenue/expenditure, credit, bank balance-sheet underlying data) are expressed in these units; section headings for euro-area countries say "converted to" the legacy currency.

2. **Legacy-currency / euro conversion rates ("Note: We assume ... where necessary").** Ireland: punt–euro 0.787564 (p.102). Italy: lira–euro 1936.27 (p.108). Netherlands: guilder–euro 2.20371 (p.130). Portugal: escudo–euro 200.482 (p.148; the text literally reads "We assume a Italian Portugese escudo-euro exchange rate of 200.482", an evident copy-paste slip). Spain: peseta–euro 166.386 (p.158; text literally reads "We assume a Italian Spanish peseta-euro exchange rate of 166.386"). These rates are used to convert post-1999 euro-denominated source data back into the legacy currency.

3. **Variable headings as they appear (with units in the heading).** Within "Macro Data": Population; GDP (in national units); Real GDP per capita (PPP, 1990 Int$, Maddison); Real GDP per capita (index, 2005=100); Real consumption per capita (index, 2006=100); Investment-to-GDP ratio; Consumer prices (index, 1990=100); Narrow Money; Broad Money; Short–term interest rate (nominal, percent per year); Long–term interest rate (nominal, percent per year); Current Account; Imports & Exports; Government Revenues; Government Expenditure; Public debt-to-GDP ratio; USD exchange rate (local currency/USD); Peg dummy; Strict peg dummy; Exogenous monetary policy shocks; House prices (nominal index, 1990=100); Unemployment rate (percent); Wages (index, 1990=100). Within "Credit Data": Total loans to non-financial private sector; Mortgage loans to non-financial private sector; Total Loans to Households; Total Loans to Business; (country-specific extras: Mortgage loans to business (NLD, NOR); Loans to Households Secured by Real Estate (NOR, SWE, USA); Other Loans to Households (USA)); Corporate Debt. Within "Bank balance sheet ratios" "(Ratios in %, underlying data in [units])": Capital ratio (with underlying Total Assets and Capital); Loans-to-Deposits ratio (with underlying Deposits and Loans); Noncore ratio.

   Mapping to dataset columns (the documentation in this range does not print column names; the mapping below follows the heading semantics and the column list of the dataset): Population → `pop`; GDP → `gdp`; Real GDP per capita (PPP, 1990 Int$, Maddison) → `rgdpmad`; Real GDP per capita (index, 2005=100) → `rgdpbarro`; Real consumption per capita (index, 2006=100) → `rconsbarro`; Investment-to-GDP ratio → `iy`; Consumer prices → `cpi`; Narrow Money → `narrowm`; Broad Money → `money`; Short-term interest rate → `stir`; Long-term interest rate → `ltrate`; Current Account → `ca`; Imports & Exports → `imports`, `exports`; Government Revenues → `revenue`; Government Expenditure → `expenditure`; Public debt-to-GDP ratio → `debtgdp`; USD exchange rate → `xrusd`; Peg dummy → `peg`; Strict peg dummy → `peg_strict` (Ireland's text also names "Peg type" → `peg_type` and "Peg Base" → `peg_base`); Exogenous monetary policy shocks → `JSTtrilemmaIV`; House prices → `hpnom`; Unemployment rate → `unemp`; Wages → `wage`; Total loans to non-financial private sector → `tloans`; Mortgage loans to non-financial private sector → `tmort`; Total Loans to Households → `thh`; Total Loans to Business → `tbus`; Corporate Debt → `bdebt`; Capital ratio → `lev`; Loans-to-Deposits ratio → `ltd`; Noncore ratio → `noncore`. Crisis dummies and the return series (`eq_tr`, `housing_tr`, `bond_tr`, `bill_rate`, `rent_ipolated`, `housing_capgain*`, `housing_rent_*`, `eq_capgain*`, `eq_dp*`, `eq_tr_interp`, `bond_rate`, `eq_div_rtn`, `capital_tr`, `risky_tr`, `safe_tr`), `ifs`, `iso`, `peg_type`, `peg_base` (except Ireland's mention) and `crisisJST`/`crisisJST_old` are **not** documented anywhere in pages 101–201.

4. **Bank balance-sheet ratio formulas** (printed verbatim in every chapter):
   - *Capital ratio = Capital / Total Assets*
   - *Loans-to-Deposits ratio = Loans / Deposits*
   - *Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — for Italy, Japan, Netherlands, Portugal, Spain, Sweden, Switzerland, UK, USA. **Norway is the exception**: *Noncore ratio = Other liabilities / (Total Assets − Capital)* (p.143).
   - UK Noncore: "1880-1945 Not computed: No distinction between deposits and other liabilities in balance sheet data ('Deposits and other accounts' item in D. Sheppard (1971) ...)" (p.192).

5. **Peg dummy coding (identical text in every chapter except Ireland and Switzerland).**
   - Peg dummy: 1870–1939 from M. Obstfeld & A. Taylor (2003), "Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31", Economic Journal, 113, p1–35. 1940–2007 from unpublished, revised version of E. Ilzetzki, C. Reinhart & K. Rogoff (2004), "Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?", Working Paper (accessible online at http://personal.lse.ac.uk/ilzetzki/IRRBack.htm). (1=1-2, all 3-6=0); broad peg category including crawling pegs. 2008–2020 extension of E. Ilzetzki, C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme (1=1-2, all 3-6=0); broad peg category including crawling pegs.
   - Strict peg dummy: same sources; coding (1=1, all 2-6=0); strict peg category excluding crawling pegs.
   - Switzerland deviates: Ilzetzki–Reinhart–Rogoff (2004) used only 1940–1980; 1981–2020 from E. Ilzetzki, C. Reinhart & K. Rogoff (2017), "The Country Chronologies to Exchange Rate Arrangements into the 21st Century: Will the Anchor Currency Hold?" (Peg: "De facto peg and de facto moving band = 1"; Strict peg: "De facto peg = 1") (pp.177–178).
   - Ireland deviates: see Ireland section (rule-based coding, p.102).

6. **Exogenous monetary policy shocks (identical text in every chapter).** "Exogenous variation in the short-term interest rate from Òscar Jordà, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. 'Global financial cycles and risk premiums'. IMF Economic Review, Volume 67 Number 1, pp. 109-150, which uses the identification strategy using local projection with instrumental variables laid out in Òscar Jordà, Moritz Schularick and Alan M. Taylor, 2020. 'The effects of quasi-random monetary experiments'. Journal of Monetary Economics 112: 22-40."

7. **Recurring splicing vocabulary.** Entries are tagged "Level(s)" (source values used as-is), "Chainlinked"/"Chain-linked" (source growth rates applied to the adjacent segment's level), "growth rate calculated from ..." (same), "residual of X and Y" (X − Y), "sum of ...", and "(gap ...)"/"(note: no data for ...)" for missing years. Several current-account entries derive the level as "% of GDP × nominal GDP = Current Account" from the IMF WEO; several public-debt entries are "divided by GDP from JST dataset"; several USD-cross-rate entries for 1870–1880/1914 are the local-currency/GBP rate multiplied by the GBP/USD rate from the UK chapter.

8. **Common cross-country source blocks (verbatim forms).**
   - Population: "Angus Maddison Database (2008), ibid. Table 1 'Population levels, 1AD–2030AD' (accessible online at http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls)" then IMF World Economic Outlook growth rates, Subject "People – population" (base year 2008, or 2009/2011 as stated).
   - Real GDP per capita (PPP, 1990 Int$, Maddison): "1870 – 2010 from The Maddison-Project, http://www.ggdc.net/maddison/maddison-project/home.htm, 2013 version. Level. 2011 – 2020 from International Monetary Fund. World Economic Outlook. Series: Gross domestic product based on purchasing-power-parity (PPP) per capita GDP. Chain-linked."
   - Real GDP per capita (index, 2005=100): "1870 – 2004 from R. Barro & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA (accessible online at http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data). 2005 – 2020 growth rate calculated from World Bank (2018/2019/2021), Category 'Economic policy and external debt,' Series 'GDP per capita (constant 2010 US$)' (http://data.worldbank.org/indicator/NY.GDP.PCAP.KD)."
   - Real consumption per capita (index, 2006=100): "1870 – 2009 from Robert C. Barro and José F. Ursúa (2010), Barro–Ursúa Macroeconomic Data. For respective sources see original data set: http://rbarro.com/data–sets/. 2010 – 2020 from World Bank household final consumption expenditure per capita (constant 2010 US$). Chain linked."
   - Consumer prices (index, 1990=100): A. Taylor (2002), "A Century of Purchasing–Power Parity", Review of Economics and Statistics, vol 84(1), pp. 139–150 to 1996; then IMF World Economic Outlook, Series "Inflation, average consumer prices" (https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx), chainlinked.
   - Long-term rate pre-1913: "sum of 'Yield on consols' (from Bank of England, Three centuries of macroeconomic data, Series: Yield on consols) and 'Spread on consols' (from Clemens, M. A. and Williamson, J. G. (2004). Wealth bias in the first global capital market boom, 1870–1913. The Economic Journal.)"; later segments from IMF IFS "Government Bonds" and OECD (2020/2021) OECD iLibrary, Long-term interest rates doi: 10.1787/662d712c-en.
   - Imports & Exports, recent: "International Monetary Fund, International Financial Statistics: archive, M10 2021, External Trade, Goods, Value of Exports, Free on Board (FOB), Domestic Currency; External trade, Imports, Goods, Value, Cost, Insurance freight, Domestic Currency."
   - Government revenue/expenditure, recent: "OECD, OECD.Stat. Database 'OECD national accounts statistics,' Dataset 'General government accounts,' Table 12 'Government deficit/surplus, revenue, expenditure, and main aggregates,' Sector GS1311 'Central government,' Measure 'National currency, current prices,' Series GTR 'Total general government revenue'" / "Series GTE 'Total general government expenditure'".
   - Public debt, recent (European countries): "European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt.18.2 – Based on ESA 2010 and former definitions. Gross Public Debt (linked series) (UDGGL). Percentage of GDP at market prices (excessive deficit procedure) (http://ec.europa.eu/economy_finance/ameco/user/serie/SelectSerie.cfm)."
   - USD exchange rate: Denzel, M.A. (2010), Handbook of World Exchange Rates, 1590-1914 (early); Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015 (http://www.measuringworth.com/exchangeglobal/); Bordo, M. D. & Jonung, L. (1996) "Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud" (WWII years); Reinhart, C. M. & Rogoff, K. S. (2010) "From financial crash to debt crisis", (Black) market exchange rate (post-war years); then IMF IFS "Nominal Exchange Rate (domestic currency / US Dollar) (end of period)".
   - House prices: Knoll et al. (2014), "No price like home: Global house prices, 1870-2012", year average values; then "OECD housing prices database. Nominal series. Chain-linked." (or "Rebased 1990=100" where the OECD series is the only source).
   - Unemployment: Mitchell, Brian (2013), International Historical Statistics, Table B2 (Europe/Asia/North America) Unemployment, chainlinked; then ILOSTAT (2020/2021), Table "Unemployment rate by sex and age (%) - Annual" based on the (EU) Labour force survey (https://ilostat.ilo.org/data/).
   - Wages: International Historical Statistics (Labour Force – Money/Wages) chainlinked; "International Monetary Fund International Financial Statistics database (IFS). Labor Markets, Wage Rates, Index" chainlinked; "1990 - 2020 OECD. OECD statistics. Average annual wages. Current prices. Levels. (http://stats.oecd.org/)".
   - Corporate Debt (all countries): a mix of (i) Karsten Müller (2018) "Credit Markets around the World, 1910–2014", SSRN (https://ssrn.com/abstract=3259636); (ii) "bank loans to business and capital market debt from 'Credit to the non-financial sector' database of the Bank of International Settlements (https://www.bis.org/statistics/totcredit.htm)"; (iii) "OECD financial accounts data on total non-equity liabilities of the private non-financial business sector"; (iv) "eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector"; (v) country-specific historical sources.

---

## (b)/(c) Variable-by-variable and country-by-country source lists

Because this part of the documentation is organised country by country, sections (b) and (c) are merged: for each country, every variable is listed with its label, units, construction notes, and sources with years, with the page numbers where the entry appears. Verbatim citations are kept; editorial notes of mine are marked "[note]".

### IRELAND (ISO IRL) — continued from before p.101; pages 101–103

[note] The chapter's unit line and the macro sections before "Government Revenues" are outside this range. Credit data heading says "(converted to millions IEP)" (p.102).

**Government Revenues** (`revenue`) — tail of list, p.101
- 1970–1975: Central Statistics Office (1975), "National Income and Expenditure", Tables A.5 and A.9.
- 1976–1980: Central Statistics Office (1982), "National Income and Expenditure", Tables A.5 and A.9.
- 1981–1995: Central Statistics Office (2020), "Historical National Income and Expenditure Tables", Tables 5, 9 and 10.
- 1996–2020: Central Statistics Office (2021), "National Income and Expenditure 2018", Tables 5 and 10.

**Government Expenditure** (`expenditure`) — p.101
- 1938 and 1944–1946: McCarthy et al. (1952), 'Symposium on national income and social accounts', Journal of the Statistical and Social Inquiry Society of Ireland, 28(5), pp. 473-514.
- 1947–1959: Central Statistics Office (1964), "National Income and Expenditure", Tables A.3, A.6, B.3 and B.6.
- 1960–1969: Central Statistics Office (1975), "National Income and Expenditure", Tables B.5 and B.9.
- 1970–1975: Central Statistics Office (1975), "National Income and Expenditure", Tables A.5 and A.9.
- 1976–1980: Central Statistics Office (1982), "National Income and Expenditure", Tables A.5 and A.9.
- 1981–1995: Central Statistics Office (2020), "Historical National Income and Expenditure Tables", Tables 5, 9 and 10.
- 1996–2020: Central Statistics Office (2021), "National Income and Expenditure 2021", Tables 5 and 10.

**Public debt-to-GDP ratio** (`debtgdp`) — p.101
- 1922–1999: Fitzgerald & Kenny (2019), 'Managing a Century of Debt', Journal of Statistical & Social Inquiry Society of Ireland, Vol.48, pp. 1-40.
- 2000–2020: Central Statistics Office, National Accounts. Table GFA02 "General Government Gross and Net Debt (ESA2010)". Gross General Government Debt (EDP face value) – Gross General Government Debt – ESA2010 Code (GGDebt). Divided by gross domestic product at current market prices from the National Accounts table.

**USD exchange rate (local currency/USD)** (`xrusd`) — p.102
- 1920–1978: Prior to 1979 the Irish punt was pegged at a fixed rate to the UK pound sterling; the series for this period is derived from the UK exchange-rate series (sources in the UK chapter).
- 1979–2020: OECD (2021), Exchange rates (indicator). doi: 10.1787/037ed317-en.
- Note: punt–euro exchange rate of 0.787564 assumed where necessary.

**Peg variables** (`peg`, `peg_strict`, `peg_type`, `peg_base`) — p.102 (rule-based, not source-based)
- Throughout 1920–2019 "Peg" = 1 and "Peg type" = "Peg". "Strict Peg" = 1 for all years except 1979–1998. "Peg Base" = GBR until 1951, USA for 1952–1978, DEU thereafter. The changes reflect: (1) the Bretton Woods coding, where sterling is classified as a strict peg with the USA as base from 1951; (2) the ERM from 1979 — a peg (but not strict) with DEU as base, 1979–1998; (3) the eurozone from 1999 — strict peg with DEU as base.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.102
- 1945–1995: Keely & Lyons (2020), "Housing Prices, Yields and Credit Conditions in Dublin since 1945", The Journal of Real Estate Finance and Economics, pp. 1-36. Chainlinked.
- 1996–2004: extended back using calculated year-on-year growth in Q4 figures from the ESRI/Permanent TSB index.
- 2005–2020: Central Statistics Office (2021), Table HPM06 "Residential Property Price Index". National – All Residential Properties. End-of-year figures.

**Credit data (converted to millions IEP)**

**Total loans to non-financial private sector** (`tloans`) — p.102
- 1932–2002: Stuart, R. (2017), '70 years of personal disposable income and consumption in Ireland', Journal of the Statistical and Social Inquiry Society of Ireland, Vol.46, pp.47-70. Chainlinked using private sector credit growth.
- 2003–2020: Central Bank of Ireland (2021), Bank Balance Sheets Data. Table A.5 "Loans to Irish Private Sector – Sector & Maturity", and Table A.5.1 "Loans to Irish Households – Purpose & Maturity". End-of-year figures. Only lending to households and non-financial corporations is used; lending to insurance corporations and pension funds, and to other financial intermediaries, is excluded.

**Mortgage loans to non-financial private sector** (`tmort`) — p.103
- 1959–2002: Stuart, R. (2017), ibid. Using annual growth in sectoral lending excluding securitized lending for 1971–2003; and lending by building societies for 1959–1971.
- 2003–2020: Central Statistics Office (2021), Bank Balance Sheets Data. Table A.5.1 "Loans to Irish Households – Purpose & Maturity". Lending for housing purchases, all durations. Caveat (verbatim): "These figures exclude securitized loans and so are best considered a measure of banking sector exposure rather than household exposure".

**Total loans to households** (`thh`) — p.103
- 1948–2002: Stuart, R. (2017), ibid. Note: the CSO (2020) series in 2003 is projected backwards using growth rates of loans to households excluding securitized loans as reported in Stuart (2017). No overlapping data exist for 1968: the average of the 1967 and 1969 growth rates is used for 1968. A gap in 1970 is filled by linear interpolation between 1969 and 1971.
- 2003–2020: Central Statistics Office (2021), Bank Balance Sheets Data. Table A.5 "Loans to Irish Private Sector – Sector & Maturity". Households. End-of-year figures.

**Total loans to business** (`tbus`) — p.103
- 1959–2002: Stuart, R. (2017), ibid. Note: the CSO (2020) series in 2003 is projected backwards using growth rates of total private-sector lending excluding personal-sector lending, lending to government authorities, non-bank financial corporations and lending to schools, hospitals etc., as reported in Stuart (2017). The classification of lending to "property companies" changes between 1968 and 1969.
- 2003–2020: Central Bank of Ireland (2021), Bank Balance Sheets Data. Table A.5 "Loans to Irish Private Sector – Sector & Maturity". Non-financial corporations. End-of-year figures.

**Corporate Debt** (`bdebt`) — p.103
- 1932–2002: Rebecca Stuart (2017) "70 years of personal disposable income and consumption in Ireland", Journal of the Statistical and Social Inquiry Society of Ireland, Vol.46, pp.47-70 and sources cited therein: bank lending to business.
- 2003–2018: Central Bank of Ireland's online Bank Balance Sheets Data, Table A.5 "Loans to the Irish Private Sector", credit to the private non-financial business sector. [note: ends 2018, not 2020.]

[note] No bank balance-sheet ratio block (Capital ratio / LtD / Noncore) is printed for Ireland in this range.

### ITALY (ISO ITA) — pages 104–113. "(Data in billions ITL)"

**Population** (`pop`) — p.104
- 1870–2008: Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD" (http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls).
- 2009–2020: growth rates from IMF World Economic Outlook, Subject "People – population" (base year 2008).

**GDP (converted to billions ITL)** (`gdp`) — p.104
- 1870–1998: Baffigi, Alberto (2011), Italian National Accounts, 1861–2011, Quaderni di Storia Economica, Number 18 – October 2011. Level.
- 1999–2020: IMF (2021), International Financial Statistics, Data Report "Economic indicators", Series "Gross domestic product (in millions) – GDP nominal" (https://data.imf.org/). Level.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** (`rgdpmad`) — p.104: standard block (Maddison-Project 2013 version 1870–2010, level; IMF WEO PPP per capita GDP 2011–2020, chain-linked).

**Real GDP per capita (index, 2005=100)** (`rgdpbarro`) — p.104: standard block (Barro & Ursúa 2010 for 1870–2004; World Bank (2021) NY.GDP.PCAP.KD growth rates 2005–2020).

**Real consumption per capita (index, 2006=100)** (`rconsbarro`) — p.104: Barro–Ursúa (2010) 1870–2009; World Bank household final consumption expenditure per capita (constant 2010 US$) 2010–2020, chain linked.

**Investment-to-GDP ratio** (`iy`) — p.105
- 1870–2007: Baffigi, Alberto (2011), Italian National Accounts, 1861–2011, Quaderni di Storia Economica No. 18. Column: fixed investment, divided by GDP series from same source.
- 2008–2020: IMF (2021), IFS, Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal" (https://data.imf.org/), divided by GDP from same source.

**Consumer prices (index, 1990=100)** (`cpi`) — p.105
- 1870–1996: A. Taylor (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
- 1997–2020: IMF World Economic Outlook (April 2021), Series "Inflation, average consumer prices". Chainlinked.

**Narrow Money (converted to billions ITL)** (`narrowm`) — p.105
- 1870–1949: Fratianni, M. and F. Spinelli, A Monetary History of Italy, Cambridge 1997, p. 50. Sum of columns bp and be.
- 1950–1997: Bank of Italy, Statistical Database, Historical Tables – Monetary and Financial Indicators, Italy Monetary Aggregates series M1 historical series: pre-EMU definitions (billions of liras) [SST_STSMB.M.M1ST.101] (infostat.bancaditalia.it).
- 1998–2020: Bank of Italy, Money and Banking, Italian components of the monetary aggregates of the euro area, Italian contribution to euro-area M1, excluding currency held by the public, end of year (www.bancaditalia.it).

**Broad Money (converted to billions ITL)** (`money`) — p.105
- 1870–1947: Weber, Warren E. 2000. International Data. 1810-1995. Research Department, Federal Reserve Bank of Minneapolis. M2. http://cdm16030.contentdm.oclc.org/cdm/singleitem/collection/p16030coll4/id/8/rec/5
- 1948–1998: Bank of Italy, Statistical Database, Historical Tables – Monetary and Financial Indicators, Italy Monetary Aggregates series M2 plus historical series. December values. (infostat.bancaditalia.it).
- 1999–2020: Bank of Italy, Money and Banking, Italian components of the monetary aggregates of the euro area. Sum of two series: Currency in circulation held by the public + Italian contribution to euro-area M2, excluding currency held by the public, December values.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.106
- 1870–1871 & 1885–1914: Neal, Larry D., and Marc D. Weidenmier. "Crises in the global economy from tulips to today." Globalization in historical perspective. University of Chicago Press, 2003. 473-514. Open Market Rate, Monthly, End of Year Value. (http://ebutts05.tripod.com/nealweidenmiergsd/)
- 1922–1929: Statistisches Handbuch der Weltwirtschaft 1936. Series: Privatdiskont, Mailand.
- 1930–1938: League of Nations, International Statistical Yearbook (various issues), Rates prevailing in the capital or chief commercial city. Bons du Tresor. League of Nations, Geneva. Average annual rate.
- 1939–1965: Banca d'Italia (2012). Table "Tassi del mercato monetario e finanziario (1938–1965; media del periodo – per cento)", Series "Buono ordinario del tresoro, 10–12 mesi (BOT, 10–12 mesi)".
- 1966–1968: Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance. T-bill rate.
- 1969–1977: IMF, International Financial Statistics (2016). Interest Rates – Money Market Rate.
- 1978–2020: IMF (2021), IFS. Interest Rates – Treasury Bill Rate – Percent per Annum.
- [note] Gaps implied: 1872–1884 and 1915–1921 are not covered by any listed source.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — pp.106–107
- 1870–1913: sum of "Yield on consols" (Bank of England, Three centuries of macroeconomic data) and "Spread on consols" (Clemens, M. A. and Williamson, J. G. (2004), Wealth bias in the first global capital market boom, 1870–1913, The Economic Journal).
- 1914–1918: Investor's Monthly Manual; Chain linked.
- 1919–1930: Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic Policy: A European Forum 32: 51–75.
- 1931–1937: Banca D'Italia. Statistiche Storiche. Serie storiche sull'attività di banche e altre istituzioni finanziarie, 1861-2010. Tassi di interesse bancari dal 1861 al 2010 – tassi di interesse attivi – tassi di interesse sui prestiti – a medio-lungo termine. https://www.bancaditalia.it/statistiche/storiche
- 1938–1945: Banca D'Italia. Statistiche Storiche. Tabelle storiche tratte dai volumi della collana storica della banca d'italia. Tassi del mercato monetario e finanziario. Titoli di stato – Totale. https://www.bancaditalia.it/statistiche/storiche/tabelle-csbi/tav21/tav21.pdf
- 1946–1947: Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. Bank of England Staff Working Paper No. 845.
- 1948–2020: IMF (2021), IFS, Data reports "Economic indicators (IFS)", Section "Interest rates", Series "Government Bonds".

**Current Account (converted to billions ITL)** (`ca`) — p.107
- 1870–2007: B. Mitchell (2013), International Historical Statistics: Europe 1750–2005, Palgrave Macmillan, London. Series: OCB (overall current balance), in USD, transformed into lira via the JST exchange-rate series. Level.
- 2008–2020: IMF (2021), World Economic Outlook. Current Account. Level.

**Imports & Exports (converted to billions ITL)** (`imports`, `exports`) — p.107
- 1870–2011: Baffigi, Alberto (2011), Italian National Accounts, 1861–2011, Quaderni di Storia Economica No. 18. Note (verbatim): "Not pdf, but xls file (see Data Sources folder) -> online pdf and xls file differ for WW2 years. Chain-linked."
- 2012–2020: IMF (2021), IFS: National Accounts, Expenditure, Gross Domestic Product, External Balance of Goods and Services, Exports/Imports of Goods and Services, Nominal, Domestic Currency.

**Government Revenues (converted to billions ITL)** (`revenue`) — p.107
- 1870–1967: Mauro, Paolo, Rafael Romeu, Ari Binder, Asad Zaman (2013), "A Modern History of Fiscal Prudence and Profligacy", IMF Working Paper No. 13/5. Ratio multiplied with GDP series from JST dataset. Level.
- 1968–1993: Mitchell, Brian (2003), International Historical Statistics: Europe, 1750–2000. Basingstoke: Palgrave Macmillan. Total Central Government Revenue. Level.
- 1994–2020: OECD.Stat "General government accounts", Table 12, Sector GS1311 "Central government", Series GTR "Total general government revenue". Level.

**Government Expenditure (converted to billions ITL)** (`expenditure`) — p.107
- 1870–1967: Mauro, Romeu, Binder, Zaman (2013), IMF WP 13/5. Ratio multiplied with nominal GDP series from JST dataset.
- 1968–1994: Mitchell, Brian (2003), International Historical Statistics: Europe, 1750–2000. Total Central Government Expenditure.
- 1995–2020: OECD.Stat, Table 12, GS1311, Series GTE "Total general government expenditure".

**Public debt-to-GDP ratio** (`debtgdp`) — pp.107–108
- 1870–2007: Banca D'Italia. Statistics. Historical Statistics. Excel file: Italian Public debt since national unification, 1861-2007 (only in Italian). Series: Debito delle Amministrazioni pubbliche (consolidato). https://www.bancaditalia.it/statistiche/tematiche/stat-storiche/stat-storiche-economia/index.html. Divided by GDP from JST dataset.
- 2008–2020: IMF eLibrary World Economic Outlook. Series: General government gross debt (percent of GDP). http://www.imf.org/external/pubs/ft/weo/2015/02/weodata/index.aspx

**USD exchange rate (local currency/USD)** (`xrusd`) — p.108
- 1870–1880: Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. ITL/GBP rate multiplied with the GBP/USD rate (see UK chapter).
- 1881–1912: Banca D'Italia. Statistiche Storiche. Table: Tassi di cambio della lira 1861-1979.
- 1913–1945: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1946–1955: Reinhart & Rogoff (2010). From financial crash to debt crisis. (Black) market exchange rate.
- 1956–2020: IFS, IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- Note: lira–euro rate of 1936.27 assumed where necessary.

**Peg dummy / Strict peg dummy** (`peg`, `peg_strict`) — p.108: standard Obstfeld–Taylor (2003) 1870–1939; Ilzetzki–Reinhart–Rogoff (2004) 1940–2007; IRR (2008) extension 2008–2020.

**Exogenous monetary policy shocks** (`JSTtrilemmaIV`) — p.109: standard Jordà–Schularick–Taylor–Ward (2019) / Jordà–Schularick–Taylor (2020) text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.109
- 1970–2020: OECD housing prices database. Nominal series. Rebased 1990=100. [note: starts only in 1970.]

**Unemployment rate (percent)** (`unemp`) — p.109
- 1919–1936: Zamagni, Vera (1994), Una ricostruzione dell'andamento mensile dei salari industriali e dell'occupazione, Table 10: Disoccupazione (1929=100), media. Ricerche per la storia della banca d'Italia, Volume V, Editori Laterza. Chainlinked.
- 1937–1939, 1947–1981: Mitchell, Brian (2013), International Historical Statistics: Europe, 1750–2010, Table B2 Europe: Unemployment. Chainlinked.
- 1982–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.
- [note] gap 1940–1946.

**Wages (index, 1990=100)** (`wage`) — p.109
- 1871–1913: International Historical Statistics. Europe's Labour Force – Money/Wages in Industry. Hourly wages of males in all activities to 1900, and daily wages subsequently. Chainlinked.
- 1914–1937: IHS, Europe's Labour Force – Money/Wages in Industry. Daily wages of males in industry and transport. Chainlinked.
- 1938–1944 and 1946–1949: IHS, Europe's Labour Force – Money/Wages in Industry. Daily wages in all activities. Chainlinked.
- 1950–1989: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1990–2020: OECD statistics. Average annual wages. Current prices. Levels.

**Credit Data (converted to billions ITL)**

**Total loans to non-financial private sector** (`tloans`) — pp.109–110
- 1870–1949: Riccardo De Bonis, Fabio Farabullini, Miria Rocchelli, Alessandra Salvio & Andrea Silvestrini, 2013. "A quantitative look at the Italian banking system: evidence from a new dataset since 1861," Working Papers 9, Department of the Treasury, Ministry of the Economy and of Finance.
- 1950–1994: sum of Total Loans to Households and Total Loans to Business.
- 1995–2013: Riccardo De Bonis & Andrea Silvestrini, 2013. "The Italian financial cycle: 1861–2011," Cliometrica: DOI 10.1007/s11698–013–0103–5, and personal correspondence.
- 2014–2020: sum of Total Loans to Households and Total Loans to Business.

**Mortgage loans to non-financial private sector** (`tmort`) — p.110
- 1870–1937: Banca d'Italia (1967), ibid. Table 28 "Bilancio complessivo dei gruppi di aziende del sistema bancario".
- 1938–1965: F. Cotula (1999), Serie Contributi, Ricerche per la Storia della Banca d'Italia, Volume III, Stabilità e Sviluppo negli Anni Cinquanta, 3. Politica Bancaria e Struttura del Sistema Finanziario. Table 3a, p893, Table 9 p926.
- 1966–1996: growth rate calculated from R. De Bonis, F. Farabullini, M. Rocchelli & A. Salvio (2012), Quaderni di Storia Economica: "Nuove serie storiche sull'attività di banche e altre istituzioni finanziarie dal 1861 al 2011: che cosa ci dicono?". Table 1 "Principali voci dell'attivo e del passivo di bilancio delle banche: 1861–2010", Series "Prestiti medio–lungo termine".
- 1997–2013: Banca d'Italia (various years), Bollettino Statistico. Series "Mutui, totale".
- 2014–2020: Bank of Italy "Mortgage loans to Total resident sectors (excluded MFI)" (infostat.bancaditalia.it), database "mortgage", Banks and Financial Institutions: Financing and Funding by Sector and Geographical Area, Loans – by technical form, geographical area and customer sector, counterpart institutional sector: Mortgage Loans.

**Total Loans to Households** (`thh`) — p.110
- 1950–1994: Banca d'Italia, R. Bonci, M. Coletta (2006), I Conti finanziari dell'Italia dal 1950 a oggi, Famiglie Passività finanziarie, Prestiti. Table A2 (note 1989: average of 1988 & 1990 due to break in series).
- 1995–2013: Banca d'Italia (2019). Supplemento al Bollettino Statistico. La Ricchezza delle Famiglie Italiane. Series "Prestiti". https://www.bancaditalia.it/pubblicazioni/ricchezza-famiglie-societa-non-fin/2017-ricchezza-famiglie-societa-non-fin/index.html
- 2014–2020: Bank of Italy, sum of "Total short-term loans, issued by households and non-profit inst. serving households, stocks" and "Total medium/long-term loans, issued by households and non-profit inst. serving households, stocks" (infostat database "Households", Financial Accounts: Households and non-profit institutions serving households).

**Total Loans to Business** (`tbus`) — p.111
- 1950–1994: Banca d'Italia Servizio Studi, R. Bonci, M. Coletta (2006), I Conti Finanziari dell'Italia dal 1950 a oggi. Table A4.
- 1995–2013: residual of Total loans to non-financial private sector and Total Loans to Households.
- 2014–2020: growth rates from Bank of Italy "Loans to non-financial companies" (infostat database "Loans", Banks and Financial Institutions: Financing and Funding by Sector and Geographical Area, Loans – by technical form, geographical area and customer sector, counterpart institutional sector: non-financial companies).

**Corporate Debt** (`bdebt`) — p.111
- 1948–1949: lending to non-financial corporate business from Karsten Müller (2018) "Credit Markets around the World, 1910–2014", SSRN (https://ssrn.com/abstract=3259636).
- 1950–1994: financial accounts data on total non-equity liabilities from Bonci and Coletta (2012) "Italy's Financial Accounts since 1950", SSRN: http://ssrn.com/abstract=2120474.
- 1995–2012: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2013–2018: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2019–2020: bank loans to business and capital market debt from "Credit to the non-financial sector" database of the BIS (https://www.bis.org/statistics/totcredit.htm).

**Bank balance sheet ratios** "(Ratios in %, underlying data in billions ITL)"

*Capital ratio = Capital / Total Assets* (`lev`) — pp.111–112
- Total Assets:
  - 1870–1936: Bank of Italy, unpublished long run data series on total assets of the banking system, sent by Francesco Vercelli. Chainlinked.
  - 1937: De Bonis R., Farabullini F., Rocchelli M. e Salvio A. (2012 and update), Nuove serie storiche sull'attività di banche e altre istituzioni finanziarie dal 1861 al 2011: che cosa ci dicono?, Banca d'Italia – Quaderni di Storia economica, 26. Chainlinked with growth rate of sum of "Depositi", "Obbligazioni emesse" and "Capitale e Riserve".
  - 1938–2010: Bank of Italy, unpublished long run data series on total assets of the banking system. Series adjusted in years 1976–1982 to reflect growth rates of sum of "Depositi", "Obbligazioni emesse" and "Capitale e Riserve" from De Bonis et al. (2012 and update).
  - 2011–2014: ECB Balance Sheet Indicators, Total Assets, Chainlinked.
  - 2015–2020: Bank of Italy, Total Assets, Series Key "BAM_BSIB.M.1070001.52000199.9.101.WRDBI2.S0.1000.997", Chainlinked.
- Capital:
  - 1870–1936: Bank of Italy, unpublished long run data series sent by Francesco Vercelli. "Capital ratio". Chainlinked (level difference in capital ratio in 1937).
  - 1937: De Bonis et al. (2012 and update), Quaderni di Storia economica 26. "Capitale e Riserve". Levels.
  - 1938–1945: Unpublished long run data series on total assets of the banking system, sent by Francesco Vercelli. Capital ratio multiplied with Total Assets.
  - 1946–1991: Bank of Italy, unpublished long run data series sent by Francesco Vercelli. Chainlinked capital ratio multiplied with Total Assets.
  - 1992–2007: OECD Statistical Supplement, "Tier1 Capital" – "Supervisory Reductions" divided by "Total assets at end of the year". Levels of capital ratio multiplied with Total Assets.
  - 2008–2020: ECB Consolidated Banking Data, series "Full sample (All banking groups / stand-alone banks irrespective of their accounting / supervisory reporting framework), Tangible equity [% of total assets]". Levels of capital ratio, multiplied with Total Assets.

*Loans-to-Deposits ratio = Loans / Deposits* (`ltd`) — pp.112–113
- Deposits:
  - 1870–2014: De Bonis, Farabullini, Rocchelli e Salvio (2012 and update), Quaderni di Storia economica 26. Series "Depositi". Levels.
  - 2015–2020: Bank of Italy, "Total Deposits of Domestic Other Residents", Chainlinked, series ID: BAM_BSIB.M.1070001.52000100.9.101.IT.S1P.1000.997.
- Loans:
  - 1870–2014: De Bonis et al. (2012 and update), Quaderni di Storia economica 26. Series "Prestiti- Totali". Levels.
  - 2015–2020: Bank of Italy, "Total Loans of Banks", Chainlinked, series ID BAM_BSIB.M.1070001.52000700.9.101.IT.S1.1000.997.

*Noncore ratio = (Total Assets – Capital – Deposits) / (Total Assets – Capital)* (`noncore`) — p.113.

### JAPAN (ISO JPN) — pages 113–124. "(Data in trillions JPY)"

**Population** (`pop`) — p.113
- 1870–2008: Angus Maddison Database (2008), ibid. Table 1 "Population levels, 1AD–2030AD".
- 2009–2017: growth rates from IMF (Aug, 2019) WEO, Subject "People – population" (base year 2008).
- 2018–2020: growth rates from IMF (Oct, 2021) WEO (base year 2008).

**GDP (trillions JPY)** (`gdp`) — pp.113–114
- 1875–1884: 100-year statistics of the Japanese economy (p.28). Series: Long-term estimates of national income (by Yuzo Yamada) – National Income. Chainlinked. [note: starts 1875.]
- 1885–1940: Global price and income history group. Nominal GDP historical series. http://gpih.ucdavis.edu/. Original source: K. Ohkawa, N. Takamatsu, and Y. Yamamoto. 'Vol. 1 National Income' in K. Ohkawa, M. Shinohara, M. Umemura (eds.), Estimates of Long-Term Economic Statistics of Japan Since 1868 (Tokyo: Tokyo Keizai Shinposha, 1974). Level.
- 1941–1944 & 1946–1959: Mitchell, B. (2013). International Historical Statistics. Series: GNP. Chainlinked. [note: 1945 missing.]
- 1960–2020: IMF (2021), IFS, "Gross domestic product (in millions) – GDP nominal".

**Real GDP per capita (PPP, 1990 Int$, Maddison)** (`rgdpmad`) — p.114: standard block.

**Real GDP per capita (index, 2005=100)** (`rgdpbarro`) — p.114: standard block (World Bank 2021).

**Real consumption per capita (index, 2006=100)** (`rconsbarro`) — p.114: Barro–Ursúa 1874–2009 [note: starts 1874]; World Bank 2010–2020 chain linked.

**Investment-to-GDP ratio** (`iy`) — p.114
- 1885–2004: Mitchell, Brian (2013), International Historical Statistics: Africa, Asia & Oceania, 1750–2005, London. Series GFCF (gross fixed capital formation) divided by GNP (gross national product). (gap in 1945). Level.
- 2005–2020: IMF (2021), World Economic Outlook. Total investment (percent of GDP). Level.

**Consumer prices (index, 1990=100)** (`cpi`) — p.114
- 1870–2000: Bas van Leeuwen, Wage differentials and economic growth in India, Indonesia, and Japan, 1800-2001. CPI series for Japan.
- 2001–2020: IMF WEO (2021), "Inflation, average consumer prices". Chainlinked.

**Narrow Money (trillions JPY)** (`narrowm`) — p.115
- 1873–1954: Mitchell, B. (2013). IHS. Notes in circulation + demand deposits from commercial banks. Level.
- 1955–2016: IMF IFS (http://elibrary–data.imf.org/). M1 seasonally adjusted. Level.
- 2017–2020: Bank of Japan, BOJ Time-Series Data Search, Money stock (from April 2003), M1/Amounts Outstanding at End of Period/Seasonally Adjusted/Money Stock, frequency: calendar year, end.

**Broad Money (trillions JPY)** (`money`) — p.115
- 1870–1954: Weber, Warren E. 2000. International Data. 1810-1995. FRB Minneapolis. M2.
- 1955–2016: IMF IFS, series M2, seasonally adjusted (period average). Level.
- 2017–2020: Bank of Japan, BOJ Time-Series Data Search, Money stock (from April 2003), M2/Average Amounts Outstanding/Seasonally Adjusted/Money Stock, frequency: calendar year, average.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.115
- 1879–1938: Bank of Japan (1986), Nihon Ginko Hyakunen–shi Shiryo–hen (The First Hundred Years – Materials), Tokyo. Table 13, Series "Discounts rate BJO", p424.
- 1957–2017: IMF (2019), IFS, Section "Economic indicators", Series "Interest Rates – money market rate".
- 2018–2020: Bank of Japan, Short-term Money Market Rates – Call Rate – Uncollateralized Overnight/Average, conversion method: averaged.
- [note] gaps: 1870–1878 and 1939–1956 not covered.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — pp.115–116
- 1870–1879: sum of "Yield on consols" (Bank of England, Three centuries) and "Spread on consols" (Clemens & Williamson 2004).
- 1880–1913: sum of "Yield on consols" (Bank of England) and "Spread on consols" from Ferguson, N. and Schularick, M. (2006). The Empire Effect: The Determinants of Country Risk in the First Age of Globalization, 1880-1913. The Journal of Economic History.
- 1914–1929: Investor's Monthly Manual. Japanese 4% 1899 Sterling-bond current yield. December values.
- 1930–1963: Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. BoE Staff Working Paper No. 845.
- 1964: Hundred-year statistics of the Japanese Economy. P.264 Long-Term Government Securities.
- 1965–2016: IMF (2019), IFS, "Government Bonds".
- 2017–2020: OECD (2021). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.116
- 1913–2008: Knoll et al. (2014). No price like home: Global house prices, 1870-2012. Year average values.
- 2008–2013: Individual transaction data on detached houses and condominiums covering the whole of Japan from the Land Registry of Japan at the Ministry of Land and Transportation (https://www.mlit.go.jp/totikensangyo/totikensangyo_tk5_000085.html). Index built at monthly frequency since 2008 using transaction-based weights and a hedonic method based on a time-dummy variable model using the rolling-window method; explanatory variables are size, age, location and transaction terms. Chain-linked.
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Current Account (trillions JPY)** (`ca`) — p.116
- 1870–1979: B. Mitchell (2013), IHS. Overall current balance. Level. (Note: no data for 1945).
- 1980–2020: IMF (2021), WEO. CA as % of GDP × nominal GDP = Current Account. Levels.

**Imports & Exports (trillions JPY)** (`imports`, `exports`) — p.116
- 1870–1947: B. Mitchell (2007), IHS: Africa, Asia & Oceania 1750–2005. Note: gap in 1944–1945 (no data).
- 1948–2020: IMF IFS archive, M10 2021, External Trade, Goods, Value of Exports FOB / Imports CIF, Domestic Currency.

**Government Revenues (trillions JPY)** (`revenue`) — pp.116–117
- 1870–1945: Statistics Department of the Bank of Japan (1966), One Hundred Years of Statistics of the Japanese Economy, p. 128. Central Government Finance, Revenue, General Account. Levels.
- 1946–1964: Statistics Bureau, Director–General for Policy Planning & Statistical Research and Training Institute (2008), Historical Statistics of Japan.
- 1965–1969: IFS, Budgetary Central Government, Revenue, 2001 Manual, Cash, National Currency.
- 1970–1993: Annual Report on National Accounts 2000. Table: Current and Capital Transactions by the Sub-sectors of General Government, current receipts central government. http://www.esri.cao.go.jp/en/sna/data/kakuhou/files/kako_top.html
- 1994–2020: OECD.Stat, Table 12, GS1311, Series GTR "Total general government revenue".

**Government Expenditure (trillions JPY)** (`expenditure`) — p.117
- 1870–1964: Statistics Department of the Bank of Japan (1966), One Hundred Years of Statistics of the Japanese Economy, p. 128. Central Government Finance, Expenditure, General Account. Levels.
- 1965–1995: Statistics Bureau (2008), Historical Statistics of Japan. General account. Levels.
- 1996–2009: Cabinet Office. Annual Report on National Accounts. Table: National Disposable Income and its Use Account, Series: final consumption expenditure general government (http://www.esri.cao.go.jp/en/sna/data/kakuhou/files/kako_top.html).
- 2010–2020: OECD.Stat, Table 12, GS1311, "Series GTR 'Total general government expenditure'" [sic — text says GTR though the series is expenditure].

**Public debt-to-GDP ratio** (`debtgdp`) — p.117
- 1875–1969: Abbas et al (2010). A historical public debt database. IMF Working Paper WP/10/245. https://www.imf.org/external/pubs/cat/longres.aspx?sk=24332.0. Level. (Note: no data for 1945).
- 1970–2020: European Commission, AMECO, Gross Public Debt (linked series) (UDGGL), % of GDP at market prices (EDP). Level.

**USD exchange rate (local currency/USD)** (`xrusd`) — pp.117–118
- 1870–1880: Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. Yen per US Dollar (contained in this dataset) (gap: 1871 and 1872).
- 1881–1915: Statistics Department of the Bank of Japan (1966), One Hundred Years of Statistics of the Japanese Economy, p. 318. Exchange rate.
- 1916–1941: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1942–1945: Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
- 1946–1970: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1971–2020: IFS, IMF eLibrary. "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy / Strict peg dummy** — p.118: standard block.

**Exogenous monetary policy shocks** — p.118: standard text.

**Unemployment rate (percent)** (`unemp`) — p.118
- 1930–1938 and 1948–1952: Mitchell, Brian (2013), IHS Africa, Asia, Oceania, 1750–2010, Table B2 Asia Unemployment. Chainlinked.
- 1953–2020: ILOSTAT (2021), "Unemployment rate by sex and age" based on the Labor force survey (LFS).

**Wages (index, 1990=100)** (`wage`) — p.119
- 1870–1884, 1888–1891, 1893 and 1915–1919: Williamson (1998) "Real Wages and Relative Factor Prices in the Third World Before 1940: What do they tell us about the Sources of Growth?". Nominal daily wage for carpenters in Japan until 1886 and daily wage of carpenters in Tokyo thereafter. Chainlinked.
- 1885–1887, 1892, 1894–1914 and 1920–1925: TOKYO DEPT. OF FINANCE GPO. "Financial and Economic Annual of Japan", various years. Average nominal daily wage of 8 non-agricultural jobs. Chainlinked.
- 1926–1945: IHS. Africa, Asia, Oceania Labour Force. Average daily rates for males. Chainlinked.
- 1946–1947: United Nations. Monthly Bulletin of Statistics, January 1951. Nominal monthly wage. Chainlinked.
- 1948–1989: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (trillions JPY)**

**Total loans to non-financial private sector** (`tloans`) — p.119
- 1874–1940: Nihon kinyu no suryo bunseki (Japanese Edition), "Flow of Funds Accounts of Prewar Japan: 1871–1940," Bank Assets, Loans.
- 1946–48: growth rate calculated from Nihon Ginkō Tōkeikyoku & Nihon Ginkō Chōsakyoku (various), Honpō–Keizai–Tōkei, Nihon Ginkō Tōkeikyoku, Tokyo. Table "Outstanding loans by kind of collateral" (various issues), Series "Total".
- 1949–2020: sum of Total Loans to Households and Total Loans to Business (exception: 1992 value interpolated, simple average of 1991 and 1993 values).

**Mortgage loans to non-financial private sector** (`tmort`) — p.119
- 1893–1940: Shin'ichi Goto (1970): Nihon no Kin'yu Tokei (Japanese Financial Statistics). Table 47 "Lending of ordinary banks by type of collateral, real estate and foundation", Series "Real estate and foundation".
- 1946–1952: growth rate calculated from Nihon Ginkō Tōkeikyoku & Chōsakyoku (various), Honpō–Keizai–Tōkei. Table "Outstanding loans of all banks by kind of collateral", Series "Loans on real estate, floating mortgages & vessels" (base year: 1953).
- 1953–2020: sum of Loans to Households Secured by Real Estate and, from Bank of Japan Time-Series Database, Loans and Bills Discounted by sector, Series "Real Estate/Outstanding/Banking Accounts/Shinkin Banks" + Series "Real Estate/Outstanding/Banking Accounts, Trust Accounts and Overseas Office Accounts/Domestically Licensed Banks", Frequency: Calendar year, Conversion method: End.

**Total Loans to Households** (`thh`) — p.120
- 1948–1952: growth rate calculated from Honpō–Keizai–Tōkei, Table "All banks: loans classified by industry", Series "Funds for personal consumption & tax payment / private households & personal (from 1951)" (base year: 1953).
- 1953–1961: growth rate from Honpō–Keizai–Tōkei, Table "Outstanding loans and discounts of all banks by industry (total)", Series "Private persons" (base year: 1962).
- 1962–1981: growth rate from Honpō–Keizai–Tōkei, Table "All banks (banking accounts): Loans classified by industry", Series "Private persons" + Keizai–Tōkei–Nenpō (various), Table "All banks (trust accounts): Loans classified by industry", Series "Private persons" (base year: 1982).
- 1982–2000: Bank of Japan Statistics (various), Deposits and loans. "Loans and bills discounted by sector (by type of major industries)", Series "Domestically licensed banks, outstanding, households" + (Series "Shinkin Banks (excluding overdrafts), outstanding, individuals" [1982-1994] and "Shinkin banks, outstanding, households" [1995-2014]).
- 2000–2020: Bank of Japan Time-Series Database. Loans and Bills Discounted by sector (Outstanding, Loans for Fixed Investment): Sum of Households/Outstanding/Banking Accounts, Trust Accounts and Overseas Office Accounts/Domestically Licensed Banks + Households/Outstanding/Banking Accounts/Shinkin Banks. Calendar year, End.

**Total Loans to Business** (`tbus`) — pp.120–121
- 1948–1959: Honpō–Keizai–Tōkei, Table "All banks: Loans classified by industry", Series "Total without lending to private households, local governments, and financial institutions".
- 1960–1961: Honpō–Keizai–Tōkei, Table "Outstanding loans and discounts of all banks by industry", Series "Total (without lending to private persons, local governments, and finance)".
- 1962–1984: calculated from Nippon Ginkō Tōkeikyoku (various), Keizai–Tōkei–Nenpō, Table "All banks (banking accounts): Loans classified by industry", Series "Total without loans to households, local government, financials, and companies overseas" + Table "All banks (trust accounts) ...", same series.
- 1985: simple average of 1984 and 1986 values.
- 1986–2004: Bank of Japan (various), Statistics 5 Deposits and Loans. Table 149–156 "Loans and bills discounted by sector (by type of major industries)", Series "Domestically licensed banks: Total without loans to local governments, households, finance and insurance, and overseas yen loans and domestic loans transferred to overseas" + Series "Shinkin Banks: Total without loans to local governments, households, finance and insurance, and overseas yen loans and domestic loans transferred to overseas".
- 2005–2020: Bank of Japan Time-Series Database, Loans and Bills Discounted by Sector (Outstanding, Loans for Fixed Investment). For Domestically Licensed Banks (Banking Accounts, Trust Accounts and Overseas Office Accounts) and Shinkin Banks: sum of total outstanding loans minus outstanding loans for Finance and Insurance, Local Governments, Households, and Overseas Yen Loans and Domestic Loans Transferred Overseas. Calendar year, End.

**Corporate Debt** (`bdebt`) — p.121
- 1948–1963: Nihon Ginkō Tōkeikyoku and Nihon Ginkō Chōsakyoku (various) as well as Honpō–Keizai–Tōkei and Nihon Ginkō Tōkeikyoku, Tokyo. 1948-59: Table "All banks: Loans classified by industry", Series "Total without lending to private households, local governments, and financial institutions". 1960-61: Table "Outstanding loans and discounts of all banks by industry", Series "Total (without lending to private persons, local governments, and finance)". 1962-63: Table "All banks (banking accounts): Loans classified by industry", Series "Total without loans to households, local government, financials, and companies overseas" + Table "All banks (trust accounts) ...", same series.
- 1964–1979: bank loans to business and capital market debt from BIS "Credit to the non-financial sector".
- 1980–2012: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2013–2020: BIS "Credit to the non-financial sector".

**Bank balance sheet ratios** "(Ratios in %, underlying data in trillions JPY)"

*Capital ratio* (`lev`) — pp.121–123
- Total Assets (trillions JPY):
  - 1893–1929: 100-year statistics of the Japanese Economy. Total liabilities estimated as sum of deposits, capital, debentures issued and other liabilities, holding the share of other liabilities constant at the average 1930-1940 value.
  - 1930–1946: Takabatake, Economic Statistics of Japan (1955), Bank of Japan, series "Assets". Levels. (1943 and 1944 values estimated using growth rates of deposits).
  - 1947–1972: Economic Statistics Annual (1972), Editor and Publisher: Sachio Watanabe, Tokyo, All banks, series "Total Assets or Liabilities and Net Worth". Levels.
  - 1973–1974: Bank of Japan. Assets and Liabilities of City Banks (Banking Accounts), Series "Total Including Other Accounts" + Assets and Liabilities of Regional Banks (Banking Accounts), same series. Files cdab0290 and cdab0300 from BoJ, sent by Ryoji Koike. Interpolated accounting for market share of city and regional banks in 1970-1972 and 1975-1976.
  - 1975–2005: Bank of Japan, 14-3-a Assets and Liabilities of Domestically Licensed Banks – Banking Accounts (1975–2005), series "Total (assets, or liabilities and capital accounts)". Levels.
  - 2006–2014: Bank of Japan, Assets and Liabilities of Domestically Licensed Banks (Banking Accounts), Financial Institutions Accounts, work sheet 72, Assets (concluded), series "Total". Levels.
  - 2015–2020: Bank of Japan Data Online: Assets and Liabilities of Domestically Licensed Banks (Banking Accounts) (End of month). Series key: BS02'FAABK_FAAB2DBEAS. Levels.
- Capital (trillions JPY):
  - 1893–1933: Japanese Banking, A history, 1859-1959, Norio Tamaki. Sum of Private/Ordinary Banks, series "Paid-in Capital" + "Reserves" and Savings Banks, series "Paid-in Capital" + "Reserves". Chainlinked.
  - 1934–1972: Economic Statistics Annual (1972), Sachio Watanabe. All banks, "Capital" + "Reserves". Levels.
  - 1973–1974: Bank of Japan, City Banks and Regional Banks (Banking Accounts), sum of series "Common stock", "New stock subscriptions", "Legal reserves", "Earned surplus – voluntary reserves". Files cdab0290 and cdab0300, sent by Ryoji Koike. Interpolated accounting for market share in 1970-1972 and 1975-1976.
  - 1975–1981: Bank of Japan, 14-3-a, sum of "Common stock", "Capital Surplus" and "Retained earnings" less "Profits and losses for the term" (in 1975-1981 these are included in "undivided profits"). Levels.
  - 1982–1991: Bank of Japan, 14-3-a, sum of "Common stock", "Capital Surplus" and "Retained Earnings". Levels.
  - 1992–2005: Bank of Japan, 14-3-a, series "Stockholder's equity". Levels.
  - 2006–2014: Bank of Japan, Financial Institutions Accounts, work sheet 78, Liabilities and stockholder's equity (concluded), series "Net Assets". Levels.
  - 2015–2020: Bank of Japan Data Online, series key BS02'FAABK_FAAB2DBECA. Levels.

*Loans-to-Deposits ratio* (`ltd`) — pp.123–124
- Deposits (trillions JPY):
  - 1893–1897: Japanese Banking, A history, 1859-1959, Norio Tamaki. Principal accounts of Private/Ordinary Banks, Series "Deposits". Chainlinked.
  - 1898–1946: 100-year statistics of the Japanese Economy. Principal accounts of all banks. Series "Deposits". Levels.
  - 1947–1972: Economic Statistics Annual (1972), Sachio Watanabe, All banks, series "Total Deposits". Levels.
  - 1973–1974: Bank of Japan, City Banks and Regional Banks (Banking Accounts), Series "Deposits". Files cdab0290/cdab0300, Ryoji Koike. Interpolated for market share 1970-1972 and 1975/1976.
  - 1975–2005: Bank of Japan, 14-3-a, series "Deposits". Levels.
  - 2006–2014: Bank of Japan, Financial Institutions Accounts, work sheet 73, Liabilities and stockholder's equity (continued), series "Deposits". Levels.
  - 2015–2020: Bank of Japan Data Online, series key BS02'FAABK_FAAB2DBEL01. Levels.
- Loans (trillions JPY):
  - 1893–1897: Japanese Banking, A history, Norio Tamaki. Principal accounts of Private/Ordinary Banks, Series "Lendings". Chainlinked.
  - 1898–1929: 100-year statistics of the Japanese Economy. Principal accounts of all banks. Series "Lendings". Levels.
  - 1930–1946: Economic Statistics of Japan (1955), Takabatake, Bank of Japan, series "Loans and Bills discounted". Levels.
  - 1947–1972: Economic Statistics Annual (1972), Sachio Watanabe, All banks, series "Total Loans" + "Bills discounted". Levels.
  - 1973–1974: Bank of Japan, City Banks and Regional Banks (Banking Accounts), Series "Loans and Bills Discounted". Files cdab0290/cdab0300, Ryoji Koike. Interpolated for market share 1970-1972 and 1975/1976.
  - 1975–2005: Bank of Japan, 14-3-a, series "Loans and Bills discounted". Levels.
  - 2006–2014: Bank of Japan, Financial Institutions Accounts, work sheet 70, series "Loans". Chainlinked.
  - 2015–2020: Bank of Japan Data Online, series key BS02'FAABK_FAAB2DBEA37. Levels.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.124.

### NETHERLANDS (ISO NLD) — pages 124–134. "(Data in millions NLG)"

**Population** (`pop`) — p.124: Maddison (2008) Table 1 for 1870–2008; IMF WEO growth rates 2009–2020 (base year 2008).

**GDP (converted to millions NLG)** (`gdp`) — p.125
- 1870–1913: van Zanden et al., National Accounts of the Netherlands, 1880–1913, Table "Final estimates GDP and GNP (total output, income and expenditure in current and constant prices), 1800-1913," (http://nationalaccounts.niwi.knaw.nl/start.htm). Level.
- 1921–1939: J.P. Smits, P.J. Woltjer and D. Ma (2009), 'A Dataset on Comparative Historical National Accounts, ca. 1870-1950: A Time-Series Perspective', Groningen Growth and Development Centre Research Memorandum GD-107 (http://www.rug.nl/research/ggdc/data/historical-national-accounts). Level.
- 1945–1968: Mitchell, B. (2013). IHS. National Accounts. Series: GDP. Level.
- 1969–2020: IMF (2021), IFS, "Gross domestic product (in millions) – GDP nominal".
- [note] gaps implied: 1914–1920 and 1940–1944.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.125: standard block.
**Real GDP per capita (index, 2005=100)** — p.125: standard block (World Bank 2018).
**Real consumption per capita (index, 2006=100)** — p.125: standard block.

**Investment-to-GDP ratio** (`iy`) — pp.125–126
- 1870–1913: van Zanden et al. National Accounts of the Netherlands. Excel file: Gross fixed capital formation. Series: current prices – total GFCF. Divided by GDP from JST dataset. http://nationalaccounts.niwi.knaw.nl/start.htm
- 1921–1939: Bakker et al (1990). "The Dutch Economy 1921-1939: Revised macroeconomic data for the interwar period". Series: Gross fixed capital formation – Government + Enterprise. Divided by GDP from JST dataset.
- 1948–1959: Mitchell, B. (2013). IHS. Series: Capital formation. Divided by GDP from JST dataset.
- 1960–2020: IMF (2019), IFS, Data Report "National Accounts", Series Gross Capital Formation, Gross Fixed Capital Formation, Corporations, Households, and Non-profit Institutions Serving Households Nominal, Seasonally adjusted. Until 1989: National Currency. From 1990 onwards the Euro series has been transformed into NLG.

**Consumer prices (index, 1990=100)** (`cpi`) — p.126: A. Taylor (2002) 1870–1996; IMF WEO (April 2019) "Inflation, average consumer prices" 1997–2020, chainlinked.

**Narrow Money (converted to millions NLG)** (`narrowm`) — p.126
- 1870–1949: Mitchell, B. (2013). IHS. Sum of banknote circulation + deposits in commercial banks. 1914-1917 deposit data interpolated with geometrical average growth rate. Gap: 1942-1944.
- 1950–1981: Mitchell, B. (2013). IHS. Series: M1.
- 1982–2017: De Nederlandsche Bank. Table 5.4 Contribution of the Netherlands to euro area monetary aggregates (stocks). Sum of Overnight + Currency in circulation (=difference of M3 incl. and excl. currency in circulation). http://www.dnb.nl/en/binaries/t5.4ek_tcm47-330724.xls?2015120611
- 2016–2020: De Nederlandsche Bank. Statistics. Data Search. Monetary aggregates. Dutch contribution to monetary aggregates in the euro area (Month)/(quarter). Sum of Overnight + Currency in circulation (=difference of M3 incl. and excl. currency in circulation). Q4 stock values using the older definition.
- [note] the 1982–2017 and 2016–2020 ranges overlap as printed.

**Broad Money (converted to millions NLG)** (`money`) — pp.126–127
- 1879–1955: Mitchell, B. (2013). IHS. Sum of banknote circulation + deposits in commercial banks + deposits in savings banks (general savings banks + post offices). 1914-1917 deposit data interpolated with geometrical average growth rate. 1922-1924 deposits in general savings banks interpolated with geometrical average growth rate. Gap: 1942-1944.
- 1956–1997: IMF (2015), IFS. Series: M2, national currency.
- 1998–2017: De Nederlandsche Bank. Table 5.4 Contribution of the Netherlands to euro area monetary aggregates (stocks). Sum of Overnight deposits + Deposits with agreed maturity up to 2 years + Deposits redeemable at a period of notice up to 3 months + Currency in circulation (=difference of M3 incl. and excl. currency in circulation).
- 2016–2020: De Nederlandsche Bank. Statistics. Data Search. Monetary aggregates. Same sum. Q4 stock values using the older definition.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.127
- 1870–1872: Neal & Weidenmier (2003), Open Market Rate, Monthly, End of Year Value.
- 1873–1879: Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition.
- 1880–1912: Bordo, Eichengreen, Klingebiel, Martinez-Peria (2001), "Is the Crisis Problem Growing More Severe?" Economic Policy 32: 51–75.
- 1913–1914: Neal & Weidenmier (2003), Open Market Rate, Monthly, End of Year Value.
- 1915–1957: Bordo et al. (2001).
- 1958–1964: IFS, Section "Interest rates", Series "Central Bank rate".
- 1965–1985: IFS, Series "Money Market rate".
- 1986–2020: OECD Statistics, Interest rates – Short-term interest rate (http://stats.oecd.org/).

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — pp.127–128
- 1870–1879: Schmelzing, P. (2020), BoE Staff Working Paper No. 845.
- 1880–1913: Flandreau and Zumer, 2004, The Making of Global Finance, Paris: OECD Development Centre.
- 1914–1947: Schmelzing, P. (2020).
- 1948–2016: IMF (2021), IFS, Series "Monetary and Financial Accounts, Interest Rates, Securities Markets, Government Debt Securities, Government Bonds, Percent per Annum".
- 2017–2020: OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en.

**Current Account (converted to millions NLG)** (`ca`) — p.128
- 1870–1913: J. Smits, E. Horlings & J. van Zanden (2000), Dutch GNP and its components 1800–1913, GGDC Research Memorandum No.5, University of Groningen. Series: Sum of net merchandise exports + net service exports + net primary incomes. Level.
- 1921–1939: Gert P. Bakker, Theo A. Huitker and Cornelis A. van Bochove (1990), The Dutch Economy 1921-39: Revised Macroeconomic Data for the Interwar, Review of Income and Wealth, Series 36, Number 2, June 1990.
- 1948–1966: B. Mitchell (2007), IHS: Europe 1750–2005.
- 1967–2007: IMF (2010), IFS. Table "Balance of payments", Series "Balances – current account balance".
- 2008–2020: IMF WEO. % of GDP × nominal GDP = Current Account.

**Imports & Exports (converted to millions NLG)** (`imports`, `exports`) — p.128
- 1870–1947: J. Smits, E. Horlings & J. van Zanden (2000), Dutch GNP and its components 1800–1913, GGDC Research Memorandum No.5; and B. Mitchell (2007), IHS: Europe 1750–2005. Note: gaps in 1944–1945. Until 1913 the data are taken from Table H.1 Imports, Exports and Net Merchandise Exports, 1802-1913 in Smits et al. (2000); between 1913 and 1947 growth rates in Mitchell (2007) are chain-linked and linearly adjusted to match Smits et al. (2000) and IMF (2019) benchmarks for 1913 and 1948, respectively. Data missing for 1944 and 1945.
- 1948–2020: IMF IFS archive, M10 2021, External Trade (exports FOB, imports CIF, domestic currency).

**Government Revenues (converted to millions NLG)** (`revenue`) — p.129
- 1870–1969: Centraal Bureau voor de Statistiek (2001), Tweehonderd Jaar Statistiek in Tijdreeksen 1800–1999, CBS, Amsterdam (www.cbs.nl/NR/rdonlyres/7934A2DE–B87C–4CDF–8BC7–D34F02225620/0/200jaarstattijdreeksen.pdf).
- 1970–2020: OECD (2019), OECD.Stat, Table 12, GS1311, Series GTR "Total general government revenue".

**Government Expenditure (converted to millions NLG)** (`expenditure`) — p.129
- 1870–1969: Centraal Bureau voor de Statistiek (2001), Tweehonderd Jaar Statistiek in Tijdreeksen 1800–1999.
- 1970–2020: OECD (2019), OECD.Stat, Table 12, GS1311, Series GTE "Total general government expenditure".

**Public debt-to-GDP ratio** (`debtgdp`) — p.129
- 1870–1974: Mauro, Romeu, Binder, Zaman (2013), "A Modern History of Fiscal Prudence and Profligacy," IMF Working Paper 13/5 (http://www.imf.org/external/pubs/cat/longres.aspx?sk=40222.0). Note: gap from 1940–1945.
- 1975–2020: European Commission AMECO, Gross Public Debt (linked series) (UDGGL), % of GDP at market prices (EDP).

**USD exchange rate (local currency/USD)** (`xrusd`) — pp.129–130
- 1870–1912: Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. Amsterdam on London.
- 1913–1939: Bordo, Eichengreen, Klingebiel, Martinez–Peria (2001), Economic Policy 32: 51–75.
- 1940–1945: Bordo, M. D. & Jonung, L. (1996).
- 1946–1955: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1956–2020: IFS, IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- Note: guilder–euro exchange rate of 2.20371 assumed where necessary.

**Peg dummy / Strict peg dummy** — p.130: standard block.
**Exogenous monetary policy shocks** — p.130: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.130
- 1870–2012: Knoll et al. (2014). No price like home. Year average values.
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — pp.130–131
- 1870–1989: Statistics Netherlands, unemployment rate (% total labor force) – obtained by dividing the series "Werkloze beroepsbevolking" by the series "totale beroepsbevolking". Chainlinked.
- 1990–2020: ILOSTAT (2020), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.131
- 1870–1947: Williamson (1995). "The evolution of global labor markets since 1830: background evidence and hypotheses". Real wages inflated with consumer price deflator from A. Taylor (2002), A Century of Purchasing–Power Parity, REStat 84(1), pp. 139–150. Chainlinked.
- 1948–1989: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (converted to millions NLG)**

**Total loans to non-financial private sector** (`tloans`) — p.131
- 1900–1981: De Nederlandsche Bank (2000), Nederlandse Financieel Instellingen in de Twintigste Eeuw: Balansreeksen en Naamlijst van Handelsbanken, Series "DNB Statistische Cahiers Nr.3".
- 1982–2020: De Nederlandsche Bank (2020), Domestic MFI–statistics (monetary). Table T5.2 "Balance sheet of MFIs in the Netherlands (excluding De Nederlandsche Bank): not adjusted for securitisations", Table 5.2.1 "Loans from MFIs to the private sector, breakdown by sector, original maturity and instrument; not adjusted for securitisations", older definition, December values (http://www.statistics.dnb.nl/en/financial–institutions/banks/domestic–mfi–statistics–monetary/index.jsp).

**Mortgage loans to non-financial private sector** (`tmort`) — pp.131–132
- 1900–1984: De Nederlandsche Bank (2000), Nederlandse Financieel Instellingen in de Twintigste Eeuw, Series "DNB Statistische Cahiers Nr.3".
- 1985–1997: calculated from De Nederlandsche Bank (2000), ibid., Series "Mortgage Credit of commercial banks, savings banks and postal bank" (note: growth rates after 1986 calculated from a spread sheet shared by Tijmen Swank (DNB)).
- 1998–2009: calculated from De Nederlandsche Bank (2012), Domestic MFI–statistics (monetary). Table 5.2.1, Series "Real Estate & Mortgage Loans to Households".
- 2010–2020: sum of Mortgage Loans to Households and Mortgage Loans to Business.

**Total Loans to Households** (`thh`) — p.132
- 1990–2020: calculated from De Nederlandsche Bank (2012), Domestic MFI–statistics (monetary). Table 5.2.1, Series "Real Estate & Mortgage Loans to Households", "Consumer credit", "All other lending to households". [note: starts 1990 only.]

**Total Loans to Business** (`tbus`) — p.132
- Residual of Total loans to non-financial private sector and Total Loans to Households.

**Mortgage Loans to Business** (no dataset column; component of `tmort`) — p.132
- 2010–2020: Dutch National Bank. Table 5.2.4 Loans from MFIs to non-financial corporations in the Netherlands, breakdown by activity; not adjusted for securitisations; Series: Real estate activities, first definition, q4 values.

**Corporate Debt** (`bdebt`) — p.132
- 1946–1989: bank lending to business sector proxied by loans of "Handelsbanken" from De Nederlandsche Bank (2000).
- 1990–1994: BIS "Credit to the non-financial sector" (bank loans to business and capital market debt).
- 1995–2018: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2019–2020: BIS "Credit to the non-financial sector".

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions NLG)"

*Capital ratio* (`lev`) — pp.132–133
- Total Assets (converted to millions NLG):
  - 1900–1981: De Nederlandsche Bank (2000), DNB Statistische Cahiers Nr.3. Sum of Table 3.1 "Balaans Total" Handelsbanken, Table 4 "Balaans Total" Landbouwkredietbanken, Table 5 "Balaans Total" Algemene Spaarbanken, Table 6 "Balaans Total" Rijkspostspaarbank, Table 7 "Balaans Total" Hypothekbanken. Levels.
  - 1982–2014: De Nederlandsche Bank (2012), Domestic MFI–statistics (monetary). Table T5.2 "Balance sheet of MFIs in the Netherlands (excluding DNB): not adjusted for securitisations". "Total Assets", Levels.
  - 2015–2020: De Nederlandsche Bank, Table 5.2, Balance sheet of Dutch-based MFIs (not including DNB) (break-adjusted), series "Total Assets". Chainlinked.
- Capital (converted to millions NLG):
  - 1900–1981: De Nederlandsche Bank (2000), DNB Statistische Cahiers Nr.3. Sum of Table 3.1 "Kapitaal en reserves" Handelsbanken (adjusting for accounting change in 1976 by splicing with difference in capital ratio), Table 4 "Kapitaal en reserves" Landbouwkredietbanken, Table 5 "Kapitalreserves" Algemene Spaarbanken, Table 6 "Reserves" Rijkspostspaarbank, Table 7 "Kapital en reserves" Hypothekbanken. Levels.
  - 1982–2014: De Nederlandsche Bank, Domestic MFI–statistics (monetary). Table T5.2. Series "Capital and reserves". Levels.
  - 2015–2020: De Nederlandsche Bank, Table 5.2 (break-adjusted), series "Capital and reserves". Chainlinked.

*Loans-to-Deposits ratio* (`ltd`) — pp.133–134
- Deposits:
  - 1900–1981: De Nederlandsche Bank (2000), DNB Statistische Cahiers Nr.3. Sum of Table 3.1 "23-25 Binnenlandse liquiditeiten", Handelsbanken, Table 4 "Giraletegoeden (29) + Deposito's (30) and Spaargeld (33)", Landbouwkredietbanken, Table 5 "Spaartegoeden (23), Termijin spaar rekening (24), Spaargiro tegoeden (31)" Algemene Spaarbanken, Table 6 "Spaartegoeden (24), Termijin spaarrekeningen (30)" after 1978 "Spaartotaal (25)" Rijkspostspaarbank. Chainlinked as a share in total debt (difference in 1982).
  - 1982–2014: De Nederlandsche Bank (2012), Domestic MFI–statistics (monetary). Table T5.2 (http://www.dnb.nl/en/statistics/statistics-dnb/financial-institutions/banks/domestic-mfi-statistics-monetary/index.jsp). "Deposits of euro area residents – total" minus "Deposits of euro area residents – MFIs". Levels.
  - 2015–2020: De Nederlandsche Bank, Table 5.2 (break-adjusted), series "Deposits – of which residents of the euro area – Total" less "Deposits – of which residents of the euro area – MFIs". Chainlinked.
- Loans:
  - 1900–1981: De Nederlandsche Bank (2000), DNB Statistische Cahiers Nr.3.
  - 1982–2013: De Nederlandsche Bank (2012), Domestic MFI–statistics (monetary). Table T5.2, Table 5.2.1 "Loans from MFIs to the private sector, breakdown by sector, original maturity and instrument; not adjusted for securitisations".
  - 2014–2020: De Nederlandsche Bank, Table 5.2 (break-adjusted), series "Loans – of which residents of the euro area – Total" less "Loans – of which residents of the euro area – MFIs". Chainlinked.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.134.

### NORWAY (ISO NOR) — pages 134–143. "(Data in millions NOK)"

**Population** (`pop`) — p.134: Maddison (2008) 1870–2008; IMF (2019) WEO growth rates 2009–2017; IMF (Oct 2021) WEO 2018–2020 (base year 2008).

**GDP (millions NOK)** (`gdp`) — p.135
- 1870–2003: Ola H. Grytten, The gross domestic product for Norway 1830–2003, chapter 6, in: Eitrheim et al. (2004), Historical Monetary Statistics for Norway, 1819–2003, Norges Bank. Note: gaps between 1940–1945.
- 2004–2020: IMF (2021), IFS, Data Report "National Accounts", Series "Gross Domestic Product, Nominal".

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.135: standard block.
**Real GDP per capita (index, 2005=100)** — p.135: standard block (World Bank 2019).
**Real consumption per capita (index, 2006=100)** — p.135: standard block.

**Investment-to-GDP ratio** (`iy`) — p.135
- 1870–2014: Ola H. Grytten, "The gross domestic product for Norway 1830–2003," chapter 6, in: Eitrheim et al. Series: Gross investments divided by GDP. Note: gaps between 1940–1945. http://www.norges-bank.no/en/Statistics/Historical-monetary-statistics/Gross-domestic-product/
- 2015–2020: IMF (2019), WEO. Subject "Total Investment – Percentage of GDP".

**Consumer prices (index, 1990=100)** (`cpi`) — p.135
- 1870–2020: Norges Bank Historical Monetary Statistics. Series: CPI for Norway, annual figures from 1516 (https://www.norges-bank.no/en/topics/Statistics/Historical-monetary-statistics/Consumer-price-indices/).

**Narrow Money (millions NOK)** (`narrowm`) — p.136
- 1870–2003: Jan T. Klovland, Monetary Aggregates in Norway 1819–2003, chapter 5, in: Eitrheim et al.
- 2004–2016: average of monthly series for M0; Norges Bank statistics, Historical statistics, money, credit and banking aggregates, Table_a2, M0 monetary base excluding Treasury deposits (www.norges-bank.no).
- 2017–2020: Statistics Norway, Economy, banking and financial markets, financial indicators, monetary aggregates, Base money M0, average of monthly series.

**Broad Money (millions NOK)** (`money`) — p.136
- 1870–2003: Jan T. Klovland, Monetary Aggregates in Norway 1819–2003, chapter 5, in: Eitrheim et al.
- 2004–2016: average of monthly series for M2; Norges Bank, Table_a2, M2 broad money.
- 2017–2020: Statistics Norway, monetary aggregates, M2, average of monthly series.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.136
- 1870–2016: Norges Bank. Historical Monetary Statistics (2019). Short-term interest rates. Excel file: Short term interest rates in Norway from 1818. Tab: p2c7_table_7A1. Series: Marginal liquidity rate. https://www.norges-bank.no/en/topics/Statistics/Historical-monetary-statistics/Short-term-interest-rates/ Level. (Note: no data 1966).
- 2017–2020: Norges Bank. Nowa (Norwegian Overnight Weighted Average) annual average. Chain-linked.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — p.136
- 1870–1929: Norges Bank. Historical Monetary Statistics for Norway. Interest rates, Bond yields, Yields on most actively traded maturities of long-term government bonds. http://www.norges-bank.no/en/statistics/historical-monetary-statistics/
- 1930–1947: Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition.
- 1948–2020: IMF IFS, Section "Interest rates", Series "Government Bonds, percent per Annum".

**Current Account (millions NOK)** (`ca`) — pp.136–137
- 1870–1939: M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103 (http://www.nber.org/databases/jones–obstfeld/).
- 1946–2010: B. Mitchell (2013), IHS. Series: Overall current balance.
- 2011–2020: IMF WEO. % of GDP × nominal GDP = Current Account.

**Imports & Exports (millions NOK)** (`imports`, `exports`) — p.137
- 1870–1947: B. Mitchell (2007), IHS: Europe 1750–2005.
- 1948–2020: IMF IFS archive, M10 2021, External Trade.

**Government Revenues (millions NOK)** (`revenue`) — p.137
- 1870–1943: Statistics Norway (various), Statistical Yearbook of Norway (various issues) (http://www.ssb.no/a/en/histstat/main.html).
- 1949–1974: Statistics Norway (1978), Historical Statistics 1978. Table 243 "Revenue and expenditure of the central government mill kroner," Series "Revenue –Total" (http://www.ssb.no/a/histstat/hs1978/hs1978.pdf).
- 1975–1994: Statistics Norway (1994), Historical Statistics 1994 (http://www.ssb.no/a/en/histstat/tables.html).
- 1995–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTR.
- [note] gap 1944–1948.

**Government Expenditure (millions NOK)** (`expenditure`) — pp.137–138
- 1870–1913: Statistics Norway (various), Statistical Yearbooks.
- 1914–1945: Mitchell, B. (2013). IHS. Government expenditure.
- 1946–1976: Statistics Norway (1978), Historical Statistics 1978. Table 243, Series "Expenditure –Total".
- 1977–1992: Statistics Norway (1994), Historical Statistics 1994. Table 23.11 Series: Current expenditure total (https://www.ssb.no/a/histstat/tabeller/23-23-11.txt). Level.
- 1993–1994: Statistics Norway. Public Sector – general government revenue and expenditure. Series: Current expenditure. (statistikkbanken, MainTable=OffForvIU3).
- 1995–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTE.

**Public debt-to-GDP ratio** (`debtgdp`) — p.138
- Note (verbatim): "Data for 1870–1979 is for central government debt; data thereafter is for general government debt. (Note: no data for 1940-1946)."
- 1880–1885: Statistics Norway, Statistical Yearbook, various issues.
- 1886–1913: Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform.
- 1914–1931: United Nations (1948). Public Debt, 1914–1946. Department of Economic Affairs, Lake Success, NY.
- 1932–1975: Statistics Norway (1978): "Historisk Statistikk". Table 242. p. 453. Column: Total, divided by GDP from JST dataset. Level.
- 1976–1978: Statistics Norway (1994). "Historisk Statistikk". Table: Offentlig forvaltning Tabell 23.12. Statsforvaltningen. Fordringer og gjeld pr 31. desember, etter finansobjekt. Mill. kr / Central government. Assets and liabilities as of 31 December, by financial instrument. Million kroner. Series: Gjeld i alt, divided by GDP from JST dataset. http://www.ssb.no/a/histstat/tabeller/23-23-12.txt
- 1979–1999: Statistics Norway, Historical Tables, General Government, Table 1: General government. Financial balance sheet per 31 December at nominal value, by financial instrument and debtor/creditor sector, including reconciliation items. 1986-1992. Million kroner. Series: General government gross debt % of GDP. (http://www.ssb.no/a/english/kortnavn/offogjeld_en/histtab.html).
- 2000–2013: Eurostat – Quarterly General Government Consolidated Gross Debt, end of year (http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=gov_q_ggdebt&lang=en).
- 2014–2020: IMF WEO, Subject "General Government Gross Debt – Percentage of GDP".
- [note] series starts 1880, not 1870.

**USD exchange rate (local currency/USD)** (`xrusd`) — p.138
- 1870–1939: Norges Bank. Historical Monetary Statistics. Table: Historical Exchange Rates. December values.
- 1940–1945: Bordo & Jonung (1996).
- 1946–1957: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1958–2020: IFS, IMF eLibrary. "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy / Strict peg dummy** — p.139: standard block.
**Exogenous monetary policy shocks** — p.139: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.139
- 1870–2012: Knoll et al. (2014). Year average values.
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — pp.139–140
- 1904–1919, 1940, 1941, 1946–1949, 1980 and 1981: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table B2 Europe: Unemployment. Chainlinked.
- 1920–1939: Grytten, Ola Honningdal. Economic policy and labour markets in Nordic countries during the great depression of the 1930s. In: XIV International Economic History Congress, Helsinki. 2006.
- 1950–1979: Maddison, Angus (1982), Phases of Capitalist Development. Table 6 – Unemployment as a percentage of total labour force. Oxford University Press. Chainlinked.
- 1982–2020: ILOSTAT (2020), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.140
- 1870–1989: Øyvind Eitrheim, Jan T. Klovland and Jan F. Qvigstad "HISTORICAL MONETARY STATISTICS FOR NORWAY – PART II". Chapter 6 Norwegian wages 1726–2006 classified by industry" Total. Average national nominal wage. Chainlinked.
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (millions NOK)**

**Total loans to non-financial private sector** (`tloans`) — p.140
- 1870–2014: Norges Bank statistics (www.norges-bank.no). Statistics – HISTORICAL MONETARY STATISTICS FOR NORWAY (O. Eitrheim, O.H. Grytten and J.T. Klovland (2007), Chapter 7: Historical Monetary Statistics for Norway – some cross checks of the new data, p 385–434 in O. Eitrheim, J.T. Klovland and J.F. Qvigstad (2007), Historical Monetary statistics for Norway – Part II, Norges Bank Occasional Papers No 38, Oslo.) Table "Total credit, end of year (1000NOK)", Series "Private banks", Series "State lending institutions", Series "Norges bank total loans".
- 2015–2020: calculated from Statistics Norway, Table 06718: "Domestic loan debt, by borrower, lender and currency (NOK million)". Sum of loans from banks, state lending institutions and mortgage companies to Households and Non-financial corporations. Value at the end of the year. (NOK + Foreign exchange) (https://www.ssb.no/en/statbank/list/kredind/).

**Mortgage loans to non-financial private sector** (`tmort`) — p.140
- 1870–1899: growth rate calculated from Eitrheim, Grytten and Klovland (2007), ibid. Table "Total credit, end of year (1000NOK)", Series "Mortgage loans".
- 1900–1974: Central Bureau of Statistics of Norway (1948), Statistical Survey 1948, Oslo. Series "Mortgages from savings banks, commercial banks and state housing banks"; and Central Bureau of Statistics of Norway (1978), Statistical Survey 1978, Oslo. Series "Mortgages from savings banks, commercial banks and state housing banks".
- 1975–1977: calculated using previous year × 1.25. [note: an assumed 25% growth for three years.]
- 1978–2020: sum of Mortgage Loans to Households and Total Loans to Business Secured by Real Estate.

**Mortgage loans to business** (no dataset column; component of `tmort`) — pp.140–141
- 1978–1991: chain-linked with total business lending.
- 1992–1997: Norges offisielle statistikk Låne- og verdipapirmarkedet 1992-1998; Statistisk sentralbyrå, Statistics Norway, table 5 Oslo–Kongsvinger.
- 1998–2008: SSB. Real estate, renting and business activities (8). Banks. Loans (utilized) by borrower sector. Mill. NOK. http://www.ssb.no/english/subjects/10/13/10/orbofbm_en/arkiv/tab-004-en.html
- 2009–2017: Statistics Norway. Tables 71 and 81; total real estate; non-financial corporations. http://www.ssb.no/orbofbm_en/ and Financial corporations, balance sheet – Banks, Mortgage Companies and State Lending Institutions – Loans Secured on Dwellings – Non-financial corporations.
- 2018–2020: Statistics Norway. Sum of: From table "Financial corporations. Loans (NOK million), by month, contents, financial corporations and debt by industry": Real estate, renting and business activities Banks, Mortgage Companies and State Lending Institutions + table "Loans by type and sector (NOK million), by month, contents, financial corporations, type of loans and borrower sector": Repayment loans secured on dwellings from Banks, Mortgage Companies and State Lending Institutions. https://www.ssb.no/en/statbank/list/banker

**Total Loans to Households** (`thh`) — p.141
- 1978–2020: residual of Total loans to non-financial private sector and Total Loans to Business.

**Loans to Households Secured by Real Estate** (no dataset column; component of `tmort`) — p.141
- 1978–2017: calculated from Statistics Norway (2015), Table "Gross domestic debt, by credit source and borrower and broken down by NOK and foreign exchange" (NOK million) Series: Loans secured on dwellings- households (1.1). Actual stock figures (NOK+Foreign exchange) (http://www.ssb.no/english/).
- 2018–2020: Statistics Norway. From table "Loans by type and sector (NOK million), by month, financial corporations, type of loans, borrower sector and contents": Repayment loans secured on dwellings Banks, Mortgage Companies and State Lending Institutions. https://www.ssb.no/en/statbank/list/banker

**Total Loans to Business** (`tbus`) — p.141
- 1978–1986: calculated from Statistics Norway (2000), The Loan and Securities Market 1992–1998, Statistics Norway, Oslo. Table 2, Series "Households etc" p28 (http://www.ssb.no/emner/11/01/nos_c589/nos_c589.pdf).
- 1987–2020: calculated from Statistics Norway, Table 06718: "Domestic loan debt, by borrower, lender and currency (NOK million)". Sum of loans from banks, state lending institutions and mortgage companies to Non-financial corporations. Value at the end of the year. (NOK + Foreign exchange) (https://www.ssb.no/en/statbank/list/kredind/).

**Corporate Debt** (`bdebt`) — pp.141–142
- 1872–1939: bank lending to non-financial business sector proxied by commercial bank lending from Historical Monetary Statistics for Norway.
- 1940–1974: lending to non-financial corporate business from Karsten Müller (2018) "Credit Markets around the World, 1910–2014", SSRN.
- 1975–1994: BIS "Credit to the non-financial sector" (bank loans to business and capital market debt).
- 1995–2013: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2019: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector. [note: ends 2019.]

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions NOK)"

*Capital ratio* (`lev`) — p.142
- Total Assets (millions NOK):
  - 1870–2015: Norges Bank statistics. Historical Monetary Statistics for Norway (Eitrheim, Grytten and Klovland (2007), Chapter 7, p 385–434 in Eitrheim, Klovland and Qvigstad (2007), Norges Bank Occasional Papers No 38, Oslo). Table "Bank Balance – Private Banks", Series "Total Assets".
  - 2016–2020: Statistics Norway, Financial corporations. Balance sheet (NOK million), by financial corporations, balance sheet, contents and month. Series 25, Total Liabilities and Equity. Chainlinked.
- Capital (millions NOK):
  - 1870–2015: Norges Bank statistics, same source. Table "Bank Balance – Private Banks", Series "Equity".
  - 2016–2020: Statistics Norway, Financial corporations. Balance sheet (NOK million). Series 24, Total Equity. Chainlinked.

*Loans-to-Deposits ratio = Loans/Deposits* (`ltd`) — p.143
- Deposits (millions NOK):
  - 1870–2015: Norges Bank statistics, same source. Table "Bank Balance – Private Banks", Series "Deposits".
  - 2016–2020: Statistics Norway, Financial corporations. Balance sheet (NOK million). Series 12, Deposits from customers. Chainlinked.
- Loans (millions NOK):
  - 1870–2015: Norges Bank statistics, same source. Table "Bank Balance – Private Banks", Series "Loans".
  - 2016–2020: Statistics Norway, Financial corporations. Balance sheet (NOK million). Series 03, Loans to and claims on customers. Chainlinked.

*Noncore ratio = Other liabilities / (Total Assets − Capital)* (`noncore`) — p.143. [note: Norway's formula differs from the other countries' (Total Assets − Capital − Deposits)/(Total Assets − Capital).]

### PORTUGAL (ISO PRT) — pages 143–154. "(Data in millions PTE)"

**Population** (`pop`) — pp.143–144
- 1870–1849 [sic; printed "1870 – 1849", evidently 1870–1949]: Angus Maddison Database (2012), ibid Table 1 "Population levels, 1AD–2030AD".
- 1950–2011: OECD (2012), OECD.Stat Extracts. Section "Demography and population", Subsection "Population statistics", Table "Population", Subject "Population (hist5), all ages, all persons" (http://stats.oecd.org/).
- 2012–2017: growth rates from IMF (Aug, 2019) WEO, "People – population" (base year: 2011).
- 2018–2020: growth rates from IMF (Oct, 2021) WEO (base year: 2011).

**GDP (converted millions to PTE)** (`gdp`) — p.144
- 1870–1953: N. Valério (ed.) (2001), Portuguese Historical Statistics 2 vol., Instituto Nacional de Estatística, Lisbon. Table 6.6 C. Series "Produto interno bruto preços correntes". Levels.
- 1954–1971: N. Valério (ed.) (2001), Table 6.6 B. Series "Produto interno bruto". Levels.
- 1972–2020: OECD.Stat: National Accounts – Main Aggregates – Gross domestic product (GDP). Series: Gross domestic product (annual). Levels.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.144: standard block.
**Real GDP per capita (index, 2005=100)** — p.144: standard block (World Bank 2018).
**Real consumption per capita (index, 2006=100)** — p.144: Barro–Ursúa 1910–2009 [note: starts 1910]; World Bank 2010–2020.

**Investment-to-GDP ratio** (`iy`) — pp.144–145
- 1953–1976: Bank of Portugal (gross fixed capital formation plus change in inventories divided by GDP, for data series see N. Valério (ed.) (2001), Portuguese Historical Statistics 2 vol., Table 6.4 B). Divided by GDP from N. Valério (ed.) (2001), Table 6.6 B. Series "Produto interno bruto".
- 1977–2020: IMF IFS Data Report "National Accounts", Series "Gross Fixed Capital Formation" (https://data.imf.org/). Divided by the nominal GDP series from IMF IFS.
- [note] series begins 1953.

**Consumer prices (index, 1990=100)** (`cpi`) — p.145
- 1870–1997: N. Valério (ed.) (2001), ibid. Table 8.1.
- 1998–2020: IMF WEO (April 2019). "Inflation, average consumer prices". Chainlinked.

**Narrow Money (converted millions to PTE)** (`narrowm`) — p.145
- 1870–1990: N. Valério (ed.) (2001), ibid. Table 7.4B "Money Supply 1834–1993: B–Immediate means of payment (M1)", Series "according to Mata, Valério, 1993".
- 1991–2017: Bank of Portugal. Séries cronológicas – Principais indicadores – Agregados monetários – Portugal – Contribuição de Portugal para o agregado M1, excl. circulação monetária – Saldos (Portuguese contribution for M1, excluding currency in circulation) (bportugal.pt EstatisticasWeb).
- 2018–2020: Bank of Portugal, Data domains, Monetary and financial aggregates, Data tables, Monetary aggregates, Portugues contribution to monetary aggregates | end-of-period value and a.r.c., PRT contribution for M1-Euro area-M€ (MFI) – PRT contribution for M1-Currency circulation-Euro area-M€ (MFI).

**Broad Money (converted millions to PTE)** (`money`) — pp.145–146
- 1870–1912: Nunes, A.B., Valério, N. and Martins de Sousa, R. "The long-run behaviour of the income velocity of money in Portugal: 1854-1992. Table in appendix. Column M2.
- 1913–1990: N. Valério (ed.) (2001), ibid. Table 7.4C "Money Supply 1834–1993: C–Money in the broad sense (M2) or total means of payment (L)", Series "According to Mata, Valério, 1993". Level.
- 1991–2017: Bank of Portugal. Séries cronológicas – Agregados monetários – Contribuição de Portugal para o agregado M2, excl. circulação monetária – Saldos (Portuguese contribution for M2, excluding currency in circulation).
- 2018–2020: Bank of Portugal, Monetary aggregates, PRT contribution for M2-Euro area-M€ (MFI) – PRT contribution for M1-Currency circulation-Euro area-M€ (MFI).

**Short-term Interest rate (nominal, percent per year)** (`stir`) — p.146
- 1880–1884: Olivier Accominotti, Marc Flandreau, and Riad Rezzik's "The Spread of Empire: Clio and the Measurement of Colonial Borrowing Costs".
- 1885–1914: Neal & Weidenmier (2003), Open Market Rate, Monthly, End of Year Value.
- 1915–1947: Valério, N. (2001). História Económica de Portugal. Uma Perspectiva global. Table 7.10. Series: discount rates.
- 1948–1977: IMF (2014), IFS. Series "Discount Rate".
- 1978–1987: IMF (2014), IFS. Series "Interbank Deposit".
- 1988–2017: Federal Reserve Bank of St. Louis; 3-Month or 90-day Rates and Yields: Interbank Rates for Portugal, Code: IR3TIB01PTA156N.
- 2018–2020: OECD, short term interest rate, % per annum, average of monthly values.
- [note] starts 1880.

**Long-term Interest rate (nominal, percent per year)** (`ltrate`) — pp.146–147
- 1870–1879: sum of "Yield on consols" (BoE, Three centuries) and "Spread on consols" (Clemens & Williamson 2004).
- 1880–1913: Accominotti, Flandreau, and Rezzik, "The Spread of Empire: Clio and the Measurement of Colonial Borrowing Costs".
- 1914–1925: Investor's Monthly Manual. Portuguese 3% 1st yield to maturity. Final redemption: 2001. Current yield.
- 1926–1930: Statistisches Handbuch der Weltwirtschaft 1936. Kurs der 3% konsolid. Inneren Staatsanleihe (vH des Nominalwerts). Current yield. December values.
- 1931–1947: Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition.
- 1948–1973: IMF (2014), IFS, Series "Government Bonds".
- 1974–1975: Bank of Portugal (2014), Bank of Portugal Statistics. Series "Yield on fixed rate treasury bonds – 10–years (monthly average)".
- 1976–2016: IMF (2019), IFS, Series "Government Bonds".
- 2017–2020: OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en.

**Current Account (converted millions to PTE)** (`ca`) — p.147
- 1870–1947: B. Mitchell (2013), IHS: Europe 1750–2010. Calculated as Exports − Imports. [note: trade balance proxy.]
- 1948–1998: N. Valério (ed.) (2001), Table 10.3 "Balança de Pagamentos 1946-1998", Series: "transacções correntes." Level.
- 1999–2020: IMF (2021). IFS. Supplementary Items, Current Account, Net (excluding exceptional financing), US Dollars. Turned into PTE with exchange rate from JST dataset. Level.

**Imports & Exports (converted millions to PTE)** (`imports`, `exports`) — p.147
- 1870–1949: B. Mitchell (2013), IHS: Europe 1750–2010. Levels.
- 1950–1953: Bank of Portugal, Series: Quadro 10.1 – "Importacoes"/"Exportacoes", in N. Valério (ed.) (2001).
- 1954–1969: Bank of Portugal, Series "Imports and exports of goods and services", in N. Valério (ed.) (2001), Table 6.4 B.
- 1970–2020: OECD (2021), OECD.StatExtracts. Path "Portugal, National accounts, GDP (Expenditure Approach)", Series B1_GE_P6 "Exports of goods and services", Series B1_GE_P7 "Imports of goods and service" in "Current prices, domestic currency".

**Government Revenues (converted millions to PTE)** (`revenue`) — p.147
- 1870–1989: N. Valério (ed.) (2001), ibid. Table 9.2. – tax revenue + other effective income.
- 1990–2020: Banco de Portugal, BPStats. E.2.1 – State revenue and expenditure – Current revenue, Series "Total revenue (state = central government)". December values.

**Government Expenditure (converted millions to PTE)** (`expenditure`) — p.147
- 1870–1989: N. Valério (ed.) (2001), ibid. Table 9.2.
- 1990–2020: Banco de Portugal, BPStats. Table: E.2.1 – State revenue and expenditure – Current expenditure, Series Total expenditure (state = central government), December values.

**Public debt-to-GDP ratio** (`debtgdp`) — p.148
- 1870–1972: Valério, Nuno (Ed.), Portuguese Historical Statistics, Lisbon, INE, Table 9.7, "Public Debt, 1850–1997". Divided by GDP from same source: Table 6.6 C "Produto interno bruto preços correntes" and Table 6.6 B "Produto interno bruto".
- 1973–2020: European Commission AMECO, Gross Public Debt (linked series) (UDGGL), % of GDP at market prices (EDP).

**USD exchange rate (local currency/USD)** (`xrusd`) — p.148
- 1870–1890: Esteves, R., J. Reis and F. Ferramosca (2009) "Market Integration in the Golden Periphery. The Lisbon/London Exchange, 1854-1891" Explorations in Economic History 46(3): 324-345. Market exchange rate: Lisbon rate on London, 1 month's usance 1854-1876; 1 week's usance (some exceptions) 1876-1882; sight (some exceptions) 1882-1891; single quotation to 3 February 1889, average of bid and ask rates from 10 February 1889 onward.
- 1891–1920: Valério, Nuno (Coordination), 2001. Estatísticas Históricas Portuguesas. Chapter 10; Table 10.6.
- 1921–1941: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1942–1945: Valério (2001), Chapter 10; Table 10.6.
- 1946–1955: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1956–2020: IFS, IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- Note: escudo–euro exchange rate of 200.482 assumed where necessary (text reads "a Italian Portugese escudo-euro exchange rate").

**Peg dummy / Strict peg dummy** — pp.148–149: standard block.
**Exogenous monetary policy shocks** — p.149: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.149
- 1988–2020: OECD housing prices database. Nominal series. Rebased 1990=100. [note: starts 1988 only.]

**Unemployment rate (percent)** (`unemp`) — p.149
- 1953–1974: Banco de Portugal, "Séries longas para a economia portuguesa – pós II Guerra Mundial", "Parte IV – População, Emprego e Desemprego" (https://www.bportugal.pt/sites/default/files/anexos/series/sl-populacao-metodologias.pdf). Chainlinked.
- 1975–1985: ILOSTAT (2020), "Unemployment rate by sex and age" based on the Labor Force Survey (1974-1985). Chainlinked.
- 1986–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — pp.149–150
- 1870–1913: Nuno Valério (2001). Estatísticas Históricas Portuguesas. Quadro 8.2 Salários. Agricultural nominal wage (average of 15 different activities) (Martins). Assumed no wage growth for the year of 1913. Chainlinked.
- 1914–1929: Valério (2001). Quadro 8.2 Salários. Nominal Wage (Branco). Chainlinked.
- 1930–1937: IHS. Europe's Labour Force – Money/Wages in Agriculture. Daily wages. Chainlinked.
- 1938–1952: Valério (2001). Quadro 8.2 Salários. Average of 25 different job wages in Lisbon (Pimenta). Chainlinked.
- 1953–1960: IHS. Europe's Labour Force – Money/Wages in Industry. Daily wages. Chainlinked.
- 1961–1985: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1986–1991: IMF IFS, Labor Markets, Manufacturing Wage Rates, Index. Chainlinked.
- 1992–1995: PORDATA. Salários – Emprego – Remuneração e ganho. Monthly average wage (www.pordata.pt). Chainlinked.
- 1996–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (converted millions to PTE)**

**Total loans to non-financial private sector** (`tloans`) — p.150
- 1870–1892: N. Valério (2001), ibid.; Table 7.7 A "Loans banks, bankers, banking houses".
- 1893–1903: Statistics Portugal (various), Statistical Yearbook of Portugal (various issues). Series "Secured loans".
- 1920: growth rate calculated from N. Valério (2001), ibid. Series "Banks, bankers, banking houses: Current accounts and secured loans".
- 1921–1929: calculated from Statistics Portugal (various), Statistical Yearbook of Portugal, Table "Situação Bancaria, bancos, empréstimos e contas correntes com caução", Series "Vias de Comunicação, Circulação e Crédito" plus series "Total Loans Secured by Real Estate".
- 1930–1946: sum of Statistics Portugal (various), Situação Bancaria/Estatísticas Financeiras (various issues), Table "Situação bancária em 31 de Dezembro de [respective year] (Bancos e restantes entidades que exercem o comércio bancário)", Series "Carteira comercial (commercial portfolio)" + Series "Contas correntes e empréstimos caucionados (Current Accounts and Secured Loans plus series "Total Loans Secured by Real Estate."
- 1947–78: Bank of Portugal (2009), ibid. Section "Monetary and financial statistics", Table "Monetary survey", Series "Loans to non–financial corporations and households".
- 1979–1982: Bank of Portugal, BPStat. Section "Monetary and financial statistics", Chapter "Monetary survey", Series "Domestic credit to NFC" + Series "Domestic credit to private individuals".
- 1983–2020: Bank of Portugal BPStat. Section "Monetary and financial statistics", Monetary and financial institutions' balance sheet", Series "Loans-NFC-PRT-M€ (OMFI)" + "Loans-Households and NPISH-PRT-M€ (OMFI)" (https://bpstat.bportugal.pt/dados/dominios/19/series).
- [note] gap 1904–1919 implied.

**Mortgage loans to non-financial private sector** (`tmort`) — p.151
- 1920–1929: Statistics Portugal (various), Statistical Yearbook of Portugal. Table "Situação Bancaria, caixas e companhias de crédito, empréstimos e contas correntes com caução", Series "Vias de Comunicação, Circulação e Crédito".
- 1930–1938: Statistics Portugal (various), Situação Bancaria (various issues). Table "Situação bancária em 31 de Dezembro de [respective year] (Bancos e restantes entidades que exercem o comércio bancário)" or Table "Bancos, caixas económicas, companhias de crédito, sociedades por cotas e em nome colectivo e firmas individuais (continente e ilhas). Saldos reunidos em 31 de Dezembro de [respective year] e [respective year], Hipotecários".
- 1939–1961: Statistics Portugal (various), Situação Bancaria / Estatísticas Financeiras (various issues). Same tables, "Hipotecários".
- 1962–1982: growth rate calculated from N. Valério (2001), ibid. Series "Mortgages".
- 1983–2017: Bank of Portugal, BPStat. Section "Monetary and financial statistics", Chapter "Details of the assets of other monetary and financial institutions vis–à–vis residents", Table "Loans of other monetary financial institutions to private individuals", Series "Housing".
- 2018–2020: Bank of Portugal, BPStat. Data Domain "Monetary and financial", Data sub-domain "Monetary financial institutions' balance sheet", Statistical Series "Loans-Households and NPISH-PRT-House purchase-M€ (OMFI)", December values.

**Total Loans to Households** (`thh`) — p.151
- 1979–2020: Bank of Portugal BPStat. Section "Monetary and financial statistics", Monetary and financial institutions' balance sheet", Series "Loans-Households and NPISH-PRT-M€ (OMFI)" (https://bpstat.bportugal.pt/dados/dominios/19/series).

**Total Loans to Business** (`tbus`) — p.151
- 1979–2020: Bank of Portugal BPStat. Series "Loans-NFC-PRT-M€ (OMFI)".

**Corporate Debt** (`bdebt`) — pp.151–152
- 1947–1978: lending to non-financial corporate business from Karsten Müller (2018) "Credit Markets around the World, 1910–2014", SSRN.
- 1979–1994: BIS "Credit to the non-financial sector" (bank loans to business and capital market debt).
- 1995–2013: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2019: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions PTE)"

*Capital ratio* (`lev`) — pp.152–153
- Total Assets (converted millions to PTE):
  - 1920–1930: Jaime Reis, Chapter 7 – Money and Credit in "Nuno Valério, Portuguese Historical Statistics". Table 7.7 — Banks, bankers and banking houses, 1858-1892, 1919-1990 (1929/1930 interpolated). Total Assets and Liabilities, Mainland. Chainlinked.
  - 1931–1960: Estatisticas Monetaria Financeiras (various issues). Series "Total" less series "Outras verbas do passivo", Bancos e Casas Bancario excluding Bank of Portugal. Chainlinked.
  - 1961: Jaime Reis, Chapter 7, Table 7.7. Total Assets and Liabilities, Mainland. Chainlinked.
  - 1962–1977: Estatisticas Monetaria Financeiras (various issues). Series "Total" less series "Contas de Ordem". "Bancos e casas bancario" excluding Banco Formento and Bank of Portugal. Chainlinked.
  - 1978–1996: Estatisticas Monetaria Financeiras. Commercial banks. Series "Total Assets", break-adjusted in 1982. Chainlinked.
  - 1997–2020: ECB Statistics, Series "Total Assets/Liabilities" BSI.M.PT.N.A.T00.A.1.Z5.0000.Z01.E.
- Capital (converted millions to PTE):
  - 1920–1930: Jaime Reis, Chapter 7, Table 7.7 (1929/1930 interpolated). Paid-up capital, Mainland. Chainlinked.
  - 1931–1961: Estatisticas Monetaria Financeiras (various issues). Series "Capital" + "Fundo de reserva". Bancos e casas bancario excluding Bank of Portugal. Chainlinked capital ratio (including Banco Formento in 1962 to adjust for break in 1961/1962).
  - 1962–1977: Estatisticas Monetaria Financeiras. Series "Capital e Reservas – Total" divided by Assets. "Bancos e casas bancario" excluding Banco Formento and Bank of Portugal. Chainlinked capital ratio.
  - 1978–1989: Estatisticas Monetaria Financeiras. Bancos comerciais. Table Balanco em 31 de Dezembro. Series "Capital" + series "Reservas" divided by "Activo – Actif" (break-adjusted in 1982). Chainlinked capital ratio.
  - 1990–1996: Estatisticas Monetaria Financeiras. Bancos comerciais. Table Balanco em 31 de Dezembro. Series "Capital subscrito" + series "Reservas" divided by "Activo – Actif". Chainlinked.
  - 1997–2006: ECB Statistical Data Warehouse, Capital ratio computed as "Capital and reserves, World not allocated (geographically), Unspecified counterpart sector" BSI.M.PT.N.A.T00.A.1.Z5.0000.Z01.E divided by "Total Assets/Liabilities, Total, World not allocated (geographically), Unspecified counterpart sector" BSI.M.PT.N.A.L60.X.1.Z5.0000.Z01.E. [note: the two SDW keys are printed this way in the PDF; the "T00" key is labelled capital here but total assets above.]
  - 2007–2020: ECB Consolidated Banking Data, series "Full sample (All banking groups / stand-alone banks irrespective of their accounting / supervisory reporting framework), Tangible equity [% of tangible total assets] (I3309), Percent (PC)".
- [note] bank ratios for Portugal begin in 1920.

*Loans-to-Deposits ratio* (`ltd`) — pp.153–154
- Deposits (converted millions to PTE):
  - 1920–1930: Jaime Reis, Chapter 7, Table 7.7 (1929/1930 interpolated). Deposits, Mainland. Chainlinked.
  - 1931–1950: Estatisticas Monetaria Financeiras (1950). Series "Depositos a prazo" + "Depositos a terme". "Bancos e casas bancario" excluding "Bank of Portugal". Chainlinked.
  - 1951–1961: Estatisticas Monetaria Financeiras (various). Series "Depositos a prazo" + "Depositos a ordem". "Bancos e casas bancario" excluding "Bank of Portugal". Chainlinked.
  - 1962–1977: Estatisticas Monetaria Financeiras (various issues). Series "Depositos a prazo – moeda nacional" + "Depositos a prazo – moeda estrangeira" + "Depositos a ordem – moeda nacional" + "Depositos a ordem – moeda estrangeira". "Bancos e casas bancario" excluding "Banco Formento" and "Bank of Portugal". Chainlinked.
  - 1978–1989: Estatisticas Monetaria Financeiras. Bancos comerciais. Table Balanco em 31 de Dezembro. Series "Depositos-Moeda Nacional". Chainlinked.
  - 1990–1992: Estatisticas Monetaria Financeiras. Bancos comerciais. Series "Debitos para com clientes". Chainlinked.
  - 1993–1996: Estatisticas Monetaria Financeiras. Bancos comerciais – nacionais + etrangeiros. Series "Debitos para com clientes". Chainlinked.
  - 1997–2020: ECB Statistical Data Warehouse, Deposit liabilities, Total, Euro area (changing composition), Non-MFIs excluding central government" BSI.M.PT.N.A.L20.A.1.U2.2300.Z01.E.
- Loans (converted millions to PTE):
  - 1920–1930: Jaime Reis, Chapter 7, Table 7.7 (1929/1930 interpolated). Loans, Mainland. Chainlinked.
  - 1931–1960: Estatisticas Monetaria Financeiras (various). Series "Carteira commercial" + "Contas correntes" + "Devedores e credores". "Bancos e casas bancario" – less "Bank of Portugal". Chainlinked.
  - 1961: Chainlinked with growth rate of deposits.
  - 1962–1977: Estatisticas Monetaria Financeiras (various issues). Series "Carteira commercial" + "Emprestimos e contas". "Bancos e casas bancario" less "Banco Formento" and "Bank of Portugal". Chainlinked.
  - 1978–1996: Estatisticas Monetaria Financeiras. Bancos comerciais. Table Balanco em 31 de Dezembro. Series "Credit over clients". Adjusted for break in 1982. Chainlinked.
  - 1997–2020: ECB Statistical Data Warehouse, Loans vis-a-vis euro area non-MFI excl. general gov. reported by MFI excluding ESCB in Portugal (stock) BSI.M.PT.N.A.A20.A.1.U2.2200.Z01.E.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.154.

### SPAIN (ISO ESP) — pages 154–164. "(Data in millions ESP)"

**Population** (`pop`) — p.155
- 1870–2020: Leandro Prados de la Escosura, Spain's Historical National Accounts: Expenditure and Output. TABLE: Absolute and Per Capita Gross Value Added and Gross Domestic Product at market prices, 1850-2020. Series: Population. http://espacioinvestiga.org/bbdd-chne/?lang=en
- [note] Spain is the only country in this range whose population does not come from Maddison/IMF.

**GDP (converted to millions ESP)** (`gdp`) — p.155
- 1870–2020: Leandro Prados de la Escosura, Spain's Historical National Accounts: Expenditure and Output. TABLE 35: Gross Domestic Product and its Expenditure Components, 1850-2020.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** (`rgdpmad`) — p.155
- 1870–2020: Leandro Prados de la Escosura (2021), Spain's Historical National Accounts: Expenditure and Output, 1850-2016. TABLE 26. Real Per Capita Gross Domestic Product, 1850-2017 (GK $1990). [note: not Maddison-Project for Spain.]

**Real GDP per capita (index, 2005=100)** (`rgdpbarro`) — p.155
- 1870–2020: Prados de la Escosura (2021), TABLE 14. Volume Indices of Absolute and Per Capita Gross Domestic Product at market prices and Gross Value Added, 1850-2016. Rebased to 2005=100.

**Real consumption per capita (index, 2006=100)** (`rconsbarro`) — p.155
- 1870–2020: Prados de la Escosura, TABLES 1 (private consumption), 3 (population) and 7 (consumption deflator). Rebased to 2006=100.

**Investment-to-GDP ratio** (`iy`) — p.155
- 1870–2020: Prados de la Escosura, Spain's Historical National Accounts: Expenditure and Output, 1850-2015. TABLE 1. Gross Domestic Product and its Expenditure Components, 1850-2017. Gross Capital Formation divided by GDP.

**Consumer prices (index, 1990=100)** (`cpi`) — p.155
- 1870–1879: Albert Carreras and Xavier Tafunell. Estadísticas históricas de España: siglos XIX-XX. Vol. 3. Fundacion BBVA, 2005, p. 1289, Table Cuadro 16.19: Indices de precios, 1800-1958, series Maluquer de Motes.
- 1880–1996: A. Taylor (2002), A Century of Purchasing–Power Parity, REStat 84(1), pp. 139–150.
- 1997–2020: IMF WEO (2021). "Inflation, average consumer prices". Chainlinked.

**Narrow Money (converted to millions ESP)** (`narrowm`) — p.156
- 1874–1998: A. Carreras and X. Tafunell (eds.), Estadísticas Históricas de España, Madrid 2005. Table 9.16. Series: Oferta Monetaria. (Note: no data for 1936-1940). End of year values.
- 1999–2020: Bank of Spain, 1.14 – Euro area monetary aggregates and the contribution of MFIs resident in Spain to the aggregates, Agregados monetarios de la UEM. M1. Contribución de las IFM residentes en España. Saldos. End of year values. Chain-linked.

**Broad Money (converted to millions ESP)** (`money`) — p.156
- 1874–1978: Carreras and Tafunell (eds.), Estadísticas Históricas de España, Madrid 2005, table 9.16. Series: Disponibilidades Líquidas. (Note: no data for 1936-1940).
- 1979–1996: Carreras and Tafunell (2005), table 9.16. Series: M3.
- 1997–2020: Banco de Espana. Contribution of the MFIs resident in Spain to the euro area monetary aggregates and counterparts of M3 – Contribución de las IFM residentes en España a la M3 de la UEM. Saldos http://www.bde.es/webbde/en/estadis/infoest/bolest1.html

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.156
- 1870–1882: Bank of Spain archive; Stock listings; Bank of Spain discount rate; annual average of monthly values.
- 1883–1914: Neal & Weidenmier (2003), Open Market Rate, Monthly, End of Year Value.
- 1915–1919: Bank of Spain archive; Stock listings; Bank of Spain discount rate; annual average of monthly values.
- 1920–1923: Carreras, Albert and Xavier Tafunell, 2005, "Estadísticas históricas de Espana, Siglos XIX – XX, Volumen I," Fundación BBVA, Table 9.17. Descuento comercial.
- 1924–1941: League of Nations, International Statistical Yearbook (various issues), Geneva. Central Bank Discount Rate.
- 1942–1974: Carreras and Tafunell (2005), Table 9.17. Redescuento Básico.
- 1975–2020: IMF (2021), IFS, Series "Interest Rates – money market rate". To calculate the value for 2018 the growth rate from OECD short term interest rate series was used.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — pp.156–157
- 1870–1879: bond price quotations in newspapers: "Diario oficial de avisos de Madrid": Current Yield calculated from the bond price notations: Renta perpétua al 3 por 100, and from "La Correspondencia de Espana": Current Yield calculated from: 3 % consolidado; renta perp. 3%.
- 1880–1913: Accominotti, Flandreau, and Rezzik, "The Spread of Empire: Clio and the Measurement of Colonial Borrowing Costs".
- 1914–1935: Carreras and Tafunell (2005), Table 10.35. Series: Deuda perpetuo interior 4%.
- 1936: Instituto Nacional de Estadística (INE). Anuarios Estadísticos (various issues). Finanzas – Bolsa – Deudas del Estado, Cotizacion – 4 por 100 interior: Yield = 4/price. Chain linked to previous series.
- 1940–1971: INE. Anuarios Estadísticos. Finanzas – Bolsa – Deudas del Estado, Cotizacion – 4 por 100 interior: Yield = 4/price.
- 1972–1978: Average end of year yield on Spanish bonds. Data taken from Spanish newspaper ABC (http://hemeroteca.abc.es/nav/Navigate.exe/hemeroteca).
- 1979–2020: IMF (2021), IFS, Series "Government Bonds, Percent per Annum".
- [note] gap 1937–1939.

**Current Account (converted to millions ESP)** (`ca`) — p.157
- 1870–1913: L. Prados De La Escosura (2010), Spain's international position 1850–1913, Journal of Iberian and Latin American Economic History, 20(1), p. 173–215.
- 1931–1974: A. Tena Junguito (2007), New series of the Spanish foreign sector, 1850–2000, Working Papers in Economic History WP 07–14, Universidad Carlos III de Madrid. Note: gaps between 1935–1939.
- 1975–1992: IMF (2010), IFS. Table "Balance of payments", Series "Balances – current account balance".
- 1993–2020: IMF WEO. % of GDP × nominal GDP = Current Account.
- [note] gap 1914–1930.

**Imports & Exports (converted to millions ESP)** (`imports`, `exports`) — p.157
- 1870–2020: Leandro Prados de la Escosura, Spain's Historical National Accounts: Expenditure and Output. TABLE: Gross Domestic Product and its Expenditure Components.

**Government Revenues (converted to millions ESP)** (`revenue`) — pp.157–158
- 1870–1994: C.B. López, A. Carreras & X. Tafunell (2005), Estadísticas Históricas de España, Fundación BBVA, Bilbao. Note: gaps between 1936–1939.
- 1995–2020: OECD.Stat, Table 12, GS1311, Series GTR "Total general government revenue".

**Government Expenditure (converted to millions ESP)** (`expenditure`) — p.158
- 1870–1994: López, Carreras & Tafunell (2005). Note: gaps between 1936–1939.
- 1995–2020: OECD.Stat, Table 12, GS1311, Series GTE "Total general government expenditure".

**Public debt-to-GDP ratio** (`debtgdp`) — p.158
- 1880–1970: Carreras, Albert and Xavier Tafunell, 2005, "Estadísticas históricas de Espana, Siglos XIX – XX, Volumen I," Fundación BBVA, Series: Cuadro 12.34: "Deuda pública total en circulación," Note: gaps between 1936–1939, 1948–1949. Divided by GDP from JST dataset. Level.
- 1971–2020: European Commission AMECO, Gross Public Debt (linked series) (UDGGL), % of GDP at market prices (EDP). Level.

**USD exchange rate (local currency/USD)** (`xrusd`) — p.158
- 1870–1934: Carreras A. & Tafunell, X. (2005). Estadísticas históricas de Espana. Table 9.19.
- 1935–1941: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1942–1945: Carreras & Tafunell (2005). Table 9.19.
- 1946–1965: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1966–2020: IFS, IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).
- Note: peseta–euro exchange rate of 166.386 assumed where necessary (text reads "a Italian Spanish peseta-euro exchange rate").

**Peg dummy / Strict peg dummy** — pp.158–159: standard block.
**Exogenous monetary policy shocks** — p.159: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.159
- 1971–2020: OECD housing prices database. Nominal series. Rebased 1990=100. [note: starts 1971.]

**Unemployment rate (percent)** (`unemp`) — p.159
- 1933–1935 and 1939–1955: Instituto Nacional de Estadística. Database: "Anuarios Estadisticos". Verbatim method note: "For all available years, I collected the number of unemployed persons who had to quit their job in an involuntary manner (as the average of the monthly observations per year, when not possible I just took the December value of the series 'Numero de parados'). Then, I divided by a labor force measure 'población activa' whenever possible or by total population" (https://www.ine.es/inebase_historia/inebase_historia.htm). Chainlinked.
- 1956–1984: OECD (2015), OECD.Stat. Database: "Labour", "Labour Force Statistics", Dataset: "ALFS summary tables", "Annual labour force statistics" (http://stats.oecd.org/). Chainlinked.
- 1985–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.160
- 1870–1916 and 1932–1934: Albert Carreras de Odriozola, Xavier Tafunell Sambola (2006) Estadísticas históricas de España, siglos XIX-XX. Índices de salarios nominales de Madrid, Barcelona, Vizcaya y media nacional, 1800-1949. Average nominal wages in Madrid, Barcelona and Minas de Viscaya. Chainlinked.
- 1917–1931, 1935 and 1943–1962: Carreras de Odriozola, Tafunell Sambola (2006). Salario medio efectivo en la industria (pesetas por dia) (cuadro 15.23). National average industrial wage. Chainlinked.
- 1963–1989: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1990–2020: OECD. Average annual wages. Current prices. Levels.
- [note] gaps 1936–1942.

**Credit Data (converted to millions ESP)**

**Total loans to non-financial private sector** (`tloans`) — p.160
- 1900–1935: C.B. López, A. Carreras & X. Tafunell (2005), ibid. Table 9.12 & Table 9.13: "Prívate banks & cajas", Sum of series "Créditos y prestamos".
- 1946–1961: growth rate calculated from López, Carreras & Tafunell (2005), ibid. Table 9.13 "Prívate banks & cajas", Series "Créditos y prestamos".
- 1962–2020: Banco de España (2021), Boletin Estadistico Series Code D_BEEA1000 "Entidades de crédito. Crédito por grupos de entidades a otros sectores residentes. Total entidades de credito," (http://www.bde.es/webbde/en/estadis/infoest/bolest.html).
- [note] gap 1936–1945.

**Mortgage loans to non-financial private sector** (`tmort`) — pp.160–161
- 1904–1935: López, Carreras & Tafunell (2005), ibid. Table 6.11, Series "Prestamos Constituidos con Hipotecas sobre Fincas Urbanas", p497.
- 1946–1951: growth rate calculated from López, Carreras & Tafunell (2005), ibid. Table 6.11, same series, p497.
- 1952–1961: growth rate calculated from Instituto Nacional de Estadístico (1962) Anuario Estadístico de España 1962. Series "Secured Credits to Private Sector (Deudores con garantía real) from Private Banks" p217; and INE (1964) Anuario Estadístico de España 1964. Same series p236.
- 1962–1984: Banco de España (2012), Series 298310 "Entidades de crédito, OSR, deudores, con garantía real", Code BE_4_3.5 (http://www.bde.es/webbde/en/estadis/infoest/bolest.html).
- 1985: average of 1984 & 1986 (break in original series for unknown reason).
- 1986–2020: Banco de España (2021), Boletin Estadistico Series Code 615195 "Entidades de crédito. Activo. Otros sectores residentes en España. Deudores con garantía real. Del cual: Con garantía hipotecaria," (http://www.bde.es/webbde/en/estadis/infoest/bolest.html).

**Total Loans to Households** (`thh`) — p.161
- 1946–1982: growth rate calculated from Loans to Households Secured by Real Estate.
- 1983–1991: growth rate calculated from Banco de España (2012), Table BE0414, Series "Bancos, OSR, crédito para otras financiaciones a hogares por funciones de gasto".
- 1992–2020: Banco de España (2021), Statistical Bulletin, 4. Credit institutions and credit financial intermediaries, 4.13. Total lending and total doubtful loans to other resident sectors by type. Total to finance productive activity and breakdown by type of spending, Series Code D_MEE62000, "EC y EFC. Créditos a OSR por finalidades. Otra financiación a hogares por funciones de gasto. Total," (http://www.bde.es/webbde/en/estadis/infoest/bolest.html).

**Total Loans to Business** (`tbus`) — p.161
- Residual of Total loans to non-financial private sector and Loans to Households.

**Corporate Debt** (`bdebt`) — p.161
- 1904–1935: bank lending to business from Estadisticas Historicas de Espana, by Lopez, Carreras, and Tafunell (1989); table 9.12: Entitades de credito.
- 1946–1979: residual of total bank loans to non-financial private sector and total loans to households (both from JST MacroHistory Database).
- 1980–2012: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2013–2019: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions ESP)"

*Capital ratio* (`lev`) — pp.161–162
- Total Assets (converted to millions ESP):
  - 1874–1913: Tedde de Lorca, Pedro (1974), "La banca privada espanola durante la restauración (1874-1914)" in Gabriel Tortella (ed.): La banca espanola en la restauracion, Madrid, Banco de Espana, Servicio de Estudios, pp. 217-456, Series "Total Activo", chainlinked.
  - 1914: Pablo Martín Aceña and M.a Ángeles Pons, "Sistema monetario y financier" in Albert Carreras and Xavier Tafunell ed (2005), Estadisticas Historicas de Espana, Siglos XIX-XX. Chainlinked with sum of "Cuentas corrientes" and "Depósitos a plazo".
  - 1915–1935: José Luis García Ruiz, "Crisis Financiera en Espana 1930 - 1935", Cuadro 7, "Desarollo de los bancos locales espanoles de 1915 a 1935". Series "Total Activo". Excludes accounts under custody. Levels. (Comment: Almost match data in Carreras and Tafunell (2005), but balance sheet looks more consistent. Also matches data in "José Luis Malo de Molina and Pablo Martín-Aceña 'The Spanish financial system - Growth and development since 1900'").
  - 1942–1946: Martín Aceña and Pons, "Sistema monetario y financier" in Carreras and Tafunell (2005), "Total Activo y Passivo".
  - 1947–1961: Anuario Estadistico de la Banca Privada – Consejo Superior Bancario (issues 1974, 1975, 1976, 1977, 1978), Table Balances Totales, Series Suma el Pasivo.
  - 1962–2020: Boletin Estadistico, Bank of Spain, Aggregated balance sheet from supervisory returns, 4. Entidades de crédito y establecimientos financieros de crédito, Table 4.1, Column 1, Total Assets. Levels. (https://www.bde.es/webbde/en/estadis/infoest/bolest4.html)
  - [note] gap 1936–1941.
- Capital (converted to millions ESP):
  - 1874–1914: Tedde de Lorca (1974), sum of "Capital" and "Reservas", chainlinked via capital ratio (constant ratio in 1914/1915).
  - 1915–1935: García Ruiz, "Crisis Financiera en Espana 1930 - 1935", Cuadro 7. Series "Capital desembolsado" + "Reservas". Levels.
  - 1942–1946: Martín Aceña and Pons (2005), "Capital desembolsado", chainlinked.
  - 1947–1961: Anuario Estadistico de la Banca Privada – Consejo Superior Bancario (issues 1974–1978), Table Balances Totales, Sum of "Capital" and "Reservas". Chainlinked.
  - 1962–2020: Boletin Estadistico, Bank of Spain, 4. Entidades de crédito y establecimientos financieros de crédito, Table 4.7 Equity, valuation adjustments and impairment allowances, Column 2, Total Equity. Levels.

*Loans-to-Deposits ratio* (`ltd`) — pp.163–164
- Deposits (converted to millions ESP):
  - 1874–1899: Tedde de Lorca (1974), series "Cuentas corrientes", chainlinked.
  - 1900–1914: Martín Aceña and Pons (2005), "Cuentas corrientes" + "Depositos a plazo", chainlinked.
  - 1915–1920: José Luis Malo de Molina and Pablo Martín-Aceña "The Spanish financial system – Growth and development since 1900", p. 106. Series "Deposits". Levels.
  - 1921–1922: Martín Aceña and Pons (2005), "Cuentas corrientes" + "Depositos a plazo", chainlinked.
  - 1923–1935: Malo de Molina and Martín-Aceña, p. 111. Series "Deposits". Levels.
  - 1942–1961: Martín Aceña and Pons (2005), "Cuentas corrientes" + "Depositos a plazo", chainlinked.
  - 1962–2020: Boletin Estadistico, Bank of Spain, 4. Entidades de crédito..., Table 4.2 Pasivo, Column 5, Deposits, Domestic, Other sectors.
- Loans (converted to millions ESP):
  - 1874–1914: Tedde de Lorca (1974), series "Prestamos", chainlinked.
  - 1915–1922: Martín Aceña and Pons (2005), "Creditos", chainlinked.
  - 1923–1935: Malo de Molina and Martín-Aceña, p. 111. Series "Loans and Credit" + "Bills discounted" (Bills discounted are only available for a few years, hence estimated using average share relative to Loans and Credit).
  - 1942–1961: Martín Aceña and Pons (2005), "Creditos" + "Inversiones", chainlinked.
  - 1962–2020: Boletin Estadistico, Bank of Spain, 4. Entidades de crédito..., Table 4.1 Activo, Credito, Domestic, Other sectors.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.164.

### SWEDEN (ISO SWE) — pages 164–172. "(Data in millions SEK)"

**Population** (`pop`) — p.164
- 1870–2009: Angus Maddison Database (2010). Table 1 "Population levels, 1AD–2030AD".
- 2010–2017: growth rates from IMF (Aug, 2019) WEO, "People – population" (base year: 2009).
- 2018–2020: growth rates from IMF (Oct, 2021) WEO (base year: 2009).

**GDP (millions SEK)** (`gdp`) — p.164
- 1870–1949: Groningen Growth and Development Centre (2014), Historical National Accounts Database, University of Groningen. Table "Sweden, value added at market prices in current price", Series "Total GDP" (http://www.ggdc.nl/databases/hna/2009/data/hna_swe_09.xls).
- 1950–2020: IMF (2021), IFS. Series "Gross domestic product, nominal".

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — pp.164–165: standard block.
**Real GDP per capita (index, 2005=100)** — p.165: standard block (World Bank 2021).
**Real consumption per capita (index, 2006=100)** — p.165: standard block.

**Investment-to-GDP ratio** (`iy`) — p.165
- 1870–1949: Rodney Edvinsson (2004), "Historical national accounts for Sweden 1800–2000 (Historiska nationalräkenskaper för Sverige 1800–2000)", Version 1.0 (http://www.historia.se/tablesAtoX.xls).
- 1950–2020: IMF IFS, Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal".

**Consumer prices (index, 1990=100)** (`cpi`) — p.165
- 1870–2020: Statistics Sweden, series "CPI, Historical numbers 1830 -". Rebased to 1990=100. (https://www.scb.se/en/finding-statistics/statistics-by-subject-area/prices-and-consumption/consumer-price-index/consumer-price-index-cpi/pong/tables-and-graphs/consumer-price-index-cpi/cpi-historical-numbers-1830/)

**Narrow Money (millions SEK)** (`narrowm`) — pp.165–166
- 1871–1994: Historical monetary statistics for Sweden 1668–2008 – series M0 (www.riksbank.se/en/The-Riksbank/Research/Historical-Monetary-Statistics-/Money-supply/). (Chain linked)
- 1995–2016: IMF eLibrary. IFS. Monetary Aggregates – M0.
- 2014–2020: Statistics Sweden. Financial Market Statistics Table tab 5.1 (Money supply and the monetary base), 5.1.1 (Money supply, M1, M2 and M3) Table 1 (Money supply, notes and coins held by Swedish non-bank public, M1 (SEK millions)) in column D (Notes and coins held by Swedish non-bank public). "There is a plus sign to the left where you can expand the timeseries. The timeseries dates back to 1998." (https://scb.se/en/finding-statistics/statistics-by-subject-area/financial-markets/financial-market-statistics/financial-market-statistics/)
- [note] printed ranges 1995–2016 and 2014–2020 overlap.

**Broad Money (millions SEK)** (`money`) — p.166
- 1871–1960: Historical monetary statistics for Sweden 1668–2008 – series M3 (riksbank.se). (chain linked)
- 1961–1996: IMF eLibrary. IFS. Monetary Aggregates – M3.
- 1997–2020: Statistics Sweden. Financial Market Statistics. Tables and graphs. Money supply. Excel Table. M3. December values.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.166
- 1870–1998: D. Waldenstroem Swedish Stock and Bond Returns, 1856–2012, IFN Working Paper No. 1027, Research Institute of Industrial Economics, Stockholm. Excel file Tab: Table II.A6.9 Short-term interest rate. Annual average of monthly series. Level.
- 1999–2020: OECD, short-term interest rate, percent per annum, average of monthly values.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — p.166
- 1870–1873: sum of "Yield on consols" (BoE, Three centuries) and "Spread on consols" (Clemens & Williamson 2004).
- 1874–2000: Daniel Waldenström (2014), "Swedish stock prices and returns and bond yields, 1856–2012," Sveriges Riksbank (http://www.riksbank.se/en/The–Riksbank/Research/Historical–Monetary–Statistics–/Interest–and–stock–returns/). Level.
- 2001–2016: IMF (2019), IFS. Data Series: "Interest rates, government securities, Government Bonds". Level.
- 2017–2020: OECD (2020). OECD iLibrary. Long-term interest rates doi: 10.1787/662d712c-en.

**Current Account (millions SEK)** (`ca`) — p.166
- 1870–1945: M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER WP 6103 (http://www.nber.org/databases/jones–obstfeld/). Level.
- 1946–2007: B. Mitchell (2013), IHS. Table: G3 Balance of Payments. Since 1948 in USD – redenominated into SEK using the exchange rate of the JST dataset. Level.
- 2008–2020: IMF WEO. % of GDP. Multiplied by nominal GDP from JST dataset = Current Account. Level.

**Imports & Exports (millions SEK)** (`imports`, `exports`) — p.167
- 1870–1947: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table: E1 Europe: External Trade Aggregate Current Value. Level.
- 1948–1993: IMF (2014), IFS: Value of Exports/Imports (National Currency). Level.
- 1994–2020: IMF IFS archive, M10 2021, External Trade (exports FOB, imports CIF, domestic currency).

**Government Revenues (millions SEK)** (`revenue`) — p.167
- 1870–1997: K. Fregert & R. Gustafsson (2008), Fiscal Statistics for Sweden 1719–2003, Research in Economic History, 25, pp169–224.
- 1998–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTR.

**Government Expenditure (millions SEK)** (`expenditure`) — p.167
- 1870–1997: K. Fregert & R. Gustafsson (2008), ibid.
- 1998–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTE.

**Public debt-to-GDP ratio** (`debtgdp`) — p.167
- 1870–1998: Fregert and Gustafsson (2005): Fiscal Statistics for Sweden 1719–2003. Research in Economic History 25, pp. 169–22. Online: http://www.riksbank.se/en/The-Riksbank/Research/Historical-Monetary-Statistics-of-Sweden/Volume-II-House-Prices-Stock-Returns-National-Accounts-and-the-Riksbank-Balance-Sheet-16202012/
- 1999–2020: European Commission AMECO, Gross Public Debt (linked series) (UDGGL), % of GDP at market prices (EDP).

**USD exchange rate (local currency/USD)** (`xrusd`) — pp.167–168
- 1870–1880: Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. SEK/GB pounds × GBP/US Dollar (contained in this dataset).
- 1881–1939: Riksbank. Historical Monetary Statistics of Sweden. SEK/GBP exchange rate multiplied with GBP/USD exchange rate (see USD exchange rate of the U.K.).
- 1940–1945: Bordo & Jonung (1996).
- 1946–1958: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1959–2020: IFS, IMF eLibrary. "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy / Strict peg dummy** — p.168: standard block.
**Exogenous monetary policy shocks** — p.168: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.168
- 1875–2012: Knoll et al. (2014). Year average values. [note: starts 1875.]
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — pp.168–169
- 1911–1919: Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter: International Comparison of Unemployment Rates, Table 1 "Unemployment Rates, Nine Countries, 1900-1950 (per cent)". Chainlinked.
- 1920–1939: Grytten, Ola Honningdal. Economic policy and labour markets in Nordic countries during the great depression of the 1930s. In: XIV International Economic History Congress, Helsinki. 2006.
- 1940–1989: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table B2 Europe: Unemployment. Chainlinked.
- 1990–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.169
- 1870–1947: Rodney Edvinsson, Tor Jacobson och Daniel Waldenström (eds.) (2010). "Historical Monetary and Financial Statistics for Sweden: Exchange Rates, Prices, and Wages, 1277-2008.". Wages (no payroll taxes) for male workers in Sweden 1803-2004. Chainlinked.
- 1948–1989: IMF IFS, Labor Markets, Wage Rates, Index. Chainlinked.
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (millions SEK)**

**Total loans to non-financial private sector** (`tloans`) — p.169
- 1871–1974: calculated from Riksbank (2008), Historical Monetary Statistics for Sweden 1668–2008, Swedish Monetary History Project. Table 2 "Bank lending, monthly figures" + growth rate calculated from Statistics Sweden (various), Financial Market Statistics. Section 3.11 "Housing credit institutions' balance sheet times series", Series "Landshypoteksinstitutionen, Sveriges Allmänna Hypoteksbank", Series "Stadshypotekskassa", Series "Bostadskreditkassan" using base value of Table 3.11.1 "Housing credit institutions' lending, SEK millions", Series "Non–financial corporations", Series "Households incl. NPISH" 1975.
- 1975–2020: calculated from Statistics Sweden (various), Monetary Financial Institutions (MFI), assets and liabilities by MFI, item and currency. Institution: "Banks", Item: Kontoposter "Non–financial corporations", Item "Households" + Institution: "Housing credit institutions", Item "Non–financial corporations", Item "Households", Currency "Total currency", end of period values.

**Mortgage loans to non-financial private sector** (`tmort`) — pp.169–170
- 1871–1911: calculated from Statistics Sweden (various), Financial Market Statistics. Section 3.11 "Housing credit institutions' balance sheet times series", Series "Landshypoteksinstitutionen, Sveriges Allmänna Hypoteksbank", Series "Stadshypotekskassa", Series "Bostadskreditkassan" + Table 4.9 "Housing loans to households", Series "Solidariska bankbolag", Series "Bankaktie–bolag/Aktiebankerna".
- 1912–1974: growth rate calculated from Statistics Sweden (various), Financial Market Statistics. Section 3.11, same three series, using base value of TLSRE1975.
- 1975–2002: calculated from growth rate Statistics Sweden (various), Financial Market Statistics. Table 3.10.1 "Banks' total lending and lending to non–MFI, SEK million", Series "Households – total" using base value of Table 4.9 "Housing loans to households" 2003 + Table 3.11.1 "Housing credit institutions' lending, SEK millions", Series "Non–financial corporations", Series "Households incl. NPISH".
- 2003–2020: calculated from Statistics Sweden. Monetary Financial Institutions (MFI), assets and liabilities by MFI, item and currency. Institutions: "Housing credit institutions" Item: Sought-after items "Lending, Swe, Collateral housing, Households" and "Lending, Swe, Non-financial Corporations" + Institutions: "Banks", Item: Sought-after items: "Lending, Swe, Collateral housing, Households", Currency: "Total currency", End of period values (https://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__FM__FM0401/MFIM1/).

**Total Loans to Households** (`thh`) — p.170
- 1871–1940: equal to Mortgage Loans to Households.
- 1975–2016: calculated from Statistics Sweden (various), Monetary Financial Institutions (MFI), assets and liabilities by MFI, item and currency. Series: "Housing credit institutions' lending, SEK millions", Series "Households incl. NPISH" + Series: "Banks' total lending and lending to non–MFI, SEK million", Series "Households – total".
- [note] gap 1941–1974 as printed; the text runs straight into the next heading without a line break.

**Loans to Households Secured by Real Estate** (no dataset column; component) — p.170
- 1871–1940: equal to Mortgage loans to non-financial private sector.
- 1945–1974: growth rate calculated from Statistics Sweden (various), Financial Market Statistics. Section 3.11, Series "Landshypoteksinstitutionen, Sveriges Allmänna Hypoteksbank", "Stadshypotekskassa", "Bostadskreditkassan" using base value of LHSRE 1975.
- 1975–2002: calculated from Statistics Sweden (various), Financial Market Statistics. Table 3.11.1 "Housing credit institutions' lending, SEK millions", Series "Households incl. NPISH" + growth rate calculated Table 3.10.1 "Banks' total lending and lending to non–MFI, SEK million", Series "Households – total" using base value of Table 4.9 "Housing loans to households" 2003.
- 2003–2020: calculated from Statistics Sweden (various), Financial Market Statistics. Series: "Housing credit institutions' lending, SEK millions, Series "Households incl. NPISH" + Series: "Housing loans to households".

**Total Loans to Business** (`tbus`) — p.170
- 1975–2020: calculated from Statistics Sweden (various), Monetary Financial Institutions (MFI), assets and liabilities by MFI, item and currency. Series: "Housing credit institutions' lending, SEK millions", Series "Non–financial corporations" + Series: "Banks' total lending and lending to non–MFI, SEK million", Series "Non–financial corporations – Total", Series "Financial corporate sector, not MFI – Total".

**Corporate Debt** (`bdebt`) — p.171
- 1872–1940: residual of total bank loans to non-financial private sector and total loans to households (both from JST MacroHistory Database); total bank loans less loans of housing credit institutions.
- 1975–1979: bank loans to business calculated from Statistics Sweden (various), Financial Market Statistics. Series: "Housing credit institutions' lending, SEK millions", Series "Non-financial corporations" + Series: "Banks' total lending and lending to non-MFI, SEK million", Series "Non-financial corporations – Total", Series "Financial corporate sector, not MFI – Total".
- 1980–1994: BIS "Credit to the non-financial sector".
- 1995–2013: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2019: eurostat financial accounts data on total non-equity liabilities of the private non-financial business sector.

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions SEK)"

*Capital ratio* (`lev`) — p.171
- Total Assets (millions SEK):
  - 1870–2005: Sveriges Riksbank Monetary History Project, Table 8, Income Statement items of the Swedish commercial banks 1870-2005, Assets. From 1993 including savings banks. Levels.
  - 2006–2020: Balance sheet statistics, Banks Total, Series A 15, Total Assets (http://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__FM__FM0402/FinBalAr/table/tableViewLayout1/?rxid=86abd797-7854-4564-9150-c9b06ae3ab07).
- Capital (millions SEK):
  - 1870–2005: Sveriges Riksbank Monetary History Project. Table 8 Income Statement items of the Swedish commercial banks 1870-2005. Capital. Includes 70% of untaxed reserves as capital (for details see Hortlund, Per (2005), The Long-Term Relationship between Capital and Earnings in Banking, SSE/EFI Working Paper Series in Economics and Finance, No 611). From 1993 including savings banks. Levels.
  - 2006–2020: Balance sheet statistics, Banks Total, Series A27-A32 Equity. Chainlinked capital ratio.

*Loans-to-Deposits ratio* (`ltd`) — p.172
- Deposits (millions SEK):
  - 1870–1995: Sveriges Riksbank Monetary History Project, Excel sheet, Table 9. The Swedish money stock and its components, monthly figures 1871-2007, Series "Total deposits of commercial banks held by the public". From 1993 including savings banks. Levels.
  - 1996–2020: Balance sheet statistics, Banks Total, Series A18 Deposits and funding from the general public. Levels.
- Loans (millions SEK):
  - 1871–2000: Sveriges Riksbank Monetary History Project, Table 2. Bank lending, Commercial Banks. From 1993 including savings banks. Levels.
  - 2001–2020: Balance sheet statistics, Banks Total, Series A4 Lending to the general public. Levels.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.172.

### SWITZERLAND (ISO CHE) — pages 172–182. "(Data in millions CHF)"

**Population** (`pop`) — pp.172–173: Maddison (2008) 1870–2008; IMF (Aug 2019) WEO growth rates 2009–2017; IMF (Oct 2021) WEO 2018–2020 (base year 2008).

**GDP (millions CHF)** (`gdp`) — p.173
- 1870–1889: Universität Zürich, Historical Statistics of Switzerland online. Nationale Buchhaltung, Q.1.a Nominales und reales Bruttoinlandprodukt (Bruttowertschöpfung) 1851-1913 (in Millionen Franken). Chain-linked.
- 1890–1948: Universität Zürich, Historical Statistics of Switzerland online. Q.16a Bruttoinlandprodukt nach Verwendungsarten in Preisen von 1929 und nominal, 1890–1948 (Wirtschaftsgeschichte der Schweiz im 20. Jahrhundert).
- 1949–1989: Universität Zürich, Historical Statistics of Switzerland online. Q.16b Bruttoinlandprodukt nach Verwendungsarten zu Preisen von 1990 und nominal, 1948–2005 in Mio. Franken (Wirtschaftsgeschichte der Schweiz im 20. Jahrhundert).
- 1990–2020: IMF (2021), IFS, "Gross domestic product (in millions) – GDP nominal".

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.173: standard block.
**Real GDP per capita (index, 2005=100)** — p.173: standard block (World Bank 2021).
**Real consumption per capita (index, 2006=100)** — p.173: standard block.

**Investment-to-GDP ratio** (`iy`) — pp.173–174
- 1870–1913: Historical Statistics of Switzerland. R) Investitionen, Bautätigkeit und Grundstückmarkt. R.1. Kapitalausgaben, Bruttoanlageinvestitionen und Ausrüstungsinvestitionen 1850-1914 (in Millionen Franken). Sum of Bruttoanlageinvestitionen + Ausrüstungsinvestitionen. GDP: from JST dataset.
- 1948–2020: IMF IFS, Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal".
- [note] gap 1914–1947.

**Consumer prices (index, 1990=100)** (`cpi`) — p.174
- 1870–1891: Historical Statistics of Switzerland. Nationale Buchhaltung. Q.1.a Nominales und reales Bruttoinlandprodukt (Bruttowertschöpfung) 1851-1913 (in Millionen Franken). Chain-linked. [note: a GDP-deflator-type table is cited for CPI here.]
- 1892–1996: A. Taylor (2002), A Century of Purchasing–Power Parity, REStat 84(1).
- 1997–2020: IMF WEO (2021). "Inflation, average consumer prices". Chainlinked.

**Narrow Money (millions CHF)** (`narrowm`) — p.174
- 1870–1907: Historical Statistics of Switzerland. Geld und Kredit. Table O.3. Schätzung der Geldmenge in der Schweiz am Jahresende 1851-1910 – M1. Chain-linked.
- 1908–1949: Historical Statistics of Switzerland. Geld und Kredit. Table O.4. Geldmengen am Jahresende 1907-1954 – M1. Chain-linked.
- 1950–1983: Swiss National Bank, Historical time series: the monetary base and the M1, M2 and M3 monetary aggregates – M1 (http://www.snb.ch/en/iabout/stat/statpub/histz/id/statpub_histz_actual). Chain-linked.
- 1984–2015: IMF eLibrary. IFS. Monetary Aggregates – M1.
- 2016–2020: Swiss National Bank, table selection, monetary aggregates M1, M2 and M3, M1, December values.

**Broad Money (millions CHF)** (`money`) — p.174
- 1880–1913: Bordo, Michael, et al. "Is the crisis problem growing more severe?." Economic policy 16.32 (2001): 51-82. Series monagglc. Level/10^6.
- 1914–1949: Historical Statistics of Switzerland. Geld und Kredit. Table O.4. Geldmengen am Jahresende 1907-1954 – Geldmengen – Liquide Aktiva des Publ. ohne Münzgeld (http://www.fsw.uzh.ch/histstat/main.php). Level.
- 1950–2004: Swiss National Bank (2007), Historical Time Series nº1 "Monetary aggregates M1, M2 and M3". Table 2.1 "Official Data". Series M3. Levels.
- 2005–2020: Swiss National Bank, table selection, monetary aggregates M1, M2 and M3, M3. December values.
- [note] starts 1880.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.175
- 1870–1893: Swiss National Bank (2007), Historical Time Series nº4: "Interest rates and yields", Table 1.1a, Series "Discount rate, Zurich". Level.
- 1894–1906: SNB (2007), HTS nº4, Table 1.1a, Series "Lombard rate in Zurich". Level.
- 1907–1968: SNB (2007), HTS nº4, Table 1.1, Series "Discount rate". Level.
- 1969–2017: IMF (2019), IFS, Series "Money Market Rates". Level.
- 2018–2020: Swiss National Bank, table selection, interest rates, yields and foreign exchange market, interest rates, money market rates, Switzerland, CHF, Call money rate (Tomorrow next), 1 day, Dec values.

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — p.175
- 1880–1892: Bordo, Eichengreen, Klingebiel, Martinez–Peria (2001), Economic Policy 32: 51–75.
- 1893–1898: Flandreau and Zumer, 2004, The Making of Global Finance, Paris: OECD Development Centre.
- 1899–1912: SNB. Historische Zeitreihen. Zinssätze und Renditen. Yield on 3.5% CHF bonds.
- 1913–1914: Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition.
- 1915: Historical Statistics of Switzerland; O. Geld und Kredit; O.18b. Diskontsätze, Lombardzinsfuss und Zinssätze für Kassenobligationen 1838-1926.
- 1916–1947: Homer and Sylla (2005).
- 1948–2020: IMF IFS, Series "Government Bonds, Percent per Annum".
- [note] starts 1880.

**Current Account (millions CHF)** (`ca`) — pp.175–176
- 1921–1939: E. Kellenberg (1939–1942), Kapitalexport und Zahlungsbilanz, Bern, A. Francke. Bd. I: S. 155, 245, 307; Bd. II: S. 87, 244f, 364f. Level.
- 1948–1976: B. Mitchell (2007), IHS: Europe 1750–2005. Level.
- 1977–2020: IMF IFS. Supplementary Items, Current Account, Net (excluding exceptional financing), US Dollars. Turned into CHF with exchange rate from JST dataset. Level.
- [note] starts 1921; gap 1940–1947.

**Imports & Exports (millions CHF)** (`imports`, `exports`) — p.176
- 1885–1947: B. Mitchell (2007), IHS: Europe 1750–2005. [note: starts 1885.]
- 1948–2020: IMF IFS archive, M10 2021, External Trade (exports FOB, imports CIF, domestic currency).

**Government Revenues (millions CHF)** (`revenue`) — p.176
- 1870–1912: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table: G6 Europe: Total Central Governmental Revenue and Main Tax Yields. Level.
- 1913–1989: H. Ritzmann–Blickenstorfer (1996), Historische Statistik der Schweiz, Chronos, Zürich.
- 1990–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTR.

**Government Expenditure (millions CHF)** (`expenditure`) — p.176
- 1871–1912: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table: G5 Europe: Total Central Governmental Expenditure.
- 1913–1989: H. Ritzmann–Blickenstorfer (1996), Historische Statistik der Schweiz, Chronos, Zürich.
- 1990–2020: OECD (2021), OECD.Stat, Table 12, GS1311, Series GTE.

**Public debt-to-GDP ratio** (`debtgdp`) — pp.176–177
- Note (verbatim): "until 1945 data is for central government debt only, data thereafter covers general government debt."
- 1880–1913: Flandreau and Zumer, 2004, The Making of Global Finance. Nominal debt divided by nominal GDP from the same dataset.
- 1914–1945: Historical Statistics of Switzerland online (Universität Zürich, Forschungsstelle für Sozial– und Wirtschaftsgeschichte) – U.45. Ausgaben, budgetierter Finanzierungssaldo und Schulden von Bund, Kantone und Gemeinden 1910–2000 (in Mio. Fr., nominal) (Zusammenstellung Sébastian Guex) (1) (Wirtschaftsgeschichte der Schweiz im 20. Jahrhundert). Column: Schulden des Bundes. Divided by GDP from JST dataset.
- 1946–1987: same source, U.45. Column: Totale Schulden. Divided by GDP from JST dataset.
- 1988–2020: IMF eLibrary. World Economic Outlook. Public debt, % of GDP.
- [note] starts 1880.

**USD exchange rate (local currency/USD)** (`xrusd`) — p.177
- 1870–1914: Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914. CHF/GBP rate multiplied with GBP/USD rate (see UK chapter).
- 1915–1939: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1940–1945: Bordo & Jonung (1996).
- 1946–1957: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1958–2020: IFS, IMF eLibrary. Nominal Exchange Rate (domestic currency / US Dollar) (end of period).

**Peg dummy** (`peg`) — p.177
- 1870–1939: Obstfeld & Taylor (2003).
- 1940–1980: unpublished, revised version of Ilzetzki, Reinhart & Rogoff (2004) (1=1-2, all 3-6=0); broad peg category including crawling pegs.
- 1981–2020: E. Ilzetzki, C. Reinhart & K. Rogoff (2017). The Country Chronologies to Exchange Rate Arrangements into the 21st Century: Will the Anchor Currency Hold? (De facto peg and de facto moving band = 1).

**Strict peg dummy** (`peg_strict`) — pp.177–178
- 1870–1939: Obstfeld & Taylor (2003).
- 1940–1980: Ilzetzki, Reinhart & Rogoff (2004) (1=1, all 2-6=0); strict peg category excluding crawling pegs.
- 1981–2020: Ilzetzki, Reinhart & Rogoff (2017), Country Chronologies (De facto peg = 1).

**Exogenous monetary policy shocks** — p.178: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.178
- 1901–2012: Knoll et al. (2014). Year average values. [note: starts 1901.]
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — p.178
- 1913–1975: Historical Statistics of Switzerland online, F.18a. Stellensuchende und Arbeitslosenquote nach Geschlecht im Jahresmittel 1913-1995. Chainlinked.
- 1976–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.178
- 1870–1989: Research center for social and economic history. Historical Statistics of Switzerland online. Hourly Earnings of Male and Female Workers 1831-1995 (nominal wages). Chainlinked. http://www.fsw.uzh.ch/histstat/main.php
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (millions CHF)**

**Total loans to non-financial private sector** (`tloans`) — pp.178–179
- 1870–1905: Historical Statistics of Switzerland online. Table O.12 "Diskontobanken, Kantonalbanken und Übrige Emissionsbanken: Passiven, Aktiven und Gewinnrechnung 1826-1910". Series "Hypotheken", "Kontokorrentdebitoren", "Vorschüsse auf Termin". Chain-linked.
- 1906–1972: Swiss National Bank (2009), Historic Time Series: Section 5 "Banks in Switzerland". Table 2 "All asset items – total for categories 1.00–5.00", Series 6. and Swiss National Bank (2009), ibid. Table 2 "All asset items – total for categories 1.00–5.00", Series 8. Level.
- 1973–2008: Swiss National Bank (2009), ibid. Table 6 "Claim again domestic customers – by bank category", Series 6. Level.
- 2009–2020: Swiss National Bank, Banks in Switzerland. Table: Bank, Selected assets – annual, Parent company perspective (survey: comprehensive year-end statistics) – Series "Mortgage loans (total)" and Series "Amounts due from customers (total)". Chain-linked.

**Mortgage loans to non-financial private sector** (`tmort`) — p.179
- 1870–1905: University of Zürich Research Center for Economic and Social History, Swiss Economic and Social History Online Database. Table O.12 "Diskontobanken, Kantonalbanken und übrige Emissionsbanken: Passiven, aktiven und Gewinnrechnung 1826–1910", Series "Hypotheken" and Swiss National Bank (2009), ibid. Table 2 "All asset items – total for categories 1.00–5.00", Series 8. Chain-linked.
- 1906–2008: Swiss National Bank (2009) Historic Time Series: Section 5 "Banks in Switzerland". Table 2 "All asset items – total for categories 1.00–5.00", Series 8.
- 2009–2020: Swiss National Bank, Banks in Switzerland. Table "Assets", All Banks – Series "Mortgage loans".

**Total Loans to Households** (`thh`) — p.179
- 1870–1976: growth rate calculated from Swiss National Bank (2009). Historic Time Series: Section 5 "Banks in Switzerland". Table 2 "All asset items – total for categories 1.00–5.00", Series 8.
- 1977–2020: residual of Total loans to non-financial private sector and Total Loans to Business.

**Total Loans to Business** (`tbus`) — p.179
- 1870–1976: residual of Total loans to non-financial private sector and Total Loans to Households.
- 1977–2007: Swiss National Bank. "Historical Time Series 5." 2009. "Banks in Switzerland.", Table 21 "Sectoral breakdown of domestic assets", Series "Non-Financial Corporations, Private legal entities".
- 2008–2020: Swiss National Bank growth rates from Banks in Switzerland. Series "Mortgage claims" and Series "Amounts due from customers (total)".

**Corporate Debt** (`bdebt`) — pp.179–180
- 1870–1976: bank loans to business from JST MacroHistory Database, building on Swiss National Bank. "Historical Time Series." 2009. Section 5: "Banks in Switzerland".
- 1977–1998: bank loans to business from Swiss National Bank, "Historical Time Series 5." 2009. "Banks in Switzerland.", Table 21 "Sectoral breakdown of domestic assets", Series "Non-Financial Corporations, Private legal entities".
- 1999–2011: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2012–2020: BIS "Credit to the non-financial sector" (bank loans to business and capital market debt).

**Bank balance sheet ratios** "(Ratios in %, underlying data in millions CHF)"

*Capital ratio* (`lev`) — p.180
- Total assets (millions CHF):
  - 1870–1905: University of Zürich Research Center for Economic and Social History, Swiss Economic and Social History Online Database, Table O.12 "Diskontobanken, Kantonalbanken und übrige Emissionsbanken: Passiven, aktiven und Gewinnrechnung 1826–1910", Series "Bilanzsumme". Chainlinked.
  - 1906–2014: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Alle Passivpositionen – Total Bankengruppen 1.00–5.00, Series "Bilanzsumme". Levels.
  - 2015–2020: Swiss National Bank, Bilanzpositionen der Banken nach Bankengruppen – Jährlich, Total Inland und Ausland, Banken in der Schweiz, Aktiven – "Total Aktiven". Chainlinked.
- Capital (millions CHF):
  - 1870–1905: University of Zürich ..., Table O.12, Sum of "Einbezahltes Kapital", "Reserven", "Verlustreserven" and "Ausstehendes Kapital". Chainlinked.
  - 1906–2014: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Alle Passivpositionen – Total Bankengruppen 1.00–5.00, Series "Eigene Mittel – Total". Levels.
  - 2015–2020: Swiss National Bank, Bilanzpositionen der Banken nach Bankengruppen – Jährlich, Total Inland und Ausland, Banken in der Schweiz, Aktiven – "Gesellschaftskapital + Gesetzliche Kapitalreserven + Freiwillige Gewinnreserven + Gewinn/Verlustvortrag". Chainlinked.

*Loans-to-Deposits ratio* (`ltd`) — pp.180–181
- Deposits (millions CHF):
  - 1870–1905: University of Zürich ..., Table O.12, Sum of "Check and Giro", "Spareinlagen" and "Obligationen, Anleihen und Depositen". Chainlinked.
  - 1906–1972: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Alle Passivpositionen – Total Bankengruppen 1.00–5.00, sum of "Verpflichtungen gegenüber Kunden" – "In Spar- und Anlageform", "Übrige auf Sicht" and "Übrige auf Zeit". Levels.
  - 1973–2008: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Sheet 1, Series "Deposits by domestic customers, Total Bankengruppen 1.00–5.00". Levels.
  - 2009–2014: Swiss National Bank, Historische Zeitreihen, Alle Passivpositionen – Total Bankengruppen 1.00–5.00, sum of Verpflichtungen gegenüber Kunden – "In Spar- und Anlageform", "Übrige auf Sicht" and "Übrige auf Zeit". Chainlinked.
  - 2015–2020: Swiss National Bank, Bilanzpositionen der Banken nach Bankengruppen – Jährlich, Total Inland und Ausland, Banken in der Schweiz, Aktiven – "Verpflichtungen aus Kundeneinlagen - Inland". Chainlinked.
- Loans (millions CHF):
  - 1870–1905: University of Zürich ..., Table O.12, Sum of "Lombards und Reports", "Kontokorrentdebitoren", "Vorschüsse auf Termin" and "Hypotheken". Chainlinked.
  - 1907–1944: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Alle Aktivpositionen – Total Bankengruppen 1.00–5.00, sum of "Forderungen gegenüber Kunden" and "Hypothekarforderungen". Levels.
  - 1945–2008: Swiss National Bank, Historische Zeitreihen, Die Banken in der Schweiz, Sheet 13, Asset items in Switzerland, total and in CHF, Total Bankengruppen 1.00–5.00, sum of "Forderungen gegenüber Kunden, davon CHF" and "Hypothekarforderungen, davon CHF". Levels.
  - 2009–2014: Swiss National Bank, Historische Zeitreihen, Alle Aktivpositionen – Total Bankengruppen 1.00–5.00, sum of "Forderungen gegenüber Kunden" and "Hypothekarforderungen". Chainlinked.
  - 2015–2020: Swiss National Bank, Bilanzpositionen der Banken nach Bankengruppen – Jährlich, Total Inland und Ausland, Banken in der Schweiz, Aktiven – "Aktiven - Forderungen gegenüber Kunden - Inland" and "Aktiven - Hypothekarforderungen - Inland". Chainlinked.
  - [note] 1906 not covered as printed (1870–1905 then 1907–1944).

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.182.

### UNITED KINGDOM (ISO GBR) — pages 182–192. "(Data in billions GBP)"

**Population** (`pop`) — p.182: Maddison (2008) 1870–2008; IMF (Aug 2019) WEO growth rates 2009–2017; IMF (Oct 2021) WEO 2018–2020 (base year 2008).

**GDP (billions GBP)** (`gdp`) — p.182
- 1870–1947: Hills, S, Thomas, R and Dimsdale, N (2015) "Three Centuries of Data - Version 2.2", Bank of England. Series: Composite estimate of nominal GDP at market prices – no break adjustment for Ireland (http://www.bankofengland.co.uk/research/Pages/onebank/threecenturies.aspx). Level. (though the Hills et al. data are retropolated).
- 1948–2020: Office for National Statistics – Quarterly National Accounts – Gross Domestic Product at market prices: Current price: Seasonally adjusted £m (Series: YBHA). Levels.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.182: standard block.
**Real GDP per capita (index, 2005=100)** — p.182: standard block (World Bank 2021).
**Real consumption per capita (index, 2006=100)** — p.183: standard block.

**Investment-to-GDP ratio** (`iy`) — p.183
- 1870–2009: Hills, Thomas and Dimsdale (2015) "Three Centuries of Data - Version 2.2", Bank of England. Level. Series: Gross fixed capital formation, spliced using within-chain shares (to ensure additivity), divided by GDP from same dataset. Note: this source is regularly updated: check for revisions.
- 2010–2020: IMF IFS, Data Report "National Accounts", Series "Gross Fixed Capital Formation, Nominal", divided by GDP from same dataset.

**Consumer prices (index, 1990=100)** (`cpi`) — p.183
- 1870–2016: Hills, S, Thomas, R and Dimsdale, N. "A millenium of macroeconomic data – version 3.1", Bank of England. Series: Headline consumer price index (cpi). Level.
- 2017–2020: Office for National Statistics (ONS), series "CPI annual rate 00: all items 2015=100" (https://www.ons.gov.uk/economy/inflationandpriceindices#timeseries). Chainlinked.

**Narrow Money (billions GBP)** (`narrowm`) — p.183
- 1870–2016: Hills, Thomas and Dimsdale. "A millenium of macroeconomic data – version 3.1", Bank of England. Series: Coins and notes in circulation. Level.
- 2017–2020: Bank of England Database. Series: "LPWVQUX". Weekly year on year growth rate of total sterling notes and coin in circulation outside the Bank of England (in sterling millions) not seasonally adjusted. Use End-of-year values as growth rate.

**Broad Money (billions GBP)** (`money`) — p.183
- 1870–2016: Hills, Thomas and Dimsdale. "A millenium of macroeconomic data – version 3.1", Bank of England. Series: Spliced broad money measure based on M3/M4/M4x. Level.
- 2017–2020: Bank of England Database. Browse Data by topic, Money and lending, M4 and M4 lending excluding intermediate OFCs, seasonally adjusted, Amounts outstanding, Aggregates excluding intermediate OFCs, Aggregate M4, quarterly (RPQB3DQ). Series name: Quarterly amounts outstanding of UK resident monetary financial institutions' sterling M4 liabilities to Private sector excluding intermediate OFCs (in sterling millions) seasonally adjusted.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.184
- 1870–2020: Measuring Worth, Short-Term Rate: Ordinary Funds, Contemporary Series. "The Series emanates from the normal course of business of financial institutions, for example, the ordinary lending of funds by commercial banks for a short time period" (www.measuringworth.com/datasets/interestrates/).

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — p.184
- 1870–2008: Hills, Sally, Ryland Thomas, and Nicholas Dimsdale (2010), "The UK recession in context — what do three centuries of data tell us?", Quarterly Bulletin of the Bank of England, 2010:4 (https://www.bankofengland.co.uk/quarterly-bulletin/2010/q4/the-uk-recession-in-context-what-do-three-centuries-of-data-tell-us). Level.
- 2009–2020: Bank of England. Statistical Database. Series code IUAALNPY. Series: End year average yield from British Government Securities, 20 year Nominal Par Yield. Level.

**Current Account (billions GBP)** (`ca`) — p.184
- 1870–2007: Hills, Thomas and Dimsdale (2015) "Three Centuries of Data - Version 2.2", Bank of England. Series: Current account deficit excluding all bullion flows. Level.
- 2008–2020: IMF WEO. % of GDP × nominal GDP = Current Account.

**Imports & Exports (billions GBP)** (`imports`, `exports`) — p.184
- 1870–1994: Hills, Thomas and Dimsdale (2015) "Three Centuries of Data - Version 2.2", Bank of England. Series: Exports/Imports – Goods (f.o.b.). Level.
- 1995–2020: IMF IFS archive, M10 2021, External Trade (exports FOB, imports CIF, domestic currency).

**Government Revenues (billions GBP)** (`revenue`) — p.184
- 1870–1999: Bank of England. "A millenium of macroeconomic data – version 3.1" Central government expenditure. [sic — the revenue entry cites "Central government expenditure".]
- 2000–2020: Office for National Statistics. Public sector finances. Table: CG: Total revenue: £m CPNSA. Level.

**Government Expenditure (billions GBP)** (`expenditure`) — pp.184–185
- 1870–1951: B. Mitchell (1988), ibid.
- 1952–1999: Office for National Statistics. Table "Public sector finances – supplementary Tables" (http://www.ons.gov.uk/ons/index.html).
- 2000–2020: Office for National Statistics. Public sector finances Table: CG: Total expenditure: £m CPNSA. Level.

**Public debt-to-GDP ratio** (`debtgdp`) — p.185
- 1870–1979: Abbas et al. 2010. A historical public debt database. Level.
- 1980–2020: IMF World economic outlook. Public debt to GDP ratio.

**USD exchange rate (local currency/USD)** (`xrusd`) — p.185
- 1870–1945: Lawrence H. Officer, "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015.
- 1946–1955: Reinhart & Rogoff (2010). (Black) market exchange rate.
- 1956–2020: IFS, IMF eLibrary. "Exchange Rates, National Currency Per U.S. Dollar, End of Period, Rate".

**Peg dummy / Strict peg dummy** — p.185: standard block.
**Exogenous monetary policy shocks** — pp.185–186: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.186
- 1899–1938 & 1946–2012: Knoll et al. (2014). Year average values. [note: gap 1939–1945; starts 1899.]
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — p.186
- 1870–1971: Mitchell, Brian (2013), IHS: Europe, 1750–2010, Table B2 Europe: Unemployment. Chainlinked.
- 1972–2020: ILOSTAT (2021), "Unemployment rate by sex and age (%) - Annual", EU Labour force survey.

**Wages (index, 1990=100)** (`wage`) — p.186
- 1870–2020: Gregory Clark "What Were the UK Earnings and Prices Then?" MeasuringWorth, 2019. UK Average Nominal Earnings. Levels. (https://www.measuringworth.com/datasets/ukearncpi/)

**Credit Data (billions GBP)**

**Total loans to non-financial private sector** (`tloans`) — p.186
- 1880–1962: David K. Sheppard (1971), The Growth and Role of UK Financial Institutions 1880–1962, Methuen & Co, London. Table (A) 2.4, p.150; Building Societies in Great Britain 1880-1967 (Assets and liabilities £ millions); total mortgage plus Table (A) 3.4, p. 184. Series: Loans and Advances and Other Accounts.
- 1963–2020: calculated from Bank of England (2021). "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to household sector (in sterling millions) seasonally adjusted" (Table LPQBC44) and "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to unincorporated businesses and non-profit institutions serving households (in sterling millions) seasonally adjusted" (Table LPQBC58) and "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to private non-financial corporations (in sterling millions) seasonally adjusted" Table (LPQBC57) (http://www.bankofengland.co.uk/).
- [note] UK credit series start in 1880.

**Mortgage loans to non-financial private sector** (`tmort`) — pp.186–187
- 1880–1962: David K. Sheppard (1971), The Growth and Role of UK Financial Institutions 1880–1962.
- 1963–2016: Bank of England. A millenium of macroeconomic data – version 3.1. Secured M4 lending secured on dwellings adjusted for the impact of securitisations. Break-adjusted stock. www.bankofengland.co.uk/satistics/research-datasets
- 2017–2020: Bank of England (2021). "Quarterly amounts outstanding of monetary financial institutions' sterling net secured lending to individuals (in sterling millions) seasonally adjusted" Table LPQBC55.

**Total Loans to Households** (`thh`) — p.187
- 1880–1950: growth rate calculated from Loans to Households Secured by Real Estate.
- 1951–2020: Bank of England (2022). "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to household sector (in sterling millions) seasonally adjusted" (Table LPQBC44) + "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to unincorporated businesses and non-profit institutions serving households (in sterling millions) seasonally adjusted" Table (LPQBC58).

**Total Loans to Business** (`tbus`) — p.187
- 1880–1950: residual of Total loans to non-financial private sector and Total Loans to Households.
- 1951–2020: Bank of England (2022). "Quarterly amounts outstanding of monetary financial institutions' sterling net lending to private non-financial corporations (in sterling millions) seasonally adjusted" (Table LPQBC57).

**Corporate Debt** (`bdebt`) — p.187
- 1880–1950: residual of total bank loans to non-financial private sector and total loans to households from JST MacroHistory Database.
- 1951–1956: Bank of England (2017); Table LPQBC57 (http://www.bankofengland.co.uk/).
- 1957–1965: total non-equity liabilities of industrial and commercial companies from Roe (1971) "The financial interdependence of the UK economy 1957–66", London: Chapman and Hall.
- 1966–1978: total non-equity liabilities of the private non-financial business sector from Pettigrew (1980) "National and sector balance sheets for the United Kingdom", Economic Trends, November, pp. 82-100.
- 1979–1986: total non-equity liabilites of industrial and commercial companies from Sbano (2008) "New historical data for assets and liabilities in the UK", Economic & Labour Market Review, Vol. 2(4), pp. 40-46.
- 1987–2013: OECD financial accounts data on total non-equity liabilities of the private non-financial business sector.
- 2014–2020: BIS "Credit to the non-financial sector" (bank loans to business and capital market debt).

**Bank balance sheet ratios** "(Ratios in %, underlying data in billions GBP)"

*Capital ratio* (`lev`) — pp.188–190
- Total Assets (billions GBP):
  - 1880–1945: D. Sheppard (1971), The Growth and Role of UK Financial Institutions 1880-1962, Table (A) 1.1, United Kingdom Banks combined Balance Sheets 1880-1966. Levels.
  - 1946–1950: Sheppard (1971), Table (A) 1.1. Chainlinked.
  - 1951–1962: Sheppard (1971), Table (A) 1.1, "Total Assets Liabilities", + Bank of England, Statistical Appendix of Quarterly Bulletins (various), Total Deposits and Current Accounts, series "Total Deposits" of British Overseas Banks, American Overseas, Foreign banks, Accepting houses and other banks.
  - 1963–1969: Bank of England – Statistical Abstracts, Number 1, London 1970, Table 8(2) Deposit banks, series "Total current and deposit accounts" + Accepting houses, overseas banks and other banks "Total current and deposit accounts" + Capital series constructed as described below.
  - 1970: Bank of England – Statistical Abstracts, Number 2, London 1975, Table 8/1, Banks in the United Kingdom: summary of banks other than deposit banks, series "Current and deposit accounts, all holders, total" + Table 8/2, Deposit Banks: London Clearing Banks "Total Gross Deposits" + Capital series constructed as described below.
  - 1971–1974: Bank of England – Statistical Abstracts, Number 2, London 1975, Banks in the United Kingdom: summary of all banks in the United Kingdom, series "Current and deposit accounts, all holders, Total" + "Total Capital" series constructed as described below.
  - 1975: Bank of England, Quarterly Bulletin 1976 Q2, Statistical Annex, Table 2/1 Banks in the United Kingdom – summary, December 10a, series "Total Assets/Liabilities" (http://www.bankofengland.co.uk/archive/Pages/digitalcontent/historicpubs/quarterlybulletins.aspx).
  - 1976: Bank of England, Quarterly Bulletin 1977 Q2, Statistical Annex, Table 2/1 Banks in the United Kingdom – summary, December 8, series "Total Assets/Liabilities".
  - 1977–1996: Bank of England, Database, B Monetary financial institutions' balance sheets, income and expenditure, Table "Table 3.1 Other bank's balance sheet (discontinued)", "Total liabilities", series key ATFU.
  - 1997–2009: Bank of England, Interactive database, series key RPATBJF: Annual amounts outstanding of UK resident banks' (excl. Central Bank) sterling and all foreign currency assets total (in sterling millions) not seasonally adjusted.
  - 2010–2020: Bank of England, Statistical Interactive Database; series key RPMB3ZN: Monthly amounts outstanding of UK resident monetary financial institutions' (excl. Central Bank) sterling and all foreign currency liabilities total (in sterling millions) not seasonally adjusted.
- Capital (billions GBP):
  - 1880–1920: Sheppard (1971), Table (A) 1.1, chainlinked.
  - 1921–1966: Sheppard (1971), Table (A) 1.1, adjusted capital series with factor for true capital from Mark Billings and Forrest Capie, Business History, Vol. 49, No. 2, March 2007, 139–162, Capital in British Banking, 1920–1970. Levels.
  - 1963–1966: Bank of England, computed as share of capital relative to deposits from Sheppard (1971) multiplied with total deposits derived from Bank of England – Statistical Abstracts, Number 1, London 1970, Table 8(2) UK Banking sector: Analysis of current and deposit accounts: Deposit banks, series "Total" + Accepting houses, overseas banks and other banks series "Total". Levels of the resulting capital ratio. [note: overlaps the 1921–1966 entry as printed.]
  - 1967–1968: interpolated capital ratio. Plausibility check: Barclay's capital ratios show very similar decline.
  - 1969–1974: Committee of London Clearing Bankers, The London clearing banks: evidence by the Committee of London Clearing Bankers to the Committee to Review the Functioning of Financial Institutions", November, 1977. Series based on Table 63 – Profit and Balance Sheet Statistics, "Ratio of Total Capital as percentage of deposits". Multiplied with deposits from: 1970-1974 Bank of England – Statistical Abstracts, Number 2, London 1975, Banks in the United Kingdom: summary of all banks in the United Kingdom, series "Current and deposit accounts, all holders. Resulting capital ratio is chainlinked.
  - 1975: Bank of England, Quarterly Bulletin 1976 Q2, Statistical Annex, Table 2/1, December 10a, series "Capital and other funds".
  - 1976: Bank of England, Quarterly Bulletin 1977 Q2, Statistical Annex, Table 2/1, December 8, series "Capital and other funds".
  - 1977–1979: Bank of England, Table 3.1 Other Banks' Balance Sheet (discontinued), Sterling liabilities, series "Capital and other funds" + other currency liabilities "Capital and other funds". Chainlinked.
  - 1980–2020: Bank of England, Financial Policy Core Indicators, CCB core indicators, Spreadsheet 11, Leverage Ratio, Simple (https://www.bankofengland.co.uk/financial-stability). Levels.

*Loans-to-Deposits ratio* (`ltd`) — pp.190–192
- Deposits (billions GBP):
  - 1880–1945: Sheppard (1971), Table (A) 1.1. "Deposits and other accounts". Chainlinked.
  - 1945–1962: Sheppard (1971), Table (A) 1.1. Chain-linked.
  - 1963–1969: Bank of England – Statistical Abstracts, Number 1, London 1970, Table 8-2, Deposit Banks, series "Total current and deposit accounts" minus series "Total current and deposit accounts - Overseas residents" + Accepting houses, overseas banks and other banks, series "Total current and deposit accounts" less series "Total current and deposit accounts - Overseas residents".
  - 1970: Bank of England – Statistical Abstracts, Number 1, London 1970, Table 8-2, series "Net Deposits" + Table 8-1, Summary of banks other than deposit banks, series "Current and deposit accounts – Other UK residents (Sterling+other currencies)".
  - 1971–1974: Bank of England – Statistical Abstracts, Number 2, London 1975, Table 8/1 "2 Banks in the United Kingdom: summary of all banks in the United Kingdom", series "Current and deposit accounts – Other UK residents (Sterling+other currencies)".
  - 1975: Bank of England, Quarterly Bulletin 1976 Q2, Statistical Annex, Table 2/1, December 10a, series "Sterling other UK residents deposits (Sight+Time)" + "Other currencies – other UK residents deposits – sight".
  - 1976: Bank of England, Quarterly Bulletin 1977 Q2, Statistical Annex, Table 2/1, December 8, same two series.
  - 1977–1996: Bank of England, Database, B Monetary financial institutions' balance sheets, income and expenditure, Table 3.1 Other Banks' Balance Sheet (discontinued), series "ATFE"+"ATFI"+"ATFP".
  - 1997–2009: Bank of England, Interactive database, series RPATBFE + RPATBFJ + RPAVYDV (http://www.bankofengland.co.uk/boeapps/iadb/newintermed.asp).
  - 2010–2020: Bank of England, Interactive database series RPMB3NM + RPMB3QM.
- Loans (billions GBP):
  - 1880–1962: Sheppard (1971), Table (A) 1.1. "Advances". Levels.
  - 1963–1969: Bank of England, Statistical Abstracts, Number 1, London 1970, Table 8-2, Deposit Banks, series "Advances UK residents" + "Advances UK companies" + Accepting houses, overseas banks and other banks, series "Advances UK residents" + "Advances UK companies".
  - 1970: Bank of England, Statistical Abstracts, Number 1, London 1970, Table 8-2, series Deposit banks "Advances" + Table 8-1, Summary of banks other than deposit banks, series "Advances UK residents (Sterling+other currencies)".
  - 1971–1974: Bank of England, Statistical Abstracts, Number 2, London 1975, Table 8/1 "2 Banks in the United Kingdom: summary of all banks in the United Kingdom", series "Advances UK residents in Sterling" + "Advances UK residents other currencies". Levels.
  - 1975–1976: Bank of England, Quarterly Bulletin 1976 Q2, Statistical Annex, Table 2/1, December 10a, series "Advances - Sterling, UK private sector" + "Market Loans and advances - other currency assets - UK private sector". Levels.
  - 1977–1996: Bank of England, Statistics, Table 3.1 Other Banks' Balance Sheet (discontinued), series "ATGM"+"ATHB".
  - 1997–2009: Bank of England, Interactive database, series RPATBHV.
  - 2010–2020: Bank of England, Interactive database series RPMB3OP. Monthly amounts outstanding of UK resident monetary financial institutions' (excl. Central Bank) sterling loans (excluding reverse repos and commercial paper) to private sector (in sterling millions) not seasonally adjusted.

*Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* (`noncore`) — p.192
- 1880–1945: Not computed: No distinction between deposits and other liabilities in balance sheet data ("Deposits and other accounts" item in D. Sheppard (1971), Table (A) 1.1, United Kingdom Banks combined Balance Sheets 1880-1966).

### UNITED STATES OF AMERICA (ISO USA) — pages 192–201. "(Data in billions USD)"

**Population** (`pop`) — p.192: Maddison (2008) 1870–2008; IMF WEO growth rates 2009–2020 (base year 2008).

**GDP (billions USD)** (`gdp`) — p.192
- 1870–1928: Louis Johnston and Samuel H. Williamson, "What Was the U.S. GDP Then?" MeasuringWorth, 2015. Series: Nominal GDP (http://www.measuringworth.com/datasets/usgdp/result.php). Levels.
- 1929–2020: Bureau of Economic Analysis (2021), GDP and the National Income and Product Account (NIPA) Historical Tables, Table 1.1.5. Gross Domestic Product (A) (Q) (https://www.bea.gov/iTable/index_nipa.cfm). Levels.

**Real GDP per capita (PPP, 1990 Int$, Maddison)** — p.193: standard block.
**Real GDP per capita (index, 2005=100)** — p.193: standard block (World Bank 2021).
**Real consumption per capita (index, 2006=100)** — p.193: standard block.

**Investment-to-GDP ratio** (`iy`) — p.193
- 1870–1945: Mitchell, Brian (2007) International Historical Statistics: The Americas 1750–2005, Palgrave, London.
- 1946–2020: IMF IFS, Data Report "National Accounts", Series "Gross Domestic Capital Formation, Nominal".

**Consumer prices (index, 1990=100)** (`cpi`) — p.193
- 1870–1946: Peter H. Lindert and Richard Sutch, "Consumer price indexes, for all items: 1774–2003." Table Cc1-2 and other tables in Historical Statistics of the United States, Earliest Times to the Present: Millennial Edition. Chainlinked.
- 1947–1977: FRED dataset. Consumer Price Index for All Urban Consumers: All Items (CPIAUCSL). Annual average of monthly observations (https://fred.stlouisfed.org/series/CPIAUCSL). Chainlinked.
- 1978–2020: Bureau of Labor Statistics (2021), CPI index, all items, year average (CPI-U-RS, All items; https://www.bls.gov/cpi/research-series/home.htm).

**Narrow Money (billions USD)** (`narrowm`) — pp.193–194
- 1870–1917: monetary base from Rousseau and Wachtel (1998), Financial Intermediation and Economic Performance: Historical Evidence from Five Industrialized Countries.
- 1918–2019: monetary base from the Federal Reserve Bank of St. Louis, Adjusted Monetary Base (http://research.stlouisfed.org/fred2/data/AMBSL.txt).
- 2020: Federal Reserve Bank of St. Louis, Monetary Base, Total, not seasonally adjusted.
- [note] US "narrow money" is the monetary base, not M1.

**Broad Money (billions USD)** (`money`) — p.194
- 1870–1947: M3 from Milton Friedman, Anna J. Schwartz and Robert Rasche listed in Anderson, R.G. (2003) Some Tables of Historical U.S. Currency and Monetary Aggregates Data. Table 3 M3 (https://research.stlouisfed.org/wp/2003/2003-006.pdf). Levels.
- 1948–1959: constructed by St. Louis Fed. Only available online: https://research.stlouisfed.org/aggreg/. Home -> monetary indices. "M2 and M3 data" excel file. Level.
- 1960–2020: St. Louis Fed. M3 for the United States. FRED economic data – Releases – Main economic indicators (https://research.stlouisfed.org/fred2/series/MABMM301USA189S#). Level.

**Short-term interest rate (nominal, percent per year)** (`stir`) — p.194
- 1870–2020: Lawrence H. Officer, "What Was the Interest Rate Then?" MeasuringWorth. Short-Term Rate: Surplus Funds, Contemporary Series. "The Series involves the short-term lending or borrowing of surplus funds, that is, funds that are considered excess by the lending institution and are required for immediate temporary use by the borrowing entity." (www.measuringworth.com/datasets/interestrates/).

**Long-term interest rate (nominal, percent per year)** (`ltrate`) — p.194
- 1870: Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. BoE Staff Working Paper No. 845.
- 1871–1939: Shiller, R. (2000). Irrational Exuberance. 10-year government bond rate. December values. Online Data. http://www.econ.yale.edu/~shiller/data.htm
- 1940–1953: Schmelzing, P. (2020).
- 1954–2020: IMF IFS, Series "Government Bonds, percent per Annum".

**Current Account (billions USD)** (`ca`) — pp.194–195
- 1870–1945: M. Jones & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER WP 6103 (http://www.nber.org/databases/jones–obstfeld/).
- 1946–1969: B. Mitchell (2007), IHS: The Americas 1750–2005.
- 1970–2020: IMF IFS. Supplementary Items, Current Account, Net (excluding exceptional financing), US Dollars (https://data.imf.org/).

**Imports & Exports (billions USD)** (`imports`, `exports`) — p.195
- 1870–1949: B. Mitchell (2007), IHS: The Americas 1750–2005.
- 1950–2020: IMF IFS: National Accounts, Expenditure, Gross Domestic Product, External Balance of Goods and Services, Exports/Imports of Goods and Services, Nominal, Domestic Currency.

**Government Revenues (billions USD)** (`revenue`) — p.195
- 1870–1900: Bureau of the Census (1949), Historical Statistics of the United States 1789–1945, U.S. Department of Commerce, Washington. Series P 89–98. "Federal Government Finances – Treasury Receipts, And Surplus Or Deficit: 1789 to 1945", P 89 Total receipts.
- 1901–2020: Office of Management and Budget (2021), Historical Tables. Table 1.1 "Summary of receipts, outlays, and surpluses or deficits (-): 1789 – 2024", Series "Total receipts".

**Government Expenditure (billions USD)** (`expenditure`) — p.195
- 1870–1900: Bureau of the Census (1949), Historical Statistics of the United States 1789–1945. Series P 99–108. "Federal Government Finances – Treasury Expenditures: 1789 to 1945", P 99 Total expenditures, excluding debt retirements.
- 1901–2020: Office of Management and Budget (2021), Historical Tables. Table 1.1, Series "Total outlays".
- [note] US fiscal series are federal government only.

**Public debt-to-GDP ratio** (`debtgdp`) — p.195
- 1870–1945: Bureau of the Census (1949), Historical Statistics of the United States 1789–1945. Series P 132–143. "Federal Government Finances – Public Debt: 1791 to 1945", Principal or public debt outstanding, Total gross debt, amount. GDP used is the one from the Macropanel. Levels.
- 1946–2020: Office of Management Budget. Table 7.1 "Federal debt at the end of year" (http://www.whitehouse.gov/omb/budget/historicals).

**USD exchange rate (local currency/USD)** (`xrusd`) — p.195
- USD/USD exchange rate = 1 at all times.

**Peg dummy / Strict peg dummy** — pp.195–196: standard block.
**Exogenous monetary policy shocks** — p.196: standard text.

**House prices (nominal index, 1990=100)** (`hpnom`) — p.196
- 1890–2012: Knoll et al. (2014). Year average values. [note: starts 1890.]
- 2013–2020: OECD housing prices database. Nominal series. Chain-linked.

**Unemployment rate (percent)** (`unemp`) — p.196
- 1890–1946: Mitchell, Brian (2013), IHS The Americas, 1750–2010, Table B2 North America Unemployment.
- 1947–2020: ILOSTAT (2021), "Unemployment rate by sex and age" based on the Current Population Survey.

**Wages (index, 1990=100)** (`wage`) — pp.196–197
- 1870–1889: International Historical Statistics. Americas Labour Force – Money/Wages in Industry. Average annual earnings of non-farm employees. Chainlinked.
- 1890–1989: IHS. Americas Labour Force – Money/Wages in Industry. Average hourly earnings in manufacturing. Chainlinked.
- 1948–1989: IMF IFS, Labor Markets, Manufacturing Wage Rates, Index. Chainlinked. [note: overlaps the 1890–1989 entry as printed.]
- 1990–2020: OECD. Average annual wages. Current prices. Levels.

**Credit Data (billions USD)** — headings carry the qualifier "(All Depository Institutions)".

**Total loans to non-financial private sector (All Depository Institutions)** (`tloans`) — p.197
- 1880–1912: calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Loans Total" and United States Census Bureau, ibid Table "Amount of resources and liabilities of savings banks", Series "Loans on Real Estate".
- 1913–1938: calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Loans Total" and R. Sutch & S.B. Carter (2006), ibid. Table Cj389–397 "Savings and loan associations–number, assets, liabilities: 1922–1989", Series Cj391 "Mortgage loans" (hsus.cambridge.org).
- 1939–1945: calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Loans Total", Table A1–a, Series "Total loans" subtracted by "Loans for purchasing or carrying securities".
- 1945–2017: calculated from Federal Reserve Bank of the United States (2014), Flow and Funds Z1. Total loans of US-chartered depository institutions and credit unions to domestic households and the non-financial business sector. Data include GSE and private mortgage backed securities held on balance sheet.
- 2017–2020: calculated from Federal Reserve Bank of the United States (2022), Flow and Funds Z1. Total loans of US-chartered depository institutions and credit unions. Data include GSE and private mortgage backed securities held on balance sheet (https://www.federalreserve.gov/releases/z1/default.htm). Steps: 1) Download csv files, 2) go to L.111 search first series codes and in L.114 search for second series. Series codes: US-chartered depository institutions: FL763065005.A FL763066000.A FL763068005.A FL763063663.A FL763063673.A FL763063653.A FL763063693.A LM763061503.A FL763061403.A FL763061603.A FL763061803.A; Credit unions: FL473068005.A FL473066000.A FL473065100.A FL473061705.A
- [note] US credit series start 1880; "Fraser Federal Reserve Archive (1959), ibid." and "United States Census Bureau, ibid." refer to full citations given before p.101 (not in this range).

**Mortgage loans to non-financial private sector (All Depository Institutions)** (`tmort`) — pp.197–198
- 1880–1895: growth rate calculated from United States Census Bureau, ibid. Table "Amount of resources and liabilities of savings banks", Series "Loans on Real Estate".
- 1896–1912: calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Loans Real Estate" and United States Census Bureau, ibid. Table "Amount of resources and liabilities of savings banks", Series "Loans on Real Estate".
- 1913–1945: calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Loans Real Estate" and R. Sutch & S.B. Carter (2006), ibid. Table Cj389–397, Series Cj391.
- 1945–2016: calculated from Federal Reserve Bank of the United States (2014), Flow and Funds Z1. Total loans of US-chartered depository institutions and credit unions to household and non-financial business secured by real estate. Data include GSE and private mortgage backed securities held on balance sheet.
- 2017–2020: calculated from Federal Reserve Bank of the United States (2022), Flow and Funds Z1 (same steps: L.111 first codes, L.114 second codes). US-chartered depository institutions: FL763065005.A FL763063663.A FL763063673.A FL763063653.A FL763063693.A LM763061503.A FL763061403.A FL763061603.A FL763061803.A; Credit unions: FL473065100.A FL473061705.A

**Total Loans to Households (All Depository Institutions)** (`thh`) — p.198
- Sum of Loans to Households Secured by Real Estate and Other Loans to Households.

**Loans to Households Secured by Real Estate (All Depository Institutions)** (component) — p.198
- 1880–1938: growth rate calculated from Mortgage loans to non-financial private sector (All Depository Institutions).
- 1939–1945: growth rate calculated from Fraser Federal Reserve Archive (1959), ibid. Table A–1, Series "Real estate on residential property".
- 1945–2017: calculated from Federal Reserve Bank of the United States (2014), Flow and Funds Z1. Total loans of US-chartered depository institutions and credit unions. Data include GSE and private mortgage backed securities held on balance sheet.
- 2017–2020: calculated from Federal Reserve Bank of the United States (2022), Flow and Funds Z1. Steps: 1) Download csv files, 2) go to csv and in L.218 search for first series code, in L.219 search for second series code, in L.111 search for series codes 3-6 and in L.114 search for series codes 7 and 8. US-chartered depository institutions: FL763065105.A FL763065403.A FL763061603.A FL763061803.A FL763063663.A FL763063673.A; Credit unions: FL473065100.A FL473061705.A

**Other Loans to Households (All Depository Institutions)** (component) — pp.198–199
- 1945–2017: calculated from Federal Reserve Bank of the United States (2014), Flow and Funds Z1. Total loans of US-chartered depository institutions and credit unions. Data include GSE and private mortgage backed securities held on balance sheet.
- 2017–2020: calculated from Federal Reserve Bank of the United States (2022), Flow and Funds Z1 (L.111 first code, L.114 second code). US-chartered depository institutions: FL763066000.A; Credit unions: FL473066000.A

**Total Loans to Business (All Depository Institutions)** (`tbus`) — p.199
- Residual of Total loans to non-financial private sector and Total Loans to Households (All Depository Institutions).

**Corporate debt** (`bdebt`) — p.199
- 1916–1938: total corporate debt less interbank debt from James, John A. and Richard Sylla (2006), "Debt and Flow of Funds" in "Historical Statistics of the United States" edited by Susan B. Carter and Scott Sigmund Gartner and Michael R. Haines and Alan L. Olmstead and Richard Sutch and Gavin Wright.
- 1945–2020: total loans, bonds and miscellaneous liabilities of non-financial corporate businesses and total loans and miscellaneous liabilities of non-financial non-corporate businesses from Board of Governors of the Federal Reserve System (2021) "Financial Accounts of the United States".
- [note] gap 1939–1944; starts 1916.

**Bank balance sheet ratios** "(Ratios in %, underlying data in billions USD)"

*Capital ratio* (`lev`) — pp.199–200
- Total Assets (billions USD):
  - 1870–1949: Historical Statistics of the United States, Table Cj265-272. Commercial banks-liabilities: 1834-1980, sum of "Deposits", "Capital" and "Other Liabilities". Chainlinked.
  - 1950–2017: FDIC, FDIC insured commercial banks, series "Total Liabilities and Equity Capital" (https://www5.fdic.gov/hsob/HSOBRpt.asp). Levels.
  - 2018–2020: FDIC, Assets and Liabilities of FDIC-Insured Commercial Banks and Savings Institutions, series "Total liabilities and capital" (https://www.fdic.gov/analysis/quarterly-banking-profile/), "Balance Sheet", chainlinked.
- Capital (billions USD):
  - 1870–1949: Historical Statistics of the United States, Table Cj265-272. Commercial banks-liabilities: 1834-1980, series "Capital Accounts". Chainlinked.
  - 1950–1983: FDIC, FDIC insured commercial banks, series "Total Equity Capital" (https://www5.fdic.gov/hsob/HSOBRpt.asp). Chainlinked (difference) ratio.
  - 1984–2017: FDIC, Assets and Liabilities of FDIC-Insured Commercial Banks and Savings Institutions, capital ratio computed, using series "Tier 1 leverage capital (PCA definition)" and "Total Liablities and Equity Capital". Capital computed using "Total Assets" series (above) and level of capital ratio (https://www.fdic.gov/bank/analytical/qbp/).
  - 2018–2020: FDIC, Assets and Liabilities of FDIC-Insured Commercial Banks and Savings Institutions, series "Tier 1 leverage capital (PCA definition)" (quarterly-banking-profile), "Balance Sheet", chainlinked.

*Loans-to-Deposits ratio* (`ltd`) — p.200
- Deposits (billions USD):
  - 1870–1949: Historical Statistics of the United States, Table Cj265-272. Commercial banks-liabilities: 1834-1980, series "Total Deposits". Chainlinked.
  - 1950–2017: FDIC, FDIC insured commercial banks, series "Total Deposits" (https://www5.fdic.gov/hsob/HSOBRpt.asp). Levels.
  - 2018–2020: FDIC, Assets and Liabilities of FDIC-Insured Commercial Banks and Savings Institutions, series "Deposits" (quarterly-banking-profile), "Balance Sheet", chainlinked.
- Loans (billions USD):
  - 1870–1949: Historical Statistics of the United States, Table Cj265-272. Commercial banks-liabilities: 1834-1980, series "Total Loans". Chainlinked.
  - 1950–2020: FDIC, FDIC insured commercial banks, series "Net Loans and Leases" (https://www5.fdic.gov/hsob/HSOBRpt.asp). Levels.
  - 2018–2020: FDIC, Assets and Liabilities of FDIC-Insured Commercial Banks and Savings Institutions, series "Net loans and leases" (quarterly-banking-profile), "Balance Sheet", chainlinked. [note: printed ranges 1950–2020 and 2018–2020 overlap.]

*Noncore ratios: Noncore ratio = (Total Assets − Capital − Deposits) / (Total Assets − Capital)* — p.201 (the only content on the final page).

---

## (d) Release-6 changes

Not covered in pages 101–201. No release notes, change log, or "what's new in R6" text appears in this range. The only dating clues are the citation years inside the source entries (e.g. "Bank of England (2022)" for UK household/business loans; "Federal Reserve Bank of the United States (2022), Flow and Funds Z1" for US credit 2017–2020; IMF (Oct, 2021) WEO for population growth rates 2018–2020; "Central Statistics Office (2021)" for Ireland), which indicate the extension of the data to 2020 for this release.

## (e) References / bibliography

There is no bibliography section in pages 101–201. The list below collects, as a list, every distinct citation that appears in the source entries of this range (wording follows the PDF; the same work is sometimes cited with slightly different wording in different chapters and only one form is kept here). Chapter-specific statistical-office tables (OECD.Stat, IMF IFS/WEO, Eurostat, AMECO, national statistical databases) are listed once in generic form.

### Academic works, books, working papers (as cited in pp.101–201)

1. Abbas et al (2010). A historical public debt database. IMF Working Paper WP/10/245. https://www.imf.org/external/pubs/cat/longres.aspx?sk=24332.0
2. Accominotti, Olivier, Marc Flandreau, and Riad Rezzik, "The Spread of Empire: Clio and the Measurement of Colonial Borrowing Costs".
3. Anderson, R.G. (2003) Some Tables of Historical U.S. Currency and Monetary Aggregates Data. Federal Reserve Bank of St. Louis WP 2003-006 (M3 from Milton Friedman, Anna J. Schwartz and Robert Rasche). https://research.stlouisfed.org/wp/2003/2003-006.pdf
4. Baffigi, Alberto (2011), Italian National Accounts, 1861–2011, Quaderni di Storia Economica, Number 18 – October 2011.
5. Bakker, Gert P., Theo A. Huitker and Cornelis A. van Bochove (1990), The Dutch Economy 1921-39: Revised Macroeconomic Data for the Interwar, Review of Income and Wealth, Series 36, Number 2, June 1990.
6. Banca d'Italia (1967), ibid. Table 28 "Bilancio complessivo dei gruppi di aziende del sistema bancario".
7. Banca d'Italia (2012). Table "Tassi del mercato monetario e finanziario (1938–1965; media del periodo – per cento)".
8. Banca d'Italia (2019). Supplemento al Bollettino Statistico. La Ricchezza delle Famiglie Italiane.
9. Banca d'Italia, Statistiche Storiche: Serie storiche sull'attività di banche e altre istituzioni finanziarie, 1861-2010; Tabelle storiche tratte dai volumi della collana storica della banca d'italia (tav21); Tassi di cambio della lira 1861-1979; Italian Public debt since national unification, 1861-2007. https://www.bancaditalia.it/statistiche/storiche
10. Bank of England, Three centuries of macroeconomic data (Series: Yield on consols).
11. Bank of England – Statistical Abstracts, Number 1, London 1970; Number 2, London 1975.
12. Bank of England, Quarterly Bulletin 1976 Q2 and 1977 Q2, Statistical Annex, Table 2/1 Banks in the United Kingdom – summary.
13. Bank of England, Financial Policy Core Indicators, CCB core indicators, Spreadsheet 11, Leverage Ratio, Simple. https://www.bankofengland.co.uk/financial-stability
14. Bank of Japan (1986), Nihon Ginko Hyakunen–shi Shiryo–hen (The First Hundred Years – Materials), Tokyo.
15. Bank of Japan, 14-3-a Assets and Liabilities of Domestically Licensed Banks – Banking Accounts (1975–2005); Financial Institutions Accounts work sheets 70, 72, 73, 78; BoJ Data Online series BS02'FAABK_FAAB2DBEAS / FAAB2DBECA / FAAB2DBEL01 / FAAB2DBEA37; BOJ Time-Series Data Search (Money stock; Loans and Bills Discounted by sector; Call Rate).
16. Bank of Portugal (2009), Monetary and financial statistics, Table "Monetary survey"; Bank of Portugal (2014), Bank of Portugal Statistics; Banco de Portugal BPStat (https://bpstat.bportugal.pt/dados/dominios/19/series); Banco de Portugal, "Séries longas para a economia portuguesa – pós II Guerra Mundial", Parte IV – População, Emprego e Desemprego.
17. Banco de España, Boletin Estadistico (Series D_BEEA1000, 298310 (BE_4_3.5), 615195, D_MEE62000, BE0414; Tables 4.1, 4.2, 4.7); Bank of Spain archive stock listings; Bank of Spain 1.14 Euro area monetary aggregates. http://www.bde.es/webbde/en/estadis/infoest/bolest.html
18. Barro, R. & J. Ursúa (2010), Macroeconomic Data Set, Harvard University, Cambridge MA. http://scholar.harvard.edu/barro/publications/barro–ursua–macroeconomic–data; Barro–Ursúa Macroeconomic Data, http://rbarro.com/data–sets/
19. Billings, Mark and Forrest Capie, Capital in British Banking, 1920–1970, Business History, Vol. 49, No. 2, March 2007, 139–162.
20. Board of Governors of the Federal Reserve System (2021) "Financial Accounts of the United States"; Federal Reserve Bank of the United States (2014; 2022), Flow and Funds Z1. https://www.federalreserve.gov/releases/z1/default.htm
21. Bonci, R. and M. Coletta (2006), I Conti finanziari dell'Italia dal 1950 a oggi, Banca d'Italia (Servizio Studi); Bonci and Coletta (2012) "Italy's Financial Accounts since 1950", SSRN: http://ssrn.com/abstract=2120474.
22. Bordo, Michael D., Barry Eichengreen, Daniela Klingebiel, and Maria Soledad Martinez–Peria. 2001. "Is the Crisis Problem Growing More Severe?" Economic Policy: A European Forum 32 (16.32): 51–75 (51-82).
23. Bordo, M. D. & Jonung, L. (1996) Monetary Regimes, Inflation And Monetary Reform: An Essay in Honor of Axel Leijonhufvud.
24. Bureau of the Census (1949), Historical Statistics of the United States 1789–1945, U.S. Department of Commerce, Washington.
25. Bureau of Economic Analysis (2021), GDP and the National Income and Product Account (NIPA) Historical Tables, Table 1.1.5.
26. Bureau of Labor Statistics (2021), CPI-U-RS, All items. https://www.bls.gov/cpi/research-series/home.htm
27. Carreras, Albert and Xavier Tafunell (eds.) (2005), Estadísticas Históricas de España, siglos XIX–XX, Vol. I and Vol. 3, Fundación BBVA, Madrid/Bilbao (Tables 9.16, 9.17, 9.19, 10.35, 12.34, 16.19); Carreras de Odriozola, Albert and Xavier Tafunell Sambola (2006), Estadísticas históricas de España, siglos XIX-XX (wage tables, cuadro 15.23).
28. Central Bank of Ireland (2021), Bank Balance Sheets Data, Tables A.5 and A.5.1.
29. Central Bureau of Statistics of Norway (1948), Statistical Survey 1948; (1978), Statistical Survey 1978, Oslo.
30. Central Statistics Office (Ireland) (1964; 1975; 1982), "National Income and Expenditure"; (2020), "Historical National Income and Expenditure Tables"; (2021), "National Income and Expenditure 2018/2021"; Table GFA02; Table HPM06 "Residential Property Price Index".
31. Centraal Bureau voor de Statistiek (2001), Tweehonderd Jaar Statistiek in Tijdreeksen 1800–1999, Amsterdam.
32. Clark, Gregory, "What Were the UK Earnings and Prices Then?" MeasuringWorth, 2019. https://www.measuringworth.com/datasets/ukearncpi/
33. Clemens, M. A. and Williamson, J. G. (2004). Wealth bias in the first global capital market boom, 1870–1913. The Economic Journal.
34. Committee of London Clearing Bankers, The London clearing banks: evidence by the Committee of London Clearing Bankers to the Committee to Review the Functioning of Financial Institutions, November 1977.
35. Cotula, F. (1999), Serie Contributi, Ricerche per la Storia della Banca d'Italia, Volume III, Stabilità e Sviluppo negli Anni Cinquanta, 3. Politica Bancaria e Struttura del Sistema Finanziario.
36. De Bonis, Riccardo, Fabio Farabullini, Miria Rocchelli, Alessandra Salvio & Andrea Silvestrini, 2013. "A quantitative look at the Italian banking system: evidence from a new dataset since 1861," Working Papers 9, Department of the Treasury, Ministry of the Economy and of Finance.
37. De Bonis, R., F. Farabullini, M. Rocchelli & A. Salvio (2012 and update), "Nuove serie storiche sull'attività di banche e altre istituzioni finanziarie dal 1861 al 2011: che cosa ci dicono?", Banca d'Italia – Quaderni di Storia economica, 26.
38. De Bonis, Riccardo & Andrea Silvestrini, 2013. "The Italian financial cycle: 1861–2011," Cliometrica, DOI 10.1007/s11698–013–0103–5.
39. De Nederlandsche Bank (2000), Nederlandse Financieel Instellingen in de Twintigste Eeuw: Balansreeksen en Naamlijst van Handelsbanken, DNB Statistische Cahiers Nr.3; De Nederlandsche Bank (2012; 2020), Domestic MFI–statistics (monetary), Tables T5.2, 5.2.1, 5.2.4; Table 5.4 Contribution of the Netherlands to euro area monetary aggregates.
40. Denzel, M.A. (2010). Handbook of World Exchange Rates, 1590-1914.
41. Edvinsson, Rodney (2004), "Historical national accounts for Sweden 1800–2000 (Historiska nationalräkenskaper för Sverige 1800–2000)", Version 1.0. http://www.historia.se/tablesAtoX.xls
42. Edvinsson, Rodney, Tor Jacobson och Daniel Waldenström (eds.) (2010). "Historical Monetary and Financial Statistics for Sweden: Exchange Rates, Prices, and Wages, 1277-2008."
43. Eitrheim, Ø., J.T. Klovland and J.F. Qvigstad (eds.) (2004), Historical Monetary Statistics for Norway, 1819–2003, Norges Bank (chapter 5: Jan T. Klovland, Monetary Aggregates in Norway 1819–2003; chapter 6: Ola H. Grytten, The gross domestic product for Norway 1830–2003).
44. Eitrheim, Ø., J.T. Klovland and J.F. Qvigstad (2007), Historical Monetary Statistics for Norway – Part II, Norges Bank Occasional Papers No 38, Oslo (chapter 6 Norwegian wages 1726–2006 classified by industry; chapter 7: O. Eitrheim, O.H. Grytten and J.T. Klovland, Historical Monetary Statistics for Norway – some cross checks of the new data, p 385–434).
45. Esteves, R., J. Reis and F. Ferramosca (2009) "Market Integration in the Golden Periphery. The Lisbon/London Exchange, 1854-1891" Explorations in Economic History 46(3): 324-345.
46. European Central Bank: Balance Sheet Indicators; Statistical Data Warehouse (BSI.M.PT.N.A.T00.A.1.Z5.0000.Z01.E; BSI.M.PT.N.A.L60.X.1.Z5.0000.Z01.E; BSI.M.PT.N.A.L20.A.1.U2.2300.Z01.E; BSI.M.PT.N.A.A20.A.1.U2.2200.Z01.E); Consolidated Banking Data (Tangible equity, I3309).
47. European Commission, Economic and Financial Affairs, AMECO database, Chapter 18 Gross Public Debt.18.2, UDGGL. http://ec.europa.eu/economy_finance/ameco/user/serie/SelectSerie.cfm
48. Eurostat financial accounts (total non-equity liabilities of the private non-financial business sector); Eurostat – Quarterly General Government Consolidated Gross Debt (gov_q_ggdebt).
49. FDIC, Historical Statistics on Banking (https://www5.fdic.gov/hsob/HSOBRpt.asp); Quarterly Banking Profile (https://www.fdic.gov/analysis/quarterly-banking-profile/; https://www.fdic.gov/bank/analytical/qbp/).
50. Ferguson, N. and Schularick, M. (2006). The Empire Effect: The Determinants of Country Risk in the First Age of Globalization, 1880-1913. The Journal of Economic History.
51. Fitzgerald & Kenny (2019), 'Managing a Century of Debt', Journal of Statistical & Social Inquiry Society of Ireland, Vol.48, pp. 1-40.
52. Flandreau and Zumer, 2004, The Making of Global Finance, Paris: OECD Development Centre.
53. Fraser Federal Reserve Archive (1959), ibid. Table A–1 / A1–a (full citation outside this range).
54. Fratianni, M. and F. Spinelli, A Monetary History of Italy, Cambridge 1997.
55. FRED / Federal Reserve Bank of St. Louis: CPIAUCSL; Adjusted Monetary Base (AMBSL); Monetary Base, Total; M3 for the United States (MABMM301USA189S); "M2 and M3 data" (https://research.stlouisfed.org/aggreg/); IR3TIB01PTA156N (Interbank Rates for Portugal).
56. Fregert, K. & R. Gustafsson (2008 / 2005), Fiscal Statistics for Sweden 1719–2003, Research in Economic History, 25, pp169–224.
57. Galenson and Zellner (1957) – The Measurement and Behavior of Unemployment, Chapter: International Comparison of Unemployment Rates, Table 1 "Unemployment Rates, Nine Countries, 1900-1950 (per cent)".
58. García Ruiz, José Luis, "Crisis Financiera en Espana 1930 - 1935", Cuadro 7, "Desarollo de los bancos locales espanoles de 1915 a 1935".
59. Global price and income history group, Nominal GDP historical series. http://gpih.ucdavis.edu/ (original: K. Ohkawa, N. Takamatsu, and Y. Yamamoto, 'Vol. 1 National Income' in K. Ohkawa, M. Shinohara, M. Umemura (eds.), Estimates of Long-Term Economic Statistics of Japan Since 1868, Tokyo: Tokyo Keizai Shinposha, 1974).
60. Goto, Shin'ichi (1970): Nihon no Kin'yu Tokei (Japanese Financial Statistics).
61. Groningen Growth and Development Centre (2014), Historical National Accounts Database, University of Groningen. http://www.ggdc.nl/databases/hna/2009/data/hna_swe_09.xls
62. Grytten, Ola Honningdal. Economic policy and labour markets in Nordic countries during the great depression of the 1930s. In: XIV International Economic History Congress, Helsinki. 2006.
63. Hills, S, Thomas, R and Dimsdale, N (2015) "Three Centuries of Data - Version 2.2", Bank of England; Hills, Thomas and Dimsdale, "A millenium of macroeconomic data – version 3.1", Bank of England; Hills, Sally, Ryland Thomas, and Nicholas Dimsdale (2010), "The UK recession in context — what do three centuries of data tell us?", Quarterly Bulletin of the Bank of England, 2010:4.
64. Historical Statistics of Switzerland online (Universität Zürich, Forschungsstelle für Sozial– und Wirtschaftsgeschichte / Research Center for Economic and Social History, Swiss Economic and Social History Online Database), tables Q.1.a, Q.16a, Q.16b, R.1, O.3, O.4, O.12, O.18b, U.45, F.18a; Hourly Earnings of Male and Female Workers 1831-1995. http://www.fsw.uzh.ch/histstat/main.php
65. Historical Statistics of the United States, Earliest Times to the Present: Millennial Edition (Susan B. Carter, Scott Sigmund Gartner, Michael R. Haines, Alan L. Olmstead, Richard Sutch, Gavin Wright, eds.) — Tables Cc1-2 (Lindert and Sutch), Cj265-272, Cj389–397 (R. Sutch & S.B. Carter (2006)); James, John A. and Richard Sylla (2006), "Debt and Flow of Funds". hsus.cambridge.org
66. Homer, S. and R. Sylla (2005). A History of Interest Rates, Fourth Edition. Wiley Finance.
67. Hortlund, Per (2005), The Long-Term Relationship between Capital and Earnings in Banking, SSE/EFI Working Paper Series in Economics and Finance, No 611.
68. Hundred-year statistics / 100-year statistics of the Japanese Economy; Statistics Department of the Bank of Japan (1966), One Hundred Years of Statistics of the Japanese Economy.
69. ILOSTAT (2020; 2021), Table "Unemployment rate by sex and age (%) - Annual". https://ilostat.ilo.org/data/
70. Ilzetzki, E., C. Reinhart & K. Rogoff (2004), Exchange Rate Arrangements Entering the 21st Century: Which anchor will hold?, Working Paper (unpublished, revised version). http://personal.lse.ac.uk/ilzetzki/IRRBack.htm
71. Ilzetzki, E., C. Reinhart & K. Rogoff (2008) exchange regime coarse classification scheme.
72. Ilzetzki, E., C. Reinhart & K. Rogoff (2017). The Country Chronologies to Exchange Rate Arrangements into the 21st Century: Will the Anchor Currency Hold?
73. International Monetary Fund, International Financial Statistics (various vintages: 2010, 2014, 2015, 2016, 2019, 2021; IFS archive M10 2021); IMF eLibrary; https://data.imf.org/; http://elibrary–data.imf.org/
74. International Monetary Fund, World Economic Outlook (various vintages: April 2019, Aug 2019, April 2021, Oct 2021). https://www.imf.org/external/pubs/ft/weo/2019/01/weodata/index.aspx; http://www.imf.org/external/pubs/ft/weo/2015/02/weodata/index.aspx
75. Instituto Nacional de Estadística (INE), Anuarios Estadísticos (various issues); Anuario Estadístico de España 1962 and 1964. https://www.ine.es/inebase_historia/inebase_historia.htm
76. International Historical Statistics (Mitchell): Mitchell, B. (1988), ibid.; Mitchell, Brian (2003), International Historical Statistics: Europe, 1750–2000, Basingstoke: Palgrave Macmillan; Mitchell, B. (2007), International Historical Statistics: Europe 1750–2005; Africa, Asia & Oceania 1750–2005; The Americas 1750–2005, Palgrave Macmillan, London; Mitchell, Brian (2013), International Historical Statistics: Europe, 1750–2010; Africa, Asia, Oceania 1750–2010; The Americas 1750–2010, Palgrave Macmillan, London.
77. Investor's Monthly Manual.
78. Johnston, Louis and Samuel H. Williamson, "What Was the U.S. GDP Then?" MeasuringWorth, 2015. http://www.measuringworth.com/datasets/usgdp/result.php
79. Jones, M. & M. Obstfeld (1997), Saving, Investment, and Gold: A Reassessment of Historical Current Account Data, NBER Working Paper No. 6103, MIT Press, Cambridge MA. http://www.nber.org/databases/jones–obstfeld/
80. Jordà, Òscar, Moritz Schularick, Alan M. Taylor and Felix Ward, 2019. "Global financial cycles and risk premiums". IMF Economic Review, Volume 67 Number 1, pp. 109-150.
81. Jordà, Òscar, Moritz Schularick and Alan M. Taylor, 2020. "The effects of quasi-random monetary experiments". Journal of Monetary Economics 112: 22-40.
82. Keely & Lyons (2020), "Housing Prices, Yields and Credit Conditions in Dublin since 1945". The Journal of Real Estate Finance and Economics, pp. 1-36.
83. Kellenberg, E. (1939–1942), Kapitalexport und Zahlungsbilanz, Bern, A. Francke. Bd. I: S. 155, 245, 307; Bd. II: S. 87, 244f, 364f.
84. Knoll et al. (2014). No price like home: Global house prices, 1870-2012.
85. League of Nations, International Statistical Yearbook (various issues), Geneva.
86. Lindert, Peter H. and Richard Sutch, "Consumer price indexes, for all items: 1774–2003." Table Cc1-2 in Historical Statistics of the United States, Millennial Edition.
87. López, C.B., A. Carreras & X. Tafunell (2005), Estadísticas Históricas de España, Fundación BBVA, Bilbao (Tables 6.11, 9.12, 9.13); Lopez, Carreras, and Tafunell (1989), Estadisticas Historicas de Espana, table 9.12.
88. Maddison, Angus, Database (2008; 2010; 2012), Table 1 "Population levels, 1AD–2030AD". http://www.ggdc.net/maddison/Historical_Statistics/horizontal–file_02–2010.xls
89. Maddison, Angus (1982), Phases of Capitalist Development. Oxford University Press.
90. The Maddison-Project, 2013 version. http://www.ggdc.net/maddison/maddison-project/home.htm
91. Malo de Molina, José Luis and Pablo Martín-Aceña, "The Spanish financial system – Growth and development since 1900".
92. Martín Aceña, Pablo and M.a Ángeles Pons, "Sistema monetario y financier[o]" in Albert Carreras and Xavier Tafunell ed (2005), Estadisticas Historicas de Espana, Siglos XIX-XX.
93. Mauro, Paolo, Rafael Romeu, Ari(el) Binder, Asad Zaman (2013), "A Modern History of Fiscal Prudence and Profligacy", IMF Working Paper No. 13/5. http://www.imf.org/external/pubs/cat/longres.aspx?sk=40222.0
94. McCarthy et al. (1952), 'Symposium on national income and social accounts', Journal of the Statistical and Social Inquiry Society of Ireland, 28(5), pp. 473-514.
95. MeasuringWorth, Short-Term Rate: Ordinary Funds (UK) / Surplus Funds (US), Contemporary Series; Officer, Lawrence H., "What Was the Interest Rate Then?" MeasuringWorth. www.measuringworth.com/datasets/interestrates/
96. Müller, Karsten (2018) "Credit Markets around the World, 1910–2014", SSRN. https://ssrn.com/abstract=3259636
97. Neal, Larry D., and Marc D. Weidenmier. "Crises in the global economy from tulips to today." Globalization in historical perspective. University of Chicago Press, 2003. 473-514. http://ebutts05.tripod.com/nealweidenmiergsd/
98. Nihon Ginkō Tōkeikyoku & Nihon Ginkō Chōsakyoku (various), Honpō–Keizai–Tōkei, Nihon Ginkō Tōkeikyoku, Tokyo; Nippon Ginkō Tōkeikyoku (various), Keizai–Tōkei–Nenpō, Nippon Ginkō, Tokyo; Bank of Japan (various), Statistics 5 Deposits and Loans; Bank of Japan Statistics (various), Deposits and loans.
99. Nihon kinyu no suryo bunseki (Japanese Edition), "Flow of Funds Accounts of Prewar Japan: 1871–1940".
100. Norges Bank, Historical Monetary Statistics (Short-term interest rates from 1818; Bond yields; Historical Exchange Rates; CPI for Norway from 1516; Gross domestic product; Table_a2 M0/M2); Norges Bank, Nowa. https://www.norges-bank.no/en/topics/Statistics/Historical-monetary-statistics/
101. Nunes, A.B., Valério, N. and Martins de Sousa, R. "The long-run behaviour of the income velocity of money in Portugal: 1854-1992".
102. Obstfeld, M. & A. Taylor (2003), Sovereign Risk, Credibility and the Gold Standard: 1870–1913 Versus 1925–31, Economic Journal, 113, p1–35.
103. OECD: OECD.Stat "OECD national accounts statistics", General government accounts, Table 12; OECD (2021) Exchange rates (indicator) doi: 10.1787/037ed317-en; OECD (2020/2021) OECD iLibrary Long-term interest rates doi: 10.1787/662d712c-en; OECD housing prices database; OECD Average annual wages; OECD short-term interest rate; OECD (2012) Population (hist5); OECD (2015) ALFS summary tables; OECD financial accounts; OECD Statistical Supplement (Tier1 Capital). http://stats.oecd.org/; http://www.oecd–ilibrary.org/statistics
104. Office for National Statistics (UK): Quarterly National Accounts (YBHA); CPI annual rate 00: all items 2015=100; Public sector finances (CG: Total revenue / Total expenditure £m CPNSA; supplementary tables).
105. Office of Management and Budget (2021), Historical Tables, Table 1.1 and Table 7.1. http://www.whitehouse.gov/omb/budget/historicals
106. Officer, Lawrence H., "Exchange Rates Between the United States Dollar and Forty-one Currencies," MeasuringWorth, 2015. http://www.measuringworth.com/exchangeglobal/
107. Pettigrew (1980) "National and sector balance sheets for the United Kingdom", Economic Trends, November, pp. 82-100.
108. PORDATA. Salários – Emprego – Remuneração e ganho. www.pordata.pt
109. Prados de la Escosura, Leandro, Spain's Historical National Accounts: Expenditure and Output (2021; 1850-2015/2016/2017/2020 tables 1, 3, 7, 14, 26, 35). http://espacioinvestiga.org/bbdd-chne/?lang=en
110. Prados De La Escosura, L. (2010), Spain's international position 1850–1913, Journal of Iberian and Latin American Economic History, 20(1), p. 173–215.
111. Reinhart, C. M. & Rogoff, K. S. (2010). From financial crash to debt crisis. (Black market exchange rates.)
112. Reis, Jaime, Chapter 7 – Money and Credit in "Nuno Valério, Portuguese Historical Statistics", Table 7.7 — Banks, bankers and banking houses, 1858-1892, 1919-1990.
113. Riksbank (2008), Historical monetary statistics for Sweden 1668–2008, Swedish Monetary History Project (Table 2 Bank lending; Table 8 Income Statement items of the Swedish commercial banks 1870-2005; Table 9 The Swedish money stock and its components 1871-2007; M0, M3; SEK/GBP exchange rate). www.riksbank.se/en/The-Riksbank/Research/Historical-Monetary-Statistics-/
114. Ritzmann–Blickenstorfer, H. (1996), Historische Statistik der Schweiz, Chronos, Zürich.
115. Roe (1971) "The financial interdependence of the UK economy 1957–66", London: Chapman and Hall.
116. Rousseau and Wachtel (1998), Financial Intermediation and Economic Performance: Historical Evidence from Five Industrialized Countries.
117. Sbano (2008) "New historical data for assets and liabilities in the UK", Economic & Labour Market Review, Vol. 2(4), pp. 40-46.
118. Schmelzing, P. (2020). Eight centuries of global real interest rates, R-G, and the 'suprasecular' decline, 1311-2018. Bank of England Staff Working Paper No. 845.
119. Sheppard, David K. (1971), The Growth and Role of UK Financial Institutions 1880–1962, Methuen & Co, London (Table (A) 1.1; Table (A) 2.4 p.150; Table (A) 3.4 p.184).
120. Shiller, R. (2000). Irrational Exuberance. Online Data. http://www.econ.yale.edu/~shiller/data.htm
121. Smits, J., E. Horlings & J. van Zanden (2000), Dutch GNP and its components 1800–1913, GGDC Research Memorandum No.5, University of Groningen.
122. Smits, J.P., P.J. Woltjer and D. Ma (2009), 'A Dataset on Comparative Historical National Accounts, ca. 1870-1950: A Time-Series Perspective', Groningen Growth and Development Centre Research Memorandum GD-107. http://www.rug.nl/research/ggdc/data/historical-national-accounts
123. Statistics Bureau, Director–General for Policy Planning & Statistical Research and Training Institute (2008), Historical Statistics of Japan.
124. Statistics Netherlands ("Werkloze beroepsbevolking" / "totale beroepsbevolking").
125. Statistics Norway (SSB): Statistical Yearbook of Norway (various); Historical Statistics 1978 (Tables 242, 243); Historical Statistics 1994 (Tables 23.11, 23.12); Historical Tables, General Government, Table 1; The Loan and Securities Market 1992–1998 (NOS C589; Låne- og verdipapirmarkedet); Table 06718; orbofbm tables 71 and 81; statbank "banker" and "kredind"; Financial corporations balance sheet; monetary aggregates. http://www.ssb.no/
126. Statistics Portugal, Statistical Yearbook of Portugal (various issues); Situação Bancaria / Estatísticas Financeiras (various issues); Estatisticas Monetaria Financeiras (various issues; 1950).
127. Statistics Sweden (SCB): CPI Historical numbers 1830–; Financial Market Statistics (Sections 3.10.1, 3.11, 3.11.1, 4.9, 5.1, 5.1.1; M3); Monetary Financial Institutions (MFI) assets and liabilities (MFIM1); Balance sheet statistics, Banks Total (FinBalAr, Series A4, A15, A18, A27-A32). https://www.statistikdatabasen.scb.se/
128. Statistisches Handbuch der Weltwirtschaft 1936.
129. Stuart, Rebecca (2017), '70 years of personal disposable income and consumption in Ireland', Journal of the Statistical and Social Inquiry Society of Ireland, Vol.46, pp.47-70.
130. Swiss National Bank (2007), Historical Time Series nº1 "Monetary aggregates M1, M2 and M3"; nº4 "Interest rates and yields"; Swiss National Bank (2009), Historic(al) Time Series 5 "Banks in Switzerland" (Tables 2, 6, 21); SNB Historische Zeitreihen (Die Banken in der Schweiz; Zinssätze und Renditen); SNB data portal (Banks in Switzerland; Bilanzpositionen der Banken nach Bankengruppen; monetary aggregates; Call money rate). http://www.snb.ch/
131. Takabatake, Economic Statistics of Japan (1955), Bank of Japan.
132. Tamaki, Norio, Japanese Banking, A history, 1859-1959.
133. Taylor, A. (2002), A Century of Purchasing–Power Parity, Review of Economics and Statistics, vol 84(1), pp. 139–150.
134. Tedde de Lorca, Pedro (1974), "La banca privada espanola durante la restauración (1874-1914)" in Gabriel Tortella (ed.): La banca espanola en la restauracion, Madrid, Banco de Espana, Servicio de Estudios, pp. 217-456.
135. Tena Junguito, A. (2007), New series of the Spanish foreign sector, 1850–2000, Working Papers in Economic History WP 07–14, Universidad Carlos III de Madrid.
136. TOKYO DEPT. OF FINANCE GPO. "Financial and Economic Annual of Japan", various years.
137. United Nations (1948). Public Debt, 1914–1946. Department of Economic Affairs, Lake Success, NY.
138. United Nations. Monthly Bulletin of Statistics, January 1951.
139. United States Census Bureau, ibid. Table "Amount of resources and liabilities of savings banks" (full citation outside this range).
140. Valério, N. (ed.) (2001), Portuguese Historical Statistics / Estatísticas Históricas Portuguesas, 2 vol., Instituto Nacional de Estatística, Lisbon (Tables 6.4 B, 6.6 B, 6.6 C, 7.4B, 7.4C, 7.7 A, 8.1, 8.2, 9.2, 9.7, 10.3, 10.6); Valério, N. (2001). História Económica de Portugal. Uma Perspectiva global. Table 7.10.
141. van Leeuwen, Bas, Wage differentials and economic growth in India, Indonesia, and Japan, 1800-2001.
142. van Zanden et al., National Accounts of the Netherlands, 1880–1913. http://nationalaccounts.niwi.knaw.nl/start.htm
143. Waldenström, Daniel (2014), "Swedish stock prices and returns and bond yields, 1856–2012," Sveriges Riksbank; D. Waldenstroem, Swedish Stock and Bond Returns, 1856–2012, IFN Working Paper No. 1027, Research Institute of Industrial Economics, Stockholm.
144. Watanabe, Sachio (ed./publisher), Economic Statistics Annual (1972), Tokyo.
145. Weber, Warren E. 2000. International Data. 1810-1995. Research Department, Federal Reserve Bank of Minneapolis. http://cdm16030.contentdm.oclc.org/cdm/singleitem/collection/p16030coll4/id/8/rec/5
146. Williamson (1995). "The evolution of global labor markets since 1830: background evidence and hypotheses".
147. Williamson (1998) "Real Wages and Relative Factor Prices in the Third World Before 1940: What do they tell us about the Sources of Growth?".
148. World Bank (2018; 2019; 2021), "GDP per capita (constant 2010 US$)" NY.GDP.PCAP.KD; household final consumption expenditure per capita (constant 2010 US$). http://data.worldbank.org/
149. Zamagni, Vera (1994), Una ricostruzione dell'andamento mensile dei salari industriali e dell'occupazione, Ricerche per la storia della banca d'Italia, Volume V, Editori Laterza.
150. Bank for International Settlements, "Credit to the non-financial sector" database. https://www.bis.org/statistics/totcredit.htm
151. Cabinet Office (Japan), Annual Report on National Accounts (2000; various). http://www.esri.cao.go.jp/en/sna/data/kakuhou/files/kako_top.html
152. Land Registry of Japan, Ministry of Land and Transportation, transaction data. https://www.mlit.go.jp/totikensangyo/totikensangyo_tk5_000085.html
153. Anuario Estadistico de la Banca Privada – Consejo Superior Bancario (issues 1974–1978).
154. Diario oficial de avisos de Madrid; La Correspondencia de Espana; ABC (hemeroteca) — newspaper bond quotations for Spain.
155. ESRI/Permanent TSB house price index (Ireland).

## (f) Pages that could not be read, or that were figures only

- All 101 pages (101–201) were read successfully with the Read tool; every page is text (no figures, charts or tables-as-images in this range).
- Page 201 contains only the heading "Noncore ratios" and the formula for the USA; the rest of the page is blank. It is the last page of the document.
- Legibility caveats: (i) p.121 — the Japanese romanised source names are printed with detached macron glyphs ("Nihon Ginko T ¨ okeikyoku", "Nihon Gink ¨ o Ch ¨ osakyoku", "¨ Honpo–Keizai–T ¨ okei"), transcribed here with the macrons restored as Tōkeikyoku / Chōsakyoku / Honpō–Keizai–Tōkei; (ii) p.111, p.142, p.151 — "Karsten Muller ( ¨ 2018)" is the same umlaut-rendering problem (Müller); (iii) p.143 — Portugal population "1870 – 1849" is as printed (should be 1949); (iv) p.133 — the Netherlands "Capital", "Deposits" and "Loans" sub-headings are printed as "Capital Total Assets (converted to millions NLG)", "Deposits Total Assets (...)", "Loans Total Assets (...)" (copy-paste artefact in the heading); (v) p.148 and p.158 — the euro conversion notes read "a Italian Portugese escudo" and "a Italian Spanish peseta"; (vi) p.117 — Japan government expenditure 2010–2020 cites "Series GTR" (revenue code) for the expenditure series; (vii) p.184 — UK Government Revenues 1870–1999 cites "Central government expenditure" from the BoE millennium dataset; (viii) p.170 — the Sweden "Total Loans to Households" 1975–2016 entry runs directly into the "Loans to Households Secured by Real Estate" heading without a paragraph break.


