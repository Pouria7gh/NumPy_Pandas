import numpy as np

prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])

prices.sort()

print(prices[::-1])
print(prices[0])
print(prices[-1])
print(prices[-3:])
print(np.median(prices))
print(np.unique(prices))