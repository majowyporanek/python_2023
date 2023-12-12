from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle{self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y}"

    def __eq__(self, other):
        return bool(self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):
        return not self == other

    @property
    def center(self):
        x = (self.pt2.x + self.pt1.x) / 2
        y = (self.pt2.y + self.pt1.y) / 2
        return Point(x, y)

    def area(self):
        pole = (abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y))
        return pole

    def move(self, x, y):  # przesunięcie o (x, y)
        move = Point(x, y)
        self.pt1 = self.pt1 + move
        self.pt2 = self.pt2 + move
        return f"[{self.pt1}, {self.pt2}]"

    def intersection(self, other):
        if (
                self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y or self.pt1.x > other.pt2.x or self.pt2.x < other.pt1.x):
            raise ValueError("Brak częsci wspólnej")
        else:
            intersection = Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y),
                                   min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        return intersection

    def cover(self, other):
        cover = Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x),
                               max(self.pt2.y, other.pt2.y))
        return cover

    def make4(self):
        krotka = (Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y),
                  Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y),
                  Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y),
                  Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y))

        return krotka

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError('Nalezy podac dwa punkty')
        rect = cls(points[0].x, points[0].y, points[1].x, points[1].y)
        return rect

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

# Point: topleft, bottomleft, topright, bottomright.
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)



