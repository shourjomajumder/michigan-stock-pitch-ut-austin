# 10 - Was our 25-route switching correlation measured at the airport-pair or the city-market level?

Question: the 3.1%/yr loyalty-only switching rate comes from <workspace>/routes/parity.py, which writes parity_points.csv. Was it measured on airport pairs or on city markets, and is it consistent to apply it to New York city-market passengers (JFK flyers vs United at EWR)?

## Short answer
- All 25 points are **DOT Consumer Airfare Report city-market shares**, not airport-pair shares. 22 come from Table 6 (SODA yj5y-b2ir). The 3 CO/NW depth-1 points come from the Table 1 PDFs, which are also city-pair. Every source CSV labels them that way: r04 says "Boston citymarketid 30721", r05 says "citymarketid 30559 Seattle", r10 says "citymarketid_1=32575&citymarketid_2=31703", and r02 says "CAR Table 1 city-pair".
- So the **unit is consistent** with a New York city-market base. In fact the current model is the mixed one: it takes a city-market rate and applies it to an airport-pair base (2.338M from T-100 BOS-xxx airport pairs, bsky/out/route_sets.csv).
- But on almost every one of the 25 points, **the two competing carriers flew the same airports**. Most of the share that moved was won by a carrier at the same airport. The correlation was never tested on "JFK carrier loses to EWR carrier". It **neither supports nor refutes cross-airport switching**. It only tells us the measurement unit is compatible.

## How DOT defines the city markets used (verified)
Source: DOT Consumer Airfare Report Table 1a (airport-level), https://data.transportation.gov/resource/tfrh-tu9e.json, grouped by city and airport for 2019Q1 and 2019Q4 (fetched 2026-11-11). Table 6 rows label the city "Boston, MA (Metropolitan Area)", citymarketid 30721 (yj5y-b2ir, 2018Q1 fetch).
- New York City (31703): EWR, HPN, ISP, JFK, LGA, SWF
- Boston (30721): BOS, MHT, PVD
- Los Angeles (32575): BUR, LAX, LGB, ONT, SNA
- San Francisco (32457): OAK, SFO, SJC
- Miami (32467): FLL, MIA
- Washington (30852): BWI, DCA, IAD
- Houston (31453): HOU, IAH
- Chicago: MDW, ORD
- Dallas: DAL, DFW
- Cleveland (30647): CAK, CLE
- Tampa (33195): TPA, PIE
- Single-airport markets: Seattle (SEA), Detroit (DTW), Memphis (MEM), Cincinnati (CVG), Minneapolis (MSP), Salt Lake City (SLC), PHL, DEN, AUS, SAN, PDX, GEG, BOI, EUG, BUF, PIT, RDU, RIC, CHS, PBI, SAV
- PSC was not returned by the fetch; it is presumably a single-airport market.

## Precedent by precedent (25 points in parity_points.csv)
| Case (n pts) | Data / unit | Airports actually served by the two named carriers | Multi-airport issue? |
|---|---|---|---|
| Delta vs JetBlue, Boston (7: BUF, PIT, TPA, RDU, RIC, CHS, PBI), depth 0 | Table 6, Boston metro (BOS+MHT+PVD) vs city; TPA market includes PIE | Both DL and B6 at BOS | Metro denominator, but the pair competed at the same airport. MHT/PVD (mostly Southwest) only dilute the denominator. |
| Delta vs Alaska, Seattle (11: GEG, PDX, LAX, SFO, SAN, BOI, PSC, EUG, DEN, AUS, SLC), depth 0 | Table 6, citymarket 30559 (SEA only) | Both at SEA. LAX and SFO ends are 5- and 3-airport metros, where Alaska also flew secondary airports (BUR/ONT/SNA/LGB, OAK/SJC; my knowledge, not re-verified) | Only SEA-LAX and SEA-SFO involve multi-airport metros. Both show **negative** loss for the incumbent (-0.9, -2.1 %/yr). |
| JetBlue Mint vs United (1: NYC-LAX, 2013Q3-2015Q3), depth 0 | Table 6, NYC metro x LA metro | B6 at JFK (plus LGB/BUR). UA p.s. was **at JFK** until 25 Oct 2015, when it moved to EWR ([Business Traveller, 17 Jun 2015](https://www.businesstraveller.com/news/2015/06/17/united-to-move-out-of-jfk/): "On October 25, the carrier will move its p.s. premium service flights"). UA also flew EWR-LAX | The 25-point window ends 2015Q3, **before** the move, so the head-to-head was mostly JFK vs JFK. UA loss 0.24 %/yr. |
| Continental / Northwest (3: CLE-DTW, DTW-IAH, IAH-MEM), depth 1 (the only loyalty-only points) | DOT CAR Table 1 PDFs, city-pair. Cleveland market includes CAK; Houston includes HOU | CO and NW each flew the same hub-to-hub airport pair (CLE/IAH vs DTW/MEM) | None for the pair. HOU is a Southwest airport, not either partner's. |
| Delta / Continental / Northwest (2: CVG-IAH, MSP-SLC), depth 2 | Table 1 PDFs, city-pair | Same airports (CVG-IAH, MSP-SLC hub-to-hub) | None. |
| American / Alaska (1: SEA-PHL), depth 2 | Table 6, single-airport markets | SEA-PHL both | None. Shift was partner to partner. |
| American / JetBlue NEA | **Not in the 25.** a5_nea: Table 6 NYC/BOS city pairs | AA at JFK/LGA, B6 at JFK, UA rival at EWR | Multi-airport. NYC-CLT/DFW DiD peak about +9pp (k6-7), then -7.8pp after the unwind. Capacity was moved deliberately, so this cannot be read as switching. |
| Alaska / Virgin America | **Not in the 25.** r08 and a4: Table 6 metro pairs | VX at SFO; AS at SFO/OAK/SJC; rivals at EWR/IAD/DCA pooled | Multi-airport. a4 found "about 0 net loss" of merged share, with rival gains of 2.5-3.5 pts. |
| Continental (EWR) vs Northwest (LGA), New York | **Not in the 25.** a2: Table 6, NYC metro | CO at EWR hub; NW at LGA/JFK | This was the one true EWR-vs-other-NY-airport alliance test. MSP-NYC NW fell -3 to -4 at k1-k2, then Sun Country entry dominated. DTW-NYC NW dipped, then fully recovered by k4-k5. Neither was usable or included. GAO RCED-99-37: Detroit-Newark was 97% NW+CO (static). |

## Sensitivity
- The full fit gives a depth-1 prediction of **3.14 %/yr** (n=25). Dropping the 3 points where the carriers' airports could differ within a metro (SEA-LAX, SEA-SFO, NYC-LAX) gives **3.24 %/yr** (n=22). The rate is not driven by multi-airport points.
- Depth-1 group mean is 2.70 %/yr (n=3). All 3 are same-airport hub-to-hub routes.

## Related in-house observations on NY airport substitution
- a10: United's 2021-22 return to JFK (JFK-SFO/LAX) produced no visible change in UA's NYC-SFO metro share (33.7% 2019 avg vs 31.9-37.3%). After it left JFK, YoY moves were -0.1, -3.1, -4.8 and -1.9 pts (2023Q1-Q4).
  - Read for us: much of UA's NYC demand was captured at EWR anyway, which is mild support for the metro being one market.
  - Read against us: UA has no presence at JFK, so a JFK-loyal flyer has to change airports.
- a7: on Blue Sky so far, NYC-only DiD is k0 +2.20 (SE 2.21) and k1 +10.12 (SE 2.84). That is the wrong sign for switching, but the controls are just 3 small upstate markets.

## Conclusion
The correlation **is measured on a city-market basis**, so applying 3.1%/yr to New York city-market passengers is consistent in units. It is arguably more consistent than the current Boston airport-pair base. However, the switching in the sample happened almost entirely between carriers at the **same airports**. So the correlation does **not** show that a JFK flyer switches to Newark. It can defend the denominator (metro O&D share). It cannot defend the substitution assumption. That has to come from separate NY-airport substitution evidence (other agents' tasks).

## Best evidence for the pitch (1-3 bullets)
- Our 25 data points are DOT city-market shares, with New York defined as EWR+JFK+LGA+HPN+ISP+SWF. Using a city-market base for New York matches how the 3.1% was measured (Table 1a/6, data.transportation.gov tfrh-tu9e / yj5y-b2ir).
- Excluding the 3 points with possible cross-airport ambiguity barely moves the rate (3.14 to 3.24 %/yr). The two multi-airport metro points from Seattle (LAX, SFO) are not the source of the switching.
- United's JFK re-entry in 2021-22 did not move its NYC-SFO metro share (a10). This is consistent with UA's EWR service already competing for the same metro demand.

## Evidence against
- In 22+ of the 25 points both carriers flew the same airport pair. The correlation never observes a passenger switching airports, and Mint NYC-LAX was JFK vs JFK in the measured window.
- The only true EWR-vs-LGA alliance precedent (CO/NW 1998, NYC routes) was excluded as unusable. Detroit-New York NW recovered fully by k4-k5, and Alaska/Virgin (SFO/OAK/SJC) showed about 0 net loyalty loss.
- Blue Sky NYC city pairs so far show JetBlue doing *better* on shared routes (k1 +10 pts, a7). Capacity and other shocks dominate.

## Suggested haircut and why
The correlation gives no estimate of JFK-to-EWR substitution, so the haircut must come from the airport-substitution evidence. Until then:
- Apply the 3.1% at full weight only to JetBlue passengers where United flies the **same airport pair**: Boston, and any JFK/LGA routes United serves.
- Apply it to the 19 JFK-vs-EWR destinations with an explicit cross-airport factor. A **50%** placeholder (about 3.2M of the 6.48M) is the neutral midpoint. Show 0% and 100% as bounds, and tell the judges the rate itself is city-market-based but the cross-airport share is an assumption.
