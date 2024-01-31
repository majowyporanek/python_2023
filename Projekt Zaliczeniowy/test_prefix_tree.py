import pytest
from prefix_tree import PrefixTree


def test_insert_and_search():
    trie = PrefixTree()
    words_to_insert = ["apple", "app", "apricot", "banana", "berry", "blueberry", "blackberry"]

    for word in words_to_insert:
        trie.insert(word)

    assert set(trie.search("app")) == set(["apple", "app"])
    assert set(trie.search("b")) == set(["banana", "berry", "blueberry", "blackberry"])
    assert set(trie.search("black")) == set(["blackberry"])
    assert trie.search("z") == []


def test_clear():
    trie = PrefixTree()
    words_to_insert = ["apple", "app"]

    for word in words_to_insert:
        trie.insert(word)

    trie.clear()
    assert trie.search("app") == []
