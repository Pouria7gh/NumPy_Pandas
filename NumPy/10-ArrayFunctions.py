import numpy as np

sales_array = np.array([[0, 5, 155, 0, 518],
                        [0, 1827, 616, 317, 325]])

median = np.median(sales_array)
print(median)

percentile = np.percentile(sales_array, 60)
print(percentile)

sales = np.unique(sales_array)
print(sales)

print(np.sqrt(sales))