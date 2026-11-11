"""Rebuild every processed input of the pair / hedge slides from the raw public files.

    python code/build_inputs.py            (run from the pair_hedge/ folder)

raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv  Yahoo Finance daily closes (JETS SPY IWM XLY HYG ULCC JBLU)
raw/yahoo/yahoo_HO=F_front_month_capture.txt             Yahoo Finance NYMEX ULSD front-month (HO=F) closes, yymmdd:cents*10
raw/fred/DJFUELUSGULF_*                                  FRED / EIA US Gulf Coast kerosene-type jet fuel spot, $/gal

Writes processed/: daily_prices.csv, yahoo_prices.csv, jet_fuel_gulf.csv, daily_returns.csv,
weekly_returns.csv, jet_fuel_vs_expected.csv, live_etfs.csv
"""
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, OUT = ROOT / 'raw', ROOT / 'processed'
OUT.mkdir(exist_ok=True)
NEW = Path(__file__).resolve().parent / 'out'; NEW.mkdir(exist_ok=True)   # files not present in data/

# ---------- Yahoo closes ----------
y = pd.read_csv(RAW / 'yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv', index_col=0, parse_dates=True)
y.index.name = 'date'
y.to_csv(NEW / 'live_etfs.csv')                                   # used by a5_*.py
legs = y[['frontier', 'jetblue']]
legs.loc['2025-11-03':'2026-11-02'].to_csv(OUT / 'daily_prices.csv')   # k2.py window (251 days)
legs.loc['2025-11-10':'2026-11-09'].to_csv(OUT / 'yahoo_prices.csv')   # k4.py, i1_index.py window

# ---------- FRED jet fuel (DJFUELUSGULF) ----------
def parse_capture(path, sep_item, sep_val, year0):
    rows, yr, prev = [], year0, None
    for it in Path(path).read_text().strip().strip(sep_item).split(sep_item):
        d, v = it.split(sep_val)
        d = d if '-' in d else d[:2] + '-' + d[2:]
        m = int(d[:2])
        if prev and m < prev:
            yr += 1
        prev = m
        rows.append((pd.Timestamp(f'{yr}-{d}'), float(v) if v else np.nan))
    return pd.Series(dict(rows))

early = parse_capture(RAW / 'fred/DJFUELUSGULF_capture_2025-08-01_2025-10-31.txt', ',', ':', 2025)
main = parse_capture(RAW / 'fred/DJFUELUSGULF_capture_2025-11-03_2026-10-27.txt', ';', ',', 2025)
late = pd.read_csv(RAW / 'fred/DJFUELUSGULF_2026-10-28_2026-11-03.csv', index_col=0, parse_dates=True).iloc[:, 0]
jet_all = pd.concat([early, main, late]).sort_index()
jet_all = jet_all[~jet_all.index.duplicated()].dropna()
jet = jet_all.loc['2025-11-03':]
jet.rename('jet_fuel').rename_axis('date').to_csv(OUT / 'jet_fuel_gulf.csv')

# ---------- daily log returns (%) on days with both stock prices and a FRED print ----------
# Window used on every hedge slide: 4 Nov 2025 - 27 Oct 2026 (FRED data available at the time ended 27 Oct).
px = legs.loc['2025-11-03':'2026-10-27']
j = jet.loc[:'2026-10-27']
both = px.join(j.rename('jet_fuel'), how='left')                 # FRED holidays stay NaN ...
dr = (np.log(both).diff().dropna() * 100)[['jet_fuel', 'frontier', 'jetblue']].round(4)   # ... so 2-day returns drop out
dr.to_csv(OUT / 'daily_returns.csv')

# ---------- weekly log returns (%), weeks ending Friday, last (partial) week ends 2 Nov 2026 ----------
dp = legs.loc['2025-11-03':'2026-11-02']
g = dp.groupby(pd.Grouper(freq='W-FRI'))
wk = np.log(g.last()).diff().dropna() * 100
wk.index = [x.index[-1] for _, x in g][1:]                      # label = last trading day of the week
wk.index.name = 'week'
wk[['jetblue', 'frontier']].round(2).to_csv(OUT / 'weekly_returns.csv')

# ---------- jet fuel vs. market expectation 30 days earlier ----------
ho = {}
for it in (RAW / 'yahoo/yahoo_HO=F_front_month_capture.txt').read_text().strip().strip(',').split(','):
    d, v = it.split(':')
    ho[pd.Timestamp('20' + d)] = int(v) / 1000
ho = pd.Series(ho).sort_index()
gap60 = (jet_all - ho).dropna().rolling(60, min_periods=1).mean()          # jet fuel minus ULSD, 60-trading-day average
dates = jet_all.loc['2025-12-01':'2026-11-02'].index          # FRED trading days (+ 28 Oct - 2 Nov)
exp = pd.Series({d: ho.loc[:d - pd.Timedelta(days=30)].iloc[-1] + gap60.loc[:d - pd.Timedelta(days=30)].iloc[-1]
                 for d in dates})
# Deck version: FRED ended 27 Oct when the slide was built, so 28 Oct - 2 Nov were estimated by rolling the
# last FRED print forward with HO=F daily % changes. The real FRED prints (published later) are kept alongside.
act = jet_all.loc[:'2026-10-27'].reindex(dates)
last = act.loc[:'2026-10-27'].dropna().iloc[-1]
for d in dates[dates > pd.Timestamp('2026-10-27')]:
    prev = ho.loc[:d - pd.Timedelta(days=1)].iloc[-1]
    last = last * ho.loc[d] / prev
    act.loc[d] = last
out = pd.DataFrame({'actual': act.round(3), 'expected_30d_earlier': exp.round(3),
                    'actual_fred_final': jet_all.reindex(dates).round(3)})
out.index.name = 'date'
out.dropna(subset=['actual']).to_csv(OUT / 'jet_fuel_vs_expected.csv')
# one-year index chart (i1_*.py) reads the Yahoo 1-year file as is
pd.read_csv(RAW / 'yahoo/yahoo_1yr_closes_JBLU_ULCC_JETS_SPY.csv').to_csv(NEW / 'i1_yahoo_1yr.csv', index=False)
print('built', ', '.join(sorted({p.name for p in list(OUT.glob('*.csv')) + list(NEW.glob('*.csv'))})))

