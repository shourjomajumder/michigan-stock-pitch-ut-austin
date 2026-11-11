# Agent 07: ORD (new) and SJU (re-test)
Source: Google Flights, one-way, 1 adult, economy, nonstop, NYC (all airports). Searched 2026-11-11 in Browser 1. Each page's date field was checked against the target date. Fare products were not shown in the list. Carry-on flags: JetBlue 1/0, United 0/0.

## ORD (Chicago O'Hare): NO DATA
- JetBlue: no nonstop on any of the 4 dates (zero JetBlue results on every page).
- United lowest: $165 on all 4 dates (2026-12-02, 12-09, 2027-01-13, 01-27), from both LGA and EWR, United Express LGA also $165.
- Gap: n/a. Within ±$10: n/a. Within ±10%: n/a.
- Side note: American and Delta were also at $165, so the route is priced at one flat fare level, but JetBlue does not fly it nonstop.

## SJU (San Juan) re-test: NO MATCH
| Date | JetBlue lowest | United lowest | Gap (B6-UA) | Gap % |
|---|---|---|---|---|
| 2027-02-03 | 99 (EWR) | 194 (EWR) | -95 | -49% |
| 2027-02-10 | 99 (EWR) | 263 (EWR) | -164 | -62% |
| 2027-02-24 | 225 (JFK/EWR) | 225 (EWR) | 0 | 0% |
| 2027-03-03 | 225 (JFK/EWR) | 225 (EWR) | 0 | 0% |
- Median gap -$47.5 (median % -24.5%). Within ±$10: 2/4 (50%). Within ±10%: 2/4 (50%).
- Verdict: NO MATCH. JetBlue undercuts United a lot on early-Feb dates and matches exactly on late Feb and March. This is consistent with the earlier mixed SJU result (Dec 2: +35, Dec 9: -95).
