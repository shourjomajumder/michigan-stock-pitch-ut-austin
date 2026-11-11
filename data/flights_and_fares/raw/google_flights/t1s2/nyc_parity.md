# NYC fare parity: JetBlue vs United (DOT Table 1a), agent 1

## Method
- Sources: <workdir>/jfk/src/dot_car_table1a_jfk_ewr_2019_2026q1.csv (JFK + 2 EWR pairs) and <workdir>/bsky/src/dot_car_table1a_bos_ewr_2023_2026q1.csv (all EWR pairs + BOS pairs, which adds LGA-BOS). No LGA data exists locally beyond LGA-BOS.
- Window: 2024 Q2 to 2026 Q1 (8 quarters). Most JFK pairs in the JFK file start in 2025 Q2, so they have 4 quarters; LAX, LAS, PHX, SEA, SLC and the EWR pairs have up to 8.
- A carrier's fare is used only when Table 1a names it as largest carrier (fare_lg) or lowest-fare carrier (fare_low). Nothing filled or estimated.
- Pair = JetBlue fare on JFK-X (or LGA-X) vs United fare on EWR-X, same destination, same quarter. Separately: JetBlue EWR-X vs United EWR-X (same airport).
- Gap = JetBlue minus United (USD, average one-way fare). Within +/-$10 counted.
- Script: <workdir>/rv/t1s2/work/nyc_parity.py. Rows: nyc_parity.csv.

## Usable pairs
- JFK/LGA vs EWR: 78 route-quarters, 17 destinations (BOS incl. LGA-BOS, BUF, DEN, FLL, IAH, JAX, LAS, LAX, MCO, ORD, PBI, PHX, RDU, RSW, SEA, SLC, TPA).
- Newark same-airport: 26 route-quarters, 5 destinations (TPA, PBI, RSW, LAS 2026Q1 only, PVD which is ~2 pax/day and should be ignored).
- United at EWR is almost always the largest carrier (fare_lg); JetBlue at JFK is largest on the Florida/East routes and lowest-fare carrier on the West routes; at EWR JetBlue is always lowest-fare carrier.
- Not usable (JetBlue fare never reported or no Table 1a coverage): JFK-SFO, JFK-SAN, JFK-ATL (Delta largest, Alaska/Frontier lowest), EWR-MCO, EWR-FLL, EWR-SJU and all SJU/international routes (outside Table 1a scope), all HPN/ISP and LGA routes except LGA-BOS.

## Results
| Set | Route-quarters | Mean gap | Median gap | Within +/-$10 | Mean gap % of United fare |
|---|---|---|---|---|---|
| JFK/LGA vs EWR | 78 | -$57.43 | -$53.96 | 1 (JFK-LAS 2024Q3, -$9.35) | -22% |
| Newark same airport | 26 | -$62.28 | -$58.08 | 0 | -25% |
| All | 104 | -$58.64 | -$55.16 | 1 | |
| Last 4 quarters only (2025Q2-2026Q1) | 69 | -$63.12 | -$58.84 | 0 | |

Per destination (JFK vs EWR mean gap): BOS -44, BUF -59, DEN -101, FLL -59, IAH -95, JAX -40, LAS -39, LAX -59, MCO -45, ORD -84, PBI -66, PHX -65, RDU -40, RSW -57, SEA -58, SLC -86, TPA -49.
Newark same airport: TPA -42, RSW -62, PBI -63.
Closest routes: LAS (-$9 to -$66; within 10% of United in 3 of 6 quarters) and LAX (-$27 to -$104; within 10% in 4 of 8 quarters, but -$70 and -$104 in the last two quarters).

## Verdict
Fare parity does NOT hold on the New York routes in this data. JetBlue's average fare is below United's on every one of the 104 usable route-quarters, by about $55-60 (roughly 22-25%) at the median, and the gap widened in 2025Q4-2026Q1. Only 1 of 104 route-quarters is within +/-$10. The Boston/FLL "same fare" table cannot be extended to New York with Table 1a.

## Caveats
- Table 1a fares are averages over all cabins and itineraries. United's EWR fare includes hub connecting, business and premium-cabin traffic, so part of the gap is mix, not the price of the same seat. This argues the gap overstates the like-for-like difference, but the data cannot measure by how much.
- Selection: JetBlue on West routes and at EWR is reported only as the lowest-fare carrier, i.e. by construction the cheapest carrier on that pair. Its fare is shown because it is low.
- JFK-X vs EWR-X are different airport pairs (DOT counts them in one NYC city market in Table 1, not in Table 1a).
- Coverage: usable destinations hold about 5.2M of JetBlue's 14.1M JFK passengers (L4Q) and 1.2M of 1.85M EWR passengers in <workdir>/nyc/4_full_overlap.csv; the largest gaps in coverage are SJU, SFO and the Caribbean.
- PVD-EWR rows (~2 pax/day) are noise; excluding them does not change any summary meaningfully.
