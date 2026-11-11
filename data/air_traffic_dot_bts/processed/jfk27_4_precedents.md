# 4. Precedents: incumbent share loss per point of rival share added (agent 4)

Run date 2026-11-11. Row-level data: `(orig workspace) rv/jfk27/4_precedents.csv`. Scripts: `(orig workspace) rv/jfk27/4_work/` (a_ua_jfk.py, b_t100_annual.py, c2_bos_ewr_entry.py, d_panel_years.py, e_table.py).

## Definitions
- **Ratio** = incumbent share points lost ÷ rival share points added. Positive means the incumbent lost share.
- **Rel (draw factor)** = ratio ÷ the incumbent's pre-entry share.
  - 1.0 means the rival drew from the incumbent in proportion to the incumbent's share.
  - This is the same quantity as "(1 − leakage)" in `(orig workspace) jfk/scenarios.py`. That model's capacity effect is UA pax × (1 − leakage) × B6 share, with leakage 50/25/0%, so its draw factor is 0.5/0.75/1.0.
- **Basis "seat"** means rival seat share from T-100. **Basis "pax"** means rival passenger share from DOT Table 1a or Table 6. Older years have no local seat data, and the proxy is close: on the JFK and EWR transcons in 2019–26, each carrier's passenger share sat within a median 0.4 pt of its seat share (p90 1.0, max 1.6; d_panel_years.py).

## Table

| Case | Route | Years | Rival share added (pts) | Incumbent: pre share → change | Ratio | Rel | Incumbent's own capacity | Source |
|---|---|---|---|---|---|---|---|---|
| United returns to JFK | JFK-SFO | 2019 vs 2021Q3–22Q3 | UA +11.25 (seat) | B6 28.65 → −4.30 | 0.38 | 1.33 | B6 cut its seat share −4.0 | T-100 panel (jfk/src) |
| same, DiD vs 5 B6 control routes (controls +1.66) | JFK-SFO | same | +11.25 | −5.96 | 0.53 | 1.85 | — | same |
| United returns to JFK | JFK-LAX | same | UA +7.85 (seat) | B6 30.01 → +0.41 | −0.05 | −0.17 | B6 held; Alaska exited (−14.5) at the same time | same |
| same, DiD | JFK-LAX | same | +7.85 | −1.25 | 0.16 | 0.53 | — | same |
| Delta JFK transcon build | JFK-LAX | 2010 vs 2019 | DL +14.0 (pax) | AA 30.5 → −10.5 | 0.75 | 2.46 | AA downgauged (A321T: 102 vs 168 seats) | Table 1a + T-100 |
| Delta JFK transcon build | JFK-LAX | 2010H2 vs 2019 | DL +14.0 | B6 13.5 → +16.5 | −1.18 | neg. | B6 grew (Mint) | same |
| Delta JFK transcon build | JFK-SFO | 2010Q1–11Q1 vs 2019 | DL +18.4 (pax) | AA 24.3 → −10.2 | 0.55 | 2.26 | AA downgauged; UA exited 2015 | same |
| Delta JFK transcon build | JFK-SFO | 2011Q3–12 vs 2019 | DL +18.4 | B6 12.8 → +15.9 | −0.86 | neg. | B6 grew | same |
| AA A321T launch (Jan 2014 LAX, Mar 2014 SFO) | JFK-LAX/SFO | 2013–2019 | n/a: AA *cut* seats per departure 168 → 102 | AA was largest on JFK-LAX in 2013 (22–27%); below DL from 2014Q1; 20.0% in 2019 | n/a | n/a | Product upgrade without seats did not hold share | Table 1a; frequentbusinesstraveler.com 2014-01-07 |
| Virgin America enters JFK (2007) | JFK-LAX | 2007H1 vs 2008 | VX +22.75 (pax) | AA 52.0 → −15.75 | 0.69 | 1.33 | unknown; 2008 recession | Table 1a |
| VX + JetBlue enter (approx.) | JFK-SFO | 2007Q1 vs 2008 | ~+43 (pax) | AA 43.0 → −15.7 | 0.37 | 0.86 | unknown | Table 1a |
| Alaska upgauges after the VX merger | JFK-SFO | 2019 vs 2023 | AS +4.7 (seat) | B6 28.7 → −2.0 | 0.43 | 1.50 | B6 seat share −1.0 | T-100 panel |
| Alaska cuts (exit recapture, sign flipped) | JFK-SFO | 2023 vs 2025Q3–26m7 | AS −8.2 (seat) | B6 26.7 → +1.1 | 0.13 | 0.49 | B6 held; DL took +5.2, AA +2.0 | T-100 panel |
| Delta Boston build, full entry | BOS-BUF | 2017Q2 vs 2019Q4 | DL +29.1 (pax) | B6 76.4 → −10.9 | 0.37 | 0.48 | unknown | Table 6 (switch/a10) |
| Delta Boston build, full entry | BOS-PIT | 2017Q3 vs 2019Q4 | DL +31.7 (pax) | B6 57.6 → −2.8 | 0.09 | 0.16 | unknown; DL mostly took AA/US share | same |
| Delta Boston build | BOS-RIC / CHS / PBI | 2014–20 | DL +8.7 / +7.8 / +3.7 | B6 +10.3 / +13.8 / +1.9 | −1.18 / −1.77 / −0.51 | neg. | B6 grew | Table 6 (routes/r04) |
| Delta Boston build | BOS-SFO | 2019 vs 2024 | DL +7.5 (seat) | B6 35.3 → −0.2 | 0.03 | 0.08 | B6 held; UA lost −7.2 (rel 1.7) | T-100 (jfk/t100.csv) |
| Delta Boston build (AA/B6/DL/UA universe only) | BOS-SFO | 2023 vs 2025Q3–26m7 | DL +5.8 (seat) | B6 36.5 → −1.7 | 0.29 | 0.79 | B6 seats +3% | T-100 (bsky/src) |
| Delta Boston, airport level | BOS | 2014/15 vs 2019 | DL departures 15 → 19% | B6 departures 25 → 29% | neg. | neg. | Both grew | travelweekly.com (late 2019) |
| Delta Seattle build | SEA-LAX | 2015Q2 vs 2017Q3 | DL +9.7 (pax) | AS 58.9 → −5.7 | 0.59 | 1.00 | unknown | Table 6 (routes/r05) |
| Delta Seattle build | SEA-SAN | 2017Q3 vs 2019Q3 | DL +13.4 | AS 58.8 → −7.3 | 0.54 | 0.92 | unknown | same |
| Delta Seattle build, near-duopolies | PDX / GEG / BOI / PSC / EUG | 2014–19 | DL +6.9 to +14.1 | AS −6.5 to −14.0 | 0.88–1.01 | 0.95–1.31 | ratio ≈1 holds by identity in a duopoly; BOI partly reversed by 2019 | same |
| Delta Seattle build, no share gained | SMF, DEN, ORD, AUS | 2015–19 | DL ≈0 | AS flat | n/a | n/a | Multi-carrier markets | same |
| Delta Seattle, airport level | SEA | 2015 vs 2019 | DL enplanements 19.3 → 24.4% | AS 51.1 → 49.4% | 0.33 | 0.65 | AS share includes the VX merger | Port of Seattle disclosures (cases/k3_hubs.csv) |
| JetBlue (+Spirit) enter United's EWR hub routes | EWR-LAX | 2019 vs 2022 | B6+NK +20.4 (seat) | UA 82.8 → −18.7 | 0.92 | 1.11 | UA cut seats −15% (abs., COVID) | T-100 panel |
| same | EWR-SFO | 2019 vs 2022 | B6 +5.0 (seat) | UA 85.5 → −3.7 | 0.74 | 0.87 | UA cut seats −17% (abs.) | same |
| United adds seats, Blue Sky period | FLL-SFO | 2023 vs 2025Q3–26m7 | UA +8.1 (seat) | B6 67.4 → −8.8 | 1.09 | 1.62 | B6 seats +1.7% (held) | T-100 (bsky/src) |

## Summary statistics (rows marked clean in the CSV)

| Set | n | Median ratio | Median rel | IQR of rel |
|---|---|---|---|---|
| All rows | 26 | 0.49 | 0.94 | 0.10–1.29 |
| Excluding rows where the incumbent grew its own capacity | 22 | 0.57 | 1.03 | 0.57–1.33 |
| Same, multi-carrier routes only (incumbent below 70%) | 14 | — | 0.96 | 0.24–1.46 |
| NYC airports only (JFK/EWR) | 11 | 0.43 | 1.11 | 0.16–1.42 |
| Rows where the incumbent grew capacity | 4 | −1.18 | negative | — |

## What the precedents say
1. **Share follows seats.** On these routes, passenger share tracks seat share almost one-for-one (median gap 0.4 pt). A rival's added seats therefore cost the incumbent roughly its proportional share (rel ≈ 1). The exception is when the incumbent or a third carrier changes its own capacity.
2. **The incumbent's response sets the outcome.**
   - JetBlue *gained* share against Delta's Boston and JFK buildups wherever it grew too: BOS-RIC/CHS, and JFK transcons with Mint.
   - American lost about 2.3–2.5x proportional at JFK after it downgauged its transcons.
   - Proportional draw only shows up when nobody reacts.
3. **The one direct precedent is mixed.** In 2021–22, United's ~2 daily round trips per route took 11.25 pts of seat share on JFK-SFO, and JetBlue lost 4.3 (rel 1.33, partly its own cut). On JFK-LAX, Alaska's simultaneous exit absorbed United's entry, and JetBlue did not lose share.
4. **Exits recapture less than entries take.** When Alaska cut JFK-SFO in 2023–26, JetBlue won back only rel 0.49, while Delta took most of it. That matches the Newark 2025 "partial substitute" finding in nyc/5.
5. **The listed cases include no clean "United at Newark vs JetBlue Newark" entry.** In 2023–26, United's share gains on EWR routes happen where JetBlue cut more than 15% of its seats (e.g. EWR-LAX: B6 pax share 16.2% in 2023, 7.9% in L4Q). That is incumbent retreat, not rival entry. The reverse case, JetBlue entering United's EWR hub routes in 2021–22, gives rel 0.87–1.11.

## Recommendation for the capacity effect (draw factor)
- **Range: 0.5–1.0 × JetBlue's pre-entry route share per point of United seat share. Point estimate: 0.75.**
- In absolute terms on JFK-LAX (JetBlue 30.5% share): **0.15–0.31 share pts per pt of UA seat share, point 0.23**. On JFK-SFO (27.7%): **0.14–0.28, point 0.21**.
- Why 0.75:
  - Rows where the incumbent did not grow cluster around 1.0. Median 1.03; NYC median 1.11.
  - But JFK-LAX/SFO have 3–4 incumbents, and Delta (44% and 41%) defended in 2021–22 by giving up 4.8 pts on SFO. Multi-carrier, incumbent-held and exit cases sit at 0.3–0.8.
  - JetBlue's JFK capacity is already shrinking (−12% seats vs 2019), which argues against a low (defensive) value.
  - Its only direct test (LAX 2021–22) came out near zero, which argues against 1.0+.
- This **confirms the existing scenarios.py base case** (leakage 25% = draw factor 0.75), and bear 0.5 / bull 1.0 are the right bounds.
  - Use 0.5 for LAX and 1.0 for SFO only if the deck wants route-specific values backed by the 2021–22 test.
- **ASSUMPTION A-4a:** JetBlue holds its own JFK-LAX/SFO seats. If the 7 slot pairs come out of JetBlue's own transcon flying, its share loss is a seat cut and should be modelled separately (not public).
- **ASSUMPTION A-4b:** Delta and American do not add seats in response. If they do, rel rises toward the upper end.

## Corrections to the brief
- **AA's A321T launched on JFK-LAX in January 2014, not 2015.** AA's release is dated 2014-01-07 and says SFO would follow "in March"; FBT (2014-01-07) gives 102 seats vs 168 on the 767. It cut seats per departure, so it is not a rival-capacity case.
- **The 2015 event on JFK-SFO is United's exit (Oct 2015).** Delta went from 22% (2015Q3) to 31–35% (2015Q4–2016) as largest carrier (Table 1a).

## Caveats
- Table 1a and Table 6 show only the largest and lowest-fare carriers, so pre/post windows are picked where both are visible.
- Table 6 is city-pair level.
- Pax share is used as a proxy for seat share before 2019.
- 2021–22 and the EWR rows are COVID-distorted.
- The bsky T-100 file covers only AA/B6/DL/UA, so WN, NK and AS are missing from totals.
- No published study reporting this ratio was found. The academic entry papers (Goolsbee-Syverson, Daraban-Fournier, in switch/a8) measure fares and traffic, not share per seat.
- Table 1a was fetched 2026-11-11 from data.transportation.gov/resource/tfrh-tu9e.csv (airport_1=JFK&airport_2=SFO; airport_1=LAX&airport_2=JFK). The values used were typed by hand into 4_work/e_table.py, so spot-check them against the source before publishing.
