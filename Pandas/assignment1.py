import numpy as np
import pandas as pd

oil = pd.read_csv('./assets/oil.csv').dropna()
oil_array = np.array(oil['dcoilwtico'].iloc[1000:1100])

oil_series = pd.Series(oil_array, name='oil_prices')
print(oil_series)
print('size:', oil_series.size)
print('name:', oil_series.name)
print('index:', oil_series.index)
print('dtype:', oil_series.dtype)

print('mean:', oil_series.mean())
print('mean:', oil_series.astype('int').mean())