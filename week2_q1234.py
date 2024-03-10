
'''
The Basics of NumPy and Pandas
week 2
'''

#q1
import pandas as pd
import numpy as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
idx = np.arange(0, df.shape[0], step=20)
col = ['Manufacturer','Model','Type']
result = df[col].iloc[idx]

print(result)

#q2

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
min_price_mean = df['Min.Price'].mean()
max_price_mean = df['Max.Price'].mean()
df['Min.Price'].fillna(min_price_mean, inplace=True)
df['Max.Price'].fillna(max_price_mean, inplace=True)
print(df[['Min.Price', 'Max.Price']])


#q3

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df[df.sum(axis=1) > 100])

#4
array = np.random.randint(1, 101, size=(4, 4))
row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
print(array)
print(row_sums)
print(column_sums)
