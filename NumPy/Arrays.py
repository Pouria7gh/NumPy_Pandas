import numpy as np

sales = [[11, 223, 233, 11, 9, 110, 10], [220, 12, 14, 88, 90, 100, 200]]
sales_array = np.array(sales)
print(sales_array)

### Array Properties ###

print(type(sales_array))
print(sales_array.dtype)
print(sales_array.ndim)
print(sales_array.shape)
print(sales_array.size)

sales_array_plus_one = sales_array + 1
print(sales_array_plus_one)

### Transpose Method ###
print(sales_array.T)
print(sales_array.T.shape)

str_array = np.array([['I', 'Love', 'Python'],
                      ['I', 'Loveeee', 'C#']])
print(str_array)
print(str_array.T)
print(str_array.dtype)
print(str_array.ndim)
print(str_array.shape)
print(str_array.size)