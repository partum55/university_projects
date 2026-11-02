"""Temp"""


def square_preceding(values: list) -> None:
    """
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    if not values:
        return
    prev = values[0]
    values[0] = 0
    for i in range(1, len(values)):
        current = values[i]
        values[i] = prev ** 2
        prev = current
