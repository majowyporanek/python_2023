import pytest
from rectangles import Rectangle, Point


def test_rectangle_creation():
    rect = Rectangle(1, 2, 3, 4)
    assert str(rect) == "[(1, 2), (3, 4)]"
    assert repr(rect) == "Rectangle(1, 2, 3, 4)"
    assert rect.width == 2
    assert rect.height == 2
    assert rect.area() == 4
    assert rect.top == 4
    assert rect.left == 1
    assert rect.right == 3
    assert rect.bottom == 2
    assert rect.center == Point(2.0, 3.0)


def test_rectangle_move():
    rect = Rectangle(1, 2, 3, 4)
    rect.move(1, 1)
    assert str(rect) == "[(2, 3), (4, 5)]"


def test_rectangle_intersection():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(3, 3, 6, 6)
    intersection = rect1.intersection(rect2)
    assert str(intersection) == "[(3, 3), (4, 4)]"


def test_rectangle_cover():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(3, 3, 6, 6)
    cover = rect1.cover(rect2)
    assert str(cover) == "[(1, 1), (6, 6)]"


def test_rectangle_from_points():
    points = [Point(1, 2), Point(3, 4)]
    rect = Rectangle.from_points(points)
    assert str(rect) == "[(1, 2), (3, 4)]"


def test_invalid_intersection():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(5, 5, 8, 8)
    with pytest.raises(ValueError, match="Brak częsci wspólnej"):
        rect1.intersection(rect2)


if __name__ == "__main__":
    pytest.main()

