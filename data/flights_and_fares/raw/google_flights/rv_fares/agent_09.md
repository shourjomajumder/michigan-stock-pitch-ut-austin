# Agent 09: SAV (new) and PHX (re-test)
Source: Google Flights, searched 2026-11-11 in Browser 1. One-way, 1 adult, economy, nonstop only, from all NYC airports. Google did not show fare product names. (x/y) is Google's carry-on / checked-bag icon, the same as in raw.txt: JetBlue 1/0, United 0/0.

## SAV (2026-12-02, 12-09, 2027-01-13, 01-27)
- JetBlue lowest (JFK): 134, 134, none, none (no JetBlue nonstop on the January dates)
- United lowest (EWR): 190, 190, 190, 190
- Gap JetBlue minus United on the 2 dates with both airlines: -56, -56. Median gap -56 (-29%).
- Within +/-$10: 0/2. Within +/-10%: 0/2 (0 of 4 dates).
- Verdict: NO MATCH. JetBlue is $56 cheaper, and it has no nonstop on the January dates. Delta is the low-fare carrier (134).

## PHX re-test (2027-02-03, 02-10, 02-24, 03-03)
- JetBlue lowest (JFK): 169, 169, 199, 199
- United lowest (EWR): 219, 219, 199, 199
- Gap: -50, -50, 0, 0. Median gap -25 (about -11%).
- Within +/-$10: 2/4 (50%). Within +/-10%: 2/4 (50%).
- Verdict: NO MATCH (just misses). The fares match only on the late-Feb and Mar dates. Earlier rounds found United cheaper or within $6 (median +6).
