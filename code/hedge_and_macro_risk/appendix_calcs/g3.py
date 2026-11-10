import numpy as np
import pandas as pd

fa_cost = 425
raises = np.array([20.5, 22.3, 26.3, 28.3, 31.6, 35.6]) / 100
months = np.array([3, 6, 9.5, 12])

hit = np.outer(raises, months) / 12 * fa_cost
grid = pd.DataFrame(hit.round(), index=raises * 100, columns=months)
print(grid.astype(int))
