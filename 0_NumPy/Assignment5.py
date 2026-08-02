import numpy as np

prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
print(prices, '\n')

products = np.array(['salad', 'bread', 'mustard', 'rare tomato', 'cola', 'gourmet ice cream'])
print(products, '\n')

products_greater_25 = products[prices > 25]
print(products_greater_25, '\n')

mask = (prices > 25) | (products == 'cola')
fancy_feast_special = products[mask]
print(fancy_feast_special, '\n')

shiping_cost = np.where(prices > 20, 0, 5)
print(shiping_cost)