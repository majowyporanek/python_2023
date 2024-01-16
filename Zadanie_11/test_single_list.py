import pytest
from single_list import SingleList
from node import Node


def test_list_initialization():
    sl = SingleList()
    assert sl.is_empty() == True
    assert sl.head is None
    assert sl.tail is None
    assert sl.count() == 0


def test_remove_tail():
    sl = SingleList()
    sl.insert_head(Node(40))
    sl.insert_tail(Node(50))
    removed_node = sl.remove_tail()
    assert removed_node.data == 50
    assert sl.tail.data == 40
    assert sl.count() == 1


def test_join_lists():
    sl1 = SingleList()
    sl2 = SingleList()
    sl1.insert_head(Node(60))
    sl2.insert_head(Node(70))
    sl1.join(sl2)
    assert sl1.tail.data == 70
    assert sl2.is_empty()


def test_clear_list():
    sl = SingleList()
    sl.insert_head(Node(80))
    sl.insert_tail(Node(90))
    sl.clear()
    assert sl.is_empty()
    assert sl.count() == 0


pytest.main()
