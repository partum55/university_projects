import unittest
from square_preceding import square_preceding


class TestSquare(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        square_preceding(lst)
        self.assertEqual(lst, [])

    def test_single_element(self):
        lst = [5]
        square_preceding(lst)
        self.assertEqual(lst, [0])

    def test_multiple_elements(self):
        lst = [1, 2, 3, 4]
        square_preceding(lst)
        self.assertEqual(lst, [0, 1, 4, 9])

    def test_negative_values(self):
        lst = [-2, 3, -4]
        square_preceding(lst)
        self.assertEqual(lst, [0, 4, 9])

    def test_floats(self):
        lst = [1.5, 2.0, 3.0]
        square_preceding(lst)
        self.assertEqual(lst, [0, 1.5 ** 2, 2.0 ** 2])

    def test_multiple_calls(self):
        lst = [2, 3, 4]
        square_preceding(lst)
        self.assertEqual(lst, [0, 4, 9])
        square_preceding(lst)
        self.assertEqual(lst, [0, 0, 16])

    def test_large_list(self):
        lst = list(range(1, 101))
        expected = [0]
        prev = 1
        for num in range(2, 101):
            expected.append(prev ** 2)
            prev = num
        square_preceding(lst)
        self.assertEqual(lst, expected)


if __name__ == '__main__':
    unittest.main()
