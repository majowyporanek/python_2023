class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 26
        self.is_end = False


class PrefixTree:
    """Klasa reprezentująca Prefix Tree."""

    def __init__(self):
        self.root = Node('\0')

    def insert(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord('a')  # indeks w tablicy
            if not current.children[index]:
                current.children[index] = Node(char)
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