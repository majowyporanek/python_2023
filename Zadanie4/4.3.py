import math


# ZADANIE 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

# 0! = 1, 1! = 1, n! = n*(n-1)!
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#
# print(math.factorial(10))  # Python 2.6+
# print(factorial(10))
