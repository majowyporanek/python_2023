import itertools as it
import random as rd

print("\na) iterator zwracający 0, 1, 0, 1,...\n")
print("b)  iterator zwracający przypadkowo jedną wartość z (`N`, `E`, `S`, `W`)\n")
print("c) iterator zwracający numery dni tygodnia\n")

choice = input("\nWybrany podpunkt: ")

match choice:
    case 'a':
        numbers = it.cycle([0, 1])
        for _ in range(30):
            print(next(numbers))

    case 'b':
        random_letter = iter(lambda: rd.choice(("N", "E", "S", "W")), 1)
        for _ in range(30):
            print(next(random_letter))

    case 'c':
        days = it.cycle(range(7))
        for _ in range(30):
            print(next(days))
