import pandas as pd

filename = "../dataset/mallcustomers.csv"
customers = pd.read_csv(filename)
# customers.head()
customers.info()
customers.describe(include = 'all').round(2)
# print(customers)