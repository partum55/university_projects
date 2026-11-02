"""Temp"""


class Point:
    """Temp"""

    def __init__(self, x: int, y: int):
        """
        Temp

        :param x:
        :param y:

        >>> point = Point(1, 2)
        >>> point.x
        1
        >>> point.y
        2
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Temp

        :return:

        >>> point = Point(1, 2)
        >>> print(point)
        x-coordinate of the point is 1, and y-coordinate is 2.
        """
        return f"x-coordinate of the point is {self.x}, and y-coordinate is {self.y}."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
