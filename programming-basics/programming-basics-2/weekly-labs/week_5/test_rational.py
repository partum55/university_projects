import unittest
from rational import *


class TestRationalOperations(unittest.TestCase):
    def test_rational_operations(self):
        rational1 = Rational(1, 4)
        self.assertEqual(rational1.numerator, 1)
        self.assertEqual(rational1.denominator, 4)
        self.assertIsInstance(rational1, Rational)
        self.assertEqual(str(rational1), "1/4")
        with self.assertRaises(ValueError) as cm:
            Rational(1, 0)
        self.assertEqual(str(cm.exception), "Denominator cannot be zero.")
        rational2 = Rational(2, 4)
        self.assertEqual(rational2.numerator, 2)
        self.assertEqual(rational2.denominator, 4)
        self.assertIsInstance(rational2, Rational)
        self.assertEqual(str(rational2), "2/4")
        rational2 = rational2.reduce()
        self.assertEqual(str(rational2), "1/2")
        rational2 = Rational(2, 5)
        self.assertEqual(str(rational1 + rational2), "13/20")
        self.assertEqual(str(rational1 - rational2), "-3/20")
        self.assertEqual(str(rational1 * rational2), "1/10")
        self.assertEqual(str(rational1 / rational2), "5/8")
        self.assertEqual(str((rational1 / rational2 * rational1) - rational1), "-3/32")
        rational3 = Rational(2, 8)
        self.assertEqual(str(rational3), "2/8")
        self.assertTrue(rational1 == rational3)
        self.assertTrue(rational1 < rational2)
        self.assertTrue(rational1 <= rational2)
        self.assertTrue(rational1 <= rational3)
        rational3 = Rational(2, -8)
        self.assertEqual(str(rational3), "-2/8")
        rational4 = Rational(10, 8)
        self.assertEqual(str(rational4), "10/8")
        self.assertEqual(rational4.mixed_form, "1 2/8")
        rational4.mixed_form = '2 3/5'
        self.assertEqual(str(rational4), '13/5')
        self.assertIsInstance(rational4, Rational)
        rational4.mixed_form = '3/5'
        self.assertEqual(str(rational4), '3/5')
        rational5 = Rational(0, -4)
        self.assertEqual(str(rational5), '0/4')
        self.assertEqual(str(rational5.reduce()), '0/1')
        rational6 = Rational(10, -8)
        self.assertEqual(str(rational6), "-10/8")
        self.assertEqual(rational6.mixed_form, "-1 2/8")
        rational7 = Rational(-10, 8)
        self.assertEqual(str(rational7), "-10/8")
        self.assertEqual(rational7.mixed_form, "-1 2/8")
        rational4.mixed_form = "-1 2/8"
        self.assertEqual(str(rational4), '-10/8')
        self.assertEqual(rational4.numerator, -10)
        self.assertEqual(rational4.denominator, 8)
        self.assertIsInstance(rational4, Rational)
        rational4.mixed_form = "0 2/8"
        self.assertEqual(str(rational4), '2/8')

class TestRationalMixedForm(unittest.TestCase):
    def test_proper_fraction(self):
        r = Rational(1, 1)
        r.mixed_form = "3/4"
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)
        self.assertEqual(r.mixed_form, "3/4")
    def test_valid_mixed_fraction(self):
        r = Rational(0, 1)
        r.mixed_form = "3 1/2"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 2)
        self.assertEqual(r.mixed_form, "3 1/2")
    def test_negative_mixed_fraction(self):
        r = Rational(0, 1)
        r.mixed_form = "-3 1/2"
        self.assertEqual(r.numerator, -7)
        self.assertEqual(r.denominator, 2)
        self.assertEqual(r.mixed_form, "-3 1/2")
    def test_negative_proper_fraction(self):
        r = Rational(0, 1)
        r.mixed_form = "-3/4"
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 4)
        self.assertEqual(r.mixed_form, "-3/4")
    def test_improper_fractional_part(self):
        r = Rational(0, 1)
        with self.assertRaises(ValueError):
            r.mixed_form = "3 5/4"
    def test_negative_fractional_part(self):
        r = Rational(0, 1)
        with self.assertRaises(ValueError):
            r.mixed_form = "3 -1/2"
    def test_extra_whitespace(self):
        r = Rational(0, 1)
        r.mixed_form = "  3   1/2  "
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 2)
        self.assertEqual(r.mixed_form, "3 1/2")
    def test_invalid_format_extra_parts(self):
        r = Rational(0, 1)
        with self.assertRaises(ValueError):
            r.mixed_form = "3 1/2 1/3"
    def test_fraction_with_zero_numerator_in_mixed(self):
        r = Rational(0, 1)
        r.mixed_form = "3 0/4"
        self.assertEqual(r.numerator, 12)
        self.assertEqual(r.denominator, 4)
        self.assertEqual(r.mixed_form, "3")
    def test_negative_denominator_in_fraction_format(self):
        r = Rational(0, 1)
        r.mixed_form = "3/-4"
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 4)
        self.assertEqual(r.mixed_form, "-3/4")
    def test_empty_string(self):
        r = Rational(0, 1)
        with self.assertRaises(ValueError):
            r.mixed_form = ""
    def test_invalid_format_no_slash(self):
        r = Rational(0, 1)
        with self.assertRaises(ValueError):
            r.mixed_form = "3 12"

if __name__ == "__main__":
    unittest.main()
