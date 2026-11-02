"""
This module provides a functions to count and output happy tickets for
tram. But doctests were broken or another logic was in problem statement.
"""


def happy_number(number: int) -> bool | None:
    """
    Determines if a ticket number is a happy number.

    :param number: The ticket number to check.
    :type number: int
    :return: True if the ticket is a happy number, False otherwise.
    :rtype: bool

    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    """
    if not isinstance(number, int):
        return None
    number = f"{number:0{8}}"
    num1, num2 = number[:4], number[4:]
    while True:
        if len(num1) == 1 and len(num2) == 1:
            break
        sum1, sum2 = 0, 0
        for i in num1:
            sum1 += int(i)
        for i in num2:
            sum2 += int(i)
        num1, num2 = f"{sum1}", f"{sum2}"
    return sum1 == sum2

def count_happy_numbers(n: int) -> int | None:
    """
    Counts the number of happy tickets from 1 to n inclusive.

    :param n: The upper limit of ticket numbers to check.
    :type n: int
    :return: The count of happy tickets in the range.
    :rtype: int

    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    >>> count_happy_numbers(10100)
    12
    >>> count_happy_numbers(100000)
    9999
    """
    if not isinstance(n, int):
        return None
    if n <= 10000:
        return 0
    k = 0
    for i in range(10000, n+1):
        if happy_number(i):
            k += 1
    return k


def happy_numbers(m: int, n: int) -> list[int] | None:
    """
    Generates a list of happy ticket numbers within the given range.

    :param m: The lower limit of ticket numbers (inclusive).
    :type m: int
    :param n: The upper limit of ticket numbers (inclusive).
    :type n: int
    :return: A list of happy ticket numbers in the range.
    :rtype: list[int]

    >>> happy_numbers(1, 10001)
    [10001]
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(1, 11)
    []
    >>> happy_numbers(10001, 10100)
    [10001, 10010, 10019, 10028, 10037, 10046, 10055, 10064, 10073, 10082, 10091, 10100]
    """
    if (not (isinstance(n, int) and isinstance(m, int))) or m > n:
        return None
    if n <= 10000:
        return []
    k = []
    for i in range(m, n+1):
        if happy_number(i):
            k.append(i)
    return k


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
