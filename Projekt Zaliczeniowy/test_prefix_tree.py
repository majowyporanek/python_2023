import unittest
from prefix_tree import PrefixTree


class TestPrefixTree(unittest.TestCase):

    def setUp(self):
        self.tree = PrefixTree()

    def test_insert_and_search(self):
        words = ["apple", "app", "application", "banana", "band", "bandana"]
        for word in words:
            self.tree.insert(word)
        self.assertEqual(sorted(self.tree.search('app')), sorted(['app', 'apple', 'application']))
        self.assertEqual(self.tree.search('xyz'), [])
        self.assertEqual(sorted(self.tree.search('ban')), sorted(['banana', 'band', 'bandana']))

    def test_clear(self):
        self.tree.insert("clear")
        self.tree.clear()
        self.assertEqual(self.tree.search("clear"), [])


if __name__ == '__main__':
    unittest.main()
