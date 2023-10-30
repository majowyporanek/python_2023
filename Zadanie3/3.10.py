# ZADANIE 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

# SPOSOB 1
dictionary_1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# SPOSOB 2
roman_nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic_nums = [1, 5, 10, 50, 100, 500, 1000]

dictionary_2 = dict(zip(roman_nums, arabic_nums))


# SPOSOB 3
dictionary_3 = {}
for i in range(len(roman_nums)):
    dictionary_3[roman_nums[i]] = arabic_nums[i]


# SPOSOB 4
dictionary_4 = dict(map(lambda x, y: (x, y), roman_nums, arabic_nums))
