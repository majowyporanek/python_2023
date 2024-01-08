# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika
# o dane, tylko korzystać z argumentów.


# ZADANIE 3.5 Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się
# z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string,
# a potem go wypisać.
#
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12
def make_ruler(n):
    l1 = '|'; l2 = '0'
    for i in range(1, n + 1):
        digit_count = len(str(i))
        l1 += '....|'
        space = ''
        for j in range(4 - digit_count + 1):
            space += ' '
        l2 += space + str(i)
    l1 = l1 + '\n'
    l2 = l2 + '\n'

    return l1 + l2


# ZADANIE 3.6 Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go
# wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:
#
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
def make_grid(rows, cols):
    if rows < 0 or cols < 0:
        return
    row = '+'
    coll = '|   '
    row = row + '---+' * rows
    coll = coll + '|   ' * rows

    rect = cols * (row + '\n' + coll + '\n')
    rect += row
    return rect



