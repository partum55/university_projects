"""
big_digits.py

This module provides functionality to convert a string of digits into large
ASCII art representations using custom patterns for each digit.

The `return_digits` function takes a string of digits (0-9) and returns a large-scale
ASCII art representation of the digits, where the stars ('*') are replaced with the
corresponding digit.
"""

import sys


ZERO = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
ONE = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
TWO = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
THREE = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
FOUR = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
FIVE = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
SIX = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
SEVEN = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
EIGHT = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
NINE = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

def return_digits(number: str) -> str:
    """
    Converts a string of digits (0-9) into a large ASCII art representation, where
    the '*' symbols are replaced with the corresponding digit.

    Parameters:
    number (str): A string of digits to be converted into ASCII art.

    Returns:
    str: A string containing the large ASCII art representation of the digits.

    Example:
    >>> return_digits("4128")
    '   4   1  222  888 \\n  44  11 2   28   8\\n 4 4   1 2  2 8\
   8\\n4  4   1   2   888 \\n444444 1  2   8   8\\n   4   1 2    8   8\\n   4\
  11122222 888 '
    """
    if not (number.isnumeric() and isinstance(number, str)):
        return None

    output = ""
    for i in range(7):
        for elem in number:
            digit = int(elem)
            output += DIGITS[digit][i].replace("*", f"{digit}")
        output += "\n" if i != 6 else ""
    return output


if __name__ == "__main__":
    try:
        digits = sys.argv[1]
        print(return_digits(digits))
    except IndexError:
        print("usage example: python bigdigits.py <number>")
    except ValueError as err:
        print(f"Error: {err} in {digits}")

    import doctest
    doctest.testmod()
