import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os as _os
_REPO = _os.environ.get('DATA_REPO', _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..')))
import pandas as pd
df = pd.read_csv(_os.path.join(_REPO, _os.path.join(_R, 'data/flights_and_fares/raw/google_flights/shared_routes/Shared_routes_fares_full.csv')))
df['within5'] = df['diff'].abs() <= 5
cols = ['JetBlue', 'United', 'diff', 'within5']
g = df.groupby('pair')[cols].mean().sort_values('diff', key=abs)
t = df[cols].mean()
print(len(g), 'routes,', len(df), 'fares')
print(f"JetBlue ${t.JetBlue:.0f}, United ${t.United:.0f}, gap {t['diff']:+.0f}, within $5 {t.within5:.0%}")
