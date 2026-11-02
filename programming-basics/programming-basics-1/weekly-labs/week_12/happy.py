"""
Module: happy_numbers

This module provides tools to determine and manipulate "happy numbers" in the context of ticket numbers.
A happy ticket number is defined as a number where the iterative sum of the first four digits equals
the iterative sum of the last four digits of an 8-digit representation of the ticket number.

Key Features:
- Calculate the iterative sum of digits.
- Check if a ticket number is a happy number.
- Count happy ticket numbers within a range.
- Generate a list of happy ticket numbers within a given range.

Functions:
- sum_func(half: str) -> int: Computes the iterative sum of digits until a single-digit number is obtained.
- happy_number(number: int) -> bool: Determines whether a ticket number is a happy number.
- count_happy_numbers(n: int) -> int: Counts all happy numbers up to a given limit.
- happy_numbers(m: int, n: int) -> list: Generates a list of happy numbers within a specified range.
"""


def sum_func(half: str) -> int:
    """
    Calculates the iterative sum of digits for a given string representing a number.

    This function takes a string of digits, computes their sum, and repeats the process
    until a single-digit number is obtained.

    Parameters:
        half (str): A string representation of the number to process.

    Returns:
        int: The single-digit result after iterative summation.

    Example:
    >>> sum_func('1234')
    1
    """
    ans = sum(int(i) for i in half)
    return ans if ans < 10 else sum_func(str(ans))


def happy_number(number: int) -> bool:
    """
    Determines if a ticket number is a happy number.

    A ticket number is considered happy if the iterative sum of its first four digits
    equals the iterative sum of its last four digits. The number is treated as an
    8-digit number by padding with leading zeros if necessary.

    Parameters:
        number (int): The ticket number to check.

    Returns:
        bool: True if the ticket is a happy number, False otherwise.

    Example:
    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    """
    return sum_func(f"{number:0{8}}"[:4]) == sum_func(f"{number:0{8}}"[4:])


def count_happy_numbers(n: int) -> int:
    """
    Counts the number of happy ticket numbers from 1 to a given limit.

    This function checks every ticket number in the range [1, n] (inclusive) and counts
    how many of them are happy numbers.

    Parameters:
        n (int): The upper limit for ticket numbers to evaluate.

    Returns:
        int: The count of happy numbers in the specified range.

    Example:
    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    """
    return 0 if n <= 10000 else sum(1 for i in range(1, n + 1) if happy_number(i))


def happy_numbers(m: int, n: int) -> list:
    """
    Generates a list of happy ticket numbers within a specified range.

    This function checks all ticket numbers in the range [m, n] (inclusive) and returns
    a list of those that are happy numbers.

    Parameters:
        m (int): The lower limit of the range (inclusive).
        n (int): The upper limit of the range (inclusive).

    Returns:
        list[int]: A list of happy ticket numbers within the range.

    Example:
    >>> happy_numbers(1, 10001)
    [10001]
    >>> happy_numbers(10000, 10010)
    [10001, 10010]
    """
    return [] if n < 10000 else [i for i in range(m, n+1) if happy_number(i)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
