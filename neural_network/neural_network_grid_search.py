# Import the data from the pickle

import pickle
import numpy as np
from random import shuffle, seed
seed(0) # Standard seed
fil = open('final_data.pickle', 'rb')
data = pickle.load(fil)
shuffle(data)
X = np.array([dat[2] for dat in data])
Y = np.array([dat[1] for dat in data])


# Train the neural network
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold


def baseline_model() -> Sequential:
    model = Sequential()
    model.add(Dense(100, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(100, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(63, kernel_initializer='normal', activation='relu'))

    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

kf = KFold(n_splits=10)
train_index, test_index = next(iter(kf.split(X)))
X_train, X_test = X[train_index], X[test_index]
Y_train, Y_test = X[train_index], Y[test_index]

max_accuracy = 0
max_epochs = 0
max_batch_size = 0


def evaluate_network_for(epochs: int, batch_size: int) -> float:
    kreg = KerasRegressor(build_fn=baseline_model, epochs=epochs, batch_size=batch_size, verbose=1)
    kreg.fit(X_train, Y_train)
    correct, false = 0, 0
    for entry, real_values in zip(kreg.predict(X_test), Y_test):
        for estimated, real in zip(entry, real_values):
            set = False
            if real == 1 and abs(estimated) > 0.5:
                correct += 1
                set = True
            elif real == 0 and abs(estimated) < 0.5:
                correct += 1
                set = True

            if not set:
                false += 1

    return correct/(correct+false)

# Perform a grid search for the best hyperparameters
def grid_search():
    max_accuracy = 0
    for epochs in (100, 150, 200, 250, 300):
        for batch_size in (100, 150, 200, 250, 300):
            acc = evaluate_network_for(epochs, batch_size)
            if acc > max_accuracy:
                max_accuracy = acc
                max_epochs = epochs
                max_batch_size = batch_size

    print(f'Max accuracy was {max_accuracy*100}% with bs={max_batch_size}, epochs={max_epochs}')
    return max_batch_size, max_epochs


grid_search()
