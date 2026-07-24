import numpy as np

inventory_array = np.array([12, 102, 18, 0, 0])
product_array = np.array(['fruits', 'vegetables', 'cereal', 'dairy', 'eggs'])


stock_array = np.where(inventory_array <= 0, 'Out of Stock', ' In Stock')
print(stock_array, '\n')

stock_array = np.where(inventory_array <= 0, 'Out of Stock', product_array)
print(stock_array, '\n')

my_array = np.arange(20)
print(my_array, '\n')

even_odd = np.where(my_array % 2 == 0, 'even', 'odd')
print(even_odd, '\n')

even_odd = np.where(my_array % 2 == 0, 'even', np.where(my_array == 9, my_array, 'odd'))
print(even_odd, '\n')