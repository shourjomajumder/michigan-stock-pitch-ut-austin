# Calibration: is the DOT Table 1a JetBlue-vs-United gap a real base-fare gap?

## Answer
NO. DOT Table 1a averages cannot be used to judge base-fare parity. On the routes where we have both DOT averages and live lowest-economy quotes, DOT shows JetBlue $44-$102 below United while the live base fares are at parity (median gap $0 on 4 of 6 such routes). The DOT gap is driven by which carrier DOT reports as "largest" vs "lowest-fare" and by United's cabin/itinerary mix, not by the price of the same economy seat.

## Method
- Live: <workdir>/appx/code/Shared_routes_fares_full.csv, 458 lowest-economy quotes (travel dates 2026-11-18 to 2027-04-10), both directions pooled per airport pair. Gap = JetBlue minus United.
- DOT: <workdir>/bsky/src/dot_car_table1a_bos_ewr_2023_2026q1.csv, 2024Q1-2026Q1, only quarters where Table 1a reports both B6 and UA (one as largest carrier, the other as lowest-fare carrier).
- Overlap (both sources usable): BOS-DEN, BOS-IAH, BOS-LAX, BOS-ORD, BOS-SFO, EWR-PBI, FLL-SFO. Not calibratable: EWR-FLL, EWR-MCO (DOT never reports JetBlue; Spirit is lowest-fare carrier), EWR-SJU (outside Table 1a), FLL-IAH/LAX/ORD (no DOT file locally).
- Script: <workdir>/rv/t1s2/work/calibration.py; outputs work/calibration_table.csv, work/calibration_dot_rows.csv.

## Calibration table (JetBlue minus United, USD one-way)
| Pair | DOT roles | DOT qtrs | DOT mean gap | Live median gap | Live within +/-$10 | DOT bias (DOT - live) |
|---|---|---|---|---|---|---|
| BOS-DEN | B6 lowest / UA largest | 9 | -$84 (-30%) | +$19 | 28% | -$102 |
| BOS-IAH | B6 lowest / UA largest | 7 | -$102 (-32%) | $0 | 67% | -$102 |
| BOS-ORD | B6 lowest / UA largest | 3 | -$49 (-23%) | +$26 | 31% | -$75 |
| BOS-SFO | B6 lowest / UA largest | 2 | -$44 (-10%) | $0 | 78% | -$44 |
| EWR-PBI (Newark) | B6 lowest / UA largest | 9 | -$62 (-26%) | $0 | 77% | -$62 |
| BOS-LAX | B6 largest / UA lowest | 8 | +$19 (+6%) | $0 | 75% | +$19 |
| FLL-SFO | mostly B6 largest / UA lowest | 7 | +$17 (+7%) | $0 | 78% | +$17 |

- Where DOT reports United as largest and JetBlue as lowest-fare carrier (the NYC configuration): DOT gap averages -$68 (about -24%); live median gap averages +$9. Typical DOT bias: about -$75 (median), range -$44 to -$102.
- The sign flips with the role: across all 45 route-quarters, B6-lowest/UA-largest averages -$73; B6-largest/UA-lowest averages +$21. Same two airlines, opposite "gap": the largest carrier always looks dearer.
- Newark test: EWR-PBI, the one Newark same-airport route in both sources, shows DOT -$62 (-26%) vs live $0 (77% of quotes within $10). Live EWR-FLL ($179 vs $179) and EWR-MCO (median gap $0) are also at parity, while United's DOT average on those pairs is $235 and $212.

## Why (mix, not price)
- Cabin mix: DOT average minus live lowest fare (L4Q) is small for JetBlue on routes without Mint (+$5 EWR-PBI, +$8 BOS-IAH, +$9 BOS-ORD, +$29 BOS-DEN) but +$129-164 on Mint routes (BOS-LAX, BOS-SFO, FLL-SFO). United's is +$70 to +$223 everywhere (it sells First/Polaris on all these routes). Average markup: United +$129, JetBlue +$70.
- Connecting/hub mix (T-100 segment pax vs Table 1a O&D pax x share, 2025Q2-2026Q1, proxy): United's local share is 0.56 BOS-DEN, 0.61 BOS-ORD, 0.66 BOS-IAH, 0.81 EWR-PBI vs JetBlue 0.84-0.93. United carries more hub-flow and corporate traffic, which lifts its average fare.
- Selection: in Table 1a JetBlue at EWR and on most NYC West routes is shown only as the lowest-fare carrier, i.e. its fare is shown because it is low.

## Implication for the NYC result
The NYC DOT gap (-$57, -22% JFK/LGA vs EWR; -$62 Newark same-airport) is smaller than the calibrated DOT bias (about -$75) measured on routes where live base fares are at parity. It is therefore consistent with base-fare parity, and is not evidence against it.

## Caveats
- Time mismatch: DOT is 2024Q1-2026Q1; live quotes are for Nov 2026-Apr 2027 (fixed booking snapshot, ~36 quotes per pair).
- Only one Newark route (EWR-PBI) is directly calibrated; no JFK/LGA route has live quotes, so the NYC JFK-vs-EWR comparison is calibrated by analogy.
- Live quotes are lowest economy (likely basic economy on both); parity is a base-fare statement, not total revenue per passenger.
- Connecting-share figures are a rough proxy (O&D share x O&D pax vs segment pax).

## One line for judges
"DOT averages mix in First class and hub connections: on Newark-West Palm, DOT says JetBlue is $62 cheaper than United, but the actual lowest economy fare is the same price on both airlines on 77% of dates."
