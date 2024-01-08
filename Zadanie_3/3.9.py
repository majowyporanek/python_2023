# ZADANIE 3.9 Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę
# zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,
# 4,3,7,18].

def sum_of_sequence(sequence):
    sums = [sum(seq) for seq in sequence]
    return sums


ex_sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
expected = [0, 4, 3, 7, 18]
my_sum = sum_of_sequence(ex_sequence)
assert my_sum == expected, f"Expected {expected}, got {my_sum}"
