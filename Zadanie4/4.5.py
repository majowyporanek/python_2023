# ZADANIE 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

# wersja iteracyjna
def odwracanie(L, left, right):
    if left < 0 or right >= len(L) or left >= right:
        raise ValueError("Niepoprawne indeksy")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return L


# wersja rekurencyjna
def odwracanie_recursive(L, left, right):
    if left >= right:
        return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_recursive(L, left + 1, right - 1)
