import pandas as pd
import matplotlib.pyplot as plt


bikes = pd.read_csv("..\\dataset\\bikes.csv")
print(bikes.head())
bikes.info()
print(bikes.describe())

bikes.plot(kind='scatter', x='temperature', y='rentals')
plt.show()
bikes.plot(kind='scatter', x='humidity', y='rentals')
plt.show()
bikes.plot(kind='scatter', x='windspeed', y='rentals')
plt.show()

response = 'rentals'
y = bikes[[response]]
print(y)

predictors = list(bikes.columns)
predictors.remove(response)
x = bikes[predictors]
print(x)