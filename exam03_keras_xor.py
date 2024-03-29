# -*- coding: utf-8 -*-
"""exam03_keras_xor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eqsJ4JRRQJPfW5qW7HBPC6rpMa-Kn4zq

#인공지능의 역사
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

training_data = np.array(
    [[0,0],[0,1],[1,0],[1,1]])
target_data = np.array(
    [[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(32, input_dim=2, activation = 'relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mse', optimizer='adam')
print(model.summary())

fit_hist = model.fit(training_data, target_data, epochs=500, verbose = 1)

plt.plot(fit_hist.history['loss'])
plt.show()

print(model.predict(np.array([[1,1]]))[0][0].round())

