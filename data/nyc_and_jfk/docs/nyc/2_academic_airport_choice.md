# 2. Academic evidence: airport choice and substitution in multi-airport regions (NYC focus)

Agent 2. All sources public, accessed 2026-11-11. Quotes kept under 15 words.

Question: does a JetBlue JFK flyer switch to United at Newark (EWR) when fares are at parity and United has the better product? What haircut should the 6.48M JFK passengers get?

Short answer: the literature says the New York airports are one market, but passengers switch airports less readily than they switch airlines. Access time (where you live) is usually the biggest driver of airport choice. Fare and product still matter, so the overlap is real but partial. 100% counting is too aggressive. Roughly 30-50% is defensible.

---

## Evidence 1. The only NYC airport cross-elasticity study: one market, but weak switching (Escobari 2017)

- Source: Diego Escobari, "Airport, Airline and Departure Time Choice and Substitution Patterns: An Empirical Analysis," MPRA Paper 79857 (June 2017), later in Transportation Research Part A, vol. 103 (2017), pp. 198-210. https://mpra.ub.uni-muenchen.de/79857/1/MPRA_paper_79857.pdf
- Data: online fares and seat sales, New York area to Toronto, 317 flights, December 2008. One city pair, so treat as illustrative.
- Method: random-coefficients logit (BLP-style), not nested logit.
- Own- and cross-price elasticities (Table 4; row = airport whose demand responds, column = airport whose price changes):

| | LGA price | JFK price | EWR price |
|---|---|---|---|
| LGA demand | -1.69 | 0.015 | 0.013 |
| JFK demand | 0.012 | -1.44 | 0.014 |
| EWR demand | 0.011 | 0.016 | -1.23 |

- Quote: the three airports "can be considered as a single market."
- Quote: "JFK and Newark appear to be relatively closer substitutes." JFK-EWR is the largest cross-elasticity pair (0.014-0.016). This is the pair that matters for the pitch.
- AGAINST: consumers "are more willing to switch to an alternative carrier than to switch between airports." Cross-elasticities are about 1% of own-elasticities. Caveat: the price coefficient is imprecise (mean -0.903 per $100, SE 0.662), and cross-elasticities in logit models are mechanically small when each product's share is small.

## Evidence 2. Market definition: researchers group the NYC airports (Brueckner, Lee and Singer 2014)

- Source: Brueckner, Lee and Singer, "City-Pairs Versus Airport-Pairs: A Market-Definition Methodology for the Airline Industry," Review of Industrial Organization 44(1), 2014, pp. 1-25. Abstract: https://ideas.repec.org/a/kap/revind/v44y2014i1p1-25.html
- Finding (abstract): "strong evidence" that city-pairs are the right market definition for "many (but not all)" large metro areas (2003-2009 quarterly panel).
- NYC grouping (secondary source): Luttmann (UC Irvine dissertation 2019, published IJIO vol. 62) takes adjacent-airport groups "from Brueckner et al. (2014)". The New York entry has LGA as primary, with EWR and JFK as adjacent. https://escholarship.org/content/qt14c1b0d4/qt14c1b0d4.pdf . I could not open the paywalled original table. Check it if a judge asks.
- Industry and antitrust practice also uses city-pair markets that include "multiple airports within a city or metropolitan area" (Analysis Group, Oct 2022). Their caveat: grouping "should therefore be considered on a case-by-case basis." https://analysisgroup.com/link/3ce4be30684f4ed8a5b75489e5b6f6da.aspx

## Evidence 3. Adjacent-airport fare discipline: real for LCCs, near zero for legacy carriers (Brueckner, Lee and Singer 2013)

- Source: Brueckner, Lee and Singer, "Airline competition and domestic US airfares: A comprehensive reappraisal," Economics of Transportation 2(1), 2013, pp. 1-17. Abstract: https://econpapers.repec.org/RePEc:eee:ecotra:v:2:y:2013:i:1:p:1-17 . Effect table summarized by IATA: https://www.iata.org/en/iata-repository/publications/economic-reports/network-vs.-lcc-competition-and-airfares-new-us-empirical-evidence

| Competitor (base model, YE 2008-Q2) | Fare effect |
|---|---|
| In-market Southwest | -29.3% |
| In-market other LCC | -12.6% |
| Adjacent-airport Southwest | -12.7% |
| Adjacent-airport other LCC | -4.7% |
| Adjacent-airport legacy carrier | not significant |
| In-market extra legacy carrier | not significant |

- Read: adjacent airports compete. An LCC at a nearby airport cuts fares about 40% as much as one on the same airport pair (12.7/29.3 for Southwest; 4.7/12.6 for other LCCs is about 37%).
- AGAINST: in the 2008 data, a legacy carrier (United is one) at an adjacent airport has no significant fare effect. Abstract: legacy competition has "weak effects on average fares." So United at EWR may not pressure JetBlue's JFK fares much. The 2000 market-weighted model did find -5.4% for adjacent legacy, but IATA's text and table disagree on the sign.
- Useful framing: an adjacent-airport rival is worth about 0.4x an on-airport rival. That supports a 30-50% weight.

## Evidence 4. What it takes to make someone switch airports: dollar trade-offs (Hess, Adler and Polak 2007)

- Source: Hess, Adler and Polak, "Modelling airport and airline choice behaviour with the use of stated preference survey data," Transportation Research Part E 43(3), 2007, pp. 221-233. US domestic stated-preference survey, May 2001, 589 respondents. https://eprints.whiterose.ac.uk/5435/1/Hesss6pdf.pdf (Tables 4-5)

| Willingness to pay ($ per trip, 2001) | Business | Holiday | VFR |
|---|---|---|---|
| 1 hour less airport access time | 75.40 | 35.80 | 35.48 |
| On-time performance +10 points | 10.39 | 7.02 | 5.57 |
| FF elite vs none | 125.24 | n.s. | n.s. |
| FF standard vs none | 49.12 | n.s. | n.s. |
| Top airline vs worst | n.s. | 25.07 | 21.06 |
| Top airport vs worst | 83.22 | 53.97 | 55.73 |
| Airport closest to home | - | - | 28.02 |

- $1 of fare equals 2.1 minutes of access time for business and about 4.6 minutes for leisure (Table 5).
- Implication for the pitch (my arithmetic): fares are at parity, so a leisure JFK flyer switches only if United's product gain beats the extra trip to Newark. A 10-point on-time edge is worth about $6-7. 30 extra minutes of access time costs about $18 for leisure. So a Brooklyn, Queens or Long Island leisure flyer should NOT switch. A Manhattan or New Jersey flyer, for whom EWR is about as close as JFK or closer, plausibly does.
- Supports the pitch: for leisure travelers the frequent-flyer effect is not significant. Airline loyalty mainly holds elite business flyers ($125). Blue Sky also lets TrueBlue members earn on United, which removes even that barrier. Quote: airline allegiance is "primarily limited to membership in frequent flier programmes."
- Caveat: stated-preference surveys may overstate responsiveness. All figures are in 2001 dollars.

## Evidence 5. Access time dominates, and passengers are "captive" to their local airport (Hess-Polak; Ishii-Jun-Van Dender; Pels-Nijkamp-Rietveld; Gupta et al.)

- Hess and Polak (2006), London, 5 airports, business travelers (TR-E 42(2), pp. 63-81): https://eprints.whiterose.ac.uk/5432/1/hesss5.pdf . Access time is "a prime determining factor." Fare was not significant. Passengers "are highly captive to their local airport." Value of access time is about GBP 16/hr.
- Hess and Polak (2005), SF Bay Area (JATM 11(2)): https://eprints.whiterose.ac.uk/id/eprint/5430/1/hesss4.pdf . Fare, frequency and access time are the consistently significant drivers. Willingness to pay for one extra daily flight (at a base of 5) is $7-12.
- Ishii, Jun and Van Dender (2006 working paper; Bay Area to LA, 1,752 travelers): https://www.economics.uci.edu/files/docs/colloqpapers/f06/VanDender.pdf . Consumers "choose among imperfect airline-airport substitutes." A 5-minute cut in SFO access time raises SFO share from 29.3% to 35.7%. Small access changes move share a lot, so geography decides who switches.
- Pels, Nijkamp and Rietveld (2001), Regional Studies 35(1): https://econpapers.repec.org/RePEc:taf:regstd:v:35:y:2001:i:1:p:1-9 . The best model has passengers choose the airport first, then the airline (airport-level nests). Frequency and access time are significant. That ordering argues against easy cross-airport airline switching.
- Gupta, Vovsha and Donnelly (2008), the New York region specifically (TRR 2042, pp. 3-11; https://www.worldtransitresearch.info/research/195): average yield (fare), access time and access cost are "the strongest determinants." A plain MNL fit better than airport-on-top nesting, a mild sign that NYC airports are closer substitutes than in nested markets. Coefficients are paywalled.

## Evidence 6. NYC natural experiment: the 2025 Newark meltdown (revealed preference, recent)

- Reuters (Doyinsola Oladipo), May 23, 2025, republished: https://www.hotel-online.com/news/demand-traffic-falls-at-newark-airport-following-outages
  - Kayak: travelers choosing Newark as arrival airport down 19%, departure down about 15%, after April 28, 2025.
  - Data Appeal: EWR arrivals down about 13% YoY, LGA up 5.7% (Apr 28-May 20).
  - Kayak CEO preference order: "LaGuardia ... number one pick, then JFK and then Newark."
- WSJ (Sider, Pohle), May 16, 2025: https://www-web.itiger.com/news/2535136591 . TravelPerk's JFK booking share up 4 percentage points within weeks. United cut about 10% of its EWR schedule.
- Supports the pitch: when quality diverges sharply, about 15-19% of NYC demand shifts between airports within weeks. NYC flyers do treat the airports as substitutes in practice.
- AGAINST, and important: the shift ran away from Newark and toward JFK and LGA. EWR has the region's weakest recent reliability reputation, and Kayak's data puts Newark last. This undercuts "United has the better product" for a JFK to EWR move. A judge can cite it. A Reuters anecdote also shows a flyer staying on United because of status, which cuts the other way: loyalty is sticky.

---

## Best evidence for the pitch (1-3 bullets)

- NYC is one market: Escobari (2017) says the three airports "can be considered as a single market," with JFK-EWR the closest substitute pair. Brueckner, Lee and Singer (2014) support grouping city-pairs, and NYC airports are grouped in their adjacent-airport scheme.
- Loyalty is not the barrier for leisure flyers: in Hess, Adler and Polak (2007), frequent-flyer membership is not significant for holiday or VFR travelers, and only elite business flyers show strong loyalty ($125). Blue Sky lets TrueBlue members earn on United, so even that barrier falls.
- Revealed switching is fast and large: after the April 2025 EWR outages, Newark bookings fell 15-19% (Kayak) and LGA arrivals rose 5.7% within about 3 weeks.

## Evidence against

- Passengers switch carriers more readily than airports (Escobari 2017). NYC cross-airport price elasticities are only about 0.011-0.016.
- A legacy carrier at an adjacent airport has no significant fare effect (BLS 2013, 2008 data). United at EWR may not discipline JetBlue at JFK.
- Access time dominates airport choice. Passengers are "highly captive to their local airport" (Hess and Polak 2006). JFK's core catchment (Brooklyn, Queens, Long Island) is 30-60+ minutes farther from EWR. For leisure travelers, that costs about $18-36 per trip in access-time value, more than a 10-point on-time edge (about $6-7).
- Newark's 2025 reliability crisis (outages, FAA-mandated cuts, Kayak preference order LGA > JFK > EWR) weakens "United has the better product" for NYC specifically.
- Missing piece: I found no public origin-ZIP survey showing what share of JFK passengers live closer to EWR. ACRP Report 98 (2013) and the 2007 FAA/PANYNJ regional studies probably have it, but the proxy blocked them (nationalacademies.org, onlinepubs.trb.org, webarchive.library.unt.edu).

## Suggested haircut and why

- Don't count the 6.48M at 100%. Base case: about 40% of the JFK overlap (about 2.6M passengers). That makes the shared-route base about 4.9M instead of 8.8M (2.338M Boston + 2.6M NYC). Bear and bull cases: 25% (1.6M) and 60% (3.9M).
- Why 40%:
  1. BLS (2013): adjacent-airport LCC competition has about 0.37-0.43x the fare effect of same-airport competition (4.7/12.6 and 12.7/29.3).
  2. Hess, Adler and Polak (2007) access-time trade-offs: only flyers for whom EWR is about as convenient as JFK (Manhattan, Staten Island, NJ, parts of Brooklyn) will switch at fare parity for a modest product edge.
  3. Escobari (2017): JFK-EWR is the closest NYC pair, but airport switching is weaker than carrier switching.
- Alternative framing that judges may find cleaner: keep the full 8.8M base, but apply a lower drift rate to the NYC block. Use 0.4 x 3.1% = about 1.2% per year (eventual about 2.4%) for JFK/EWR overlap passengers, versus the full 3.1% for Boston airport-pair overlap.
- Re-run the short at the 40% weight before presenting. Moving from 2.3M to about 4.9M in base passengers is a bit more than half of the jump to 8.8M. Whether the short goes negative depends on the model; I did not re-run it.
