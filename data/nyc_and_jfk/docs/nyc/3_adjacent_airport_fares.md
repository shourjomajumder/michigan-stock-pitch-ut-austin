# 3. Adjacent-airport competition: are JFK, EWR and LGA one fare market?

Agent 3. Researched 2026-11-11. Public sources only. All quotes are under 15 words.

## 1. DOT counts all NYC airports as one city market (Table 1), but not airport by airport (Table 1a)

Source: US DOT, *Domestic Airline Consumer Airfare Report*, Q1 2026 (posted Sept 2026).
https://www.transportation.gov/sites/dot.gov/files/2026-09/Domestic%20Airfare%20Consumer%20Report%202026q1_0.pdf

- **Table 1** lists city-pair markets labeled "New York City, NY (Metropolitan Area)". **Table 1a** "breaks out markets by specific airport-pairs" and is published only on the DOT DataHub, so it is not in the PDF. I could not pull JFK-LAX and EWR-LAX separately.
- **Which airports DOT groups.** The PDF has no list of the airports. The report's own Table 7 (airport level, Q1 2026) gives the answer by arithmetic:

| Airport | Q1 2026 passengers | Avg fare |
|---|---|---|
| JFK | 3,691,186 | $314 |
| LGA | 5,080,162 | $241 |
| EWR | 5,244,674 | $282 |
| HPN | 411,614 | $256 |
| ISP | 289,717 | $200 |
| SWF | 39,423 | $119 |
| **Sum** | **~14.76M** | |
| NYC metro city-market total (same report) | 14,350,371 | $272 |

  The six airports add up to roughly the metro total; the small gap is probably due to market-size cutoffs. So DOT's NYC city market contains EWR (and HPN, ISP, SWF), not just JFK and LGA. EWR is the largest of the six by passengers.
- **Table 1 rows show United's Newark traffic inside the "New York" market (Q1 2026):**

| City market | Pax/day | Avg fare | Largest carrier | Low-fare carrier |
|---|---|---|---|---|
| NYC - Los Angeles | 10,752 | $454 | **UA 31%** | B6 17% ($359) |
| NYC - San Francisco | 7,028 | $518 | **UA 37%** | AS 13% ($293) |
| NYC - Las Vegas | 4,232 | $369 | **UA 37%** | B6 24% ($305) |
| NYC - Orlando | 12,092 | $190 | B6 27% | NK 10% ($115) |

  LaGuardia's 1,500-mile perimeter rule keeps it out of LAX, SFO and LAS. United's New York transcontinental flying is at Newark, so a 31-37% United share in these markets is EWR traffic. DOT therefore reports JetBlue (JFK) and United (EWR) as competitors in a single NYC-LAX, NYC-SFO and NYC-LAS market.
- FLL and SJU have no NYC row in Table 1. FLL is probably folded into a Miami metro market, and SJU falls outside the table's 48-state scope.

**Use in pitch:** the federal government's own fare statistics treat a JFK-LAX JetBlue flyer and an EWR-LAX United flyer as the same market.

## 2. Academic evidence that NYC airports form one market (Escobari 2017)

Source: Diego Escobari, "Airport, airline and departure time choice and substitution patterns: An empirical analysis," *Transportation Research Part A* 103 (2017) 198-210. Open version: https://mpra.ub.uni-muenchen.de/79857/1/MPRA_paper_79857.pdf

- The data are ticket-level NYC-Toronto trips from JFK, LGA and EWR to YYZ, estimated with a random-coefficients logit model.
- Conclusions:
  - "these three New York City area airports can be considered as a single market" (p. 19)
  - JFK and Newark "appear to be relatively closer substitutes" (p. 19)
- Airport cross-price elasticities (Table 4, p. 35):
  - JFK share with respect to EWR price: 0.0143
  - EWR share with respect to JFK price: 0.0160
  - These are the largest airport-to-airport pairs in the table.
- **Cuts against:** consumers are "more willing to switch to an alternative carrier than between airports" (abstract). The airport cross-elasticities (0.011-0.016) are small in absolute terms, and the sample is one international short-haul route.

## 3. Brueckner, Lee & Singer (2013): adjacent-airport competition and fares

Source: Brueckner, Lee & Singer, "Airline competition and domestic US airfares: A comprehensive reappraisal," *Economics of Transportation* 2(1), 2013, 1-17. https://econpapers.repec.org/RePEc:eee:ecotra:v:2:y:2013:i:1:p:1-17
Coefficients as summarized by IATA: https://www.iata.org/en/iata-repository/publications/economic-reports/network-vs.-lcc-competition-and-airfares-new-us-empirical-evidence

- Abstract: LCC competition "has dramatic fare impacts, whether it occurs on the airport-pair, at adjacent airports," or as potential competition.

| Competitor at an adjacent airport | Fare effect, YE 2008-Q2 (base / market-weighted) | 2000 |
|---|---|---|
| Southwest nonstop | -12.7% / -17.0% | -38.7% |
| Other LCC nonstop | -4.7% / -6.4% | n.s. |
| **Extra legacy/network carrier** | **not significant** | -5.4% |

- **Supports the pitch:** fares at one airport do respond to competition at a neighboring airport in the same metro. The model would define a JFK route as "adjacent" to the matching EWR route.
- **Cuts against:** United is a network carrier. In the 2008 data, an extra network carrier at the adjacent airport had **no significant fare effect**, so this paper does not show that United at EWR disciplines JFK fares. Our thesis is about loyalty-driven passenger switching, not fare discipline, so this is not fatal. Still, do not cite this paper as "United at EWR constrains JetBlue at JFK".

Related: Morrison (2001), *J. Transport Economics & Policy* 35(2), found Southwest's actual, adjacent and potential competition saved travelers $12.9B in 1998, of which $9.5B came from rivals' fare responses (https://ideas.repec.org/a/tpe/jtecpo/v35y2001i2p239-256.html). This is general precedent that adjacent-airport effects exist. It has nothing NYC-specific.

## 4. The strongest counter-evidence: DOJ, using JetBlue's own documents, said EWR is NOT a domestic substitute

Source: *US et al. v. American Airlines & JetBlue* (NEA) complaint, D. Mass. No. 1:21-cv-11558, filed 2021-09-21. https://www.mass.gov/doc/northeast-alliance-complaint/download

- ¶42 (p. 17): "Ground transport times can vary significantly for airports within the same metropolitan area." DOJ argues that airlines price each airport separately.
- ¶45 (p. 18), headed "JFK and LaGuardia (for Domestic Travel)": many JFK/LGA passengers "do not view service to Newark Liberty as a reasonable substitute."
  - The complaint cites **JetBlue's own** description of EWR as having a distinct catchment area that "does not largely overlap with LGA."
- ¶46 (pp. 18-19): for **transatlantic** trips, DOJ does group JFK, LGA and EWR, citing "longer flight times and the need to go through customs."
- Implication: the longer the trip, the more substitutable the airports, and judges may know this case. The 1st Circuit upheld the NEA ruling in 2024, and JetBlue was the defendant. Expect a judge to ask why JetBlue's own documents said Newark is a different catchment.

## Best evidence for the pitch
- **DOT Table 1 (Q1 2026)** puts JFK and EWR in one "New York City" market. United is the largest carrier on NYC-LAX (31%), NYC-SFO (37%) and NYC-LAS (37%), with JetBlue in the same rows. The government's fare data counts JetBlue and United as head-to-head.
- **Escobari (2017, TR-A)** concludes the NYC airports "can be considered as a single market," and JFK and EWR are the closest-substituting pair.
- **Brueckner-Lee-Singer (2013)**: competition at adjacent airports measurably moves fares (up to -17% for Southwest), so the industry-standard model treats metro airports as linked.

## Evidence against
- The DOJ NEA complaint (2021, ¶45) quotes JetBlue saying Newark's catchment is distinct, and treats EWR as **not** a domestic substitute for JFK/LGA.
- In Brueckner-Lee-Singer, an extra **network** carrier at the adjacent airport had no significant fare effect in 2008. There is no evidence that United at EWR disciplines JFK fares.
- Escobari: travelers switch carriers more readily than airports, and the airport cross-elasticities are small.
- I could not obtain Table 1a airport-pair data (DataHub only), so the JFK and EWR splits within each city market are not shown here.

## Suggested haircut and why
- **Do not count 100% of the 6.48M.** The DOJ/JetBlue "distinct catchment" language means the airports are partial substitutes, not equivalents.
- **Tier by stage length**, following DOJ's own ¶46 logic that longer trips make the airports more substitutable:
  - Long-haul / transcon markets that LGA cannot serve (LAX, SFO, LAS, PHX, DEN, plus SJU/BQN): count **~50%**. DOT already scores these as one market, and United leads them.
  - Short and medium-haul East Coast and Florida markets (MCO, FLL, PBI, TPA, RSW, JAX, BOS, BUF, RDU, CHS, SAV, MSY): count **~25%**. Ground access dominates the airport choice on these trips, and LGA is a closer substitute for JFK than EWR is.
- I do not have per-route passengers, so I applied the tiers as a blended **~33-40%** of 6.48M, or about **+2.1M to +2.6M**. That lifts the base from 2.338M to roughly **4.5-4.9M**, instead of the full 8.8M.
- The parent should re-run the model with per-route pax and the tiers. This is defensible against a judge who cites the NEA case, and it still raises the base about 2x.
