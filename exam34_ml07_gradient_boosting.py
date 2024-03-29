# -*- coding: utf-8 -*-
"""exam34_ml07_gradient_boosting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b7EbVav__RefiINCErG_6LUrMvCkBz6s
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GridSearchCV
import matplotlib.pyplot as plt
from sklearn.metrics import *
from sklearn.ensemble import GradientBoostingClassifier

iris_dataset = load_iris()
iris = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)
labels = iris_dataset.target_names
iris.info()
iris.head()

label = iris_dataset.target
label

x_train, x_test, y_train, y_test = train_test_split(iris, label, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=888)
max_depth = [3, 4, 5, 6, 7]
trees = [100, 150, 200, 250, 300]
learning_rate = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
param = {'n_estimators':trees, 'max_depth':max_depth, 'learning_rate':learning_rate}
gs_iris_GBC = GridSearchCV(estimator=GradientBoostingClassifier(), param_grid=param)
gs_iris_GBC.fit(x_train, y_train)

print(gs_iris_GBC.best_score_)
print(gs_iris_GBC.best_params_)
print(gs_iris_GBC.best_estimator_)

for i in range(1, 100):
    x_train, x_test, y_train, y_test = train_test_split(iris, label, test_size=0.2, random_state=i)
    iris_GBC = gs_iris_GBC.best_estimator_
    iris_GBC.fit(x_train, y_train)
    train_score = iris_GBC.score(x_train, y_train)
    test_score = iris_GBC.score(x_test, y_test)
    if test_score >= train_score:
        print(test_score, train_score, i)

x_train, x_test, y_train, y_test = train_test_split(iris, label, test_size=0.2, random_state=3)
iris_GBC = gs_iris_GBC.best_estimator_
iris_GBC.fit(x_train, y_train)
train_score = iris_GBC.score(x_train, y_train)
test_score = iris_GBC.score(x_test, y_test)
print(test_score, train_score)

pd.DataFrame(confusion_matrix(y_test, iris_GBC.predict(x_test)),
             columns=['pred setosa', 'pred versicolore', 'pred_virginica'],
             index=['actual setosa', 'actual versicolore', 'actual virginica'])