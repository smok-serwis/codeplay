import numpy as np
import pickle
from random import shuffle, seed

from keras.layers import Dense, Dropout
from keras.models import Sequential
from satella.coding.sequences import index_of_max
from sklearn.preprocessing import StandardScaler
from keras.wrappers.scikit_learn import KerasRegressor

__all__ = ['X', 'Y', 'evaluate_network_for']

seed(0)  # Standard seed
fil = open('final_data.pickle', 'rb')
data = pickle.load(fil)
shuffle(data)
X = np.array([dat[2] for dat in data])
Y = np.array([dat[1] for dat in data])


def baseline_model() -> Sequential:
    model = Sequential()
    model.add(Dense(100, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(100, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(19, kernel_initializer='normal', activation='softmax'))

    # model.compile(loss='mean_squared_error', optimizer='adam')
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model


# Scale the data
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Preprocess the data
indices_to_remove = set()
for i, row in enumerate(Y):
    if list(row).count(1) != 1:
        indices_to_remove.add(i)

new_X, new_Y = [], []
for i in range(len(X)):
    if i in indices_to_remove:
        continue
    new_X.append(X[i])
    new_Y.append(Y[i])

X = np.array(new_X)
Y = np.array(new_Y)


def evaluate_network_for(x_train, y_train, x_test, y_test, epochs: int, batch_size: int) -> float:
    k_reg = KerasRegressor(build_fn=baseline_model, epochs=epochs,
                           batch_size=batch_size, verbose=0)
    k_reg.fit(x_train, y_train)
    correct, false = 0, 0
    for predicted, real_values in zip(k_reg.predict(x_test), y_test):
        if index_of_max(predicted) == index_of_max(real_values):
            correct += 1
        else:
            false += 1

    return correct / (correct + false)
