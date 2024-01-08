# ZADANIE 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć:
sequence1 = [1, 56, 88, 99, 101, 1, 5, 4]
sequence2 = [666, 44, 88, 101, 2, 4, 5, 1, 5, 5, 5]

# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
a = list(set(sequence1) & set(sequence2))
expected_a = [1, 4, 5, 88, 101]
assert sorted(a) == expected_a, f"Expected {expected_a}, got {a}"

# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
b = list(set(sequence1 + sequence2))
expected_b = [1, 2, 4, 5, 44, 56, 88, 99, 101, 666]
assert sorted(b) == expected_b, f"Expected {expected_b}, got {b}"
