# Agent 04: On-time performance, cancellations and airline demand/share

Angle: academic and industry evidence on how OTP/cancellations move demand and share; translate a 6.6-pt OTP gap (United 77.6% vs JetBlue 71.0%) into an implied share shift.

## Sources and verbatim quotes

### 1. Gayle & Yimga, "How much do Consumers really Value Air travel On-time Performance..." (Economics of Transportation, forthcoming; draft dated Dec 1, 2017). Data: DB1B + BTS On-Time, Q1 2002 to Q4 2012
URL: https://www.k-state.edu/economics/pdfs/websitefiles/gayle/Manuscript_Gayle_Yimga_website.pdf
- "Our demand estimates show that consumers are willing to pay $1.56 per minute late to avoid delay." (p. 6)
- "The mean own elasticity of arrival delay minutes is -0.256." / "a 10% increase in a product's arrival delay minutes causes consumers to decrease their demand for the product by 2.56%." (p. 26)
- "The mean cross elasticity of arrival minutes late is 0.004." (p. 27) -> authors read this as some customers switching to rival airlines, but the cross effect is very small.
- Table 5: cutting arrival delay minutes by 10% raises demand 2.39%; 25% -> 6.10%; 50% -> 12.64%; 75% -> 19.66%; 100% -> 27.21%.
- Mean minutes late per product: 12.31 (Table 3).
- 2SLS coefficients: arrival minutes late -0.0109; price -0.0070.

### 2. Suzuki (2000), "The relationship between on-time performance and airline market share: a new approach," Transportation Research Part E 36(2):139-154
URL: https://ideas.repec.org/a/eee/transe/v36y2000i2p139-154.html
- "the passengers who experienced flight delays are more likely to switch airlines for the subsequent flight than those passengers who did not experience delays."
- "on-time performance affects a carrier's market share primarily through the passengers' experience, and not though the "advertisement" of performance."
- No numeric transition probabilities in public abstract; full text is paywalled (not accessed). Implication: DOT rankings themselves do not drive share; what matters is how many JetBlue passengers personally get delayed.

### 3. Mazzeo (2003), "Competition and Service Quality in the U.S. Airline Industry," Review of Industrial Organization 22:275-296 (BTS data, 2000)
URL: https://www.kellogg.northwestern.edu/faculty/mazzeo/htm/airline_ontime.pdf
- "both the prevalence and duration of flight delays are significantly greater on routes where only one airline provides direct service."
- Monopoly routes run ~1.35 min later on average (Table III coefficient 1.353).
- Citing Suzuki: "the consequences of poor on-time performance can be substantial in competitive markets."
- Counterweight: "there is no evidence that relatively poor on-time performance has driven any firm out of a particular city-pair market."

### 4. Forbes (2008), "The effect of air traffic delays on airline prices," IJIO 26(5):1218-1232 (LaGuardia natural experiment), as quoted by later papers
- Bilotkach & Lakew (Feb 2019), https://pauloslakew.github.io/research/BilotkachLakew_Feb2019.pdf : "Her study suggested that average airfares drop by $1.42 in response to an extra minute of delay."
- Fageda & Flores-Fillol (Nov 2015), https://diposit.ub.edu/dspace/bitstream/2445/107690/1/657514.pdf : "$1.42 for direct passengers"; $0.77 for connecting passengers.
- Bilotkach & Lakew own estimate: "a one-minute increase in delays is associated with a $1.97-2.25 drop in average fares."
- Meaning: carriers with worse delays must discount to hold load factor. Penalty shows up in yield, not only in share.

### 5. Ferrer, Rocha e Oliveira & Parasuraman (2012), "The behavioral consequences of repeated flight delays," J. Air Transport Management 20:35-38
URL: https://ideas.repec.org/a/eee/jaitra/v20y2012icp35-38.html
- "passengers who have experienced delays fly less than passengers who have not experienced any delay."
- The effect is "convex in the number of delays experienced, stronger in members of the frequent flyer program," and "non-decreasing in time." (Abstract has no numbers; full text not accessed.)
- Relevance: switching builds up over time and with repeated delays, which fits a 1-2 year window. It hits loyalty members hardest, and Blue Sky lets those members earn and burn on United.

### 6. OAG traveler survey (Business Wire, Jun 1, 2023). Stated preference, not observed behavior
URL: https://www.businesswire.com/news/home/20230601005149/en/Travel-Habits-and-Loyalty-Shaped-by-Age-and-Disruption-OAG-Survey-Reveals
- "Thirty-seven percent of all travelers changed their airline loyalty due to having experienced significant delays or cancellations in the past year."
- Millennials: "42% switching their airline loyalty because of a significant delay or cancellation."

## Translation: what does a 6.6-pt OTP gap imply? (our arithmetic, not from any paper)

A. Elasticity route (Gayle & Yimga)
- Late-flight share: JetBlue 29.0% vs United 22.4%. JetBlue is late (29.0/22.4 - 1) = ~29% more often. Using "late share" as a proxy for delay minutes, JetBlue carries ~29% more delay.
- Own elasticity -0.256 x 29% = ~7.5% lower demand for a JetBlue product than one with United-level delays, all else equal.
- Caveat 1: this is a static level effect against all alternatives, including not flying. The cross elasticity (0.004) says only a small slice goes to any one rival.
- Caveat 2: the gap has existed for years, so today's shares already reflect it. The OTP gap does not produce new switching by itself. It only adds switching once something lowers switching costs, which is the Blue Sky thesis. So ~7.5% is best read as a ceiling on the OTP-driven part of demand.
- WTP framing: $1.56/min (Gayle-Yimga) or $1.42/min (Forbes). Each 5 min of extra average delay is worth ~$7-8 per trip to the customer. At equal base fares, that is a real price advantage for United.

B. Experience route (Suzuki / Ferrer / OAG)
- Per trip, an extra 6.6% of JetBlue passengers get delayed compared with United.
- If 10-37% of delayed passengers defect (37% is the OAG stated figure, an upper bound), the incremental defection is 6.6% x 10-37% = ~0.7-2.4% of passengers per trip-cycle.
- Repeat flyers taking 3-5 trips over 1-2 years compound this to roughly 2-10% (illustrative, not estimated). Ferrer says the effect is convex and non-decaying, which supports the higher end for frequent flyers.

Bottom line: the OTP literature bounds the OTP-driven switching rate at roughly 2-8% over 1-2 years. The 10% base case needs the other levers too (Wi-Fi, network, loyalty reciprocity). OTP alone looks below 10%.

## Time series
None found that can go straight into a line graph. The Gayle-Yimga Table 5 curve (delay reduction 10/25/50/75/100% -> demand +2.39/6.10/12.64/19.66/27.21%) can be plotted as a dose-response line. For a real time series, use BTS monthly on-time % for B6 vs UA (transtats.bts.gov), not pulled here.

## Not accessed
Suzuki (2000) full text (paywalled, so no transition probabilities); Forbes (2008) original (paywalled, so the figure is quoted via citing papers); Ferrer et al. numeric effect sizes.
