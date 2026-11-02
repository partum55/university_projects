"""
Module: math_functions

This module provides recursive and iterative implementations of two fundamental mathematical concepts:
factorials and Fibonacci numbers. The module includes functions to compute these values using both
approaches, demonstrating different methodologies for achieving the same results.

Key Features:
- Calculate the factorial of a number using recursion and iteration.
- Calculate Fibonacci numbers using recursion and iteration.

Functions:
- factorial_recursive(n: int) -> int: Recursively computes the factorial of a number.
- factorial_iterative(n: int) -> int: Iteratively computes the factorial of a number.
- fibonacci_recursive(n: int) -> int: Recursively computes the nth Fibonacci number.
- fibonacci_iterative(n: int) -> int: Iteratively computes the nth Fibonacci number.
"""

from functools import lru_cache


@lru_cache()
def factorial_recursive(n: int) -> int:
    """
    Recursively computes the factorial of a given number.

    The factorial of a non-negative integer n is defined as the product of all positive integers less than or equal to n:
        n! = n × (n-1) × ... × 2 × 1
    By definition, 0! = 1.

    Parameters:
        n (int): The number for which the factorial is to be computed.

    Returns:
        int: The factorial of the given number.

    Example:
        >>> factorial_recursive(6)
        720
    """
    return 1 if n == 0 else factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Iteratively computes the factorial of a given number.

    The factorial of a non-negative integer n is defined as the product of all positive integers less than or equal to n:
        n! = n × (n-1) × ... × 2 × 1
    By definition, 0! = 1.

    Parameters:
        n (int): The number for which the factorial is to be computed.

    Returns:
        int: The factorial of the given number.

    Example:
        >>> factorial_iterative(6)
        720
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@lru_cache()
def fibonacci_recursive(n: int) -> int:
    """
    Recursively computes the nth Fibonacci number.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.

    Example:
        >>> fibonacci_recursive(7)
        13
    """
    return 0 if n == 0 else 1 if n == 1 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Iteratively computes the nth Fibonacci number.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.

    Example:
        >>> fibonacci_iterative(7)
        13
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def time_test(function, verbose=False):
    ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
