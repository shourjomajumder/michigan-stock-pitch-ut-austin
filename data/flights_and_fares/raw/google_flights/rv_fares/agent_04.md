# Agent 04: NYC-JAX (new) and NYC-FLL (re-test)

Source: Google Flights (public), searched 2026-11-11. Nonstop only, one-way, 1 adult, economy, all NYC airports. Gap = JetBlue minus United, using each airline's lowest NYC fare. JAX dates 12-02, 12-09 and 01-13 ran on the first browser. After the connection dropped, JAX 01-27 and all FLL dates ran on Browser 1. No CAPTCHA or blocking.
Fare products: product pages not opened. JetBlue's lowest fares show 1 carry-on; United's lowest show none (likely Basic Economy).

## NYC-JAX (2026-12-02, 12-09, 2027-01-13, 01-27)
- JetBlue lowest (JFK; no JetBlue nonstop shown from other NYC airports): 154, 154, 154, 154
- United lowest (EWR; no United nonstop shown from other NYC airports): 154, 154, 154, 154
- Median gap: $0. Within ±$10: 100%. Within ±10%: 100%.
- Verdict: MATCH. Delta also flies JFK $154 and LGA $254.

## NYC-FLL (R) (2027-02-03, 02-10, 02-24, 03-03)
- JetBlue lowest: 179 (LGA/EWR), 179 (LGA), 179 (LGA/EWR), 179 (LGA/EWR). JetBlue JFK: 184, 184, 229, 229
- United lowest (EWR): 179, 279, 179, 179
- Gaps: 0, -100, 0, 0. Median gap: $0. Within ±$10: 75%. Within ±10%: 75%.
- Verdict: MATCH. The earlier match holds; on 02-10 United EWR was $100 above JetBlue.
- Same airport (JetBlue EWR vs United EWR): 179/179, 254/279, 179/179, 179/179.
- JFK only (JetBlue JFK vs United EWR): +5, -95, +50, +50, so the JFK-only comparison would not match.
