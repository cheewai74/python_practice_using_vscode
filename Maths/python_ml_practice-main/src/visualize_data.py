import pandas as pd
import matplotlib.pyplot as plt

vehicles = pd.read_csv("..\\dataset\\vehicles.csv")
print(vehicles.head())
# vehicles.plot(kind='scatter', x='citympg', y='co2emissions')
# plt.show()
# vehicles['co2emissions'].plot(kind='hist')
# plt.show()
# vehicles.pivot(columns='drive',values='co2emissions').plot(kind='box',figsize=(10,6))
# plt.show()
# print(vehicles.groupby('year')['drive'].value_counts())
print(vehicles.groupby('year')['drive'].value_counts().unstack())
vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind='bar', stacked = True, figsize=(10,4))
plt.show()