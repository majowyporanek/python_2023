import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [-1, 2]  # -1/2
        self.f2 = [1, -2]  # -1/2 (niejednoznaczność)
        self.f3 = [0, 1]  # zero
        self.f4 = [0, 2]  # zero (niejednoznaczność)
        self.f5 = [3, 1]  # 3
        self.f6 = [6, 2]  # 3 (niejednoznaczność)
        self.f7 = [1, 2]  # 1/2
        self.f8 = [1, 3]  # 1/3
        self.f9 = [7, 99]  # 7/99
        self.f10 = [-99, 7]  # -99/7

    def test_add_frac(self):
        self.assertEqual(add_frac(self.f7, self.f8), [5, 6])
        self.assertEqual(add_frac(self.f5, self.f6), [6, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f1, self.f2), [0, 1])
        self.assertEqual(sub_frac(self.f9, self.f8), [-26, 99])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f9, self.f10), [-1, 1])
        self.assertEqual(mul_frac(self.f5, self.f6), [9, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f5, self.f6), [1, 1])

        with self.assertRaises(ValueError, msg="Denominator cannot be zero."):
            div_frac(self.f7, self.f3)

    def test_is_positive(self):
        self.assertTrue(is_positive(self.f5))
        self.assertFalse(is_positive(self.f10))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.f6))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f3, self.f4), 0)
        self.assertEqual(cmp_frac(self.f3, self.f10), 1)
        self.assertEqual(cmp_frac(self.f10, self.f7), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.f8), 1 / 3)
        self.assertEqual(frac2float(self.f9), 7 / 99)
        self.assertEqual(frac2float(self.f10), -99 / 7)
        self.assertEqual(frac2float(self.f3), 0.0)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
