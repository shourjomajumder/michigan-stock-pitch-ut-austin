import json, os
# Consensus inputs (ASM, RPM, passengers, yield, consensus LF for Q4 2026E / Q1 2027E) come from the Bloomberg
# consensus carried in the valuation model's Operating Model. They are NOT redistributed in this repo.
# To rerun, create ../private/consensus_inputs.json with keys asm, rpm, pax, yld, cons (2-item lists, Q4 2026E then Q1 2027E).
c = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'private', 'consensus_inputs.json')))
asm, rpm, pax, yld, cons = c['asm'], c['rpm'], c['pax'], c['yld'], c['cons']
# ASM = same quarter last year x (1 + seat growth) with seat growth 5.4% / 6.1% as in e2_build.py
# (Q4 matches management's 5-6% capacity guidance, Q3 2026 call); RPM = ASM x consensus load factor.
ours = [82.800, 81.640]   # our load factor, unrounded (load factor build)
tot_pax = tot_rev = 0

for q, a, r, p, y, c, o in zip(['Q4 2026E', 'Q1 2027E'], asm, rpm, pax, yld, cons, ours):
    x_rpm = a * (o - c) / 100
    x_pax = round(x_rpm / (r / p) * 1000, -4)
    x_rev = x_rpm * y / 100
    tot_pax, tot_rev = tot_pax + x_pax, tot_rev + x_rev
    print(f'{q}  LF {c:.1f}% -> {o:.1f}%  pax {x_pax:,.0f}  revenue ${x_rev:.1f}M')

print(f'Total     pax {tot_pax:,.0f}  revenue ${tot_rev:.1f}M')
