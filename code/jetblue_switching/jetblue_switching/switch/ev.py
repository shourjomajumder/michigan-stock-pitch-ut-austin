import numpy as np
def ser(s): return [np.nan if v=='' else float(v) for v in s.split(',')]
AS = {
 'SEA-GEG (Spokane)': (ser("78,81,82,80,82,88,88,85,99,99,99,99,99,99,99,99,99,99,99,94,93.9,93.5,93.1,92.5,90.4,92.3,90.7,88.2,89.3,87.1,84.3,79.2,88,87,83.5,80,79.9,75,83.5,84.8"), 19),
 'SEA-BOI (Boise)': (ser("60,62,59,61,63,68,69,63,97,99,99,99,99,99,99,99,99,99,99,98,98.8,87.2,82.2,80.3,76.7,80.4,77.6,75.3,73,74.1,67.6,70.5,76.7,75.8,72.5,72.4,76.6,75.2,78,77.1"), 21),
 'SEA-EUG (Eugene)': (ser("93,94,95,93,94,94,93,94,93,90,93,94,95,94,96,96,96,94,97,97,98.7,98.4,98.2,97.4,98.3,98.5,98.6,98.5,98.3,75.8,71.9,73.7,70.8,66.7,67.6,70.5,65.4,65,69.1,69.8"), 29),
 'SEA-PDX (Portland)': (ser("95,94,99,93,93,92,91,93,90,84,87,89,93,86,92,90,92,92,93,93,94.5,94,93.5,93.5,93.3,92.6,89,86.8,91.7,92.3,87.6,84.9,89.5,89.3,89.8,85.6,86.3,79.9,84.5,86"), 18),
}
def path(v, e, K=12):
    v = np.array(v)
    pre = np.nanmean(v[e-4:e])
    out = []
    for k in range(0, K+1):
        if e+k >= len(v): out.append(np.nan); continue
        # same-quarter-of-year comparison to remove seasonality: change vs pre average
        out.append(pre - v[e+k])
    return pre, np.array(out)
rows = []
for n, (v, e) in AS.items():
    pre, p = path(v, e)
    end = np.nanmean(p[9:13])
    sm = np.array([np.nanmean(p[max(0,k-1):k+2]) for k in range(len(p))])
    frac = sm / end
    first50 = next((k for k in range(len(frac)) if frac[k] >= 0.5), None)
    first90 = next((k for k in range(len(frac)) if frac[k] >= 0.9), None)
    rows.append((n, pre, end, p[0], first50, first90))
    print(f"{n:22} pre {pre:5.1f}  loss q0 {p[0]:5.1f}  q2 {p[2]:5.1f}  q4 {p[4]:5.1f}  q8 {p[8]:5.1f}  end(q9-12) {end:5.1f}  50% by q{first50}  90% by q{first90}")
    print('   frac path', np.round(frac,2))
