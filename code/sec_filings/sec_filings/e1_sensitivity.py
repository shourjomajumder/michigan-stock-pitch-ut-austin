"""Sensitivity of the Thesis 1 regression (frontier/code/e1.py) to the Allegiant ASM-basis issue found here.
Run from sec_filings/code. Reads ../../frontier/processed/lcc_quarters.csv and ../processed/lcc_quarters_check.csv."""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, statsmodels.formula.api as smf
base = pd.read_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/processed/lcc_quarters.csv'))
chk = pd.read_csv(_os.path.join(_R, 'data/sec_filings/processed/lcc_quarters_check.csv'))
def fit(df, label):
    m = smf.ols('traffic ~ fare + seats', df).fit(); r = smf.ols('traffic ~ fare', df).fit()
    print(f'{label:45} seats-fixed fare {m.params.fare:.3f} R2 {m.rsquared:.3f} | fares-only {r.params.fare:.3f} R2 {r.rsquared:.3f}')
fit(base, 'as published (lcc_quarters.csv)')
a = base.copy(); a.loc[(a.airline == 'Allegiant') & (a.quarter == '2025Q2'), 'seats'] = 15.68
fit(a, 'Allegiant 2025Q2 seats fixed (total basis 15.68)')
s = base.copy()
for _, r in chk[(chk.airline == 'Allegiant') & (chk.field == 'lcc_quarters.seats')].iterrows():
    sched = float(r.note.split('scheduled-service basis would be ')[-1]) if 'scheduled-service basis would be' in r.note else \
            float(r.note.split('scheduled ')[-1]) if r.match == 'NO' else r.our_value
    s.loc[(s.airline == 'Allegiant') & (s.quarter == r.quarter), 'seats'] = sched
fit(s, 'all Allegiant seats on scheduled basis')
