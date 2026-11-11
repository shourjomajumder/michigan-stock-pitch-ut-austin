# JetBlue Driver 2 (Blue Sky switching): verification and rebuild
Hook Em, Michigan Ross pitch. Run date: Nov 8, 2026. Every number traces to a file in `out/` or `src/` in the accompanying zip.

**Headline:** The elite-period test came back with the wrong sign. In July 2026, the first and only month of elite-period data, JetBlue filled *more* seats on the shared routes than on its other Boston routes, not fewer. The placebo also failed, and the pre-trend test failed. Our own data cannot support the "switching has started" claim, and it does not yet measure a leak. Per the brief's instruction, the driver should be reframed as **precedent-based, with our data described as too early to read**. Several mechanism facts got *stronger*: the one-way status rule is confirmed on both airlines' official pages. Several got *weaker*: the Delta–Alaska timing argument, the catalyst timing, and JetBlue's own Q3 loyalty disclosures.

---

## 1. Thesis restatement (before data), with flags

**Claim.** Blue Sky lets JetBlue's elite (Mosaic) flyers try United at no cost to their status, while United flyers earn no status on JetBlue. Some JetBlue elites on the 14 routes both airlines fly will move their flying to United.

**Two-stage mechanism.**
- **Stage 1:** a measurable flight switch. JetBlue loses the fare, net of whatever United pays for TrueBlue points.
- **Stage 2:** an estimated full defection. JetBlue loses card and loyalty revenue from flyers who move their status and card to United.

**Timing.**
- Elite perks went live the week of May 14, 2026.
- The effect is expected from Q4 2026 to Q3 2027.
- Catalysts:
  - JetBlue's Q2 and Q3 2027 results
  - United's commentary on Blue Sky
  - United's JFK launch

**Size.** About $14M of fares through Q4 2027 in the base case. Because JetBlue carries so much debt, that equals roughly 3–6% of equity value.

**Why it matters.** The elite flyers at risk are the high-yield customers JetBlue's recovery depends on.

**Flags found before running anything:**
1. **The "free trial" has a condition.** To earn TrueBlue points or Mosaic credit, or to get Mosaic perks on United, the flight must be **booked on jetblue.com or the JetBlue app**. JetBlue keeps the booking channel and the customer record. Blue Sky is "not a codeshare" (jetblue.com FAQ). So a switcher is partly still JetBlue's customer, and Stage 1 overstates the loss unless JetBlue earns nothing on those bookings. That economics is not public.
2. **The May 2026 start date rests on a mismatch.** The brief dates the effect from elite perks and cites Delta–Alaska. But Delta and Alaska had shared elite benefits since about 2004. Their share shift began in 2013–14, when **Delta built a Seattle hub**. The precedent dates the effect from capacity, not from perks.
3. **The brief mixes units in one place.** It treats 0.88M treated JetBlue seats a quarter as the base. The verified figure is 0.68–0.72M. One load-factor point is about 6,800–7,200 passengers, not 8,800.
4. **The equity figure is not on the same basis as the $14M.** The "3–6% of equity" comes from an end-2027 *run-rate*, not from the $14M cumulative total.
5. **The proposed catalyst may not exist.** JetBlue reports system-level unit revenue only. The 10-Q has no Northeast-versus-system split, so "Northeast unit revenue vs system" is probably not a reportable catalyst.

---

## 2. Verification table

Full version with sources: `out/verification_table.csv`.

| Input | Package value | Status | Verified value | Source |
|---|---|---|---|---|
| Shared routes | 13–14/qtr | Confirmed | 13 most quarters; 12 in 2025Q1 and Jul 2026 (JetBlue left EWR–RSW and EWR–LAS); 14 in 2026Q2 | T-100, B6 and UA ≥10 departures each month |
| Passengers on shared routes | 2.73M (UA 2.0M, B6 0.74M) | **Corrected** | **2.97M/qtr** (UA 2.24M, B6 0.74M), 2025 average | T-100, 14 routes |
| Average fare | ~$284 | Confirmed | $284.44 (Q1 2026, passenger-weighted) | DOT Table 1a |
| 1 share point | 27,300 pax, $7.8M | **Corrected** | **29,700 pax, $8.46M/qtr** ($6.58M at JetBlue's own fare) | Recomputed |
| Treated JetBlue seats | 0.88M | **Corrected** | **0.68–0.72M/qtr** | T-100 |
| Delta–Alaska | +0.83 (2014), +0.52 (2015) | **Corrected** (direction holds) | +0.81 (2014), **+0.97** (2015), +0.40 (2016), −0.50 (2017); quarterly peak +1.52 | T-100 2012–19, SEA |
| NEA | +0.36 / +0.50 | Not re-verified | — | Package CSV |
| Blue Sky, United-share metric | −0.82 → −0.26 | **Corrected** | Baseline −0.91; miles-only −0.60; Jul 2026 +0.26 | T-100 |
| Timeline | Oct 23 / Feb 10 / May 14 | Confirmed | Same | JetBlue IR, United newsroom, united.com |
| One-way status rule | Blogs | **Confirmed on official pages, with the booking condition** | JetBlue: United flights count toward Mosaic if booked on jetblue.com. United: "Premier qualifying credit is not earned on … JetBlue" | jetblue.com/jetblue-united; united.com partner page |
| On-time, Jan–Jun 2026 | 77.6% vs 71.0% | Confirmed | UA 77.60% (3rd of 9); B6 71.02% (8th of 9) | DOT ATCR, Aug 2026, Table 1C |
| July cancellations | B6 9.8% vs UA 2.7% | **Unverified** | June: B6 1.5%, UA 1.1% | DOT ATCR, Aug 2026, Table 6 |
| J.D. Power | #1 premium, #3 economy | Confirmed | #1 first/business (759); #3 economy (655) | J.D. Power, May 6, 2026 |
| JetBlue LF | 83.6% Q3 | Confirmed | 83.6% (85.5% on treated routes, 2025) | 10-Q; T-100 |
| EV/EBITDAR 2027E | 9.2x | **Not reproduced** | [third-party multiple removed]; deck used 10.8x | deck |
| Share price, market cap | $3.15 | Updated | $3.16 (Nov 6); 377.35M shares; **$1.19B** | public quote; 10-Q cover |
| Southwest–ATA, Lederman, Gayle | — | Confirmed earlier | — | Primary papers and press |

---

## 3. Results: every number requested

**Data used.**
- **T-100 Domestic Segment** (class F), through **July 2026**. That means **Q3 2026 = July only**, compared with July 2025.
- **DB1B ends at Q2 2025** (TranStats "latest available: June 2025"), and the download failed twice. It cannot cover the elite period.
- **DOT Table 1a** runs through **Q1 2026**.

**Route sets.**
- **Treated:** the 12 shared routes, excluding FLL.
- **Comparison:** 24 JetBlue Boston routes. No Newark route qualified, because United flies every JetBlue Newark route.
- **Leisure-only comparison:** 7 routes.
- Rules are in `prep.py`.

**Thresholds I added before seeing any results.**
- A carrier "flies" a route if it has at least 10 departures in a month.
- A route-quarter is usable if it has at least 30 departures (at least 10 for July-only).

| Number | Result | What it means |
|---|---|---|
| **β₁, placebo (miles-only)** | **+2.50 LF pts (SE 1.06)**; Q2 2026 dropped: +1.70 (1.09); YoY version +2.39 (1.58) | **Placebo fails.** Shared routes outperformed even before elite perks. |
| **β₂, elite period (July 2026)** | **+3.75 LF pts (SE 1.09)**, 36 routes, 10 treated in July; Q2 dropped +3.78 (1.10); leisure-only +1.52 (1.46); seat-weighted +3.21 (1.24); route×season FE +1.90 (1.95); YoY version **+0.85 (1.86)** | **Wrong sign.** No measured switching. The YoY version, which nets out the pre-trend, is zero. |
| β₂ for revenue and for fare | **Not estimable.** Fare data end Q1 2026 (Table 1a) and Q2 2025 (DB1B). Placebo-period proxy on Table 1a (9 treated, 23 comparison routes): fare **+4.8% (SE 2.5%)**, revenue **+6.0% (3.0%)**, LF +0.7 (1.1) | JetBlue's fares and revenue on shared routes *rose* relative to comparison routes before elite perks. That is pricing strength, not a leak. |
| Switchers per quarter (−β₂ × seats) | **−25,400** (main); −5,700 (YoY). Upper 95% bound, YoY: **≤18,900/qtr** | No measured leak. The data can't rule out up to about 19k passengers a quarter, but that rests on one month. |
| Baseline σ; thresholds | σ = **1.40 LF pts** (7 baseline quarters); single-quarter 2σ = **2.80**; pooled 2σ/√k = 1.98 (k=2), 1.62, 1.40, 1.25, **1.14 (k=6)** | |
| First detectable quarter (base case) | **Q4 2027**, using 6 pooled quarters; DOT release around **March 2028** | **Outside the 3–12-month catalyst window.** |
| F_elite, F_replace, P_points, V_member | F_replace **$221** (JetBlue's own fare, Table 1a); F_elite **$332** (A1: 1.5×, no DB1B); P_points **$27 / $33 / $40** (8 pts/$ × $332 × 1.0/1.25/1.5¢, A2); V_member **$68**/yr ($1,190M ÷ 17.5M members, A3: count unverified, understates elites) | |
| Stage 1 loss per switcher | Empty seat **$299**; refilled **$78**; blended (ρ=50%) **$188** (range $137–239 for ρ 30–70%) | |
| Stage 2 | 10/25/50% defection: **$0.4M / $1.0M / $2.0M a year** at the base run-rate (upper bound) | Small |
| Bear / base / bull, through Q4 2027 | **Measured: $0.** Precedent paths as written: $3.4M / $13.6M / $27.5M. With verified inputs at $284: $3.7M / $14.8M / $30.0M. At JetBlue's $221 fare: **$2.9M / $11.5M / $23.4M** | |
| Run-rate EBITDAR, EV lost, market cap, equity hit | Base (0.5 share pts at end-2027): 59,500 pax/yr × $188 = **$11.2M EBITDAR**. EV lost at 9.2x = **$103M**. Market cap **$1.19B**. Equity impact **8.6% at 100% persistence / 4.3% at 50%**. Brief's worked example recomputed: 6.0% / 3.0% | **Hypothetical: precedent-based, not measured** |
| United-share metric (original method) | Baseline −0.91, miles-only −0.60, July 2026 **+0.26** (+1.18 vs baseline) | **Disagrees with JetBlue's own load factor.** Most of the move is the AA control falling in July, and United's Newark connecting traffic inflates it. |
| Delta–Alaska, recomputed | vs 2013: **+0.81 (2014), +0.97 (2015)**, +0.40 (2016), −0.50 (2017), −0.79 (2018); quarterly peak +1.52 (2014Q4); pre-period quarterly SD 0.50; only 3–7 Delta routes in 2012–13 | Precedent holds in direction. It coincides with the Delta hub build, not with elite perks. |
| Leave-one-out; leisure-only | β₂ ranges **+3.38 to +4.04** across 12 drops, never negative; leisure-only +1.52 | Robust, but robustly the wrong sign. |
| JetBlue's guided Blue Sky benefit | **"$50 million more in incremental EBIT than we had initially planned for a partnership"**; JetForward raised to $850–950M by end-2027 | JetBlue Q2 2025 release, Jul 29, 2025 |
| Answer to "Blue Sky is a net positive" | JetBlue's figure counts points sales, Paisly distribution of United's hotels and cars, and feed. JetBlue's Q3 2026 results show **loyalty revenue +20% YoY**, **"record levels of active TrueBlue members and elite status qualifications,"** and **1.1B TrueBlue points redeemed on United**. | These cut *against* elites leaving so far. |
| One-way status rule | **Confirmed on both official pages** | See table 2 |

---

## 4. Triple-check list

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | Route totals match published totals in 2 months | **Partial** | Carrier-month totals were computed from the same T-100 pull (`src/t100_carrier_month_totals.csv`). BTS's separately published summary was not pulled. JetBlue's reported passengers (10.4M in Q3 2025) include international flying, so they don't compare to domestic T-100 (7.2M). |
| 1b | Directions combined, no double count | Pass | route = sorted airport pair |
| 1c | Missing quarters listed | Pass | 13 gaps: EWR–LAS (operated only 2026Q1–Q2), EWR–LAX 2025Q1 and 2026Q1, EWR–TPA 2026Q1, EWR–RSW Jul 2026 |
| 1d | Latest month stated | Pass | T-100 Jul 2026; DB1B Q2 2025; Table 1a Q1 2026 |
| 1e | DB1B ≥100 sampled passengers | **Fail / N/A** | DB1B not usable. Table 1a (fare where JetBlue is the largest or lowest-fare carrier) was used instead. |
| 2a | Route sets and periods as written | Pass, with disclosures | Added the departure thresholds above. EWR–LAS stays treated although JetBlue entered and exited it during the study. |
| 2b | β₁ reported | Pass | +2.50 (1.06): **the placebo fails** |
| 2c | With and without Q2 2026 | Pass | +3.75 / +3.78 |
| 2d | Leisure-only same sign | Pass | Both positive, i.e., both the wrong sign for the thesis |
| 2e | Pre-trends parallel | **Fail** | Baseline effect averages **+1.37 pts/qtr (t=2.59, p=0.04)**. Shared routes were already outgrowing comparison routes. |
| 2f | United-share cross-check | Run; **disagrees** | United-share metric moves toward the thesis (+1.18 vs baseline). JetBlue's own load factor moves against it (β₂ +3.75; YoY +0.85). |
| 2g | Revenue and LF point the same way | Partial | Only the placebo period is available. All three rose (fare +4.8%, revenue +6.0%, LF +0.7). |
| 2h | Leave-one-out | Pass | No sign flip |
| 3a | Every input confirmed or corrected | Pass | Table 2. NEA not re-verified; member count unverified. |
| 3b | One-way rule on both official pages | Pass | Quoted above |
| 3c | Guided Blue Sky benefit found | Pass | $50M incremental EBIT by 2027 |
| 3d | Scenario and equity math recomputed | Pass | As written: $3.4M / $13.6M / $27.5M; worked example 6.0% / 3.0% |
| 3e | Shares and market cap from 10-Q and a dated price | Pass | 377,351,854 shares (Sep 30, 2026); $3.16 (Nov 6); $1.19B |

---

## 5. Refined thesis, what weakened it, and extra analyses

**Refined thesis (what the evidence supports).**
- **What's confirmed:** Blue Sky created an asymmetric loyalty link. JetBlue elites can earn Mosaic credit on United flights booked through jetblue.com, but United elites earn no Premier credit on JetBlue (confirmed on both airlines' official pages). United also runs the more reliable operation: 77.6% on time versus 71.0% in the first half of 2026, per DOT.
- **What the precedent shows:** when Delta and Alaska were loyalty partners and Delta added Seattle capacity, Delta's planes ran fuller than Alaska's on shared routes by about **+0.8 to +1.0 points a year in 2014–15**. That faded by 2017.
- **What our data shows:** the one month of JetBlue data since elite perks started (July 2026) shows **no leak**. JetBlue's load factor on the shared routes *rose* relative to its other Boston routes. Its fares and revenue there were rising even before elite perks.
- **What would make it visible:** if switching follows the Delta–Alaska size, a base-case leak (0.5 share points by end-2027, about 15k passengers a quarter) would not be statistically visible in DOT data until **Q4 2027**, published around **March 2028**.
- **How to present it:** as a **precedent-based structural risk**, not a measured effect and not a 3–12-month catalyst. If it happens, the base case is worth about **$11M of run-rate EBITDAR, or 4–9% of JetBlue's equity**. That range spans 50–100% persistence at 9.2x; it is 6–12% at

**What changed from your version.**
- The size is about the same, though passengers per share point are higher.
- The timing moves out by about 6 months.
- The catalyst changes from JetBlue's earnings to DOT data in 2028.
- The mechanism now carries the jetblue.com booking condition.
- "Switching has started" and "visible by Q3 2027" should not be said.

**What weakened the thesis.**
1. The elite-period effect is the wrong sign (+3.75, SE 1.09), and zero in the YoY version (+0.85, SE 1.86).
2. The placebo failed (+2.50, SE 1.06), and the pre-trend test failed (p=0.04). Shared routes were already diverging upward, partly because JetBlue cut capacity on EWR–RSW, EWR–TPA and EWR–LAX.
3. The elite period has one month of data.
4. Delta–Alaska elite perks predate its effect by about 9 years. The precedent supports "partner plus capacity," not "elite perks → switching."
5. To keep Mosaic credit, switchers must book United on jetblue.com, so JetBlue keeps the channel.
6. JetBlue's Q3 2026 results show loyalty revenue +20%, record elite qualifications, and an eightfold rise in premium-card sign-ups.
7. The detection date (Q4 2027 data, published March 2028) falls outside the catalyst window.
8. A JetBlue Northeast unit-revenue split doesn't appear in filings.
9. The EV/EBITDAR 9.2x multiple could not be reproduced.

**Extra analyses (all run).**
- **Randomization inference.** I reassigned "shared" to 300 random 12-route sets. The actual β₂ is larger than 99.7% of placebo draws (p=0.003). The positive result is not noise, and it is in the wrong direction.
- **YoY-differenced regression.** This nets out the pre-trend: β₁ +2.39 (1.58), β₂ +0.85 (1.86). Both are statistically zero. This is the cleanest read, and it says "no effect yet."
- **Fare and revenue placebo on DOT Table 1a.** Fares on the shared routes rose 4.8% relative to comparison routes in the miles-only period. That is a pricing-power story, the opposite of a leak.

**What to rerun, and when.**
- **T-100:** August–September 2026 data will be out around December 2026; Q4 2026 data around March 2027.
- **DOT Table 1a:** Q3 2026 will be out around February 2027. That makes Calc 4 possible for the elite period.
- Rerun `calc3.py`, `verify.py`, `tables.py` and `sizing.py` unchanged.

---

**Files.** All in the zip.
- `out/quarterly_effect_lf.csv`: quarterly effect, by period, with the 2σ band.
- `out/jetblue_lf_fare_revenue_by_quarter.csv`
- `out/calc7_scenarios.csv`: bear, base, bull and measured.
- `out/delta_alaska_quarterly_recomputed.csv` and `_annual_`
- `out/calc6_loss_per_switcher.csv`
- `out/calc8_equity.csv`
- `out/regression_lf.csv`
- `out/united_share_crosscheck.csv`
- `out/calc5_detection.csv`
- `out/route_sets.csv`
- `out/verification_table.csv`
- `src/`: raw T-100 and DOT extracts.
- Scripts: `prep.py`, `calc3.py`, `verify.py`, `tables.py`, `sizing.py`.
