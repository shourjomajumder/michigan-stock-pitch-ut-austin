traffic, elasticity = 0.110, 0.16   # 11% traffic growth: between Q2 (+9.0%) and Q3 (+15.2%) 2026 actuals
builds = {'Q4 2026E': (78.9, 2.2, 5.4), 'Q1 2027E': (78.4, 2.9, 6.1)}

for q, (lf, fare, seats) in builds.items():
    up = lf * traffic
    drag = (lf + up) * elasticity * fare / 100
    full = lf + up - drag
    cap = full - full / (1 + seats / 100)
    print(f"{q}: {lf} +{up:.1f} -{drag:.1f} -{cap:.1f} = {full - cap:.1f}%")
