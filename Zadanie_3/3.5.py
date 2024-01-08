# ZADANIE 3.5 Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się
# z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string,
# a potem go wypisać.
#
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12

def draw(length):
    l1 = '|'; l2 = '0'
    for i in range(1, length+1):
        digit_count = len(str(i))
        l1 += '....|'
        space = ''
        for j in range(4 - digit_count + 1):
            space += ' '
        l2 += space + str(i)
    l1 = l1 + '\n'
    l2 = l2 + '\n'

    return l1 + l2


x = input("Podaj dlugosc miarki ")
try:
    x = int(x)
except ValueError:
    print("To nie jest liczba!")
else:
    y = draw(x)
    print(y)



