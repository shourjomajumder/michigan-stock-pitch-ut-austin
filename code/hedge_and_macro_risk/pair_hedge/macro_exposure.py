"""Exposure after the hedge: the four non-oil risk boxes (appendix 'Correlation With Each Risk', deck 'Exposure').

    cd processed && python ../code/macro_exposure.py

Pair = long $1 Frontier (ULCC) / short $H JetBlue (JBLU). Positive = the pair gains when the shock hits.
Box             Slide value  How it is built here
Wage inflation  +10.8%       one year of a 5% rise in FY2025 salaries, wages & benefits / market cap, netted
Credit stress   +6.5%        HYG -5% in a month through factor betas; midpoint of assumed-vol (+5.3%) and
                             measured-vol (+7.7%) cases
Interest rates  +3.5%        +100bp on floating debt plus refinancing 2027-28 maturities at +100/+200bp,
                             one year of pre-tax earnings / market cap; range +2.7% to +3.7%, slide rounds to 3.5
Demand shock    -4.5%        historical sudden-demand episodes (Mar 2020, 2020 high-to-low, 2025 tariff scare):
                             -2.7% to -5.7%; slide uses the middle of the -3% to -6% read
All inputs are public (Yahoo closes, SEC 10-K/10-Q/8-K figures, our own correlations). Factor vols marked ASSUMED
are our assumptions; 'measured' vols are realized 60-day vols read from public option-analytics pages.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

H = 1.16                                     # rounded ratio used in the slide's wage stack
_f = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0)
HX = np.polyfit(_f.jet_fuel, _f.frontier, 1)[0] / np.polyfit(_f.jet_fuel, _f.jetblue, 1)[0]   # 1.163, used below
# ---------------- wage inflation (appendix stack, recomputed) ----------------
swb = {'ULCC': 249 + 254 + 251 + 262, 'JBLU': 863 + 852 + 865 + 874}  # FY2025 SWB $M, quarterly 10-Q/10-K figures
price = {'ULCC': 8.35, 'JBLU': 3.94}                                  # Yahoo close 9 Nov 2026
shares = {'ULCC': 230.24, 'JBLU': 377.3}                               # M shares, Q3 2026 10-Q
u = -0.05 * swb['ULCC'] / (price['ULCC'] * shares['ULCC'])
j = -0.05 * swb['JBLU'] / (price['JBLU'] * shares['JBLU'])
wage = u - H * j
print(f'wage +5%: Frontier {u:+.2%}  JetBlue {j:+.2%}  pair {wage:+.1%}  (SWB {swb})')

# ---------------- credit stress: factor betas from correlations x vols ----------------
px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_prices.csv'), index_col=0, parse_dates=True)
r = px.pct_change().dropna().loc['2025-11-04':'2026-10-27']
sU, sJ = r.frontier.std() * np.sqrt(252), r.jetblue.std() * np.sqrt(252)
sP = (r.frontier - HX * r.jetblue).std() * np.sqrt(252)
corr = {'SPY': (0.422, 0.451), 'JETS': (0.770, 0.757), 'XLY': (0.424, 0.468),   # |corr| of daily returns,
        'IWM': (0.501, 0.521), 'HYG': (0.411, 0.489)}                           # a5_corr.py / same window
vol_assumed = {'SPY': .13, 'JETS': .336, 'XLY': .20, 'IWM': .22, 'HYG': .065}
vol_measured = {'SPY': .13, 'JETS': .336, 'XLY': .175, 'IWM': .195, 'HYG': .045}
def beta_pair(f, v):
    ru, rj = corr[f]
    return (ru * sU - HX * rj * sJ) / v[f]
shock = -0.05                                                                 # HYG -5% over one month
credit_lo, credit_hi = beta_pair('HYG', vol_assumed) * shock, beta_pair('HYG', vol_measured) * shock
credit = (credit_lo + credit_hi) / 2
rows = [dict(factor=f, beta_pair_assumed_vol=beta_pair(f, vol_assumed), beta_pair_measured_vol=beta_pair(f, vol_measured),
             factor_vol_assumed=vol_assumed[f], factor_vol_measured=vol_measured[f]) for f in corr]
pd.DataFrame(rows).round(4).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/macro_factor_betas.csv'), index=False)
print(f'credit (HYG -5%): {credit_lo:+.1%} (assumed vol) to {credit_hi:+.1%} (measured vol), midpoint {credit:+.1%}')

# ---------------- interest rates: floating debt + refinancing, one year of pre-tax earnings ----------------
close = px.iloc[-1]                                                           # Yahoo close 2 Nov 2026
co = {'ULCC': dict(px=close.frontier, sh=230.4176, flt=320, m27=102, m28=39),  # $M; ULCC Q3 2026 10-Q
      'JBLU': dict(px=close.jetblue, sh=377.3, flt=2000, m27=477, m28=582)}    # $M; JBLU 10-Q Item 3, Q3 release
def hit(d, refi_bp):
    mc = d['px'] * d['sh']
    return -(d['flt'] * 0.01 + (d['m27'] + d['m28']) * refi_bp / 1e4) / mc
rates_lo = hit(co['ULCC'], 100) - HX * hit(co['JBLU'], 100)
rates_hi = hit(co['ULCC'], 200) - HX * hit(co['JBLU'], 200)
print(f'rates (+100bp floating, refi +100/+200bp): {rates_lo:+.1%} to {rates_hi:+.1%}  -> slide +3.5%')

# ---------------- sudden demand shock: past episodes (pair = r_long - HX * r_JBLU) ----------------
eps = [('Mar 2020, Spirit as ULCC proxy', -0.547, -0.433),                      # monthly returns, March 2020
       ('2020 high to low, Spirit as proxy', 7.2368 / 40.2765 - 1, 6.86 / 21.56 - 1),
       ('2025 tariff scare, Jan high to Apr low', 2.79 / 10.26 - 1, 3.425 / 8.09 - 1)]
ep = pd.DataFrame([dict(episode=n, long=a, jblu=b, pair=a - HX * b) for n, a, b in eps])
ep.round(4).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/macro_demand_episodes.csv'), index=False)
demand = ep.pair.mean()
print(ep.round(3).to_string(index=False))
print(f'demand shock: range {ep.pair.max():+.1%} to {ep.pair.min():+.1%}, mean {demand:+.1%}  -> slide -4.5%')

box = pd.DataFrame([('Wage inflation', wage, wage), ('Credit stress', credit_lo, credit_hi),
                    ('Interest rates', rates_lo, rates_hi), ('Sudden demand shock', ep.pair.max(), ep.pair.min())],
                   columns=['risk', 'low', 'high'])
box['slide'] = [0.108, 0.065, 0.035, -0.045]
box.round(4).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/macro_exposure_boxes.csv'), index=False)
print(box.round(3).to_string(index=False))
