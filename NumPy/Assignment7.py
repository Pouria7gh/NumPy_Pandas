import pandas as pd
import numpy as np

retail_df = pd.read_csv('./assets/retail_2016_2017.csv', skiprows= range(1, 11000), nrows=1000)

family_array = np.array(retail_df['family'])
sales_array = np.array(retail_df['sales'])

produce_array = sales_array[family_array == 'PRODUCE']

print(produce_array.size, '\n')

rng = np.random.default_rng(2022)

random_array = rng.random(produce_array.size)

random_half = produce_array[random_array < 0.5]

mean = np.mean(random_half) 
print(mean)
median = np.median(random_half)
print(median)

filltered_random = np.where((random_half > mean) & (random_half > median) , "above_both",
                            np.where(random_half > median,"above_median", 'below_both'))

print(filltered_random[:5])