import numpy as np
import pandas as pd

sales = [0, 5, 155, 0, 518]
# sales_series = pd.Series(sales)

# print(sales_series, '\n')

# print(sales_series[2], '\n')

# print(sales_series[2:4])

items = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']

sales_series = pd.Series(sales, index=items, name='Sales')
print(sales_series, '\n')

print('coffee:', sales_series['coffee'], '\n')
print('bananas to coconut:')
print(sales_series['bananas':'coconut'])

my_series = pd.Series(range(5))

print(my_series[3])
print(my_series[1:3])
print(my_series[1::2])