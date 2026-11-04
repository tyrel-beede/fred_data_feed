# No Price Like Home — online appendix, as encoded for this repository

# "No Price Like Home: Global House Prices, 1870–2012" — Online Appendix, extraction of PDF pages 1–90

Source file: `/tmp/claude-0/-home-claude/942b62dd-c373-526c-a70e-951b52f841cf/scratchpad/history/src/NPLH_documentation.pdf` (171 pages total; this file covers PDF pages 1–90).

Page convention: **PDF page = printed page + 1** (PDF p.1 is the unnumbered title page; PDF p.2 carries printed page "1"). All page references below are PDF pages unless marked "printed".

---

## (a) What the document is

- **Title:** "No Price Like Home: Global House Prices, 1870–2012" (PDF p.1).
- **Authors:** Katharina Knoll, Moritz Schularick and Thomas Steger (PDF p.1).
- **Document type:** "Online Appendix" (PDF p.1). The data part self-describes as: "This data appendix supplements the paper, 'No Price Like Home: Global House Prices' by Knoll, Schularick and Steger that introduces residential house price indices for 14 advanced economies for the period 1870 to 2012. It details and discusses the sources for constructing long-run house price indices." (PDF p.12).
- **Date / version:** Not stated anywhere in pages 1–90. The latest-dated citations in this range are 2016 (CGEDD 2016; OECD 2016; Jordà, Schularick and Taylor 2016), so the version is 2016 or later. [Outside the document: the paper appeared in the *American Economic Review* 107(2), 2017 — this is background knowledge, not something stated in pages 1–90.]
- **Where published:** Not stated in pages 1–90.
- **Structure of the range:**
  - Appendix A "Supplementary material" (PDF pp.2–11): A.1 House price indices: methodology (pp.2–3); A.2 Structural break tests (p.4); A.3 Robustness (pp.5–6); A.4 Alternative decompositions (pp.6–8); A.5 Additional tables and figures (pp.9–11).
  - Appendix B "Data appendix" (PDF p.12 onward): B.1 Description of the methodological approach (pp.12–19); B.2 Australia (pp.19–29); B.3 Belgium (pp.30–37); B.4 Canada (pp.37–46); B.5 Denmark (pp.46–52); B.6 Finland (pp.52–59); B.7 France (pp.59–65); B.8 Germany (pp.66–75); B.9 Japan (pp.76–82); B.10 The Netherlands (pp.83–88); B.11 Norway (p.89– , continues past p.90).
- **Acknowledgments (PDF p.12):** Paul de Wael, Christopher Warisse, Willy Biesemann, Guy Lambrechts, Els Demuynck, Erik Vloeberghs (Belgium); Debra Conner, Gregory Klump, Marvin McInnis (Canada); Kim Abildgren, Finn Østrup, Tina Saaby Hvolbøl (Denmark); Riitta Hjerppe, Kari Leväinen, Juhani Väänänen, Petri Kettunen (Finland); Jacques Friggit (France); Carl-Ludwig Holtfrerich, Petra Hauck, Alexander Nützenadel, Ulrich Weber, Nikolaus Wolf (Germany); Alfredo Gigliobianco (Italy); Makoto Kasuya, Ryoji Koike (Japan); Alfred Moest, Marjan Peppelmann (Netherlands); Roger Bjornstad, Trond Amund Steinset (Norway); Daniel Waldenström (Sweden); Annika Steiner, Robert Weinert, Joel Floris, Franz Murbach, Iso Schmid, Christoph Enzler (Switzerland); Peter Mayer, Neil Monnery, Joshua Miller, Amanda Bell, Colin Beattie, Niels Krieghoff (UK); Jonathan D. Rose, Kenneth Snowden, Alan M. Taylor (US). Magdalena Korb and Katharina Mühlhoff helped with translation.

---

## (b) General methodology

### b.1 Index types (A.1, PDF pp.2–3)

- **Stratification:** "splits the sample into several strata with specific price determining characteristics. A mean or median price index is calculated for each sub-sample and the aggregate index is computed as a weighted average of these sub-indices." Equation (4):

  ΔP^h_T = Σ_{m=1}^{M} ( w^m_t · ΔP^m_T )

  where ΔP^h_T is the aggregate house price change in period T, ΔP^m_T the price change in sub-sample m, and w^m_t the weight of sub-sample m at time t. Weights "are either based on stocks or on transactions and on quantities or values (European Commission, 2013; Silver, 2014)." Stratification "neither controls for changes in the mix of houses that are not related to the sub-samples nor for changes within each sub-sample"; "If the stratification controls for quality change, the method is known as **mix-adjustment** (Mack and Martínez-García, 2011)." (PDF p.2)
- **Hedonic regression:** "the intercept of a regression of the house price on a set of characteristics – such as the number of rooms, the lot size or whether the house has a garage or not – is converted into a house price index (Case and Shiller, 1987). If the set of variables is comprehensive, the hedonic regression method adjusts for changes in the composition and changes in quality." The most common specification is linear, equation (5) (PDF p.3):

  P_t = β^0_t + Σ_{k=1}^{K} ( β^k_t · z^{n,k} ) + ε^n_t

  "where β^0_t is the intercept term and β^k_t the parameter for characteristic variable k and z^{n,k} the characteristic variable k measured in quantities n." (This is the only estimation model shown near the start; the other equations in A are index/accounting identities, see b.6.)
- **Repeat sales:** "circumvents the problem of unobserved heterogeneity as it is based on repeated transactions of individual houses (Bailey, Muth and Nourse, 1963)." **SPAR** (sales price appraisal ratio) "instead of using two transaction prices, matches an appraised value and a transaction price." Caveat: "Because of depreciation and new investments, the constant-quality assumption becomes more problematic the longer the time span between two transactions (Case and Wachter, 2005)." **Weighted repeat sales** (Case and Shiller, 1987) "assigns less weight to transaction pairs of long time intervals." **Hybrid** hedonic/repeat-sales methods (Shiller, 1993; Case, Pollakowski and Wachter, 1991; Case and Quigley, 1991) "may reduce the quality bias." "Yet despite differences in the way house price indices are constructed, different methods tend to deliver similar overall results (Nagarja and Wachter, 2014; Pollakowski, 1995)." (PDF p.3)
- Additional methods encountered in country sections: **median asking/sales price** (Australia), **average transaction price per square metre of developed lots** (Germany pre-1938), **average replacement value** (Canada 1921–49), **average appraised land value** (Japan), **farm real-estate value per acre / per unit of land valuation** (Canada 1949–56 link, Denmark 1875–1938), **Laspeyres-type mix-adjusted** (ABS Australia), **chain Laspeyres stratified** (Statistics Belgium), **matched-model constant-quality** (Statistics Canada new housing), **hedonic + mix-adjusted** (Statistics Finland, INSEE, Statistics Norway), **SPAR** (Danmarks Nationalbank, Statistics Denmark, CBS Netherlands), **hedonic repeat sales** (Eichholtz Herengracht; Eitrheim–Erlandsen aggregate Norway), **weighted repeat sales** (Eitrheim–Erlandsen city indices).

### b.2 Data sources (B.1, PDF pp.12, 14)

"Most countries' statistical offices or central banks began only recently to collect data on house prices. For the 14 countries covered in our sample, data from the early 1970s to the present can be accessed through three principal repositories: the databases maintained by the Bank for International Settlements (2013), the OECD, and the Federal Reserve Bank of Dallas (2013). To extend these back to the 19th century, we used three principal types of country specific data." (PDF p.12)
1. "national official statistical publications, such as the Helsinki Statistical Yearbook or the annual publications of the Swiss Federal Statistical office, and collections of data based on official statistical abstracts. Typically, such official statistics publications contained raw data on the number and value of real estate transactions and in some cases price indices."
2. "published and unpublished data gathered by legal or tax authorities (e.g., the U.K. Land Registry) or national real estate associations (e.g., the Canadian Real Estate Association)."
3. "the previous work of financial historians and commercial data providers." (PDF p.14)

### b.3 Selection principles and the primary series (PDF pp.14–15)

- "Constructing long-run data series usually involved a good many compromises between the ideal and the available data. We often found series spanning short time periods and had to splice them to arrive at a long-run index."
- Three guiding principles: **constant quality, longitudinal consistency, and historical plausibility.**
- "We selected a primary series that is available up to 2012, refers to existing dwellings, and is constructed using a method that reflects the pure price change, i.e. controls for changes in composition and quality. When extending the series, we concentrated on within-country consistency to avoid principal structural breaks that may arise from changes in the market segment a country index covers. We aimed to ensure the broadest geographical coverage for each of the 14 country indices. Likewise we tried to keep the type of house covered constant over time, be it single-family houses, terraced houses, or apartments."
- Historical plausibility: "We heavily draw on country specific economic and social history literature as well as primary sources such as newspaper accounts or contemporary studies on the housing market to scrutinize the general trends and short-term fluctuations in the indices." (PDF pp.14–15)
- "In all cases, the primary series does not extend back to 1870 but has to be complemented with other series." (PDF p.15)

### b.4 Splicing / chain-linking: the decision tree (Figure 17, PDF p.13)

The decision tree (Figure 17, "Methodological decision tree") reads, in order:
1. "Does the current primary series extend back to 1870?" — No → "Is a series available for earlier years that can be used to extend the series backwards?"
2. If no such series → "Is *any* series available for earlier years?" — Yes → "Can we gauge the increase/decrease of house prices between the end of the one series and the [start of the other]?" — Yes → "Splice with growth rates"; No → "No house price index since 1870 available."
3. If an extension series exists → "Does this series extend back to 1870?" (loop) → "Does the method control for quality changes over time?" — No → "Are there equivalent series available that do control for quality change over time?" — No → "Use the one that best accounts for quality change."
4. "Does the series cover the same geographical area as the primary series?" — No → "Are there equivalent series available that cover the same geographical area?" — No → "Use the one that (1) covers a similar area (e.g. rural vs. urban) and (2) provides the broadest geographical coverage."
5. "Does the series cover the same property type as the primary series?" — No → "Are there equivalent series available that cover the same property type?" — No → "Use the one that covers the most similar property type."
6. → "**Splice with growth rates.**"
7. "Is the series historically plausible?" — No → "Is there an equivalent series available that is historically plausible?" — No → "No house price index since 1870 available."
8. "Is the series annual?" — No → "Frequency conversion."
9. "Are irregular components present in any series?" — Yes → "Smooth the series with excess volatility."
10. → "**Construct Index**."

So all country indices are chain-linked by growth rates of the sub-series; where no overlapping series exists, a point estimate of the cumulative change over a gap is used (Canada 1949–56 via farm real-estate values; Germany 1939–61 via a survey estimate of a 300 percent rise in building-site prices; Japan 1931–35 via paddy-field prices).

### b.5 Nominal vs real; coverage; quality grading

- The country tables document **nominal** indices. Real indices are obtained by deflating with CPI; CPI sources are listed per country (mostly Taylor (2002) to 2007 and IMF (2012) after; France: Mitchell (2013)/IMF (2015); Japan: van Leeuwen (2004)/IMF (2012); Belgium: National Bank of Belgium (2012)/IMF (2012)). The authors caution: "historical CPI series are often confined to urban areas. Due to limited data availability, changes in the quality of commodities and the timing of the introduction of new commodities are not always adequately captured by the historical CPI data. See Grytten (2004) and Officer (2007)." (PDF p.19). Figure 14 (PDF p.9) also shows real prices deflated by "average inflation over preceding 5 years" (expected inflation) as a check.
- **Coverage:** mixed. Pre-1900/pre-WWII portions are frequently single-city or regional (Melbourne; Brussels; Helsinki; Paris; Berlin → Hamburg → 10 cities; Tokyo/six cities; Herengracht street in Amsterdam; four Norwegian city centres), or farm property (Denmark 1875–1938; Canada 1949–56 link), or building sites/land only (Finland 1905–46; Germany 1962–70; Japan throughout). National coverage typically only from the 1930s–1970s onward.
- **Quality grading:** there is **no formal letter/numeric quality grade** in pages 1–90. Instead each country section ends with an explicit list of "weaknesses"/"drawbacks"/"flaws", and for several countries a crude constant-quality adjustment is computed but *not* used: real average annual growth adjusted downward using estimates of expenditure on alterations/additions as a share of housing value. Reported: Australia 1.68% → 1.11% (1870–2012); Belgium 1.96% → 1.77% (1878–2012); Canada 2.21% → 1.67% (1921–2012); Denmark 0.99% → 0.57% (1875–2012). Each time: "As this is a rather crude adjustment, we use the unadjusted index … for our analysis."
- Each country's sub-series carries a **Series ID** (AUS1–AUS8, BEL1–BEL5, CAN1–CAN3, DNK1–DNK3, FIN1–FIN3, FRA1–FRA3, DEU1–DEU6, JPN1–JPN3, NLD1–NLD3); bridging segments without an ID are listed in the tables without an ID (Canada 1949–56; Germany 1939–61; Japan 1931–35).

### b.6 Other methodological material in Appendix A

- **A.2 Structural break tests (Table 3, PDF p.4):** Bai and Perron (2003), on the log-level of the real house price index, trimming 10 percent, significance 0.05, White heteroskedasticity-consistent standard errors, heterogeneous error distributions across breaks; break dates = first date of new regime; sample 1870–2012; italics = downward breaks.

  | Country | k=1 | k=2 | k=3 |
  |---|---|---|---|
  | Australia | 1963 | 1950, 1988 | 1950, 1970, 1999 |
  | Belgium | 1991 | 1966, 1998 | 1966, 1998 |
  | Canada | 1973 | 1949, 1974 | 1947, 1973, 2004 |
  | Denmark | 1961 | 1961, 2000 | 1961, 2000 |
  | Finland | 1962 | 1962 | 1962 |
  | France | 1964 | 1964 | 1964 |
  | Germany | 1964 | 1964 | 1887, *1916*, 1963 |
  | Great Britain | 1972 | 1963, 1987 | 1946, 1977, 2001 |
  | Japan | 1960 | 1960 | *1945*, 1955, 1965 |
  | Netherlands | 1995 | 1970, 1998 | 1970, 1998 |
  | Norway | 1999 | 1999 | 1999 |
  | Sweden | 2000 | 2000 | 2000 |
  | Switzerland | 1952 | 1952 | 1952 |
  | USA | 1953 | 1953 | 1953 |

- **A.3 Robustness (PDF pp.5–6):** Figure 9 (population- and GDP-weighted mean real house price indices, 14 countries, 1990=100), Figure 10 (area- and GDP p.c.-weighted), Figure 11 (fixed samples: 4 countries with continuous data since 1870 = Australia, France, Netherlands, Norway; 6 since 1880 = + Denmark, Sweden; 9 since 1905 = + Switzerland, US, Belgium is not in the 9 — the note lists Australia, Denmark, France, Netherlands, Norway, Sweden, Switzerland, U.S.; that is 8 names for a "9-country" sample, as printed). Note on borders: "most border changes were relative minor. Exceptions include the changes for Germany in the interwar period, after World War II and after reunification in 1990, and the change for the U.K. after the Irish Free State seceded in 1922."
- **A.4 Alternative decompositions (PDF pp.6–8):** The main-text decomposition of house prices into land and construction costs assumes Cobb-Douglas with α = 0.5. The appendix derives the Leontief case F(Z,H)=min{Z/a, X/b}: p^H = a·p^Z + b·p^X; growth-rate accounting equation (6) p^H_{t+1}/p^H_t = w_t·p^Z_{t+1}/p^Z_t + (1−w_t)·p^X_{t+1}/p^X_t with w_t := p^Z_t Z_t/(p^H_t F(.)); imputed land price equation (7) p^Z_{t+1}/p^Z_t = (1/w_t)·p^H_{t+1}/p^H_t − ((1−w_t)/w_t)·p^X_{t+1}/p^X_t. Davis and Heathcote (2007) start from p^Z_t Z_t = p^H_t H_t − p^X_t X_t and obtain the same accounting equation (8). Figure 12: sensitivity of imputed land prices to α (0.25, 0.5, 0.75); Figure 13: Cobb-Douglas vs Leontief (w_t = 0.5). Equation (9) adds a cost term v_t (ad valorem sales tax, building permit fees): p^H_t = B/(1−v_t)·(p^Z_t)^α (p^X_t)^{1−α}, B := α^{−α}(1−α)^{−(1−α)}; "Yet Figure 8 indicates that such additional factors do not systematically bias the results."
- **A.5 Additional tables and figures (PDF pp.9–11):** Figure 14 real house prices, 14 countries (also deflated by expected inflation); Figure 15 real construction costs, 14 countries; Figure 16 real residential land prices, 6 countries (AUS, BEL, CHE, GBR, JPN, USA; 1990=100, CHE 1975=100); Table 4 (below).

- **Table 4: Annual summary statistics by country and by period (PDF p.11).** Columns: Δ log Nominal House Price Index (N, mean, s.d.) | Δ log CPI (N, mean, s.d.) | Δ log Real GDP p.c. (N, mean, s.d.). Rows: Full Sample / Pre-World War II / Post-World War II. Note: "World wars (1914–1919 and 1939–1947) omitted."

  | Country / period | HP N | HP mean | HP s.d. | CPI N | CPI mean | CPI s.d. | GDPpc N | GDPpc mean | GDPpc s.d. |
  |---|---|---|---|---|---|---|---|---|---|
  | Australia Full | 127 | 0.047 | 0.106 | 127 | 0.027 | 0.047 | 127 | 0.016 | 0.040 |
  | Australia Pre-WWII | 62 | 0.009 | 0.083 | 62 | 0.001 | 0.037 | 62 | 0.011 | 0.054 |
  | Australia Post-WWII | 65 | 0.083 | 0.114 | 65 | 0.052 | 0.041 | 65 | 0.021 | 0.019 |
  | Belgium Full | 119 | 0.043 | 0.094 | 126 | 0.021 | 0.054 | 127 | 0.021 | 0.041 |
  | Belgium Pre | 54 | 0.029 | 0.126 | 61 | 0.008 | 0.069 | 62 | 0.019 | 0.055 |
  | Belgium Post | 65 | 0.056 | 0.054 | 65 | 0.034 | 0.031 | 65 | 0.023 | 0.020 |
  | Canada Full | 75 | 0.048 | 0.078 | 127 | 0.019 | 0.044 | 127 | 0.018 | 0.046 |
  | Canada Pre | 17 | -0.014 | 0.048 | 62 | -0.001 | 0.048 | 62 | 0.017 | 0.062 |
  | Canada Post | 58 | 0.066 | 0.076 | 65 | 0.038 | 0.032 | 65 | 0.019 | 0.023 |
  | Denmark Full | 122 | 0.032 | 0.074 | 127 | 0.021 | 0.053 | 127 | 0.019 | 0.024 |
  | Denmark Pre | 57 | -0.002 | 0.060 | 62 | -0.004 | 0.058 | 62 | 0.017 | 0.025 |
  | Denmark Post | 65 | 0.061 | 0.074 | 65 | 0.046 | 0.032 | 65 | 0.020 | 0.024 |
  | Finland Full | 92 | 0.088 | 0.156 | 127 | 0.031 | 0.059 | 127 | 0.026 | 0.034 |
  | Finland Pre | 27 | 0.094 | 0.244 | 62 | 0.006 | 0.055 | 62 | 0.023 | 0.036 |
  | Finland Post | 65 | 0.085 | 0.105 | 65 | 0.054 | 0.053 | 65 | 0.028 | 0.031 |
  | France Full | 127 | 0.062 | 0.075 | 127 | 0.036 | 0.071 | 127 | 0.020 | 0.038 |
  | France Pre | 62 | 0.023 | 0.055 | 62 | 0.017 | 0.73 [sic, as printed] | 62 | 0.013 | 0.049 |
  | France Post | 65 | 0.099 | 0.072 | 65 | 0.054 | 0.065 | 65 | 0.027 | 0.022 |
  | Germany Full | 110 | 0.040 | 0.108 | 123 | 0.025 | 0.097 | 127 | 0.027 | 0.043 |
  | Germany Pre | 60 | 0.043 | 0.140 | 58 | 0.022 | 0.139 | 62 | 0.019 | 0.049 |
  | Germany Post | 50 | 0.037 | 0.046 | 65 | 0.027 | 0.026 | 65 | 0.034 | 0.035 |
  | Japan Full | 84 | 0.078 | 0.155 | 127 | 0.027 | 0.120 | 127 | 0.029 | 0.046 |
  | Japan Pre | 19 | -0.006 | 0.093 | 62 | 0.011 | 0.150 | 62 | 0.015 | 0.049 |
  | Japan Post | 65 | 0.103 | 0.162 | 65 | 0.043 | 0.081 | 65 | 0.042 | 0.038 |
  | Netherlands Full | 127 | 0.026 | 0.091 | 127 | 0.015 | 0.044 | 127 | 0.019 | 0.031 |
  | Netherlands Pre | 62 | -0.009 | 0.086 | 62 | -0.007 | 0.049 | 62 | 0.014 | 0.036 |
  | Netherlands Post | 65 | 0.059 | 0.084 | 65 | 0.036 | 0.026 | 65 | 0.024 | 0.023 |
  | Norway Full | 127 | 0.041 | 0.087 | 127 | 0.020 | 0.058 | 127 | 0.023 | 0.027 |
  | Norway Pre | 62 | 0.013 | 0.085 | 62 | -0.007 | 0.066 | 62 | 0.018 | 0.033 |
  | Norway Post | 65 | 0.068 | 0.080 | 65 | 0.045 | 0.035 | 65 | 0.027 | 0.018 |
  | Sweden Full | 122 | 0.036 | 0.077 | 127 | 0.021 | 0.047 | 127 | 0.022 | 0.029 |
  | Sweden Pre | 57 | 0.010 | 0.052 | 62 | -0.004 | 0.045 | 62 | 0.022 | 0.036 |
  | Sweden Post | 65 | 0.059 | 0.089 | 65 | 0.045 | 0.035 | 65 | 0.022 | 0.021 |
  | Switzerland Full | 96 | 0.030 | 0.051 | 127 | 0.008 | 0.048 | 127 | 0.019 | 0.035 |
  | Switzerland Pre | 31 | 0.019 | 0.062 | 62 | -0.008 | 0.061 | 62 | 0.016 | 0.044 |
  | Switzerland Post | 65 | 0.036 | 0.044 | 65 | 0.024 | 0.022 | 65 | 0.016 | 0.024 |
  | United Kingdom Full | 98 | 0.044 | 0.089 | 127 | 0.024 | 0.047 | 127 | 0.015 | 0.025 |
  | UK Pre | 33 | -0.008 | 0.088 | 62 | -0.004 | 0.035 | 62 | 0.011 | 0.030 |
  | UK Post | 65 | 0.070 | 0.080 | 65 | 0.050 | 0.042 | 65 | 0.019 | 0.019 |
  | United States Full | 107 | 0.026 | 0.078 | 127 | 0.015 | 0.040 | 127 | 0.017 | 0.041 |
  | US Pre | 42 | 0.006 | 0.115 | 62 | -0.007 | 0.040 | 62 | 0.015 | 0.053 |
  | US Post | 65 | 0.038 | 0.039 | 65 | 0.036 | 0.027 | 65 | 0.020 | 0.023 |
  | All Countries Full | 1557 | 0.044 | 0.097 | 1900 | 0.024 | 0.069 | 1905 | 0.021 | 0.037 |
  | All Pre-WWII | 645 | 0.016 | 0.102 | 925 | 0.004 | 0.082 | 930 | 0.016 | 0.048 |
  | All Post-WWII | 912 | 0.066 | 0.087 | 975 | 0.043 | 0.046 | 975 | 0.025 | 0.027 |

  (The N column for house prices reveals the effective length of each series: Canada 75, Japan 84, Finland 92, Switzerland 96, UK 98, US 107, Germany 110 out of a possible 127 non-war years.)

### b.7 Construction cost and other series (B.1, PDF pp.15–19)

- Replacement cost would be ideal; "Data on replacement costs that perfectly matches our long-run house prices series, however, are not available. For the U.S., estimates of changes in replacement values exist for 1930–2012 (Davis and Heathcote, 2007). In all other cases, we use long-run price indices for construction costs to proxy for replacement costs of residential buildings." Assumption: cost of constructing new buildings and cost of replacing the structures move together in the long run "since both are primarily a function of the price of materials and wages." (PDF p.15)
- Two index types: **input cost indices** (factor prices: wages, materials, equipment hire, transport, energy) and **output price indices** (prices contractors charge; also reflect profit margins, productivity, overhead; Eurostat 1996; OECD and EUROSTAT 1996). Architect fees, legal fees, VAT and land are in neither (Figure 18, PDF p.16). "Whenever possible, we therefore rely on output price indices as estimates of replacement costs." Equations (10) ICI = Σ_i (Σ_k I^m_{c,k} w^m_{c,k} + I^w w^w_c) w_c and (11) OPI = Σ_i (I^c w^c) (PDF p.17).
- Construction cost indices "do not adjust for quality changes" and are regularly rebased; possible bias to the decomposition acknowledged: "While we cannot gauge the exact size and direction of the bias, it is unlikely to systematically distort the long-run trends we uncover." (PDF p.18)
- Real unit labour cost indices for construction, 1950–1970, for Canada, France, Finland, Germany, Norway, Sweden, UK, US: ULC_t = C_t/O_t (equation 12), wages deflated by CPI, output deflated by construction cost index (Bosworth and Perry, 1994). (PDF p.18)
- Other housing statistics: farmland prices; total value of housing stock (OECD national accounts; Goldsmith 1981, 1985; Piketty and Zucman 2014 for Australia, Canada, France, Germany, Italy, Japan, US, UK; Davis and Heathcote 2007 for the US). Macro/financial variables from Jordà, Schularick and Taylor (2016). (PDF pp.18–19)

---

## (c) Country-by-country documentation (house price index)

### AUSTRALIA — B.2, PDF pp.19–29 (printed 18–27). Data available 1870–2012.

**Sources discussed**
- Stapledon (2012b): Sydney and Melbourne indices 1880–2011. 1880–1943 "computed from the median asking price for all residential buildings, indiscriminate of their characteristics and specifics"; 1943–1949 "estimates a fixed price" (fn 25: price controls on houses and land imposed 1942, removed 1948, Stapledon 2007, 23 f.); 1950–1970 median sales price; 1970–1985 Abelson and Chung (2005) medians; 1986–2011 ABS (2013) established houses. Fn 26: "The ask price series for residential houses (1880–1943) and the sales price series (1948–1970) are compiled from weekly property market reports in the *Sydney Morning Herald* and the *Melbourne Age*. The reports are for auction sales and private treaty sales." (PDF p.19)
- Abelson and Chung (2005) medians for Sydney (1991 Applied Economics/Travers Morgan study on Land Title Office data 1970–1989; NSW Valuer-General 1990–2003) and Melbourne (Productivity Commission / Valuer-General data 1970–1979, Victorian Valuer-General 1980–2003); also Brisbane, Adelaide, Perth, Hobart, Darwin, Canberra (fn 27). (PDF pp.19–20)
- Stapledon (2007, 64 ff.): aggregate median price series for detached houses in the six state capitals (Adelaide, Brisbane, Hobart, Melbourne, Perth, Sydney) 1880–2006. Pre-1973 prices for the four non-Sydney/Melbourne capitals are *estimated* from census weekly rents via "rent-to-rent ratios" (fn 28: census years 1911, 1921, 1933, 1947, 1954) applied to the weighted Sydney–Melbourne series 1901–1973, and the same method backwards to 1880–1900 (fn 29). After 1972: Abelson and Chung (1973–1985) and ABS (1986–2006). (PDF p.20)
- Four early series: Abelson (1985) Sydney 1925–1970 (fn 30: NSW Valuer-General records, ~200 lots in each of 23 local government areas; mean, median and repeat valuation index); Neutze (1972) four Sydney areas 1949–1967 (fn 31: Redfern, Randwick, Bankstown, Liverpool; low-to-medium income; sales prices; method not stated); Butlin (1964) Melbourne 1861–1890 (fn 32: advertisements in *Melbourne Age* and *Argus*; asking price in terms of rooms rather than houses, so partial quality adjustment); Fisher and Kent (1999) aggregate capital value of ratable properties, 1880s–1890s, Melbourne and Sydney. (PDF pp.20–21)
- ABS (2013) 1986–2012: quarterly indices for eight cities, (i) established detached dwellings and (ii) project homes; "mix-adjusted method"; State Valuer-General sales data supplemented by mortgage-lender loan applications (ABS 2014). Fn 33: eight cities = Sydney, Melbourne, Brisbane, Adelaide, Perth, Hobart, Darwin, Canberra; Laspeyres-type; stratified by locational, structural and neighbourhood characteristics; reviews in 2004 and 2007 changed pricing point, stratification and weights; two separate series 1986–2005 and 2002–2012 that "move, however, closely together in the years they overlap." Fn 34: unpublished Treasury index 1960–2004 (corr. 0.995 with Abelson–Chung for 1986–2003, 0.774 for 1970–1985); OECD index 1970–2012 based on ABS eight-capital index; FRB Dallas 1975–2012 splices ABS and Treasury. (PDF p.21)

**Plausibility comparisons**
- Figure 19 (PDF p.24; nominal 1870–1900, 1890=100): Butlin Melbourne, Stapledon Melbourne and Sydney, six-capital index. The six-capital index is "stagnant" 1880–1887 with a boom limited to 1888–1891 (+25%), "at odds with various accounts (Daly, 1982; Stapledon, 2012b)" — "the stagnation of the six-capital-index during most of the 1880s appears rather implausible." (PDF p.22)
- Figure 20 (PDF p.25; 1900–1970, 1960=100): Stapledon Sydney/Melbourne, Neutze, Abelson, six-capital — "almost fully correspond" (Neutze) or "very similar trend" (Abelson). Fn 36: "The only very moderate rise in nominal house prices between the beginning of the 20th century and 1950 is striking"; attributed partly to the large volume of urban land developed in the 1880s boom; price controls lifted 1949; 1960 credit squeeze. (PDF pp.22–23)
- Figure 21 (PDF p.25; 1970–2012, 1990=100): "all indices for the years from 1970–2012 follow a joint, almost identical path. It is only after 2004 that the increase in Melbourne property prices shows to be more pronounced." Fn 37: ABS series spliced in 2003; several of the series are by construction identical 1970–1985 and post-1986. (PDF p.23)

**Splicing decisions** (PDF pp.23–24): "the series constructed by Stapledon (2007) for the six capitals constitutes the basis for the long-run index. Due to the above mentioned possible deficiencies of the index for the time of the 1880s boom and subsequent contraction, the Stapledon (2012b) index for Melbourne is used for 1880–1899. Therefore, the index may be biased upward to some extent since the boom of the 1880s was particularly pronounced in Melbourne when compared to, for example, Sydney. The index is extended backwards to 1870 using the index calculated from the Melbourne series by Butlin (1964). Hence, prior to 1900, our index only refers to Melbourne. … Beginning in 2003, the index is spliced with the Australian Bureau of Statistics (2013) eight-cities-index."

**Known caveats** (PDF pp.24–25): "three weaknesses: first, prior to 1943, the index is based on asking prices. These may differ from actual transaction prices and thus result in a bias of unknown size and direction. Second, the index does not explicitly control for quality changes, i.e. depreciation or improvement. Third, only after 1986 the index controls for quality changes." Stapledon (2007) estimates improvements add 0.95% p.a. to value and changing composition subtracts 0.35% p.a. from the median; 0.55% p.a. assumed for 1914–18, 1940–45, 1891–95, 1930–35. Adjusted real growth 1870–2012: 1.68% → 1.11% p.a.; unadjusted index used.

**Table 5: Australia: sources of house price index, 1870–2012 (PDF p.26)**

| Period | ID | Source | Geographic coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1870–1880 | AUS1 | Butlin (1964) | Melbourne | All kinds of existing dwellings | Advertisements in newspapers | Median asking prices |
| 1881–1899 | AUS2 | Stapledon (2012b) | Melbourne | All kinds of existing dwellings | Advertisements in newspapers | Median asking prices |
| 1900–1942 | AUS3 | Stapledon (2007) | Six capital cities | All kinds of existing dwellings | Advertisements in newspapers and Census estimates of average rents | Median asking prices |
| 1943–1949 | AUS4 | Stapledon (2007) | Six capital cities | All kinds of existing dwellings | Estimate of the fixed price | Estimate of fixed price |
| 1950–1972 | AUS5 | Stapledon (2007) | Six capital cities | All kinds of existing dwellings | Weekly property reports in newspapers and Census estimates of average rents | Median sales prices |
| 1973–1985 | AUS6 | Abelson and Chung (2005), as used in Stapledon (2007) | Six capital cities | All kinds of existing dwellings | Land Title Offices (LTOs); Productivity Commission data; Valuer-General Offices | Weighted average of median prices |
| 1986–2002 | AUS7 | Australian Bureau of Statistics (2013) as used in Stapledon (2007) | Six capital cities | New and existing detached houses | State Valuer-General Offices, supplemented by property loan applications from major mortgage lenders | Weighted average of mix-adjusted house price indices |
| 2003–2012 | AUS8 | Australian Bureau of Statistics (2013) | Eight capital cities | New and existing detached houses | Same | Mix adjustment |

**Construction cost (PDF pp.27–28; Table 6):** Stapledon (2012a, Table 2) 1881–2012 combining Butlin (1962) 1870–1938 (Victoria; cost per room; loan applications of the Modern Permanent Building Society and County of Bourke Building Society for 1870–1890 and 1900–1939, tender prices from *Australasian Builder and Contractors' News* for the 1890s; output price index; 1870s extended with input cost indices; three-year moving average), Butlin (1977) 1939–1949 (input cost, no details), ABS (2015) 1949– (implicit price deflator for private residential construction, alterations and additions = replacement value). Table 6: 1870–1880 Butlin (1962) Victoria input cost; 1881–1900 and 1901–1939 Butlin (1962) in Stapledon (2012a) Victoria output price; 1940–1948 Butlin (1977) in Stapledon (2012a) input (no coverage info); 1949–2012 ABS (2015) in Stapledon (2012a) nationwide replacement values. Figure 22 (PDF p.28): nominal construction cost sub-indices 1881–1939.

**Land price (PDF p.29):** Stapledon (2007) 1880–2005, decennial median land prices Sydney and Melbourne 1880–1940, quinquennial 1950–2005; not adjusted for lot size; 1880–1970 newspaper advertisements, "predominantly new allotments in outer suburbs" (urban fringe); 1970–1989 BIS-Schrapnel medians; since 1990 ABS value of residential land by state (average land value per dwelling). Authors use an unweighted average of Melbourne and Sydney.

**Other (PDF p.29):** Value of housing stock: Goldsmith (1985) and Garland and Goldsmith (1959) benchmarks 1903, 1915, 1929, 1947, 1956, 1978; OECD (2013) 1988–2011; Piketty and Zucman (2014) 1959–2011. CPI: 1870–2007 Taylor (2002); 2008–2012 International Monetary Fund (2012).

---

### BELGIUM — B.3, PDF pp.30–37 (printed 29–36). Data available 1878–2012 (with a WWI gap 1914–1918 in the source table).

**Sources discussed**
- De Bruyne (1956): greater Brussels area 1878–1952; "annual median price per square meter of the interquartile range for four real estate categories: i) residential property [maisons d'habitation] in the center of Brussels, ii) maisons de rentier, iii) building sites (since 1885), and iv) commercial properties (since 1879)." Fn 38: maisons d'habitation = "houses of rather inferior quality … usually inhabited by workers or employees, small, and do not have electricity, central heating, gas or water"; fn 39: maisons de rentier = "properties that are located in a good neighborhood, have usually more than one story, are well maintained, and serve as a single-family dwelling"; fn 41: data from the *Guide de l'Expert en Immeubles* (Union des Géomètres-Experts de Bruxelles), urban parts of Brussels district (Brussels, Etterbeek, Ixelles, Molenbeek, Saint-Gilles, Saint-Josse, Schaerbeek, Koekelberg, Laeken), with separate series for more rural communes. (PDF p.30)
- Janssens and de Wael (2005): two indices, 1919–1960 and 1960–2003. 1919–1950 relies on the Antwerpsche Hypotheekkas (1961) Brussels index for maisons de rentier (median of interquartile range). 1950–1960: nationwide data on all *public* housing sales subject to registration rights (Statistics Belgium), weighted mean sales price, weights = share of national sales in each of 43 arrondissements. 1960–2003: same method but public and private sales. (PDF pp.30–31)
- Statistics Belgium (2013): since 1986 quarterly stratified indices for building lots, apartments, villas, single-family dwellings; national/regional/district/communal. Fn 42: chain Laspeyres; stratification refined 2005 (break 2004–05); "It does not control for quality changes"; OECD 1970–2012 index is based on the Bank of Belgium index which draws on Statistics Belgium; FRB Dallas 1975–2012 uses Statistics Belgium and Stadim (2013). (PDF p.31)

**Plausibility comparisons**
- Figure 23 (PDF p.32; 1878–1913, 1913=100): the four De Bruyne property-type indices; three move closely together, building sites more volatile; "nominal house prices trend downwards until the late 1880s and slowly recover afterwards", in line with macro trends (fn 43: 1880s recession, recovery mid-1890s, 1899 housing act). (PDF p.31)
- Figure 24 (PDF p.33; 1919–1960, 1919=100): De Bruyne Brussels, Janssens–de Wael Brussels, AHK Antwerp "move closely together" 1919–1952 (fn 44: corr. 0.995 for the two Brussels indices, 0.993 Antwerp vs Brussels). Leeman (1955, 67) on Brussels, Antwerp, Mechelen, Leuven, Bruges, Dinant, Lier 1914–1943: Brussels trends mirror other regions. Fn 45 narrative: 1919–22 rise from postwar housing shortage; 1930s decline; postwar growth and shortage. (PDF pp.32–33)
- 1986–2003: Janssens–de Wael and Statistics Belgium "show the same statistical characteristics" (fn 47: Stadim cooperated with Statistics Belgium; Janssens and De Wael are founding members of Stadim). (PDF p.35)

**Known caveats (PDF p.35):** "The most important limitation of the long-run series is the lack of correction for changing qualitative characteristics of and quality differences between the dwellings in the sample. To some extent the latter aspect may be less of a problem for 1878–1950 since for that period the index is confined to a certain market segment, i.e. maisons de rentier. Prior to 1950, the series is also adjusted for the size of the dwelling as it is based on price data per square meter." Possible that this segment is not representative of other residential types for 1878–1950. Crude quality adjustment: 1.96% → 1.77% p.a. real (1878–2012); unadjusted used.

**Table 7: Belgium: sources of house price index, 1878–2012 (PDF p.34)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1878–1913 | BEL1 | De Bruyne (1956) | Brussels area | Existing maisons de rentier | Guide de l'Export [sic] en Immeubles | Median sales prices |
| 1919–1950 | BEL2 | Janssens and de Wael (2005); based on Antwerpsche Hypotheekkas (1961) | Brussels area | Maisons de rentier | Antwerpsche Hypotheekkas (1961) | Median sales prices |
| 1951–1959 | BEL3 | Janssens and de Wael (2005) | Nationwide | Small & medium-sized existing houses | Transaction prices (public sales; gathered by Statistics Belgium) | Weighted average of mean sales prices |
| 1960–1985 | BEL4 | Janssens and de Wael (2005) | Nationwide | 1960–1970: small & medium-sized existing houses; 1971 onwards: all kinds of existing dwellings (villas & mansions included) | Transaction prices (public and private sales) gathered by Statistics Belgium | Weighted average of mean sales prices |
| 1986–2012 | BEL5 | Statistics Belgium (2013) | Nationwide | Existing, single-family dwellings | Transaction prices | Weighted mix-adjusted index |

Note: the table has **no entry for 1914–1918**; Table 4 reports N=119 (vs 127 possible) for Belgium.

**Construction cost (PDF pp.35–36; Table 8):** ABEX output price index (Belgian Association of Surveyors, 2013) for all types of new buildings 1914–2012, published March and November, annual = unweighted average. Comparison: Buyst (1992) real input cost indices 1890–1913, 1920–1939, 1946–1961 (materials from Buyst; wages from Scholliers 1982, *Arbeidsblad*, *Statistisch Bulletin*). Table 8: 1914–2012 Belgian Association of Surveyors (2013), nationwide, all types of buildings, output price index.

**Land price (PDF p.36):** Stadim (2013) 1953–2012, building lots per square metre, Kadaster transactions; weighted average of Flemish and Walloon regions (fn 48: transaction numbers as weights).

**Other (PDF pp.36–37):** Farmland 1980–2007 Vlaamse Overheid (series by email, Els Demuynck); 2008–2009 Bergen (2011); none for 2010–2012. Value of housing stock: Goldsmith (1985) 1950 and 1978; Poullet (2013) 2005–2011. CPI: 1870–2007 National Bank of Belgium (2012) (fn 51: "Indice des prix à la Consommation en Belgique", from Daisy Dillen); 2008–2012 IMF (2012).

---

### CANADA — B.4, PDF pp.37–46 (printed 36–45). Data available 1921–2012 (no 19th-century data).

**Sources discussed**
- "Historical data on house prices in Canada are scarce even though real estate boards were already established in the early 20th century." (PDF p.37)
- Firestone (1951) 1921–1949: "calculated using data on the average value of residential real estate (including land) and the number of existing dwellings and hence reflects the average replacement value of existing dwellings rather than prices realized in transactions." Fn 52 describes the perpetual-inventory style method (1921 construction cost per dwelling, age-adjusted, revalued annually with construction costs, depreciation, destruction, gross residential capital formation; land value from land/construction cost ratios). (PDF p.37)
- Canadian Real Estate Association (1981) 1956–1981: annual average value and number of MLS transactions "for all properties, i.e. it includes both residential and non-residential real estate." Subocz (1977): mean price index for new and existing single-family detached houses 1949–1976, Greater Vancouver (Vancouver and New Westminster Registry offices). CREA second series 1980–2012 (fn 53: by email, Gregory Klump): secondary-market residential MLS transactions, average of all sales prices. UBC Sauder (Centre for Urban Economics and Real Estate, UBC, 2013) 1975–2012: existing bungalows (fn 54: detached, one-storey, three-bedroom, ~111 m²) and two-storey executive detached houses in ten main metropolitan areas; population-weighted neighbourhood changes; weighted across housing types by share of units sold; data from the Royal LePage survey (fn 55: standardized housing types give "some degree of constant quality"). Statistics Canada (2013c) new housing price indices 1981–2012 (buildings, land, real estate), survey of contractors in 21 metropolitan areas, matched-model constant-quality. (PDF pp.37–39)

**Plausibility** (PDF pp.39–42): Firestone "is hence the only available source for house prices in Canada prior to the 1950s"; nominal index stable in 1920s, falls after Great Depression, rises after 1935 — consistent with Anderson (1992) (fn 56: 1935 Dominion Housing Act, 1937 Home Improvement Loan Guarantee Act, 1938 National Housing Act); "Overall, the trajectory of the Firestone (1951) appears plausible." Figure 25 (PDF p.40; 1956–2012, 1981=100): CREA (1981), CREA (2012), Statistics Canada new housing, UBC Sauder — all strongly positive post-1980 but magnitudes differ; CREA more pronounced because simple average (composition bias) though it covers ~70% of marketed residential properties; Statistics Canada new-house index lower because suburban. "For the years since 1975 we use the UBC Sauder index as it is confined to a certain market segment … and thus should be less prone to composition bias than the CREA series." Fn 57: CREA appears stagnant 1975–1980 unlike UBC/StatCan, so UBC Sauder used also for 1975–1980. Figure 26 (PDF p.42; 1949–1981, 1971=100): Subocz vs CREA; Subocz "appears more consistent with narratives by Clayton and Miron (1987) and Poterba (1991) for the period 1949–1976" but "relies only on a rather small sample size and is confined to property sales in the Greater Vancouver area" and reports "an astonishing 280 percent" real increase 1956–1974 vs CREA's ~87%; "Therefore, despite its potential weaknesses, we rely on the CREA index."

**Splicing** (PDF p.42): "Data on residential house prices is available for 1921–1949 and for 1956 onwards. For 1921–1949, the series on average value of existing farm and existing non-farm dwellings including land are highly correlated (Firestone, 1951, Tables 69 & 80) [fn 60: 0.856]. Since no data on residential house prices is available for 1949–1956, we use the percentage change in the value of farm real estate per acre to link the 1921–1949 and the 1956–1974 series (Buckley and Urquhart, 1965)."

**Known caveats** (PDF pp.42–43): "three drawbacks: first, data prior to 1949 is not based on actual list or transaction prices but calculated as the average replacement value of existing dwellings including land value … This approach may result in a bias of unknown size and direction. Second, for 1956–1974, the index refers to both residential and non-residential real estate and is not adjusted for compositional changes. Third, the index is not adjusted for quality improvements for the years after 1956. The bias should be mitigated for the post-1975 years due to the way the Royal LePage survey is set up." Crude adjustment for 1956–1974: 2.21% → 1.67% p.a. real (1921–2012); unadjusted used.

**Table 9: Canada: sources of house price index, 1921–2012 (PDF p.45)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1921–1949 | CAN1 | Firestone (1951) | Nationwide | All kinds of existing dwellings (farm and non-farm) | Estimates of the value of residential structures and the value of residential land as well as data on all available residential dwellings | Average replacement values |
| 1949–1956 | — | Buckley and Urquhart (1965) | Nationwide | Farm real estate | — | Value of farm real estate per acre |
| 1956–1974 | CAN2 | Canadian Real Estate Association (1981) | Nationwide | All kinds of real estate (residential and non-residential) | Transactions registered in the MLS system | Average sales prices |
| 1975–2012 | CAN3 | Centre for Urban Economics and Real Estate, University of British Columbia (2013) | Five cities [as printed; the text on PDF p.38 says "ten main metropolitan areas"] | Existing bungalows and two story executive dwellings | Royal LePage real estate experts | Average prices |

**Construction cost (PDF pp.43–45; Table 10):** Urquhart (1993) 1870–1921 input cost (building materials index: unweighted average of Rymes 1967 materials index and Statistics Canada 1983 K38 wood products; wage index weighted; weights wages 0.387 / materials 0.613); Firestone (1951) 1921–1949 input cost (Dominion Bureau of Statistics wholesale house-building materials + Department of Labor building-trade wage rates; 1946 survey weights); Statistics Canada (1983, S327, K136) 1926–1976 input cost for new residential construction, continued to 1985 (fn 61 weights wages 0.359 / materials 0.641); Statistics Canada (2013b) 1986–2012 output price index for apartment buildings in seven metropolitan areas (fn 62: Halifax, Montréal, Toronto, Calgary, Edmonton, Vancouver, Ontario), index house = 1981 concrete apartment block of 53 units. Table 10: 1870–1920 Urquhart nationwide input; 1921–1925 Firestone nationwide single-family input; 1926–1985 Statistics Canada urban single-family input; 1986–2012 Statistics Canada (2013b) metropolitan apartment output. Real unit labour costs 1950–1970 (Statistics Canada 2014): +33%.

**Other (PDF pp.44–46):** Farmland 1901–1956 Buckley and Urquhart (1965); 1965–2009 Manitoba Agriculture, Food and Rural Initiatives (2010); 2010–2011 Province of Manitoba (2012). Value of housing stock: Goldsmith (1985) 1950, 1978; OECD (2013) 1970–2011; Piketty and Zucman (2014) benchmarks 1895–1955. CPI: 1870–2007 Taylor (2002); 2008–2012 IMF (2012).

---

### DENMARK — B.5, PDF pp.46–52 (printed 45–51). Data available 1875–2012.

**Sources discussed**
- Abildgren (2006): single-family house index 1938–2005 (annual average sales prices; Økonomiministeret 1966 for 1938–1965; Danmarks Nationalbank; Statistics Denmark 1966–2005) and farm index 1875–2005 ("sales price per unit of land valuation based on estimated productivity" — fn 64: per barrel of *hartkorn* — for 1875–1959; average sales prices per farm 1960–2005; fn 65: all farms 1960–67, 10–100 ha 1968–75, 15–60 ha 1976–2005). Fn 63: Økonomiministeret (1966) five areas (Copenhagen & Frederiksberg; provincial towns; Copenhagen area; towns >1500; rural); until 1950 properties valued ≤ 20,000 DKK, from 1951 one-apartment properties — "the break in the series may cause an upward bias for 1950–1951." (PDF p.46)
- Danmarks Nationalbank (2003; fn 66 series by email, Tina Saaby Hvolbøl): quarterly SPAR series for new and existing single-family dwellings since 1971, data from the Ministry of Taxation (SKAT). Statistics Denmark (2013): nationwide SPAR index for single-family houses and multifamily types, 1992–2012. (PDF p.47)

**Plausibility** (PDF pp.47–48): Figure 27 (PDF p.48; 1938–2005, 1995=100): farm and house indices "strongly correlated" (fn 67: 0.996). Kristensen (2007, 12): ~50% of the population rural at end of WWII, so farm property "may be used as a proxy for Danish house prices prior to 1938. Nevertheless, the series for 1875–1937 must be treated with caution" — fn 68: the 1895–1907 Copenhagen building boom/bubble and 1907 crisis are *not* reflected in the farm index. Figure 28 (PDF p.49; 1938–1965, 1938=100): urban vs rural single-family prices similar until the 1960s, when urban grows faster. Correlations: Abildgren vs Statistics Denmark 0.971 (1992–2010); Statistics Denmark vs Nationalbank 0.999 (1992–2012); Abildgren vs Nationalbank 0.999 (1971–2005).

**Splicing** (PDF p.48): "To keep the number of data sources to construct an aggregate index to the minimum, the here composed long-run index relies on Danmarks Nationalbanken index for the period since 1971."

**Known caveats** (PDF pp.48–49): "two weaknesses: first, the series used for 1875–1938 only reflects the price development of farm property which may deviate to some extent from price developments of other residential properties. Second, the series used for 1875–1970 is adjusted neither for compositional changes nor for quality changes." Quality effect from Laursen and Madsen (2013): 0.99% → 0.57% p.a. real (1875–2012); unadjusted used.

**Table 11: Denmark: sources of house price index, 1875–2012 (PDF p.50)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1875–1938 | DNK1 | Abildgren (2006) | Nationwide | Existing farms | Data from various sources (see text) | Average prices |
| 1939–1971 | DNK2 | Abildgren (2006) | Nationwide | Existing single-family houses | Data drawn from various sources (see text) | Average prices |
| 1972–2012 | DNK3 | Danmarks Nationalbank | Nationwide | New and existing single-family houses | Ministry of Taxation (SKAT) | SPAR method |

**Construction cost (PDF pp.49–51; Table 12):** Statistics Denmark input cost index for small farms (fn 71: 3 rooms, kitchen, laundry, stable; redefined 1926, 1959) from 1920 (Statistics Copenhagen 1937), covering 1914–1970; apartment houses 1940–1970 (fn 72: three-storey, 6 staircases, 36 apartments); from 1969 one-family houses, apartments, aggregate (Statistics Denmark 2015). Correlations: farms vs apartments 0.98 (1939–55); apartments vs one-family 0.99 (1986–2012). Table 12: 1914–1939 rural small farms input; 1940–1968 nationwide apartment houses input; 1969–2012 nationwide single-family input. Figure 29 (PDF p.51).

**Other (PDF p.52):** Farmland 1875–2005 Abildgren (2006); 1870–1912 O'Rourke, Taylor and Williamson (1996). Value of housing stock: Goldsmith (1985) 1880, 1900, 1913, 1929, 1938, 1948, 1960, 1965, 1973, 1978. CPI: 1870–2007 Taylor (2002); 2008–2012 IMF (2012).

---

### FINLAND — B.6, PDF pp.52–59 (printed 51–58). Data available 1905–2012 (nothing for 1870–1904).

**Sources discussed**
- Statistical Office of the City of Helsinki (various years) 1904–1962: "average annual prices of building sites for dwellings per square meter offered for sale by the city of Helsinki." The authors "construct a three-year-average price index for residential building sites for 1905–1961 to smooth out some of the year-to-year fluctuations stemming from variation in the number of transactions." (PDF p.52)
- Leväinen (1991, 39): building-site price index 1909–1989, sites for detached and terraced houses in Southern Finland/Helsinki (fn 75: chain index of ratios of successive years; simple average where several sources); updated Leväinen (2013) to 1910–2011 (1989–2011 from National Land Survey). (PDF pp.52–53)
- Statistics Finland 1985–2012: nationwide index for existing single-family dwellings and plots, "combination of hedonic regression and a mix-adjusted method" (fn 76: stratified by type, rooms, location; hedonic per stratum; weighted by dwelling stock value; Saarnio 2006), from the National Land Survey real estate register; second index for dwellings in housing companies (blocks of flats and terraced houses) from asset-transfer-tax statements (Statistics Finland 2011; fn 77: formerly "Prices of Dwellings"). Also average prices per m² of dwellings in "old" blocks of flats (fn 78: built before the statistics year and the year before) in the centre of Helsinki 1947–2012, and for greater Helsinki (fn 79: Helsinki, Espoo, Vantaa, Kauniainen; by email, Petri Kettunen) and whole country 1970–2012 (fn 80: Helsinki centre "quite well represents" Finnish prices before 1970; afterwards Helsinki rose faster). Pre-1987 from real estate agencies, since 1987 tax statements (fn 81: structural break 1986–87, also methodological — from fixed-weighted Laspeyres unit value to hedonic/mix-adjusted; FRB Dallas splices 1975–2012 from flats 1975–85 and single-family 1985–2012). (PDF p.53)

**Plausibility** (PDF pp.54–55): Figure 30 (PDF p.55; 1905–1945, 1920=100): HSY vs Leväinen. Both show booms peaking ~1910 and in the 1920s, but for the 1920s "a disjoint and inconsistent picture": Leväinen >10× real trough-to-peak 1920–1931 vs HSY 7× 1921–1929; Leväinen keeps rising through the Depression and early WWII, HSY falls ~20% 1929–33, recovers ~1936, collapses in WWII. Construction peaked 1937/38, so "a continued increase in site prices until 1942 … appearing unreasonable. Therefore, the empirical analysis undertaken here relies on the HSY-index for the period prior to 1947." Both cover only the Helsinki area. Site prices as proxy for house prices: old blocks of flats (Helsinki centre) 1947–2012 vs Leväinen site index corr. 0.96 (fn 82). Figure 31 (PDF p.56; 1945–2012, 1990=100): all indices show boom peaking early 1970s, late-1980s boom, early-1990s bust, rise from mid-1990s; "For the sake of coherence with respect to property types, the long-run index uses the data for old blocks of apartments also for the post-1970 period"; Helsinki centre overstates the 1990s/2000s boom, "Hence, for the years since 1970 we use the nationwide series for old blocks of flats."

**Known caveats** (PDF p.56): "the long-run index controls for quality changes only after 1970. For 1905–1947, the index refers to building sites and should not be diluted by unobserved changes in quality. In contrast, since for 1947–1969 the index is only based on simple average prices, it may be biased due to quality changes in the structures that are not controlled for. Since the series is restricted to one very specific market segment (i.e. existing apartments in the center of Helsinki), compositional bias should not play a major role."

**Table 13: Finland: sources of house price index, 1905–2012 (PDF p.57)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1905–1946 | FIN1 | Statistical Office of the City of Helsinki (various years) | Helsinki | Residential building sites | Sales prices | Three year moving average of average prices |
| 1947–1969 | FIN2 | Statistics Finland | Center of Helsinki | Dwellings in existing blocks of flats | Data from Statistics Finland | Average prices |
| 1970–2012 | FIN3 | Statistics Finland (2011) | Nationwide | Dwellings in existing blocks of flats | Data from Statistics Finland | Hedonic mix-adjusted method |

**Construction cost (PDF pp.58–59; Table 14):** Hjerppe (1989, Appendix Table 13) 1870–1984, built from Heikkonen (1971) 1870–1934 (input cost: construction wages + timber, stone, metal; Bank of Finland weights for Helsinki apartment houses), Bank of Finland 1935–1955 (apartment houses Helsinki; input cost incl. architect fees and contractors' overhead/profit at 10% — fns 83–84), Statistics Finland 1955–1984 (apartment buildings; wages from collective agreements, >50 materials; reweighted every 5–10 years), extended to 2012. Table 14: 1870–1934 Heikkonen in Hjerppe, Helsinki apartment buildings input; 1935–1955 Bank of Finland (1946, 1952, 1955) Helsinki apartment input; 1956–2012 Statistics Finland nationwide apartment input. Real unit labour costs 1950–1970 (Hjerppe 1989): real construction costs and ULC "decreased by a little more 7 percent."

**Other (PDF p.59):** Farmland 1985–2012 National Land Survey of Finland (by email, Juhani Väänänen), median transaction price per hectare. CPI: 1870–1996 Taylor (2002); 1997–2012 IMF (2012).

---

### FRANCE — B.7, PDF pp.59–65 (printed 58–64). Data available 1870–2012.

**Sources discussed**
- Conseil Général de l'Environnement et du Développement Durable (2016, CGEDD): national repeat-sales index for all categories of existing dwellings (apartments and single-family houses) 1936–2013; pre-1999 from two notarial databases (fn 88: BIEN base of the Chambre Interdépartementale des Notaires de Paris for the Paris region; Perval France base for the provinces; see Beauvois et al. 2005); databases established in the 1980s but include earlier transactions (Friggit 2002); post-1999 spliced with the INSEE mix-adjusted hedonic index. (PDF pp.59–60)
- CGEDD Paris index (extended back to 1200): for 1870–2012 three parts: 1840–1944 Duon (1946) repeat-sales index from Tax Department property registers, covering apartment buildings (commercial, single-family and apartments sold by the unit excluded; fn 89: apartments could not be sold by the unit before WWI); 1944–1999 CGEDD repeat sales of apartments sold by the unit from notaries (raw data only 1950–1999; "the gap … 1945–1949, has been filled applying simple linear interpolation (Friggit, 2002)"); post-1999 INSEE existing apartments in Paris. (PDF p.60)
- INSEE (National Institute of Statistics and Economic Studies, 2012): since 1996 mix-adjusted hedonic nationwide index with sub-indices for detached houses and apartments, regional sub-indices (fn 90: FRB Dallas splices CGEDD 1975–1995 and INSEE 1996–2012). (PDF p.60)

**Plausibility** (PDF pp.61–63): Figure 32 (PDF p.62; 1936–2012, 1990=100): "throughout the years 1936–1976 the Paris index is in cadence with the CGEDD France and the INSEE national indices. Considering also the broad macroeconomic trends prior to 1936 and narrative evidence … the Paris index may serve as a fairly reliable measure for the trends in national house prices." But: Paris prices "may for some years not be a reliable proxy" (fn 92: Paris index refers only to apartment buildings; ~3.3% of Paris houses owner-occupied pre-WWI); Friggit: Paris real prices more devalued in WWI than elsewhere (fn 93: wartime rent controls, alternately relaxed/tightened interwar); "also the national index for the time prior to 1950 can only serve as a rough estimate"; possible upward bias in the 1950s because share of vacant (higher-priced) properties sold rose. Paris below national 1976–1986, then above to 1991 (regional boom/bust); 1996–2012 INSEE and CGEDD nearly identical. Fn 91: long narrative of 1870s–1920s (Franco-Prussian war, 1876–1882 boom, 1882 Union Générale crash, stagnation to 1906, WWI rent controls, mid-1920s recovery).

**Splicing / caveats** (PDF p.63): "The long-run index has two major drawbacks: First, as no house price series for France as a whole is available for the years prior to 1936, we rely on the CGEDD Paris index instead. Second, despite the fact that by using the repeat sales method the effect of quality differences between houses is somewhat reduced, it does not control for all potential changes in the quality and standards of dwellings over time."

**Table 15: France: sources of house price index, 1870–2012 (PDF p.65)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1870–1935 | FRA1 | Conseil Général de l'Environnement et du Développement Durable (2016) | Paris | Apartment buildings | Data from property registers of the Tax Department | Repeat sales method |
| 1936–1996 | FRA2 | Conseil Général de l'Environnement et du Développement Durable (2016) | Nationwide | All types of existing dwellings | Notarial database | Repeat sales method |
| 1997–2012 | FRA3 | National Institute of Statistics and Economic Studies (2012) | Nationwide | All types of existing dwellings | — | Hedonic, mix-adjusted index |

**Construction cost (PDF pp.63–65; Table 16):** CGEDD (2016) input cost index originally by the Société Centrale des Architectes (fn 94: renamed Académie d'Architecture 1953), apartment buildings, Paris region, 1914–1953 (Duon 1946; Guet 1969); Fédération Française du Bâtiment (2015) input cost for Paris apartments since 1942; Statistics France (2015b) output price index for all residential dwellings (excl. public housing) since 1953 (fn 95: corr. 0.99 with FFB 1953–2012 but FFB rises more; Figure 33, PDF p.64). Table 16: 1914–1953 CGEDD Paris region apartment houses input; 1954–2012 Statistics France (2015b) nationwide all residential output. Real unit labour costs 1950–1970 (OECD 2016): +19%.

**Other (PDF p.64):** Value of housing stock: Goldsmith (1985) 1880, 1913, 1929, 1950, 1960, 1972, 1977; OECD (2013) 1978–2011; Piketty and Zucman (2014) 1870–1954 and 1970–2011. CPI: 1870–1965 Mitchell (2013); 1966–2012 IMF (2015).

---

### GERMANY — B.8, PDF pp.66–75 (printed 65–74). Data available 1870–1938 and 1962–2012 (gap 1939–1961 bridged by one survey-based growth estimate).

**Sources discussed**
- Statistics Berlin (various years): transactions of developed lots (lots including structures) in Berlin 1870–1918 (fn 96: number of lots and total value; no data for 1911 and 1914). Annual index from average transaction prices; "impossible to control for size, number of structures erected on the lot, and type or use of buildings." (PDF p.66)
- Matti (1963): developed lots in Hamburg 1903–1935 (number, average sales price per m²; fn 97: 1923 and 1924 missing — hyperinflation); size of lot controlled; also 1955–1962 lot price index for Hamburg. (PDF p.66)
- Statistical Yearbooks of German Cities / Municipalities (Association of German Municipal Statisticians): developed lots 1924–1935 and building sites 1935–1939 (number, total size, total value; public and private; no type/use). Fn 100: Wagemann (1935) index for "representative cities" 1925–1935. (PDF p.66)
- Federal Statistical Office of Germany (various years, b): average building-site sales prices per m² since 1962 (fn 101: West Germany before 1991); since 2000 hedonic index for new owner-occupied dwellings (Dechent 2006b) and Expert Committee-based indices (Dechent and Ritzheim 2012). (PDF p.67)
- Deutsche Bundesbank (2014): (i) 100 West + 25 East agglomerations >100,000 since 1995, six building-type indices (all existing, all new, existing terraced [fn 103: ~100 m²], new terraced, existing flats, new flats), BulwienGesa AG data (fn 105: real-estate agents, chambers, building societies, surveys, advertisements, mystery shopping), population weights; "do not control for quality differences between houses or quality changes over time but only cover properties that provide 'comfortable living conditions' and are located in 'average to good locations'"; (ii) West-German agglomerations 1975–2012 (50 towns 1975–89, 100 since 1990): all new dwellings, new terraced houses, new flats, building sites for detached single-family (fn 107: flats/sites per m², others per dwelling); new terraced extended back to 1970 (OECD; fn 108: Mack and Martínez-García note it may include existing dwellings). (PDF pp.67–68)

**Plausibility** (PDF pp.68–71): Figure 34 (PDF p.70; 1870–1935, 1903=100): Berlin (points) and Hamburg; Berlin is the only series 1870–1903, "accords with narrative and scattered quantitative evidence on other German housing markets" (Carthaus 1917; Führer 1995; Rothkegel 1920; Ensgraber 1913). WWI/hyperinflation: nominal prices rise but "significantly lag inflation"; real collapse explained by rent controls (fn 110: Teuteberg 1992), negative returns, foreign buyers; *Wall Street Journal* (1921): "an apartment house valued at $100,000 before the war can be bought for $5,000"; *New York Times* (1923); WSJ (1927): apartment-house prices "but 25 percent to 40 percent of pre-war at the beginning of 1926." Figure 35 (PDF p.71; 1924–1938, 1925=100): 10-city weighted index (fn 111: transaction numbers as weights) vs Matti Hamburg, "far away from perfect lockstep" but same trend (fn 112: corr. 0.73); lot prices peak 1928 (Hamburg) / 1929 (10 cities), recover from 1936. Building-site prices (Federal Statistical Office) vs Bundesbank new terraced 1970–1991: corr. 0.992 (fn 114) → "prices for building land may serve a good approximation for house prices prior to 1970."

**Splicing** (PDF pp.71–73): "For 1870–1902 we use the index for Berlin but rely on the index for Hamburg for 1903–1923 mainly for two reasons: first, in contrast to the Berlin index, the Hamburg index controls for the size of the lots sold … Second, the boom in Berlin between 1902 and 1906 was stronger and the recession preceding World War I started earlier than in most other German urban housing markets (Carthaus, 1917). For 1924–1938 we use the index for 10 cities due to its wider geographical coverage. Unfortunately, price data for houses or building lots to the authors knowledge is not available for the period 1939–1954 such that a complete index for house prices can only be constructed for the period since 1955." Matti's Hamburg 1955–1962 index "reports a quintupling of prices" — "must be considered to either have been specific to the city of Hamburg or to have resulted from measurement errors. Accordingly, the index by Matti (1963) is not used … the here constructed index only starts in 1962 and for the period from 1962 to 1970 relies on price data of building sites per square meter [fn 115: actual coverage 1962–2012]. To obtain our long-run index, we link the two sub-indices, i.e. 1870–1938 and 1962–2012, assuming an average increase in prices of building sites of 300 percent based on the results of a survey conducted by Deutsches Volksheimstättenwerk (1959)." Justification: Wirtschaftswunder; 1936 building-site price controls fully abolished only in the 1960 Bundesbaugesetz (sites already at 250–300% of the 1936 ceiling in 1959; *DER SPIEGEL* 1961; Koch 1961); rent control largely abolished by 1965. "For the time since 1971, we use the urban index for new terraced dwellings produced by the German Central Bank (as reported by Bank for International Settlements (2013))."

**Known caveats** (PDF p.73): "three flaws: First, while the Hamburg and Berlin indices appear to well reflect the developments in housing markets as discussed in the literature, it – due to the limited availability of property price data – remains uncertain to what extent they can be considered a fully reliable image of the national trend. A second limitation of the index prior to 1938 remains the lack of correction for changing structural characteristics of and quality differences between the developed lots as well as quality change in the structures built on these lots over time. Third, for 1970–2012, the extent to which the effect of quality differences are indeed reduced through confining the index to a certain market segment remains difficult to determine."

**Table 17: Germany: sources of house price index, 1870–2012 (PDF p.75)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1870–1902 | DEU1 | Statistics Berlin (various years) | Berlin | All kinds of existing dwellings | Sales prices collected by Statistics Berlin | Average transaction prices |
| 1903–1923 | DEU2 | Matti (1963) | Hamburg | All kinds of existing dwellings | Sales prices collected by Statistics Hamburg | Average transaction prices |
| 1924–1938 | DEU3 | Association of German Municipal Statisticians (various years) | Ten cities | All kinds of existing dwellings | Sales prices collected by the city's statistical offices | Weighted average transaction price index |
| 1939–1961 | — | Deutsches Volksheimstättenwerk (1959) | Western Germany | Building sites | Data collected through survey | Estimated increase in sales prices |
| 1962–1970 | DEU4 | Federal Statistical Office of Germany (various years, b) | Western Germany | Building sites | Sales prices collected by the Federal Statistical Office of Germany | Average sales prices |
| 1971–1995 | DEU5 | Bundesbank as reported by OECD | Urban areas in Western Germany | New terraced homes | Various data sources collected by BulwienGesa | Weighted average sales price index |
| 1995–2012 | DEU6 | Bundesbank as reported by OECD | Urban areas in Western Germany | New and existing terraced homes | Various data sources assembled by BulwienGesa | Weighted average sales price index |

(Note: Table 17 gives DEU5 as 1971–1995 and DEU6 as 1995–2012, overlapping in 1995, as printed. Table 4 reports N=110 for Germany, with only 50 post-WWII observations, consistent with the index resuming in 1962.)

**Construction cost (PDF pp.73–75; Table 18):** Federal Statistical Office (2012) monthly construction cost report 1913–2012, input cost 1913–1958, output price thereafter (Horstmann 1959); fn 116 territory: German Reich 1913–44, former federal territory excl. Berlin and Saarland 1945–59, excl. Berlin 1960–65, former federal territory 1966–90, Germany since 1991; "unlikely to bias the index given the high level of standardization" (Vorholt 1995). Also output price index for prefabricated one-family dwellings since 1968; input cost index since 2000 (Dechent 2006b). Table 18: 1914–1958 nationwide all residential input; 1959–2012 nationwide all residential output. Real unit labour costs 1950–1970 (Federal Statistical Office 1991): +59%.

**Other (PDF p.74):** Farmland 1961–2012 Federal Statistical Office (various years, a, v). Value of housing stock: Goldsmith (1985) 1875, 1913, 1929, 1950, 1978; OECD (2013) 1991–2011; Piketty and Zucman (2014) 1870–2011. CPI: 1870–1996 Taylor (2002); 1997–2012 IMF (2012).

---

### JAPAN — B.9, PDF pp.76–82 (printed 75–81). Data available 1881–2012, but the long-run index **starts only in 1913** and is a **residential land-price** index throughout (no structures).

**Sources discussed**
- Bank of Japan, Statistics Department (1970a): prices of rural residential land (Yen/10 are) for selected years 1880–1915, Tokyo prefecture and national average; from public surveys for land-taxation assessments (Teikoku Statistics Annual); structural break 1913 attributed to the 1910 Residential Land Price Revision Law. (PDF p.76)
- Bank of Japan (1986a): urban land price index for six cities (fn 117: Tokyo, Kyoto, Osaka, Yokohama, Kobe, Nagoya) 1913–1930; paddy-field index 1897–1942. (PDF p.76)
- Bank of Japan (1986b): 1936–1965 urban average / commercial / residential / industrial land indices for all cities and six largest; paddy-field prices 1913–1965 for eleven districts (owner-operated farmland transactions; land assessors' surveys; BoJ 1970b). (PDF pp.76–77)
- Japan Real Estate Institute urban land price indices 1955–2004 and 1969–2012 (Statistics Japan 2012, 2013), by use (commercial, residential, industrial, average) and location (nationwide = 233 cities; six largest; nationwide excl. six largest); "Data for index calculation is drawn from appraisals." (PDF p.77)
- MLIT Land Appraisal Committee (Ministry of Land, Infrastructure, Transport and Tourism, Land and Water Bureau, 2009): 1974–2009 annual growth rates of appraised prices for "standard" commercial and residential properties, five geographic sub-series. (PDF p.77)

**Plausibility** (PDF pp.77–79): Figure 36 (PDF p.78; 1880–1942, 1915=100): the rural residential index "suggests that land prices continuously decreased between 1881 and 1913. The Meiji-era (1868–1912), however, was a time of considerable economic growth which makes the decrease in land values seem rather surprising." Two explanations: poor data quality (assessed, not sales, values; taxable amounts not adjusted — fn 118: email with Makoto Kasuya) and rural coverage during urbanization. "Since the land price trend as suggested by Bank of Japan, Statistics Department (1970a) seems partially implausible considering the economic environment, our long-run index for Japan only starts in 1913." BoJ (1986b) and Statistics Japan nationwide urban residential indices are "perfect substitutes" 1955–1965 (fn 119: corr. 0.998). Figure 37 (PDF p.79; 1974–2012, 1990=100): MLIT and Statistics Japan follow the same trend 1975–2009.

**Splicing** (PDF p.79): "No data for urban residential land prices, however, is available for 1931–1935 [fn 120: Nanjo (2002) estimates urban land prices fell >20% in 1931, stable 1932–1933]. The paddy field index and the urban residential land index, however, are strongly correlated for the years they overlap [fn 121: 0.778 for 1913–1930; 0.934 for 1936–1965]. To obtain our long-run index we thus link the two sub-indices, i.e. 1913–1930 and 1936–2012 using the growth rate of the paddy field index 1930–1936. For 1936–1954 we rely on the urban land price index for all cities by Bank of Japan (1986b). The long-run index uses the Statistics Japan (2013, 2012) index for the whole 1955–2012 period for two reasons: first, the index produced by Statistics Japan (2012) reflects appraised values rather than actual sales prices. Hence, the Statistics Japan (2013, 2012) may better reflect real price trends. Second, to keep the number of data sources … to the minimum, we do not use the [MLIT] (2009) for the post-1970 period."

**Known caveats** (PDF pp.79–80): "Three aspects have to be considered when using the series on urban residential sites. First, the index only refers to sites for residential use, and thus does not include the value of the structures. However, … particularly in urban areas the land price constitutes a large share of the overall real estate value. Fluctuations in property prices in such densely populated areas are often driven by changes in site prices (Möckel, 2007, 142). Second, Nakamura and Saita (2007) suggest that the land price series … may actually underestimate the general development in site prices. Both indices are calculated as simple averages thus assigning the same weight to high priced plots and low priced lots … Simple averages may hence underestimate the magnitude of these movements. Third, for 1936–1954, the index reflects appraised land values which may deviate from actual sales prices."

**Table 19: Japan: sources of house price index, 1880–2012 (PDF p.82)** (title says 1880 although the index starts 1913)

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1913–1930 | JPN1 | Bank of Japan (1986a) | Tokyo [as printed; text says six cities] | Urban residential land | — | Average price index |
| 1931–1935 | — | Bank of Japan (1986b) | Kanto district | Paddy fields | Transaction data obtained through surveys | Average price index |
| 1936–1954 | JPN2 | Statistics Japan (2012) [as printed; text on PDF p.79 says Bank of Japan (1986b) urban land index for all cities] | Urban areas | Residential land | Appraisal of land value as if vacant | Average price index |
| 1955–2012 | JPN3 | Statistics Japan (2013) | Urban areas | Residential land | Appraisal of land value as if vacant | Average price index |

**Construction cost (PDF pp.80–82; Table 20):** Statistics Japan (2012): construction costs of wooden houses in 46 cities 1938–2004 (fn 122: all prefectural capitals except Naha; 1938–1954 from Toyo Keizai Shinposha 1991), Japan Real Estate Institute surveys of per-m² market value of medium-quality wooden-frame houses (building only) = replacement values. MLIT (2015): construction cost deflator 1960–2006 with residential sub-indices, input cost, Greater Tokyo 1960–1990 then 10 cities. Long-run: MLIT 1960–2012 and Statistics Japan 1955–1959 (fn 123: corr. 0.99). Table 20 as printed: 1955–1959 Statistics Japan (2012) urban wooden houses replacement costs; **1981–2012** MLIT (2015) urban all residential input cost (the table's start year 1981 conflicts with the text's 1960; as printed).

**Other (PDF p.81):** Farmland 1880–1954 Bank of Japan, Statistics Department (1966) paddy fields; 1955–2012 Statistics Japan (2012, 2013) paddy fields. Value of housing stock: Goldsmith (1985) 1885, 1900, 1913, 1930, 1940, 1955, 1965, 1970, 1977; Statistics Bureau, Ministry of Internal Affairs and Communications (2013) 1954–1998; OECD (2013) 2001–2011. CPI: 1870–2000 van Leeuwen (2004); 2001–2012 IMF (2012).

---

### THE NETHERLANDS — B.10, PDF pp.83–88 (printed 82–87). Data available 1870–2012.

**Sources discussed**
- Eichholtz (1997): Herengracht, Amsterdam, "biannual hedonic repeat sales index for the period 1628–1973" from transaction data for ~200 buildings (fn 124: constant high quality, homogeneous; only one hedonic variable — use of the building; many converted to offices in the 20th century; data from *Vier eeuwen Herengracht*, Amsterdam's 750th anniversary, 1975). "To obtain an annual index we apply linear interpolation." (PDF pp.83–84)
- Kadaster index 1970–1994 for all existing dwellings (not directly available; in FRB Dallas (Mack and Martínez-García 2011) and OECD databases; fn 125: original only since 1976, OECD backcast 1970–2012): 1970–1992 median sales price from the Dutch Association of Real Estate Agents (NVM); since 1992 Land Registry sales prices, repeat sales (De Haan, van der Wal and de Vries 2008). (PDF p.83)
- Statistics Netherlands (CBS): since 1995 monthly SPAR indices for several property types, from Kadaster sales prices and municipal property-tax appraisals. (PDF pp.83–84)

**Plausibility** (PDF pp.84–85): "Even though the index only refers to real estate on one street in the city of Amsterdam (Herengracht), the series appears to be in line with the general trends in house prices as discussed in the literature (Elsinga 2003; Van Zanden 1997; Van Zanden and van Riel 2000; Van der Heijden, Visscher and Meijer 2006; Vandevyvere and Zenthöfer 2012; Van der Schaar 1987; De Vries 1980)." Fn 126 narrative: real prices +~70% 1870–1886; construction boom 1866–1886; second boom to 1907 crisis; 1901 housing law; stable 1914–1918; "long stagnation" 1929–1949; real prices −30% 1930–1936; WWII; postwar shortage; rent controls until end of 1950s; liberalization from 1959. Figure 38 (PDF p.85; 1970–2012, 1995=100): Kadaster/OECD, CBS all dwellings, CBS single-family — "perfect substitutes" 1995–2012.

**Known caveats** (PDF p.85): "two weaknesses: first, as no house price series for the Netherlands as a whole is available for the years prior to 1970, we rely on the Herengracht index instead. The extent to which house prices at the Herengracht are representative of house prices in other urban areas or the Netherlands as a whole remains, however, difficult to determine. Second, despite the fact that by using the repeat sales method the effect of quality differences between houses is somewhat reduced, it does not control for all potential changes in the quality and standards of dwellings over time."

**Table 21: The Netherlands: sources of house price index, 1870–2012 (PDF p.88)**

| Period | ID | Source | Coverage | Dwelling type | Data | Method |
|---|---|---|---|---|---|---|
| 1870–1969 | NLD1 | Eichholtz (1997) | Amsterdam | All types of existing dwellings | Sales prices published in *Vier eeuwen Herengracht* | Hedonic repeat sales method |
| 1970–1994 | NLD2 | Kadaster Index, as published by OECD | Nationwide | All types of existing dwellings | Nederlandse Vereniging van Makelaars, Kadaster | 1970–1991: median sales price; 1992–1994: repeat sales method |
| 1997–2012 | NLD3 | Statistics Netherlands (CBS) | Nationwide | All types of existing dwellings | Kadaster, officially appraised values determined by municipalities as basis for the residential property tax | SPAR method |

(As printed, the table leaves **1995–1996 unassigned** — NLD2 ends 1994 and NLD3 starts 1997 — although the text says CBS indices exist since 1995 and the three series are identical 1995–2012.)

**Construction cost (PDF pp.85–88; Table 22):** CBS output price index for new dwellings since 1914: 1914–1999 council houses (fn 127: public rental housing by municipalities) incl. VAT, hedonically quality-adjusted; since 1995 all dwelling types (incl./excl. VAT versions). BDB (Bureau Documentatie Bouwwezen; fn 128: by email, Marjan Peppelmann) input cost index single-family houses 1914–2012. CBS input cost index since 1995 (fn 129: eight representative projects from 1998; fn 130: corr. 0.91 with output index). Figure 39 (PDF p.87). Table 22: 1914–1994 CBS nationwide council houses output; 1995–2012 CBS nationwide all dwellings output (incl. VAT).

**Other (PDF p.87):** Farmland 1963–1989 and 1990–2001 CBS sales price index for farmland (without lease). Value of housing stock: CBS 1952; OECD (2013) 1996–2011. CPI: 1870–2007 Taylor (2002); 2008–2012 IMF (2012).

---

### NORWAY — B.11, PDF pp.89–90 (printed 88–89), **section continues beyond page 90**. Data available 1870–2012.

**Sources discussed (within range)**
- Eitrheim and Erlandsen (2004): five house price indices — inner city of Oslo, Bergen, Trondheim (data only since 1897), Kristiansand, and an aggregate — covering 1819–2003. "For the years 1819–1985 the indices are computed from nominal transaction prices of real estate property (mostly residential). The data has been compiled from real property registers of the four cities and refers to property in city centers. The four city indices are computed using the weighted repeat sales method, for the aggregate index the hedonic repeat sales method is applied. However, the hedonic regression only controls for location (Eitrheim and Erlandsen, 2004, 358 ff.)." For years since 1986 they use the monthly NEF/EFF index (Norges Eiendomsmeglerforbund 2012, with EFF, Finn.no and Pöyry): 1986–2001 voluntarily reported sales by NEF members, since 2002 all transactions by NEF/EFF agents; prices per m²; sub-series for all residential, detached, semi-detached, apartments; county level; hedonic controlling location and square metres (Eiendomsverdi, Eiendomsmeglerforetakenes forening, and Finn.no 2013); coverage ~70% of transactions. (PDF pp.89–90)
- Statistics Norway (2013b): quarterly indices 1991–2012 for all houses, detached, row houses, multi-family dwellings; FINN.no sales; "mix-adjusted hedonic index" (fn 131: hedonic controls dwelling size and location only; mix adjustment for other characteristics, per Mack and Martínez-García 2011). (PDF p.90)
- Figure 40 (referenced on PDF p.90, figure itself beyond p.90): real indices for Bergen, Kristiansand, Oslo, Trondheim and aggregate 1870–2002 "follow the same trends throughout the observation period and are in line with developments in the Norwegian housing market as discussed in the literature." Fn 132 narrative (cut off at the end of PDF p.90, mid-sentence "Husbanken (2011) in-"): 1890s boom from population growth/urbanization, 1899 building-industry crash, consolidation to 1905, WWI (neutral but nominal prices lag inflation; 1916 rent controls), 1920s rise, Grytten (2010) explains 1920s–30s real rise by nominal stability during general deflation; banking crisis to 1991/1993 and strong expansion thereafter (fn 130-series text at top of p.90).
- **Not in range:** the Norway sources table (would be Table 23), the Norway splicing decisions and caveats, construction cost, land, CPI.

---

## (d) Headline interpretations about long-run house prices stated or shown in pages 1–90

The appendix is mostly documentation; interpretive statements in this range are:

1. **Flat-then-rising ("hockey stick") pattern, visible in the robustness figures (PDF pp.5–6):** the weighted and fixed-sample mean real house price indices (1990=100) hover roughly between 40 and 70 from 1870 to around 1950, with a dip through the world wars, and then rise steeply to 150–230 by 2010 (Figures 9, 10, 11). The authors' text here only states the weighting schemes; the pattern is in the plots.
2. **Summary statistics (Table 4, PDF p.11):** across all 14 countries, mean annual Δlog nominal house price is 0.016 pre-WWII vs 0.066 post-WWII, with CPI inflation 0.004 vs 0.043 — i.e. (my arithmetic, not stated by the authors) roughly 1.2% vs 2.3% real per year. Several countries have *negative* mean nominal growth pre-WWII (Canada −0.014, Denmark −0.002, Japan −0.006, Netherlands −0.009, UK −0.008).
3. **Structural breaks (Table 3, PDF p.4):** with k=1 the single break in the log real house price index falls in 1952–1973 for 10 of 14 countries (Switzerland 1952, USA 1953, Japan 1960, Denmark 1961, Finland 1962, Australia 1963, France 1964, Germany 1964, Great Britain 1972, Canada 1973); only Belgium (1991), Netherlands (1995), Norway (1999) and Sweden (2000) break later. Downward breaks are flagged only for Germany 1916 and Japan 1945 (k=3).
4. **Role of land (A.4, PDF pp.6–8 and Figures 12–13, 16):** the main-text decomposition attributes house price growth to land vs construction cost via a Cobb-Douglas housing production function with α = 0.5; the appendix shows the imputed real land price index (14-country mean) is roughly flat from the 1880s to the 1950s and then rises several-fold to 2010 under either Cobb-Douglas or Leontief technology and for α ∈ {0.25, 0.5, 0.75}; additional cost wedges (sales taxes, permit fees) "do not systematically bias the results." Real construction costs (Figure 15, PDF p.9) rise only modestly by comparison. Figure 16 (PDF p.10) shows real residential land prices for AUS, BEL, CHE, GBR, JPN, USA rising steeply after mid-century (Japan peaking ~1990 then falling).
5. **Country narratives of weak pre-1950 prices:** Australia — "The only very moderate rise in nominal house prices between the beginning of the 20th century and 1950 is striking" (fn 36, PDF p.22), attributed partly to the stock of urban land developed in the 1880s and to wartime price controls lifted in 1949; Germany — real prices collapsed in WWI/hyperinflation under rent control, still "substantially below their pre-World War I level" in the mid-1920s (PDF p.69), and the 1950s–60s surge is tied to abolition of the 1936 building-site price ceilings (1960) and rent controls (by 1965) (PDF p.72); Netherlands — "long stagnation" 1929–1949, real prices −30% 1930–36, rent controls until 1959 (fn 126, PDF p.84); Norway — 1916 rent controls and nominal prices lagging WWI inflation (fn 132, PDF p.90); France — wartime rent controls "severe and long-lasting" (fn 91, PDF p.61). A recurring mechanism named in these narratives is **rent control / price control** depressing real house prices through mid-century.
6. **Measurement caveats the authors repeatedly emphasise:** city-only early coverage; asking vs transaction prices; no quality adjustment before the 1970s–80s; CPI deflators are urban-biased and quality-unadjusted (PDF p.19). They nonetheless conclude: "Based on extensive historical research, we are confident that the indices offer an accurate picture of house price developments in each of our 14 countries." (PDF pp.14–15)

---

## (e) Reference list

**Not in pages 1–90.** No bibliography appears in this range; citations are in-text (author, year) with hyperlinks. For cross-referencing with the bibliography in later pages, the citation keys encountered in this range are:

- *Methodology (A.1, B.1):* European Commission (2013); Silver (2014); Mack and Martínez-García (2011); Case and Shiller (1987); Bailey, Muth and Nourse (1963); Case and Wachter (2005); Shiller (1993); Case, Pollakowski and Wachter (1991); Case and Quigley (1991); Nagarja and Wachter (2014); Pollakowski (1995); Bai and Perron (2003); Davis and Heathcote (2007); Bank for International Settlements (2013); Federal Reserve Bank of Dallas (2013); Stapledon (2012a); Maiwald (1954); Fleming (1966); Belgian Association of Surveyors (2013); Engineering News Record (2013); Eurostat (1996); OECD and EUROSTAT (1996); Dechent (2006a); Bosworth and Perry (1994); Goldsmith (1981, 1985); Piketty and Zucman (2014); Jordà, Schularick and Taylor (2016); Grytten (2004); Officer (2007).
- *Australia:* Stapledon (2007, 2012a, 2012b); Abelson and Chung (2005); Australian Bureau of Statistics (2013, 2014, 2015); Abelson (1985); Neutze (1972); Butlin (1962, 1964, 1977); Fisher and Kent (1999); Daly (1982) [also cited as Daly (1981) on PDF p.24]; Garland and Goldsmith (1959); Goldsmith (1985); OECD (2013); Piketty and Zucman (2014); Taylor (2002); International Monetary Fund (2012).
- *Belgium:* De Bruyne (1956); Janssens and de Wael (2005); Antwerpsche Hypotheekkas (1961); Statistics Belgium (2013); European Central Bank (2013); Stadim (2013); Van der Wee (1997); Van den Eeckhout (1992); Leeman (1955); Buyst (1992); Scholliers (1982); Bergen (2011); Poullet (2013); National Bank of Belgium (2012); Goldsmith (1985); IMF (2012).
- *Canada:* Firestone (1951); Canadian Real Estate Association (1981); Subocz (1977); Centre for Urban Economics and Real Estate, University of British Columbia (2013); Statistics Canada (1983; 2013a; 2013b; 2013c; 2014; various years); European Commission (2013); Anderson (1992); Clayton and Miron (1987); Poterba (1991); Buckley and Urquhart (1965); Urquhart (1993); Rymes (1967); Manitoba Agriculture, Food and Rural Initiatives (2010); Province of Manitoba (2012); Goldsmith (1985); OECD (2013); Piketty and Zucman (2014); Taylor (2002); IMF (2012).
- *Denmark:* Abildgren (2006); Økonomiministeret (1966); Danmarks Nationalbank (2003; various years); Statistics Denmark (1958; 2013; 2015; various years a, b); Hansen and Svendsen (1968); Mack and Martínez-García (2011); Kristensen (2007); Nielsen (1933); Hyldtoft (1992); Østrup (2008); Laursen and Madsen (2013); Statistics Copenhagen (1937); O'Rourke, Taylor and Williamson (1996); Goldsmith (1985); Taylor (2002); IMF (2012).
- *Finland:* Statistical Office of the City of Helsinki (various years); Leväinen (1991, 2013); Saarnio (2006); Statistics Finland (2001; 2011; 2013; various years); Heikkonen (1971); Hjerppe (1989); Bank of Finland (1946, 1952, 1955); Taylor (2002); IMF (2012).
- *France:* Conseil Général de l'Environnement et du Développement Durable (2016); Friggit (2002); Beauvois et al. (2005); Duon (1946); National Institute of Statistics and Economic Studies (2012); Price (1981); Caron (1979); Lescure (1992); Duclaud-Williams (1978); Guet (1969); Fédération Française du Bâtiment (2015); Statistics France (2015a, 2015b); OECD (2013, 2016); Goldsmith (1985); Piketty and Zucman (2014); Mitchell (2013); IMF (2015).
- *Germany:* Statistics Berlin (various years); Matti (1963); Association of German Municipal Statisticians (various years); Wagemann (1935); Federal Statistical Office of Germany (1991; 2012; various years a, b); Dechent (2006b); Dechent and Ritzheim (2012); Deutsche Bundesbank (2014); Bank for International Settlements (2013); Mack and Martínez-García (2011); Carthaus (1917); Führer (1995); Rothkegel (1920); Ensgraber (1913); Deutsche Bauzeitung (1921, 1922, 1923); Hausbesitzer-Zeitung für die Rheinprovinz (1922a, 1922b); Wall Street Journal (1921, 1927); The New York Times (1923); Teuteberg (1992); Deutsches Volksheimstättenwerk (1959); DER SPIEGEL (1961); Koch (1961); Horstmann (1959); Vorholt (1995); Goldsmith (1985); OECD (2013); Piketty and Zucman (2014); Taylor (2002); IMF (2012).
- *Japan:* Bank of Japan, Statistics Department (1966; 1970a; 1970b); Bank of Japan (1986a, 1986b); Nanjo (2002); Statistics Japan (2012, 2013); Ministry of Land, Infrastructure, Transport and Tourism, Land and Water Bureau (2009, 2015); Möckel (2007); Nakamura and Saita (2007); Toyo Keizai Shinposha (1991); Statistics Bureau, Ministry of Internal Affairs and Communications (2013); Goldsmith (1985); OECD (2013); van Leeuwen (2004); IMF (2012).
- *Netherlands:* Eichholtz (1997); Mack and Martínez-García (2011); De Haan, van der Wal and de Vries (2008); Statistics Netherlands (CBS); Elsinga (2003); Van Zanden (1997); Van Zanden and van Riel (2000); Van der Heijden, Visscher and Meijer (2006); Vandevyvere and Zenthöfer (2012); Van der Schaar (1987); De Vries (1980); Glasz (1935); Prak and Primus (1992); OECD (2013); Taylor (2002); IMF (2012).
- *Norway (to p.90):* Eitrheim and Erlandsen (2004); Norges Eiendomsmeglerforbund (2012); Eiendomsverdi, Eiendomsmeglerforetakenes forening, and Finn.no (2013); Statistics Norway (2013b); Mack and Martínez-García (2011); Grytten (2010); Husbanken (2011).

---

## (f) Pages not readable or figure-only

- **All 90 pages rendered legibly** (as page images; no OCR failures). No page was skipped.
- **Title page only:** PDF p.1.
- **Figure-only or predominantly figure pages:** PDF p.5 (Figures 9–10), p.9 (Figures 14–15), p.10 (Figure 16), p.13 (Figure 17 decision tree, fully transcribed above). Pages that are a figure plus text: p.6 (Fig. 11), p.7 (Fig. 12), p.8 (Fig. 13), p.16 (Fig. 18), p.24 (Fig. 19), p.25 (Figs. 21 and 20), p.28 (Fig. 22 + Table 6), p.32 (Fig. 23), p.33 (Fig. 24), p.40 (Fig. 25), p.42 (Fig. 26), p.48 (Fig. 27), p.49 (Fig. 28), p.51 (Fig. 29), p.55 (Fig. 30), p.56 (Fig. 31), p.62 (Fig. 32), p.64 (Fig. 33), p.70 (Fig. 34), p.71 (Fig. 35), p.78 (Fig. 36), p.79 (Fig. 37), p.85 (Fig. 38), p.87 (Fig. 39). Figure *values* were not transcribed (only the captions and the authors' verbal readings of them).
- **Table-only pages:** p.4 (Table 3), p.11 (Table 4), p.26 (Table 5), p.34 (Tables 7–8), p.45 (Tables 9–10), p.50 (Tables 11–12), p.57 (Tables 13–14), p.65 (Tables 15–16), p.75 (Tables 17–18), p.82 (Tables 19–20), p.88 (Tables 21–22) — all transcribed above.
- **Internal inconsistencies noticed (reported, not resolved):** Table 9 says UBC Sauder covers "Five cities" vs text "ten main metropolitan areas"; Table 19 JPN1 coverage "Tokyo" vs text "six cities", and JPN2 source "Statistics Japan (2012)" vs text "Bank of Japan (1986b)"; Table 20 MLIT start "1981" vs text "1960"; Table 21 leaves 1995–1996 unassigned; Table 17 DEU5/DEU6 both include 1995; Table 4 France pre-WWII CPI s.d. printed as "0.73"; Figure 11 note lists eight countries for the "9-country" sample; Daly cited as both 1981 and 1982.
- **Range ends mid-country:** PDF p.90 stops inside the Norway section (B.11), in footnote 132, mid-sentence ("Husbanken (2011) in-"). The Norway sources table, splicing decisions, caveats, construction cost, land and CPI entries, Figure 40, and all later countries (Sweden, Switzerland, UK, USA) are beyond this range.


# "No Price Like Home" documentation — extraction, part 2 (PDF pages 91–171)

Source file: `NPLH_documentation.pdf` (171 PDF pages). This part covers **PDF pages 91–171**.

**Page numbering:** the PDF page number is the printed page number + 1 (PDF p. 91 = printed p. 90; PDF p. 171 = printed p. 170). Below, pages are cited as "PDF p. X (printed Y)".

**Range starts mid-country.** PDF p. 91 (printed 90) opens in the middle of appendix section B.11 **Norway** (Figure 40 and the tail of footnote 132). The B.11 heading, the opening Norway discussion of Eitrheim and Erlandsen (2004) and the beginning of footnote 132 are before my range (part 1).

Contents of the range: end of B.11 Norway (PDF 91–94), B.12 Sweden (95–99), B.13 Switzerland (100–107), B.14 United Kingdom (108–119), B.15 United States (119–131), B.16 Summary of house price series (132–143, summary tables for all 14 countries), References (144–171).

---

## (a) Country-by-country documentation

### Norway (B.11, continued) — PDF pp. 91–94 (printed 90–93)

**Long-run house price index 1870–2012 (Table 23, PDF p. 94 / printed 93):**

| Period | Series ID | Source (as cited) | Details (verbatim from Table 23) |
|---|---|---|---|
| 1870–2003 | NOR1 | Eitrheim and Erlandsen (2004) | Geographic Coverage: Four cities; Type(s) of Dwellings: All types of existing dwellings; Data: Real Property Registers; Method: Hedonic weighted repeat sales method. |
| 2004–2012 | NOR2 | Norges Eiendomsmeglerforbund (2012) | Geographic Coverage: Four cities; Type(s) of Dwellings: All types of existing dwellings; Data: Voluntary reports of real estate agents regarding sales of dwellings; Method: Hedonic regression. |

Full references: *Eitrheim, Oyvind, and Solveig K. Erlandsen. 2004. "House Price Indices for Norway, 1819–2003." In Historical Monetary Statistics for Norway 1819–2003. Vol. 35 of Norges Bank Skriftserie / Occasional Papers, ed. Oyvind Eitrheim, Jan T. Klovland and Jan F. Ovigstad, 349–375. Oslo: Norges Bank.* — *Norges Eiendomsmeglerforbund. 2012. "Boligprisstatistikk." http://www.nef.no/xp/pub/topp/boligprisstatistikk.*

Coverage (B.16 summary, PDF pp. 132–143): both series annual; both "Four cities" (not nationwide); property type "All kinds of dwellings"; vintage "Existing"; priced unit: NOR1 per dwelling, NOR2 "Cannot be determined from the source"; method: NOR1 repeat sales + hedonic, NOR2 hedonic. The four cities (Figure 40/41) are Oslo, Bergen, Trondheim, Kristiansand.

Splicing decisions and comparisons (PDF pp. 91–92 / printed 90–91):
- Figure 40 (PDF p. 91): "Norway: nominal house price indices 1870–2003 (1990=100)" — Oslo, Bergen, Trondheim, Kristiansand, Total.
- Figure 41 (PDF p. 92): "Norway: nominal house price indices 1985–2012 (1990=100)" compares four indices for the post-1985 period: Eitrheim and Erlandsen (2004); the national NEF index (all houses); a four-cities index obtained by averaging the NEF data for Bergen, Kristiansand, Oslo and Trondheim (all houses); and the national index by Statistics Norway (all houses). Footnote 133: because Eitrheim and Erlandsen (2004) refers to all kinds of existing dwellings, the "all houses" series from Norges Eiendomsmeglerforbund (2012) and Statistics Norway (2013b) are used for comparison.
- Result: the four indices "move in almost perfect lock-step." Statistics Norway (2013) attributes minor differences between its nationwide index and NEF's to different aggregation weights. After 2000 the national NEF and four-cities indices follow a slightly more pronounced upward trend than the Statistics Norway index.
- Eitrheim and Erlandsen (2004) "perfectly mirrors the level, trend, and volatility of the national NEF index for the time in which they overlap (1990–1999)". Hence "splicing the Eitrheim and Erlandsen (2004) and the NEF index appears recommendable." Caveat (verbatim): "this approach may result in slightly overestimating the increase in house prices in Norway as a whole in the years after 2000 as the NEF index for the whole of Norway indicates a more pronounced rise in house prices when compared to the other indices available."
- Quality caveat (PDF p. 92–93): "A drawback of the long-run index is that prior to 1986 it accounts for quality changes only to some extent. By using the repeat sales method the effect of quality differences between houses is somewhat reduced, but not all potential changes in the quality and standards of dwellings over time are controlled for."

Historical narrative in footnote 132 (continued on PDF p. 91): supply shortage diagnosed as a principal price driver; house prices collapsed during the German occupation (1940–1945); Norwegian State Housing Bank (Husbanken) established 1946; strict housing market regulation 1940–1969 with "house prices essentially fixed until 1954", which "may explain why real house prices continued to decrease after the war until mid-1950"; regulations gradually relaxed 1955–1960; banking liberalization from the late 1970s; the State Housing Bank financed about 87 percent of new dwellings in 1976 and about 53 percent in 1984 (Pugh, 1987); from the mid-1980s a pronounced house price increase "fueled by credit liberalization and a considerable credit boom (Grytten, 2010)"; recession when oil prices fell at the end of the 1980s.

Construction cost data (PDF p. 93 / printed 92; Table 24 on PDF p. 94): available 1935–2012 from Statistics Norway (2013a). 1935–1977: data by Aspelin-Stormbull (a steel, iron and building materials company) for the Oslo area, two indices (brick-built houses; wooden two-family houses), moving closely together (Figure 42, PDF p. 94: "Norway: nominal construction cost indices, 1940–1977 (1955=100)"); 1935–1967 an additional series for rural dwellings. Since 1978 two nationwide series (multifamily houses; detached houses of wood), correlation 0.99 (fn 134). Long-run CC index uses the wooden-house series: 1935–1977 Statistics Norway (2013a), Oslo area, wooden two-family houses, input cost index; 1978–2012 Statistics Norway (2013a), nationwide, detached houses of wood, input cost index. Real unit labor costs in construction 1950–1970 (from Statistics Norway 1981, 1979, 1965) "rose by a little less than 3 percent."

Other data (PDF p. 93): Value of housing stock: Goldsmith (1985), benchmark years 1880, 1899, 1913, 1930, 1939, 1953, 1965, 1972, 1978. Farmland prices: 1985–2005 Statistics Norway (series sent by email, contact Trond Amund Steinset; fn 135) — average purchase price of agricultural and forestry properties sold on the free market; 2006–2010 Statistics Norway (2011), same concept. CPI 1870–2012: Bank of Norway (2015).

### Sweden (B.12) — PDF pp. 95–99 (printed 94–98)

House price data available 1875–2012.

**Long-run house price index 1875–2012 (Table 25, PDF p. 99 / printed 98):**

| Period | Series ID | Source (as cited) | Details (verbatim) |
|---|---|---|---|
| 1875–1956 | SWE1 | Blöndal, Edvinsson and Söderberg (2014); Bohlin (2014) | Geographic Coverage: Stockholm and Gothenburg; Type(s) of Dwellings: Existing multifamily dwellings; Data: Tax assessment values from *Stockholms adresskalender* and *Göteborgs adresskalender*, sales price data from register of certificates of title to properties and other archival sources; Method: SPAR method. |
| 1957–2012 | SWE2 | Blöndal, Edvinsson and Söderberg (2014) | Geographic Coverage: Stockholm and Gothenburg; Type(s) of Dwellings: New and existing single- and two-family houses; Data: Swedish real property register, Statistics Sweden; Method: Mix-adjusted SPAR index. |

Full references: *Blöndal, Sölvi, Rodney Edvinsson, and Johan Söderberg. 2014. "A Price Index for Residential Property in Stockholm, 1875–2012." In Historical Monetary and Financial Statistics for Sweden: House Prices, Stock Returns, National Accounts, and the Riksbank Balance Sheet, 1620–2012. Vol. 2, ed. Rodney Edvinsson, Tor Jacobsen and Daniel Waldenström, 63–100. Stockholm: Ekerlids.* — *Bohlin, Jan. 2014. "A Price Index for Residential Property in Göteborg, 1875–2010." In [same volume], 26–62. Stockholm: Ekerlids.*

Coverage (B.16): both annual; both "Two Cities"; property type SWE1 multi-family, SWE2 "Single- and two family houses"; vintage: both marked "New & Existing" in the B.16 vintage table (note: Table 25 calls SWE1 "Existing multifamily dwellings" — internal inconsistency); priced per dwelling; method SWE1 SPAR, SWE2 mix-adjusted + SPAR.

Sources discussed (PDF p. 95 / printed 94):
- Bohlin (2014): index for multifamily dwellings in Gothenburg 1875–1957, based on sales price data and tax assessments, SPAR method. Blöndal, Edvinsson and Söderberg (2014): SPAR index for multifamily dwellings in inner Stockholm 1875–1957. Fn 136: both also present a repeat sales index with a similar long-run increase, but "because the repeat sales analysis still requires further scrutiny, the authors regard the SPAR index as preferable."
- The same authors also present indices for Stockholm, Gothenburg and Sweden for (i) single- to two-family houses and (ii) multifamily dwellings, 1957–2012 (fn 137: combining Sandelin (1977) and Statistics Sweden data; since 1975 Statistics Sweden (2014c)).
- Statistics Sweden (2014c): annual indices for new and existing one- and two-family dwellings for 12 geographical areas 1975–2012 (fn 138 lists the areas: Sweden as a whole, Greater Stockholm, Greater Gothenburg, Greater Malmö, Stockholm production county, Eastern Central Sweden, Småland with the islands, South Sweden, West Sweden, Northern Central Sweden, Central Norrland, Upper Norrland); combines mix-adjustment and SPAR using the real property register (Lantmäteriet). Fn 139: the OECD (1970–2012) and the Federal Reserve Bank of Dallas (1975–2012) rely on this index.

Comparisons (PDF pp. 96–97 / printed 95–96):
- Figure 43 (PDF p. 96): "Sweden: nominal house price indices 1875–1957 (1912=100)", Gothenburg vs Stockholm. They "generally move together" (correlation 0.954, fn 140); main difference is a comparably stronger increase in Gothenburg after the 1920s and more pronounced fluctuations in the 1950s. Fn 141: Stockholm index grows 0.95 percent per year (nominal) 1920–1957, Gothenburg 2.05 percent. Fn 142: Blöndal et al. caution that the index "may not adequately depict the exact extent of the crises and their aftermaths in 1885–1893 and 1907."
- Figure 44 (PDF p. 97): caption "Sweden: nominal house price indices 1975–2012 (1990=100)" (text says the figure shows indices for 1957–2012; six series: Stockholm/Gothenburg/Sweden × single- and two-family houses / apartment buildings). Apartment-building prices rose less than single- and two-family houses; per Blöndal et al. rent regulation introduced in WWII held down apartment prices, so single-/two-family indices "better reflect market prices". Whether apartment prices were already dampened before 1957 "cannot be determined". Fn 143: rent controls introduced in WWI, abolished 1923; reintroduced 1942 (rents frozen); 1968 Rent Act; fully abolished 1975.

Splicing decision (verbatim, PDF p. 97): "As we aim to provide house price indices with the most comprehensive coverage possible, we use a simple average of the index for Gothenburg and the index for Stockholm. While the index prior to 1957 refers to multifamily dwellings only, we nevertheless use the index for single- to two-family dwellings for 1957–2012 as the index for multifamily dwellings may underestimate the increase in house prices particularly during the 1960s and 1970s." Caveat: property-type break at 1957 (multifamily → single/two-family); city-only coverage (two cities) throughout 1875–2012.

Construction cost data (PDF p. 98 / printed 97; Table 26 on PDF p. 99): 1910–2012, Statistics Sweden (2014a) index for multifamily dwellings built from four sources: 1910–1935 Dickson (1946) input cost index for apartment buildings in Stockholm (relying on Johansson (1944) and Svenska Handelsbanken); 1936–1949 Royal Housing Board (Kungl. Bostadsstyrelsen) input index, Stockholm; 1950–1967 Royal Board of Social Affairs (Kungl. Socialstyrelsen) input index, Stockholm; 1968–2012 Statistics Sweden input price index for apartment buildings, nationwide. Real unit labor costs 1950–1970 (Edvinsson 2005): "increased by about 30 percent."

Other data (PDF p. 98): Value of housing stock: Waldenström (2016). Farmland prices: 1870–1930 Bagge, Lundberg and Svennilson (1933); 1967–1987 Statistics Sweden (various years); 1988–2012 Statistics Sweden (2014b). CPI 1870–2012: Statistics Sweden (2015).

### Switzerland (B.13) — PDF pp. 100–107 (printed 99–106)

House price data available 1901–2012.

**Long-run house price index 1901–2012 (Table 27, PDF p. 107 / printed 106):**

| Period | Series ID | Source (as cited) | Details (verbatim) |
|---|---|---|---|
| 1901–1929 | CHE1 | Swiss Federal Statistical Office (2013) | Geographic Coverage Zurich; Type(s) of Dwellings: Developed lots and building sites; Data: Sales prices collected by Statistics Zurich; Method: Five year moving average of average prices. |
| 1930–1969 | CHE2 | Wüest and Partner (2012) | Geographic Coverage: Nationwide (predominantly large & medium-sized urban centers); Type(s) of Dwellings: Apartment houses; Data: Insurance Companies; Method: Hedonic index. |
| 1970–2012 | CHE3 | Swiss National Bank (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: Apartments; Data: List prices; Method: Mix-adjustment. |

Full references: *Swiss Federal Statistical Office. 2013. "Stadt Zürich: Handänderungen von Grundstücken nach Art des Kaufs 1899–1990." http://www.bfs.admin.ch/bfs/portal/de/index/infothek/lexikon/lex/2.Document.81325.xls.* — *Wüest and Partner. 2012. Immo-Monitoring 2012-1.* — *Swiss National Bank. 2013. "Q4-3 Immobilienpreisindizes - Gesamte Schweiz." Statistisches Monatsheft, Juli 2013.*

Coverage (B.16): CHE1 annual, "Five year moving average of annual data"; CHE2 annual, "Five year moving average of annual index"; CHE3 "Average of quarterly data". Area: CHE1 Zurich; CHE2 "Nationwide, predominantly large & medium-sized urban centers"; CHE3 nationwide. Property type: CHE1 "All kinds of real estate (residential & non-residential)"; CHE2 multi-family; CHE3 "Apartments". Vintage: all existing. Priced unit: CHE1 per square meter; CHE2, CHE3 per dwelling. Method: CHE1 mean/median; CHE2 hedonic; CHE3 mix-adjusted.

Sources (PDF pp. 100–101 / printed 99–100):
- Swiss Federal Statistical Office (2013): average sales prices per square meter for developed lots and building sites in several urban areas since the early 20th century; most comprehensive for Zurich (1899–1990) from the annual Statistical Abstracts of the city. The authors "compute an index based on the five year moving average of the average sales price per square meter of building sites and developed lots in Zurich to smooth out some of the fluctuation stemming from year-to-year variation in the number [of] transaction[s]."
- Wüest and Partner (2012, 40 ff.): two indices since 1930 (multi-family houses; commercial property), hedonic regression (fn 144: controls for quality of local community (size, agglomeration, purchasing power), year of construction, square footage, volume) on pooled cross-sections (fn 145: year N pooled with N−2…N+2). Prior to 2011 built from 2900 arm's-length transactions of commercial and residential property, mostly in large and medium-sized urban centers; raw data from insurance companies (fn 146: Generali, Mobiliar, Nationale Suisse, Swiss Life, Zurich Insurance).
- Swiss National Bank, 1970–2012, quarterly: two mix-adjusted indices (single-family houses; apartments sold by the unit), produced by Wüest and Partner from ~100,000 entries per year of **list prices (not sales prices)** with location, size (rooms), new/existing (Wüest and Partner 2013). Fn 147: the Federal Reserve Bank of Dallas (1975–2012; Mack and Martínez-García 2011) and the OECD use this SNB/W&P index.

Comparisons and splicing (PDF pp. 101–103 / printed 100–102):
- Figure 45 (PDF p. 102): "Switzerland: nominal house price indices 1901–1975 (1930=100)" — building sites in Zurich (raw and 5-yr MA; Statistics Switzerland 2013) and apartment houses (Wüest and Partner 2012). Before 1930 the Zurich index accords with macro narratives (Böhi 1964; Müller and Woitek 2012; Werczberger 1997; Michel 1927; fn 148 gives the narrative: 1920s building boom, rent controls abolished 1924, 1930–36 contraction with recovery after the 1936/37 devaluation, WWII slump, postwar housing shortage, wartime rent controls abolished by 1954, rents +160 percent 1954–1972, shortage until the mid-1970s). W&P and the Zurich site index move together 1930–1975 (correlation 0.85, fn 149).
- 1960s problem: the two indices are "disjoint and inconsistent". W&P's strong fluctuations are "rather surprising"; explanations: poor data quality, or apartment-house specificity (apartment ownership by the unit legalized in 1965, creating uncertainty about apartment houses as investment property; Werczberger 1997), so after 1965 the W&P index reflects apartment-house-specific fluctuations. The Statistics Switzerland index, in turn, "depicts an exaggerated growth trend as house prices are reported to have roughly tripled between 1960 and 1970", which the authors deem implausible given no supporting narrative. Decision (verbatim): "For constructing our long-run index, we therefore rely on the index produced by Wüest and Partner (2012). To smooth out some of the irregular fluctuation, we use a five year moving average of the index."
- Figure 46 (PDF p. 104): "Switzerland: nominal house price indices 1970–2012 (1990=100)" — W&P apartment houses, SNB single-family houses, SNB apartments; "generally follow the same trend". For 1970–2012 the authors use the SNB apartments index for two reasons: (1) the W&P apartment-house index fluctuates more widely (smaller number of observations), so SNB "may hence be a more reliable indicator"; (2) consistency of property type over time ("As the index for 1930–1969 refers to apartment houses only, we also use the index for apartments for 1970–2012").
- Caveats: CHE1 is a land/developed-lot price per m² for one city (Zurich), smoothed by a 5-year moving average; CHE2 is apartment houses only, 5-year moving average, insurance-company data; CHE3 is based on list prices, not transactions.

Construction cost data (PDF pp. 103–105 / printed 102–104; Table 28 on PDF p. 107): 1874–2012. Michel (1927): fire insurance appraisals of newly built residential dwellings in Basel (fn 150: excludes very low-quality dwellings such as WWI barracks and luxury houses); index of average construction cost per cubic meter from >125 appraisals per year; biannual 1874–1916, annual 1916–1924; the authors linearly interpolate to annual. Stadt Zürich (2012): output price index for apartment houses in Zurich 1914–2012 based on quoted prices from a sample of building firms (printed with a stray "?" before the citation: "(?Statistics Zurich, 1958)"; fn 151: index house redefined several times since first published 1932; fn 152: since 1932 bids from 85 to 150 firms). Overlap 1914–1924 similar trend but Basel rises more (fn 153: factor 1.9 vs 1.7). Splice: Michel (1927) Basel for 1874–1913; Zurich (Stadt Zürich 2012) from 1914 (chosen "since the house price index relies on data for Zurich between 1901–1929"). Table 28: 1874–1913 Michel (1927), Basel, all types of residential dwellings, average construction value per cubic meter; 1914–2012 Stadt Zürich (2012), Zurich, apartment houses, output price index.

Land price data (PDF p. 105 / printed 104): 1899–1977 from the Swiss Federal Statistical Office (2013) (Zurich Statistical Abstracts): number of transactions, total value and total area of undeveloped lots → average price per m²; index (1914=100) for 1901–1975 on a five-year moving average; on average 595 transactions per year. A matching Zurich house price index from developed lots (>1200 transactions per year) is computed to compare imputed with empirical land prices in Figure 8 (main text, outside range).

Other data (PDF pp. 105–106): Farmland prices 1953–2012: Swiss Farmers' Union (various years) — average purchase price of farm real estate per hectare in canton Zurich and canton Bern. Value of housing stock: Goldsmith (1985, 1981), benchmark years 1880, 1900, 1913, 1929, 1938, 1948, 1960, 1965, 1973, 1978. CPI: 1870–2007 Taylor (2002); 2008–2012 International Monetary Fund (2012).

### United Kingdom (B.14) — PDF pp. 108–119 (printed 107–118)

House price data available 1899–2012.

**Long-run house price index 1899–2012 (Table 29, PDF p. 114 / printed 113):**

| Period | Series ID | Source (as cited) | Details (verbatim) |
|---|---|---|---|
| 1899–1929 | GBR1 | Land Registry | Geographic Coverage: Three cities; Type(s) of Dwellings: All kinds of existing properties (residential and commercial); Data: Land Registry; Method: Average property value. |
| 1930–1938 | GBR2 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: All dwellings; Data: Holmans (2005) using data from Halifax Building Society; Method: Hypothetical average house price. |
| 1946–1952 | GBR3 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: Modern, existing dwellings; Data: Co-operative Building Society. |
| 1952–1965 | GBR4 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: New Dwellings; Data: BS4 survey of mortgage completions; Method: Average house prices. |
| 1966–1968 | GBR5 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: Existing dwellings; Data: Building Societies Mortgage Survey (BSM); Method: Average house prices. |
| 1969–1992 | GBR6 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: Existing dwellings; Data: Building Societies Mortgage Survey (BSM); Method: Mix-adjustment. |
| 1993–1995 | GBR7 | Department for Communities and Local Government (2013) | Geographic Coverage: Nationwide; Type(s) of Dwellings: Existing dwellings; Data: Five Percent Survey of Mortgage Lenders; Method: Mix-adjustment. |
| 1995–2012 | GBR8 | Land Registry (2013) | Geographic Coverage: England and Wales; Type(s) of Dwellings: Existing dwellings; Data: Land Registry; Method: Repeat sales method. |

Note: **no series for 1939–1945** ("There is no data available for the years of World War II, i.e. 1939–1945", PDF p. 108). How the gap is bridged in the long-run index is not stated in my range.

Full references: *Department for Communities and Local Government. 2013. "Table 502: House prices from 1930, annual house price inflation, United Kingdom, from 1970." https://www.gov.uk/government/statistical-data-sets/live-tables-on-housing-market-and-house-prices.* — *Land Registry. 2013. "House Price Index." http://landregistry.data.gov.uk/app/ukhpi.* — The 1899–1955 Land Registry data were "kindly provided by Peter Mayer, Land Registry" (fn 154); no formal reference entry.

Coverage (B.16): GBR1–GBR7 annual; GBR8 "Average of monthly index". Area: GBR1 "Three cities"; GBR2–7 nationwide; GBR8 "England & Wales". Property type: GBR1 "All kinds of real estate (residential & non-residential)"; GBR2–8 all kinds of dwellings. Vintage: GBR4 new; all others existing. Priced per dwelling throughout. Method: GBR1 mean/median; GBR2 "Hypothetical average price"; GBR3–5 mean/median; GBR6–7 mix-adjusted; GBR8 repeat sales.

Sources discussed (PDF pp. 108–110 / printed 107–109):
- Land Registry 1899–1955: prices registered at first registrations or transfers in "compulsory" areas; value and number of buildings for freehold and leasehold; non-compulsory areas 1930–1956 (fn 154: price paid taken as market value; estimate required for non-monetary transfers).
- Braae 1920–1938 (in Holmans 2005, 270 f.): 1920–1927 property values from contract prices for newly constructed local-authority properties; 1928–1938 estimated average construction costs of private dwellings from building permits.
- DCLG (2013) from 1930 (fn 155: transferred to ONS in March 2012): 1930–1938 Holmans (2005, 128) hypothetical average house price (fn 156: from average value of new loans and Halifax Building Society deposit percentages); 1946–1952 Co-operative Building Society index for modern existing dwellings (fn 157: original covers 1946–1970; likely interwar-built houses; the Co-operative Permanent Building Society became Nationwide in 1970); 1952–1965 MHLG BS4 survey on mortgage completions for new dwellings (fn 158: BS4 and Co-operative series show the same trajectory where they overlap, suggesting new and existing prices did not differ significantly); 1966–2005 the "five percent survey" of building societies — 1966–1992 Building Societies Mortgage (BSM) Survey, mix-adjusted (the "DoE mix-adjusted index", fn 159), existing dwellings; 1993–2002 and 2003–2005 Survey of Mortgage Lenders; 2005–2010 Regulated Mortgage Survey. Fn 160: the OECD (1970–2012) and FRB Dallas (1975–2012) use the DCLG mix-adjusted series.
- Land Registry index since 1995: Price Paid Dataset (all residential transactions in England and Wales), repeat sales (fn 161: excludes new houses), quality adjustment "rather simplistic" because few dwelling characteristics are recorded.
- Nationwide Building Society (2012, 2013): quarterly 1952–2012, four categories (all/new/modern/old houses); method changed over time: 1952–1959 simple average; 1960–1973 floor-area weighted; 1974–1982 weighted by ground floor area, property type and region; since 1983 hedonic (fn 163). Halifax (Lloyds Banking Group 2013): monthly from 1983, hedonic (fn 164). Both "suffer from sample selection bias as they are solely based on price information from finalized and approved mortgages" (fn 165).

Comparisons (PDF pp. 110–113 / printed 109–112):
- Figure 48 (PDF p. 115): "United Kingdom: nominal house price indices 1899–1954 (1930=100)" — Land Registry, DCLG, Braae. DCLG and Braae share a trend; Land Registry fluctuates more and rises in the early 1930s while the others fall, because Land Registry data were "to a very large extent … collected for property in the London area" (fn 166: in the 1930s, 73 percent of first registrations outside London were in the four counties bordering London; Yorkshire the only northern county). Pre-Depression (1899–1929) London prices were comparably less elevated relative to the rest of the country (Justice 1999). Fn 167 corroborates the pre-WWI trajectory with Holmans (2005, Table I.20) capital values 1895–1913, Offer (1981) property sales 1892–1912 and The Economist (1912, 1914, 1918): rise through the 1890s, peak in the early 1900s, fall to WWI; prices "surprisingly stable" in WWI; 1915 rent controls; postwar depression with prices depressed until 1922. Sigsworth and Wilkinson (1977) hedonic indices for 15 Yorkshire towns 1900–1970 (fn 169 lists the towns) follow a similar trend except in the 1930s, so "with the exception of the 1930s, the Land Registry data may provide a reasonable approximation of broad trends in national property markets."
- Figure 47 (PDF p. 113): "United Kingdom: nominal house price indices 1946–2012 (1995=100)" — DCLG (2013), Nationwide (2012), Halifax (2013), Land Registry (2013). All follow the same trend where they overlap; marked increase in the three decades after WWII peaking in the late 1980s; Halifax and Nationwide show a nominal contraction in the early 1990s while DCLG is stagnant; from 1995 all accelerate until the Great Recession. DCLG rises more since the mid-1990s because it uses price weights (biased toward expensive areas such as South England; DCLG 2012); Land Registry rises less because repeat sales exclude new structures (Wood 2005).
- Splicing decision (verbatim, PDF p. 113): "For the period after 1930, we use the DCLG-index. As discussed above, this source is in comparison to the indices by Halifax and Nationwide considered least vulnerable for possible distortions and biases. For the period after 1995, the here constructed long-run index draws on the index by the Land Registry as it relies on the largest possible data source."
- Weaknesses stated (PDF p. 115 / printed 114): "First, before 1930, the index is only based on house prices in the London area and Southeast England. … Second, the index does not control for quality changes prior to 1969, i.e. depreciation and improvements." Using Feinstein and Pollard (1988) estimates of changing size and quality of dwellings, "the average annual real growth rate 1899–2012 of 1.02 percent becomes 0.72 percent in constant quality terms. As this is a rather crude adjustment, however, we use the unadjusted index (see Table 29) for our analysis." (Note Table 29 labels GBR1 "Three cities" whereas the text describes it as London area/Southeast England.)

Construction cost data (PDF pp. 115–117 / printed 114–116; Table 30 on PDF p. 114): 1870–2012. Maiwald (1954) 1845–1938, all kinds of buildings, input cost index from hourly wage rates in 39 large towns (fn 170) and an unweighted average of 10 building materials (fn 171), equal weights (fn 172 sources). Jones (1933) London 1845–1922 output price index (fn 173); Saville (1949) extends it to 1933; neither exclusively residential. Fleming (1966) 1914–1963: residential dwellings in England and Wales tendered to local authorities, average prices per square foot (pre-WWII non-parlor houses; post-WWII three-bedroom; since 1951 standardized to 900 sq ft; fn 174). Department for Business, Innovation and Skills (2013) 1955–2012 output price index for private housing (overlap correlation 0.86 for 1955–1963, fn 175). Interwar extras: Bowley (1945) 1920–1938 local-authority three-bedroom houses; The Economist input cost index (fn 176). Figure 49 (PDF p. 117): "United Kingdom: nominal construction cost indices 1870–1939 (1930=100)". Splice (Table 30): 1870–1913 Maiwald (1954), urban areas, all types of building, input cost index; 1914–1954 Fleming (1966), England and Wales, single-family houses built by local authorities, output price index; 1955–2012 Department for Business, Innovation and Skills (2013), nationwide, all types of (private) residential dwellings, output price index. Real unit labor costs 1950–1970 (Central Statistical Office 1970, 1965, 1957): "real construction costs decreased by 21 percent, real unit labor costs fell by 29 percent."

Land price data (PDF p. 118 / printed 117): 1983–2010 Homes and Community Agency (2014), land prices per hectare in England excluding London; based on local surveyors' estimates for a "typical" serviced site with planning consent, not transactions; England series = simple average of regional series.

Other data (PDF pp. 118–119): Farmland prices: 1870–1914 O'Rourke, Taylor and Williamson (1996); 1915–1943 Ward (1960); 1944–2004 U.K. Department for Environment, Food and Rural Affairs (2011) — average price of agricultural land sales per hectare; 2005–2012 RICS farmland price index (fn 177: series by email, Joshua Miller, RICS). Value of housing stock: Goldsmith (1985) benchmark years 1875, 1895, 1913, 1927, 1937, 1948, 1957, 1965, 1973, 1977; since 1957 ONS (fn 178: by email, Amanda Bell; definitional break at the ESA1979→ESA1995 transition in 1998). Land share 2010 built from Wightman (2010) (Scotland), Lyons and Wightman (2014) (Northern Ireland), DCLG (2015) (residential land value per hectare, England and Wales) and ONS (2010) (amount of residential land). CPI: 1870–2009 Dimsale and Thomas (2010); 2010–2012 International Monetary Fund (2012).

### United States (B.15) — PDF pp. 119–131 (printed 118–130)

House price data available 1890–2012.

**Long-run house price index 1890–2012 (Table 31, PDF p. 131 / printed 130):**

| Period | Series ID | Source (as cited) | Details (verbatim) |
|---|---|---|---|
| 1890–1928 | USA1 | Grebler, Blank and Winnick (1956) | Geographic Coverage: 22 cities; Type(s) of Dwellings: Owner-occupied existing and new single-family dwellings; Data: Financial Survey of Urban Housing, assessment of home owners; Method: Repeat sales method. |
| 1929–1940 | USA2 | Fishback and Kollmann (2015) | Geographic Coverage: 106 cities; Type(s) of Dwellings: Existing single-family dwellings; Data: HOLC city survey; Method: Hedonic index. |
| 1941–1952 | USA3 | Shiller (2009) | Geographic Coverage: Five cities; Type(s) of Dwellings: Existing single-family houses; Data: Newspaper advertisements and Fisher (1951); Method: Average of median home prices. |
| 1953–1974 | USA4 | Shiller (2009) | Geographic Coverage: Nationwide; Type(s) of Dwellings: New and existing dwellings; Data: Federal Housing Administration data as used in the home purchase component of the CPI; Method: Weighted, mix-adjusted index. |
| 1975–2012 | USA5 | Federal Housing Finance Agency (2013) (former OFHEO House Price Index) | Geographic Coverage: Nationwide; Type(s) of Dwellings: New and existing single-family houses; Data: FNMA and FHLMC; Method: Weighted repeat sales method. |

Full references: *Grebler, Leo, David M. Blank, and Louis Winnick. 1956. Capital Formation in Residential Real Estate: Trends and Prospects. Princeton: Princeton University Press.* — *Fishback, Price V., and Trevor Kollmann. 2015. "Hedonic Housing Indexes during the Great Depression." unpublished manuscript.* — *Shiller, Robert J. 2009. Irrational Exuberance. 2nd revised and updated ed., New York: Broadway Books.* — *Federal Housing Finance Agency. 2013. "House Price Indexes." http://www.fhfa.gov/AboutUs/reportsplans/Pages/All-Reports.aspx.*

Coverage (B.16): USA1 annual; USA2 annual with "Interpolate missing values (1930, 1931)"; USA3, USA4 annual; USA5 "Average of quarterly index". Area: USA1 22 cities; USA2 106 cities; USA3 five cities; USA4, USA5 nationwide. Property type: USA1–3 and USA5 single-family; USA4 all kinds of dwellings. Vintage: USA1 marked "New" in B.16 (Table 31 says "existing and new"); USA2, USA3 existing; USA4, USA5 new & existing. Priced per dwelling. Method: USA1 repeat sales; USA2 hedonic; USA3 mean/median; USA4 mix-adjusted; USA5 repeat sales.

Sources discussed (PDF pp. 119–122 / printed 118–121):
- Shiller (2009) is "the standard reference", 1890–2012, combining: 1890–1934 Grebler, Blank and Winnick (1956); 1934–1953 an average price index for 5 cities; 1953–1975 the home-purchase component of the CPI; 1975–1987 the OFHEO national index; since 1987 the Case-Shiller-Weiss index.
- Grebler, Blank and Winnick (1956), 1890–1934: new and existing owner-occupied single-family dwellings in 22 cities, "an approach similar to the repeat sales method", from the 1934 Financial Survey of Urban Housing (owners reported acquisition year, price paid and estimated 1934 value; fn 179). Drawback: 1934 self-assessed values may be systematically biased and ignore quality change; GBW argue depreciation outweighs additions and provide a depreciation-adjusted index (fn 180: 1.374 percent annual compound depreciation). Shiller uses the **non-adjusted** index.
- Five further pre-/Depression-era indices with limited geographic coverage: Garfield and Hoad (1937) three-year moving averages for new owner-occupied six-room single-family "farm houses" [sic; described as wooden dwellings of similar size] in Cleveland and Seattle 1907–1930; Wyngarden (1927) median ask/list prices in three Ann Arbor districts 1913–1925 (fn 181) (the text also says the Wyngarden index "is computed using a repeat sales method and price data for all kinds of existing properties for 1918–1947" — as printed); Fisher (1951) Washington, DC, ask prices of existing single-family houses from newspaper advertisements collected for an unpublished National Housing Agency study (fn 183: 100 metropolitan areas; DC the longest series); Nicholas and Scherbina (2013) hedonic index for Manhattan (residential and commercial) 1920–1930 (fn 184); Fishback and Kollmann (2015) hedonic national index 1929–1940 from the HOLC City Survey covering 106 cities.
- 1934–1953 Shiller: average of five indices — Chicago, Los Angeles, New Orleans and New York (annual median ask prices from local newspapers) plus Washington, DC (Fisher 1951).
- 1953–1975 Shiller: CPI home-purchase component — one-family dwellings bought with FHA-insured loans, mix-adjusted for age and square footage (fn 185: Greenlees 1982). Gillingham and Lane (1982, 10): "the data represents a small and specialized segment of the housing market" (fn 186 quotes their three drawbacks: processing delays, few FHA transactions in the Northeast, FHA mortgage ceiling excludes higher-priced homes). Davis and Heathcote (2007) conclude the index "may underestimate house price appreciation during the 1960s and 1970s."
- 1975–1987 Shiller: OFHEO weighted repeat sales index (now FHFA 2013, fn 187) for single-family dwellings with conventional conforming mortgages bought by Freddie Mac/Fannie Mae (fn 188: controls for renovation/depreciation and infrequent-transaction variance); comprehensive geography but only debt-financed conforming single-family houses. Fn 189: FRB Dallas (1975–2012) uses OFHEO/FHFA; OECD (1970–2012) uses the FHFA all-transactions index.
- Since 1987 Shiller: Case-Shiller-Weiss and successors (fn 190: Fiserv CSW and S&P/Case-Shiller), national index from nine census-division repeat-sales indices for existing single-family homes (fn 191 exclusions).

Comparisons (PDF pp. 122–126 / printed 121–125):
- Figure 50 (PDF p. 124): "United States: nominal house price indices 1907–1946 (1920=100)" (Ann Arbor, Cleveland, Seattle, Manhattan, Washington DC, 22 cities adjusted/unadjusted). Pre-WWI "relative nominal price stability"; moderate increase after WWI; the 1920s boom in Florida and Chicago (White 2014; Galbraith 1955) "is hardly detectable in the inflation-adjusted Shiller-index", so White (2014) argues the Shiller index "may have a substantial downward bias" for the 1920s. "Overall, the performance of U.S. real estate prices in the 1920s and 1930s continues to be debated."
- Figure 51 (PDF p. 124): "United States: nominal house price indices 1929–1940 (1929=100)": the two GBW–Shiller hybrids (unadjusted and depreciation-adjusted) imply a nominal fall of "a little more than 20 percent" 1929–1933 and recovery to "a little more than 90 percent of pre-Depression values by 1940", whereas Fishback and Kollmann (2015) show a fall of "about 40 percent" and prices "significantly below pre-Depression levels until 1940."
- Post-WWII: "a brief but substantial house price boom" (Shiller 2009, 236 f.); 1934–1953 covers only five cities, but Shiller argues the boom was nationwide if weaker. Glaeser (2013): prices did not trend upward 1950s–1970s because supply increased; Shiller's index is "by and large stable between the mid-1950s and the 1970s", possibly downward biased (Davis and Heathcote 2007; Gillingham and Lane 1982).
- Figure 52 (PDF p. 126): "United States: nominal house price indices 1975–2012 (1990=100)", OFHEO vs S&P/Case-Shiller: "reasonable substitutes"; CSW weaker in the first half of the 1990s, catching up by 2000; 2000–2006/7 acceleration more pronounced in CSW; CSW peaks 2006, OFHEO 2007 (Shiller 2009, 235: OFHEO includes refinance appraisals; Leventis 2007: geographic coverage and weighting differences — harmonized, the two are almost identical after 2000). Decision (verbatim): "Due to the broader geographical coverage of the OFHEO index vis-à-vis the CSW index the here constructed long-run index uses the OFHEO-index for the post-1987 period."

Splicing and quality caveats (PDF pp. 126–127 / printed 125–126, verbatim where quoted):
- "A drawback of the index is that it does not represent constant-quality home prices throughout the whole 1890–2012 period. This is particularly the case for 1940–1952."
- "For 1890–1929, we use the depreciation-adjusted index computed by Grebler, Blank and Winnick (1956) to somewhat reduce the quality bias."
- Revision vs earlier version: "In a previous version of this paper, we relied on the adjusted index by Grebler, Blank and Winnick (1956) for 1890–1934 and combined it with the index for 5 cities reported by Shiller (2009) for 1935–1952. Recall from Section 2 that we choose constant quality indices wherever available. In this version, we therefore use the new estimates by Fishback and Kollmann (2015) for 1929, and 1932–1940. To construct an annual index, we interpolate between 1929 and 1932 using growth rates in nominal house prices as indicated by the adjusted Grebler, Blank and Winnick (1956)-index while taking the 1929 and 1932 point estimates by Fishback and Kollmann (2015) as given." Figure 53 (PDF p. 127): "United States: old and revised house price index 1890–2012 (1990=100)" shows both CPI-adjusted versions.
- "Moreover, for 1940–1952, the index has a rather limited geographic coverage that may result in a bias of unknown size and direction. Finally, as suggested by Gillingham and Lane (1982) and Davis and Heathcote (2007), the index for 1953–1974 may suffer from a downward bias."

Construction cost data (PDF pp. 127–129 / printed 126–128; Table 32 on PDF p. 131): 1889–2012. Grebler, Blank and Winnick (1956, Table B-10) 1889–1953: 1910–1953 the Boeckh residential construction cost index (frame and brick one- to six-family houses in 20 cities), extended back to 1889 with building-material prices and construction wage rates (fn 192: Historical Statistics of the United States (1949); union wage rates in 39 cities 1907–1912; the Aldrich report (Senate Committee on Finance 1893) and Department of Commerce and Labor (1908)); weights from Housing and Home Finance Agency (1948, 31) (fn 193: wages 1.0, material 1.5). Davis and Heathcote (2007) 1930–2012: price index for residential structures from BEA data = replacement values; since 1975 constructed to match the FHFA house price series. Engineering News Record (2013) 1909–2012 construction-cost and building-cost input indices (steel, cement, lumber + skilled vs common labor wages in 20 cities), general not residential-specific; other general series exist (U.S. Bureau of the Census 1975, Series N118–137). Splice (Table 32): 1889–1909 Grebler, Blank and Winnick (1956), nationwide, all types of dwellings, input cost index; 1910–1929 Boeckh residential construction cost index as reported in GBW (1956), urban areas, 1–6-family houses, input cost index; 1930–2012 Davis and Heathcote (2007), nationwide, all types of dwellings, replacement values. Real unit labor costs 1950–1970 (Bureau of Economic Analysis 2016): "increased by about 2 percent."

Land price data (PDF p. 129 / printed 128): 1930–2012 Davis and Heathcote (2007) — an imputed land price (house value minus structures), "neither based on actual transactions or appraisals", similar to the paper's Section 4 decomposition.

Other data (PDF pp. 129–130): Farmland prices: 1870–1985 Lindert (1988), value per acre; 1986–2012 U.S. Department of Agriculture (2013), value per acre. Value of housing stock: Goldsmith (1962) benchmark years 1900, 1912, 1922, 1929, 1933, 1939, 1945, 1950, 1958; Davis and Heathcote (2007) total market value of housing stock, dwellings and land 1930–2000; Piketty and Zucman (2014) household wealth incl. housing and land 2001–2012. CPI: 1870–2007 Taylor (2002); 2008–2012 International Monetary Fund (2012).

---

## (a-bis) B.16 Summary of house price series — all 14 countries (PDF pp. 132–143, printed 131–142)

Opening sentence: "The sources of the respective series are listed in Tables 5–31." The summary consists of six check-mark tables; transcribed here in full (also covering countries outside my range).

**Frequency** (PDF pp. 132–133): annual unless stated.
- Australia: AUS1–AUS7 annual; AUS8 other — Average of quarterly index.
- Belgium: BEL1–BEL5 annual.
- Canada: CAN1, CAN2 annual; CAN3 other — Average of quarterly index.
- Denmark: DNK1, DNK2 annual; DNK3 other — Average of quarterly index.
- Finland: FIN1 annual — Three year moving average of annual data; FIN2 annual; FIN3 other — Average of quarterly index.
- France: FRA1, FRA2 annual; FRA3 other — Average of quarterly index.
- Germany: DEU1–DEU4 annual; DEU5, DEU6 other — Average of quarterly index.
- Japan: JPN1, JPN2 annual; JPN3 other — Average of semi-annual index.
- The Netherlands: NLD1 other — Interpolate biannual index; NLD2 other — Average of monthly index; NLD3 other — Average of monthly index.
- Norway: NOR1, NOR2 annual. Sweden: SWE1, SWE2 annual.
- Switzerland: CHE1 annual — Five year moving average of annual data; CHE2 annual — Five year moving average of annual index; CHE3 other — Average of quarterly data.
- United Kingdom: GBR1–GBR7 annual; GBR8 other — Average of monthly index.
- United States: USA1 annual; USA2 annual — Interpolate missing values (1930,1931); USA3, USA4 annual; USA5 other — Average of quarterly index.

**Covered area** (PDF pp. 134–135): Nationwide vs Other (coverage named).
- Australia: AUS1, AUS2 Melbourne; AUS3–AUS7 Six capital cities; AUS8 Eight capital cities.
- Belgium: BEL1, BEL2 Brussels Area; BEL3–BEL5 nationwide.
- Canada: CAN1, CAN2 nationwide; CAN3 Five cities.
- Denmark: DNK1 nationwide (coverage note "Rural areas"); DNK2, DNK3 nationwide.
- Finland: FIN1, FIN2 Helsinki; FIN3 nationwide.
- France: FRA1 Paris; FRA2, FRA3 nationwide.
- Germany: DEU1 Berlin; DEU2 Hamburg; DEU3 Ten cities; DEU4 Western Germany; DEU5, DEU6 Urban areas in Western Germany.
- Japan: JPN1 Six cities; JPN2, JPN3 All cities.
- The Netherlands: NLD1 Amsterdam; NLD2, NLD3 nationwide.
- Norway: NOR1, NOR2 Four cities. Sweden: SWE1, SWE2 Two Cities.
- Switzerland: CHE1 Zurich; CHE2 Nationwide, predominantly large & medium-sized urban centers; CHE3 nationwide.
- United Kingdom: GBR1 Three cities; GBR2–GBR7 nationwide; GBR8 England & Wales.
- United States: USA1 22 cities; USA2 106 cities; USA3 Five cities; USA4, USA5 nationwide.

**Property type** (PDF pp. 136–137): Single-Family / Multi-Family / All Kinds of Dwellings / Other (named).
- Australia: AUS1–AUS6 all kinds of dwellings; AUS7, AUS8 single-family.
- Belgium: BEL1, BEL2 single-family; BEL3, BEL4 other — Small & medium sized dwellings; BEL5 single-family.
- Canada: CAN1 all kinds of dwellings; CAN2 other — All kinds of real estate (residential & non-residential); CAN3 other — Bungalows and two story executive buildings.
- Denmark: DNK1 other — Farms; DNK2, DNK3 single-family.
- Finland: FIN1 other — Building sites for residential use; FIN2, FIN3 multi-family.
- France: FRA1 multi-family; FRA2, FRA3 all kinds of dwellings.
- Germany: DEU1, DEU2, DEU3 other — All kinds of real estate (residential & non-residential); DEU4 other — Land only; DEU5, DEU6 single-family.
- Japan: JPN1, JPN2, JPN3 other — Land only.
- The Netherlands: NLD1 other — All kinds of real estate (residential & non-residential); NLD2, NLD3 all kinds of dwellings.
- Norway: NOR1, NOR2 all kinds of dwellings.
- Sweden: SWE1 multi-family; SWE2 other — Single- and two family houses.
- Switzerland: CHE1 other — All kinds of real estate (residential & non-residential); CHE2 multi-family; CHE3 other — Apartments.
- United Kingdom: GBR1 other — All kinds of real estate (residential & non-residential); GBR2–GBR8 all kinds of dwellings.
- United States: USA1, USA2, USA3 single-family; USA4 all kinds of dwellings; USA5 single-family.

**Property vintage** (PDF pp. 138–139): Existing / New / New & Existing / Other.
- Australia: AUS1–AUS6 existing; AUS7, AUS8 new & existing.
- Belgium: BEL1–BEL5 existing. Canada: CAN1–CAN3 existing.
- Denmark: DNK1, DNK2 existing; DNK3 new & existing.
- Finland: FIN1 new & existing — Land only; FIN2, FIN3 existing.
- France: FRA1–FRA3 existing.
- Germany: DEU1–DEU3 existing; DEU4 new & existing — Land only; DEU5, DEU6 new & existing.
- Japan: JPN1–JPN3 new & existing — Land only.
- The Netherlands: NLD1–NLD3 existing. Norway: NOR1, NOR2 existing.
- Sweden: SWE1, SWE2 new & existing. Switzerland: CHE1–CHE3 existing.
- United Kingdom: GBR1–GBR3 existing; GBR4 new; GBR5–GBR8 existing.
- United States: USA1 new; USA2, USA3 existing; USA4, USA5 new & existing.

**Priced unit** (PDF pp. 139–141): Per Dwelling / Per Square Meter / Other (unit named).
- Australia: AUS1 other — Per Room; AUS2–AUS8 no entry (blank).
- Belgium: BEL1, BEL2 per square meter; BEL3–BEL5 per dwelling.
- Canada: CAN1–CAN3 per dwelling. Denmark: DNK1–DNK3 per dwelling.
- Finland: FIN1–FIN3 per square meter. France: FRA1–FRA3 per dwelling.
- Germany: DEU1 per dwelling; DEU2, DEU3, DEU4 per square meter; DEU5, DEU6 per dwelling.
- Japan: JPN1, JPN2 other — Cannot be determined from the source; JPN3 per square meter.
- The Netherlands: NLD1–NLD3 per dwelling.
- Norway: NOR1 per dwelling; NOR2 other — Cannot be determined from the source.
- Sweden: SWE1, SWE2 per dwelling. Switzerland: CHE1 per square meter; CHE2, CHE3 per dwelling.
- United Kingdom: GBR1–GBR8 per dwelling. United States: USA1–USA5 per dwelling.

**Method** (PDF pp. 142–143): Repeat Sales / Mix-Adjusted / Hedonic / SPAR / Mean-Median / Other (named).
- Australia: AUS1–AUS3 mean/median; AUS4 other — Estimate of Fixed Price; AUS5, AUS6 mean/median; AUS7, AUS8 mix-adjusted.
- Belgium: BEL1–BEL4 mean/median; BEL5 mix-adjusted.
- Canada: CAN1 other — Estimated replacement value; CAN2 mean/median; CAN3 mean/median — Based on price information of standardized dwellings.
- Denmark: DNK1 mean/median — Adjusted for size of property; DNK2 mean/median; DNK3 SPAR.
- Finland: FIN1, FIN2 mean/median; FIN3 mix-adjusted + hedonic.
- France: FRA1, FRA2 repeat sales; FRA3 mix-adjusted + hedonic.
- Germany: DEU1–DEU4 mean/median; DEU5, DEU6 mix-adjusted.
- Japan: JPN1–JPN3 mean/median.
- The Netherlands: NLD1 repeat sales; NLD2 repeat sales + mean/median; NLD3 SPAR.
- Norway: NOR1 repeat sales + hedonic; NOR2 hedonic.
- Sweden: SWE1 SPAR; SWE2 mix-adjusted + SPAR.
- Switzerland: CHE1 mean/median; CHE2 hedonic; CHE3 mix-adjusted.
- United Kingdom: GBR1 mean/median; GBR2 other — Hypothetical average price; GBR3–GBR5 mean/median; GBR6, GBR7 mix-adjusted; GBR8 repeat sales.
- United States: USA1 repeat sales; USA2 hedonic; USA3 mean/median; USA4 mix-adjusted; USA5 repeat sales.

---

## (b) General methodology notes found in the range

- **Index construction = splicing of heterogeneous series.** Every country's long-run index "splices the available series as shown in Table N" (Norway PDF p. 92, Sweden p. 97, Switzerland p. 103, UK p. 113, US p. 126). Series IDs (NOR1…USA5) are assigned per sub-period; the B.16 tables (PDF pp. 132–143) classify every sub-series by frequency, covered area, property type, vintage, priced unit and method (repeat sales, mix-adjusted, hedonic, SPAR, mean/median, other). No splicing arithmetic (e.g. overlap-year chaining) is described in this range.
- **Constant-quality preference.** "Recall from Section 2 that we choose constant quality indices wherever available" (PDF p. 126/127, printed 125–126) — this motivates replacing the Shiller 5-city series with Fishback–Kollmann hedonic estimates for 1929–1940 and using the depreciation-adjusted Grebler–Blank–Winnick index for 1890–1929. Quality grading is otherwise narrative: each country section ends with a "drawback" paragraph (Norway: quality only partly controlled before 1986; UK: no quality control before 1969 and London-only before 1930; US: not constant-quality, esp. 1940–1952; 1953–1974 possibly downward biased).
- **Preference for broad coverage and transaction-based data.** Choices are justified by (i) largest data source (UK Land Registry post-1995), (ii) broadest geography (US OFHEO over CSW post-1987), (iii) least vulnerability to bias (UK DCLG over Halifax/Nationwide, which have mortgage-approval selection bias), (iv) consistency of property type over time (Switzerland apartments; Sweden single/two-family post-1957), and (v) city averages where national series are absent (Sweden: simple average of Gothenburg and Stockholm; Norway: four cities).
- **Smoothing/frequency conversions.** Five-year moving averages for Swiss CHE1 and CHE2; three-year moving average for FIN1; quarterly/monthly/semi-annual series converted by annual averaging; biannual NLD1 interpolated; US 1930–1931 interpolated using adjusted GBW growth rates with FK 1929/1932 point estimates fixed.
- **Nominal vs real.** All figures in the range are **nominal** indices (Figures 40–52), except Figure 53 (US, "CPI-adjusted"). Each country lists the CPI source used for deflation (Norway: Bank of Norway 2015; Sweden: Statistics Sweden 2015; Switzerland and US: Taylor 2002 to 2007, IMF 2012 for 2008–2012; UK: Dimsale and Thomas 2010 to 2009, IMF 2012 for 2010–2012). The UK real growth figure (1.02% p.a. 1899–2012) and the "real house prices continued to decrease after the war until mid-1950" statement for Norway are the only real-terms numbers in the range.
- **Construction cost indices.** Each country has a parallel spliced construction-cost index (Tables 24, 26, 28, 30, 32), with a stated preference for indices covering residential dwellings (or replacement values) rather than all buildings; distinction between input cost indices (wages + materials) and output price indices (tender/quoted prices). Real unit labor costs in construction 1950–1970 are computed from national accounts for each country (Norway +<3%, Sweden +~30%, UK −29% with real construction costs −21%, US +~2%).
- **Land prices.** Observed land prices are used where available (Zurich undeveloped lots 1899–1977; England ex-London surveyor estimates 1983–2010); the US land price (Davis and Heathcote 2007) is imputed, as is the paper's own decomposition (Section 4, Figure 8 — outside my range).
- **Data-provenance notes.** Several series were obtained by email (Norway farmland: Trond Amund Steinset, Statistics Norway; UK farmland 2005–2012: Joshua Miller, RICS; UK housing wealth: Amanda Bell, ONS; UK Land Registry 1899–1955 data: Peter Mayer).
- **Other users of the same series.** The OECD and FRB Dallas (Mack and Martínez-García 2011) rely on the same national sources (Statistics Sweden 2014c; SNB; DCLG; OFHEO/FHFA) — footnotes 139, 147, 160, 189.

## (c) Headline interpretive statements about long-run house prices (with pages)

- Norway (fn 132, PDF p. 91): house prices collapsed during the 1940–1945 occupation; with prices "essentially fixed until 1954", "real house prices continued to decrease after the war until mid-1950"; a pronounced increase from the mid-1980s "fueled by credit liberalization and a considerable credit boom", followed by recession when oil prices fell in the late 1980s.
- Sweden (PDF p. 96, fn 141): 1920–1957 nominal growth 0.95% p.a. (Stockholm) vs 2.05% p.a. (Gothenburg); apartment-building prices held down by WWII rent regulation, so single-/two-family indices "better reflect market prices" (PDF p. 97).
- Switzerland (PDF pp. 102–103): "we can nevertheless assume that Swiss house prices rose during the 1960s", but a tripling 1960–1970 (Statistics Switzerland index) is "implausible"; rents rose 160% 1954–1972 after rent-control abolition (fn 148).
- United Kingdom (PDF p. 115, printed 114): "the average annual real growth rate 1899–2012 of 1.02 percent becomes 0.72 percent in constant quality terms" (Feinstein–Pollard adjustment; unadjusted index retained). Narrative (fn 167, PDF pp. 111–112): rise in the 1890s, peak early 1900s, fall to WWI; "surprisingly stable" in WWI; depressed until 1922; postwar (Figure 47, PDF p. 112–113): marked increase for three decades after WWII peaking in the late 1980s, early-1990s contraction, "impressive acceleration" from 1995 to the Great Recession.
- United States (PDF pp. 122–126): pre-WWI nominal stability; the 1920s boom "hardly detectable" in the real Shiller index (possible substantial downward bias, White 2014); "the performance of U.S. real estate prices in the 1920s and 1930s continues to be debated"; Fishback–Kollmann imply a ~40% nominal fall 1929–1933 with no recovery to pre-Depression levels by 1940, vs ~20% fall and >90% recovery in the Shiller/GBW hybrids; "brief but substantial house price boom" in the late 1940s; prices "by and large stable between the mid-1950s and the 1970s" (possibly downward biased); "remarkable acceleration" 2000–2006/7 with CSW peaking in 2006 and OFHEO in 2007.
- The paper's overall thesis (long-run flatness then post-war rise, role of land) is **not** stated in my range; the range only cross-references Section 2 (constant-quality choice), Section 4 (land/structure decomposition) and Figure 8 (Zurich imputed vs observed land prices).

## (d) Reference list (PDF pp. 144–171, printed 143–170) — complete transcription

Transcribed from the page images; ligatures and en-dashes restored where the PDF text layer dropped them; spellings as printed (e.g. "Dimsale", "Nagarja", "Cheltenhem", "Derviation", "Agricultual"). URLs as printed.

1. Abelson, Peter. 1985. "House and Land Prices in Sydney: 1925 to 1970." *Urban Studies*, 22: 521–534.
2. Abelson, Peter, and Demi Chung. 2005. "The Real Story of Housing Prices in Australia from 1970 to 2003." *Australian Economic Review*, 38(3): 265–281.
3. Abildgren, Kim. 2006. "Monetary Trends and Business Cycles in Denmark 1875–2005." *Danmarks Nationalbank Working Papers*, 43/2006.
4. Anderson, George D. 1992. *Housing Policy in Canada: Lecture Series*. Vancouver: Centre for Human Settlements, University of British Columbia for Canada Mortgage and Housing Corporation.
5. Antwerpsche Hypotheekkas. 1961. *Waarde der Onroerende Goederen: Evolutie en Huidig Peil*. Antwerp: Antwerpsche Hypotheekkas.
6. Association of German Municipal Statisticians. various years. *Statistisches Jahrbuch Deutscher Städte*. Jena: Gustav Fischer.
7. Australian Bureau of Statistics. 2013. "House Price Indexes: Eight Capital Cities." http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/6416.0Mar%202013?OpenDocument.
8. Australian Bureau of Statistics. 2014. "Residential Property Price Indexes: Concepts, Sources and Methods, Australia." http://www.abs.gov.au/ausstats/abs@.nsf/PrimaryMainFeatures/6464.0.
9. Australian Bureau of Statistics. 2015. "Australian National Accounts: National Income, Expenditure and Product. Table 5. Expenditure on Gross Domestic Product (GDP), Implicit price deflators." http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/5206.0Jun%202015?OpenDocument.
10. Bagge, Gösta, Erik Lundberg, and Ingvar Svennilson. 1933. *Wages, Cost of Living and National Income in Sweden 1860–1930*. Stockholm Economic Studies, London: P.S. King & Son Ltd.
11. Bai, Jushan, and Pierre Perron. 2003. "Computation and Analysis of Multiple Structural Change Models." *Journal of Applied Econometrics*, 18(1): 1–22.
12. Bailey, Martin J., Richard F. Muth, and Hugh O. Nourse. 1963. "A Regression Method for Real Estate Price Index Construction." *Journal of the American Statistical Association*, 58(304): 933–942.
13. Bank for International Settlements. 2013. "Property Price Statistics." http://www.bis.org/statistics/pp.htm.
14. Bank of Finland. 1946. "Bank of Finland Building Cost Index." *Bank of Finland Monthly Bulletin*, 20(4–6): 35–36.
15. Bank of Finland. 1952. "Bank of Finland Building Cost Index Renewed." *Bank of Finland Monthly Bulletin*, 16(3–4): 33–34.
16. Bank of Finland. 1955. "Building Cost Index." *Bank of Finland Monthly Bulletin*, 14(8): 37.
17. Bank of Japan. 1986a. *Bank of Japan: The First Hundred Years: Appendices*. Tokyo: Bank of Japan.
18. Bank of Japan. 1986b. *Bank of Japan: The First Hundred Years: Materials*. Tokyo: Bank of Japan.
19. Bank of Japan, Statistics Department. 1966. *Hundred-Year Statistics of the Japanese Economy*. Tokyo: Bank of Japan.
20. Bank of Japan, Statistics Department. 1970a. *Supplement to Hundred-Year Statistics of the Japanese Economy: English Translation of Explanatory Notes*. Tokyo: Bank of Japan.
21. Bank of Japan, Statistics Department. 1970b. *Supplement to Hundred-Year Statistics of the Japanese Economy: English Translation of Footnotes*. Tokyo: Bank of Japan.
22. Bank of Norway. 2015. "Historical Monetary Statistics: Consumer Price Index for Norway 1516–2003." http://www.norges-bank.no/en/Statistics/Historical-monetary-statistics/Consumer-price-indices/.
23. Beauvois, Martine, Alain David, Francois Dubujet, Jacques Friggit, Christian Gourieroux, Anne Laferrere, Sandra Massonnet, and Edmond Vrancken. 2005. "INSEE Methodes. The Notaires-INSEE Housing Prices Indexes: Version 2 of Hedonic Models." *INSEE Methodes*, 111.
24. Belgian Association of Surveyors. 2013. "ABEX Construction Cost Index." https://www.abex.be/fr/index-revues/index-abex/historique/.
25. Bergen, Dirk. 2011. *Grond te koop? Elementen voor de vergelijking van prijzen van landbouwgronden en onteigeningsvergoedingen in Vlaanderen en Nederland*. Brussels: Department Landbouw en Visserij.
26. Blöndal, Sölvi, Rodney Edvinsson, and Johan Söderberg. 2014. "A Price Index for Residential Property in Stockholm, 1875–2012." In *Historical Monetary and Financial Statistics for Sweden: House Prices, Stock Returns, National Accounts, and the Riksbank Balance Sheet, 1620–2012*. Vol. 2, , ed. Rodney Edvinsson, Tor Jacobsen and Daniel Waldenström, 63–100. Stockholm: Ekerlids.
27. Böhi, Hans. 1964. "Hauptzüge einer schweizerischen Konjunkturgeschichte." *Swiss Journal of Economics and Statistics*, 100(1-2): 71–105.
28. Bohlin, Jan. 2014. "A Price Index for Residential Property in Göteborg, 1875–2010." In *Historical Monetary and Financial Statistics for Sweden: House Prices, Stock Returns, National Accounts, and the Riksbank Balance Sheet, 1620–2012*. Vol. 2, , ed. Rodney Edvinsson, Tor Jacobsen and Daniel Waldenström, 26–62. Stockholm: Ekerlids.
29. Bosworth, Barry, and George L. Perry. 1994. "Productivity and Real Wages: Is There a Puzzle?" *Brookings Papers on Economic Activity*, 1/1994: 317–344.
30. Bowley, Marian. 1945. *Housing and the State 1919–1944*. London: George Allen and Unwin Ltd.
31. Buckley, Kenneth A.H., and Malcolm C. Urquhart. 1965. *Historical Statistics of Canada*. Cambridge: Cambridge University Press.
32. Bureau of Economic Analysis. 2016. "National Income and Product Accounts." http://www.bea.gov/iTable/iTable.cfm?ReqID=9&step=1reqid=9&step=1&isuri=1.
33. Butlin, Matthew W. 1977. "A Preliminary Annual Database 1900/01 to 1973/74." *Reserve Bank of Australia Research Discussion Paper*, 7701.
34. Butlin, Noel G. 1962. *Australian Domestic Product, Investment, and Foreign Borrowing 1861-1938/39*. Cambridge, MA : Cambridge University Press.
35. Butlin, Noel G. 1964. *Investment in Australian Economic Development, 1861–1900*. Cambridge: Cambridge University Press.
36. Buyst, Eric. 1992. *An Economic History of Residential Building in Belgium between 1890 and 1961*. Leuven: Leuven University Press.
37. Canadian Real Estate Association. 1981. *Annual Report 1981*. Ottawa: Canadian Real Estate Association.
38. Caron, Francois. 1979. *An Economic History of Modern France*. London: Methuen.
39. Carthaus, Vilma. 1917. *Zur Geschichte und Theorie von Grundstückskrisen in deutschen Grossstädten mit besonderer Berücksichtigung von Gross-Berlin*. Jena: Gustav Fischer.
40. Case, Bradford, and John M. Quigley. 1991. "The Dynamics of Real Estate Prices." *Review of Economics and Statistics*, 22(1): 50–58.
41. Case, Bradford, and Susan Wachter. 2005. "Residential Real Estate Price Indices as Financial Soundness Indicators: Methodological Issues." In *Real Estate Indicators and Financial Stability*. Vol. 21 of BIS Papers, 197–211. Basel: Bank for International Settlements, Washington DC: The International Monetary Fund.
42. Case, Bradford, Henry O. Pollakowski, and Susan M. Wachter. 1991. "On Choosing Between House Price Index Methodologies." *American Real Estate and Urban Economics Association Journal*, 19(3): 286–307.
43. Case, Karl E., and Robert J. Shiller. 1987. "Prices of Single-Family Homes Since 1970: New Indexes for Four Cities." *New England Economic Review*, 5(Sept.): 45–56.
44. Central Statistical Office. 1957. *National Income and Expenditure 1957*. London : H.M.S.O.
45. Central Statistical Office. 1965. *National Income and Expenditure 1965*. London : H.M.S.O.
46. Central Statistical Office. 1970. *National Income and Expenditure 1970*. London : H.M.S.O.
47. Centre for Urban Economics and Real Estate, University of British Columbia. 2013. "Canadian Cities Housing and Real Estate Data." http://www.sauder.ubc.ca/Faculty/Research_Centres/Centre_for_Urban_Economics_and_Real_Estate/Residential_Real_Estate_2.
48. Clayton, Frank, and John R. Miron. 1987. *Housing in Canada 1945–1986: An Overview and Lessons Learned*. Ottawa: Canada Mortgage and Housing Corporation.
49. Conseil General de l'Environnement et du Developpement Durable. 2016. "House Prices in France: Property Price Index, French Real Estate Market Trends in the Long Run." http://www.cgedd.developpement-durable.gouv.fr/house-prices-in-france-property-price-index-french-a1117.html.
50. Daly, Maurice T. 1982. *Sydney Boom Sydney Bust: The City and Its Property Market 1850–1981*. Sydney: George Allen and Unwin.
51. Danmarks Nationalbank. 2003. *Mona - A Quarterly Model of the Danish Economy*. Copenhagen: Danmarks Nationalbank.
52. Danmarks Nationalbank. various years. *Monetary Review*. Copenhagen: Danmarks Nationalbank.
53. Davis, Morris A., and Jonathan Heathcote. 2007. "The Price and Quantity of Residential Land in the United States." *Journal of Monetary Economics*, 54(8): 2595–2620; data located at Land and Property Values in the U.S., Lincoln Institute of Land Policy http://www.lincolninst.edu/resources/.
54. De Bruyne, Jean-Pierre. 1956. "L'Évolution des Prix des Immeubles Urbains de l'Agglomération Bruxelloise de 1878 à 1952." *Bulletin de l'Institut de Recherches Economiques et Sociales*, 22: 57–93.
55. Dechent, J. 2006a. "Zur Entwicklung eines Baukostenindex." *Wirtschaft und Statistik*, 2/2006: 172–181.
56. Dechent, Jens. 2006b. "Häuserpreisindex - Entwicklungsstand und aktualisierte Ergebnisse." *Wirtschaft und Statistik*, 12/2006: 1285–1295.
57. Dechent, Jens, and Stefan Ritzheim. 2012. "Preisindizes für Wohnimmobilien: Ergebnisse für 2011 und Einführung eines Online-Erhebungsverfahrens." *Wirtschaft und Statistik*, 10/2012: 891–897.
58. De Haan, Jan, Erna van der Wal, and Paul de Vries. 2008. "The Measurement of House Prices: A Review of the Sale-Price-Appraisal-Ratio-Method." http://www.cbs.nl/NR/rdonlyres/1392243B-5BF2-4C56-8A4B-6C0C1A1CC6EE/0/20080814sparmethodart.pdf.
59. Department for Business, Innovation and Skills. 2013. "BIS Prices and Cost Indices: Output Price Indices." https://www.gov.uk/government/publications/bis-prices-and-cost-indices.
60. Department for Communities and Local Government. 2012. "Housing Statistical Release." http://webarchive.nationalarchives.gov.uk/20120919132719/www.communities.gov.uk/documents/statistics/pdf/2066836.pdf.
61. Department for Communities and Local Government. 2013. "Table 502: House prices from 1930, annual house price inflation, United Kingdom, from 1970." https://www.gov.uk/government/statistical-data-sets/live-tables-on-housing-market-and-house-prices.
62. Department for Communities and Local Government. 2015. "Land Value Estimates for Policy Appraisal 2014." https://www.gov.uk/government/publications/land-value-estimates-for-policy-appraisal.
63. Department of Commerce and Labor. 1908. *Bulletin of the Department of Labor No. 77*. Washington, D.C.: United States Government Printing Office.
64. DER SPIEGEL. 1961. "Baulandpreise: Noch mal davongekommen." *DER SPIEGEL*, 11: 32–33.
65. Deutsche Bauzeitung. 1921. "Wege zur Milderung der Wohnungsnot in Deutschland." *Deutsche Bauzeitung*, 55(56): 250–251.
66. Deutsche Bauzeitung. 1922. "Gedanken zum Reichsmieten-Gesetz." *Deutsche Bauzeitung*, 56(5): 29–30.
67. Deutsche Bauzeitung. 1923. "Über die Wirkung der Wohnungs-Zwangswirtschaft in Deutschland." *Deutsche Bauzeitung*, 57(5): 27–28.
68. Deutsche Bundesbank. 2014. "Methodische Erläuterungen zu den Indikatoren." http://www.bundesbank.de/Navigation/DE/Statistiken/IWF_bezogenen_Daten/FSI/Methodische_Erlaeuterungen/methodische_erlaeuterungen.html.
69. Deutsches Volksheimstättenwerk. 1959. *Handhabung des Preisstops, Grundstückspreisentwicklung und Anwendung des Baulandbeschaffungsgesetzes*. Vol. 14 of Wissenschaftliche Untersuchungen und Vorträge, Cologne: Deutsches Volksheimstättenwerk.
70. De Vries, J. 1980. "Die Benelux-Länder 1920–1970." In *Die europäischen Volkswirtschaften im zwanzigsten Jahrhundert*. , ed. Carlo M. Cipolla and K. Borchard, 1–46. Stuttgart: Fischer Verlag.
71. Dickson, Harald. 1946. *Byggnadskostnader och byggnadsmaterialmarknader*. Meddelanden, Stockholm: Statens Kommitte för Byggnadsforskning.
72. Dimsale, Nicholas, Sally Hills, and Ryland Thomas. 2010. "The UK Recession in Context - What Do Three Centuries of Data Tell Us?" *Quarterly Bulletin of the Bank of England*, 4/2010.
73. Duclaud-Williams, Roger H. 1978. *The Politics of Housing in Britain and France*. London: Heinemann.
74. Duon, Gaston. 1946. *Documents sur le Problème du Logement à Paris*. Vol. 1 of Études Économiques, Paris : Imprimerie Nationale.
75. Edvinsson, R. 2005. *Growth, Accumulation, Crisis: With New Macroeconomic Data for Sweden 1800-2000*. Almqvist and Wiksell International.
76. Eichholtz, Piet M.A. 1997. "A Long Run House Price Index: The Herengracht Index, 1628–1973." *Real Estate Economics*, 25(2): 175–192.
77. Eiendomsverdi, Eiendomsmeglerforetakenes forening, and Finn.no. 2013. "Eiendomsmeglerbransjens boligprisstatistikk." http://www.nef.no/xp/pub/mx/filer/boligprisstatistikk/markedsrapporter/05-Finn-13-05mai_639635.pdf.
78. Eitrheim, Oyvind, and Solveig K. Erlandsen. 2004. "House Price Indices for Norway, 1819–2003." In *Historical Monetary Statistics for Norway 1819–2003*. Vol. 35 of Norges Bank Skriftserie / Occasional Papers, , ed. Oyvind Eitrheim, Jan T. Klovland and Jan F. Ovigstad, 349–375. Oslo: Norges Bank.
79. Elsinga, M.G. 2003. "Encouraging Low Income Home Ownership in the Netherlands: Policy Aims, Policy Instrument and Results." In *Making cities work, ENHR-conference*. 1–24.
80. Engineering News Record. 2013. "1Q Cost Report Economic Analysis." http://enr.construction.com/economics/quarterly_cost_reports/.
81. Ensgraber, Wilhelm. 1913. *Die Entwicklung Darmstadts und seiner Bodenpreise in den letzten 40 Jahren*. Leipzig: A. Deichert.
82. European Central Bank. 2013. "Residential Property Prices Documentation." https://stats.ecb.europa.eu/stats/sdw/docu/databases/ecb/RPP_metadata.pdf.
83. European Commission. 2013. *Handbook on Residential Property Price Indices (RPPIs)*. Luxemburg: Publications Office of the European Union.
84. Eurostat. 1996. *Methodological Aspects of Construction Price Indices*. Luxemburg: Office of Official Publications of the European Communities.
85. Federal Housing Finance Agency. 2013. "House Price Indexes." http://www.fhfa.gov/AboutUs/reportsplans/Pages/All-Reports.aspx.
86. Federal Statistical Office of Germany. 1991. *Volkswirtschaftliche Gesamtrechnungen, Fachserie 18, Reihe S.15, Revidierte Ergebnisse 1950-1990*. Wiesbaden: Federal Statistical Office of Germany.
87. Federal Statistical Office of Germany. 2012. *Preisindizes für die Bauwirtschaft*. Fachserie 17, Reihe 4, Wiesbaden: Federal Statistical Office of Germany.
88. Federal Statistical Office of Germany. various years,a. *Kaufpreissammlung für landwirtschaftliche Betriebe und Stückländereien*. Fachserie B: Land- und Forstwirtschaft, Fischerei, Wiesbaden: Federal Statistical Office of Germany.
89. Federal Statistical Office of Germany. various years,b. *Kaufwerte für Bauland*. Fachserie 17 Reihe 5, Wiesbaden: Federal Statistical Office of Germany.
90. Federal Statistical Office of Germany. various years,c. *Kaufwerte für landwirtschaftlichen Grundbesitz*. Fachserie 3: Land- und Forstwirtschaft, Fischerei, Wiesbaden: Federal Statistical Office of Germany.
91. Federation Francaise du Batiment. 2015. "Indice FFB du Cout de la Construction." http://www.ffbatiment.fr/federation-francaise-du-batiment/le-batiment-et-vous/en_chiffres/indices-index/Chiffres_Index_FFB_Construction.html.
92. Feinstein, Charles H., and Sidney Pollard. 1988. *Studies in Capital Formation in the United Kingdom, 1750–1920*. Oxford: Clarendon Press.
93. Firestone, Otto J. 1951. *Residential Real Estate in Canada*. Toronto: University of Toronto Press.
94. Fishback, Price V., and Trevor Kollmann. 2014. "New Multi-City Estimates of the Changes in Home Values, 1920-1940." In *Housing and Mortgage Markets in Historical Perspective*. , ed. Kenneth Snowden Price V. Fishback and Eugene N. White, 203–244. Chicago: University of Chicago Press.
95. Fishback, Price V., and Trevor Kollmann. 2015. "Hedonic Housing Indexes during the Great Depression." *unpublished manuscript*.
96. Fisher, Chay, and Christopher Kent. 1999. "Two Depressions, One Banking Collapse." *Reserve Bank of Australia Research Discussion Paper*, 1999-06.
97. Fisher, Ernest M. 1951. *Urban Real Estate Markets: Characteristics and Financing*. New York: National Bureau of Economic Research.
98. Fleming, M.C. 1966. "The Long-Term Measurement of Construction Costs in the United Kingdom." *Journal of the Royal Statistical Society*, 129(4): 534–556.
99. Friggit, J. 2002. "Long Term Home Prices and Residential Property Investment Performance in Paris in the Time of the French Franc, 1840–2001." http://www.cgedd.developpement-durable.gouv.fr/IMG/doc/house-price-france-1840-2001_cle5a8666.doc.
100. Führer, Karl Christian. 1995. "Managing Scarcity: The German Housing Shortage and the Controlled Economy 1914–1990." *German History*, 13(3): 326–354.
101. Galbraith, John K. 1955. *The Great Crash 1929*. Boston: Houghton Mifflin.
102. Garfield, Frank R., and William M. Hoad. 1937. "Construction Costs and Real Property Values." *Journal of the American Statistical Association*, 32(200): 643–653.
103. Garland, John. M., and Raymond W. Goldsmith. 1959. "The National Wealth of Australia." In *The Measurement of National Wealth. Income and Wealth Series VIII*, , ed. Raymond W. Goldsmith and Christopher Saunders, 323–364. Chicago: Quadrangle Books.
104. Gillingham, Robert, and Walter Lane. 1982. "Changing the Treatment of Shelter Costs for Homeowners in the CPI." *Monthly Labor Review*, 6/1982: 9–14.
105. Glaeser, Edward L. 2013. "A Nation of Gamblers: Real Estate Speculation and American History." *American Economic Review*, 103(3): 1–42.
106. Glasz, Ch. 1935. *Hypotheekbanken en Woningmarkt in Nederland*. Nederlandsch Economisch Instituut, 15, Haarlem: Bohn.
107. Goldsmith, Raymond W. 1962. *The National Wealth of the United States in the Postwar Period*. Princeton: Princeton University Press.
108. Goldsmith, Raymond W. 1981. "A Tentative Secular National Balance Sheet for Switzerland." *Schweizerische Zeitschrift für Volkswirtschaft und Statistik*, 117(2): 175–187.
109. Goldsmith, Raymond W. 1985. *Comparative National Balance Sheets: A Study of Twenty Countries, 1688–1978*. Chicago: University of Chicago Press.
110. Grebler, Leo, David M. Blank, and Louis Winnick. 1956. *Capital Formation in Residential Real Estate: Trends and Prospects*. Princeton: Princeton University Press.
111. Greenlees, John S. 1982. "An Empirical Evaluation of the CPI Home Purchase Index, 1973–1978." *Real Estate Economics*, 10(1): 1–24.
112. Grytten, O. H. 2004. "A Consumer Price Index for Norway, 1516–2003." In *Historical Monetary Statistics for Norway 1819–2003*. 47–98. Oslo: Norges Bank.
113. Grytten, Ola Honningdal. 2010. "The Economic History of Norway." In *EH.Net Encyclopedia*. , ed. Robert Whaples. http://eh.net/encyclopedia/the-economic-history-of-norway/.
114. Guet, Jean. 1969. "Les indices du cout de la construction." *Economie et statistique*, 2(1): 75–79.
115. Hansen, Svend A., and Knud E. Svendsen. 1968. *Dansk Pengehistorie, 1700–1914*. Copenhagen: Danmarks Nationalbank.
116. Hausbesitzer-Zeitung für die Rheinprovinz. 1922a. "Die zunehmende Ueberfremdung Bayerns." *Hausbesitzer-Zeitung für die Rheinprovinz*, 3(3).
117. Hausbesitzer-Zeitung für die Rheinprovinz. 1922b. "Wie sich Häuser verzinsen." *Hausbesitzer-Zeitung für die Rheinprovinz*, 11(3).
118. Heikkonen, Eero. 1971. *Asuntopalvelukset Suomessa 1860–1965*. Kasvututkimuksia III, Helsinki: Suomen Pankin Taloustieteellisen Tutkimuslaitoksen Julkaisuja.
119. Hjerppe, Riitta. 1989. *The Finnish Economy 1860–1985: Growth and Structural Change*. Vol. XIII of Studies on Finland's Economic Growth, Helsinki: Bank of Finland.
120. Holmans, Alan E. 2005. *Historical Statistics of Housing in Britain*. Cambridge: Cambridge Center for Housing and Planning Research.
121. Homes and Community Agency. 2014. "Residential Land Value Data." http://webarchive.nationalarchives.gov.uk/20140805133148/http://www.homesandcommunities.co.uk/ourwork/residential-land-value-data.
122. Horstmann, K. 1959. "Neuberechnung von Preismesszahlen für Wohngebäude." *Wirtschaft und Statistik*, 11: 586–593.
123. Housing and Home Finance Agency. 1948. *Housing Statistics Handbook*. Washington, D.C.: United States Government Printing Office.
124. Husbanken. 2011. "The History of the Norwegian State Housing Bank." http://www.husbanken.no/english/the-history-of-the-norwegian-state-housing-bank/.
125. Hyldtoft, Ole. 1992. "Denmark." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley. Leicester: Leicester University Press.
126. International Monetary Fund. 2012. "World Economic Outlook. Series "Inflation, average consumer prices (index)"." http://imf.org/external/pubs/ft/weo/2012/01/weodata/index.aspx.
127. International Monetary Fund. 2015. "IMF eLibrary Data: International Financial Statistics." http://data.imf.org/?sk=7CB6619C-CF87-48DC-9443-2973E161ABEB.
128. Janssens, Philippe, and Paul de Wael. 2005. *50 Jaar Belgische Vastgoedmarkt: Waar Geschiedenis Tot Toekomst Vergroeit*. Brussels: Roularta Books.
129. Johansson, A. 1944. "Byggnadsproduktionens förutsättningar efter ett vapenstillestand. Utredningar angaende ekonomisk eferkrigsplanering." *Statens Offentliga Utredningar*, 1944(7).
130. Jones, G.T. 1933. *Increasing Return: A Study of the Relation between the Size and Efficiency of Industries with Special Reference to the History of Selected British and American Industries 1850–1910*. Cambridge, MA : Cambridge University Press.
131. Jordà, Òscar, Moritz Schularick, and Alan M. Taylor. 2016. "The Great Mortgaging: Housing Finance, Crises, and Business Cycles." *Economic Policy*, 31(85): 107–152.
132. Justice, Jonathan. 1999. "Bricks Are Worth Their Weight in Gold. A Century of House Prices." *The Guardian*, December 18.
133. Koch, Günther. 1961. "Der geprellte Bausparer: Die Familienheim-Politiker bekommen kalte Füsse." *DIE ZEIT*, 28/1961.
134. Kristensen, Hans. 2007. *Housing in Denmark*. Copenhagen: Centre for Housing and Welfare - Realdania Research.
135. Land Registry. 2013. "House Price Index." http://landregistry.data.gov.uk/app/ukhpi.
136. Laursen, Maria L., Jens Lunde, and Anders H. Madsen. 2013. "A Countrywide House Price Index for 152 Years." *mimeo*.
137. Leeman, August. 1955. *De Woningmarkt in Belgie 1890–1950*. Kortrijk: Uitgeverij Jos. Vermaut.
138. Lescure, Michel. 1992. "France." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley. Leicester: Leicester University Press.
139. Leväinen, Kari I. 1991. *A Calculation Method for a Site Price Index*. Helsinki: The Association of Finnish Cities.
140. Leväinen, Kari I. 2013. *Kiinteistö- ja Toimitilajohtaminen*. Helsinki: Helsinki University Press.
141. Leventis, Andrew. 2007. "A Note on the Difference between the OFHEO and S&P/Case-Shiller House Price Indexes." http://www.fhfa.gov/PolicyProgramsResearch/Research/PaperDocuments/20070725_RP_NoteDifferencesOFHEOSPCaseShillerHPI_N508.pdf.
142. Lindert, Peter H. 1988. "Long-Run Trends in American Farmland Values." *Agricultural History*, 62(3): 45–85.
143. Lloyds Banking Group. 2013. "Halifax House Price Index." http://www.lloydsbankinggroup.com/media1/economic_insight/halifax_house_price_index_page.asp.
144. Lyons, Ronan, and Andy Wightman. 2014. "A Land Value Tax for Northern Ireland." http://www.andywightman.com/docs/NICVA_LVT.pdf.
145. Mack, Adrienne, and Enrique Martínez-García. 2011. "A Cross-Country Quarterly Database of Real House Prices: A Methodological Note." *FRB Dallas Globalization and Monetary Policy Institute Working Paper*, 99(99).
146. Magnusson, Lars. 2000. *An Economic History of Sweden*. London: Routledge.
147. Maiwald, K. 1954. "An Index of Building Costs in the United Kingdom, 1845–1938." *The Economic History Review*, 7(2): 187–203.
148. Manitoba Agriculture, Food and Rural Initiatives. 2010. *Manitoba Agriculture Yearbook 2009*. Winnipeg: Manitoba Agriculture, Food and Rural Initiatives.
149. Matti, Werner. 1963. "Hamburger Grundeigentumswechsel und Baulandpreise 1903–1937 und 1955–1962." *Hamburg in Zahlen: Monatsschrift des Statistischen Landesamtes der Freien und Hansestadt Hamburg*, 1963/1.
150. Michel, Oskar. 1927. *Die Preisentwicklung der Basler Wirtschaftsliegenschaften von 1899–1924*. Bern: Staempfli & Cie.
151. Ministry of Land, Infrastructure, Transport and Tourism, Land and Water Bureau. 2009. "Land Price Trends in 2009 as Indicated by the Public Notice of Land Prices (Overview)." http://tochi.mlit.go.jp/english/wp-content/uploads/2013/04/Land_price_public_notice_20094.pdf.
152. Ministry of Land, Infrastructure, Transport and Tourism, Land and Water Bureau. 2015. "Construction Cost Deflator." http://www.mlit.go.jp/toukeijouhou/chojou/csg/chapter_5.htm.
153. Mitchell, Brian. 2013. "International Historical Statistics, 1750–2010 [Online]." http://www.palgraveconnect.com/pc/doifinder/10.1057/9781137305688.
154. Möckel, Rainer. 2007. "Bodenwert." In *Lexikon der Immobilienwertermittlung*. , ed. Siegfried Sandner and Ulrich Weber, 170–174. Köln: Bundesanzeiger Verlag.
155. Müller, Margrit, and Ulrich Woitek. 2012. "Wohlstand, Wachstum und Konjunktur." In *Wirtschaftsgeschichte der Schweiz im 20. Jahrhundert*. , ed. Patrick Halbeisen, Margrit Müller and Beatrice Veyrassat, 91–222. Basel: Schwabe Verlag.
156. Nagarja, Chaitra H., Lawrence D. Brown, and Susan M. Wachter. 2014. "Repeat Sales House Price Index Methodology." *Journal of Real Estate Literature*, 22(1): 23–46.
157. Nakamura, Koji, and Yumi Saita. 2007. "Land Prices and Fundamentals." *Bank of Japan Working Paper Series*, 07-E-08.
158. Nanjo, Takashi. 2002. "Developments in Land Prices and Bank Lending in Interwar Japan: Effects of the Real Estate Finance Problem on the Banking Industry." *Bank of Japan Monetary and Economic Studies*, 20(3): 117–142.
159. National Institute of Statistics and Economic Studies. 2012. "Comptes du Logement 2011: Tableaux de Donnees 2011 et Series Chronologiques 1984–2011." http://www.statistiques.developpement-durable.gouv.fr/publications/p/references/comptes-logement-2011-premiers-resultats-2012.html.
160. Nationwide Building Society. 2012. "Nationwide House Price Index." http://www.nationwide.co.uk/hpi/Nationwide_HPI_Methodology.pdf.
161. Nationwide Building Society. 2013. "UK Series: UK House Prices Since 1952." http://www.nationwide.co.uk/hpi/datadownload/data_download.htm.
162. Needleman, Lionel. 1965. *The Economics of Housing*. London: Staples Press.
163. Neutze, Max. 1972. "The Cost of Housing." *Economic Record*, 48(3): 357–373.
164. Nicholas, Tom, and Anna Scherbina. 2013. "Real Estate Prices During the Roaring Twenties and the Great Depression." *Real Estate Economics*, 41(2): 276–309.
165. Nielsen, Axel. 1933. *Dänische Wirtschaftsgeschichte*. Jena: Gustav Fischer.
166. Norges Eiendomsmeglerforbund. 2012. "Boligprisstatistikk." http://www.nef.no/xp/pub/topp/boligprisstatistikk.
167. OECD. 2013. "Table 9B. Balance-sheets for non-financial assets." http://stats.oecd.org/Index.aspx?DataSetCode=SNA_TABLE9B.
168. OECD. 2016. "Aggregate National Accounts, SNA 2008 (or SNA 1993): Gross domestic product." http://dx.doi.org/10.1787/data-00001-en.
169. OECD and EUROSTAT. 1996. "Sources and Methods: Construction Price Indices." http://www.oecd.org/industry/business-stats/2372435.pdf.
170. Offer, Avner. 1981. *Property and Politics 1870–1914: Landownership, Law, Ideology and Urban Development in England*. Cambridge: Cambridge University Press.
171. Office for National Statistics. 2010. "Land Use Statistics (Generalised Land Use Database)." http://data.gov.uk/dataset/land_use_statistics_generalised_land_use_database.
172. Officer, Lawrence H. 2007. "What Was the Consumer Price Index Then? A Data Study." http://www.measuringworth.com/docs/cpistudyrev.pdf.
173. Økonomiministeret. 1966. *Inflationens Arsager: Betænkning Afgivet af det Økonomiministeren den 2. juli 1965 Nedsatte Udvalg*. Copenhagen: Statens Trykningskontor.
174. O'Rourke, Kevin, Alan M. Taylor, and Jeffrey G. Williamson. 1996. "Factor Price Convergence in the Late Nineteenth Century." *International Economic Review*, 37(3): 499–530.
175. Østrup, Finn. 2008. *Finansielle Kriser*. Copenhagen: Thomson.
176. Piketty, Thomas, and Gabriel Zucman. 2014. "Capital Is Back: Wealth-Income Ratios in Rich Countries, 1700–2010." *Quarterly Journal of Economics*, 129(3): 1255–1310.
177. Pollakowski, Henri O. 1995. "Data Sources for Measuring House Price Changes." *Journal of Housing Research*, 6(3): 377–388.
178. Pooley, Colin G. 1992. "England and Wales." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley, 73–104. Leicester: Leicester University Press.
179. Poterba, James M. 1991. "House Price Dynamics: The Role of Tax Policy and Demography." *Brookings Papers on Economic Activity*, 2/1991: 143–203.
180. Poullet, Ghislaine. 2013. "Real Estate Wealth by Institutional Sector." *NBB Economic Review*, Spring 2013: 79–93.
181. Prak, Niels, and Hugo Primus. 1992. "The Netherlands." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley, 325–348. Leicester: Leicester University Press.
182. Price, Roger. 1981. *An Economic History of Modern France, 1830–1914*. London: Macmillan Press Ltd.
183. Province of Manitoba. 2012. "Agriculture Statistics." http://www.gov.mb.ca/agriculture/market-prices-and-statistics/yearbook-and-state-of-agriculture/-statistics-tables.html.
184. Pugh, Cedric. 1987. "The Political Economy of Housing Policy in Norway." *Scandinavian Housing and Planning Research*, 4(4): 227–241.
185. Rothkegel, Walther. 1920. *Untersuchungen über Bodenpreise, Mietpreise und Bodenverschuldung in einem Vorort von Berlin*. Berlin: Duncker & Humblot.
186. Rydenfeld, Sven. 1981. "The Rise, Fall, and Revival of Swedish Rent Control." In *Rent Control: Myths & Realities*. , ed. Walter Block and Edgar Olsen. Vancouver: The Fraser Institute.
187. Rymes, Thomas K. 1967. *Fixed Capital Flows and Stocks, Manufacturing, Canada 1926-1960, Methodology*. Ottawa: Queen's Printer.
188. Saarnio, Miko. 2006. "Housing Price Statistics at Statistics Finland." *Paper presented at the OECD-IMF Workshop on Real Estate Price Indices, Paris, France*.
189. Sandelin, Bo. 1977. *Prisutveckling och Kapitalvinster på Bostadsfastigheter*. Gothenburg: University of Gothenburg.
190. Saville, John. 1949. "The Measurement of Real Cost in the London Building Industry, 1923–1939." *Bulletin of Economic Research*, 1(2): 67–80.
191. Scholliers, Peter. 1982. "Verschuivingen in het Arbeidersconsumptiepatroon, 1890–1930." *Journal of Belgian History*, 13(2–3): 273–312.
192. Senate Committee on Finance. 1893. *Report on Wholesale Prices, on Wages, and on Transportation. Senate Report No. 1394, 52d Congress, 2d Session*. Vol. 1, Washington, D.C.: United States Government Printing Office.
193. Shiller, Robert J. 1993. "Measuring Asset Values for Cash Settlement in Derivative Markets: Hedonic Repeated Measures Indices and Perpetual Futures." *Journal of Finance*, 48(3): 911–931.
194. Shiller, Robert J. 2009. *Irrational Exuberance*. . 2nd revised and updated ed., New York: Broadway Books.
195. Sigsworth, Eric M., and Roy K. Wilkinson. 1977. "Trends in Property Values and Transactions and Housing Finance in Yorkshire since 1900." *Social Science Research Council Report*.
196. Silver, Mick. 2014. "The Degree and Impact of Differences in House Price Index Measurement." *Journal of Economic and Social Measurement*, 39(4): 305–328.
197. S&P Dow Jones Indices. 2013. "S&P CoreLogic Case-Shiller Home Price Indices Methodology." http://eu.spindices.com/search/?query=case+shiller+methodology&Search=GO&Search=GO.
198. Stadim. 2013. "Stadimindexen." http://www.stadim.be/nl/tools/stadim-indexen.
199. Stadt Zürich. 2012. "Zürcher Index der Wohnbaupreise." https://www.stadt-zuerich.ch/prd/de/index/statistik/themen/bauen-wohnen/wohnbaupreise/zuercher-index-der-wohnbaupreise.html.
200. Stapledon, Nigel D. 2007. "Long Term Housing Prices in Australia and Some Economic Perspectives." PhD diss. University of New South Wales, Sydney.
201. Stapledon, Nigel D. 2012a. "Historical Housing-Related Statistics for Australia 1881–2011 – A Short Note." *UNSW Australian School of Business Research Paper*, 52/2012.
202. Stapledon, Nigel D. 2012b. "Trends and Cycles in Sydney and Melbourne House Prices from 1880 to 2011." *Australian Economic History Review*, 52(3): 293–317.
203. Statistical Office of the City of Helsinki. various years. *Helsinki Statistical Yearbook*. Helsinki: Statistical Office of the City of Helsinki.
204. Statistics Belgium. 2013. "Bouw En Industrie - Verkoop Van Onroerende Goederen 1986–2012." http://statbel.fgov.be/nl/modules/publications/statistiques/economie/downloads/bouw_en_industrie_verkoop_onroerende_goederen.jsp.
205. Statistics Berlin. various years. *Statistisches Jahrbuch der Stadt Berlin*. Berlin: Statistisches Amt der Stadt Berlin.
206. Statistics Bureau, Ministry of Internal Affairs and Communications. 2013. "Historical Statistics of Japan: Chapter 3 - National Accounts." http://www.stat.go.jp/english/data/chouki/03.htm.
207. Statistics Canada. 1983. "Historical Statistics of Canada: Section S - Construction and Housing." http://www.statcan.gc.ca/pub/11-516-x/sections/4057757-eng.htm.
208. Statistics Canada. 2013a. "New Housing Price Index, 2007 Base: Technical Note." http://www23.statcan.gc.ca/imdb-bmdi/document/2310_D1_T2_V4-eng.pdf.
209. Statistics Canada. 2013b. "Price Indexes of Apartment and Non-Residential Building Construction, by Type of Building and Major Sub-Trade Group." http://www5.statcan.gc.ca/cansim/a03.
210. Statistics Canada. 2013c. "Table 327-0005 - New Housing Price Indexes, Monthly (Index), CANSIM (database)." http://www5.statcan.gc.ca/cansim/a26?lang=eng&id=3270005.
211. Statistics Canada. 2014. "Table S60-64: Principal statistics of the construction industry (construction contractors), 1934 to 1976." http://www.statcan.gc.ca/access_acces/archive.action?l=eng&loc=S60_64-eng.csv.
212. Statistics Canada. various years. *Statistical Review*. Ottawa: Dominion Bureau of Statistics.
213. Statistics Copenhagen. 1937. *Statistisk Maanedsskrift*. Vol. 13, Copenhagen: Statistics Copenhagen.
214. Statistics Denmark. 1958. *Landbrugets Priser 1900–1957*. Vol. 1 of Statistiske Undersøgelser, Copenhagen: Statistics Denmark.
215. Statistics Denmark. 2013. "EJEN5: Price Index for Sales of Property (2006=100) by Category of Real Property (Quarter)." www.statbank.dk/EJEN5.
216. Statistics Denmark. 2015. *Documentation of Statistics for Construction Cost Index for Residential Buildings 2015 Quarter 2*. Copenhagen: Statistics Denmark.
217. Statistics Denmark. various years,a. *Statistical Ten-Year Review*. Statistics Denmark.
218. Statistics Denmark. various years,b. *Statistical Yearbook*. Statistics Denmark.
219. Statistics Finland. 2001. *Rakennuskustannusindeksi 2000=100: Käyttäjän käsikirja*. Käsikirjoja, Helsinki: Statistics Finland.
220. Statistics Finland. 2011. "Prices of Dwellings in Housing Companies." http://www.stat.fi/til/ashi/index_en.html.
221. Statistics Finland. 2013. "Real Estate Prices." http://www.stat.fi/til/kihi/index_en.html.
222. Statistics Finland. various years. *Statistical Yearbook of Finland*. Helsinki: Statistics Finland.
223. Statistics France. 2015a. "Documentation: Indice du cout de la construction (ICC)." http://www.bdm.insee.fr/bdm2/documentationGroupe.action?codeGroupe=1&page=liste.
224. Statistics France. 2015b. "Indice du cout de la construction des immeubles a usage d'habitation (ICC)." http://www.bdm.insee.fr/bdm2/affichageSeries.action?bouton=OK&idbank=000008630&codeGroupe=1.
225. Statistics Japan. 2012. "Historical Statistics of Japan." http://www.stat.go.jp/english/data/chouki/index.htm.
226. Statistics Japan. 2013. "Japan Statistical Yearbook 2013." http://www.stat.go.jp/english/data/nenkan/index.htm.
227. Statistics Netherlands (CBS). 2000. "Een nieuw prijsindexcijfer voor de bouwkosten van nieuwe woningen." http://www.cbs.nl/NR/rdonlyres/0DA1AFF8-8D5C-4220-A605-1813B1881918/0/Een_nieuwe_prijsindex.pdf.
228. Statistics Netherlands (CBS). 2009a. "Landbouwgrond; koop - en pachtprijzen, regio, 1990–2001." http://statline.cbs.nl/StatWeb/publication/?VW=T&DM=SLNL&PA=37411LLB&D1=a&D2=1-3&D3=0&D4=4,9,14,19,24,29,34,39,44,49,54-55&HD=131202-0917&HDR=T&STB=G1,G2,G3.
229. Statistics Netherlands (CBS). 2009b. "Methodebeschrijving Outputprijsindexcijfer van Nieuwbouwwoningen." http://www.cbs.nl/NR/rdonlyres/24DC74BD-AD6C-482D-A4D8-902687BF13CE/0/Methodenbeschrijving_PINW2005100.pdf.
230. Statistics Netherlands (CBS). 2013a. "Historie Bouwnijverheid vanaf 1899." http://statline.cbs.nl/StatWeb/publication/?PA=37286.
231. Statistics Netherlands (CBS). 2013b. "Landbouw en Visserij; 1899–1999." http://statline.cbs.nl/StatWeb/publication/?VW=T&DM=SLNL&PA=37858&D1=424-425,432-437&D2=a&HD=131202-0920&HDR=T&STB=G1.
232. Statistics Netherlands (CBS). 2013c. "New Dwellings; Input Price Indices Building Costs." http://statline.cbs.nl/StatWeb/publication/?VW=T&DM=SLEN&PA=81911ENG&LA=EN.
233. Statistics Netherlands (CBS). 2013d. "Prijzen Bestaande Koopwoningen." http://www.cbs.nl/nl-NL/menu/themas/prijzen/cijfers/default.htm.
234. Statistics Netherlands (CBS), Department of National Accounts. 1959. "The Preparation of a National Balance Sheet: Experience in the Netherlands." In *The Measurement of National Wealth. Income and Wealth Series VIII*, , ed. Raymond W. Goldsmith and Christopher Saunders, 119–146. Chicago: Quadrangle Books.
235. Statistics Norway. 1965. *Nasjonalregnskap 1865-1960*. Oslo: Statistisk Sentralbyra.
236. Statistics Norway. 1979. *Nasjonalregnskap 1962–1978*. Oslo: Statistisk Sentralbyra.
237. Statistics Norway. 1981. *Nasjonalregnskap 1949–1962*. Oslo: Statistisk Sentralbyra.
238. Statistics Norway. 2011. "Transfers of Agricultural Properties." https://www.ssb.no/statistikkbanken/selectvarval/Define.asp?subjectcode=&ProductId=&MainTable=Tinglyst9&nvl=&PLanguage=1&nyTmpVar=true&CMSSubjectArea=jord-skog-jakt-og-fiskeri&KortNavnWeb=laeiti&StatVariant=&checked=true.
239. Statistics Norway. 2013a. "Construction Cost Index for Residential Buildings." https://www.ssb.no/en/priser-og-prisindekser/statistikker/bkibol/.
240. Statistics Norway. 2013b. "House Price Index." http://www.ssb.no/en/priser-og-prisindekser/statistikker/bpi.
241. Statistics Sweden. 2014a. "Construction Costs 1910–2013." http://www.scb.se/en_/Finding-statistics/Statistics-by-subject-area/Prices-and-Consumption/Building-price-index-and-Construction-cost-index-for-bu/Construction-cost-index-for-buildings-CCI--input-price-index/Aktuell-Pong/12529/72178/.
242. Statistics Sweden. 2014b. "Real Estate Price Index for Agricultural Real Estate (1992=100) by Region. Years 1988–2013." http://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__BO__BO0501__BO0501A/FastpiLantbrukRegAr/?rxid=e0bbbee4-571e-42d8-9575-8e3b5c334cec.
243. Statistics Sweden. 2014c. "Real Estate Price Index for One- or Two-Dwelling Buildings for Permanent Living (1981=100) by Region. Years 1975–2013." http://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__BO__BO0501__BO0501A/FastpiPSRegAr/?rxid=1b182879-62d6-4d6b-8cbc-42bea3fbfdd9.
244. Statistics Sweden. 2015. "Price Level in Sweden 1830–2014." http://www.scb.se/en_/Finding-statistics/Statistics-by-subject-area/Prices-and-Consumption/Consumer-Price-Index/Consumer-Price-Index-CPI/Aktuell-Pong/33779/Consumer-Price-Index-CPI/33837/.
245. Statistics Sweden. various years. "Priser på Jordbruksfastigheter." *Statistika meddelanden*, P20.
246. Statistics Switzerland. 2013. "Bodenpreise." http://www.bfs.admin.ch/bfs/portal/de/index/dienstleistungen/history/01/00/05/04.html.
247. Statistics Zurich. 1958. "Der Zürcher Baukostenindex auf neuer Grundlage." *Schweizerische Bauzeitung*, 76(46): 693–694.
248. Strömberg, Thord. 1992. "Sweden." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley. Leicester: Leicester University Press.
249. Subocz, Irene Ursula. 1977. "Housing Price Indices." Master's diss. University of British Columbia Faculty of Commerce & Business Administration.
250. Swiss Farmers' Union. various years. *Statistische Erhebungen und Schätzungen über Landwirtschaft und Ernährung*. Brugg: Swiss Farmers' Union.
251. Swiss Federal Statistical Office. 2013. "Stadt Zürich: Handänderungen von Grundstücken nach Art des Kaufs 1899–1990." http://www.bfs.admin.ch/bfs/portal/de/index/infothek/lexikon/lex/2.Document.81325.xls.
252. Swiss National Bank. 2013. "Q4-3 Immobilienpreisindizes - Gesamte Schweiz." *Statistisches Monatsheft*, Juli 2013.
253. Taylor, Alan M. 2002. "A Century of Purchasing-Power Parity." *Review of Economics and Statistics*, 84(1): 139–150.
254. Teuteberg, Hans J. 1992. "Germany." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley. Leicester: Leicester University Press.
255. The Economist. 1912. "Sales Of Land And House Property In 1911." *The Economist*, January 6, 1912.
256. The Economist. 1914. "Land And House Property In 1913." *The Economist*, January 17, 1914.
257. The Economist. 1918. "Land And Property In 1917." *The Economist*, January 12, 1918.
258. The Economist. 1923. "Land And Property In 1922." *The Economist*, January 27, 1923.
259. The Economist. 1927. "Land And Property In 1926." *The Economist*, January 29, 1927.
260. The New York Times. 1923. "Invite Speculation in Berlin Flats: Drop in the Mark Brings Out Something Novel in Enterprises Far Afield." *The New York Times*, April 10.
261. Toyo Keizai Shinposha. 1991. *Kanketsu showa kokusei soran*. Vol. 2, Tokyo: Toyo Keizai Shinposha.
262. U.K. Department for Environment, Food and Rural Affairs. 2011. "Agricultural Land Sales and Prices in England." http://archive.defra.gov.uk/evidence/statistics/foodfarm/farmgate/agrilandsales/.
263. Urquhart, Malcolm C. 1993. *Gross National Product, Canada, 1870-1926: The Derviation of Estimates*. Kingston and Montreal: McGill-Queen's University Press.
264. U.S. Bureau of the Census. 1975. *Historical Statistics of the United States: Colonial Times to 1970*. Washington, DC: United States Department of Commerce.
265. U.S. Department of Agriculture. 2013. "Land Use, Land Value and Tenure." http://www.ers.usda.gov/topics/farm-economy/land-use,-land-value-tenure.aspx.Up4ei2RYQqQ.
266. Van den Eeckhout, Patricia. 1992. "Belgium." In *Housing Strategies in Europe, 1880–1930*. , ed. Colin G. Pooley, 190–220. Leicester: Leicester University Press.
267. Van der Heijden, Johannes J., Henk Visscher, and Frits Meijer. 2006. "Development of Dutch Building Control (1982–2003): Towards Certified Building Control." *Paper presented at XXIII FIG Congress 2006 in Munich*.
268. Van der Schaar, Jan. 1987. *Groei en Bloei van het Nederlandse Volkshuisvestingsbeleid*. Delft: Delftse Universitaire Pers.
269. Van der Wee, Herman. 1997. "The Economic Challenge Facing Belgium in the 19th and 20th Centuries." In *The Economic Development of Belgium Since 1870*. , ed. Herman Van der Wee and Jan Blomme. Cheltenhem: Edward Elgar Publishing.
270. Vandevyvere, Windy, and Andreas Zenthöfer. 2012. "The Housing Market in the Netherlands." *European Commission Economic Papers*, 457/2012.
271. van Leeuwen, Bas. 2004. "Wage Differentials and Economic Growth in India, Indonesia, and Japan, 1800-2000." http://www.iisg.nl/hpw/globalhistory.php.
272. Van Zanden, Jan L. 1997. *Een klein Land in de 20e eeuw: Economische Geschiedenis van Nederland 1914–1995*. Utrecht: Het Spectrum.
273. Van Zanden, Jan L., and Arthur van Riel. 2000. *Nederland 1780–1914: Staat, instituties en economische ontwikkeling*. Amsterdam: Uitgeverij Balans.
274. Vorholt, Hubert. 1995. "Zur Neuberechnung der Baupreisindizes auf Basis 1991." *Wirtschaft und Statistik*, , (1): 21–29.
275. Wagemann, Ernst. 1935. *Konjunkturstatistisches Handbuch 1936*. Berlin: Hanseatische Verlagsanstalt.
276. Waldenström, Daniel. 2016. "The National Wealth of Sweden 1810–2014." *Scandinavian Economic History Review*, 64(1): 36–54.
277. Wall Street Journal. 1921. "Investments in Germany Should Be Avoided." *Wall Street Journal*, February 4.
278. Wall Street Journal. 1927. "German Real Estate Value: Credit Lifting of Official Rent Restrictions and Return to More Normal Conditions." *Wall Street Journal*, April 5.
279. Ward, John T. 1960. "A Study of Capital and Rent Values of Agricultual Land in England and Wales between 1858 and 1958." PhD diss. Imperial College London.
280. Werczberger, Elia. 1997. "Home Ownership and Rent Control in Switzerland." *Housing Studies*, 12(3): 337–353.
281. White, Eugene N. 2014. "Lessons from the Great American Real Estate Boom and Bust of the 1920s." In *Housing and Mortgage Markets in Historical Perspective*. , ed. Kenneth Snowden Fishback, Price V. and Eugene N. White, 115–158. Chicago: University of Chicago Press.
282. Wightman, Andy. 2010. "A Land Value Tax for Scotland: Fair, Efficient, Sustainable. A Report prepared by Andy Wightman for the Green MSPs in the Scottish Parliament." http://www.andywightman.com/docs/LVTREPORT.pdf.
283. Wood, Robert A. 2005. "A Comparison of UK Residential House Price Indices." In *Real Estate Indicators and Financial Stability*. Vol. 21 of BIS Papers, 212–227. Basel: Bank for International Settlements, Washington DC: The International Monetary Fund.
284. Wüest and Partner. 2012. *Immo-Monitoring 2012-1*.
285. Wüest and Partner. 2013. "Asking Price Index Methodology." http://www.wuestundpartner.com/online_services/immobilienindizes/angebotspreisindex/information/index_e.phtml.
286. Wyngarden, Herman. 1927. "An Index of Local Real Estate Prices." *Michigan Business Studies*, 1(2).

(286 entries; the list runs Abelson → Wyngarden with no further pages after PDF p. 171.)

## (e) Pages not readable / figure-only / near-empty

All 81 pages (PDF 91–171) were read as page images; none failed. Pages with no or minimal text:
- PDF p. 124 (printed 123): figures only — Figure 50 (US nominal indices 1907–1946, 1920=100) and Figure 51 (US 1929–1940, 1929=100).
- PDF p. 106 (printed 105): only two lines (Swiss value of housing stock and CPI), rest blank.
- PDF p. 130 (printed 129): a single word, "(2012)." (end of the US CPI sentence).
- PDF p. 141 (printed 140): tail of the Priced-unit table (GBR8, USA1–USA5) only.
- Figure-plus-table pages: PDF p. 94 (Figure 42 + Tables 23–24), p. 96 (Figure 43), p. 97 (Figure 44), p. 102 (Figure 45), p. 104 (Figure 46), p. 113 (Figure 47), p. 115 (Figure 48), p. 117 (Figure 49), p. 126 (Figure 52), p. 127 (Figure 53). Figure data values were not transcribed (only captions and the authors' descriptions).
- Text-layer caveat: pdftotext drops "fi/ff/ffi" ligatures and en-dashes in this PDF; the transcription above was made from the page images, with the text layer used only to confirm URLs.


