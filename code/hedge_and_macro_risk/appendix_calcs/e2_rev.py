import json, os
# Consensus ASM/RPM/pax/yield/load factor for Q4 2026E and Q1 2027E come from Bloomberg and are NOT distributed.
# Provide them in LF_CONSENSUS_JSON: {"e2_rev": {"asm": [..,..], "rpm": [..], "pax": [..], "yld": [..], "cons": [..]}}
C = json.load(open(os.environ.get('LF_CONSENSUS_JSON', 'consensus_private.json')))['e2_rev']
asm, rpm, pax, yld, cons = C['asm'], C['rpm'], C['pax'], C['yld'], C['cons']
ours = [81.294, 80.178]   # our load-factor forecast (lfcalc/model.py)
tot_pax = tot_rev = 0

for q, a, r, p, y, c, o in zip(['Q4 2026E', 'Q1 2027E'], asm, rpm, pax, yld, cons, ours):
    x_rpm = a * (o - c) / 100
    x_pax = round(x_rpm / (r / p) * 1000, -4)
    x_rev = x_rpm * y / 100
    tot_pax, tot_rev = tot_pax + x_pax, tot_rev + x_rev
    print(f'{q}  LF {c:.1f}% -> {o:.1f}%  pax {x_pax:,.0f}  revenue ${x_rev:.0f}M')

print(f'Total     pax {tot_pax:,.0f}  revenue ${tot_rev:.0f}M')
