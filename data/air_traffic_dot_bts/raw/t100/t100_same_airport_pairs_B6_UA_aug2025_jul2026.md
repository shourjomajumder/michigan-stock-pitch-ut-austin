# JetBlue vs United passengers on same-airport pairs

Source: BTS TranStats T-100 Domestic Segment (U.S. Carriers), CLASS F, both directions, pulled 2026-11-11. Period Aug 2025-Jul 2026 (latest 12 months; page shows data through July 2026). Scheduled passengers (CLASS F), both directions summed. Extracted in-browser with the (orig workspace) jfk method (yearly 2025 and 2026 zip downloads, carriers B6/UA). Departures shown for context.

| pair | group | B6 pax | B6 deps | UA pax | UA deps |
|---|---|---:|---:|---:|---:|
| FLL-LAX | requested | 484,030 | 3,517 | 162 | 2 |
| FLL-SFO | requested | 208,271 | 1,506 | 147,084 | 980 |
| FLL-IAH | requested | 15,220 | 133 | 463,807 | 3,633 |
| FLL-ORD | requested | 11,024 | 82 | 466,520 | 2,996 |
| FLL-EWR | requested | 276,921 | 1,975 | 769,673 | 5,282 |
| BOS-SFO | focus_x_hub_both>=10k | 464,206 | 3,394 | 579,594 | 3,762 |
| BOS-LAX | focus_x_hub_both>=10k | 462,535 | 3,197 | 224,906 | 1,416 |
| EWR-MCO | focus_x_hub_both>=10k | 379,579 | 2,610 | 1,194,524 | 7,863 |
| EWR-SJU | focus_x_hub_both>=10k | 193,385 | 1,265 | 385,563 | 2,203 |
| BOS-DEN | focus_x_hub_both>=10k | 169,747 | 1,334 | 641,437 | 3,756 |
| BOS-ORD | focus_x_hub_both>=10k | 120,692 | 1,054 | 818,087 | 5,358 |
| BOS-IAH | focus_x_hub_both>=10k | 111,879 | 896 | 450,929 | 3,085 |
| EWR-PBI | other_both>=10k | 189,149 | 1,384 | 754,168 | 5,415 |
| EWR-LAX | other_both>=10k | 133,023 | 968 | 1,400,188 | 6,940 |
| EWR-LAS | other_both>=10k | 77,015 | 604 | 710,531 | 4,821 |
| EWR-RSW | other_both>=10k | 71,183 | 544 | 490,250 | 3,342 |
| EWR-TPA | other_both>=10k | 65,505 | 457 | 710,630 | 4,588 |
| DEN-FLL | focus_x_hub_b6<10k | 5,147 | 42 | 348,300 | 2,391 |
| LAX-MCO | focus_x_hub_b6<10k | 300 | 2 | 247,552 | 1,664 |
| BOS-IAD | focus_x_hub_b6<10k | 250 | 2 | 430,259 | 2,860 |
| BOS-EWR | focus_x_hub_b6<10k | 278 | 2 | 620,154 | 5,244 |
| IAH-MCO | focus_x_hub_b6<10k | 136 | 1 | 735,111 | 4,895 |
| IAD-SJU | focus_x_hub_b6<10k | 130 | 1 | 203,296 | 1,265 |

Notes:
- FLL-LAX: United carried only 162 pax on 2 departures (diversions/one-offs); effectively JetBlue-only.
- FLL-ORD (B6 11,024 on 82 deps) and FLL-IAH (B6 15,220 on 133 deps) clear 10k but JetBlue service is thin/seasonal.
- Focus-city x United-hub pairs where both carried >=10k: FLL-SFO, FLL-EWR, FLL-IAH, FLL-ORD, BOS-SFO, BOS-LAX, BOS-DEN, BOS-ORD, BOS-IAH, EWR-MCO, EWR-SJU. No MCO or SJU pair other than EWR qualifies; nothing at IAD qualifies.
- 'other_both>=10k' = the remaining pairs nationally where both carried >=10k (all EWR-Florida/LAX/LAS; no focus city).
- 'focus_x_hub_b6<10k' = United big routes where JetBlue only has diversion-level traffic; listed for completeness, not overlaps.
