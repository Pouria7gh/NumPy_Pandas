import numpy as np

sales = [[11, 223, 233, 11, 9, 110, 10], [220, 12, 14, 88, 90, 100, 200]]
sales_array = np.array(sales)
print(sales_array, '\n')

print(sales_array + 2, '\n')

quantity = sales_array[0, :]
price = sales_array[1, :]

print(quantity * price)