# 8. Model: JetBlue passengers and revenue lost on JFK-LAX / JFK-SFO from United's JFK return

Agent 8, run 2026-11-11. Code: `model.py`. Inputs with sources: `model_inputs.json`. Outputs:
- `8_scenarios.csv`: quarterly, 2026Q4-2030Q4, 9 scenarios.
- `8_scenarios_by_route.csv`: same, split by route.
- `8_annual.csv`: annual totals.
- `8_sensitivity.csv`: one-at-a-time changes to the central case.

All inputs came from agents 2, 3, 4, 5 and 7. Nothing is still on a fallback; the $180 fare is shown only as a sensitivity.

## Bottom line
- **Central case (launch Q3 2027, 7 daily round trips at 172 seats):**
  - About **210k JetBlue passengers and $35M of revenue a year by 2029-30**. That is 14.5% of JetBlue's 1.449M passengers on the two routes.
  - **$111M cumulative** from 2026Q4 to 2030Q4.
  - 2027 revenue loss is only $10.6M.
- **Range across all 9 scenarios:** $24-44M a year at run rate. Cumulative is $61M (low capacity, Q1 2028 launch) to $153M (230-seat aircraft, Q2 2027 launch).
- **The capacity effect drives about 76% of the run-rate loss** (159k of 210k passengers). Blue Sky same-airport switching adds about 51k passengers a year once it reaches its 6% cap, about 2 years after launch.
- **The capacity effect is also the least certain input.**
  - With no capacity effect (the 2021-22 JFK-LAX null result), the loss falls to **$8.4M a year** (switching only).
  - With agent 3's per-seat regression estimate, it rises to **$78M a year**.
- **Passenger-base view:** the switching mechanism alone adds about 0.84M passengers to the Thesis 1 base (0.4 × 921k LAX + 0.9 × 528k SFO). At the brief's rule of −$0.138/share per 1M, that is about **−$0.12/share** if counted fully. The capacity effect is outside the reverse-DCF passenger-base framework, so it is reported only in revenue terms.

## Mechanics
1. **(a) Same-airport switching** (incremental to the thesis):
   - Lost passengers = JetBlue route passengers × (fare-parity weight − 10% NY weight) × s(t).
   - s(t) = min(3.1% × years since launch, 6%), measured at mid-quarter.
   - The 10% New York slice is already in the thesis, building from Q4'26, so it is not counted again here. The `memo_thesis_ny10_switch_pax` column shows it for reference only.
2. **(b) Capacity effect:**
   - Lost passengers = United seats × 82.5% load factor × draw factor 0.75 × JetBlue's pre-entry route share (30.5% LAX, 27.7% SFO).
   - That works out to about 0.18 JetBlue passengers per United seat.
   - The launch quarter is at 50% of capacity.
3. **Combining (a) and (b):**
   - The two effects are added, as in the prior run, and capped at 50% of JetBlue's route passengers. The cap never binds.
   - The prior run's A6 Delta-Alaska preference effect is **not** added. It is the same loyalty mechanism as (a), so adding it would double count. It is kept as the `memo_A6_pref_pax_not_added` column.
   - Floor variant: max(a, b) instead of a + b. This assumes switchers simply fill United's fixed seats. It gives $26.6M a year in the central case.
4. **Revenue** = lost passengers × JetBlue's lowest nonstop economy fare. No yield response is modelled; see caveats.

## Assumptions and sources
| # | Input | Value | Source |
|---|---|---|---|
| 1 | JetBlue passengers by quarter (seasonality) | LAX 209k/243k/234k/235k (Q1-Q4); SFO 117k/141k/142k/128k; held flat to 2030 | BTS T-100, 2025Q3-26Q2 (sums 921,049 / 527,561), `raw/jfk/t100_panel...csv` |
| 2 | Route totals and JetBlue share | LAX 3.015M (30.5%); SFO 1.907M (27.7%) | T-100 L4Q, prior run csv1. Agent 7: JetBlue's LAX share was flat at 29-33% from 2019 to 2026 |
| 3 | Switching rate and cap | 3.1%/yr, linear from launch; 6% cap | Brief |
| 4 | NY weight already in the thesis | 10% | Brief. nyc/SYNTHESIS.md argues for 30% (sensitivity) |
| 5 | Fare-parity weight | LAX 0.5, SFO 1.0 | Agent 5, Google Flights 2026-11-11: JetBlue within ±$15 of United EWR on 3 of 6 dates for LAX (median −$17) and 6 of 6 for SFO (median −$5). **ASSUMPTION A8-1:** weight = share of dates at parity |
| 6 | Launch | Q2'27 / Q3'27 / Q1'28 | Task spec. Slots "as early as 2027" (JetBlue/United release, Jul 29 2025); Nocella, Oct 21 2026. Agent 10 puts P(in service by Q3'27) at about 35% |
| 7 | United capacity | Low: 4 RT × 172 seats (502k seats/yr). Base: 7 RT × 172 (879k). High: 7 RT × 230 (1.18M) | Agent 2 (`2_slots.md`): the 7 RT contractual cap; the 2027 ramp of about 4 RT (held through 2030 in the low case); 172 = United's 2021-22 JFK average seats per departure; 230 = United's EWR-LAX/SFO average |
| 8 | Route split | 4 LAX / 3 SFO (low case: 2 / 2) | Prior run A4, roughly in line with market size. Low case is **ASSUMPTION A8-2** |
| 9 | United load factor | 82.5% | United JFK 2021-22, T-100 (agent 2). Agent 3 regression check: 0.80 passengers per seat |
| 10 | Draw factor (1 − leakage) | 0.75 (range 0.5-1.0) | Agent 4 (`4_precedents.md`), 26 precedents. Median rel is 1.03 excluding cases where the incumbent grew; JFK-LAX 2021-22 was about 0. Matches the prior run's A5 base |
| 11 | Launch-quarter ramp | 50% | Prior run A10 (**ASSUMPTION**), based on United's 2021 ramp |
| 12 | Fare | LAX $167.5, SFO $166.5 | Agent 5: JetBlue's lowest nonstop economy fare from JFK, median of 6 dates (Dec 2026-Jun 2027) |
| 13 | JetBlue capacity on LAX/SFO | No change | Agent 2: slots likely come from short-haul or Latin flying; no transcon cuts in T-100. Agent 7: no 2027 JFK change announced |
| 14 | Loss cap | 50% of route passengers | Prior run A12 (**ASSUMPTION**); never binds |

## Results: lost revenue $M (all scenarios)
| Scenario | 2027 | 2028 | 2029 | 2030 | Cum. 26Q4-30Q4 | 2030 lost pax | 2030 floor $M |
|---|---|---|---|---|---|---|---|
| L27Q2_low | 10.8 | 20.6 | 23.5 | 23.6 | 78.4 | 141k | 15.1 |
| L27Q2_base | 18.0 | 32.1 | 35.0 | 35.1 | 120.2 | 210k | 26.6 |
| L27Q2_high | 23.6 | 41.1 | 44.0 | 44.1 | 152.8 | 264k | 35.6 |
| L27Q3_low | 6.3 | 19.5 | 23.2 | 23.6 | 72.5 | 141k | 15.1 |
| **L27Q3_base** | **10.6** | **31.0** | **34.7** | **35.1** | **111.4** | **210k** | **26.6** |
| L27Q3_high | 14.0 | 40.0 | 43.7 | 44.1 | 141.8 | 264k | 35.6 |
| L28Q1_low | 0 | 15.5 | 21.7 | 23.6 | 60.7 | 141k | 15.1 |
| L28Q1_base | 0 | 25.6 | 33.2 | 35.1 | 93.9 | 210k | 26.6 |
| L28Q1_high | 0 | 33.4 | 42.2 | 44.1 | 119.7 | 264k | 35.6 |

- **Split of the 2030 passengers:** switching 50.6k in every scenario. Capacity effect 90k (low), 159k (base), 213k (high).
- **Central case by route, 2030:**
  - LAX: 117k passengers, $19.6M, 12.7% of JetBlue's route passengers.
  - SFO: 93k passengers, $15.5M, 17.6%.
- **Central case by quarter:** $3.5M in 2027Q3, $7.1M in 2027Q4, then rising to about $8.8-8.9M a quarter by 2029.

## Sensitivity (central case L27Q3_base; one change at a time)
| Case | 2027 $M | 2028 $M | 2030 $M | Cum. $M |
|---|---|---|---|---|
| Central | 10.6 | 31.0 | 35.1 | 111.4 |
| Draw factor 0.5 / 1.0 (agent 4 bounds) | 7.3 / 14.0 | 22.2 / 39.9 | 26.2 / 44.0 | 81.5 / 141.4 |
| Agent 3 TWFE: −0.47 JetBlue pax per United seat (95% placebo range −1.07 to +0.13, p = 0.32) | 26.7 | 73.6 | 77.7 | 255.3 |
| No capacity effect (JFK-LAX 2021-22 null; switching only) | 0.5 | 4.4 | 8.4 | 21.5 |
| LAX treated as full fare match | 10.9 | 33.5 | 39.7 | 123.2 |
| NY weight 30% | 10.4 | 29.5 | 32.2 | 104.1 |
| Fares $180 (task fallback) | 11.4 | 33.4 | 37.8 | 120.1 |
| Fares = Table 1a JetBlue all-cabin average ($370 / $340) | 22.7 | 66.4 | 74.9 | 238.1 |
| JetBlue route passengers +3%/yr | 10.6 | 31.4 | 36.3 | 113.8 |
| Overlap floor max(a, b) | 10.1 | 26.6 | 26.6 | 90.0 |

## Caveats
- **The capacity effect is the swing factor, and the history is mixed.**
  - In 2021-22, JFK-LAX showed no JetBlue share loss (agents 3, 4, 10).
  - JFK-SFO's loss came with JetBlue's own seat cut.
  - Agent 3's regression is about 2.5× this model's per-seat draw (0.47 vs about 0.18) and is not robust (8 controls: p = 0.19).
- **Yield, not passengers.** In 2021-22, route fares fell about 6-8% relative to controls while United flew (agents 3 and 10). JetBlue may lose yield across all of its about $242M of route revenue at base fares (1.449M passengers × about $167) instead of losing passengers. This model does not include that effect.
- **Fares.** Lowest economy fares understate the revenue lost if capacity-effect passengers include Mint flyers. The Table 1a all-cabin sensitivity roughly doubles the loss.
  - Mint is $236-784 below United business (agent 5), so Mint flyers are not on fare parity with United.
- **Route use is not certain.** Agent 10 puts 85% on LAX/SFO given a launch, and 60% on LAX/SFO service by the end of 2027. These figures are not probability-weighted here.
- **Durability.** United's access depends on Blue Sky continuing and on the FAA renewing the JFK Order, which expires Oct 28, 2028 (agent 2).
- **No offsets.** Neither of the following is netted out:
  - The undisclosed slot consideration United pays JetBlue.
  - JetBlue's ability to redeploy or refill seats. The prior run's case B assumed 55% EBITDAR flow-through.
