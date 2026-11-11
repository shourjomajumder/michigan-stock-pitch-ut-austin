# JetBlue vs United on same-airport international pairs

Source: BTS TranStats T-100 International Segment (All Carriers table filtered to UNIQUE_CARRIER B6/UA), CLASS F, both directions, pulled 2026-11-11. Period Aug 2025-Jul 2026 (page: "Latest Available Data: July 2026"). Yearly 2025 and 2026 zips downloaded in-browser (same method as <workspace>/jfk), CLASS F only, both directions summed by (US airport, foreign airport). Months = months with any scheduled traffic.

| pair | group | B6 pax | B6 deps | B6 mo | UA pax | UA deps | UA mo |
|---|---|---:|---:|---:|---:|---:|---:|
| EWR-STI | both>=10k | 127,104 | 906 | 12 | 344,843 | 2,152 | 12 |
| EWR-CUN | both>=10k | 89,432 | 658 | 12 | 366,485 | 2,377 | 12 |
| EWR-PUJ | both>=10k | 96,375 | 650 | 12 | 238,378 | 1,488 | 12 |
| EWR-AUA | both>=10k | 46,848 | 326 | 12 | 248,504 | 1,504 | 12 |
| EWR-SDQ | both>=10k | 39,242 | 291 | 7 | 340,138 | 2,147 | 12 |
| EWR-LHR | requested_ewr | 57 | 1 | 1 | 684,158 | 4,924 | 12 |
| EWR-MBJ | requested_ewr | 0 | 0 | 0 | 111,646 | 693 | 12 |
| EWR-NAS | requested_ewr | 0 | 0 | 0 | 182,741 | 1,328 | 12 |
| JFK-PUJ | requested | 386,552 | 2,511 | 12 | 0 | 0 | 0 |
| JFK-MBJ | requested | 223,368 | 1,411 | 12 | 0 | 0 | 0 |
| JFK-NAS | requested | 143,297 | 1,194 | 12 | 0 | 0 | 0 |
| JFK-LHR | requested | 164,861 | 1,436 | 12 | 0 | 0 | 0 |
| JFK-SDQ | requested | 555,989 | 3,719 | 12 | 0 | 0 | 0 |
| JFK-STI | requested | 670,008 | 4,354 | 12 | 0 | 0 | 0 |
| JFK-CUN | requested | 337,132 | 2,223 | 12 | 0 | 0 | 0 |
| JFK-AUA | requested | 314,809 | 1,970 | 12 | 0 | 0 | 0 |
| BOS-PUJ | requested | 183,259 | 1,233 | 12 | 0 | 0 | 0 |
| BOS-MBJ | requested | 33,345 | 250 | 12 | 0 | 0 | 0 |
| BOS-NAS | requested | 43,235 | 348 | 11 | 0 | 0 | 0 |
| BOS-LHR | requested | 79,082 | 721 | 12 | 138 | 1 | 1 |
| BOS-SDQ | requested | 228,046 | 1,440 | 12 | 212 | 2 | 2 |
| BOS-STI | requested | 158,031 | 1,085 | 12 | 165 | 1 | 1 |
| BOS-CUN | requested | 162,448 | 1,005 | 12 | 0 | 0 | 0 |
| BOS-AUA | requested | 298,700 | 1,882 | 12 | 0 | 0 | 0 |
| LGA-PUJ | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-MBJ | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-NAS | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-LHR | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-SDQ | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-STI | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-CUN | requested | 0 | 0 | 0 | 0 | 0 | 0 |
| LGA-AUA | requested | 0 | 0 | 0 | 0 | 0 | 0 |

Notes:
- Only 5 airport pairs nationwide where both B6 and UA carried >=10k: all EWR to the Caribbean/Mexico (STI, CUN, PUJ, AUA, SDQ). No overlap at BOS, JFK, FLL, MCO, SJU or any UA hub other than EWR.
- EWR-SDQ: JetBlue flew only 7 of 12 months (Aug-Oct 2025, Dec 2025-Jan 2026, Jun-Jul 2026) - seasonal.
- LGA: JetBlue carried zero scheduled international passengers to any of the 8 destinations in the BTS data.
- JFK: United carried zero on all 8; BOS: United only diversion-level (1-2 flights) on LHR/SDQ/STI.
- EWR-LHR B6 57 pax on 1 flight = diversion; JetBlue's London service is JFK/BOS only.
- United's own big flows on these destinations from other hubs (B6 = 0 at those airports): e.g. IAH-CUN 566,347; ORD-CUN 341,956; SFO-LHR 363,000; IAD-PUJ 162,971; ORD-PUJ 117,360 (not overlaps).
- Other B6 origins to these 8 destinations (no UA at same airport): FLL-NAS 222,195; SJU-SDQ 210,536; SJU-PUJ 188,580; FLL-MBJ 187,413; FLL-CUN 172,419; MCO-SDQ 152,567; FLL-PUJ 146,088; FLL-SDQ 131,720; MCO-CUN 118,135; MCO-PUJ 105,269; MCO-STI 96,470; MCO-MBJ 92,985; TPA-CUN 88,437; SJU-STI 71,312; MCO-NAS 60,911; FLL-STI 52,349; TPA-PUJ 33,974; FLL-AUA 28,269.
- JFK figures differ slightly from raw/nyc/intl_raw.txt (different window/pull); this file is the Aug 2025-Jul 2026 pull.
