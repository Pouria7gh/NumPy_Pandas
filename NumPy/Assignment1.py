import numpy as np

finance = [x * 10 for x in range(1, 12)]
finance_array = np.array(finance)
print(finance_array)

print('ndim:', finance_array.ndim)
print('shape:', finance_array.shape)
print('size:', finance_array.size)
print('dtype:', finance_array.dtype)
print('T:', finance_array.T)