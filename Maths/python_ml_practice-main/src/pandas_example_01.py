import pandas as pd
from pandas import read_csv

filename = "../dataset/Iris.csv"

df= pd.read_csv(filename,header=None,names=['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species'])
# df= pd.read_csv(filename)


print(df)
print(df.loc[10,'Species'])
print(df.loc[0:3,'Species'])
print(df.iloc[10,1])
print(df.iloc[0:3,1])

# describe: Basic statistics(count, mean, std,min, quantiles, max)
print(df.describe())