# -*- coding: utf-8 -*-
"""exam30_ml03_kmc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ikwh8_MxgLbC5nCuyEQIhWzxOJ9wpalV
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import KMeans

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

plt.figure(figsize=(8, 6))
plt.title('Dendrograms')
shc.dendrogram(shc.linkage(x_train, method='ward'))
plt.axhline(y=7, color='r', linestyle='--')
plt.show()

cluster = KMeans(n_clusters=3)
preds = cluster.fit_predict(x_train)
preds

y_train

labels

pred_labels = [labels[1], labels[0], labels[2]]

pred_labels

actual_species = []
pred_species = []
for i in y_train:
    actual_species.append(labels[i])
for i in preds:
    pred_species.append(pred_labels[i])
df = pd.DataFrame({'target':actual_species, 'predict':pred_species})
df

df['OX'] = 0
for i in range(len(df)):
    df.loc[i, 'OX'] = df.loc[i, 'target'] == df.loc[i, 'predict']
df['OX'].value_counts()

data = pd.read_csv('./wholesale.csv')
data

"""# 새 섹션"""

from sklearn.preprocessing import normalize
scaled_data = normalize(data)
scaled_data = pd.DataFrame(scaled_data, columns=data.columns)
scaled_data

plt.figure(figsize=(5, 4))
plt.title('Dendrograms')
shc.dendrogram(shc.linkage(scaled_data, method='ward'))
plt.axhline(y=4, color='r', linestyle='--')
plt.show()

cluster = KMeans(n_clusters=4)
print(cluster.fit_predict(scaled_data))

plt.figure()
plt.scatter(scaled_data['Milk'], scaled_data['Grocery'], c=cluster.labels_)
plt.show()

pd.plotting.scatter_matrix(scaled_data.iloc[:, 2:], c=cluster.labels_, figsize=(15, 15))
plt.show()

