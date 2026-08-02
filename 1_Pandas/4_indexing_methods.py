import pandas as pd
import numpy as np

# iloc: access data via index

products = ['coffee', 'banana', 'tea', 'coconut', 'sugar']
sales = [0, 5, 155, 0, 518]

sales_series = pd.Series(sales, index=products, name='Sales')
print(sales_series, '\n')

print('third row:', sales_series.iloc[2], '\n')

print('last row:', sales_series.iloc[-1], '\n')

print('row range:\n', sales_series.iloc[2:4], '\n')

print('multiple rows:\n', sales_series.iloc[[1, 2, -1]], '\n')

# loc: access data via labels

print('tea:', sales_series.loc['tea'], '\n')
print('bananas:coconut:\n', sales_series.loc['banana':'coconut'], '\n')

my_series = pd.Series(
    [0, 1, 2, 3, 4],
    index= ['day 0', 'day 1', 'day 2', 'day 3', 'day 4']
)

print(my_series, '\n')

print('day 1:', my_series.loc['day 1'], '\n')

print('day 1:day 3\n', my_series.loc['day 1':'day 3'], '\n')

print('droped index:\n', my_series.reset_index(drop=True), '\n')

