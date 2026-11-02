import unittest
from line import Line, Point

class TestLine(unittest.TestCase):
    def setUp(self):
        """Initialize test lines for use in tests."""
        self.line1 = Line(Point(0, 0), Point(1, 1))
        self.line2 = Line(Point(0, 1), Point(1, 0))
        self.line3 = Line(Point(0, 0), Point(1, 2))
        self.line4 = Line(Point(0, 0), Point(2, 4))
        self.line5 = Line(Point(2, 2), Point(3, 3))
        self.line6 = Line(Point(1, 1), Point(2, 2))
    def test_intersect_at_point(self):
        """Check finding the intersection point."""
        intersection = self.line1.intersect(self.line2)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection, Point(0.5, 0.5))
    def test_no_intersection(self):
        """Check that method returns None for non-intersecting lines."""
        self.assertIsNone(self.line1.intersect(self.line5))
    def test_coinciding_lines(self):
        """Check that method returns the first point for coinciding lines."""
        result = self.line3.intersect(self.line4)
        self.assertEqual(result, self.line3.p1)
    def test_vertical_horizontal(self):
        """Check intersection of a vertical and horizontal line."""
        vertical_line = Line(Point(2, 0), Point(2, 3))
        horizontal_line = Line(Point(0, 1), Point(3, 1))
        intersection = vertical_line.intersect(horizontal_line)
        self.assertEqual(intersection, Point(2, 1))
    def test_intersection_at_endpoint(self):
        """Check that method correctly finds intersection at an endpoint."""
        intersection = self.line1.intersect(self.line6)
        self.assertEqual(intersection, Point(1, 1))
    def test_diagonal_intersection(self):
        """Check intersection for a general case of diagonal lines."""
        line_a = Line(Point(1, 1), Point(4, 4))
        line_b = Line(Point(1, 3), Point(3, 1))
        intersection = line_a.intersect(line_b)
        self.assertEqual(intersection, Point(2, 2))
    def test_identical_lines(self):
        """Check that intersecting identical lines returns the first point."""
        identical_line = Line(Point(0, 0), Point(1, 1))
        result = self.line1.intersect(identical_line)
        self.assertEqual(result, self.line1.p1)
    def test_reversed_order(self):
        """Check that intersecting a line with its reversed order returns the first point."""
        reversed_line = Line(Point(1, 1), Point(0, 0))
        result = self.line1.intersect(reversed_line)
        self.assertEqual(result, self.line1.p1)
    def test_intersect_self(self):
        """Check that a line intersected with itself returns the first point."""
        result = self.line1.intersect(self.line1)
        self.assertEqual(result, self.line1.p1)
    def tearDown(self):
        """Clean up after each test."""
        del self.line1, self.line2, self.line3, self.line4, self.line5, self.line6

if __name__ == "__main__":
    unittest.main()
