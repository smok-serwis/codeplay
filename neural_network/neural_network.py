# Import the data from the pickle

import pickle
import os
import numpy as np
fil = open('plik.py', 'rb')
data = pickle.load(fil)

X = np.array([dat[1] for dat in data])
Y = np.array([dat[2] for dat in data])

# Learn the neural network

import typing as tp
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.preprocessing import StandardScaler


def baseline_model() -> Sequential:
    model = Sequential()
    model.add(Dense(200, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(100, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(50, kernel_initializer='normal', activation='tanh'))

    opt = keras.optimizers.Adam(learning_rate=0.01)
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
train_index, test_index = next(iter(kf.split(X)))
X_train, X_test = X[train_index], X[test_index]
Y_train, Y_test = X[train_index], Y[test_index]

kreg = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=100, verbose=1)
kreg.fit(X_train, Y_train)
correct, false = 0, 0
for entry, real_values in zip(kreg.predict(X_test), Y_test):
    for estimated, real in zip(entry, real_values):
        set = False
        if estimated == 1 and abs(real) > 0.5:
            correct += 1
            set = True
        elif estimated == 0 and abs(real) < 0.5:
            correct += 1
            set = True

        if not set:
            false += 1

print(f'Correct = {correct}, false={false}')
