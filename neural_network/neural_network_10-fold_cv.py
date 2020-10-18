from sklearn.model_selection import KFold
import numpy as np

from common import X, Y, evaluate_network_for


accuracies = []
i = 0
for train_index, test_index in KFold(n_splits=10).split(X):
    X_train, X_test, Y_train, Y_test = X[train_index], X[test_index], Y[train_index], Y[test_index]
    accuracies.append(evaluate_network_for(X_train, Y_train, X_test, Y_test,
                                           epochs=80, batch_size=150))
    i += 1
    print(f'{i/10*100}% ready, got {accuracies[-1]*100}% accuracy')

print(f'Average accuracy was {np.average(accuracies)*100}%')
print(f'Maximum accuracy was {max(accuracies)*100}%, minimum was {min(accuracies)*100}%')
