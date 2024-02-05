# Słownik T9 - Program Konsolowy

## Opis Projektu
Program konsolowy wykorzystujący słownik T9 do wyszukiwania wyrazów. Umożliwia użytkownikowi wprowadzenie sekwencji cyfr, a następnie przeszukuje i wyświetla pasujące słowa zgodnie z logiką klawiatury T9.

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

## Instrukcje Uruchomienia
1. Upewnij się, że masz zainstalowanego Pythona.
2. Uruchom `t9_dictionary.py` w terminalu.
   - **Uruchomienie Skryptu**:
      - Otwórz terminal lub wiersz poleceń.
      - Przejdź do katalogu, w którym znajduje się skrypt `t9_dictionary.py`.
      - Uruchom skrypt, wpisując `python t9_dictionary.py` i naciskając Enter.

3. **Interakcja z Programem**:
   - Po uruchomieniu skryptu, zobaczysz interfejs konsolowy.
   - Postępuj zgodnie z instrukcjami na ekranie, aby wprowadzać sekwencje cyfr i wyszukiwać odpowiadające im słowa.

## Technologie
   - Python

