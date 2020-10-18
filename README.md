codeplay
========

To repozytorium oddaje naszą pracę na Asseco Codeplay 2020. Film z prezentacją
można zobaczyć [tu](http://mail.dms-serwis.com.pl/asseco-codeplay.mp4).

Projekt jest napisany w języku Python.

# Struktura projektu

## [requirements.txt](requirements.txt)

Wymagania Pythonowe niezbędne do uruchomienia projektu.

## [Spendings](spendings/)  

Bierze CSV'ki od Asseco i dokonuje kompilacji słownika
Rok => Użytkownik => Wektor cech pod względem wydatków.

## [Income](income/)

Bierze CSV'ki od Asseco i dokonuje kompilacji słownika
Rok => Użytkownik => Wektor cech pod względem dochodu.

## [User_loans_policy](user_loans_policy/)

Moduł ten parsuje pliki CSV dostarczone z Asseco i wyciąga jakie produkty wzięli dani
klienci, z podziałem na kategorie.
 
## [single_file_generator.py](single_file_generator.py)

Zbiera dane z poprzednich trzech modułów do jednego Pythonowego pickla

## [neural_network](neural_network/)

Dokonuje właściwej analizy kategorycznej za pomocą perceptrona wielowarstwowego (MLP).

# Sieć neuronowa

Zastosowano tutaj prosty perceptron wielowarstwowy. Wejście miało wymiar 63, a wyjście 19 klas.
Zastosowano architekturę 63 - 100 - 100 - 19 z funkcją aktywacji ReLU i regularyzacją Dropout=0.5.

## Preprocessing danych

Na samym początku dane poddano standaryzacji.

Potem odrzucono dane wszystkich klientów, 
którzy nie kupili niczego i tych, którzy kupili więcej niż
jeden produkt. Potem kazano sieci wskazać, który produkt weźmie dany klient.

## Wyniki

W wyniku pobieżnego [grid search](neural_network/neural_network_grid_search.py) ustalono
optymalne hiperparametry. Był to batch size=150 i liczba epok=80 przy dokładności 72%.

Następnie przeprowadzono [10-krotną walidację skrośną](neural_network/neural_network_10-fold_cv.py).
W wyniku jej otrzymano średnią dokładność 62%, maksymalną 71% i minimalną 56%.   

