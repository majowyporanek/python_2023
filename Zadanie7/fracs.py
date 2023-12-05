class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError('Denominator cannot be zero.')
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return f"{self.x}/{self.y}"

    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    # Py2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        self_num = self.x * other.y
        other_num = other.x * self.y
        return self_num < other_num

    def __le__(self, other):
        self_num = self.x * other.y
        other_num = other.x * self.y
        return self_num <= other_num

    def __gt__(self, other):
        self_num = self.x * other.y
        other_num = other.x * self.y
        return self_num > other_num

    def __ge__(self, other):
        self_num = self.x * other.y
        other_num = other.x * self.y
        return self_num >= other_num

    def __add__(self, other):
        if isinstance(other, Frac):
            common_denominator = self.y * other.y
            self_num = self.x * other.y
            other_num = other.x * self.y
            result = Frac(self_num + other_num, common_denominator)
            return result
        elif isinstance(other, int):
            result = Frac(self.x + other * self.y, self.y)
            return result
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    __radd__ = __add__  # int+frac

    def __sub__(self, other):
        if isinstance(other, Frac):
            common_denominator = self.y * other.y
            self_num = self.x * other.y
            other_num = other.x * self.y
            result = Frac(self_num - other_num, common_denominator)
            return result
        elif isinstance(other, int):
            result = Frac(self.x - other * self.y, self.y)
            return result
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, Frac):
            result = Frac(self.x * other.x, self.y * other.y)
            return result
        elif isinstance(other, int):
            result = Frac(self.x * other, self.y)
            return result
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    __rmul__ = __mul__  # int*frac

    def __div__(self, other):
        if isinstance(other, Frac):
            result = Frac(self.x * other.y, self.y * other.x)
            return Frac(result.x // result.y, 1)
        elif isinstance(other, int):
            result = Frac(self.x, self.y * other)
            return Frac(result.x // result.y, 1)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __rdiv__(self, other):
        if isinstance(other, Frac):
            result = Frac(other.x * self.y, other.y * self.x)
            return Frac(result.x // result.y, 1)
        elif isinstance(other, int):
            result = Frac(other * self.y, self.x)
            return Frac(result.x // result.y, 1)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, Frac):
            result = Frac(self.x * other.y, self.y * other.x)
            return result
        elif isinstance(other, int):
            result = Frac(self.x, self.y * other)
            return result
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, Frac):
            result = Frac(other.x * self.y, other.y * self.x)
            return result
        elif isinstance(other, int):
            result = Frac(other * self.y, self.x)
            return result
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):
        return Frac(self.x * (-1), self.y)  # -frac = (-1)*frac

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
