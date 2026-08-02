from numpy.random import default_rng

seed = 12345
rng = default_rng(seed)

random_array = rng.random(10)
print(random_array.reshape(5, 2))
print()

mean, stddev = 5, 1
random_array = rng.normal(mean, stddev, size=10)
print(random_array.reshape(5, 2))
print()

random_array = rng.integers(0, 10, 20)
print(random_array.reshape(5, 4))
print()