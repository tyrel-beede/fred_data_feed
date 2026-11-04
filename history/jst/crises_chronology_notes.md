# JST Financial Crisis Chronology — extraction notes

Source file: `JSTcrisis_chronology.pdf` (51 PDF pages). All 51 pages were read (PDF pp. 1-20, 21-40, 41-51). Printed page numbers start at 1 on PDF page 4, so **PDF page = printed page + 3**. Page references below and in `jst_crises.csv` are PDF pages unless marked "printed".

## (a) Title, authors, date/version

- **Title:** "JST Financial Crisis Chronology"
- **Authors:** Òscar Jordà (Federal Reserve Bank of San Francisco and University of California, Davis); Moritz Schularick (Federal Reserve Bank of New York, University of Bonn and CEPR); Alan M. Taylor (University of California, Davis, NBER, and CEPR)
- **Date:** February 25, 2021 (title page, PDF p. 1). The document accompanies the **5th release** of the Jordà-Schularick-Taylor Macrohistory Database ("the 18 countries included in the 5th release of the database", Introduction, PDF p. 4). Research assistance: Dimitrios Kanelis. Standard Fed/NBER disclaimer on the title page.
- **Structure:** 1 Introduction; 2 Narrative Chronology (2.1 Australia ... 2.18 United States of America, printed pp. 1-24 / PDF 4-27); 3 Changes to the Previous Version (3.1 Newly added crisis years, 3.2 Removed crisis years; PDF 28-29); 4 Comparison with Different Databases (PDF 30-35); 5 Deviations from other databases and reasoning (5.1-5.4; PDF 36-44); References (PDF 45-51).

## (b) Definition of a systemic financial (banking) crisis — verbatim

From the Introduction (PDF p. 4):

> "The banking crisis variable (crisisJST) takes unity in the first year a country is experiencing a systemic banking crisis, and zero else. An episode of banking distress is coded as a systemic banking crisis if it is characterized by major bank failures, banking panics, substantial losses in the banking sector, significant recapitalization, and/or significant government intervention. Importantly, this definition excludes the failures or losses of individual/small banks without systemic implications from being coded as a crisis episodes."

Section 5 (PDF p. 36) additionally restates the original Schularick & Taylor definition, quoting "Schularick & Taylor (2013, p. 1038)" (the reference list entry is the AER 2012 paper, vol. 102(2), 1029-1061):

> "In line with previous studies, we define financial crises as events during which a country's banking sector experiences bank runs, sharp increases in default rates accompanied by larges losses of capital that result in public intervention, bankruptcy, or forced merger of financial institutions"

Note: the document consistently calls the coded events "systemic banking crises" (not "systemic financial crises"); the CSV `type` column therefore uses "systemic banking crisis" for every episode.

## (c) Methodology: dating, what counts, relation to crisisJST / crisisJST_old

- **Dating rule:** crisisJST = 1 **only in the first year** of a systemic banking crisis; all other years are 0. Multi-year episodes are therefore a single 1. The narrative never gives explicit end years, which is why `end_year` is blank throughout the CSV; where a narrative mentions later years (e.g., USA runs through 1931, NLD interventions in 1922 and 1924, ITA 1990-94 mergers, JPN 2001 "part of the ... crisis that started already in 1997", DNK 1987 "stretched over several years") this is recorded in the description instead.
- **What counts:** major bank failures, banking panics, substantial losses in the banking sector, significant recapitalization, and/or significant government intervention (any of these; see the verbatim definition).
- **What does not count:** failures or losses of individual/small banks without systemic implications. The deviation tables (Section 5.4) make the operative exclusions explicit: (i) bank-equity collapses caused purely by the outbreak of the First World War (1914 in BEL, FRA, GBR, ITA, NLD, NOR) are not crises; (ii) years that are a continuation of an already-coded crisis are not re-coded (BEL/ESP/PRT 2011 and 2010 linked to 2008; JPN 2001 to 1997; JPN 1922 to 1920; DNK 1992 to 1987; IRL 2007 folded into 2008); (iii) "borderline" crises, isolated fraud-driven failures resolved privately with no panic and no public support, or distress without bank suspensions/bank holidays are excluded (CAN 1873/1920/1983, NLD 1907/1931, GBR 1878, USA 1884/1890, FRA 1994, DNK 2011, ITA 2011, JPN 1882/1990); (iv) a year with no narrative evidence of systemic distress is not coded even if other chronologies code it (CHE 1919, DEU 1925).
- **Evidence base:** each episode has a short narrative built from secondary historical literature, with extensive citations (reference list of 108 entries). Section 5 says that "for each banking crisis, the return on bank capital for the respective crisis year is listed" — but the tables that follow do **not** actually print any return-on-bank-capital figures; only verbal reasons are given.
- **crisisJST vs crisisJST_old:** footnote on PDF p. 4: "The most recent update of JST Macrohistory entailed a revision of the crisis chronology. The previous version of the chrisis [sic] chronology is also included in dataset under the label *crisisJST_old*. For details on the changes enacted in the newest release, see Section 3 of this document." Section 3 (PDF p. 28): "The changes in the Jordà-Schularick-Taylor Macrohistory Database are limited to a recoding of specific individual years, which have attracted particular attention through the publication of Baron et al. (2021)). A total of seven years are recoded in five countries. New additions are **Belgium (1876)** and **Japan (1901)**. Excluded from the Macrohistory Database are **Germany (1907)**, **Denmark (1931)**, **Netherlands (1893)**, **Netherlands (1907)** and **Netherlands (1939)**." Hence crisisJST_old = crisisJST − {BEL 1876, JPN 1901} + {DEU 1907, DNK 1931, NLD 1893, NLD 1907, NLD 1939}; 88 vs 91 episodes.

### Section 3.1 — Newly added crisis years (PDF p. 28), verbatim reasons

| New JST Crisis | Reason |
|---|---|
| Belgium (1876) | A few smaller banks went into receivership, and the larger Banque de Belgique, Banque de Bruxelles, and Banque Centrale Anversoise had to be reorganized (Grossman, 2010, p. 299) |
| Japan (1901) | The crisis of 1901 is described as a banking panic that marks the climax of the banks' founding boom and led to the failure of many banks. This banking crisis encouraged Japanese policymakers to consolidate the Japanese banking system (Inoue & Yabushita (1993, pp. 391-393), Okazaki & Yokoyama (2002, pp. 3-4)) |

### Section 3.2 — Removed crisis years (PDF p. 29), verbatim reasons

| Removed JST Crisis | Reason |
|---|---|
| Germany (1907) | Borderline banking crisis |
| Denmark (1931) | Compared with other countries, commercial bank deposits fell only slightly during 1931; there was no general run on the banks and no suspension of payments by any commercial bank (Grossman, 2010, p. 315) |
| Netherlands (1893) | Borderline banking crisis |
| Netherlands (1907) | Borderline banking crisis |
| Netherlands (1939) | Due to the imminent war, some banks were affected by financial distress and the bank Mendelssohn & Co. Amsterdam collapsed. However, there is no narrative evidence that this initiated a systemic banking crisis. |

## (d) Relationship to other chronologies

### Section 4 — Comparison with Different Databases (PDF pp. 30-35)

Intro text (PDF p. 30), paraphrased closely: the JST chronology is compared with Bordo et al. (2001), Reinhart & Rogoff (2009), Laeven & Valencia (2018) and Baron et al. (2021); the table lists whether each database also identifies a banking crisis in the respective year. "Reinhart & Rogoff (2009) cover the entire period between 1870 and 2010, and they distinguish between several forms of crisis. Bordo et al. (2001) cover the period between 1880 and 1997 and classify between banking crises and currency crises. Laeven & Valencia (2018) cover the period between 1970 and 2017 and set several conditions about the degree of financial distress within the banking system and the kind of public intervention. If a banking crisis fulfills half of these criteria, then its identified as 'systemic' in the sense of Laeven & Valencia (2018). Baron et al. (2021) cover the whole relevant period and define '"banking distress' as bank equity declines of over 30% in a year and then separate these bank equity declines into 'panic' versus 'quiet' (non-panic) episodes based on a systematic reading of the narrative evidence for each of these episodes."' (Baron et al., 2021)."

Table legend: Y = (systemic) banking crisis identified; X = not identified; – = no data available (outside that database's coverage); Y(yyyy) = banking crisis identified but dated yyyy.

| Country | JST year | Bordo et al. (2001) | Reinhart & Rogoff (2009) | Laeven & Valencia (2018) | Baron et al. (2021) |
|---|---|---|---|---|---|
| Australia | 1893 | Y | Y | – | Y |
| Australia | 1989 | Y | Y | X | Y |
| Belgium | 1870 | – | Y | – | X |
| Belgium | 1876 | – | X | – | Y |
| Belgium | 1885 | X | X | – | Y (1883) |
| Belgium | 1925 | Y | Y | – | X |
| Belgium | 1931 | Y | Y | – | Y (1929) |
| Belgium | 1934 | Y | Y | – | X |
| Belgium | 1939 | Y | Y | – | X |
| Belgium | 2008 | – | Y | Y | Y |
| Canada | 1907 | X | Y (1908) | – | Y |
| Switzerland | 1870 | – | Y | – | Y |
| Switzerland | 1910 | X | Y | – | X |
| Switzerland | 1931 | Y | Y | – | Y |
| Switzerland | 1991 | X | X | X | Y (1990) |
| Switzerland | 2008 | – | Y | Y | Y |
| Germany | 1873 | – | X | – | Y (1874) |
| Germany | 1891 | X | X | – | Y |
| Germany | 1901 | Y | X | – | Y |
| Germany | 1931 | Y | Y | – | Y (1930) |
| Germany | 2008 | – | Y | Y | Y |
| Denmark | 1877 | – | Y | – | Y |
| Denmark | 1885 | Y | Y | – | Y |
| Denmark | 1908 | Y (1907) | Y (1907) | – | Y (1907) |
| Denmark | 1921 | Y | Y | – | Y (1919) |
| Denmark | 1987 | Y | Y | X | X |
| Denmark | 2008 | – | Y | Y | Y |
| Spain | 1883 | X | X | – | Y (1882) |
| Spain | 1890 | X | X | – | Y |
| Spain | 1913 | X | X | – | X |
| Spain | 1920 | Y | Y | – | Y |
| Spain | 1924 | Y | Y | – | Y |
| Spain | 1931 | Y | Y | – | Y |
| Spain | 1977 | Y | Y | Y | Y (1975) |
| Spain | 2008 | – | Y | Y | Y |
| Finland | 1877 | – | X | – | Y |
| Finland | 1900 | Y | X | – | Y |
| Finland | 1921 | Y | Y | – | Y |
| Finland | 1931 | Y | Y | – | Y |
| Finland | 1991 | Y | Y | Y | Y (1990) |
| France | 1882 | Y | Y | – | Y |
| France | 1889 | Y | Y | – | Y |
| France | 1930 | Y | Y | – | Y |
| France | 2008 | – | Y | Y | Y |
| United Kingdom | 1890 | Y | Y | – | Y |
| United Kingdom | 1974 | Y | Y | X | Y (1973) |
| United Kingdom | 1991 | X | Y | X | Y |
| United Kingdom | 2008 [sic; narrative says 2007] | – | Y | Y | Y (2007) |
| Ireland | 2008 | – | – | Y | Y (2007) |
| Italy | 1873 | – | X | – | Y |
| Italy | 1887 | X | Y | – | Y (1889) |
| Italy | 1893 | Y | Y | – | Y (1891) |
| Italy | 1907 | Y | Y | – | Y |
| Italy | 1921 | Y | Y | – | Y |
| Italy | 1930 | Y | Y | – | Y |
| Italy | 1935 | Y | Y | – | X |
| Italy | 1990 | Y | Y | X | Y (1992) |
| Italy | 2008 | – | X | Y | Y |
| Japan | 1871 | – | X | – | X |
| Japan | 1890 | X | X | – | Y |
| Japan | 1901 | Y | Y | – | Y |
| Japan | 1907 | Y | Y | – | Y |
| Japan | 1920 | X | X | – | Y |
| Japan | 1927 | Y | Y | – | Y |
| Japan | 1997 | Y | Y | Y | Y |
| Netherlands | 1921 | Y | Y | – | Y |
| Netherlands | 2008 | – | Y | Y | Y |
| Norway | 1899 | X | Y | – | Y (1898) |
| Norway | 1922 | Y | Y | – | Y (1919) |
| Norway | 1931 | Y | Y | – | Y |
| Norway | 1988 | Y | Y | Y (1991) | Y (1987) |
| Portugal | 1890 | X | Y | – | Y |
| Portugal | 1920 | Y | Y | – | Y (1921) |
| Portugal | 1923 | Y | Y | – | Y |
| Portugal | 1931 | Y | Y | – | Y |
| Portugal | 2008 | – | Y | Y | Y |
| Sweden | 1878 | – | Y | – | Y |
| Sweden | 1907 | Y | Y | – | Y |
| Sweden | 1922 | X | Y | – | Y (1919) |
| Sweden | 1931 | Y | Y | – | Y (1932) |
| Sweden | 1991 | Y | Y | Y | Y |
| Sweden | 2008 | – | X | Y | Y |
| USA | 1873 | – | Y | – | Y |
| USA | 1893 | Y | Y | – | Y |
| USA | 1907 | Y | Y | – | Y |
| USA | 1930 | Y | Y (1929) | – | Y |
| USA | 1984 | Y | Y | Y (1988) | Y |
| USA | 2007 | – | Y | Y | Y |

Summary of the table: JST episodes **not identified at all** by Baron et al. (2021): BEL 1870, 1925, 1934, 1939; CHE 1910; DNK 1987; ESP 1913; ITA 1935; JPN 1871 (nine; Section 5.3 discusses eight of them and omits BEL 1939). JST episodes within the LV 1970-2017 window that Laeven & Valencia (2018) do **not** identify: AUS 1989, CHE 1991, DNK 1987, GBR 1974, GBR 1991, ITA 1990. Reinhart & Rogoff (2009) do not identify: BEL 1876, BEL 1885, CHE 1991, DEU 1873, 1891, 1901, ESP 1883, 1890, 1913, FIN 1877, 1900, ITA 1873, ITA 2008, JPN 1871, 1890, 1920, SWE 2008. Bordo et al. (2001) do not identify (within 1880-1997): BEL 1885, CAN 1907, CHE 1910, CHE 1991, DEU 1891, ESP 1883, 1890, 1913, GBR 1991, ITA 1887, JPN 1890, 1920, NOR 1899, PRT 1890, SWE 1922. Eighteen JST years are dated differently by at least one other database (listed in the table). The document does not compare itself to Schularick & Taylor (2012/2013) explicitly beyond quoting its definition; Section 3 is the only explicit statement of changes relative to the earlier JST coding (crisisJST_old).

### Section 5 — "Deviations from other databases and reasoning" (PDF pp. 36-44), complete

Intro (PDF p. 36): "Below are tables of all banking crises that have not been coded by Baron et al. (2021) or Laeven & Valencia (2018). This section should explain the coding of these 'controversial' banking crises by the Jordà-Schularick-Taylor database." It then quotes the Schularick & Taylor (2013, p. 1038) definition (see (b) above) and says: "For each banking crisis, the return on bank capital for the respective crisis year is listed, together with the reasoning of why the Jordà-Schularick-Taylor database has coded the respective crisis." (No return-on-bank-capital figures actually appear in the tables.)

#### 5.1 Detailed comparison with Laeven & Valencia (2018) — JST crises that LV do not code (PDF p. 37), verbatim reasons

| Current JST Crisis | Reason |
|---|---|
| Australia (1989) | Ratio of current losses to the average value of banks' lending increased from nearly 0 percent to about 3 percent within 1989; non-performing business loans increased in 1989 and reached 12 percent; two large banks, the State Bank of South Australia (SBSA) and the State Bank of Victoria (STV) effectively failed and they had to rely on extraordinary government support. |
| Switzerland (1991) | Swiss banks incurred loan losses of about 8.5 percent of total loans or more than 10 percent of Swiss GDP; 200 banks did not survive the crisis and lost their independence; sharp increases of default rates accompanied by large losses of capital resulted in forced merger of financial institutions. |
| Denmark (1987) | 142 banks were involved in 75 mergers and acquisitions; the Varde Bank encountered financial difficulties, and the Danish Government supported five banks; the cumulated losses over 1990-1992 were 9 percent of loans; larges losses of capital resulted in forced merger of financial institutions. |
| United Kingdom (1974) | Bank of England created a 1.2 billion pounds lifeboat with public and private funds; 24 secondary banks were supported, 8 secondary banks failed, and several had to merge. |
| United Kingdom (1991) | The Bank of England worried about financial contagion effects and intervened by providing emergency loans to British banks; 25 banks failed until 1994 due to loan defaults and loss of capital. |
| Italy (1990) | 58 banks, with 11 percent of lending, merged with other institutions; the ratio of non-performing loans in southern Italy increased from 10.2 to 25.4 percent from 1993 till 1996. |

#### 5.2 Crises in Laeven & Valencia (2018) but not in Macrohistory (PDF p. 38)

"There is no crisis in Laeven & Valencia (2018) that are not coded in Macrohistory database." (I.e., JST is a superset of LV for these 18 countries; LV's different dates — NOR 1991 vs JST 1988, USA 1988 vs JST 1984 — are not treated as separate crises.)

#### 5.3 Crises in Macrohistory but not in Baron et al. (2021) (PDF p. 39), verbatim reasons

| Current JST Crisis | Reason |
|---|---|
| Belgium (1870) | Sources indicate an extensive bank panic, which made it necessary to close the central bank and the bank counters (Buyst & Maes, 2007, pp. 131-132). |
| Belgium (1925) | Government borrowed in USD to guarantee the liabilities of the Belgian banks; merging activity between banks increased. |
| Belgium (1934) | The failure of the large Belgian bank, Banque du Travail provoked bank runs; government intervened actively to stabilize the banks. |
| Switzerland (1910) | 45 local and regional banks collectively incurred losses of 112 million Swiss francs; 28 banks merged with either a cantonal or a major bank. |
| Denmark (1987) | We have coded the year 1987 because this date is considered the starting point of the Nordic Banking Crisis in Denmark (Abildgren et al., 2011, p. 6). |
| Spain (1913) | It was the first time that the Spanish central bank intervened as Lender of Last Resort, and during this period, Spanish real bank stock prices declined significantly. |
| Italy (1935) | The role of Government and the Bank of Italy was crucial to overcome the crisis and preventing major banks from failing. |
| Japan (1871) | Failure of nine out of ten exchange companies, which were precursors of banks. |

(Belgium 1939 is marked X under Baron et al. (2021) in the Section 4 table but is not discussed here.)

#### 5.4 Crises in Baron et al. (2021) (BVX) but not in Macrohistory (PDF pp. 40-44), complete, verbatim reasons

Columns: BVX crisis year | Bordo et al. (2001) | Reinhart & Rogoff (2009) | Laeven & Valencia (2018) | Macrohistory Database | Reason. Legend as in Section 4 (Y = identified, X = not identified, – = no data, Y(yyyy) = identified in year yyyy).

| Country | BVX year | Bordo | R&R | L&V | JST | Reason (verbatim) |
|---|---|---|---|---|---|---|
| Belgium | 1914 | Y | Y | – | X | Bank stock prices collapsed due to the beginning of the First World War. |
| Belgium | 2011 | – | – | Y(2008) | Y(2008) | Crisis is linked to the financial crisis of 2008. |
| Canada | 1873 | – | Y | – | X | Despite a small reference in Conant (1915, p. 459), we will not code this year due to a lack of more detailed narrative evidence. |
| Canada | 1920 | Y (1923) | Y (1923) | – | X | We did not find narrative evidence for banking problems during 1920 only for 1923. However, in 1923, the failure of the Home Bank, due to fraud, was notable but isolated. No panic and no public support (Grossman, 2010, p. 301). |
| Canada | 1983 | Y | Y | X | X | No banking panic or systemic risks (Caprio & Klingebiel, 2003, p. 15). |
| Switzerland | 1919 | X | Y (1921) | – | X | We did not find any narrative evidence for a (systemic) banking crisis in Switzerland during 1919. |
| Germany | 1925 | X | Y | – | X | We did not find any narrative evidence for a (systemic) banking crisis in Germany during 1925. |
| Denmark | 1992 | Y | Y | X | X | We have coded the year 1987 since this crisis stretched over several years (Abildgren et al., 2011, p. 6). |
| Denmark | 2011 | – | – | X | X | No banking panic or systemic risks. |
| Spain | 2010 | – | Y | Y(2008) | Y(2008) | Crisis is linked to the financial crisis of 2008. |
| France | 1914 | X | Y | – | X | Bank stock prices collapsed due to the beginning of the First World War. |
| France | 1994 | Y | Y | X | X | Insolvency problems at Credit Lyonnais; no banking panic or systemic risks (Caprio & Klingebiel, 2003, p. 15). |
| United Kingdom | 1878 | – | X | – | X | No extensive bank failures in 1878. The business of individual banks suffered a major blow but the great majority survived the immediate pressure (Collins, 1989). |
| United Kingdom | 1914 | X | Y | – | X | Bank stock prices collapsed due to the beginning of the First World War. |
| Italy | 1914 | Y | Y | – | X | Bank stock prices collapsed due to the beginning of the First World War. |
| Italy | 2011 | – | – | X | X | Despite an increase in financial stress, there was no systemic crisis. |
| Ireland | 2007 | – | – | Y(2008) | Y(2008) | Stock prices for Irish banks started to decrease in 2007 due to increasing mortgage defaults. As part of the global liquidity crisis banks quickly collapsed in 2008. |
| Japan | 1882 | X | X | – | X | The Japanese economy was confronted with a sharp fall in the value of its paper currency and the fragmentation of its banking system. Tamaki (1995, pp. 57-63) identifies the currency system as one of the core problems. |
| Japan | 1922 | X | X | – | Y (1920) | Since bank failures happened three years in a row, we define this as one systemic banking crisis. |
| Japan | 1923 | X | Y | – | X | The Great Kanto earthquake increased the ratio of non-performing loans; however, government intervention postponed the resulting systemic crisis until 1927. |
| Japan | 1990 | X | X | X | X | In 1990, bank share prices slumped sharply, but there was no systemic banking crisis or banking panic. Instead, losses accumulated slowly over the years up to 1997 (Nelson & Tanaka, 2014, pp. 37-41). |
| Japan | 2001 | – | Y | Y (1997) | Y (1997) | We consider this year as part of the systemic banking crisis that started already in 1997. |
| Netherlands | 1907 | X | X | – | X | Borderline banking crisis |
| Netherlands | 1914 | Y | Y | – | X | Bank stock prices collapsed due to the beginning of the First World War. |
| Netherlands | 1931 | X | X | – | X | Substantial write-downs of bank capital, but no major bank suspensions or bank holidays (Grossman, 2010, p. 316). |
| Norway | 1914 | X | Y | – | X | Back [sic] stock prices collapsed due to the beginning of the First World War. |
| Portugal | 2011 | – | – | Y(2008) | Y(2008) | Crisis is linked to the financial crisis of 2008. |
| USA | 1884 | Y | Y | – | X | No public support; crisis was quickly contained by private intervention. |
| USA | 1890 | X | Y | – | X | Crisis was avoided by the intervention of several major private banks. |
| USA | 1990 | Y | Y | X | X | At the beginning of 1989 there were no more systemic dangers arising from the banking system (Laeven & Valencia, 2018). |

That is 30 BVX years in 14 countries that JST does not code as separate crises: 7 are folded into an existing JST episode (BEL 2011, ESP 2010, PRT 2011 -> 2008; IRL 2007 -> 2008; JPN 1922 -> 1920; JPN 2001 -> 1997; DNK 1992 -> 1987) and 23 are rejected outright.

### Other differences stated in the document

- The document contains no explicit list of differences versus Schularick & Taylor (2012) beyond Section 3 (the only changes relative to the previous JST coding are the seven recoded years: +BEL 1876, +JPN 1901; −DEU 1907, −DNK 1931, −NLD 1893, −NLD 1907, −NLD 1939).
- Internal inconsistency: the UK's last crisis is headed **GBR-2007** in the narrative (PDF p. 16) but printed as **2008** in the Section 4 table (PDF p. 33), where Baron et al. are shown as Y (2007). The CSV uses 2007 (the narrative heading); verify against the dataset's crisisJST column.
- Section 5.3 omits Belgium 1939 although the Section 4 table shows it as not identified by Baron et al. (2021).
- Narrative country codes GER, DEN and IRE are used in the headings for Germany, Denmark and Ireland (mapped to DEU, DNK, IRL in the CSV).
- Two narratives (BEL 1925, ITA 1921) cite no source at all.
- The narratives for ESP 1977 and ESP 2008 both state "At its peak, 5.8 percent of all loans were non-performing (Laeven & Valencia, 2018)" — probably a copy-paste; flagged, not corrected.

## (e) Reference list (PDF pp. 45-51), transcribed

1. Abildgren, K., Buchholst, B. V., Qureshi, A., & Staghøj, J. (2011). Real Economic Consequences of Financial Crises. *Danmarks Nationalbank Monetary Review*, 50(3), 2.
2. Aliber, R., & Kindleberger, C. (2015). *Manias, Panics, and Crashes: A History of Financial Crises* (7. ed.). Palgrave Macmillan.
3. Balluck, K., Galiay, A., Ferrara, G., & Hoggarth, G. (2016). *The small bank failures of the early 1990s: another story of boom and bust* (No. 1).
4. Bank of Italy. (2010). *Annual Report 2009. Abridged Version.* Ordinary Meeting of Shareholders. Rome, 31 May 2010.
5. Baron, M., Verner, E., & Xiong, W. (2019). *Salient Crises, Quiet Crises.* Working Paper. (Version: July 2019)
6. Baron, M., Verner, E., & Xiong, W. (2021). Banking Crises Without Panics. *Quarterly Journal of Economics*, 136(1), 51–113.
7. Barrell, R., & Davis, E. P. (2008). The Evolution of the Financial Crisis of 2007—8. *National Institute Economic Review*, 206, 5–14.
8. Bartoletto, S., Chiarini, B., Marzano, E., & Piselli, P. (2018). Banking Crises and Boom-Bust Dynamics: Evidence for Italy (1861-2016). *CESifo Working Papers No. 6972*.
9. Basel Committee on Banking Supervision (Ed.). (2004). *Bank Failures in Mature Economies.* Bank of International Settlements.
10. Basel Committee on Banking Supervision. (2010). *Report and Recommendations of the Cross-border Bank Resolution Group.* Bank For International Settlement.
11. Bernanke, B. S. (2000). *Essays on the Great Depression*. Princeton University Press.
12. Bernanke, B. S., & James, H. (1991). The Gold Standard, Deflation, and Financial Crisis in the Great Depression: An International Comparison. In R. G. Hubbard (Ed.), *Financial Markets and Financial Crises* (pp. 33–68). University of Chicago Press.
13. Betrán, C., & Pons, M. A. (2013). Understanding Spanish Financial crises, 1850-2000: What determined their severity? *Paper presented at European Historical Society Conference*, 6, 7.
14. Betrán, C., Martín-Aceña, P., & Pons, M. A. (2012). Financial crises in Spain: lessons from the last 150 years. *Revista de Historia Económica - Journal of Iberian and Latin American economic History*, 3, 417–446.
15. Betrán, C., Martín-Aceña, P., & Pons, M. A. (2014). 150 Years of Financial Regulation in Spain. What Can We Learn? *Journal of European Economic History*, 43(1-2), 35–82.
16. Bordo, M., Eichengreen, B., Klingebiel, D., & Martinez-Peria, M. S. (2001). Is the Crisis Problem Growing More Severe? *Economic Policy*, 16(32).
17. Branco, A., Sousa, R. M., & Valério, N. (2012). Echoes from the Past: Portuguese Stabilizations of the 1890s and 1920s. *Gabinete de História Económica e Social - Série Documentos de Trabalho No. 47*.
18. Brunnermeier, M. K., & Schnabel, I. (2016). Bubbles and central banks: Historical perspectives. In M. D. Bordo, Ø. Eitrheim, M. Flandreau, & J. F. Qvigstad (Eds.), *Central Banks at a Crossroads: What Can We Learn from History?* (pp. 493–562). Cambridge University Press.
19. Burhop, C. (2008). Finanzinstitutionen als Risikofaktor: Der Zusammenbruch der Leipziger Bank als Problem der Unternehmensverfassung. *Bankhistorisches Archiv*, 34(1), 18.
20. Buyst, E., & Maes, I. (2007). Central Banking in 19th Century Belgium: Was the NBB a Lender of Last Resort? In P. Mooslechner & E. Gnan (Eds.), *Proceedings of the 2nd Conference of the South-Eastern European Monetary History Network* (pp. 118–144). Österreichische Nationalbank.
21. Buyst, E., & Maes, I. (2009). Financial Crisis and Regulation - An Overview of the Belgian Experience. In A. Gigliobianco & G. Toniolo (Eds.), *Proceedings of the workshop on Financial Market Regulation in the Wake of Financial Crises: The Historical Experience* (pp. 95–117). Bank of Italy.
22. Calomiris, C., & Haber, S. H. (2014). *Fragile by design: The political origins of banking crises and scarce credit* (1st ed.). Princeton University Press.
23. Caprio, G., & Klingebiel, D. (2003). Episodes of Systemic and Borderline Financial Crises. *World Bank Discussion Papers*, 428, 31–49.
24. Carlson, M. (2005). Causes of Bank Suspensions in the Panic of 1893. *Explorations in Economic History*, 42(1), 56–80.
25. Cecchetti, S., & Schoenholtz, K. (2017). *The financial crisis, ten years on.* VOX CEPR Policy Portal.
26. Centonze, A. L. (2014). The Irish Banking Crisis. *The Review of Business and Finance Studies*, 5(2), 85–108.
27. Collins, M. (1989). The banking crisis of 1878. *The Economic History Review*, 42(4), 504–527.
28. Committee of the Causes of the Financial Crisis. (2013). *The Financial Crisis in Denmark – Causes, Consequences and Lessons.* Ministry of Industry, Business and Financial Affairs, Denmark.
29. Conant, C. A. (1915). *A History of Modern Banks of Issue*. G.P. Putnam's Sons.
30. Eichengreen, B., & Temin, P. (2000). *The Gold Standard and the Great Depression.* Contemporary European History. Cambridge University Press.
31. Englund, P., & Vihriälä, V. (2009). Financial crisis in Finland and Sweden: similar but not quite the same. In L. Jonung, J. Kiander, & P. Vartia (Eds.), *The Great Financial Crisis in Finland and Sweden. The Nordic Experience of Financial Liberalization* (pp. 71–130). Edward Elgar Publishing Limited.
32. European Commission. (2009). *State Aid N 466/2009 – Italy. Prolongation of the recapitalization scheme.*
33. Federal Deposit Insurance Corporation (FDIC). (2017). *Crisis and Response: An FDIC History, 2008–2013.* Washington, DC: FDIC.
34. Feinstein, C. (Ed.). (1995). *Banking, Currency, and Finance in Europe between the Wars.* Clarendon Press, Oxford.
35. Fischer, A. (2013). Die Bankenkrise von 1931. Anstoß zur staatlichen Bankenregulierung. In D. Lindenlaub, C. Burhop, J. Scholtyseck, et al. (Eds.), *Schlüsselereignisse der deutschen Bankengeschichte* (pp. 257–269). Franz Steiner Verlag, Stuttgart.
36. Fisher, C., & Kent, C. (1999). Two Depressions, One Banking Collapse. *Reserve Bank of Australia. Research Discussion Paper 1999-06*.
37. Fratianni, M., & Spinelli, F. (1997). *A Monetary History of Italy*. Cambridge University Press.
38. Friedman, M., & Schwartz, A. J. (1963). *A Monetary History of the United States: 1867 – 1960*. Princeton, N. J.: Princeton University Press.
39. Gerdrup, K. R. (2003). Three episodes of financial fragility in Norway since the 1890s. *BIS Working Paper No. 142*.
40. Giddey, T. (2014). La surveillance bancaire belge de 1935 façonnée sur le modèle suisse: un discret transfert de politique publique? *Revue belge de Philologie et d'Histoire*, 92(4), 1211–1243.
41. Giddey, T. (2017). Évolution de la pratique de la Commission bancaire (1935-1975). *Courrier hebdomadaire du Centre de recherche et d'information socio-politiques*(34), 5–58.
42. Gigliobianco, A., & Giordano, C. (2010). Economic Theory and Banking Regulation: The Italian Case (1861 – 1930s). *Bank of Italy Economic History Working Papers*(5).
43. Gigliobianco, A., Giordano, C., & Toniolo, G. (2009). Innovation and Regulation in the Wake of Financial Crises in Italy (1880s-1930s). In A. Gigliobianco & G. Toniolo (Eds.), *Proceedings of the workshop on Financial Market Regulation in the Wake of Financial Crises: The Historical Experience* (pp. 45–74). Bank of Italy.
44. Gigliobianco, A., & Toniolo, G. (Eds.). (2009). *Proceedings of the workshop on Financial Market Regulation in the Wake of Financial Crises: The Historical Experience.* Bank of Italy.
45. Grossman, R. S. (2010). *Unsettled Account: The Evolution of Banking in the Industrialized World since 1800*. Princeton University Press.
46. Grytten, O. H., & Hunnes, A. (2010). A Chronology of Financial Crises for Norway. *Norwegian School of Economics Discussion Paper No. 13*.
47. Hagberg, T., & Jonung, L. (2009). How costly was the crisis in Finland and Sweden? In L. Jonung, J. Kiander, & P. Vartia (Eds.), *The Great Financial Crisis in Finland and Sweden. The Nordic Experience of Financial Liberalization.* Edward Elgar Publishing Limited.
48. Hansen, P. H. (1991). From Growth to Crisis. The Danish Banking System from 1850 to the Interwar Period. *Scandinavian Economic History Review*, 39(3), 20–40.
49. Hansen, P. H. (2012). *Making Sense of Financial Crisis and Scandal: A Danish Bank Failure in the First Era of Finance Capitalism*. Oxford University Press.
50. Harada, E. (2001). The Japanese Financial Crisis during the 1990s. In Basel Committee on Banking Supervision (Ed.), *Bank Failures in Mature Economies* (pp. 7–14). Bank of International Settlements.
51. Hautcoeur, P., Riva, A., & White, E. N. (2014). Floating a "lifeboat": The Banque de France and the crisis of 1889. *Journal of Monetary Economics*, 65, 104–119.
52. Hellwig, M. (2008). Systemic Risk in the Financial Sector: An Analysis of the Subprime-Mortgage Financial Crisis. *Max Planck Institute for Research on Collective Goods*.
53. Hellwig, M. (2017). Deutschland und die Finanzkrise(n). *Wirtschaftsdienst*, 97(9).
54. Herrala, R. (1999). Banking crises vs. Depositor Crises: The Era of the Finnish Markka, 1865–1998. *Scandinavian Economic History Review*, 47(2), 5–22.
55. Honohan, P. (2019). *Currency, credit and crisis: Central Banking in Ireland and Europe*. Cambridge University Press.
56. Inoue, A., & Yabushita, S. (1993). The Stability of the Japanese Banking System. *Journal of the Japanese and International Economies*, 7, 387–407.
57. Jonker, J., & van Zanden, J. L. (1995). Method in the Madness? Banking Crises between the Wars, and International Comparison. In C. Feinstein (Ed.), *Banking, Currency, and Finance in Europe between the Wars.* Clarendon Press, Oxford.
58. Jonung, L., Kiander, J., & Vartia, P. (2009a). The great financial crisis in Finland and Sweden: the dynamics of boom, bust and recovery, 1985–2000. In L. Jonung, J. Kiander, & P. Vartia (Eds.), *The Great Financial Crisis in Finland and Sweden. The Nordic Experience of Financial Liberalization.* Edward Elgar Publishing Limited.
59. Jonung, L., Kiander, J., & Vartia, P. (Eds.). (2009b). *The Great Financial Crisis in Finland and Sweden. The Nordic Experience of Financial Liberalization.* Edward Elgar Publishing Limited.
60. Jordà, Ò., Knoll, K., Kuvshinov, D., Schularick, M., & Taylor, A. M. (2019). The Rate of Return on Everything, 1870–2015. *The Quarterly Journal of Economics*, 134(3), 1225–1298.
61. Jordà, Ò., Schularick, M., & Taylor, A. M. (2015). Leveraged Bubbles. *Journal of Monetary Economics 76: S1-S20*, 76, 1–20.
62. Kellermann, J. (2009). *'The Financial Crisis in the Netherlands; Measures Taken and Lessons Learned'.* Speech by Joanne Kellermann. Seminar: A New World for Financial Industry? A comparative approach. DeNederlandscheBank.
63. Kelly, M. (2009). The Irish credit bubble. *UCD Centre for Economic Research Working Paper Series, No. WP09/32*.
64. Knutsen, S., & Sjögren, H. (2009). Institutional Clash and Financial Fragility. An Evolutionary Model of Banking Crises. *Munich Personal RePEc Archive Working Papers No. 13133*.
65. Laeven, L., & Valencia, F. (2018). *Systemic Banking Crises Revisited.* IMF Working Paper.
66. Lindenlaub, D., Burhop, C., Scholtyseck, J., et al. (Eds.). (2013). *Schlüsselereignisse der deutschen Bankengeschichte.* Franz Steiner Verlag, Stuttgart.
67. Martín-Aceña, P. (2014). The Savings Banks Crises In Spain: When and How? *Documentos de trabajo de la Asociación Española de Historia Económica*(14), 4.
68. Martín-Aceña, P., & Pons, M. A. (2010). Financial Crises and Financial Reforms in Spain – What Have We Learned? *UC3M Working Papers in Economic History*.
69. Mian, A., & Sufi, A. (2014). *House of Debt. How They (and You) Caused the Great Recession, and How We Can Prevent It from Happening Again*. University of Chicago Press.
70. Mitchener, K. J., & Weidenmier, M. D. (2008). The Baring Crisis and the Great Latin American Meltdown of the 1890s. *The Journal of Economic History*, 462–500.
71. Molin, J. (2009). How has the Riksbank managed the financial crisis? *Sveriges Riksbank Economic Review*, 1.
72. Mommen, A. (1994). *The Belgian economy in the twentieth century*. Routledge.
73. Nelson, B., & Tanaka, M. (2014). Dealing with a banking crisis: what lessons can be learned from Japan's experience? *Bank of England. Quarterly Bulletin*, 54(1), 36.
74. Nordvik, H. W. (1995). Norwegian Banking in the Inter-War Period: A Scandinavian Perspective. In C. Feinstein (Ed.), *Banking, Currency, and Finance in Europe between the Wars.* Clarendon Press, Oxford.
75. Okazaki, T., & Yokoyama, K. (2002). Measuring the Extent and Implications of Director Interlocking in the Pre-war Japanese Banking Industry. *ADBI Research Paper Series No. 39*.
76. Paolera, G. D., & Taylor, A. M. (2001). A Monetary and Financial Wreck: The Baring Crisis, 1890-91. In G. D. Paolera & A. M. Taylor (Eds.), *Straining at the Anchor: The Argentine Currency Board and the Search for Macroeconomic Stability, 1880-1935* (pp. 67–79). University of Chicago Press.
77. Payne, J. E., & Rodgers, M. T. (2014). Was the Panic of 1907 a Global Crisis? Testing the Noyes Hypothesis. *Unpublished manuscript*.
78. Pereira, P. T., & Wemans, L. (2015). Portugal and the Global Financial Crisis - short-sighted politics, deteriorating public finances and the bailout imperative. In J. Wanna, E. A. Lindquist, & J. De Vries (Eds.), *The Global Financial Crisis and Its Budget Impacts in OECD Nations: Fiscal Responses and Future Challenges* (pp. 232–254). Edward Elgar Publishing.
79. Plumpe, W. (2012). *Wirtschaftskrisen: Geschichte und Gegenwart* (2nd ed.). C. H. Beck.
80. Reid, M. (1982). *The Secondary Banking Crisis, 1973-75. Its Causes and Course* (1st ed.). Palgrave Macmillan UK.
81. Reinhart, C. M., & Rogoff, K. S. (2009). *This Time Is Different: Eight Centuries of Financial Folly*. Princeton University Press.
82. Reis, J. (1995). Portuguese Banking in the Inter-War Period. In C. Feinstein (Ed.), *Banking, Currency, and Finance in Europe between the Wars.* Clarendon Press, Oxford.
83. Reis, R. (2013). The Portuguese Slump and Crash and the Euro Crisis. *Brookings Papers on Economic Activity*.
84. Rich, G. (1989). Canadian Banks, Gold, and the Crisis of 1907. *Explorations in Economic History*, 26(2), 135–160.
85. Richardson, G., & Sablik, T. (2015). *Banking Panics of the Gilded Age: 1863–1913.* Federal Reserve History. Retrieved from https://www.federalreservehistory.org/essays/banking_panics_of_the_gilded_age
86. Rodgers, D. (2015). Credit Losses at Australian Banks: 1980-2013. *Reserve Bank of Australia Discussion Papers*.
87. Rudolph, B. (2013). *Die Finanzkrise 2007-09. Schlüsselereignis für die zukünftige Entwicklung des Finanzsystems.* Franz Steiner Verlag, Stuttgart.
88. Sauvy, A. (1969). *The economic crisis of the 1930s in France.* Journal of Contemporary History, Vol. 4, No. 4, The Great Depression (Oct., 1969), pp. 21-35. Sage Publications, Ltd.
89. Schnabel, I. (2004). The German Twin Crisis of 1931. *The Journal of Economic History*, 64(3), 822–871.
90. Schularick, M., & Taylor, A. M. (2013). Credit Booms Gone Bust: Monetary Policy, Leverage Cycles and Financial Crises, 1870-2008. *American Economic Review*, 102(2), 1029-1061. [Note: cited as 2013 throughout the document; the AER volume/pages are those of the 2012 article.]
91. Shin, H. S. (2009). Reflections on Northern Rock: The Bank Run that Heralded the Global Financial Crisis. *Journal of Economic Perspectives*, 23(1).
92. Shin, H. S. (2012). Global Banking Glut and Loan Risk Premium. *IMF Economic Review*, 60(2).
93. Stolz, S. M., & Wedow, M. (2010). Extraordinary measures in extraordinary times – public measures in support of the financial sector in the EU and the United States. *Bundesbank Discussion Paper Series 1: Economic Studies No. 13*.
94. Swiss National Bank. (2009). *Financial Stability Report 2009.* Zürich.
95. Tallman, E. W., & Moen, J. R. (1990). Lessons from the panic of 1907. *Federal Reserve Bank of Atlanta Economic Review*, 75(3), 2–13.
96. Tallman, E. W., & Wicker, E. R. (2009). Banking and Financial Crises in United States History: What Guidance can History Offer Policymakers? *Munich Personal RePEc Archive Working Papers No. 28139*.
97. Tamaki, N. (1995). *Japanese banking: A history, 1859–1959*. Cambridge University Press.
98. Tilly, R. (2013). Der Ruin des Bankhauses Hirschfeld & Wolff und das Börsengesetz von 1896. Aktienspekulationen, Betrüger und staatlicher Anlegerschutz. In D. Lindenlaub, C. Burhop, J. Scholtyseck, et al. (Eds.), *Schlüsselereignisse der deutschen Bankengeschichte.* Franz Steiner Verlag, Stuttgart.
99. Toniolo, G. (1995). Italian Banking, 1919–1936. In C. Feinstein (Ed.), *Banking, Currency, and Finance in Europe between the Wars.* Clarendon Press, Oxford.
100. Vale, B. (2004). The Banking Crisis in Norway. In Basel Committee on Banking Supervision (Ed.), *Bank Failures in Mature Economies* (pp. 15–26). Bank of International Settlements.
101. Vastrup, C. (2009). How did Denmark avoid a banking crisis? In L. Jonung, J. Kiander, & P. Vartia (Eds.), *The Great Financial Crisis in Finland and Sweden. The Nordic Experience of Financial Liberalization.* Edward Elgar Publishing Limited.
102. Vogler, R. (2001). The genesis of Swiss banking secrecy: political and economic environment. *Financial History Review*, 8, 73–84.
103. Wetter, E. (1918). *Bankkrisen und Bankkatastrophen der letzten Jahre in der Schweiz*. Institut Orell Füssli.
104. White, E. N. (2007). The Crash of 1882, Counterparty Risk, and the Bailout of the Paris Bourse. *NBER Working Paper Series No. 12933*.
105. Wiggins, R., Tente, N., & Metrick, A. (2014a). European Banking Union C: Cross-Border Resolution–Fortis Group. *Journal of Financial Crises*, 1.
106. Wiggins, R., Tente, N., & Metrick, A. (2014b). European Banking Union D: Cross-Border Resolution—Dexia Group. *Journal of Financial Crises*, 1.
107. Ziegler, S. (2004). The Swiss Case. In Basel Committee on Banking Supervision (Ed.), *Bank Failures in Mature Economies* (pp. 43–48). Bank of International Settlements.
108. Zurlinden, M. (2003). Gold Standard, Deflation and Depression: The Swiss Economy during the Great Depression. *Swiss National Bank Quarterly Bulletin*(2).

## (f) Pages that could not be read

None. All 51 PDF pages were rendered and read (three Read calls: pp. 1-20, 21-40, 41-51). Pages 2-3 are the table of contents; page 38 (Section 5.2) and page 29 (Section 3.2) are mostly blank by design. The only legibility caveat is that the comparison tables use check-mark glyphs, transcribed here as "Y".

## CSV conventions used in `jst_crises.csv`

- `year` = the year in the narrative heading (e.g. "AUS-1893"); this is the first (coded) crisis year. `end_year` is blank for every row because the document never states an end year.
- `type` = "systemic banking crisis" for all rows (the document's own label for every coded episode).
- `description` = my paraphrase of the narrative, retaining all named institutions, quantities, policy responses and the document's cross-references to Sections 3 and 5; the document's own wording is kept where a date or claim is ambiguous.
- `sources` = all citations the narrative gives for that episode, in order of appearance (inline citations separated by "; "; the explicit "Sources:" line of the narrative is reproduced verbatim where one exists). Empty for BEL 1925 and ITA 1921, which cite nothing.
- `pages` = PDF pages of the narrative, followed by the PDF page(s) of any Section 3 / Section 5 table that discusses the episode. Every episode also appears in the Section 4 table (PDF pp. 30-35), not repeated per row.
