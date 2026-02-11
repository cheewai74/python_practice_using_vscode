from pandas import read_csv
from matplotlib import pyplot
from sklearn.linear_model import LogisticRegression

filename = "dataset/Iris.csv"
data = read_csv(filename)
print(data.shape)
peek = data.head(20)
print(peek)
shape = (data.shape)
print(shape)
data.hist()
pyplot.show()