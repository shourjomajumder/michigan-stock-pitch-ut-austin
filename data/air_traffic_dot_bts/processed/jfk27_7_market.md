# Agent 7: JFK-LAX / JFK-SFO market by carrier (+ EWR United context), JetBlue 2027 JFK schedule, current frequencies
Run date: Nov 11, 2026. Files: `7_market.csv` (quarterly, by route x carrier), `7_market_build.py`, `7_market_raw.txt` (fresh BTS monthly extracts).

## 1. Data and method
- **Source:** BTS T-100 Domestic Segment (U.S. Carriers), class F (scheduled passenger). Both directions are summed. https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIM&QO_fu146_anzr=Nv4%20Pn44vr45. The page still read "Latest Available Data: July 2026" on Nov 11, 2026.
- **Quarterly panel:** reused `(orig workspace) jfk/src/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv` from the Nov 8 run (same source and vintage).
  - Quarter rows with fewer than 3 departures are dropped.
  - Minor carriers are grouped as OT. On JFK-LAX, OT is mostly Frontier (F9): 67,974 passengers in Aug 2025-Jul 2026. On EWR-LAX, OT is Spirit (NK), which last flew it in Q2 2026.
  - **2020 is not in the panel** (COVID, excluded in the prior run).
  - **2026Q3 = July 2026 only.**
- **Re-verified Nov 11:** I re-downloaded 2025-2026 from BTS. The 2026Q2 and July 2026 cells by carrier match the panel exactly (e.g., B6 JFK-LAX Q2'26: 242,674 passengers / 269,251 seats / 1,679 departures). The fresh pull also adds scheduled departures (`7_market_raw.txt`).
- **CSV columns:** passengers, seats, departures, LF, average daily round trips, passenger and seat share, route totals, B6 passenger and seat share.

## 2. Key figures (T-100)
| Route | Period | Total pax | Route LF | B6 pax share | Carrier shares (pax) |
|---|---|---|---|---|---|
| JFK-LAX | 2019 | 3,596,019 | – | 30.0% | DL 35.5, B6 30.0, AA 20.0, AS 14.5 |
| JFK-LAX | 2025 | 2,912,230 (−19%) | – | 30.4% | DL 45.4, B6 30.4, AA 20.7, OT(F9) 3.5; AS exited |
| JFK-LAX | 2026Q2 | 808,489 | 89.4% | 30.0% | — |
| JFK-LAX | Jul 2026 | 258,215 | 92.0% | 32.3% | — |
| JFK-SFO | 2019 | 1,997,176 | – | 28.7% | DL 36.4, B6 28.7, AS 20.8, AA 14.1 |
| JFK-SFO | 2025 | 1,888,238 (−5%) | – | 27.2% | DL 40.7, B6 27.2, AS 18.8, AA 13.3 |
| JFK-SFO | 2026Q2 | 510,489 | 90.5% | 27.6% | — |
| EWR-LAX | 2025 | 1,843,324 | – | 8.5% | UA 72.6, AS 11.7, B6 8.5, NK 7.2 |
| EWR-SFO | 2025 | 1,742,967 | – | 0% | UA 88.0, AS 12.0 |

- **JetBlue load factors.** JFK-LAX: 89.1% in 2019, 82.7% in 2025. JFK-SFO: 86.9% in 2019, 85.8% in 2025.
- **JetBlue last 12 months (Aug 2025-Jul 2026).** JFK-LAX: 923,776 passengers, 6,750 departures. JFK-SFO: 532,218 passengers. The brief's 921k / 528k use the 2025Q3-2026Q2 window.
- **JetBlue's JFK-LAX share has been flat at 29-33% every quarter from 2019 to 2026.** JFK-SFO has held at 24-30%. Delta took the share that Alaska gave up on JFK-LAX.
- **United precedent (2021-22).** United ran about 1.9 daily round trips per route and took 7.3-7.8% of JFK-LAX and 9.7-13.3% of JFK-SFO (full quarters 2021Q3-2022Q3). Load factor was 70-89%. It exited in Oct 2022 (2022Q4: 0.62 daily round trips).
- **United at Newark (2025).**
  - EWR-LAX: 1.34M passengers, 9.41 daily round trips, 85.5% LF.
  - EWR-SFO: 1.53M passengers, 10.03 daily round trips, 88.5% LF.
  - Both are below 2019 (1.47M / 1.76M passengers).

## 3. Current daily frequencies by carrier
**A. July 2026, T-100 (latest month).** Daily round trips are departures (both directions) ÷ 2 ÷ 31.

| Route | B6 | DL | AA | AS | UA |
|---|---|---|---|---|---|
| JFK-LAX sched / performed | 10.2 / 9.0 | 9.5 / 8.7 | 9.7 / 9.2 | – | – |
| JFK-SFO sched / performed | 5.7 / 5.3 | 6.5 / 5.8 | 4.7 / 4.4 | 3.1 / 2.8 | – |
| EWR-LAX sched / performed | 2.3 / 2.1 | – | – | 1.0 / 0.9 | 9.7 / 9.3 |
| EWR-SFO sched / performed | – | – | – | – (AS gone after Q2'26) | 11.8 / 11.2 |

Note: JetBlue completed only 557 of 634 scheduled JFK-LAX departures in July 2026 (87.9%).

**B. Forward schedule: Google Flights, nonstop one-way departures on Wed Dec 9, 2026 (viewed Nov 11, 2026, no login).**

| Route | B6 | DL | AA | AS | UA | Total |
|---|---|---|---|---|---|---|
| JFK→LAX | 11 | 9 | 10 | 0 | 0 | 30 |
| JFK→SFO | 5 | 6 | 5 | 4 | 0 | 20 |
| EWR→LAX | 0 | 0 | 0 | 3 | 10 | 13 |
| EWR→SFO | 0 | 0 | 0 | 0 | 11 | 11 |

- This is a single weekday and one direction. Google lists flights by operating carrier.
- No JetBlue EWR-LAX flight is listed for Dec 9. FlyMag (below) says the route ends after Jan 4, 2027, so Dec 9 may simply not be operated; this is unverified.
- **ILLUSTRATION (assumption, not announced):** if United used all 7 pairs as 4 JFK-LAX + 3 JFK-SFO, daily departures each way would rise about 13% (30→34) and 15% (20→23).

## 4. JetBlue's announced 2027 JFK schedule changes (press)
- **No 2027 JFK schedule change by JetBlue was found.**
  - Q3 2026 call (Oct 27, 2026; transcript via webull.com/news/15821575681355776): no JFK statement.
  - JetBlue President Marty St. George (the transcript renders him as "Martin J. George"; his title there is not shown) on 2027 capacity: "Now we are not guiding 2027 on this call." He referenced an earlier "low- to mid-single-digits" 2027 guide.
- **Related 2027 item:** JetBlue Newark-LAX is "scheduled to disappear after January 4, 2027". Source: FlyMag, Jun 18, 2026, https://flymag.com/jetblue-trims-newark-transcon-flying-as-fort-lauderdale-mint-growth-accelerates/.
- **Recent JFK changes, all 2026:**
  - JFK-Chicago O'Hare and JFK-Nashville discontinued from Oct 24, 2026.
  - JFK-Vero Beach, JFK-Daytona Beach and JFK-Antigua ended Sept 8, 2026.
  - Summer 2026 JFK departing seats were down almost 5% year on year (OAG).
  - Source: Aviation Week, Jul 16, 2026, https://aviationweek.com/air-transport/airlines-lessors/jetblue-reshapes-network-part-fort-lauderdale-expansion.
  - JFK-Tulum exited Mar 2026 (FlyMag, Jan 7, 2026). JFK-Cleveland daily began Mar 30, 2026 (AirlineGeeks, Dec 30, 2025).
- **United side:** InsideFlyer (Oct 31, 2026) says "The timing and final slot total remain unclear". It also names 757-200/767-300ER aircraft and LAX/SFO routes, and repeats the unsourced "up to 20" slot-pair goal (https://www.insideflyer.com/posts/united-plans-2027-return-to-jfk-with-slot-hunt/). Still no United JFK schedule is filed or announced.

## 5. Caveats
- T-100 counts segment passengers, not O&D. Connecting passengers are included.
- The OT group hides F9/NK detail in quarterly rows. The monthly raw file breaks them out for 2025-26.
- Daily round-trip figures average both directions over calendar days.
