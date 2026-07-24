import numpy as np

sales_array = np.array([[0, 5, 155, 0, 518],
                        [0, 1827, 616, 317, 325]])

sales_array.sort()

print((sales_array.reshape(1,10))[::-1])