"""Temp"""


import point


class Triangle:
    """Temp"""

    def __init__(self, p1, p2, p3):
        """
        Temp

        :param p1:
        :param p2:
        :param p3:

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_triangle(self):
        """
        Temp

        :return:

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        return (abs(self.p1.x * (self.p2.y - self.p3.y) + self.p2.x * \
                    (self.p3.y - self.p1.y) + self.p3.x * (self.p1.y - self.p2.y)) / 2) > 0

    def perimeter(self):
        """
        Temp

        :return:
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        return  ((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)**(1/2) + \
            ((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)**(1/2) + \
            ((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)**(1/2)

    def area(self):
        """
        Temp

        :return:

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        return abs(self.p1.x * (self.p2.y - self.p3.y) + self.p2.x * \
                    (self.p3.y - self.p1.y) + self.p3.x * (self.p1.y - self.p2.y)) / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
