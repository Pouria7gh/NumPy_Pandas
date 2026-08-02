import pandas as pd

oil = pd.read_csv('./assets/oil.csv').dropna().iloc[1000:1100]

date = oil.loc[:,'date']
price = oil.loc[:,'dcoilwtico']

oil_series = pd.Series(price.values,
                        index=date.values,
                        name='oil_prices')
print(oil_series, '\n')

first_ten_mean = oil_series.iloc[:10].values.mean()

print(first_ten_mean, '\n')

last_ten_mean = oil_series.iloc[-10:].values.mean()

print(last_ten_mean, '\n')

date_span_prices = oil_series.loc['2017-01-01':'2017-01-07']

print(date_span_prices.reset_index(drop=True))