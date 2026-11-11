# Agent 5: JFK transcon fares (JFK-LAX, JFK-SFO), United at EWR

Source: Google Flights (public, no login), searched 2026-11-11. Query form: `https://www.google.com/travel/flights?q=Flights from NYC to {LAX|SFO} on {date} one way nonstop` (business: `... business class`). One-way, 1 adult, Economy (include Basic), nonstop only; lowest of "Best" and "Cheapest" tabs after "more flights". All dates are Wednesdays. No CAPTCHA or block seen. Data: `5_fares.csv`; raw lines `5_work/raw.txt`, `tiers.txt`, `prem.txt`.

Caveats:
- Lowest-fare product: United's lowest is always Basic Economy (no carry-on). JetBlue, Delta, American and Alaska lowest fares all show 1 free carry-on.
- JetBlue OTA prices: on LAX 12-09 ($135), 01-13 ($140), 02-10 ($141) and SFO 12-09 ($136), the JetBlue figure is under $144. On 01-13 I opened the booking page: $140 came from an online travel agency (wego), while JetBlue's own Main Base was $144. On 12-09 the "Best" tab also showed JetBlue at $144. So read these four as about $144 when booking with JetBlue directly (not checked for the other three). Other carriers' figures may include OTA prices too (not checked).
- Alaska: flies JFK-SFO but not JFK-LAX. Its LAX fares are from EWR. Delta also showed EWR-LAX on 04-14 ($199) and 06-16 ($304), which are not in the JFK figures.

### NYC-LAX

| Date | JetBlue JFK | Delta JFK | American JFK | Alaska | United EWR | JFK spread (max-min of B6/DL/AA) | JFK cluster ≤$15 | B6 − UA |
|---|---|---|---|---|---|---|---|---|
| 2026-12-09 | 135 | 169 | 164 | 136 (EWR) | 149 | 34 | no | -14 |
| 2027-01-13 | 140 | 179 | 174 | 229 (EWR) | 149 | 39 | no | -9 |
| 2027-02-10 | 141 | 439 | 174 | 221 (EWR) | 247 | 298 | no | -106 |
| 2027-03-10 | 194 | 214 | 214 | 166 (EWR) | 214 | 20 | no | -20 |
| 2027-04-14 | 194 | 214 | 214 | 186 (EWR) | 214 | 20 | no | -20 |
| 2027-06-16 | 244 | 214 | 214 | 186 (EWR) | 258 | 30 | no | -14 |

Medians: JetBlue 167.5 (n=6); Delta 214 (n=6); American 194 (n=6); Alaska 186 (n=6); United 214 (n=6)
Median gap JetBlue minus: Delta -46.5; American -26.5; Alaska -18.5; United -46.5

### NYC-SFO

| Date | JetBlue JFK | Delta JFK | American JFK | Alaska | United EWR | JFK spread (max-min of B6/DL/AA) | JFK cluster ≤$15 | B6 − UA |
|---|---|---|---|---|---|---|---|---|
| 2026-12-09 | 136 | 149 | 144 | 131 (JFK) | 149 | 13 | yes | -13 |
| 2027-01-13 | 144 | 149 | 144 | 131 (JFK) | 149 | 5 | yes | -5 |
| 2027-02-10 | 144 | 149 | 144 | 143 (JFK) | 149 | 5 | yes | -5 |
| 2027-03-10 | 189 | 194 | 189 | 176 (JFK) | 189 | 5 | yes | +0 |
| 2027-04-14 | 189 | 194 | 189 | 189 (JFK) | 189 | 5 | yes | +0 |
| 2027-06-16 | 214 | 194 | 189 | 189 (JFK) | 221 | 25 | no | -7 |

Medians: JetBlue 166.5 (n=6); Delta 171.5 (n=6); American 166.5 (n=6); Alaska 159.5 (n=6); United 169 (n=6)
Median gap JetBlue minus: Delta -5; American +0; Alaska +7; United -2.5

The "Median gap" lines above are differences between medians. Per-date median gaps (JetBlue minus carrier, median of the 6 dates):

| Route | vs United EWR | vs Delta JFK | vs American JFK | Dates JetBlue within ±$15 of United |
|---|---|---|---|---|
| NYC-LAX | -17 | -27 | -24.5 | 3 of 6 (all at -14 or -9; 6 of 6 have JetBlue at or below United) |
| NYC-SFO | -5 | -5 | 0 | 6 of 6 |

## Do JFK carriers cluster within $15?
- **SFO: yes, on 5 of 6 dates.** JetBlue, Delta and American at JFK were within $5-13 of each other, and United at EWR was within $0-13 of JetBlue. The exception is 06-16 (spread $25: JetBlue $214 vs AA $189). Alaska at JFK matched or undercut the group by $0-18.
- **LAX: no, on all 6 dates (spread $20-298).** Delta and American at JFK were within $5-10 of each other on 5 of 6 dates (excluding Delta's $439 on 02-10). JetBlue sat $20-39 below them from Dec to Apr and $30 above them on 06-16. Even using JetBlue's direct $144 on the 3 OTA dates, the spread is $20-35.

## Fare tiers (booking page, airline direct)
| Route-date | JetBlue lowest / Main | United Basic / Economy | JetBlue Main minus United Economy |
|---|---|---|---|
| JFK/EWR-LAX 2027-01-13 | Main Base 144 / Main 199 | 149 / 214 | -15 |
| JFK/EWR-SFO 2027-06-16 | Main Base 214 / Main 269 | 221 / 286 | -17 |
The upgrade from the lowest fare to the standard tier costs $55 at JetBlue and $65 at United in both cases. Comparing like for like (both with a carry-on), JetBlue is $15-17 cheaper.

## Premium cabins (lowest nonstop business, one-way)
| Route-date | JetBlue Mint (JFK) | United business (EWR) | Delta JFK | American JFK | Alaska | Mint minus United |
|---|---|---|---|---|---|---|
| LAX 2027-01-13 | 988 | 1,224 | 1,599 | 1,899 | 836 (EWR) | -236 |
| LAX 2027-04-14 | 988 | 1,224 | 1,599 (EWR 1,269) | 1,299 | 851 (EWR) | -236 |
| SFO 2027-01-13 | 740 | 1,524 | 1,199 | 1,774 | 696 (JFK) | -784 |
| SFO 2027-04-14 | 1,037 | 1,524 | 1,499 | 1,774 | 834 (JFK) | -487 |
Google shows only "Business"; it does not label United's product as Polaris. Alaska's figure is its premium cabin on that flight.

## Read-across for the United JFK return (my reading of the data)
- On SFO, the JFK carriers and United at EWR already price as one cluster (JetBlue within $0-13 of United on every date). This is consistent with treating JFK-SFO as a "within $15" route if United re-enters at JFK.
- On LAX, JetBlue is the low-price leader at JFK from Dec to Apr: $14-20 below United's Basic Economy and $20-39 below DL/AA. That gap is wider than the 2026-11-11 4-date check found (-5). Matching would need United to price at JetBlue's level at JFK.
- In premium, Mint is $236-784 below United business. Mint passengers are not on fare parity with United.
