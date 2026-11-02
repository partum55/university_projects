"""
Module to calculate the area of a convex quadrilateral formed by four lines.

This module provides the following functionalities:
1. Calculate the intersection points of four lines.
2. Compute the distance between points.
3. Calculate the area of a quadrilateral formed by the intersection of four lines.
4. Check if lines are parallel, and handle such cases.

Main function:
    - four_lines_area: Given four lines, calculate the area of the quadrilateral formed.

Helper functions:
    - lines_intersection: Finds the intersection point of two lines.
    - distance: Calculates the Euclidean distance between two points.
    - quadrangle_area: Computes the area of a quadrilateral based on sides and diagonals.
"""


import math

def four_lines_area(k1: float | int, c1: float | int, k2: float | int,\
    c2: float | int, k3: float | int, c3: float | int, k4: float | int, c4: float | int) -> float:
    """
    Calculate the area of a convex quadrilateral formed by the intersection of four lines.

    Args:
        k1, c1: Floats or integers, slope (k1) and intercept (c1) of the first line.
        k2, c2: Floats or integers, slope (k2) and intercept (c2) of the second line.
        k3, c3: Floats or integers, slope (k3) and intercept (c3) of the third line.
        k4, c4: Floats or integers, slope (k4) and intercept (c4) of the fourth line.

    Returns:
        Float rounded to two decimal places representing the area of the quadrilateral.
        Returns 0 if no valid quadrilateral can be formed (e.g., three parallel lines).

    Doctest:
    >>> four_lines_area(1, 0, -1, 4, 1, -4, -1, 0)
    8.0
    >>> four_lines_area(2, 3, 2, 5, 3, 1, -2, 0)
    0
    """
    intr1 = lines_intersection(k1, c1, k2, c2)
    intr2 = lines_intersection(k2, c2, k3, c3)
    intr3 = lines_intersection(k3, c3, k4, c4)
    intr4 = lines_intersection(k4, c4, k1, c1)

    if not all([intr1, intr2, intr3, intr4]):
        return 0

    a = distance(intr1[0], intr1[1], intr2[0], intr2[1])
    b = distance(intr2[0], intr2[1], intr3[0], intr3[1])
    c = distance(intr3[0], intr3[1], intr4[0], intr4[1])
    d = distance(intr4[0], intr4[1], intr1[0], intr1[1])

    f1 = distance(intr1[0], intr1[1], intr3[0], intr3[1])
    f2 = distance(intr2[0], intr2[1], intr4[0], intr4[1])

    area = quadrangle_area(a, b, c, d, f1, f2)
    return round(area, 2)


def lines_intersection(k1: float | int, c1: float | int,\
    k2: float | int, c2: float | int) -> tuple | None:
    """
    Calculate the intersection point of two lines y = k1*x + c1 and y = k2*x + c2.

    Args:
        k1, c1: Floats or integers, slope (k1) and intercept (c1) of the first line.
        k2, c2: Floats or integers, slope (k2) and intercept (c2) of the second line.

    Returns:
        Tuple (x, y) representing the intersection point.
        Returns None if lines are parallel or coincident.

    Doctest:
    >>> lines_intersection(1, 0, -1, 4)
    (2.0, 2.0)
    >>> lines_intersection(2, 3, 2, 5)

    """
    if k1 == k2:
        return None
    x = (c1 - c2) / (-k1 + k2)
    y = (-k1 * c2 + k2 * c1) / (-k1 + k2)
    return round(x, 2), round(y, 2)


def distance(x1: float | int, y1: float | int, x2: float | int, y2: float | int) -> float:
    """
    Calculate the distance between two points (x1, y1) and (x2, y2).

    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.

    Returns:
        Float rounded to two decimal places representing the distance.

    Doctest:
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(1, 1, 4, 5)
    5.0
    """
    dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return round(dist, 2)


def quadrangle_area(a: float, b: float, c: float, d: float, f1: float, f2: float) -> float | None:
    """
    Calculate the area of a convex quadrilateral using side lengths and diagonals.

    Args:
        a, b, c, d: Lengths of the quadrilateral's sides.
        f1, f2: Lengths of the quadrilateral's diagonals.

    Returns:
        Float rounded to two decimal places representing the area of the quadrilateral.
        Returns None if no valid quadrilateral can be formed.

    Doctest:
    >>> quadrangle_area(5.0, 5.0, 5.0, 5.0, 7.07, 7.07)
    24.99
    >>> quadrangle_area(3.0, 4.0, 5.0, 6.0, 8.0, 7.0)
    27.64
    """
    try:
        area = (math.sqrt(4 * (f1**2) * (f2**2) - ((b**2 + d**2 - a**2 - c**2) ** 2))) / 4
    except ValueError:
        return None
    return round(area, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
