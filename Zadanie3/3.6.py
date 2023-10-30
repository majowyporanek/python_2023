# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:
#
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
def draw_rect(r, c):
    if r < 0 or c < 0:
        return
    row = '+'
    coll = '|   '
    row = row + '---+' * r
    coll = coll + '|   ' * r

    rect = c * (row + '\n' + coll + '\n')
    rect += row
    return rect


try:
    x = int(input("Podaj długość x: "))
    y = int(input("Podaj długość y: "))
except ValueError:
    print("To nie jest liczba!")
else:
    result = draw_rect(x, y)
    print(result)
