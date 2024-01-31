import json
from prefix_tree import PrefixTree
from linked_list import LinkedList


def load_words_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data['words']


class DictionaryT9:
    def __init__(self, filepath):
        self.words_store = PrefixTree()
        self.nums_to_letters = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        self.filepath = filepath
        self.read_words(filepath)
        self.wordstore = []

    def read_words(self, filepath):
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    self.words_store.insert(line.strip())
        except IOError:
            print("Error with opening a file with words!")

    def find_words_by_prefix(self, prefix):
        return self.words_store.search(prefix)

    def search_words_by_numbers(self, numbers, length, prefix, result=None):
        if result is None:
            result = LinkedList()

        if length == 0:
            for word in self.find_words_by_prefix(prefix):
                result.push_back(word)
            return result

        letters = self.nums_to_letters.get(numbers[0], "")

        for letter in letters:
            new_prefix = prefix + letter
            self.search_words_by_numbers(numbers[1:], length - 1, new_prefix, result)

        return result

    def get_words(self, numbers):
        self.wordstore.clear()
        results = self.search_words_by_numbers(numbers, len(numbers), "")

        # Sort the results based on word length
        sorted_results = sorted(results, key=len)

        # Start from the length of the input number string
        starting_length = len(numbers)
        for word in sorted_results:
            if len(word) >= starting_length:
                self.wordstore.append(word)

        return self.wordstore


def display_phone_keypad():
    keypad = [
        "|1      | 2 abc | 3 def",
        "|4 ghi  | 5 jkl | 6 mno",
        "|7 pqrs | 8 tuv | 9 wxyz",
        "|*      | 0     | #"
    ]
    for line in keypad:
        print(line)


def t9_text_interface(dictionary):
    sentence = []

    while True:
        display_phone_keypad()
        input_string = input("Enter number sequence (or 'exit' to quit): ").lower()

        if input_string == 'exit':
            break

        if input_string == 'ok':
            if sentence:
                print("Final Sentence:", ' '.join(sentence))
                break
            else:
                print("No sentence created.")
                continue

        try:
            number_sequence = [int(char) for char in input_string if char.isdigit()]
            words = dictionary.get_words(number_sequence)

            word_index = 0
            while True:
                if not words:
                    print("No words found for this sequence.")
                    break

                print("Current Word:", words[word_index])
                choice = input(
                    "Press 'Enter' to change word, type 'ok' to select, 'new' to enter a new sequence: ").lower()

                if choice == 'ok':
                    sentence.append(words[word_index])
                    print("Current Sentence:", ' '.join(sentence))
                    break
                elif choice == 'new':
                    break
                else:
                    word_index = (word_index + 1) % len(words)
        except ValueError:
            print("Please enter a valid number sequence.")


if __name__ == '__main__':
    file_path = './words.txt'
    dictionary_t9 = DictionaryT9(file_path)
    t9_text_interface(dictionary_t9)
