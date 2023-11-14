# ZADANIE 4.6 Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać
# zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sekwencja):
    lista = []
    for x in sekwencja:
        if isinstance(x, (list, tuple)):
            lista = lista + sum_seq(x)
        else:
            lista.append(x)

    return lista

# sekwencja = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
# lista_wynik = sum_seq(sekwencja)
# print(sum(lista_wynik))