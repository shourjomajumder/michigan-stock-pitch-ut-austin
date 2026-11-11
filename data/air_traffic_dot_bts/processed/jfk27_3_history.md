# 3. History: what United's JFK flying did to JetBlue (2021-22 entry/exit, 2015 exit)

Agent 3, run 2026-11-11. Scripts: `3_history.py` (main), `3_sensitivity.py`, `3_extra.py`. Inputs reused read-only from `(orig workspace) jfk/` (BTS T-100 segment data pulled Nov 8 2026 from transtats.bts.gov; DOT Consumer Airfare Report Table 1a, data.transportation.gov dataset tfrh-tu9e) and DOT Table 6 values in `(orig workspace) switch/a4work/vx.py` (data.transportation.gov dataset yj5y-b2ir). No new web data: data.transportation.gov is blocked by this container's proxy (HTTP 403), and no browser was used.

## Bottom line

**Best estimate: JetBlue loses about 5 share points of the route per 10 points of United seat share (95% range about -10 to 0).**
- The range is wide. The primary spec's placebo-inverted 95% CI is **-9.6 to -2.0**. That result is not robust: adding three more control routes (DEN, ORD, IAH) gives -8.4 with p = 0.19.
- A simple proportional benchmark (United takes share from everyone in proportion) would be about -2.9 (JetBlue's ~29% share × 10 points). The data put JetBlue's loss at roughly 1.5-2x that benchmark.
- **Mechanism: JetBlue's seat share moved one-for-one with its passenger share, and its load factor did not fall** (+1.8 pts per 10, n.s.). In 2021-22, JetBlue lost share by flying fewer seats on those routes, not by flying emptier planes. For 2027 this matters: the slots come from JetBlue's own T6 pool, so JetBlue's seat cut is built in.

| Estimator (JetBlue pax share, pp per +10pp United seat share) | Estimate | Uncertainty | p (placebo) |
|---|---|---|---|
| A. Quarterly TWFE, 2019 + 2021Q1-2026Q2, 5 controls (headline spec) | **-5.7** | placebo SE 2.2; RI 95% CI -9.6 to -2.0 | 0.02 (min possible, 1/42) |
| D. Same spec but ends 2024Q4 and drops 2021H1 (pre-specified window) | -4.5 | route-placebo SD 3.0 | 0.12 |
| E. 8 controls (+DEN, ORD, IAH) | -8.4 | placebo SE 5.7 | 0.19 |
| A + Alaska seat share as covariate (Alaska left JFK-LAX in 2021-22) | -6.8 (-5.9 ending 2024) | placebo SD 2.4-2.9 | 0.02 |
| Monthly sharp exit, Sep-Oct to Nov-Dec 2022 vs the same window in 2019/21/23 | -6.9 LAX, -4.5 SFO (avg -5.7) | no CI; 2 routes × 1 event | n/a |
| Period DiD vs 2019, UA era (2021Q3-22Q3), scaled by 9.6pp dose | -3.5 | placebo SD 4.7 | 0.52 |
| Quarterly exit DiD (2022Q1-3 to 2023Q1-3), scaled by 9.1pp removal | -1.9 | placebo SD 2.7 | 0.48 |

Inference uses three methods, because 2 treated routes make normal standard errors meaningless:
- **Route placebo:** United's LAX/SFO dose paths are moved onto every other ordered pair of routes (41 placebos).
- **Time placebo:** the 2021-22 dose profile is placed on LAX/SFO in seven windows from 2023-26, when United was absent.
- **Wild cluster bootstrap** (Webb weights). This one is indicative only.

The `placebo_se` column combines the route and time placebo variances. Full detail is in `3_did_dose_results.csv`, `3_did_sensitivity.csv` and `3_did_with_alaska_control.csv`.

## Setup

- **Treated:** JFK-LAX, JFK-SFO. **Controls:** JFK-SEA, LAS, SAN, PHX, SLC (same as `hist_check.py`). Alternative controls add JFK-DEN, ORD, IAH; United never flew these from JFK.
- **Sample:** 2019Q1-Q4 and 2021Q1-2026Q2. 2020 (COVID) is dropped, and so is 2026Q3, which is July only.
- **Dose:** United seat share of route seats (T-100, both directions, class F). United ran ~1.9 daily round trips per route, 172 seats/departure (`(orig workspace) jfk/JetBlue_Driver2_JFK_2027.md`, row 7). That gave 7.5-8.2% seat share on LAX and 9.6-13.4% on SFO.
- **Fixed effects:** route × quarter-of-year (seasonality) plus calendar quarter (the common COVID recovery).
- **Pre-trends are untestable:** only 2019 is available pre-entry locally. 2017-18 T-100 was not pulled.

## Quarterly: JetBlue on JFK-LAX / JFK-SFO vs controls (T-100 share %, Table 1a fare $)

| Qtr | LAX UA seat sh | LAX B6 sh | LAX B6 seat sh | LAX B6 LF | LAX DL sh | LAX fare | SFO UA seat sh | SFO B6 sh | SFO B6 seat sh | SFO B6 LF | SFO DL sh | SFO fare | Ctrl B6 sh | Ctrl fare |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 avg | 0 | 30.0 | 29.8 | 89.1 | 35.5 | 398 | 0 | 28.7 | 28.4 | 86.9 | 36.4 | 371 | 25.5 | 290 |
| 2021Q3 | 8.2 | 27.6 | 28.0 | 90.2 | 42.7 | 381 | 13.4 | 29.0 | 29.6 | 85.6 | 40.0 | 354 | 28.8 | 282 |
| 2021Q4 | 8.1 | 29.2 | 29.7 | 88.0 | 41.5 | 378 | 12.3 | 21.7 | 21.8 | 80.8 | 36.0 | 310 | 25.3 | 278 |
| 2022Q1 | 7.9 | 28.6 | 32.0 | 68.1 | 41.7 | 349 | 11.3 | 21.1 | 22.3 | 60.2 | 31.6 | 251 | 23.2 | 278 |
| 2022Q2 | 7.6 | 32.5 | 32.7 | 91.5 | 39.8 | 514 | 10.6 | 23.9 | 23.8 | 90.7 | 26.4 | 423 | 26.6 | 358 |
| 2022Q3 | 7.5 | 33.4 | 33.1 | 89.8 | 39.6 | 482 | 9.6 | 25.4 | 24.9 | 87.6 | 27.5 | 398 | 30.4 | 330 |
| 2022Q4 (exit Oct) | 2.5 | 37.0 | 37.4 | 89.2 | 40.4 | 514 | 3.4 | 27.3 | 27.2 | 88.0 | 28.7 | 412 | 31.1 | 335 |
| 2023Q2 | 0 | 33.2 | 33.8 | 88.9 | 46.7 | 479 | 0 | 26.5 | 27.0 | 87.5 | 35.4 | 379 | 28.7 | 331 |
| 2024Q2 | 0 | 31.0 | 32.0 | 86.6 | 47.1 | 522 | 0 | 24.3 | 24.3 | 91.5 | 39.1 | 457 | 21.5 | 339 |
| 2025Q2 | 0 | 29.0 | 30.4 | 84.5 | 48.0 | 499 | 0 | 27.6 | 28.3 | 86.0 | 39.7 | 440 | 18.8 | 346 |
| 2026Q2 | 0 | 30.0 | 29.8 | 90.1 | 45.7 | n/a | 0 | 27.6 | 27.3 | 91.4 | 40.0 | n/a | 18.5 | n/a |

The full quarterly series is in `3_quarterly_treated_vs_control.csv`. The route-quarter panel for all 10 routes (all carriers, seats, deps, LF, fares) is in `3_quarterly_panel_2019_2026.csv`.

**Monthly** (JFK-LAX/SFO plus BOS and EWR comparisons, 2019-01 to 2024-04; later months are not local) is in `3_monthly_lax_sfo_2019_2024m4.csv`. The key months:

| | Oct 2022 (UA in) | Nov 2022 (UA out) |
|---|---|---|
| JFK-LAX | UA seat share 6.9, B6 share 33.0, B6 seat share 33.2 | B6 share 39.8, B6 seat share 40.1 |
| JFK-SFO | UA seat share 9.2, B6 share 25.9 | B6 share 27.4 |

On SFO, JetBlue's share fell from 29-31% (Jul-Aug 2021) to 19-21% (Nov 2021-Jan 2022). That drop came while United was steady at 11-14%, and it tracked JetBlue's own seat-share cut (32.3 to 21.6).

## Capacity effect (passengers per United seat; 5 controls, quarterly TWFE)

- **United filled 0.80 passengers per seat**, which matches its reported LF of 80-84%, so the model checks out.
- **JetBlue: -0.47 passengers per United seat added** (95% placebo range -1.07 to +0.13; p = 0.32). With 8 controls: -0.44.
- **Others:** Alaska -0.17, Delta +0.04, American +0.10 (all n.s.).
- **Total route traffic: +0.38 per seat** (n.s.). There was weak market stimulation at best.
- **Scale:** 10pp of seat share on JFK-LAX is ~385k United seats a year. At 0.47, that is ~180k JetBlue passengers, consistent with the share estimate (5pp × ~3.0M route pax ≈ 150k).
- **Assumption (labelled):** this scale-up uses the L4Q route size in `(orig workspace) jfk/src/t100_jfk_top_b6_routes_L4Q_2025q3_2026q2.csv` (3,463,142 seats; 3,015,438 pax).

## Price effect (DOT Table 1a route average fare; JetBlue's own fare shows only when it is largest or lowest-fare carrier)

- **Average fare: -7.6 log points per +10pp United seat share** (placebo 95% range -14.3 to -0.9; route-placebo p = 0.05).
- **Period DiD for the UA era vs 2019: -6.2%** (LAX +4.5%, SFO -8.3%, controls +4.2%; placebo p = 0.29). Fares recovered after the exit (exit DiD +1.8%, n.s.).
- **Confound:** LAX/SFO are business-heavy, and business travel recovered late in 2021-22. That biases toward finding a fare cut.
- **JetBlue's own fare is visible only on LAX** (it was the lowest-fare carrier there 2021Q2-2026Q1), so no DiD is possible for it.

## Delta and American

- **During United's flying:** Delta -2.3 pp per 10pp (n.s.; -3.8 with Alaska control); American +1.2 (n.s.). The JetBlue+American combined share (the NEA partners Jul 2021-Jul 2023) was -4.5 per 10pp.
- **When United left (quarterly exit DiD), Delta was the clearest gainer:** +4.4 pp vs controls (p = 0.05). JetBlue +1.7 (p = 0.48), American +2.2 (p = 0.76).
- **By month, Sep-Oct to Nov-Dec 2022, excess over normal seasonality:**
  - JFK-LAX: JetBlue +4.9, Delta +1.6
  - JFK-SFO: JetBlue +3.9, Delta +5.6
  - American was about 0 on both (`3_monthly_exit_2022_excess.csv`).
- **Confound on LAX:** Alaska left JFK-LAX at the same time United entered: 14.5% share in 2019, 2.3% in 2021, 0 from 2022 (T-100). Delta's LAX share rose 35.5 to 39.6-42.7 over that period. That is why the Alaska covariate matters.

## 2015-16: United leaves JFK

United moved its JFK p.s. flights (LAX/SFO) to EWR in Oct 2015 (crankyflier.com/2015/06/18/united-exits-jfk-consolidates-its-power-at-newark, as cited in `(orig workspace) nyc/5_natural_experiments.md`).

**Data limit:** airport-level T-100 for 2014-16 is not local, and it cannot be pulled here (no browser; data.transportation.gov is blocked). The only local evidence is DOT Table 6 city-market shares (NYC metro incl. EWR), and Table 6 shows a carrier only when it is the largest or the lowest-fare carrier. Values are in `3_exit_2015_table6_city_markets.csv`.

| City market | United share 2015Q1-Q3 avg | 2015Q4 | 2016Q1 | 2016Q2-Q4 avg | Same-quarter YoY, 2016 vs 2015 (Q1/Q2/Q3) |
|---|---|---|---|---|---|
| NYC-SFO | 34.7 | 29.4 | 27.8 | 33.3 | -7.0 / -1.6 / -1.9 |
| NYC-LAX | 27.7 | 24.0 | 22.4 | 25.8 | -3.9 / -1.9 / -3.2 |

- **United's net city-market loss:** United lost ~5-7 pts in the first two quarters after the move and kept a net loss of ~2-3 pts through 2016, even after consolidating at EWR. So customers only partly followed it across airports.
- **Who gained cannot be measured from Table 6:**
  - JetBlue (the lowest-fare carrier on NYC-SFO) went from 14.5% (2015Q1) to 16.7% (2016Q1), +2.2. It is not visible for the rest of 2016.
  - On NYC-LAX, JetBlue was visible at 17.9-19.5% in 2015, then disappeared from the table in 2016, when Virgin America became the lowest-fare carrier at 15-17%.
  - Delta and American are never shown.
- **Confound:** JetBlue's Mint launched on JFK-LAX (Jun 2014) and JFK-SFO (2015) (`(orig workspace) cases/k5_product.csv`).
- **To close this gap:** pull BTS T-100 segment data for 2014-2016 (JFK/EWR-LAX/SFO by carrier) via the TranStats page and `(orig workspace) jfk/browser_extract_t100_table1a.js`.

## Caveats

1. **2 treated routes, 1 entry and 1 exit.** Every interval here is a placebo distribution with 20-41 draws, not a sampling-theory CI.
2. **The JetBlue share effect works through JetBlue's own capacity.** In 2021-22 that was partly JetBlue's choice (NEA network reshuffle, the SFO cut in late 2021), so attributing it all to United overstates the causal effect. In 2027, though, the slots come from JetBlue.
3. **Alaska's JFK-LAX exit and slow business recovery** coincide with the treatment window.
4. **The sign of the result depends on which post period the late-2025-26 data are compared with:** JetBlue shrank on the control routes (SEA, SLC) in 2025-26.
5. **Minor data notes:**
   - JetBlue pax log changes for the 2025-26 period are undefined because JetBlue had zero passengers on one control route in some quarters (`inf` in `3_did_period_vs2019.csv`).
   - One truncated monthly row (Apr 2024) in the source file was dropped.
