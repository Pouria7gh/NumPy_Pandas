import numpy as np
import pandas as pd

sales = [0, 5, 155, 0, 518, 0, 1827, 616, 317, 325]
sales_series = pd.Series(sales, name='Sales')
print(sales_series, '\n')

### Props ###

print('index:\n', sales_series.index, '\n')
print('values:\n', sales_series.values, '\n')

print('dtype:', sales_series.dtype, '\n')
print('name:', sales_series.name, '\n')

array = np.arange(5)

series = pd.Series(array, name='test array')

print(series)

print(series.values)

print(series.values.mean())
print(series.mean())
print(series.index)

series.index = [10, 20, 30, 40, 50]
print(series)

series.name = 'Poooria'
print(series)

print(series.dtype)