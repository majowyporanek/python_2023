import pytest
from randomqueue import RandomQueue


def test_insert():
    queue = RandomQueue(5)
    for i in range(5):
        queue.insert(i)
        assert not queue.is_empty()

    with pytest.raises(OverflowError):
        queue.insert(6)


def test_remove():
    queue = RandomQueue(5)
    for i in range(5):
        queue.insert(i)

    removed_items = set()
    while not queue.is_empty():
        removed_items.add(queue.remove())

    assert len(removed_items) == 5
    assert all(item in range(5) for item in removed_items)

    with pytest.raises(IndexError):
        queue.remove()


def test_is_empty():
    queue = RandomQueue()
    assert queue.is_empty()
    queue.insert(1)
    assert not queue.is_empty()


def test_is_full():
    queue = RandomQueue(2)
    assert not queue.is_full()
    queue.insert(1)
    queue.insert(2)
    assert queue.is_full()


def test_clear():
    queue = RandomQueue()
    queue.insert(1)
    queue.insert(2)
    queue.clear()
    assert queue.is_empty()
