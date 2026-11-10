import numpy as np

deals = {'Hawaiian 2025': (7.7, 6.0), 'American 2024': (14.5, 20.5),
         'Southwest 2024': (16.7, 22.3), 'United 2026': (20.6, 26.3),
         'Alaska 2025': (24.4, 28.3)}
gap, pay_raise = np.array(list(deals.values())).T

slope, intercept = np.polyfit(gap, pay_raise, 1)
r = np.corrcoef(gap, pay_raise)[0, 1]
print(f'raise = {slope:.2f} x gap {intercept:+.2f}   r = {r:.2f}')
print(f'JetBlue at a 25% gap: {slope * 25 + intercept:.1f}% raise')
