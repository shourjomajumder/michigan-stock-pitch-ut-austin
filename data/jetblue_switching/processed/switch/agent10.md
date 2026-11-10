# Agent 10: Route-level JetBlue (B6) vs United (UA) shares, DOT Consumer Airfare Report Table 6

Source for every number below: US DOT, "Consumer Airfare Report: Table 6 - Contiguous State City-Pair Markets That Average At Least 10 Passengers Per Day", Socrata API https://data.transportation.gov/resource/yj5y-b2ir.json (queried 2026-11-10; latest quarter available = 2026 Q1). Shares are origin-and-destination passenger shares at the city-market level (all airports in a metro combined; e.g. "New York City" = JFK+LGA+EWR, "Miami" = MIA+FLL, Chicago = ORD+MDW, Houston = IAH+HOU). Passengers = average per day, both directions.

Important limitation: Table 6 only reports the LARGEST carrier (carrier_lg, large_ms) and the LOWEST-FARE carrier (carrier_low, lf_ms). A carrier's share is visible only when it holds one of those two slots. "n/a" = not shown. Puerto Rico (EWR/NYC-SJU) is not in Table 6 (contiguous states only): query returned empty. EWR alone cannot be isolated (metro-level data).

Blue Sky start = Jul 2025, so post-period = 2025 Q3, Q4, 2026 Q1. Compare with same quarter a year earlier (seasonality).

## Raw quarterly series (share of city-pair passengers)

### Boston - Denver (both carriers visible every quarter; best series)
| Qtr | Pax/day | UA share | B6 share |
|---|---|---|---|
| 2023Q1 | 1764 | .489 | .155 |
| 2023Q2 | 2228 | .462 | .179 |
| 2023Q3 | 2761 | .408 | .216 |
| 2023Q4 | 2160 | .470 | .180 |
| 2024Q1 | 1760 | .409 | .152 |
| 2024Q2 | 2478 | .437 | .147 |
| 2024Q3 | 2920 | .379 | .207 |
| 2024Q4 | 2327 | .455 | .168 |
| 2025Q1 | 1864 | .445 | .159 |
| 2025Q2 | 2516 | .457 | .166 |
| 2025Q3 | 2784 | .409 | .204 |
| 2025Q4 | 2118 | .464 | .163 |
| 2026Q1 | 1618 | .458 | .153 |
Fares (avg / UA as largest / B6 as low-fare): 2025Q3 $245/$280/$200; 2025Q4 $265/$293/$203; 2026Q1 $248/$275/$193.

### Boston - Houston
| Qtr | Pax/day | UA | B6 |
|---|---|---|---|
| 2023Q1 | 1058 | .562 | .183 |
| 2023Q2 | 1437 | .500 | .225 |
| 2023Q3 | 1550 | .493 | .265 |
| 2023Q4 | 1481 | .563 | .192 |
| 2024Q1 | 1111 | .571 | .185 |
| 2024Q2 | 1719 | .518 | n/a (NK low-fare .135) |
| 2024Q3 | 1642 | .532 | n/a (NK low-fare .131) |
| 2024Q4 | 1589 | .552 | .163 |
| 2025Q1 | 1170 | .580 | .163 |
| 2025Q2 | 1622 | .547 | .226 |
| 2025Q3 | 1532 | .558 | .230 |
| 2025Q4 | 1512 | .589 | .179 |
| 2026Q1 | 1139 | .605 | .131 |
Fares UA/B6: 2025Q3 $321/$202; 2025Q4 $324/$220; 2026Q1 $318/$222.

### Boston - Chicago (UA largest; B6 visible only 2024Q1 = .109)
UA share: 23Q1 .293, 23Q2 .288, 23Q3 .295, 23Q4 .312, 24Q1 .298, 24Q2 .288, 24Q3 n/a (AA largest .284), 24Q4 .313, 25Q1 .320, 25Q2 .326, 25Q3 .316, 25Q4 .342, 26Q1 .364. Pax/day 26Q1 2707.

### Boston - Los Angeles metro (B6 largest; UA mostly low-fare)
| Qtr | Pax/day | B6 | UA |
|---|---|---|---|
| 2023Q1 | 2982 | .323 | .197 |
| 2023Q2 | 3858 | .282 | .173 |
| 2023Q3 | 4252 | .289 | .146 |
| 2023Q4 | 3654 | .351 | .179 |
| 2024Q1 | 2988 | .318 | .201 |
| 2024Q2 | 4010 | .307 | .159 |
| 2024Q3 | 4368 | .323 | n/a |
| 2024Q4 | 4028 | .323 | .189 |
| 2025Q1 | 2836 | .379 | .159 |
| 2025Q2 | 4059 | .338 | .171 |
| 2025Q3 | 3903 | .324 | .157 |
| 2025Q4 | 3514 | .304 | .182 |
| 2026Q1 | 2828 | .271 | .181 |

### Boston - San Francisco metro (patchy)
Largest: 23Q1 UA .347, 23Q2 UA .315, 23Q3 B6 .325, 23Q4 B6 .357, 24Q1 UA .339 (B6 low-fare .315), 24Q2 B6 .327, 24Q3 B6 .334, 24Q4 B6 .333, 25Q1 UA .367, 25Q2 UA .311, 25Q3 UA .312, 25Q4 UA .330 (B6 .295), 26Q1 UA .360 (B6 .313).
B6 was the largest carrier in 5 of 6 quarters 23Q3-24Q4; UA has been largest every quarter since 25Q1 (i.e. the flip predates Blue Sky).

### Miami metro (incl. FLL) - San Francisco metro
UA: 23Q2 .269 (low-fare), 23Q3 .200, 24Q1 .328, 24Q2 .315, 24Q3 .260, 24Q4 .337, 25Q1 .377, 25Q2 .359, 25Q3 .292, 25Q4 .373, 26Q1 .426.
B6: 23Q4 .242, 24Q1 .272, 24Q2 .305, 25Q1 .207, 26Q1 .193.

### New York metro - Orlando (B6 largest; UA not visible)
B6: 23Q1 .368, 23Q2 .391, 23Q3 .399, 23Q4 .402, 24Q1 .349, 24Q2 .361, 24Q3 .404, 24Q4 .355, 25Q1 .333, 25Q2 .374, 25Q3 .356, 25Q4 .330, 26Q1 .270. Pax/day ~12,100-13,300.

### Miami metro (incl. FLL) - New York metro (UA not visible)
B6 largest through 25Q2: .308, .304, .270, .269, .256, .255, .256, .256, .245, .255. From 25Q3 DL is largest (.251, .244, .256), so B6 is at or below those levels (exact B6 share not shown).

## Year-over-year changes, post-Blue Sky (pts of share; same quarter prior year)
| Route | Carrier | 25Q3 | 25Q4 | 26Q1 | Pre-period (25Q1, 25Q2 YoY) |
|---|---|---|---|---|---|
| BOS-DEN | B6 | -0.3 | -0.5 | -0.6 | +0.7, +1.9 |
| BOS-DEN | UA | +3.0 | +0.9 | +1.3 | +3.6, +2.0 |
| BOS-HOU | B6 | n/a | +1.6 | -3.2 | -2.2, n/a |
| BOS-HOU | UA | +2.6 | +3.7 | +2.5 | +0.9, +2.9 |
| BOS-ORD | UA | n/a | +2.9 | +4.4 | +2.2, +3.8 |
| BOS-LAX | B6 | +0.1 | -1.9 | -10.8 | +6.1, +3.1 |
| BOS-LAX | UA | n/a | -0.7 | +2.2 | -4.2, +1.2 |
| BOS-SFO | UA | n/a | n/a | -0.7 | +2.8, n/a |
| MIA-SFO | UA | +3.2 | +3.6 | +4.9 | +4.9, +4.4 |
| MIA-SFO | B6 | n/a | n/a | -1.4 | -6.5, n/a |
| NYC-MCO | B6 | -4.8 | -2.5 | -6.3 | -1.6, +1.3 |

Relative JetBlue share loss (pts lost / prior share), 26Q1 YoY: BOS-DEN -3.8%; BOS-HOU -19.6%; BOS-LAX -28.5%; MIA-SFO -6.8%; NYC-MCO -18.9%.

## Interpretation (my own calculations, not from a source)
- Cleanest route (BOS-DEN, both carriers every quarter): B6 lost only 0.3-0.6 pts (2-4% of its share) in the three post-Blue Sky quarters, while UA gained 0.9-3.0 pts. Implies switching well BELOW 10%.
- United was already gaining share on its hub routes before Jul 2025 (25Q1/25Q2 YoY gains of +0.9 to +4.9 pts on DEN, HOU, ORD, MIA-SFO). Post-period UA gains are similar in size, not clearly accelerated, so a diff-in-diff attribution to Blue Sky is weak.
- Larger B6 drops in 26Q1 (BOS-HOU -3.2, BOS-LAX -10.8, NYC-MCO -6.3 pts) would imply 19-29% relative loss (ABOVE 10%), but these coincide with JetBlue's own capacity cuts/network changes and with BOS-LAX UA gaining only +2.2 pts, so most of that loss is not going to United. Treat as an upper bound, not a switching rate.
- Fare gap persists: on BOS-DEN and BOS-HOU, UA's average fare is $75-$100 above B6's (Q3 2025-Q1 2026), so the "same price" premise is not supported at the route-average level (averages mix fare classes).
- Upshot: route data supports a low-single-digit switching rate in the first 3 quarters (roughly 2-6% of B6 shared-route share), with 10% plausible only as a 1-2 year cumulative figure or on routes where B6 also cuts capacity.

## Not obtained
- BTS T-100 and airport (Massport/PANYNJ/Broward) carrier-level reports: data.transportation.gov reachable only via WebFetch; did not get to these within budget. No searches used.
- EWR-SJU / NYC-SJU: not in Table 6 (Puerto Rico excluded).
