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

  # plt.scatter(xs, ys, c=colors[i])





## SGD Classifier

from sklearn.linear_model import SGDClassifier

clf = SGDClassifier()
clf.fit(Xtrain, Ytrain)

print('clf.coef', clf.coef_)
print('clf.intercept', clf.intercept_)

Xmin, Xmax = Xtrain[:, 0].min() - 0.5, Xtrain[:, 0].max() + 0.5
Ymin, Ymax = Xtrain[:, 1].min() - 0.5, Xtrain[:, 1].max() - 0.5
xs = np.arange(Xmin, Xmax, 0.5)

fig, axes = plt.subplots(1,3)
fig.set_size_inches(10, 6)
for i in [0, 1, 2]:
  axes[i].set_aspect('equal')
  axes[i].set_xlim(Xmin, Xmax)
  axes[i].set_ylim(Ymin, Ymax)
  xx = Xtrain[:, 0]
  yy = Xtrain[:, 1]
  axes[i].scatter(xx, yy, c=Ytrain, cmap=plt.cm.prism)
  ys = (-clf.intercept_[i] - xs * clf.coef_[i, 0])/ clf.coef_[i, 1]
  axes[i].plot(xs, ys)

# plt.show()

print(clf.predict(scaler.transform([[4.7,3.1]])))

print(clf.decision_function(scaler.transform([[4.7, 3.1]])))


from sklearn import metrics

yTrainPred = clf.predict(Xtrain)
print(metrics.accuracy_score(Ytrain, yTrainPred))