import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

x_iris, y_iris = iris.data, iris.target

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

x, y = x_iris[:, :2], y_iris

Xtrain, Xtest, Ytrain, Ytest = train_test_split(x, y, test_size=0.25, random_state=33)

scaler = preprocessing.StandardScaler().fit(Xtrain)

Xtrain = scaler.transform(Xtrain)

Xtest = scaler.transform(Xtest)

colors = ['red', 'greenyellow', 'blue']

for i in range(len(colors)):
  xs = Xtrain[:, 0][Ytrain == i]
  ys = Xtrain[:, 1][Ytrain == i]
  plt.scatter(xs, ys, c=colors[i])


plt.show()

# print(x.shape, y.shape)
# print(x[0], y[0])