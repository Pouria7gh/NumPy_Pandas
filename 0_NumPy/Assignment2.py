import numpy as np

array = np.arange(10, 101, 10, dtype='float')
print(array.reshape(5, 2))
print()

array = np.linspace(10, 100, num=10)
print(array.reshape(5, 2))
print()

array = np.arange(1, 11, dtype='float') * 10
print(array.reshape(5, 2))
print()

seed = 616
rng = np.random.default_rng(seed)

array = rng.random(9)
print(array.reshape(3, 3))
print()