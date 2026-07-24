import numpy as np

rng = np.random.default_rng(12345)
prices = (rng.integers(5, 60, 6) - rng.random(6)).round(2)

print('prices:', prices)

owed = (1 - rng.random(6)).round(2)
print('owed:', owed)

final_owed = prices * owed

print('final owed:', final_owed)