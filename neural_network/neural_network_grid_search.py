

# Perform a grid search for the best hyperparameters
import itertools

from sklearn.model_selection import KFold

from common import evaluate_network_for, X, Y

train_index, test_index = next(iter(KFold(n_splits=10).split(X)))
X_train, X_test = X[train_index], X[test_index]
Y_train, Y_test = Y[train_index], Y[test_index]


def grid_search():
    max_accuracy = 0
    EPOCHS_TO_CHECK = (50, 80, 100, 150, 200, 250, 300)
    BATCH_SIZES_TO_CHECK = (100, 150, 200, 250, 300)
    epochs_batch_size = list(itertools.product(EPOCHS_TO_CHECK, BATCH_SIZES_TO_CHECK))
    for i, epoch_batch_size in enumerate(epochs_batch_size):
        epochs, batch_size = epoch_batch_size
        acc = evaluate_network_for(X_train, Y_train, X_test, Y_test, epochs, batch_size)
        if acc > max_accuracy:
            max_accuracy = acc
            max_epochs = epochs
            max_batch_size = batch_size
        print(f'Processed {i/len(epochs_batch_size)*100}%')

    return max_batch_size, max_epochs, max_accuracy


max_batch_size, max_epochs, max_accuracy = grid_search()
print(f'Max accuracy was {max_accuracy * 100}% with bs={max_batch_size}, epochs={max_epochs}')

