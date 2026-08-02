import numpy as np

products = ['fruits', 'vegtables', 'cereal', 'dairy', 'eggs', 
            'snacks', 'beverages', 'coffee', 'tea', 'spices']

product_array = np.array(products)
print(product_array)
print(product_array[1])
print(product_array[-1])
print(product_array[:5])
print(product_array[4::2])
print()

product_array2d = product_array.reshape(2,5)
print(product_array2d)
print(product_array2d[1,2])
print(product_array2d[:,1:3])
print(product_array2d[1:2,-3:])