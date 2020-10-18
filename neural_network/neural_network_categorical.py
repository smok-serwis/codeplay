# Import the data from the pickle
import itertools
import pickle
from random import shuffle, seed

import numpy as np

seed(0)  # Standard seed
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
    model.add(Dense(63, kernel_initializer='normal', activation='softmax'))

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

print(f'Size of dataset is {len(X)}')

kf = KFold(n_splits=10)
train_index, test_index = next(iter(kf.split(X)))
X_train, X_test = X[train_index], X[test_index]
Y_train, Y_test = X[train_index], Y[test_index]


def evaluate_network_for(epochs: int, batch_size: int, cutoff: float = 0.5) -> float:
    kreg = KerasRegressor(build_fn=baseline_model, epochs=epochs,
                          batch_size=batch_size, verbose=0)
    kreg.fit(X_train, Y_train)
    correct, false = 0, 0
    ones, zeros = 0, 0
    for entry, real_values in zip(kreg.predict(X_test), Y_test):
        for estimated, real in zip(entry, real_values):
            was_set = False
            if real == 1:
                ones += 1
            elif real == 0:
                zeros += 1

            if real == 1 and abs(estimated) > cutoff:
                correct += 1
                was_set = True
            elif real == 0 and abs(estimated) < cutoff:
                correct += 1
                was_set = True

            if not was_set:
                false += 1

    return correct / (correct + false)


# Perform a grid search for the best hyperparameters
def grid_search():
    max_accuracy = 0
    epochs_batch_size = list(itertools.product((100, 150, 200, 250, 300),
                                               (100, 150, 200, 250, 300)))
    for i, epoch_batch_size in enumerate(epochs_batch_size):
        epochs, batch_size = epoch_batch_size
        acc = evaluate_network_for(epochs, batch_size)
        if acc > max_accuracy:
            max_accuracy = acc
            max_epochs = epochs
            max_batch_size = batch_size
            print(f'New best values found for bs={batch_size}, ep={epochs}, '
                  f'acc={acc*100}%')
        print(f'Processed {i/len(epochs_batch_size)*100}%')

    print(f'Max accuracy was {max_accuracy * 100}% with bs={max_batch_size}, epochs={max_epochs}')
    return max_batch_size, max_epochs


grid_search()
