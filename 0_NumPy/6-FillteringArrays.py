import numpy as np

sales_array = np.array([[0, 5, 155, 0, 518],
                        [0, 1827, 616, 317, 325]])
print(sales_array, '\n')

print(sales_array != 0, '\n')

print(sales_array[sales_array != 0], '\n')

print(sales_array[(sales_array == 616) | (sales_array < 100)], '\n')

print(sales_array[(sales_array < 500) & (sales_array > 100)], '\n')

mask = (sales_array > 100) & (sales_array < 500)

print(mask, '\n')

print(sales_array[mask], '\n')

sales_array = np.array([0, 5, 155, 0, 518])
product_array = np.array(['fruits', 'vegetables', 'cereal', 'dairy', 'eggs'])

print(product_array[sales_array > 10], '\n')

my_array = np.arange(20)

print(my_array, '\n')

mask = my_array % 2 == 1

print(my_array[mask], '\n')

even_odd = np.array(['even', 'odd'] * 10)

print(even_odd, '\n')

mask = even_odd != 'odd'

print(mask, '\n')

print(even_odd[mask], '\n')

even_odd[mask] = 'hello'

print(even_odd, '\n')