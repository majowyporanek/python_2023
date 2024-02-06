import unittest
from unittest.mock import patch, mock_open
from t9_dictionary import DictionaryT9


class TestDictionaryT9(unittest.TestCase):

    def setUp(self):
        self.sample_words = ["apple", "banana", "grape", "orange", "peach", "apply", "applet", "bat", "cat", "cater",
                             "date"]
        self.dictionary_t9 = DictionaryT9('./test_words.txt')

        with patch("builtins.open", mock_open(read_data="\n".join(self.sample_words))):
            self.dictionary_t9.read_words('./test_words.txt')

    def test_find_words_by_prefix(self):
        self.assertEqual(sorted(self.dictionary_t9.find_words_by_prefix('ap')), sorted(['apple', 'apply', 'applet']))
        self.assertEqual(sorted(self.dictionary_t9.find_words_by_prefix('ca')), sorted(['cat', 'cater']))

    def test_search_words_by_numbers(self):
        self.assertIn('apple', self.dictionary_t9.search_words_by_numbers([2, 7, 7, 5, 3], 5, ''))
        self.assertIn('bat', self.dictionary_t9.search_words_by_numbers([2, 2, 8], 3, ''))

        multi_word_numbers = [2, 2, 8]  # 'bat', 'cat'
        results = self.dictionary_t9.search_words_by_numbers(multi_word_numbers, len(multi_word_numbers), '')
        self.assertTrue(set(['bat', 'cat']).issubset(set(results)))

    def test_get_words(self):
        number_sequence = [2, 2, 8]  # 'bat', 'cat'
        results = self.dictionary_t9.get_words(number_sequence)
        print(results)
        self.assertTrue(set(['bat', 'cat']).issubset(set(results)))
        long_sequence = [2, 2, 8, 3, 7]
        self.assertIn('cater', self.dictionary_t9.get_words(long_sequence))


if __name__ == '__main__':
    unittest.main()
