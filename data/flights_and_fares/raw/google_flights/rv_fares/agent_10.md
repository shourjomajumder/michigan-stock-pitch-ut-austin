# Agent 10: NYC-SLC (new) and NYC-RDU (re-test)

Source: Google Flights (public), searched 2026-11-11, Browser 1. NYC all airports, nonstop, one-way, 1 adult, economy (basic allowed). Gap = JetBlue minus United (each airline's lowest NYC fare). Fare product names were not shown in result labels; the lowest JetBlue fare includes 1 carry-on, the lowest United fare includes 0 (Basic Economy pattern). United Express (Republic) RDU flights were shown at the same price as mainline United and are folded into United@EWR. Only JFK (JetBlue) and EWR (United) had nonstops for these two airlines on these routes.

## NYC-SLC (dates 2026-12-02, 12-09, 2027-01-13, 01-27)
- JetBlue (JFK): 154, 154, 234, 234
- United (EWR): 154, 154, 252, 209
- Gaps: 0, 0, -18, +25; median gap $0
- Within ±$10: 50% (2/4); within ±10%: 75% (3/4) (-18/252 = -7.1%; +25/209 = +12.0%)
- Verdict: MATCH (median 0%, 3 of 4 within 10%), though January fares drift apart
- Note: Delta nonstops from EWR at 159 to 244 and from JFK at 279 to 299

## NYC-RDU re-test (dates 2027-02-03, 02-10, 02-24, 03-03)
- JetBlue (JFK): 144, 144, 164, 164
- United (EWR): 144, 144, 164, 164
- Gaps: 0, 0, 0, 0; median gap $0
- Within ±$10: 100%; within ±10%: 100%
- Verdict: MATCH (holds from the earlier run: 144 vs 144 on all 4 earlier dates)
- Note: American and Delta also price at 144 or 164 (Delta LGA 214 on the late-Feb and March dates), so this looks like market-wide fare matching, not a United-specific match
