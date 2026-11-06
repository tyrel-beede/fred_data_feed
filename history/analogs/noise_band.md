# The cadence noise band

Base + physical features, era split, refit years shifted by 0, 1, 2, 3 years (4 runs). Each cell: min–max across the runs (range). A like-for-like difference smaller than the range in its column is inside the noise.

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.61–0.61 (0.00) | 0.55–0.60 (0.05) | 0.75–0.77 (0.02) | 0.62–0.64 (0.02) |
| credit_contraction_3y | 0.63–0.63 (0.00) | 0.67–0.70 (0.02) | 0.64–0.69 (0.05) | 0.68–0.70 (0.02) |
| gdp_fall_3y | 0.66–0.66 (0.00) | 0.65–0.68 (0.02) | 0.61–0.63 (0.02) | 0.53–0.55 (0.02) |
| unemp_spike_3y | 0.55–0.55 (0.00) | 0.55–0.60 (0.05) | 0.66–0.68 (0.02) | 0.62–0.63 (0.01) |
| crisis_3y | 0.58–0.58 (0.00) | 0.58–0.59 (0.01) | 0.61–0.63 (0.02) | 0.59–0.60 (0.01) |

## Before 2004 (the window most skill rests on)

| target | knn | logit | gbt | ensemble |
|---|---|---|---|---|
| dd30_3y | 0.55–0.55 (0.00) | 0.54–0.62 (0.07) | 0.71–0.74 (0.03) | 0.66–0.67 (0.02) |
| credit_contraction_3y | 0.60–0.60 (0.00) | 0.64–0.66 (0.02) | 0.61–0.67 (0.06) | 0.66–0.67 (0.01) |
| gdp_fall_3y | 0.67–0.67 (0.00) | 0.70–0.73 (0.03) | 0.61–0.63 (0.02) | 0.51–0.54 (0.02) |
| unemp_spike_3y | 0.52–0.52 (0.00) | 0.52–0.57 (0.05) | 0.62–0.65 (0.03) | 0.58–0.60 (0.02) |
| crisis_3y | 0.64–0.64 (0.00) | 0.59–0.61 (0.01) | 0.61–0.64 (0.03) | 0.59–0.60 (0.01) |

Mean range by learner: knn 0.000, logit 0.031, gbt 0.025, ensemble 0.016.

Reading: a comparison between two feature sets is a finding only where it exceeds the band of the learner it was made with; the trees' band is the tighter one, and the logit's cadence sensitivity is a reason to prefer the trees for any claim about a family's contribution.
