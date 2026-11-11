"""Build the processed fare tables for the JetBlue Thesis 1 base-fare parity slides (appendix E2, JFK1, deck slide 28).

Run from anywhere:  python3 code/build_fare_tables.py
All paths are repo-relative. Inputs are Google Flights quotes we collected on 2026-11-11 (raw/google_flights/...)
and BTS T-100 passenger counts (raw/t100_context/...). Outputs go to processed/.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os, glob
import pandas as pd

ROOT = os.path.normpath(os.path.join(_R, 'data', 'flights_and_fares'))  # data root (raw/, processed/)
RAW, OUT = os.path.join(ROOT, 'raw'), os.path.join(ROOT, 'processed')
GF = os.path.join(RAW, 'google_flights')
p = lambda *a: os.path.join(*a)


def trim_mean(s):
    """Mean after dropping the single date with the largest |gap| (the parity rule used on slide E2)."""
    s = s.reset_index(drop=True)
    return s.drop(s.abs().idxmax()).mean() if len(s) > 1 else s.mean()


# ---------------------------------------------------------------- 1. all NYC Google Flights quotes, long form
files = [p(GF, 't1s2', 'live_jfk_ewr.csv')] + sorted(glob.glob(p(GF, 'rv_fares', 'agent_*.csv')))
q = pd.concat([pd.read_csv(f).assign(source_file=os.path.relpath(f, ROOT)) for f in files], ignore_index=True)
q['route'] = q.route.str.replace('NYC-', '', regex=False)
q['round'] = q.source_file.map(lambda f: 'round1_12_routes' if 'live_jfk_ewr' in f else
                               ('same_airport_ewr' if f.endswith(('agent_21.csv', 'agent_23.csv')) else 'round2_agents'))
q.to_csv(p(OUT, 'google_flights_nyc_quotes_long.csv'), index=False)
qn = q[pd.to_numeric(q.fare, errors='coerce').notna()].copy()
qn['fare'] = qn.fare.astype(float)
qn['carrier'] = qn.airline.str.replace(' Express', '', regex=False)

# ---------------------------------------------------------------- 2. same-airport list ("Same Airports, Base Fares Within $15")
pax = pd.read_csv(p(RAW, 't100_context', 'same_airport_pairs.csv')).set_index('pair')
SLIDE6 = [('BOS-LAX', 'BOS-LAX', 462.5, 0), ('BOS-SFO', 'BOS-SFO', 464.2, 3), ('FLL-SFO', 'FLL-SFO', 208.3, -2),
          ('FLL-IAH', 'FLL-IAH', 15.2, -9), ('EWR-FLL', 'FLL-EWR', 276.9, -1), ('EWR-PBI', 'EWR-PBI', 188.8, -2)]
full = pd.read_csv(p(GF, 'shared_routes', 'Shared_routes_fares_full.csv'))
full['gap_b6_minus_ua'] = full.JetBlue - full.United            # NB: column 'diff' in this file is United minus JetBlue
rev = lambda r: '-'.join(r.split('-')[::-1])
rows = []
for route, t100key, pax_slide, gap_slide in SLIDE6:
    a, b = route.split('-')
    rec = dict(route=route, jetblue_pax_t100_aug25_jul26=int(pax.loc[t100key, 'b6_pax']), jetblue_pax_on_slide_k=pax_slide,
               gap_on_slide=gap_slide)
    s = full[full.route.isin([route, rev(route)])].gap_b6_minus_ua
    rec.update(live458_n=len(s), live458_mean=round(s.mean(), 2), live458_median=s.median(),
               live458_share_within_15=round((s.abs() <= 15).mean(), 3))
    if a == 'EWR':   # JetBlue EWR vs United EWR, 8 dates in round 1 + re-tests: reproduces the slide with the E2 rule
        x = qn[qn.route == b]
        jb = x[(x.carrier == 'JetBlue') & (x.airport == 'EWR')].groupby('date').fare.min()
        ua = x[(x.carrier == 'United') & (x.airport == 'EWR')].groupby('date').fare.min()
        g = (jb - ua).dropna()
        rec.update(rebuilt_n_dates=len(g), rebuilt_gap=round(trim_mean(g), 2), rebuilt_rounded=round(trim_mean(g)),
                   status='REBUILT from raw/google_flights (JetBlue EWR vs United EWR, mean after dropping largest-|gap| date)')
    else:
        rec.update(status='SLIDE VALUE, per-route quote set not found on disk; live458 columns give the closest file-based check')
    rows.append(rec)
sa = pd.DataFrame(rows)
sa.to_csv(p(OUT, 'same_airport_6_routes.csv'), index=False)

# per-pair statistics for all 13 shared routes in the 458-quote file (supporting)
g = full.groupby('pair').gap_b6_minus_ua
pd.DataFrame({'n': g.size(), 'mean_gap': g.mean().round(2), 'median_gap': g.median(),
              'share_within_10': g.apply(lambda s: round((s.abs() <= 10).mean(), 3)),
              'share_within_15': g.apply(lambda s: round((s.abs() <= 15).mean(), 3)),
              'mean_gap_ex_largest': g.apply(lambda s: round(trim_mean(s), 2))}).reset_index() \
    .to_csv(p(OUT, 'shared_routes_458_quotes_pair_stats.csv'), index=False)

# ---------------------------------------------------------------- 3. JFK-SFO / JFK-LAX checks (slide JFK1)
t = pd.read_csv(p(GF, 'jfk27', '5_fares.csv'))
e = t[t.section == 'economy_lowest']
jb = e[(e.airline == 'JetBlue') & (e.airport == 'JFK')].set_index(['dest', 'date']).fare
ua = e[(e.airline == 'United') & (e.airport == 'EWR')].set_index(['dest', 'date']).fare
dl = e[(e.airline == 'Delta') & (e.airport == 'JFK')].set_index(['dest', 'date']).fare
aa = e[(e.airline == 'American') & (e.airport == 'JFK')].set_index(['dest', 'date']).fare
j = pd.DataFrame({'jetblue_jfk': jb, 'united_ewr': ua, 'delta_jfk': dl, 'american_jfk': aa}).reset_index()
j['gap_b6_minus_ua'] = j.jetblue_jfk - j.united_ewr
j['within_15'] = j.gap_b6_minus_ua.abs() <= 15
j.to_csv(p(OUT, 'jfk_transcon_check_by_date.csv'), index=False)
j.groupby('dest').agg(dates=('date', 'size'), within_15=('within_15', 'sum'), median_gap=('gap_b6_minus_ua', 'median'),
                      mean_gap=('gap_b6_minus_ua', 'mean')).reset_index().to_csv(p(OUT, 'jfk_transcon_check_summary.csv'), index=False)

# ---------------------------------------------------------------- 4. international pairs
INTL = ['STI', 'SDQ', 'PUJ', 'CUN', 'AUA', 'MBJ', 'SXM', 'LHR', 'NAS', 'PLS', 'SJO']
rows = []
for d in INTL:
    for scope, x in [('NYC any airport', qn[(qn.route == d) & (qn['round'] != 'same_airport_ewr')]),
                     ('EWR same airport', qn[(qn.route == d) & (qn['round'] == 'same_airport_ewr')])]:
        jb = x[x.carrier == 'JetBlue'].groupby('date').fare.min()
        ua = x[x.carrier == 'United'].groupby('date').fare.min()
        gg = (jb - ua).dropna()
        if len(x) == 0:
            continue
        r = dict(dest=d, scope=scope, dates_both=len(gg), jetblue_dates=len(jb), united_dates=len(ua))
        if len(gg):
            pct = gg / ua.reindex(gg.index)
            r.update(gaps=' '.join(f'{v:+.0f}' for v in gg), median_gap=gg.median(), mean_gap=round(gg.mean(), 2),
                     mean_gap_ex_largest=round(trim_mean(gg), 2), within_15=int((gg.abs() <= 15).sum()),
                     within_10pct=int((pct.abs() <= 0.10).sum()),
                     verdict_rule='MATCH' if (abs(gg.median() / ua.reindex(gg.index).median()) <= 0.10 and (pct.abs() <= 0.10).sum() >= 3) else 'NO MATCH')
        else:
            r.update(verdict_rule='NO DATA')
        rows.append(r)
ip = pd.DataFrame(rows)
tp = pd.read_csv(p(RAW, 't100_context', 'intl_pairs.csv'))[['pair', 'b6_pax', 'ua_pax']]
for ap in ['JFK', 'EWR']:
    m = tp[tp.pair.str.startswith(ap + '-')].assign(dest=lambda z: z.pair.str[4:]).set_index('dest')
    ip[f'b6_pax_{ap}_t100'] = ip.dest.map(m.b6_pax)
    ip[f'ua_pax_{ap}_t100'] = ip.dest.map(m.ua_pax)
ip.to_csv(p(OUT, 'intl_pairs_fare_check.csv'), index=False)

print(sa[['route', 'gap_on_slide', 'rebuilt_rounded', 'live458_mean', 'live458_median', 'status']].to_string(index=False))
print('slide avg of 6 =', round(sa.gap_on_slide.mean(), 4), '| pax sum on slide =', sa.jetblue_pax_on_slide_k.sum(),
      '| pax sum T-100 file =', sa.jetblue_pax_t100_aug25_jul26.sum())
print(pd.read_csv(p(OUT, 'jfk_transcon_check_summary.csv')).to_string(index=False))
print(ip[['dest', 'scope', 'gaps', 'median_gap', 'verdict_rule']].to_string(index=False))
