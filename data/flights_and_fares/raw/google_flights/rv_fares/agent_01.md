# Agent 01: NYC-RSW (new) and NYC-LAX (re-test)

Source: Google Flights (public), searched 2026-11-11; one-way, 1 adult, economy incl. basic, nonstop, all NYC airports. Gap = JetBlue minus United (each airline's lowest NYC nonstop). Percent gap uses the United fare as the base. Bags: JetBlue lowest fare showed 1 carry-on; United lowest showed none (Basic Economy). Products not opened.

## NYC-RSW

- JetBlue lowest: 2026-12-02 $179 (JFK), 2026-12-09 $179 (JFK), 2027-01-13 $184 (JFK), 2027-01-27 $184 (JFK)
- United lowest: 2026-12-02 $200 (EWR), 2026-12-09 $200 (EWR), 2027-01-13 $200 (EWR), 2027-01-27 $200 (EWR)
- Gaps: [-21, -21, -16, -16]; median gap $-18.5 (-9.2% of median United fare)
- Within ±$10: 0/4 (0%); within ±10%: 2/4 (50%)
- Verdict: **NO MATCH**

## NYC-LAX

- JetBlue lowest: 2027-02-03 $144 (JFK), 2027-02-10 $144 (JFK), 2027-02-24 $194 (JFK), 2027-03-03 $194 (JFK)
- United lowest: 2027-02-03 $149 (EWR), 2027-02-10 $247 (EWR), 2027-02-24 $214 (EWR), 2027-03-03 $214 (EWR)
- Gaps: [-5, -103, -20, -20]; median gap $-20.0 (-9.3% of median United fare)
- Within ±$10: 1/4 (25%); within ±10%: 3/4 (75%)
- Verdict: **MATCH**

## Notes
- RSW: JetBlue JFK cheaper every date ($16-21 below United EWR). United gap is 10.5% on Dec dates, 8.0% on Jan dates, so 2/4 within 10%: borderline NO MATCH. American and Delta LGA undercut both at $119 in December.
- LAX re-test: earlier match (JetBlue $144 vs United $149) held on 02-03 only. On 02-10 United EWR jumped to $247 vs JetBlue $144. 02-24 and 03-03: $194 vs $214 (9.3% under United, but 10.3% if JetBlue is the base). The MATCH is marginal and depends on that convention. JetBlue was cheapest on every date.
- Other carriers per search are in agent_01_notes.txt.
