# codeplay
Repozytorium Asseco Codeplay


## neural_network

Neural network dokonuje końcowej ~klasyfikacji~ regresji.
## Grid search
[neural_network_grid_search.py](neural_network/neural_network_grid_search.py)
przyporządkowuje każdej kategorii produktu punktację od 0 (nie kupi) do 1 (na pewno kupi).
Najlepsza sieć finalnie nauczyła się na 91%, z batch size=250, epochs=100.

## Categorical

[neural_network_categorical.py](neural_network/neural_network_categorical.py)
Sieć kategoryczna (przyporządkowuje klientowi tylko jeden produkt) nauczyła się na 95%.
Sieć ta odrzuca wszystkich klientów, którzy nie kupili niczego.

# Spendings  

Bierze CSV'ki od Asseco i dokonuje kompilacji słownika
Rok => Użytkownik => Wektor cech pod względem wydatków.

# Income

Bierze CSV'ki od Asseco i dokonuje kompilacji słownika
Rok => Użytkownik => Wektor cech pod względem dochodu.


 
