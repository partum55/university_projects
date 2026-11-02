"""
Module for creating a summation table and flattening nested lists.

This module provides two main functionalities:
1. `create_table`: Generates a table where each element is the sum of the elements
   above and to the left.
2. `flatten`: Flattens a nested list into a single list.

Examples:
    create_table(4, 6)
    flatten([1, [2, [3]]])
"""


def create_table(n: int, m: int) -> list[list[int]]:
    """
    Generates a table of dimensions n x m where each element is the sum
    of the element directly above it and the element directly to its left.

    Base cases:
    - If n == 1, the table is a single row filled with 1s.
    - If m == 1, the table is a single column filled with 1s.

    :param n: Number of rows
    :param m: Number of columns
    :return: A list of lists representing the table

    Example:
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    if n == 1:
        return [[1] * m]
    if m == 1:
        return [[1] for _ in range(n)]
    table = create_table(n - 1, m)
    last_row = table[-1]
    new_row = [1] * m
    for j in range(1, m):
        new_row[j] = new_row[j - 1] + last_row[j]
    table.append(new_row)
    return table


def flatten(lst: list) -> list:
    """
    Flattens a nested list into a single list. If the input is not a list,
    it is returned as is.

    :param lst: A potentially nested list to flatten
    :return: A flat list containing all elements of the nested list

    Example:
    >>> flatten([1, [2]])
    [1, 2]
    >>> flatten([1, 2, [3, [4, 5], 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2, [[]]], [True]])
    ['wow', 2, True]
    >>> flatten([])
    []
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    if not isinstance(lst, list):
        return lst
    ans = []
    for elem in lst:
        if isinstance(elem, list):
            ans.extend(flatten(elem))
        else:
            ans.append(elem)
    return ans


if __name__ == "__main__":
    import doctest
    doctest.testmod()
