# Agent 10: Red-team review of counting United's 2027 JFK return
Run date: 2026-11-11. Public sources only. Quotes are under 15 words. Labels: **[A#]** = my assumption, **[J]** = my judgement.

## Part 1. The case AGAINST counting JFK-LAX/SFO in the switching base

### 1.1 Brief correction (fix before it reaches the deck)
- **Blue Sky was announced May 29, 2025, not Jul 29, 2025.** Jul 29, 2025 is the date the **DOT review was completed** (BusinessWire release 20250729944822).
  - AP and NBC carried the May 29, 2025 announcement. View from the Wing dated its story May 30, 2025.
  - The Jul 29 release says JetBlue will give United access to JFK slots for "up to seven daily round-trip flights out of JFK Terminal 6", starting "as early as 2027". It also describes a "net-neutral exchange" of eight Newark timings. It names **no DOT conditions** and no route restrictions.
  - Sources: https://www.businesswire.com/news/home/20250729944822/en/JetBlue-and-United-Complete-DOT-Review-of-Blue-Sky-Collaboration (fetched 2026-11-11); https://viewfromthewing.com/?p=227604 (May 30, 2025).

### 1.2 United has left JFK twice
| Episode | What happened | Source (date) |
|---|---|---|
| 2015 exit | United announced Jun 16, 2015 that it would swap its JFK slots to Delta for Delta's Newark slots. Last flights Oct 25, 2015. Reuters reported United's JFK routes had "failed to post profits" for **seven years**. Neither side disclosed slot counts. | https://fortune.com/2015/06/16/united-airlines-jfk/ (Jun 16, 2015); https://crankyflier.com/2015/06/18/united-exits-jfk-consolidates-its-power-at-newark (Jun 18, 2015) |
| 2021-22 return | United came back in Mar 2021 on **temporary**, pandemic-era slots: JFK-LAX and JFK-SFO, about 1.9 daily round trips per route, using 767-300ER and then 757-200 aircraft. | T-100, `raw/jfk/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv` |
| 2022 exit | United suspended JFK at the end of Oct 2022 after the FAA refused it permanent slots. Its memo said "without permanent slots, we can't serve JFK effectively". | https://onemileatatime.com/news/united-airlines-abandon-jfk/ (Sep 30, 2022) |

**Bear reading.** United has never made JFK transcon flying stick, and both exits had the same cause: too few slots to compete with Delta, American and JetBlue. Seven pairs is about 1.8 times the 2021-22 operation, but still sub-scale against Delta.
- OMAAT (Oct 31, 2026) calls United a would-be fourth-place JFK carrier with weaker loyalty and less connecting traffic.
- OMAAT says United wants "up to 20 daily slot pairs", which implies seven alone may not be enough.
- The 20-pair figure has no primary source. The nearest on-record comment is Kirby to CNBC: "We got a bunch of irons in the fire". He gave no number.
- Sources: https://onemileatatime.com/insights/united-airlines-jfk-return-imminent-strategy/ (Oct 31, 2026); https://airlinegeeks.com/2026/08/24/united-aims-to-grow-at-jfk/ (Aug 24, 2026); https://ch-aviation.com/news/170944-united-mulls-buying-slots-at-jfk-to-bolster-presence (Aug 25, 2026).

### 1.3 Slot-transfer details that weaken the case
- **These are access rights, not a sale.** The release says JetBlue will "provide United access to slots". The slots stay in JetBlue's portfolio and depend on Blue Sky continuing. United's consideration is not public. View from the Wing: "we don't know what cash may be changing hands".
- **No routes and no start date.**
  - ch-aviation (Aug 25, 2026) expected JFK routes to be announced on Aug 25, 2026 alongside United's international batch. That release contained **no JFK routes** (prior run, fromthetraytable Aug 25, 2026).
  - Nocella on the Oct 21, 2026 UAL Q3 call said United is "excited to reestablish JFK as the destination in 2027."
  - In the bullfincher transcript, that is the call's **only** JFK mention. There is no mention of slots, routes, Blue Sky or aircraft. The transcript is secondary; verify against the United IR webcast.
  - Source: https://bullfincher.io/companies/united-airlines-holdings/earnings-call/fy2026-q3 (fetched 2026-11-11).
- **Seasonality [A1].** FAA JFK slots run by IATA season: summer 2027 starts late March 2027, winter 2027/28 starts late October 2027. Summer 2027 was largely on sale by Nov 2026 with no United JFK flights loaded (no route announcement found). That makes a launch after mid-2027 more likely than a spring start.

### 1.4 The Coastliner is late and goes to Newark first
- **Timing.** The Coastliner A321neo was meant to debut in summer 2026. United said Airbus delayed delivery and gave no timetable.
  - United network chief Patrick Quayle: "As soon as we get it, we will start flying it."
  - TPG says JFK will come only "eventually".
  - Source: https://thepointsguy.com/news/united-airlines-international-routes-returning-coastliner-delayed (Aug 26, 2026).
- **First routes are Newark.** The first jet has arrived. Service is due on **EWR-LAX and EWR-SFO from early 2027**, with 50 on order. JFK is described as "likely to show up" once United returns, which is not confirmed.
  - Source: https://thepointsparty.com/articles/united-a321neo-coastliner-early-2027 (Nov 6, 2026).
- **Kirby tied the 2027 timing to aircraft.** At the Bernstein conference (May 2025, as paraphrased by Cranky Flier), Kirby said United "won't have good transcon airplanes available" until 2027. JetBlue's Marty St. George said the timing was "entirely United's decision" (also paraphrased).
  - With deliveries late and Newark first in line, United may not have Coastliners for JFK in 2027.
  - It could launch with 757/767s, as it did in 2021. InsideFlyer (Oct 31, 2026) names 757-200 and 767-300ER. But that is the product that lost to Delta and JetBlue Mint in 2015 and 2021-22.
  - Source: https://crankyflier.com/2025/06/02/jetblue-and-united-begin-their-partnership-with-a-few-buried-surprises/ (Jun 2, 2025).

### 1.5 United could use the seven pairs on other routes
- **Hub routes (JFK-ORD, DEN, IAH).** These are the network-logical use: they feed United's hubs and SFO's transpacific flights. JetBlue does fly them, but they are small for JetBlue: about 120k, 121k and 21k passengers a year (`<workspace>/jfk/out/csv1_jetblue_top15_jfk_routes.csv`). If United uses the slots there, the JFK addition to the base is about 0.26M passengers, not 1.45M.
- **International.** T6 is an international terminal. Kirby's stated priorities are South America and the Southeast US, which he calls "holes for United" (ch-aviation, Aug 25, 2026). JFK long-haul would not touch JetBlue's domestic base at all [J].
- **Counter-evidence (be fair).** Every 2026 trade report names **LAX and SFO** (InsideFlyer, Oct 31, 2026: "frequent flights to Los Angeles and San Francisco"), and so did both earlier United JFK eras. So LAX/SFO is the most likely use, not a certainty. I put **85%** on LAX/SFO, conditional on United launching JFK [A2].

### 1.6 JetBlue would respond on fare and capacity, not just lose passengers
- **2021-22 test (T-100 and DOT Table 1a; `<workspace>/jfk/out/hist_period_means.csv`, `hist_check.json`).**
  - **JFK-LAX:** JetBlue's passenger share was 30.0% in 2019, **30.3%** while United flew (7.6% United share), and 32.8% after United left. No share loss.
  - **JFK-SFO:** JetBlue's share fell from 28.7% to 24.2%. But its own seat share fell 3.9 points relative to 2019, which reflects JetBlue's own capacity choice (the NEA period).
  - **Pooled vs 5 control routes:** −3.3 share points, SE about 5.1, so not distinguishable from zero. Control routes alone ranged from −4.7 to +10.5 points.
  - **JetBlue load factor:** +2.3 points relative to controls. JetBlue was relatively fuller, not emptier.
- **The response was on price.**
  - The route average fare fell about 6% against controls (SE 4.6%) while United flew, then recovered after it left.
  - JetBlue's own JFK-LAX fare fell 7.3% while control routes' fares rose 5.7%.
  - **Implication:** United's entry cost JetBlue some yield, not passengers. A passenger-count switching base is the wrong tool for that effect.
- **Capacity shifts.** JetBlue has already shrunk New York temporarily: JFK seats are 12% below 2019 (T-100), and the CFO said on the Q3 2026 call that it "shrunk pretty significantly in Boston, New York". JetBlue can move seats away from overlap routes and refill them, so lost revenue is less than lost passengers × fare.
- **Base switching mechanism is weaker at JFK.** Blue Sky's Mosaic credit on United flights applies only to bookings made on jetblue.com, so JetBlue keeps part of the loyalty economics (prior run, verification table). Also, JFK-LAX JetBlue passengers are much more Mint/premium than the base-fare economy flyers the thesis models. The thesis is about economy fare parity.

### 1.7 Analyst and market views
- [Broker analyst comment removed: sell-side research text is excluded from this repo.]
- [Broker analyst comment removed: sell-side research text is excluded from this repo.]
- **Gary Leff (View from the Wing), May 30, 2025:** United "almost certainly overpaid". Read: JetBlue was paid for the slots, so part of any JFK revenue loss is pre-compensated.
- **OMAAT (Oct 31, 2026):** the author is sceptical United can make 20 pairs profitable against three entrenched carriers, which supports the likelihood of a small or temporary operation.
- **Missing coverage:** I found no sell-side note quantifying JetBlue's loss from United at JFK. Do not cite any analyst figure for it.

### 1.8 Probability and weighting
**P(United operates JFK-LAX and/or JFK-SFO on any date by Dec 31, 2027) = 60%** (range 50-70%) [J].
- **Factors for (start at about 75% that United launches any JFK service in 2027):**
  - The contractual slots are "as early as 2027".
  - The CCO restated 2027 on Oct 21, 2026.
  - Kirby has publicly committed.
  - 757/767 aircraft are available, as in 2021.
- **Factors against:**
  - Routes were missed in the Aug 2026 release, and nothing was loaded for summer 2027 as of Nov 2026.
  - The Coastliner is late and goes to EWR first.
  - United has a history of exits.
  - "As early as" is soft wording.
- **Calculation:** 0.75 × 0.85 (routes are LAX/SFO, given launch) ≈ 0.64, rounded down for slip risk to **0.60**.
- **P(in service by Q3 2027) ≈ 35%** [J], because summer 2027 has no load.

**Recommended weighting for the JFK increment** (add on top of the 2.3M base; JetBlue's JFK-LAX + SFO = 1.449M passengers; rule of thumb is −$0.138/share per 1M):

| Case | Weight | Definition | JFK pax added | $/share at full count | Timing |
|---|---|---|---|---|---|
| Bull | 20% | Launches by Q2 2027 on LAX + SFO; 20-pair expansion talk real | 1.449M | −$0.200 | from Q2 2027 |
| Base | 40% | Launches H2 2027 on LAX/SFO; only part of JetBlue's passengers face a parity United option (7 pairs vs JetBlue's frequency) | 50% of 1.449M = 0.72M [A3] | −$0.100 | from Q4 2027 |
| Bear | 40% | No LAX/SFO by end-2027, or hub/international use, or a 2021-22-style null result | 0 | $0.000 | — |
| **Weighted** | | | **0.58M** | **≈ −$0.080/share** | |

**Calculation:** 0.2 × 0.200 + 0.4 × 0.100 = −$0.080.

**Revision after reading agent 8 (supersedes the table above for the deck).**
- Agent 8 applies two adjustments to the switching base:
  - Fare parity: LAX is at parity on only 3 of 6 dates (weight 0.5), SFO on 6 of 6 (weight 1.0).
  - The 10% New York weight already in the thesis is removed so it is not counted twice.
- With those adjustments, the incremental JFK base is **0.843M passengers**, which is **−$0.116/share** fully counted (−$0.108 at agent 5's $167 fare).
- Re-weighted with my cases (bull 20% full, base 40% half, bear 40% zero): 0.2 × 0.116 + 0.4 × 0.058 = **−$0.046/share**.
- Simple version: P = 0.6 × −$0.108 = **−$0.065/share**.

**Recommendation.**
- **Do not add JFK to the headline base.** Present it as probability-weighted upside to the thesis: about −$0.05 to −$0.07/share, or about −$0.11 if fully counted, as switching only.
- Label it "contingent: no route announced; United exited JFK in 2015 and 2022".
- Include the 2021-22 JFK-LAX null result in the Q&A backup. Judges can find it.

---

## Part 2. Independent check of agent 8 (model) and agent 9 (valuation)
Files checked:
- Agent 8: `8_model.md`, `8_scenarios.csv`, `8_sensitivity.csv`, `model_inputs.json` (FINAL, 12:25).
- Agent 9: `9_valuation.md` (12:27), `out/<scenario>/JBLU_Model_Valuation.xlsx` and `JBLU_numbers.json`.
- My scripts: `<workspace>/rv/jfk27_10work/chk8.py`, `chk8b.py`. Both were written separately from agent 8's code.

### 2.1 Arithmetic: everything reproduces
| Item | Agent | My recompute | OK? |
|---|---|---|---|
| Central L27Q3_base, 2027Q3 lost pax / $M | 20,948 / 3.500 | 20,948 / 3.500 | yes |
| 2027Q4 | 42,609 / 7.119 | 42,609 / 7.119 | yes |
| 2028Q1 | 42,964 / 7.179 | 42,964 / 7.179 | yes |
| 2030Q4 | 52,719 / 8.807 | 52,719 / 8.807 | yes |
| Annual $M, 2027 / 28 / 29 / 30 | 10.62 / 31.04 / 34.71 / 35.08 | 10.62 / 31.04 / 34.71 / 35.08 | yes |
| Workbook T2 input row (Operating Model r46) vs `8_scenarios.csv` | 3.5, 7.119, 7.179, … 8.807 | same | yes |
| T2 EBIT = 88% of revenue | 9.345 on 10.619 (FY27) | 9.345 | yes |
| T1 at 2.316M: −$0.138 × 2.316 | −0.320 | −0.3202; rule check 0.85 / 6.147 = 0.1383 | yes |
| T1 run-rate revenue: 2.316M × 6% × $180 | $25.0M/yr (6.253/qtr) | $25.01M | yes |
| T2 $/share via revenue scaling (T1 gives −$0.01281/share per $1M run-rate revenue) | −0.439 | 35.08 × 0.01281 = −0.449 (gap = T2's later ramp) | yes |
| T2 $/share via passenger-equivalents: 210k lost ÷ 6% = 3.5M equivalent × −0.138 × (167 / 180) | −0.439 | −0.448 | yes |
| Agent 8 base view: 0.4 × 921k + 0.9 × 528k = 0.843M → × 0.138 | −$0.12 | −$0.116 | yes |
| Workbook health | 0 errors, balance 0 | checked central xlsx cached values; DCF!C72/C73 = −0.3204 / −0.4386 | yes |

**No arithmetic errors.** The issues are framing and assumptions.

### 2.2 Errors and issues, ranked by $/share impact
1. **[Material: framework inconsistency] Agent 9 puts the capacity effect into the DCF. Agent 8 says it should not be counted in passenger-base terms.**
   - Agent 8 states that the capacity effect is "outside the reverse-DCF passenger-base framework" and gives a passenger-base view of **−$0.12**.
   - Agent 9 instead loads total `lost_rev_M`, about 76% of which is capacity effect, and gets **−$0.44**.
   - That makes JFK larger than all of Thesis 1 (−$0.32), which is not defensible given:
     - the 2021-22 JFK-LAX null result (JetBlue share 30.0 → 30.3%);
     - the pooled result of −3.3 pp (SE 5.1), not distinguishable from zero;
     - agent 3's regression at p = 0.32.
   - **Fix:** headline T2 = switching only. In the workbook, either replace the T2 input row with `lost_rev_switching_M`, or set capacity to a sensitivity. Switching only is about $8.4M/yr by 2030, worth about **−$0.11/share** on either cross-check.
2. **[Material] Launch is assumed to be certain.** All 9 scenarios assume United launches on LAX/SFO. My estimate is P = 0.60 by end-2027. Also, agent 9's "Bull" is consensus (no thesis), not a no-JFK case.
   - **Fix:** T2 × P. Central becomes −$0.26 with capacity effect, or **−$0.065** switching only.
3. **[Material] Persistence into the terminal value at 100%** (Assumptions C13 = 1). United's access depends on Blue Sky continuing and on the FAA JFK Order, which expires Oct 28, 2028 (agent 2). United also exited JFK in 2015 and 2022.
   - A perpetual capacity loss is the most aggressive choice available.
   - **Suggest:** keep persist = 1 for T2 switching only (loyalty-driven, like T1). Give any capacity effect a finite life or a haircut.
4. **[Moderate] No offsets.**
   - 88% flow-through with no refill or redeployment. The prior run used 55-85% EBITDAR flow-through.
   - The undisclosed slot consideration from United is not netted.
   - JetBlue's 2021-22 response was on yield: the route average fare fell about 6% relative to controls, and JetBlue's own LAX fare fell 7.3%. That is a different loss shape, which agent 8 notes but does not model.
   - The direction of these omissions overstates T2.
5. **[Moderate] Bear multiplier compounds an assumption-heavy add-on.** Bear = 150% of total thesis, so the central bear price is $2.80 (−28.9%). Apply the 150% to T1 only, or show T2 as a separate line.
6. **[Minor] Timing convention differs between theses.** T1 uses end-of-quarter switching (Q4'26 = 0.775% = 0.031 × 1/4). Agent 8's T2 uses mid-quarter (0.031 × 0.5/4). T1 is slightly front-loaded relative to T2; the effect is under 1¢/share. Pick one convention.
7. **[Minor] Fare inconsistency.** T1 uses $180 (brief). T2 uses $167.5 / $166.5 (agent 5, live lowest economy fare). At $180, T2 rises about 7.6% (sensitivity: cumulative $120.1M vs $111.4M). Either is defensible; label it.
8. **[Minor, opposite direction] Cabin mix.** The capacity effect uses JetBlue's all-cabin share but values lost passengers at the economy fare. If the capacity effect is real, revenue is understated, because Table 1a all-cabin fares double it (agent 8 sensitivity: $74.9M/yr). Mint is $236+ below United business (agent 5), so Mint flyers are not at parity. Keep this as a sensitivity only.
9. **[Minor] Consensus price drift.** Consensus DCF is $3.9415 versus the $3.94 price. Thesis $/share is measured against $3.9415 but downside against $3.94. Negligible, and agent 9 disclosed it.
10. **[Fact] Brief date.** Blue Sky was announced May 29, 2025. Jul 29, 2025 is the DOT-review release. Agent 8 cites Jul 29 for the "as early as 2027" wording, which is correct because that release does contain it, but it is not the announcement date.

### 2.3 Recommended numbers for the deck
| Line | $/share | Basis |
|---|---|---|
| T1 Blue Sky switching (2.316M base) | **−0.320** | Agent 9, verified |
| T2 JFK, switching only, × P(0.60) | **≈ −0.065** | Agent 8 switching-only $8.4M/yr → −$0.108 × 0.6 |
| **Headline thesis** | **≈ −0.385 → about $3.56 (−9.8%)** | sum. **[J]** Not re-run in the workbook; it is additive because agent 9 reports interaction = 0.000 |
| Sensitivity: T2 incl. capacity effect, × P | −0.26 | −0.439 × 0.6 |
| Sensitivity: T2 incl. capacity effect, certain launch (agent 9 central) | −0.44 → thesis −0.76, $3.18 (−19.2%) | Agent 9 |
