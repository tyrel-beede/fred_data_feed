# License and attribution for the JST files in this directory

The files `JSTdatasetR6.xlsx`, `jst_r6.csv`, `features.csv`, `coverage.csv`, `crises_indicator.csv`, `crises_chronology.csv`
and the documentation encodings in this directory are derived from the **Jordà-Schularick-Taylor Macrohistory Database,
Release 6 (July 2022)**, http://www.macrohistory.net/data, consulted 2026-11-04.

The database is distributed under a **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
(CC BY-NC-SA 4.0)**. Its terms of use grant every user a license to use and/or share the material, in whole or in part,
for non-commercial purposes, provided the dataset is properly attributed and cited, and provided it is shared only under
identical license terms. Commercial data providers may not integrate or resell it. The files listed above are therefore
shared here under the same CC BY-NC-SA 4.0 terms, for non-commercial use.

Required citation (from the documentation):

> Òscar Jordà, Moritz Schularick, and Alan M. Taylor. 2017. Macrofinancial History and the New Business Cycle Facts.
> in NBER Macroeconomics Annual 2016, volume 31, edited by Martin Eichenbaum and Jonathan A. Parker. Chicago:
> University of Chicago Press.

For any use of the asset-price or rate-of-return variables (`eq_tr`, `housing_tr`, `bond_tr`, `bill_rate` and the
related columns), the documentation asks for this citation as well:

> Òscar Jordà, Katharina Knoll, Dmitry Kuvshinov, Moritz Schularick, and Alan M. Taylor. 2019. "The Rate of Return on
> Everything, 1870–2015." Quarterly Journal of Economics 134(3): 1225–1298.

(The documentation's own wording of that citation predates publication and reads "Quarterly Journal of Economics. Forthcoming."; the published reference is given above.)

The house-price series (`hpnom`) rest on Knoll, Schularick and Steger (2017), "No Price Like Home: Global House Prices,
1870–2012," American Economic Review 107(2): 331–353.

The authors advise stating the date the database was consulted, because statistics are revised between releases:
**consulted 2026-11-04, Release 6.** Nothing in this directory alters a JST value; derived files are labeled derived and
say how they were computed (`../tools/jst_build.py`).
