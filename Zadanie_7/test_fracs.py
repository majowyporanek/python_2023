import unittest
from fracs import Frac


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(1, 2)
        self.frac2 = Frac(3, 4)
        self.int_val = 5

    def test_str(self):
        self.assertEqual(self.frac1.__str__(), "1/2")
        self.assertEqual(Frac(5, 1).__str__(), "5")

    def test_repr(self):
        self.assertEqual(self.frac1.__repr__(), "Frac(1, 2)")

    def test_eq(self):
        self.assertEqual(self.frac1, Frac(1, 2))
        self.assertNotEqual(self.frac1, self.frac2)
        self.assertTrue(self.frac1.__eq__(Frac(1, 2)))

    def test_ne(self):
        self.assertNotEqual(self.frac1, self.frac2)
        self.assertEqual(self.frac1, Frac(1, 2))
        self.assertFalse(self.frac1.__ne__(Frac(1, 2)))

    #
    def test_lt(self):
        self.assertTrue(self.frac1.__lt__(self.frac2))

    #
    def test_le(self):
        self.assertTrue(self.frac1.__le__(Frac(1, 2)))

    def test_gt(self):
        self.assertFalse(self.frac1.__gt__(Frac(1, 2)))

    #
    def test_ge(self):
        self.assertFalse(self.frac1.__ge__(self.frac2))

    #
    def test_add(self):
        result = self.frac1.__add__(self.frac2)
        self.assertEqual(result, Frac(10, 8))

    #
    def test_radd(self):
        result = self.frac1.__add__(2)
        self.assertEqual(result, Frac(5, 2))

    def test_sub(self):
        result = self.frac1.__sub__(self.frac2)
        self.assertEqual(result, Frac(-2, 8))

    #
    def test_mul(self):
        result = self.frac1.__mul__(self.frac2)
        self.assertEqual(result, Frac(3, 8))

    #
    def test_div(self):
        result = self.frac1.__div__(self.frac2)
        self.assertEqual(result, Frac(0, 1))

    def test_rdiv(self):
        result = self.frac2.__rdiv__(2)
        self.assertEqual(result, Frac(2, 1))

    def test_truediv(self):
        result = self.frac1.__truediv__(self.frac2)
        self.assertEqual(result, Frac(4, 6))

    #
    def test_rtruediv(self):
        result = self.frac1.__rtruediv__(2)
        self.assertEqual(result, Frac(4, 1))

    def test_pos(self):
        result = +self.frac1
        self.assertEqual(result, self.frac1)

    def test_neg(self):
        result = -self.frac1
        self.assertEqual(result, Frac(-1, 2))

    def test_invert(self):
        result = ~self.frac1
        self.assertEqual(result, Frac(2, 1))

    def test_float(self):
        result = float(self.frac1)
        self.assertEqual(result, 0.5)

    def test_hash(self):
        result = hash(self.frac1)
        self.assertIsInstance(result, int)

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_unsupported_operand_type(self):
        with self.assertRaises(TypeError):
            result = self.frac1 + "string"


if __name__ == '__main__':
    unittest.main()
