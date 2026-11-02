"""Temp"""


class Point:
    """Class Point"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    """Class Line"""

    def __init__(self, p1: Point, p2: Point):
        if p1 == p2:
            raise ValueError("A line cannot be defined by two equal points")
        self.p1 = p1
        self.p2 = p2

    def intersect(self, other: 'Line'):
        """Temp"""
        A1 = self.p2.y - self.p1.y
        B1 = self.p1.x - self.p2.x
        C1 = A1 * self.p1.x + B1 * self.p1.y
        A2 = other.p2.y - other.p1.y
        B2 = other.p1.x - other.p2.x
        C2 = A2 * other.p1.x + B2 * other.p1.y
        denom = A1 * B2 - A2 * B1
        if denom != 0:
            x = (B2 * C1 - B1 * C2) / denom
            y = (A1 * C2 - A2 * C1) / denom
            if (min(self.p1.x, self.p2.x) <= x <= max(self.p1.x, self.p2.x) and
                    min(self.p1.y, self.p2.y) <= y <= max(self.p1.y, self.p2.y) and
                    min(other.p1.x, other.p2.x) <= x <= max(other.p1.x, other.p2.x) and
                    min(other.p1.y, other.p2.y) <= y <= max(other.p1.y, other.p2.y)):
                return Point(x, y)
            return None
        else:
            if A1 * other.p1.x + B1 * other.p1.y != C1:
                return None
            common = {(self.p1.x, self.p1.y), (self.p2.x, self.p2.y)}.intersection(
                {(other.p1.x, other.p1.y), (other.p2.x, other.p2.y)})
            if common:
                if len(common) == 1:
                    x, y = list(common)[0]
                    return Point(x, y)
                return self.p1
            if self.p1.x != self.p2.x:
                a, b = sorted([self.p1.x, self.p2.x])
                c, d = sorted([other.p1.x, other.p2.x])
            else:
                a, b = sorted([self.p1.y, self.p2.y])
                c, d = sorted([other.p1.y, other.p2.y])
            overlap_start = max(a, c)
            overlap_end = min(b, d)
            if overlap_start > overlap_end:
                return None
            elif overlap_start == overlap_end:
                if self.p1.x != self.p2.x:
                    t = (overlap_start - self.p1.x) / (self.p2.x - self.p1.x)
                    return Point(overlap_start, self.p1.y + t * (self.p2.y - self.p1.y))
                else:
                    t = (overlap_start - self.p1.y) / (self.p2.y - self.p1.y)
                    return Point(self.p1.x + t * (self.p2.x - self.p1.x), overlap_start)
            else:
                return self.p1

    def __eq__(self, other):
        return isinstance(other, Line) and self.p1 == other.p1 and self.p2 == other.p2

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"
