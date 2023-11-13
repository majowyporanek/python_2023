# ZADANIE 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2).
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    r1, r2 = 0, 1

    for _ in range(2, n + 1):
        r1, r2 = r2, r1 + r2

    return r2
