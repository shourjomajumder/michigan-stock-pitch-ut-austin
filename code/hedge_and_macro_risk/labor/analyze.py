import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # intermediates
import pandas as pd, numpy as np
from scipy import stats

d = pd.read_csv(_os.path.join(_R, "data/hedge_and_macro_risk/labor/data.csv"), parse_dates=["amendable", "deal", "talks_start"])
s = pd.read_csv(_os.path.join(_R, "data/hedge_and_macro_risk/labor/settle.csv"), parse_dates=["ratified"])

def months(a, b):
    return (b - a).dt.days / 30.44

d["months"] = months(d["amendable"], d["deal"])

# peers settled = same-cycle, same work group, other airline, ratified before this deal date
def peers(r, kinds=None):
    x = s[(s.cycle == r.cycle) & (s.airline != r.airline) & (s.ratified < r.deal)]
    if kinds is not None:
        x = x[x.kind.isin(kinds)]
    return len(x)

d["peers_all"] = d.apply(peers, axis=1)
d["peers_reg"] = d.apply(lambda r: peers(r, ["regular"]), axis=1)

# COVID pause: talks broadly frozen Mar 2020 - Dec 2021
c0, c1 = pd.Timestamp("2020-03-01"), pd.Timestamp("2022-01-01")
def covid_overlap(r):
    lo, hi = max(r.amendable, c0), min(r.deal, c1)
    return max((hi - lo).days, 0) / 30.44
d["covid_mo"] = d.apply(covid_overlap, axis=1)
d["months_adj"] = d["months"] - d["covid_mo"]

# early opener: talks started >= 3 months before amendable
d["early"] = np.where(d.talks_start.isna(), np.nan,
                      ((d.amendable - d.talks_start).dt.days / 30.44 >= 3).astype(float))

d["clean"] = d.flag.isna() | (d.flag == "proxy_amendable")
d["strict"] = d.flag.isna() & (d.date_quality == "good")

pd.set_option("display.width", 200)
cols = ["id", "months", "covid_mo", "months_adj", "peers_all", "peers_reg", "early", "flag"]
print(d[cols].round(1).to_string(index=False))

def test(sub, y, x, label):
    sub = sub.dropna(subset=[y, x])
    n = len(sub)
    r, p = stats.pearsonr(sub[x], sub[y])
    rho, ps = stats.spearmanr(sub[x], sub[y])
    slope = np.polyfit(sub[x], sub[y], 1)[0]
    # permutation p for Spearman
    rng = np.random.default_rng(0)
    perm = [stats.spearmanr(rng.permutation(sub[x].values), sub[y])[0] for _ in range(5000)]
    pp = np.mean(np.abs(perm) >= abs(rho))
    print(f"{label:58s} n={n:2d}  r={r:+.2f} (p={p:.2f})  rho={rho:+.2f} (perm p={pp:.2f})  slope={slope:+.1f} mo/peer")
    return dict(label=label, n=n, r=r, p=p, rho=rho, perm_p=pp, slope=slope)

print("\n=== Correlation: months to deal vs peers already settled ===")
res = []
A = d[d.clean]
S = d[d.strict]
res.append(test(d, "months", "peers_all", "All 29 deals, raw months"))
res.append(test(A, "months", "peers_all", "Edge cases removed, raw months"))
res.append(test(A, "months_adj", "peers_all", "Edge cases removed, COVID-adjusted"))
res.append(test(A[A.id != "NK_F_16"], "months_adj", "peers_all", "Edge cases + Spirit 9-yr outlier removed, COVID-adj"))
res.append(test(A, "months_adj", "peers_reg", "Edge cases removed, COVID-adj, regular peers only"))
res.append(test(S, "months_adj", "peers_all", "Strict (good dates only), COVID-adj"))
for g in ["pilot", "fa"]:
    res.append(test(A[A.group == g], "months_adj", "peers_all", f"{g} only, edge cases removed, COVID-adj"))
for c in ["P2010s", "P2020s", "F2010s", "F2020s"]:
    sub = A[A.cycle == c]
    if len(sub) >= 4:
        res.append(test(sub, "months_adj", "peers_all", f"cycle {c}, COVID-adj"))

# OLS with controls
import statsmodels.formula.api as smf
B = A[A.id != "NK_F_16"].copy()
B["fa"] = (B.group == "fa").astype(int)
m1 = smf.ols("months_adj ~ peers_all + fa", data=B).fit()
print("\n=== OLS: COVID-adj months ~ peers + FA dummy (outlier removed) ===")
print(m1.summary().tables[1])
Be = B.dropna(subset=["early"])
m2 = smf.ols("months_adj ~ peers_all + early + fa", data=Be).fit()
print("\n=== OLS: + early-opener dummy ===")
print(m2.summary().tables[1], "\nn =", int(m2.nobs), " R2 =", round(m2.rsquared, 2))

print("\n=== Early opener vs not (edge cases + outlier removed, COVID-adj) ===")
print(Be.groupby("early")["months_adj"].agg(["count", "median", "mean"]).round(1))
print("\nDeals reached within 9 months of amendable date:")
print(d[d.months <= 9][["id", "months", "early", "flag"]].round(1).to_string(index=False))

print("\nMedian months (edge cases removed): raw", round(A.months.median(), 1),
      " COVID-adj", round(A.months_adj.median(), 1))
print("Share of clean deals settled by month 9:", round((A.months <= 9).mean(), 2))

d.to_csv(_os.path.join(_O, "dataset_computed.csv"), index=False)
pd.DataFrame(res).to_csv(_os.path.join(_O, "results.csv"), index=False)
