import pandas as pd

sales = [0, 5, 155, 0, 518]
items = ['coffee', 'coffee', 'tea', 'coconut', 'sugar']

sales_series = pd.Series(sales, index=items, name='Sales')

print(sales_series.loc['coffee'], '\n')

print(sales_series.reset_index(), '\n')

print(sales_series.reset_index(drop=True), '\n')

my_series = pd.Series(
    range(5),
    index=['day 0', 'day 0', 'day 0', 'day 2', 'day 2']
)

print(my_series, '\n')

print(my_series.loc['day 0'], '\n')

print(my_series.reset_index(), '\n')

print(my_series.reset_index(drop=True), '\n')