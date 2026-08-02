import numpy as np
from numpy.random import default_rng

rng = default_rng(12345)
array = rng.random(9).reshape(3, 3)

print(array)
print()

print(array[:2])
print()

print(array[:, 0])

print(array[2,1])
print()