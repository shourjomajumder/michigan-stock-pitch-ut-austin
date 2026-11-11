# 9. Valuation: JetBlue reverse DCF with the 2.316M base and United's JFK return

Agent 9, 2026-11-11. Workbooks: `processed/jfk27/out/<scenario>/JBLU_Model_Valuation.xlsx` (plus `JBLU_numbers.json`, `JBLU_rows.json`). Generator: scratch copy `<tmp>/jfk27gen` of `<workspace>/rv/gen` (original not edited).

## What changed in the model
- Assumptions `pax_ov` (Thesis 1 base) = **2.316M** = same-airport 1.616M + 10% of NYC domestic 0.553M + 10% of NYC international 0.147M. Switching 3.1%/yr from Q4'26, cap 6%, $180 fare, unchanged.
- New **Thesis 2: United JFK return** block (Operating Model): quarterly input row = `lost_rev_M` from `8_scenarios.csv` (Q4'26-Q4'30, blue hardcodes); Thesis 2 revenue = -input x `t2_on`; variable cost saving = 12% (88% flow-through, same as Thesis 1); after the last CSV quarter the row = prior x `persist` (the CSV runs to Q4'30, the last model quarter, so FY2030E carries into the terminal value). Feeds thesis revenue/EBIT, IS, BS/CF, DCF.
- DCF thesis bridge and Summary now show Thesis 1 and Thesis 2 separately; scenario notes updated. Bull/Base/Bear = 0%/100%/150% of (our - consensus), weights 25/50/25 (unchanged).
- Market-implied WACC **12.9491%** unchanged (`implied_wacc.json`, solved on consensus earlier; not re-solved).
- Checks: recalc success, **0 errors** in all 10 workbooks (5,332 formulas); balance check 0 every column; FY2028E adj EBIT = consensus + thesis EBIT (diff 0).
- Note: consensus DCF price is now **$3.9415** (was $3.9400): 12/31/26E cash includes Q4'26 thesis NI, and the smaller base loses less in Q4'26. Bull = consensus price. Downsides below are vs the $3.94 share price.

## Results ($/share; downside vs $3.94)
| Case | Launch | Capacity | T1 switching | T2 JFK | Thesis total | Base price | Downside | Bull | Bear | Weighted target | Weighted downside |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | no JFK | - | -0.320 | 0.000 | -0.320 | 3.62 | -8.1% | 3.94 | 3.46 | 3.66 | -7.1% |
| L27Q2_low | L27Q2 | low | -0.320 | -0.300 | -0.621 | 3.32 | -15.7% | 3.94 | 3.01 | 3.40 | -13.7% |
| L27Q2_base | L27Q2 | base | -0.320 | -0.453 | -0.773 | 3.17 | -19.6% | 3.94 | 2.78 | 3.27 | -17.1% |
| L27Q2_high | L27Q2 | high | -0.320 | -0.571 | -0.891 | 3.05 | -22.6% | 3.94 | 2.60 | 3.16 | -19.8% |
| L27Q3_low | L27Q3 | low | -0.320 | -0.291 | -0.611 | 3.33 | -15.5% | 3.94 | 3.02 | 3.41 | -13.5% |
| L27Q3_base | L27Q3 | base | -0.320 | -0.439 | -0.759 | 3.18 | -19.2% | 3.94 | 2.80 | 3.28 | -16.8% |
| L27Q3_high | L27Q3 | high | -0.320 | -0.554 | -0.874 | 3.07 | -22.1% | 3.94 | 2.63 | 3.18 | -19.4% |
| L28Q1_low | L28Q1 | low | -0.320 | -0.273 | -0.594 | 3.35 | -15.0% | 3.94 | 3.05 | 3.42 | -13.1% |
| L28Q1_base | L28Q1 | base | -0.320 | -0.412 | -0.732 | 3.21 | -18.5% | 3.94 | 2.84 | 3.30 | -16.2% |
| L28Q1_high | L28Q1 | high | -0.320 | -0.520 | -0.840 | 3.10 | -21.3% | 3.94 | 2.68 | 3.21 | -18.6% |

Thesis total = our DCF price - consensus DCF price (interaction/other = 0.000 in every case). Central case (agent 8) = L27Q3_base.

## FY Thesis 2 revenue lost ($mm, FY2026E-FY2030E)
- L27Q2_low: 0.00, -10.75, -20.60, -23.49, -23.55
- L27Q2_base: 0.00, -18.00, -32.13, -35.02, -35.08
- L27Q2_high: 0.00, -23.65, -41.11, -44.01, -44.06
- L27Q3_low: 0.00, -6.26, -19.51, -23.18, -23.55
- L27Q3_base: 0.00, -10.62, -31.04, -34.71, -35.08
- L27Q3_high: 0.00, -14.02, -40.02, -43.69, -44.06
- L28Q1_low: 0.00, 0.00, -15.46, -21.69, -23.55
- L28Q1_base: 0.00, 0.00, -25.57, -33.22, -35.08
- L28Q1_high: 0.00, 0.00, -33.45, -42.20, -44.06

## Read
- No-JFK case at 2.316M: thesis **-$0.32/share**, base $3.62 (-8.1%), weighted $3.66 (-7.1%). Consistent with -$0.138/share per 1M (2.316 x 0.138 = 0.320).
- JFK return adds -$0.27 to -$0.57/share; central L27Q3_base adds -$0.44 for a thesis of **-$0.76**, base $3.18 (-19.2%), weighted $3.28 (-16.8%).
- Caveat (agent 8): about 76% of the JFK loss is the capacity effect, which was near zero on JFK-LAX in 2021-22; switching-only would be about $8.4M/yr by 2030. JFK effect is an ASSUMPTION-heavy add-on, not a sourced company figure.
