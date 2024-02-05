class Node:
    def __init__(self, value, number=None):
        self.value = value
        self.number = number  # field to store matching T9 number
        self.children = [None] * 26
        self.is_end = False


class PrefixTree:
    """Class representing Prefix Tree."""

    def __init__(self):
        self.root = Node('\0')

        self.letter_to_number = {
            'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3,
            'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5,
            'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7,
            't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9
        }

    def insert(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = Node(char, self.letter_to_number[char])
            current = current.children[index]
        current.is_end = True

    def search_words(self, node, found_word, all_words):
        if not node:
            return
        if node.value != '\0':
            found_word += node.value
        if node.is_end:
            all_words.append(found_word)
        for child in node.children:
            if child:
                self.search_words(child, found_word, all_words)

    def search(self, word):
        current = self.root
        found_word = ''
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                return []
            found_word += current.children[index].value
            current = current.children[index]

        all_words = []
        if found_word == word:
            self.search_words(current, found_word[:-1], all_words)
        return all_words

    def clear(self):
        self.root = Node('\0')