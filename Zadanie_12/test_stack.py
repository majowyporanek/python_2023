import pytest
from stack import Stack


def test_push_pop():
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()


def test_is_full():
    stack = Stack(2)
    stack.push(1)
    assert not stack.is_full()
    stack.push(2)
    assert stack.is_full()


def test_overflow_error():
    stack = Stack(1)
    stack.push(1)
    with pytest.raises(OverflowError):
        stack.push(2)


def test_index_error():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
