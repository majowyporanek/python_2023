# ZADANIE 2.10
# Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami
# (spacja, tabulacja, newline).

def countWords(string):
    if len(string) == 0:
        return 0
    words = string.split()
    return len(words)


line = input("2.10 Zostanie policzona liczba wyrazow w podanym napisie wielowierszowym: ")
result = countWords(line)
print("wynik: " + str(result))

# ZADANIE 2.11
# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
word = input("\n2.11 Znaki podanego slowa zostana rozdzielone znakiem podkreslenia:")
word = "_".join(word.strip())
print("wynik: ", word)

# ZADANIE 2.12 Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z
# ostatnich znaków wyrazów z wiersza line.
line = input("\n2.12 Zostana zbudowane napisy z pierwszych i ostatnich znakow podanego wiersza: ")
line = line.strip()
words_of_line = line.split()
first_letters_of_words = map(lambda x: x[0], words_of_line)
last_letters_of_words = map(lambda x: x[len(x) - 1], words_of_line)
word1 = ''.join(list(first_letters_of_words))
word2 = ''.join(list(last_letters_of_words))
print("Wyraz z pierwszych znakow wyrazow z wiersza line: ", word1)
print("Wyraz z ostatnich znakow wyrazow z wiersza line: ", word2)

# ZADANIE 2.13
# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
line = input("\n2.13 Zostanie znaleziona laczna dlugosc wyrazow w podanym napisie: ")
words = line.strip().split()
words = list(map(lambda x: len(x), words))
print("Laczna dlugosc wyrazow w napisie: ", sum(words))

# ZADANIE 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
line = input("\n2.14 Zostana znalezione: a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w podanym napisie: ")
words = line.strip().split()
words_lengths = list(map(lambda x: len(x), words))
max = max(words_lengths)
index = words_lengths.index(max)

print("(a) najdluzszy wyraz: ", words[index])
print("(b) dlugosc najdluzszego wyrazu: ", max)

# ZADANIE 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

print("\n2.15 Zostanie stworzony napis bedacy ciagiem cyfr kolejnych liczb podanej listy.")
n = int(input("Liczba elementow listy L: "))
L = []

for i in range(n):
    L.append(input("Element " + str(i + 1) + " listy: "))

print('Ciag cyfr kolejnych liczb z listy L: ', "".join(L))

# ZADANIE 2.16
# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

line = input("\n2.16 Ciag znakow 'GvR' w podanym tescie zostanie zamieniony na 'c': ")
line = line.replace('GvR', 'Guido van Rossum')
print(line)

# ZADANIE 2.17
# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
line = input("\n2.17 Wyrazy z podanego napisu zostana posortowane: (a) alfabetycznie i (b) pod wzgledem dlugosci: ")
line_words = line.split()
a_sorted = sorted(line_words)
b_sorted = sorted(line_words, key=len)
print("(a) alfabetycznie: ", a_sorted)
print("(b) pod wzgledem dlugosci: ", b_sorted)

# ZADANIE 2.18
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

n = int(input("\n2.18 Zostanie znaleziona liczba cyfr zero w podanej liczbie calkowitej: "))
n = str(n)
zero_count = n.count('0')
print("Liczba cyfr zero: ", zero_count)

# ZADANIE 2.19 Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych
# bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
print("\n2.19 Zostanie zbudowany napis z trzycyfrowych blokow z dopelnieniem zera.")
n = int(input("Liczba elementow listy L: "))
L = []

for i in range(n):
    L.append(input("Podaj liczbe jedno-/dwu-/trzycyfrowa do listy: " + str(i + 1) + " listy: "))

print("Podana lista: ", L)
filled_L = list(map(lambda x : str(x).zfill(3), L))
print('Wynik: ', " ".join(filled_L))