# Testing the target: is the JST crisis label a good one?

The flag is a narrative judgment dated to the first year of an episode. Four tests against the measured record.

## 1. Do labelled crisis years look different in the measured data?

AUC of each aftermath variable as a detector of a labelled crisis year (oriented so that more stress scores higher; 0.5 = the label is unrelated to the variable):

| aftermath variable (window) | AUC | median, crisis years | median, other years | n crisis / other |
|---|---|---|---|---|
| real_eq_min_t_t1 | 0.71 | -0.153 | -0.009 | 80 / 2139 |
| rgdp_pc_min_growth_t_t2 | 0.70 | -0.030 | +0.001 | 86 / 2510 |
| unemp_max_rise_t_t2 | 0.77 | +2.685 | +0.300 | 52 / 1816 |
| dloans_gdp_min_t_t3 | 0.50 | -0.006 | -0.002 | 76 / 2291 |
| lev_min_change_t_t2 | 0.53 | -0.660 | -0.374 | 77 / 2204 |
| noncore_change_t_t2 | 0.46 | -0.242 | +0.204 | 75 / 2074 |
| ltrate_change_t_t1 | 0.47 | -0.069 | -0.040 | 86 / 2461 |

## 2. Can the label be reproduced from measured stress alone?

**five_condition_3of5** — first year of a run with >= 3 of 5 conditions (real equity <= -20%, real GDP/cap <= -2%, unemployment +1.5 pp, loans/GDP -2 pp, bank capital ratio -0.7 pp); years with fewer than 3 conditions observable are skipped. Events found: 44; labels: 86.

- Precision (measured events with a label within ±1 year): 27%
- Recall (labels with a measured event within ±1 year): 14%

Labelled crises with no measured stress within ±1 year (74): AUS 1893, AUS 1989, BEL 1876, BEL 1885, BEL 1925, BEL 1934, BEL 1939, BEL 2008, CAN 1907, CHE 1910, CHE 1931, CHE 1991, CHE 2008, DEU 1873, DEU 1891, DEU 1901, DEU 2008, DNK 1877, DNK 1885, DNK 1908, DNK 1921, DNK 1987, DNK 2008, ESP 1883, ESP 1890, ESP 1913, ESP 1920, ESP 1924, ESP 1931, ESP 2008, FIN 1877, FIN 1900, FIN 1931, FRA 1882, FRA 1889, FRA 2008, GBR 1890, GBR 1974, GBR 1991, GBR 2007, IRL 2008, ITA 1873, ITA 1887, ITA 1893, ITA 1907, ITA 1930, ITA 1935, ITA 1990, ITA 2008, JPN 1871, JPN 1890, JPN 1901, JPN 1907, JPN 1920, JPN 1927, JPN 1997, NLD 1921, NOR 1899, NOR 1922, NOR 1988, PRT 1890, PRT 1920, PRT 1931, PRT 2008, SWE 1878, SWE 1907, SWE 1922, SWE 1991, SWE 2008, USA 1873, USA 1893, USA 1907, USA 1984, USA 2007

Measured stress with no label within ±1 year (32): AUS 1930, BEL 1942, CAN 1930, CAN 1933, CAN 1982, CHE 1917, CHE 1936, DEU 1919, DNK 1915, DNK 1918, DNK 1940, ESP 1993, ESP 2012, FIN 1915, FIN 1945, ITA 1915, ITA 1943, JPN 1917, JPN 1944, JPN 1974, NLD 1931, NLD 1934, NOR 1920, PRT 1975, PRT 2011, SWE 1918, SWE 1993, USA 1917, USA 1920, USA 1933, USA 2009, USA 2020

**real_economy_2of3** — first year of a run with >= 2 of 3 real-economy conditions (real equity <= -20%, real GDP/cap <= -2%, unemployment +1.5 pp); years with fewer than 2 observable are skipped. Events found: 83; labels: 86.

- Precision (measured events with a label within ±1 year): 28%
- Recall (labels with a measured event within ±1 year): 27%

Labelled crises with no measured stress within ±1 year (63): AUS 1893, AUS 1989, BEL 1876, BEL 1885, BEL 1925, BEL 1934, BEL 1939, BEL 2008, CAN 1907, CHE 1910, CHE 1991, CHE 2008, DEU 1873, DEU 1891, DEU 1931, DEU 2008, DNK 1877, DNK 1885, DNK 1908, DNK 1987, ESP 1883, ESP 1890, ESP 1913, ESP 1920, ESP 1924, FIN 1877, FIN 1900, FIN 1921, FIN 1931, FRA 1882, FRA 1889, GBR 1890, GBR 1974, GBR 1991, GBR 2007, ITA 1873, ITA 1887, ITA 1893, ITA 1907, ITA 1930, ITA 1935, ITA 1990, ITA 2008, JPN 1871, JPN 1890, JPN 1901, JPN 1907, JPN 1920, JPN 1927, JPN 1997, NLD 1921, NLD 2008, NOR 1899, NOR 1988, PRT 1890, PRT 1920, PRT 1931, SWE 1878, SWE 1907, SWE 1991, USA 1873, USA 1984, USA 2007

Measured stress with no label within ±1 year (60): AUS 1915, AUS 1930, AUS 1991, BEL 1917, BEL 1942, CAN 1921, CAN 1930, CAN 1954, CAN 1982, CAN 1991, CAN 2009, CAN 2020, CHE 1917, CHE 1921, CHE 1935, DEU 1914, DEU 1919, DEU 1923, DEU 1929, DNK 1918, DNK 1932, DNK 1940, ESP 1975, ESP 1993, ESP 2012, FIN 1917, FIN 1976, FIN 2009, FRA 1927, FRA 1943, GBR 1892, GBR 1908, GBR 1919, GBR 1931, GBR 2009, ITA 1944, ITA 1970, ITA 2012, JPN 1944, JPN 1974, JPN 2009, NLD 1931, NLD 1941, NOR 1918, PRT 1918, PRT 1975, PRT 2011, SWE 1917, SWE 1993, USA 1904, USA 1914, USA 1917, USA 1920, USA 1938, USA 1946, USA 1954, USA 1958, USA 1982, USA 2009, USA 2020

## 3. Timing

Year of maximum measured stress relative to the label year (t−1 / t / t+1 / t+2 / no stress at all): 18 / 30 / 16 / 11 / 11

## 4. Contestedness across chronologies

From the chronology document's own comparisons: 6 post-1970 JST episodes are absent from Laeven–Valencia; 9 JST episodes are absent from Baron–Verner–Xiong, who in turn date 30 crisis years JST rejects; the authors recoded 7 episodes between releases. 88 labelled episodes; roughly one in ten is contested by at least one other chronology, and the authors themselves recoded seven between releases.

## 5. Predictability from the state (walk-forward, all 45 features, from test2)

| target | AUC |
|---|---|
| crisis_3y | 0.58 |
| stress3_3y | 0.56 |
| dd30_3y | 0.67 |
| credit_contraction_3y | 0.68 |
| unemp_spike_3y | 0.59 |
| gdp_fall_3y | 0.61 |

Horizon curve for the label: 1y 0.54, 2y 0.56, 3y 0.58, 4y 0.51, 5y 0.48
