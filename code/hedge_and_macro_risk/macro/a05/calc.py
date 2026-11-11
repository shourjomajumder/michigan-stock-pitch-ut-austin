# Agent 05: non-oil macro exposures, per company and netted (ULCC - 1.163*JBLU), per $1 long.
H=1.163
# Market caps ($m): price 2026-11-02 (pair_daily.csv) x shares (ASSUMED ~228m ULCC, ~363m JBLU)
mc={'ULCC':7.49*228,'JBLU':3.16*363}
# FY2025 (Q4-25 releases): revenue, opex, SWB ($m)
fy={'ULCC':dict(rev=3724,opex=3873,swb=1016),'JBLU':dict(rev=9062,opex=9430,swb=3453)}
# Shock -> operating income hit ($m, negative = loss)
shocks={
 'Wage +5% (SWB)':{k:-0.05*v['swb'] for k,v in fy.items()},
 'USD +10% (non-USD rev est.)':{'ULCC':-0.10*0.02*3724,'JBLU':-0.10*400},   # ULCC ~2% non-USD rev ASSUMED; JBLU ~$400m (half of Atlantic + ~5% LatAm) ASSUMED
 'Shutdown like Oct-Nov 2025':{'ULCC':-30,'JBLU':-40},                       # ULCC $30m disclosed; JBLU ESTIMATE (not disclosed)
 'Aircraft tariff 10% on ~half of 2026 delivery capex':{'ULCC':-0.10*0.5*300,'JBLU':-0.10*0.5*900}, # JBLU capex $900m disclosed; ULCC ~$300m own-funded ASSUMED (mostly sale-leaseback)
}
print('mcap',mc)
for k,v in fy.items(): print(k,'SWB % opex',round(100*v['swb']/v['opex'],1))
print('shock,ULCC_%mcap,JBLU_%mcap,pair_per_$1')
for s,d in shocks.items():
  u=d['ULCC']/mc['ULCC']; j=d['JBLU']/mc['JBLU']
  print(f"{s},{100*u:.2f},{100*j:.2f},{100*(u-H*j):+.2f}")
