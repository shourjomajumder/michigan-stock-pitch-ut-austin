# Agent 05: NYC-BQN (new) and NYC-TPA (re-test)

Source: Google Flights (public), searched 2026-11-11, Browser 1. One-way, 1 adult, economy, nonstop, all NYC airports. Gap = JetBlue minus United (each airline's lowest NYC fare). Lowest JetBlue fares show 1 carry-on; lowest United fares show none. Fare product names were not shown.

## NYC-BQN (dates 2026-12-02, 12-09, 2027-01-13, 01-27)
- JetBlue (JFK only): 285, 199, 220, 174
- United (EWR only): 277, 203, 203, 203
- Gaps: +8, -4, +17, -29; median gap +$2
- Within ±$10: 50%; within ±10%: 75%
- Verdict: MATCH (just meets the rule: 3 of 4 dates within 10%; Jan 27 JetBlue $29 cheaper)

## NYC-TPA re-test (dates 2027-02-03, 02-10, 02-24, 03-03)
- JetBlue (JFK only): 179, 179, 184, 184
- United (EWR only): 179, 248, 184, 184 (02-10 also a United EWR fare with a carry-on at 509)
- Gaps: 0, -69, 0, 0; median gap $0
- Within ±$10: 75%; within ±10%: 75%
- Verdict: MATCH (earlier match holds; same pattern as before, with one United outlier date)
