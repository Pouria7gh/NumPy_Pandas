import pandas as pd

sales_series = pd.Series(
    [0, 5, 155, 0, 518],
    index=['coffee', 'coffee', 'tea', 'coconut', 'sugar'],
    name='Sales'
)

print(sales_series, '\n')

print(sales_series.loc[sales_series > 0], '\n')

mask = (sales_series > 0) & (sales_series.index == 'coffee')

print(sales_series.loc[mask], '\n')

mask = sales_series == 5

print(mask, '\n')

mask = sales_series.eq(5)

print(mask, '\n')

print('mean:', sales_series.loc[mask].mean(), '\n')

result = sales_series.index.isin(['coffee', 'tea'])

print(result)

result = ~sales_series.index.isin(['coconut', 'sugar'])

print(result, '\n')

my_series = pd.Series(
    range(5),
    index=['day 0', 'day 1', 'day 2', 'day 3', 'day 4']
)

print(my_series, '\n')

print(my_series == 2, '\n')

print(my_series != 2, '\n')

print(my_series.loc[my_series != 2], '\n')

print(my_series.loc[~(my_series != 2)], '\n')

print(my_series.loc[my_series.isin([1, 2])], '\n')

print(my_series.loc[~my_series.isin([1, 2])], '\n')

print(my_series.loc[my_series > 2], '\n')

print(my_series.loc[my_series > 2], '\n')

print(my_series.loc[~(my_series > 2)], '\n')

print(my_series.loc[~my_series.gt(2)], '\n')

mask = (~my_series.gt(5)) & (my_series == 2)

print(my_series.loc[mask], '\n')