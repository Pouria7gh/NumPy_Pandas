import numpy as np
import pandas as pd

series = pd.Series([0, 5, 155, 0, 518])

print(series.dtype)

float_series = series.astype('float')

print(float_series.dtype)

print(float_series.astype('bool'))

# float_series.astype('datetime64')

series = pd.Series(range(5))
print(series)

print(series.astype('bool'))
print(series.astype('string'))
print(series.astype('float'))
print(series.astype('object'))