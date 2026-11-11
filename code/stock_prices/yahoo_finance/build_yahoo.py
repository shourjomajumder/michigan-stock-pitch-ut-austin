"""Build every processed Yahoo Finance table from raw/ and check the raw files against each other.

    python3 code/build_yahoo.py        (run from the yahoo_finance/ folder; needs pandas, numpy)

Raw inputs (see README.md):
  raw/yahoo_daily_close_JETS_SPY_IWM_XLY_HYG_ULCC_JBLU_2025-10-31_2026-11-09.csv   Close (not dividend adjusted)
  raw/yahoo_daily_adjclose_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv            Adj Close
  raw/yahoo_comps_inputs_2026-11-10.csv                                            Comps sheet inputs
  raw/browser_captures/*                                                           compact page captures
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, OUT = ROOT / 'raw', ROOT / 'processed'
OUT.mkdir(exist_ok=True)
CAP = RAW / 'browser_captures'

close = pd.read_csv(RAW / 'yahoo_daily_close_JETS_SPY_IWM_XLY_HYG_ULCC_JBLU_2025-10-31_2026-11-09.csv',
                    index_col=0, parse_dates=True)
adj = pd.read_csv(RAW / 'yahoo_daily_adjclose_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv',
                  index_col=0, parse_dates=True)
checks = []


def check(name, ok, detail=''):
    checks.append((name, 'OK' if ok else 'MISMATCH', detail))


# ---------- 1. decode the browser captures and compare with the csv files ----------
def b36(s):
    neg = s.startswith('-')
    v = int(s.lstrip('-'), 36)
    return -v if neg else v


enc = {}
for line in (CAP / 'live_closes_base36_delta_JETS_SPY_IWM_XLY_HYG_ULCC_JBLU.txt').read_text().split():
    tk, body = line.split('|')
    vals = np.cumsum([b36(x) for x in body.strip(',').split(',')])
    enc[tk] = vals
hyg = np.cumsum([b36(x) for x in (CAP / 'live_HYG_close_x1000_base36_delta.txt').read_text().strip().strip(',').split(',')])
for tk, col in [('JETS', 'jets'), ('SPY', 'spy'), ('IWM', 'iwm'), ('XLY', 'xly'), ('ULCC', 'frontier'), ('JBLU', 'jetblue')]:
    v = enc[tk] / 100
    n = min(len(v), len(close))
    check(f'enc.txt {tk} (cents) vs close csv', len(v) == len(close) and np.allclose(v[:n], close[col].values[:n], atol=0.006),
          f'{len(v)} values vs {len(close)} rows')
check('hyga.txt HYG (x1000) vs close csv', len(hyg) == len(close) and np.allclose(hyg / 1000, close.hyg.values, atol=0.0006),
      f'{len(hyg)} values')

rows = [r.split(',') for r in (CAP / 'stock_1yr_compact_JBLU_ULCC_JETS_SPY_x100.txt').read_text().replace('\n', ';').split(';') if r.strip()]
st = pd.DataFrame([[int(x) / 100 for x in r[1:]] for r in rows], columns=adj.columns,
                  index=pd.to_datetime([r[0] for r in rows], format='%y%m%d'))
j = adj.join(st, rsuffix='_cap', how='inner')
check('stock/raw.txt vs adjclose csv (common dates)',
      all(np.allclose(j[c], j[c + '_cap'], atol=0.006) for c in adj.columns),
      f'{len(st)} capture rows, {len(adj)} csv rows, {len(adj) - len(j)} csv dates not in capture')

sr = [r.split(',') for r in (CAP / 'stocks_raw_ULCC_JBLU_2025-11-03_2026-10-30.txt').read_text().replace('\n', ';').split(';') if r.strip()]
sr = pd.DataFrame([[float(r[1]), float(r[2])] for r in sr], columns=['frontier', 'jetblue'],
                  index=pd.to_datetime(['20' + r[0] for r in sr]))
j = close[['frontier', 'jetblue']].join(sr, rsuffix='_cap', how='inner')
check('slides/stocks_raw.txt vs close csv (common dates)',
      np.allclose(j.frontier, j.frontier_cap) and np.allclose(j.jetblue, j.jetblue_cap),
      f'{len(sr)} capture rows over {len(close.loc["2025-11-03":"2026-10-30"])} trading days')

# ---------- 2. Close vs Adj Close: dividend adjustment ----------
c = close.loc['2025-11-10':, ['jetblue', 'frontier', 'jets', 'spy']]
c.columns = adj.columns
check('JBLU, ULCC: Adj Close == Close (no dividends)', np.allclose(c[['JBLU', 'ULCC']], adj[['JBLU', 'ULCC']]))
ratio = (adj[['JETS', 'SPY']] / c[['JETS', 'SPY']]).round(4)
ratio.columns = ['JETS_adj_factor', 'SPY_adj_factor']
ratio.rename_axis('date').to_csv(OUT / 'adjclose_over_close_JETS_SPY.csv')

# ---------- 3. price tables used by the models and the appendix ----------
legs = close[['frontier', 'jetblue']]
close[['frontier', 'jetblue', 'spy']].rename_axis('date').to_csv(OUT / 'prices_daily_ULCC_JBLU_SPY.csv')   # models prices.csv
legs.loc['2025-11-10':'2026-11-09'].rename_axis('date').to_csv(OUT / 'yahoo_prices.csv')                  # i1_index.py, k4.py
legs.loc['2025-11-03':'2026-11-02'].rename_axis('date').to_csv(OUT / 'daily_prices.csv')                  # k2.py (Yahoo-only)
close.rename_axis('date').to_csv(OUT / 'live_etfs.csv')                                                    # a5_*.py, mdl_beta.py
adj.to_csv(OUT / 'i1_yahoo_1yr.csv')                                                                       # i1_*.py

# one-year share price chart (company overview slide): Adj Close indexed to 10 Nov 2025 = 100
ix = (adj[['JBLU', 'JETS']] / adj[['JBLU', 'JETS']].iloc[0] * 100).round(1)
ix.columns = ['JetBlue (JBLU)', 'Airline sector (JETS)']
ix.to_csv(OUT / 'JBLU_vs_JETS_indexed_1yr.csv')
ixu = (adj[['ULCC', 'JBLU', 'JETS', 'SPY']] / adj[['ULCC', 'JBLU', 'JETS', 'SPY']].iloc[0] * 100).round(1)
ixu.to_csv(OUT / 'indexed_1yr_ULCC_JBLU_JETS_SPY.csv')

# ---------- 4. returns ----------
dp = legs.loc['2025-11-03':'2026-11-02']
dlr = (np.log(dp).diff().dropna() * 100).round(4)
dlr.rename_axis('date').to_csv(OUT / 'daily_log_returns_ULCC_JBLU.csv')
g = dp.groupby(pd.Grouper(freq='W-FRI'))
wk = np.log(g.last()).diff().dropna() * 100
wk.index = [x.index[-1] for _, x in g][1:]          # label = last trading day of the week
wk.index.name = 'week'
wk[['jetblue', 'frontier']].round(2).to_csv(OUT / 'weekly_returns.csv')

# ---------- 5. pair statistics (Pair Overview slide) ----------
dr = np.log(dp).diff().dropna()
stats = {
    'window': '2025-11-03 to 2026-11-02, Yahoo closes only',
    'corr_weekly_log_returns': round(wk.frontier.corr(wk.jetblue), 2),
    'corr_daily_log_returns': round(dr.frontier.corr(dr.jetblue), 2),
    'ann_vol_frontier_daily_pct': round(dr.frontier.std() * np.sqrt(252) * 100, 1),
    'ann_vol_jetblue_daily_pct': round(dr.jetblue.std() * np.sqrt(252) * 100, 1),
    'frontier_52w_high': close.frontier.loc['2025-11-10':].max(), 'frontier_52w_low': close.frontier.loc['2025-11-10':].min(),
    'jetblue_52w_high': close.jetblue.loc['2025-11-10':].max(), 'jetblue_52w_low': close.jetblue.loc['2025-11-10':].min(),
    'frontier_close_2026-11-09': close.frontier.iloc[-1], 'jetblue_close_2026-11-09': close.jetblue.iloc[-1],
    'spy_close_2026-11-09': close.spy.iloc[-1],
}
pd.Series(stats, name='value').rename_axis('stat').to_csv(OUT / 'pair_price_stats.csv')

# ---------- 6. comps (Yahoo inputs, 11/10/2026) ----------
cp = pd.read_csv(RAW / 'yahoo_comps_inputs_2026-11-10.csv')
cp['implied_diluted_shares_mm'] = (cp.market_cap_usd_mm / cp.price_usd).round(3)
cp['enterprise_value_usd_mm'] = (cp.market_cap_usd_mm + cp.total_debt_incl_op_leases_usd_mm - cp.cash_usd_mm).round(3)
cp['ev_to_fy2027e_sales'] = (cp.enterprise_value_usd_mm / cp.fy2027e_revenue_usd_mm).round(2)
cp['pe_fy2027e'] = np.where(cp.fy2027e_eps_usd > 0, (cp.price_usd / cp.fy2027e_eps_usd).round(2), np.nan)
# final models: ULCC / JBLU rows re-priced at the 11/09/2026 Yahoo close (comps.py CUR_PX), market cap rescaled
cur = {'ULCC': close.frontier.iloc[-1], 'JBLU': close.jetblue.iloc[-1]}
cp['final_model_price_usd'] = cp.ticker.map(cur).fillna(cp.price_usd)
cp['final_model_market_cap_usd_mm'] = (cp.market_cap_usd_mm / cp.price_usd * cp.final_model_price_usd).round(3)
cp.to_csv(OUT / 'comps_yahoo_2026-11-10.csv', index=False)
peers = cp[cp.role == 'peer']
pct = pd.DataFrame({q: [peers.ev_to_fy2027e_sales.quantile(v), peers.pe_fy2027e.quantile(v)]
                    for q, v in [('p25', .25), ('median', .5), ('p75', .75)]}, index=['ev_to_sales', 'pe']).round(4)
pct.rename_axis('multiple').to_csv(OUT / 'comps_peer_percentiles.csv')

# ---------- report ----------
pd.DataFrame(checks, columns=['check', 'result', 'detail']).to_csv(OUT / 'raw_consistency_checks.csv', index=False)
for r in checks:
    print(' | '.join(r))
print(pd.Series(stats))
print(pct)
