# 5. Natural experiments: do NYC flyers switch between EWR and JFK/LGA?

Agent 5. Compiled 2026-11-11. Public sources only. Supporting calculation: `5_ewr_2025_shift.csv` (same folder).

## Bottom line
- **Newark 2025 meltdown (Apr-Jun 2025), the cleanest test:** EWR lost about 1.3-1.6M passengers. Port Authority counts show JFK and LGA together gained only about **0.3M above their trend**, so roughly **24% recapture**. In the worst week of May, TSA screening data show about **44% recapture**, almost all of it at LGA. Most travelers who left EWR flew another time, flew from PHL, or did not fly at all; they did not cross to JFK.
- **United leaves JFK (Oct 2015):** customers did **not** fully follow United to Newark. United's president later called the move a mistake and said it lost West Coast and corporate customers. No public share number exists.
- **What this means for the pitch:** the airports are *partial* substitutes, roughly 25-45%, not one market. Counting 100% of the 6.48M JFK passengers will not survive judges' questions. A weight of about 30% does.

---

## Experiment 1: Newark ATC/radar outages and runway 4L-22R closure (Apr 28 - mid-Jun 2025)

### 1a. Port Authority official monthly passengers (best data)
Source: Port Authority 2025 Annual Airport Traffic Report, Section 2.2.2, https://www.panynj.gov/content/dam/airports/statistics/statistics-general-info/annual-atr/ATR_2025.pdf (accessed 2026-11-11).

| Month 2025 | EWR pax / YoY | JFK pax / YoY | LGA pax / YoY |
|---|---|---|---|
| April | 3,868,358 / -6.4% | 5,197,968 / +0.6% | 2,785,536 / -0.4% |
| May | 3,492,550 / **-20.9%** | 5,599,325 / +1.0% | 2,981,490 / -1.2% |
| June | 3,844,039 / -10.5% | 5,694,544 / -0.5% | 2,865,431 / -2.0% |

Both columns are my calculations. The 2024 base is backed out from the YoY figures. "Vs trend" compares each airport to its own background growth: EWR -2.7% (March 2025, before the outage, per Reuters below), JFK -1.0% (full-year 2025), LGA -2.2% (full-year 2025).

| Apr-Jun 2025 | Raw change vs 2024 | Change vs trend |
|---|---|---|
| EWR | -1,638,000 | -1,292,000 |
| JFK | +58,000 | +222,000 |
| LGA | -106,000 | +90,000 |
| **JFK+LGA recapture** | ~0% | **~24% (312k / 1.29M)** |

- May 2025 is the peak month. EWR fell by about 923k passengers, which matches Sherwood's estimate of "roughly 880,000" (https://sherwood.news/business/passenger-volume-at-newark-airport-where-united-is-king-fell-20-in-may, 2025-06-27). JFK and LGA together were up only about 19k raw, or about 142k against trend.
- The full year shows the same picture. Domestic passengers in 2025: EWR down 6.4% (-2.15M), JFK up 0.3% (+94k), LGA down 2.1% (-658k), all from the same Port Authority report. The domestic passengers EWR lost did not show up at JFK.
- Port Authority mid-year release: "first half 2025 vs 2024: EWR -7.3%, JFK -0.2%, LGA -2.4%" (https://airfreight.news/articles/full/port-authority-reports-facility-volumes-for-first-half-of-2025).

### 1b. TSA checkpoint data, worst week of May 2025 (upper bound)
NBC News, about 2025-05-20, https://www.nbcnews.com/news/us-news/fewer-people-flying-newark-airport-this-time-last-year-rcna207942. Average daily travelers, second week of May, 2024 vs 2025:
- EWR: 72,983 to 58,496, which is **-14,487/day (-20%)**
- LGA: 36,367 to 42,037, which is **+5,670/day (+16%)**
- JFK: 96,392 to 97,061, which is **+669/day (+0.7%)**
- Recapture: (5,670 + 669) / 14,487 = **44%**, almost all at LGA. This is one week, and the monthly Port Authority data do not show an LGA surge, so treat it as an upper bound.

### 1c. Booking-intent data
Reuters, 2025-05-23, https://www.ajot.com/news/demand-traffic-falls-at-newark-airport-following-outages:
- Kayak: travelers choosing Newark as their arrival airport fell 19% after April 28.
- Data Appeal: Newark arrivals Apr 28 - May 20 fell about 13% YoY, LGA arrivals rose 5.7%, and JFK traffic fell 7%. Reuters blamed the JFK drop on weaker international demand.
- Kayak's CEO said travelers prefer LaGuardia first, then JFK, then Newark. This preference ordering works *against* JFK-to-EWR switching.

### 1d. What the airlines said
- **United Q2 2025 (2025-07-16):** the Newark disruptions cost $218M and 1.2 points of pre-tax margin. They "drove customer bookaway", and booking volumes have since "normalised". https://aeromorning.com/en/newark-disruptions-cost-united-218-million-in-q2/
- **American CFO Devon May (2025-05-22):** "some amount of book-away from Newark flights over into LaGuardia, JFK", which he called "relatively modest". https://www.nbcnewyork.com/news/business/money-report/american-airlines-cfo-says-some-travelers-are-avoiding-newark-airport/6275312/
- **JetBlue Q2 2025 call (Marty St. George):** customers shifted "temporarily" to alternate airports until the runway reopened. Easter added "almost 1.5 points" to RASM, and Easter plus Newark together were "roughly two points". That implies Newark added about **0.5 pt of revenue, roughly $11M** on Q2 revenue of $2.18B. The transcript is garbled in places. https://www.fool.com/earnings/call-transcripts/2025/08/05/jetblue-jblu-q2-2025-earnings-call-transcript
- **Pitch use:** JetBlue itself admits EWR and JFK are linked markets: customers moved to JetBlue when United failed. But the flow was small (about $11M for JetBlue against about $218M of cost to United) and it reversed by June.

### Caveats on the 24-44% figure
- **It probably understates true willingness to switch:**
  - JFK and LGA are slot-controlled and were already near peak in May, so they could not absorb a surge.
  - Part of EWR's loss was United connecting passengers. They rebook through IAD or ORD, never through JFK, which inflates the denominator.
- **It probably overstates switching in our direction:**
  - The 2025 shock was severe: an unreliable airport, flights cut, and free rebooking.
  - Blue Sky offers only a mild nudge (a better product at equal fare), and it asks travelers to move toward the airport they rank last (Kayak ranking).

## Experiment 2: United leaves JFK and moves p.s. transcons to EWR (Oct 2015)
- United moved all JFK p.s. flights (LAX/SFO) to EWR, with up to 15 daily to LA and 17 to SF. https://crankyflier.com/2015/06/18/united-exits-jfk-consolidates-its-power-at-newark
- Scott Kirby, United president, at a Newark town hall (2017-04-21): "I wish I could roll back the clock and change the decision". United lost West Coast customers who wanted to fly into NYC, not New Jersey. https://skiftstaging.dev/?p=228532
- Kirby (same week): the move "let American Airlines in particular go win a bunch of big corporate accounts". Separately, United's New York share fell from 30% to 26% after the merger; that figure is not attributed to Kirby and does not isolate the JFK exit. https://viewfromthewing.com/2017/04/21/united-says-made-mistake-leaving-new-york-jfk-still-wont-go-back/
- United went back to JFK in 2021. Blue Sky now gives it up to 7 daily JFK slot pairs, from 2027 at the earliest. https://yourmileagemayvary.com/2025/06/05/united-jfk-mistake-jetblue-partnership/
- **Reading:** this is the closest precedent to our thesis: the same carrier, the same product, a different NYC airport. A meaningful share of premium JFK customers *did not follow* United to Newark. I found no public DB1B share figure. A DOT DB1B pull of NYC-LAX/SFO share for 2014 vs 2016 would quantify it, but I did not do it.

## Experiment 3: Delta's JFK/LGA buildup and storm closures
- Nothing quantified turned up quickly.
- Sandy-type closures shut all three airports at once, so they show nothing about substitution.
- Skipped to stay within scope.

---

## Best evidence for the pitch (1-3 bullets)
- When Newark failed in 2025, JetBlue's commercial chief said customers moved to alternate airports and that this lifted JetBlue's Q2 revenue (Easter plus Newark was about 2 pts, so Newark alone was about 0.5 pt, roughly $11M). Management is on record that JFK and EWR compete for the same passengers.
- Against trend, JFK+LGA picked up about 24% of the passengers EWR lost in Apr-Jun 2025 (Port Authority data), and about 44% in the peak week (TSA). Cross-airport switching is real and measurable.
- United paid to get JFK slots back through Blue Sky. That shows United thinks the two airports are separate markets, which also means JFK passengers are reachable only through JetBlue's own JFK and Blue Sky links.

## Evidence against
- Raw Port Authority data show **zero net** gain at JFK/LGA in Apr-Jun 2025 (JFK +58k, LGA -106k, against EWR -1.64M). Full-year EWR domestic fell 2.15M while JFK domestic rose only 94k. Most lost EWR travelers did not switch airports.
- 2015: United's own leadership said customers did not follow it from JFK to EWR and called the exit a mistake. Airport loyalty in NYC is sticky, especially for premium and West Coast travelers.
- Kayak's preference ordering is LGA, then JFK, then EWR. The thesis asks JFK flyers to move toward the least-preferred airport, and with only a mild reason (fare parity plus a better product), not an operational collapse.
- The 2025 effect was "temporary": United bookings "normalised" by July, and JetBlue's lift ended in early June.

## Suggested haircut and why
- Count JFK passengers at about **30%** of Boston-route intensity: 6.48M x 0.30 = **1.94M**. The shared-route base becomes about **4.3M** instead of 8.8M.
  - The central estimate is 24%, from the trend-adjusted Port Authority data.
  - I round it up to 30% for two reasons: the slot constraints and the connecting-passenger dilution both bias the measured number down.
- Show the following range:

| Case | Weight | Basis |
|---|---|---|
| Bear | 0% | Raw Port Authority data; 2015 United experience |
| Base | 30% | |
| Bull | 45% | TSA peak week |

- Avoid 100%. No natural experiment supports it, and United's own JFK history contradicts it.
