import pandas as pd

sales_series = pd.Series(
    [0, 5, 155, 0, 518],
    index=['coffee', 'coffee', 'tea', 'coconut', 'sugar'],
    name='Sales'
)

print(sales_series, '\n')

print(sales_series.sort_values(), '\n')

print(sales_series.sort_values(ascending=False), '\n')

print(sales_series.sort_index(), '\n')

print(sales_series.sort_index(ascending=False), '\n')

my_series = pd.Series(
    range(5),
    index=['day 0', 'day 1', 'day 2', 'day 3', 'day 4']
)

print(my_series, '\n')

print(my_series.sort_values(ascending=False, inplace=True), '\n')

print(my_series.sort_index(), '\n')