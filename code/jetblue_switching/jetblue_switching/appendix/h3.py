cancel = {'United': 1.36, 'JetBlue': 1.65}
ontime = {'United': 77.6, 'JetBlue': 72.3}

for airline, rate in cancel.items():
    chance = 1 - (1 - rate / 100) ** 20
    print(f'{airline:8} at least 1 cancel in 20 flights: {chance:.0%}')
print(f'on-time gap: {ontime["United"] - ontime["JetBlue"]:.1f} pts')
