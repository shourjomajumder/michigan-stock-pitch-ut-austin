import pandas as pd,numpy as np,glob
import os; _R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')  # repo root
_K = os.path.join(_R, 'data/jetblue_switching/processed/cases')  # k1..k6 case CSVs
d=pd.concat([pd.read_csv(os.path.join(_K, f)).assign(f=f[:2]) for f in sorted(glob.glob('k*.csv', root_dir=_K))],ignore_index=True)
d=d[d.role=='loser'].copy()
d['rel']=np.where(d.share_before_pct.notna()&d.share_after_pct.notna(),(d.share_after_pct/d.share_before_pct-1)*100,d.pct_passengers_change)
d=d[d.rel.notna()&d.months_elapsed.notna()]
d['ann']=d.rel/d.months_elapsed*12
pd.set_option('display.width',250)
print(d[['case','market','carrier','depth','share_before_pct','share_after_pct','months_elapsed','rel','ann']].round(1).to_string())
