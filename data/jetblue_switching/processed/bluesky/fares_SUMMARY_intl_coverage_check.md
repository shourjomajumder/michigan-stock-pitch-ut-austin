# JetBlue Thesis 1: live base-fare parity check, New York routes (2026-11-11)

Method: Google Flights, lowest posted nonstop economy fare, one-way from New York (all airports), JetBlue vs United. Two rounds: 12 routes x 4 dates (Dec 2026 - Jan 2027), then 40 route-sets x 4 dates via 20 agents (new routes Dec-Jan dates; re-tests on Feb-Mar 2027 dates). Raw data: rv/fares/agent_NN.*, rv/t1s2/live_jfk_ewr.*. Match = median gap within 10% and at least 3 of 4 dates within 10%.

## Verdicts
* MATCH (17 domestic): LAX (barely), SFO, FLL (cheapest NYC airport), PBI, TPA, RDU, SAN, BOS, ATL, JAX, CHS, SLC, MSY, CLE, BQN (barely), DEN and IAH (both only vs United LGA).
* NO MATCH: MCO and PHX (matched in round 1, failed on Feb-Mar dates), LAS, SJU, RSW, SRQ, SAV (JetBlue usually cheaper).
* NO DATA (no JetBlue nonstop on searched dates): ORD, BNA, SEA, SMF, PWM, BZN.
* International: match PUJ, MBJ (barely), NAS (borderline -9.6%); no match STI, SDQ, CUN, AUA, SXM, LHR, PLS, SJO. Blue Sky international coverage unconfirmed; excluded.

## Boston base correction
The old 2.338M Boston base counted any route with United passengers > 0 (e.g. BOS-LAS had 66 United passengers in a year). Real United competition from Boston: LAX, SFO, DEN, ORD, IAH (1.318M JetBlue pax). Live fares match on LAX, SFO, IAH = 1.026M.

## New passenger base (matched routes only)
Boston 1.026M + JetBlue Newark FLL/PBI 0.458M + 30% x JFK/LGA matched 5.400M (1.620M) = 3.104M.

## Implied JetBlue valuation (linear from the reverse-DCF model, implied WACC 12.95%; not yet rebuilt)
Blue Sky thesis -$0.43/share; base $3.51 (-10.9%); bear $3.30; bull $3.94; weighted $3.56 (-9.5%) vs $3.94. Window loss Q4'26-Q3'27 = $10.8M.
