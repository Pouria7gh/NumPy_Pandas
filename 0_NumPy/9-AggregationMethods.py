import numpy as np
from numpy.random import default_rng

sales_array = np.array([[0, 5, 155, 0, 518], 
                        [0, 1827, 616, 317, 325]])

print('sum:', sales_array.sum(), '\n')
print('mean:', sales_array.mean(), '\n')
print('max:', sales_array.max(), '\n')
print('min:', sales_array.min(), '\n')

print('sum(axis=0):', sales_array.sum(axis=0), '\n')
print('sum(axis=1):', sales_array.sum(axis=1), '\n')

rng = default_rng(616)
price = (rng.random(10) * 10).round(2)
inventory = rng.integers(0, 100, 10)
print(price, '\n')
print(inventory, '\n')

print(inventory.mean(), '\n')
print(inventory.sum(), '\n')
print(inventory.max(), '\n')
print(inventory.min(), '\n')

print((inventory * price).argmax())
print((inventory * price).argmin())

price_2d = price.reshape(5, 2)
print(price_2d.max(axis=0))
print(price_2d.mean(axis=1))