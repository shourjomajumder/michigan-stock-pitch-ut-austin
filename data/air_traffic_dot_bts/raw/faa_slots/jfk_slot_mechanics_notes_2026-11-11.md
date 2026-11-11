# Agent 2: JFK slot mechanics under Blue Sky (run Nov 11, 2026)

## Conclusion (read this first)
- **United capacity that is plausible:** 7 daily round trips (RT), which is the contractual cap.
  - **Base:** about **1,200 seats/day each way** (2,400/day both directions, about 0.88M seats/yr). This assumes United's own 2021–22 JFK gauge of 172 seats per departure.
  - **2027 ramp (low):** about 700/day each way if only about 4 RT fly in year one.
  - **Gauge upside:** about 1,600/day each way if United uses its Newark transcon gauge of about 230 seats.
  - Nothing beyond 7 RT is contracted. The "20 pairs" figure is still unverified.
- **JetBlue capacity shrink:**
  - **Gross:** 14 slot movements a day, which is **3.9% of JetBlue's about 360 JFK slots**. In seats that is about 2,200 seats/day, or 0.80M/yr, about **7.4% of JetBlue's domestic JFK seats**.
  - **Net versus today's schedule:** likely **close to zero to small**. JetBlue already has slack: domestic JFK movements are down 17% vs 2019, it has cut several JFK routes, and an FAA waiver lets it park up to 10% of slots through Oct 30, 2027.
  - **JFK–LAX/SFO:** no sign of cuts in the T-100 trend. JetBlue is unlikely to give up transcon frequencies to make room.
  - **Practical read:** United's capacity is an *addition* on JetBlue's best routes. It is not offset by JetBlue shrinking them.

## 1. Deal terms (primary + near-primary)
| Item | Exact figure / quote | Source (date) |
|---|---|---|
| JFK slots | "access to slots at JFK International Airport for up to seven daily round-trip flights" … "out of JFK Terminal 6 to begin as early as 2027" | JetBlue/United release, BusinessWire, Jul 29 2025 https://www.businesswire.com/news/home/20250729944822/en/ |
| Newark | "as part of a net-neutral exchange, JetBlue and United will exchange eight flight timings at Newark" | same |
| DOT | "completed the U.S. Department of Transportation (DOT) review"; no conditions or published DOT decision found | same; LiveandLetsFly Jul 30 2025; Economic Liberties Jul 29 2025 (says DOT issued no press release, and Spirit's complaint led to a comments docket with no deadline) |
| Timing | "beginning in 2027 at the earliest" | ch-aviation, May 30 2025 |
| Consideration | **Not public.** Releases name no payment. VFTW: "we don't know what cash may be changing hands" (May 30 2025). St. George says partner choice was NPV-based: "It all came down to money" (via VFTW, May 30 2025). The only quantified JetBlue benefit is the guided $50M incremental EBIT (prior run, JetBlue IR Jul 29 2025) | https://viewfromthewing.com/?p=227604 |
| Legal form | Under the FAA JFK Order, a carrier "may not buy, sell…" slots except as allowed. It "may enter into a lease or trade… for any consideration", and the FAA must approve in writing beforehand. **Inference:** United's "access" is a lease or trade; JetBlue stays the slot holder. The term is not public | FAA Order extension, 91 FR, Jun 23 2026 (2026-12591) https://www.federalregister.gov/documents/2026/06/23/2026-12591/ |

## 2. JFK slot rules
- **Level 3:** "The FAA has designated JFK as an IATA Level 3 airport consistent with the Worldwide Slot Guidelines" (FR 2024-19034, Aug 23 2024).
- **FAA Order:**
  - Covers 6:00–22:59 ET.
  - Caps scheduled operations at 81 per hour.
  - Requires each slot to be used 80% of the time, or it is withdrawn.
  - The Order "remains effective until October 28, 2028" (2026-12591).
  - **Durability risk (inference):** United's access past Oct 2028 depends on the FAA renewing the Order. In the Spirit-to-JetBlue LGA deal, a transfer beyond the Order's duration needed an exemption (FAA notice 2026-20664, Oct 8 2026).
- **Use-or-lose relief (N90 controller staffing):**
  - Carriers "return up to 10 percent of their slots", covering W26/27 (Oct 25 2026–Mar 27 2027) and S27 (Mar 28–Oct 30 2027).
  - Returns for S27 are due Jan 15 2027.
  - JFK returns are expected at 1300–2259 local.
  - The "FAA will not reallocate the temporarily returned slots at JFK".
  - Source: FAA notice 2026-12593, Jun 23 2026. VFTW (Jun 19 2026) puts the effective threshold at 70% instead of 80%.
- **Port Authority role:**
  - Owns and operates the airport and leases terminals. T6 is a $4.2B private terminal with 10 gates, "nine of which will accommodate widebody aircraft", with the first gates in 2026 (Travel Weekly, undated, 2026 opening).
  - Slot allocation and transfer approval belong to the FAA, not the Port Authority.
  - Gauge is not restricted by slots. A slot is one movement, whatever the aircraft size.

## 3. JetBlue slot base and slack
- **Holdings:** JetBlue had 360 operated JFK slots (22.3%) in Summer 2025, vs Delta 492 (30.5%) and AA 195 (12.1%) (VFTW, Jun 19 2026, citing FAA data).
  - **Assumption S1:** these are daily slot movements (arrivals plus departures), so about 180 RT.
  - 7 RT = 14 slots = **3.9%** of the 360.
- **United's own JFK holding:** United "actually holds 47 slots at New York JFK", "leased permanently to Delta in 2015" (same VFTW). It is not a near-term source of United capacity.
- **Domestic JFK use** (T-100, B6, both directions; `(orig workspace) jfk/src/t100_b6_jfk_vs_system_by_quarter.csv`):
  - 2019: 225.8 movements/day.
  - Last four quarters (2025Q3–26Q2): 188.3/day, **−16.6%**. Seats are −11.8% (12.23M to 10.79M); average 157 seats per departure.
  - Q2 movements per day: 202.6 (2024), 204.1 (2025), 196.3 (2026). July 2026: 188.4/day.
  - Some of the 2019 gap may have moved to international flying, which the domestic T-100 does not show.
- **Routes already cut that free slots:**
  - JFK–ORD ends Oct 25 2026. It ran about 1.5 RT/day (1,098 departures over the last four quarters, `out/jetblue_top25_jfk_routes_full.csv`). Source: deeparrival, citing TPG and Aviation Week.
  - JFK–Belize, Guatemala City and San Pedro Sula: each "1 daily service cancelled" from May 21 2026 to Jan/Feb 2027 (AeroRoutes, Mar 4 2026).
  - Together that is about **4.5 RT/day** freed, before the 10% waiver (up to 36 slots, or 18 RT).
  - JetBlue's June 2026 NY-system seats were −2.9% YoY, and >83% of them were at JFK (Aviation Week, Jun 18 2026).
- **Lightly used slots:** carrier-level usage rates are not public.
  - **Inference:** at least about 4–5 RT of the 7 can come from flying already cut, plus waiver-protected slack.
  - Leasing them to United also protects them once the waiver lapses on Oct 30 2027 and the 80% rule returns.

## 4. Will JetBlue cut JFK–LAX/SFO? (T-100 panel, both directions)
| | 2019 RT/day | Last 4 qtrs RT/day | Q2'25 vs Q2'26 departures | Jul 2026 RT/day |
|---|---|---|---|---|
| JFK–LAX | 10.3 | 9.3 | 1,678 vs 1,679 (flat) | 9.0 |
| JFK–SFO | 5.7 | 5.2 | 1,037 vs 968 (−7%) | 5.3 |

- Seats per departure are 157–160 (A321 with Mint) throughout.
- There is no sign of transcon retrenchment. These are JetBlue's #1 and #5 JFK routes and its highest-fare ones (prior run: $341M and $179M estimated seat revenue).
- **Conclusion:** the slots will come from short-haul or Latin flying, not transcons. JetBlue's capacity on United's likely routes stays the same.

## 5. United aircraft
- **Coastliner A321neo:**
  - 20 Polaris suites and 12 Premium Plus seats. The total seat count is not published.
  - Launches early 2027 on EWR–LAX/SFO and "will likely also figure into" JFK (TPG, Nov 6 2026).
- **2021–22 JFK flying:**
  - 767-300ER at 167 seats (46/22/43/56), per From the Tray Table (Mar 24 2026).
  - Then 757-200; 172 seats per departure average (T-100, `src/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv`).
- **Larger aircraft:**
  - Possible. Slots do not limit gauge, and 9 of the 10 T6 gates take widebodies.
  - United's EWR–LAX/SFO averaged **230 seats per departure** (2025Q3–26Q2 T-100 panel).
  - United's stated premium-transcon direction points to a smaller, premium-heavy gauge, so 230 is an upper case.

## 6. United capacity grid (per day; both directions = 2×; LF 82.5% = UA 2021–22 JFK)
| Case | RT | Seats/dep | Seats/day each way | Seats/yr (both) | Pax/day each way |
|---|---|---|---|---|---|
| 2027 ramp (assump. R1: ~4 RT) | 4 | 172 | 688 | 502k | 568 |
| **Base** | 7 | 172 | **1,204** | **879k** | **993** |
| 767 premium config | 7 | 167 | 1,169 | 853k | 964 |
| Gauge upside (EWR avg) | 7 | 230 | 1,612 | 1,177k | 1,330 |

The base matches the prior run (`(orig workspace) jfk`, 879k seats, 725k pax).

## 7. Open items
- Lease term, price and FAA approval filing: not found publicly.
- JetBlue's 10-K PDF was unreadable through the fetch tool. SEC full-text search was blocked by the proxy.
- The slot-count basis (daily vs other) in the VFTW/FAA figure is unconfirmed (S1).
