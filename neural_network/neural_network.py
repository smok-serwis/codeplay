# Import the data from the pickle

import pickle
import os
print(os.listdir('..'))

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


estimators = []
estimators.append(('standarize', StandardScaler()))
estimators.append(
    ('mlp', KerasRegressor(build_fn=baseline_model, epochs=50, batch_size=100, verbose=1)))
kfold = KFold(n_splits=10)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))
