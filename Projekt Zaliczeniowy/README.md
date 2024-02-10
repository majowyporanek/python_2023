# Słownik T9 - Program Konsolowy

## Opis Projektu
Program konsolowy wykorzystujący słownik T9 do wyszukiwania wyrazów w języku angielskim. Umożliwia użytkownikowi wprowadzenie sekwencji cyfr, a następnie przeszukuje i wyświetla pasujące słowa zgodnie z logiką klawiatury T9.

## Składniki Projektu

Projekt składa się z dwóch głównych modułów:

### Moduł: `prefix_tree.py`

#### Klasa: `Node`
Reprezentuje węzeł w drzewie prefiksowym.

- **`__init__(self, value, number=None)`**
  - `value`: Wartość przechowywana w węźle (litera).
  - `number`: Odpowiedni numer T9 dla danej litery.

#### Klasa: `PrefixTree`
Reprezentuje drzewo prefiksowe używane do przechowywania i wyszukiwania słów.

- **`__init__(self)`**
  - Konstruktor klasy PrefixTree. Inicjalizuje korzeń drzewa i mapowanie liter na odpowiadające im numery T9.
  
- **`insert(self, word)`**
  - `word`: Słowo do wstawienia.
  
- **`search_words(self, node, found_word, all_words)`**
  - `node`: Aktualny węzeł.
  - `found_word`: Dotychczas znalezione słowo.
  - `all_words`: Lista znalezionych słów.

- **`search(self, word)`**
  - `word`: Prefiks do wyszukania.

- **`clear(self)`**
  - Czyści drzewo prefiksowe, resetując je do stanu początkowego.

### Moduł: `t9_dictionary.py`

#### Funkcja: `load_words(filepath)`
Ładuje słowa z pliku.
- `filepath`: Ścieżka do ze słowami. Plik użyty w projekcie: [słowa](https://www.mit.edu/~ecprice/wordlist.10000)

#### Klasa: `DictionaryT9`
Zarządza słownikiem T9.

- **`__init__(self, filepath)`**
  - `filepath`: Ścieżka do pliku z słowami.

- **`read_words(self, filepath)`**
  - `filepath`: Ścieżka do pliku z słowami.

- **`find_words_by_prefix(self, prefix)`**
  - `prefix`: Prefiks do wyszukania.

- **`search_words_by_numbers(self, numbers)`**
  - `numbers`: Sekwencja numerów do przekształcenia.

- **`get_words(self, numbers)`**
  - `numbers`: Sekwencja numerów.

#### Funkcja: `display_phone_keypad()`
Wyświetla reprezentację klawiatury telefonu na ekranie.

#### Funkcja: `t9_text_interface(dictionary)`
Interfejs tekstowy dla słownika T9.
- `dictionary`: Instancja słownika T9.

## Przykład użycia programu
przykład nr. 1: docelowy zwrot: "hello world" 
1. Użytkownik jest proszony o wpisanie wybranej sekwencji cyfr
   ![1](https://github.com/majowyporanek/python_2023/assets/80955254/98b436d6-2e02-4436-9955-c83b1cb07d64)
2. Użytkownik widzi pierwszą sugestię na podstawie wpisanego znaku. Aby zobaczyć kolejne sugestie wciska "Enter". Jeżeli sugestia jest trafna - wpisuje "ok". Jeśli chce wpisać nową sekwencje cyfr wpisuje "new".
   ![2](https://github.com/majowyporanek/python_2023/assets/80955254/201a1978-1d25-4978-8cee-9c5f4f45a3ff)
3. Pierwsza sugestia jest trafna. Użytkownik przechodzi do wpisania następnej sekwencji znaków (ilość cyfr != docelowej długości słowa).
   ![image](https://github.com/majowyporanek/python_2023/assets/80955254/20796bb2-4ce3-4996-b0c4-e5869b94d8ad)
4. Użytkownik ma na myśli "world" - pierwsza sugestia nie jest trafna. Naciska 'Enter' aby wyświetlić pozostałe sugestie.
   ![3](https://github.com/majowyporanek/python_2023/assets/80955254/de16f97a-a23c-4292-9563-32ad98376916)
5. Użytkownik akceptuje sugestię "world" a następnie wpisuje "exit" w celu zakończenia działania programu.
   ![4](https://github.com/majowyporanek/python_2023/assets/80955254/999fd34c-6819-4078-bcd7-2ba6ff292cc7)

przykład nr. 2: docelowy zwrot: "experiance" (literówka w wyrazie, poprawnie - "experience")

1. Użytkownik jest proszony o wpisanie wybranej sekwencji cyfr
   ![image](https://github.com/majowyporanek/python_2023/assets/80955254/18368a58-112c-4a18-aedb-a8b1813aa9b6)
2. Użytkownik wpisuje wybraną sekwencję. Okazuję się, że nie ma takiego słowa w słowniku. Użytkownik widzi informację "No words found for this sequence.". Ma możliwość wpisania nowej sekwencji lub wyjścia z programu poprzez 'exit'.
   ![image](https://github.com/majowyporanek/python_2023/assets/80955254/6c6f1855-8e8b-44e5-8452-34681eef84f3)


## Instrukcje Uruchomienia
1. Upewnij się, że masz zainstalowanego Pythona.
2. Sklonuj repozytorium:
      - Otwórz terminal lub wiersz poleceń.
      -`git clone [URL_REPOZYTORIUM]`
      - Przejdź do katalogu projektu: `cd [NAZWA_KATALOGU]`
4. Uruchom `t9_dictionary.py` w terminalu.
   - **Uruchomienie Skryptu**:
      - Uruchom skrypt, wpisując `python t9_dictionary.py` i naciskając Enter.

5. **Interakcja z Programem**:
   - Po uruchomieniu skryptu, zobaczysz interfejs konsolowy.
   - Postępuj zgodnie z instrukcjami na ekranie, aby wprowadzać sekwencje cyfr i wyszukiwać odpowiadające im słowa.

## Testy Jednostkowe

Projekt zawiera testy jednostkowe, które mają na celu zapewnienie poprawności działania kluczowych komponentów aplikacji. Testy jednostkowe są skoncentrowane na weryfikacji funkcjonalności klas PrefixTree i DictionaryT9, a także sprawdzają poprawność operacji wyszukiwania słów i zarządzania drzewem prefiksowym.

### Składniki Testów Jednostkowych
#### prefix_tree_test.py:
Testuje działanie klasy PrefixTree, w tym wstawianie słów, wyszukiwanie prefiksów i czyszczenie drzewa.
#### t9_dictionary_test.py:
Testuje funkcjonalność klasy DictionaryT9, w tym ładowanie słów, wyszukiwanie słów na podstawie prefiksów i numerów T9.
Wykonywanie Testów
Aby uruchomić testy jednostkowe, wykonaj następujące kroki:

Przygotowanie: Upewnij się, że masz zainstalowane wymagane zależności.

#### Uruchomienie Testów:

1. Otwórz terminal lub wiersz poleceń w katalogu projektu.
2. Uruchom testy dla PrefixTree, wpisując python -m unittest test_prefix_tree.
3. Uruchom testy dla DictionaryT9, wpisując python -m unittest test_t9_dictionary.

#### Przykładowy Test
Oto przykład testu jednostkowego dla metody find_words_by_prefix w klasie DictionaryT9:

```python
def test_find_words_by_prefix(self):
    self.assertEqual(sorted(self.dictionary_t9.find_words_by_prefix('ap')), sorted(['apple', 'apply', 'applet']))
```
Test sprawdza, czy metoda find_words_by_prefix poprawnie zwraca listę słów zaczynających się od danego prefiksu.


## Technologie
   - Python

## Źródła
   - [baeldung - tries](https://www.baeldung.com/cs/tries-prefix-trees)
   - [wikipedia - słownik T9](https://pl.wikipedia.org/wiki/S%C5%82ownik_T9)

