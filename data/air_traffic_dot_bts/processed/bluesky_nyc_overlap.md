# 4 - Full New York metro overlap: JetBlue passengers on city pairs United also flies nonstop from NYC

Data: BTS TranStats T-100 Segment, CLASS F (scheduled pax), both directions summed, carriers B6 and UA, last 4 quarters available = Q3 2025 - Q2 2026 (Jul 2025 - Jun 2026). Page showed "Latest Available Data: July 2026" on 2026-11-11.
- Domestic (incl. SJU/BQN/PSE/STT): https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIM&QO_fu146_anzr=Nv4%20Pn44vr45 (T-100 Domestic Segment, U.S. Carriers)
- International: https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FJE&QO_fu146_anzr=Nv4%20Pn44vr45 (T-100 International Segment, All Carriers)
- NYC airports: JFK, LGA, EWR, HPN, ISP, SWF (JetBlue flies none from SWF). Routes with <12 departures in the year (diversions/one-offs), intra-NYC hops and PHL (tiny) dropped.
- Check: the JFK top-19 subset re-sums to 6,480,314 = the brief's 6.48M floor, and JFK route figures match (orig workspace) jfk/src/t100_jfk_top_b6_routes_L4Q_2025q3_2026q2.csv exactly.
- Row detail: (orig workspace) nyc/4_full_overlap.csv (route, B6 pax, match type, UA pax and departures from NYC to that destination, UA airport split, thin flag, in-floor flag).

Definitions
- Strict = same destination airport (e.g., JFK-LAX vs EWR-LAX). JetBlue's NYC origin can be any NYC airport.
- Metro = strict + same destination metro: LA basin (LAX/BUR/ONT/SNA/LGB), Bay Area (SFO/OAK/SJC), South Florida (FLL/MIA), Washington (DCA/IAD/BWI). PBI is kept as its own market.
- Thin = United has <250 departures from NYC on that pair in the year (under ~5 a week; e.g., BUF 235, ROC 62, SYR 78, PIT 22, DTW 194). United is not a real alternative on these.

## Headline totals (JetBlue passengers, Q3'25-Q2'26)

| Cut | Domestic | Change vs 6.48M floor |
|---|---|---|
| Brief's floor: JFK top 25, 19 overlap routes | 6,480,314 | - |
| JFK only, strict, all routes | 7,926,334 | +1.45M |
| JFK + LGA + EWR, strict | 10,459,421 | +3.98M |
| All NYC airports (adds HPN/ISP), strict | 12,078,630 | +5.60M |
| All NYC, strict, without thin routes | 11,459,912 | +4.98M |
| All NYC, metro | 12,234,996 | +5.75M |
| All NYC, metro, without thin routes | 11,616,278 | +5.14M |
| Memo: all JetBlue NYC domestic pax (any route) | 12,653,269 | |

So 95% of JetBlue's NYC domestic traffic is on a destination United also serves nonstop from NYC (91% if thin routes are dropped).

What the JFK-only strict number adds beyond the floor (+1.45M): ATL 258,869; SAN 187,608; ROC 123,054 (thin); ORD 120,117; BNA 119,312; SLC 94,297; SRQ 89,692; DTW 87,379 (thin); SYR 73,874 (thin); PIT 67,254 (thin); PWM 58,537; SEA 55,466; SMF 54,912; IAH 21,380; BZN 21,125; CLE 13,144. Note BUF (267,157) is inside the floor but United only runs about 235 flights a year EWR-BUF, so it is thin too.

By JetBlue NYC airport (domestic strict): JFK 7.93M; EWR 1.41M (100% overlap, same airport as United: MCO, FLL, PBI, LAX, SJU, TPA, RSW, LAS); LGA 1.12M (FL routes); HPN 1.24M; ISP 0.38M (all FL/SJU).

Metro-only additions (+156K): JFK-DCA 62,945 (UA EWR/LGA-IAD), JFK-ONT 52,845 and JFK-BUR 40,576 (UA EWR-LAX/SNA). LA basin note: JetBlue to LAX alone = 1,056,280 (JFK+EWR); LA basin = 1,149,701. United NYC-LAX 1,393,640; NYC-LA basin incl. SNA 1,655,431.

Domestic routes with no United NYC nonstop (418K): ACK (JFK/HPN/LGA 79K), BDL, PVD, DAB, ABQ, VRB, RNO, MVY, PSE, HYA, VPS, MHT.

## International (separate line, check whether Blue Sky reciprocity covers it)
- JetBlue NYC international: 6,044,158 pax. Strict overlap with a United NYC nonstop: 5,180,638 (4,375,949 without thin routes). Big ones: STI 808,684 (JFK+EWR), SDQ 607,045, PUJ 500,091, CUN 445,934, AUA 372,198, MBJ 233,637, SXM 182,881, LHR 164,608, NAS 143,029, PLS 112,709, SJO 101,826, GUA 100,458, CDG 83,220.
- Thin United options (POS, UVF, BGI, CUR, POP, ANU, SKB, BZE, TQO, BON) total about 805K.
- No United NYC nonstop: KIN 306,772, GEO 174,973, GYE 139,274, CTG 108,564, GND 108,317, SVD 25,620.
- Data note: JetBlue's seasonal JFK-MAD/BCN-type Europe flights did not appear in the extract for this window. United does fly EWR-MAD/BCN/FCO/LIS, so no overlap is counted there.

## Caveats
- T-100 counts segment passengers (connecting passengers included), not O&D. The DOT Table 1a O&D figures would be lower. The ratio is about the same on point-to-point leisure routes.
- HPN/ISP JetBlue flyers (1.62M) live in Westchester/Long Island, a long way from EWR, so substitution there is weakest. LGA/JFK to EWR is weaker than EWR to EWR.
- On hub routes (ORD, IAH, DEN) United's NYC capacity is huge, but JetBlue's JFK flyers there are often Delta/American-type travelers. These pairs are fine to include but add little (about 262K).

Best evidence for the pitch (1-3 bullets)
- Even on the narrowest definition (JFK only, same airport) the overlap is 7.93M, 1.45M above the 6.48M floor. The floor left out ATL, SAN, ORD, BNA, SLC, SRQ, SEA and others where United flies EWR nonstop.
- JetBlue's 1.41M EWR passengers are 100% on routes United also flies from the same airport. That is a direct substitute with no airport-switch question.
- Across all NYC airports, 12.08M (95%) of JetBlue's 12.65M NYC domestic passengers fly destinations United serves nonstop from NYC. Without thin routes it is 11.46M.

Evidence against
- 2.78M of the all-NYC number comes from LGA/HPN/ISP Florida flyers, whose switch to EWR is a real geographic stretch, especially from Westchester and Long Island.
- About 619K of strict domestic traffic (BUF, ROC, SYR, PIT, DTW) has fewer than 5 United flights a week from NYC. That is not a usable alternative.
- T-100 segment counts overstate local O&D on routes with connections.

Suggested haircut and why
- Defensible base: JFK+LGA+EWR strict without thin routes, about 9.84M (10,459,421 minus 619K thin). Count EWR at 100%, and haircut JFK/LGA by the airport-substitution factor from the other agents' evidence. Leave HPN/ISP and international out of the base and show them only as upside.
