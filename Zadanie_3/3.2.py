# 3.2 Co jest złego w kodzie:
# Odpowiedzi w komentarzach: 

L = [3, 5, 4]; L = L.sort() # sort nie zwraca posortowanej, porzadkuje w miejscu

x, y = 1, 2, 3 # liczba zmiennych po lewej stronie rozni się od liczby wartosci do przypisania

X = 1, 2, 3 ; X[1] = 4 # wykonanie operacji przypisania na krotce

X = [1, 2, 3] ; X[3] = 4 #probojemy przypisać wartość poza zakresem, dostaniemy 'index out of range'

X = "abc" ; X.append("d") # string nie ma operacji 'append'

L = list(map(pow, range(8))) # zbyt mala liczba informacji aby mapowowac
