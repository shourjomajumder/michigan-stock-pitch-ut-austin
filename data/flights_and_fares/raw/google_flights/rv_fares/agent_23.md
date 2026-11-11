# Agent 23: same-airport EWR international, JetBlue EWR nonstop vs United EWR nonstop (one-way, lowest economy incl. basic)

Source: Google Flights, searched 2026-11-11, origin EWR only, nonstop filter. Fare product and carry-on not shown in list view (?). Arajet also flies EWR-PUJ/SDQ nonstop (not counted).

## STI

| Date | JetBlue@EWR | United@EWR | Gap (JB-UA) |
|---|---|---|---|
| 2026-12-02 | 323 | 305 | 18 |
| 2026-12-09 | 323 | 354 | -31 |
| 2027-01-13 | 258 | 220 | 38 |
| 2027-01-27 | 141 | 209 | -68 |
| 2027-02-10 | 258 | 303 | -45 |
| 2027-02-24 | 231 | 301 | -70 |

- Gaps: [18, -31, 38, -68, -45, -70]
- Mean gap: -26.3; median: -38.0
- Mean after dropping largest-|gap| date (2027-02-24, -70): -17.6
- Dates within +/-$15: 0/6 (0%)
- Verdict: **NOT WITHIN $15**

## PUJ

| Date | JetBlue@EWR | United@EWR | Gap (JB-UA) |
|---|---|---|---|
| 2026-12-02 | none | 269 | n/a |
| 2026-12-09 | none | 269 | n/a |
| 2027-01-13 | none | 252 | n/a |
| 2027-01-27 | none | 252 | n/a |
| 2027-02-10 | none | 509 | n/a |
| 2027-02-24 | none | 309 | n/a |

- JetBlue has no EWR nonstop on any of the 6 dates (Google shows United only). Verdict: **NO DATA (no JetBlue EWR nonstop)**

## CUN

| Date | JetBlue@EWR | United@EWR | Gap (JB-UA) |
|---|---|---|---|
| 2026-12-02 | none | 332 | n/a |
| 2026-12-09 | none | 221 | n/a |
| 2027-01-13 | none | 254 | n/a |
| 2027-01-27 | none | 221 | n/a |
| 2027-02-10 | none | 376 | n/a |
| 2027-02-24 | none | 249 | n/a |

- JetBlue has no EWR nonstop on any of the 6 dates (Google shows United only). Verdict: **NO DATA (no JetBlue EWR nonstop)**

## AUA

| Date | JetBlue@EWR | United@EWR | Gap (JB-UA) |
|---|---|---|---|
| 2026-12-02 | none | 296 | n/a |
| 2026-12-09 | none | 205 | n/a |
| 2027-01-13 | none | 189 | n/a |
| 2027-01-27 | none | 104 | n/a |
| 2027-02-10 | none | 268 | n/a |
| 2027-02-24 | none | 133 | n/a |

- JetBlue has no EWR nonstop on any of the 6 dates (Google shows United only). Verdict: **NO DATA (no JetBlue EWR nonstop)**

## SDQ

| Date | JetBlue@EWR | United@EWR | Gap (JB-UA) |
|---|---|---|---|
| 2026-12-02 | none | 303 | n/a |
| 2026-12-09 | none | 328 | n/a |
| 2027-01-13 | none | 250 | n/a |
| 2027-01-27 | none | 146 | n/a |
| 2027-02-10 | none | 252 | n/a |
| 2027-02-24 | none | 292 | n/a |

- JetBlue has no EWR nonstop on any of the 6 dates (Google shows United only). Verdict: **NO DATA (no JetBlue EWR nonstop)**

## Other international EWR routes with both carriers nonstop

None found. Probes on 2027-01-13: EWR-POP no nonstops at all; EWR-MBJ United only ($155); EWR-NAS United only ($104). Among the 5 assigned destinations, only STI has a JetBlue EWR nonstop.

## Summary

- STI: mean -26.3, median -38.0, outlier-dropped -17.6, 0% within $15 -> NOT WITHIN $15
- PUJ: NO DATA (no JetBlue EWR nonstop)
- CUN: NO DATA (no JetBlue EWR nonstop)
- AUA: NO DATA (no JetBlue EWR nonstop)
- SDQ: NO DATA (no JetBlue EWR nonstop)
