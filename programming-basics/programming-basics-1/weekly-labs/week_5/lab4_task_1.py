"""
Complete all of the following functions. Currently, they all just
'pass' rather than explicitly return value, meaning they
implicitly return None. They all include doctests, which you can
test by running this file.
The doctests are just examples. Feel free to add your doctests.
"""


# ****************************************
# Problem 1
# ****************************************
def get_position(char: str) -> int | None:
    """
    Return the integer position of the letter in the English alphabet.

    :param char: str, The character to find the position of.
    :return: int or None, The position of the letter in the English alphabet,
    or None if the argument is not a letter.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj') is None
    True
    >>> get_position('1') is None
    True
    """
    if not isinstance(char, str):
        return None
    if len(char) != 1 or not char.isalpha():
        return None

    char = char.upper()
    return ord(char) - 64


# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1: str, ch2: str) -> bool | None:
    """
    Compare two char by their position in the English alphabet.

    :param ch1: str, The first character to compare.
    :param ch2: str, The second character to compare.
    :return: bool or None, True if letter ch2 appears before ch1,
    False otherwise. If neither ch1 nor ch2 are letters,
    the function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('C', 'b')
    True
    >>> compare_char('d', 'ad') is None
    True
    >>> compare_char('2', 2) is None
    True
    >>> compare_char('1', '2') is None
    True
    """
    if not (isinstance(ch1, str) and isinstance(ch2, str)):
        return None
    if len(ch1) != 1 or len(ch2) != 1:
        return None
    if ch1.isalpha() and ch2.isalpha():
        ch1 = ch1.upper()
        ch2 = ch2.upper()
        return ch1 > ch2
    return None


# ****************************************
# Problem 3
# ****************************************
def compare_str(s1: str, s2: str) -> bool | None:
    """
    Compare two strings lexicographically according to the English alphabet.
    Return True if string s1 is larger than string s2 and False otherwise.
    If arguments aren't strings, the strings have different lengths, or
    any character in the string is not alphabetic,
    the function should return None.

    :param s1: str, The first string to compare.
    :param s2: str, The second string to compare.
    :return: bool or None, True if string s1 is larger than string s2,
    False otherwise. If arguments aren't strings or if the strings have
    different lengths or if any character in the string is not alphabetic,
    the function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    >>> compare_str('1', '2')

    >>> compare_str('za1', 'za2')

    """
    if not (isinstance(s1, str) and isinstance(s2, str)):
        return None
    if len(s1) != len(s2):
        return None
    if not (s1.isalpha() and s2.isalpha()):
        return None

    return s1.lower() > s2.lower()


# ****************************************
# Problem 4
# ****************************************
def type_by_angles(alpha: int, beta: int, gamma: int) -> str | None:
    """
    Detect the type of triangle by its angles in degrees and return the type
    as a string ("right triangle", "obtuse triangle", "acute triangle").
    If there is no triangle with such angles,
    then the function should return None.

    :param alpha: int, The first angle of the triangle.
    :param beta: int, The second angle of the triangle.
    :param gamma: int, The third angle of the triangle.
    :return: str or None, The type of triangle or None if the angles do not
    form a triangle.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right triangle'
    >>> type_by_angles(120, 30, 30)
    'obtuse triangle'
    >>> type_by_angles(2015, 2015, 2015) is None
    True
    """
    if not (isinstance(alpha, int) and isinstance(beta, int) and isinstance(gamma, int)):
        return None

    if alpha + beta + gamma == 180:
        if alpha < 90 and beta < 90 and gamma < 90:
            return 'acute triangle'
        elif alpha == 90 or beta == 90 or gamma == 90:
            return 'right triangle'
        else: return 'obtuse triangle'
    else:
        return None


# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a: int | float, b: int | float, c: int | float) -> str | None:
    """
    Detect the type of triangle by its sides and return the type as a string
    ("right triangle", "obtuse triangle", "acute triangle"). If there is no
    triangle with such sides, then the function should return None.

    :param a: int or float, The first side of the triangle.
    :param b: int or float, The second side of the triangle.
    :param c: int or float, The third side of the triangle.
    :return: str or None, The type of triangle or None if the sides do not
    form a triangle.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3.5, 3.5, 6.5)
    'obtuse triangle'
    >>> type_by_sides(3, 4, 5)
    'right triangle'
    >>> type_by_sides(3, 4, 6)
    'obtuse triangle'
    >>> type_by_sides(3, 3, 2015)

    """
    if not all(isinstance(_, (int, float)) for _ in [a, b, c]):
        return None
    if a + b > c:
        if (a**2) + (b**2) > (c**2):
            return 'acute triangle'
        elif (a**2) + (b**2) == (c**2):
            return 'right triangle'
        else:
            return 'obtuse triangle'
    else:
        return None


# ****************************************
# Problem 6
# ****************************************
def number_of_sentences(s: str) -> int | None:
    """
    Find the number of sentences in the string.
    Sentences end only with the following symbols: ..., ., ?, !, ?!
    And there are no such symbols in the middle of a sentence.
    If the argument is not a string, the function should return None.

    :param s: str, The string to count sentences in.
    :return: int or None, The number of sentences or
    None if the argument is not a string.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences("Is this the real life? Is this just fantasy?!")
    2
    >>> number_of_sentences("This is the end... Or just the beginning?!")
    2
    >>> number_of_sentences(2015)

    """
    if not isinstance(s, str):
        return None

    comma = s.count(",")
    excl_que = s.count("?!")
    exclam = s.count("!") - excl_que
    quest = s.count("?") - excl_que
    dot_3 = s.count("...")
    dot = s.count(".") - dot_3 * 3

    return dot + dot_3 + comma + exclam + quest + excl_que


# ****************************************
# Problem 7
# ****************************************
def decrypt_message(s: str) -> str | None:
    """
    Replace all letters in the input string with the previous letters
    in English alphabet, wrapping around so that 'A' becomes 'Z'
    and 'a' becomes 'z'.
    If the argument is not a string, the function should return None.

    :param s: str, The string to decrypt.
    :return: str or None, The decrypted string,
    or None if the argument is not a string.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message("Afwfs abuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Zever zate your enemies. It affects your judgment.'
    >>> decrypt_message(2015) is None
    True
    >>> decrypt_message(123)
    
    """
    if not isinstance(s, str):
        return None

    output_str = ""
    for _, elem in enumerate(s):
        if elem == "a":
            output_str += "z"
        elif elem == "A":
            output_str += "Z"
        elif elem.isalpha():
            output_str += chr(ord(elem) - 1)
        else:
            output_str += elem
    return output_str


# ****************************************
# Problem 8
# ****************************************
def exclude_letters(s1: str, s2: str) -> str | None:
    """
    Delete all letters from string s2 in string s1.
    If arguments aren't strings or any character in s1 or s2 is not alphabetic,
    function should return None.

    :param s1: str, The string to delete letters from.
    :param s2: str, The string containing letters to delete.
    :return: str or None, The modified string or
    None if the arguments aren't strings or
    any character in s1 or s2 is not alphabetic.

    >>> exclude_letters("aaabb", "b")
    'aaa'
    >>> exclude_letters("abcc", "cczzyy")
    'ab'
    >>> exclude_letters(2015, "sasd")

    >>> exclude_letters("sa.d", "sasd")

    """
    if not (isinstance(s1, str) and isinstance(s2, str)):
        return None

    if s1.isalpha() and s2.isalpha():
        s_answer = ""
        s2 = "".join(set(s2))
        s2 += s2 + s2.upper()
        for _, elem in enumerate(s1):
            if elem not in s2:
                s_answer += elem
        return s_answer
    else:
        return None


# ****************************************
# Problem 9
# ****************************************
def create_string(lst: list) -> str | None:
    """
    Create and return a string from the histogram of letters.
    If the argument isn't a list of 26 non-negative
    integer numbers function should return None.

    :param lst: list, The histogram of letters.
    :return: str or None, The created string or None
    if the argument isn't a list of 26 non-negative integers.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    'bcc'
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    'aaaazzzz'
    >>> create_string([4, 0, 0, 0, 0, 0])

    >>> create_string([4, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])

    """
    if not isinstance(lst, list):
        return None
    if len(lst) != 26 or any(lst[j] < 0 for j in range(26)):
        return None

    output_string = ""
    for i in range(26):
        output_string += chr(i + 97) * lst[i]
    return output_string


# ****************************************
# Problem 10
# ****************************************
def get_letters(n: int) -> str | None:
    """
    Create and return a string of the first n letters of the English alphabet.

    If n is not a positive integer between 1 and 26 (inclusive),
    the function returns None.

    :param n: int, The number of letters to include.
    :return: str or None, A string of the first n letters of the alphabet,
    or None if n is invalid.

    >>> get_letters(0) is None
    True
    >>> get_letters(1)
    'a'
    >>> get_letters(5)
    'abcde'
    >>> get_letters(26)
    'abcdefghijklmnopqrstuvwxyz'
    >>> get_letters(34) is None
    True
    >>> get_letters(-2015) is None
    True
    """
    if 0 < n < 27:
        output_string = ""
        for i in range(n):
            output_string += chr(i + 97)
        return output_string
    else:
        return None


# ****************************************
# Problem 11
# ****************************************
def polynomial_eval(coefficients: list, value: int | float) -> float:
    """
    Calculate the value of a polynomial f(x).

    :param coefficients: list, The list of coefficients of the polynomial terms.
    :param value: int or float, The value of x.
    :return: float, The calculated value of the polynomial.

    f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2, 3, 0, 4], 4)
    180

    f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6

    f(x) = 6x^2 - 2x - 20, f(-1) = -12
    >>> polynomial_eval([6, -2, -20], -1)
    -12

    f(x) = 6x^5 - 8x^3 - 8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6, 0, -8, 0, -8, 0], 2)
    112
    >>> polynomial_eval([6, 0, -8, 0, -8, 0], 1)
    -10
    >>> polynomial_eval([6, 0, -8, 0, -8, 0], 0)
    0
    """
    power = len(coefficients)
    ans = 0
    i = 0

    while power > 0:
        ans += coefficients[i] * (value ** power)
        power -= 1
        i += 1
    try:
        return int(ans / value)
    except ZeroDivisionError:
        return 0


# ****************************************
# Problem 12
# ****************************************
def pattern_number(sequence: list | str) -> tuple | None:
    """
    Takes a sequence and returns a tuple (pattern, number of repetitions),
    where the number of repetitions is an integer value >=2. The pattern is
    list of the elements of the sequence that repeat. The list does not
    just contain repeating sequences, but is entirely made up of such
    sequences. The function should return None if
    no repeating patterns are found.

    :param sequence: list or str, The sequence to check for repeating patterns.
    :return: tuple or None, A tuple (pattern, number of repetitions)
    if a repeating pattern is found, otherwise None.

    >>> pattern_number([])

    >>> pattern_number([42])

    >>> pattern_number([1, 2])

    >>> pattern_number([1, 1])
    ([1], 2)
    >>> pattern_number([1, 2, 1])

    >>> pattern_number([1, 2, 3, 1, 2, 3])
    ([1, 2, 3], 2)
    >>> pattern_number([1, 2, 3, 1, 2])

    >>> pattern_number([1, 2, 3, 1, 2, 3, 1])

    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('mama')
    ('ma', 2)
    >>> pattern_number('drum')

    """
    for i in range(1, len(sequence) + 1):
        pattern = sequence[:i]
        if pattern == sequence:
            return None
        for j in range(1, len(sequence) + 1):
            if pattern * j == sequence:
                return pattern, int(len(sequence) / len(pattern))


# ****************************************
# Problem 13
# ****************************************
def one_swap_sorting(sequence):
    """
    The function checks whether the given list of integers can
    become sorted by swapping at most one pair of elements.
    If possible, it returns True; otherwise, it returns False.
    Sequences that are already sorted or cannot be sorted
    with a single swap will return False.

    :param sequence: list of int, The list of integers to evaluate.
    :return: bool, True if the sequence can be sorted with at most one swap,
    False otherwise.

    >>> one_swap_sorting([0, 1, 2, 3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3, 2])
    True
    >>> one_swap_sorting([2, 2])
    False
    >>> one_swap_sorting([5, 2, 3, 4, 1, 6])
    True
    >>> one_swap_sorting([1, 2, 3, 5, 4])
    True
    >>> one_swap_sorting([7, 2, 3, 1, 4, 6])
    False
    >>> one_swap_sorting([1, 2, 3, 7, 4, 5])
    False
    >>> one_swap_sorting([1, 2, 3, 7, 4, 5, 0, 6])
    False
    """
    if any (not isinstance(elem, int) for elem in sequence):
        return False
    if all(elem == sequence[0] for elem in sequence) if sequence else True:
        return False
    sort_list = sorted(sequence)
    if sequence == sort_list:
        return False
    for i, _ in enumerate(sequence):
        for j, _ in enumerate(sequence):
            if i != j:
                sequence[i], sequence[j] = sequence[j], sequence[i]
                if sequence == sort_list:
                    return True
                else:
                    sequence[j], sequence[i] = sequence[i], sequence[j]
    return False


# ****************************************
# Problem 14
# ****************************************
def numbers_ulam(n, start=(1, 2)):
    """
    Generates the first `n` Ulam numbers starting with the given initial two values.

    Ulam numbers are a sequence of numbers where each subsequent number is the
    smallest integer that can be expressed as the sum of two distinct earlier numbers
    in exactly one way. The function returns a list containing the first `n` numbers
    in the sequence, starting from the values provided in `start`.

    If `n == 1`, the function will return a list containing only the first element
    of the `start` tuple. If `n < 1`, an empty list will be returned.

    :param n: int, The number of Ulam numbers to generate.
    :param start: tuple, The initial two values of the Ulam sequence. Defaults to (1, 2).
    :return: list, A list of the first `n` Ulam numbers.

    >>> numbers_ulam(1)
    [1]
    >>> numbers_ulam(-1)
    []
    >>> numbers_ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_ulam(4)
    [1, 2, 3, 4]
    >>> numbers_ulam(2)
    [1, 2]
    >>> numbers_ulam(20)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69]
    >>> numbers_ulam(10, (1, 3))
    [1, 3, 4, 5, 6, 8, 10, 12, 17, 21]
    """
    if n < 1:
        return []

    output_list = list(start)

    for _ in range(n):
        summary = []
        for i, elem1 in enumerate(output_list):
            for j, elem2 in enumerate(output_list):
                if i != j:
                    if elem1 + elem2 > output_list[-1]:
                        summary.append(elem1 + elem2)
        summary = sorted(summary)
        for i, elem in enumerate(summary):
            if summary.count(elem) == 2:
                output_list.append(elem)
                break
    return output_list[:n]


# ****************************************
# Problem 15
# ****************************************
def happy_number(n: int) -> bool:
    """
    Determine whether a given natural number is a happy number.

    A happy number is defined by the following process:
    - Starting with any positive integer,replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 
    (where it will stay), or it loops endlessly in a cycle that does not include 1.
    - A number for which this process ends in 1 is a happy number.

    :param n: int, The number to check.
    :return: bool, True if n is a happy number, False otherwise.

    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    >>> happy_number(10**100)
    True
    >>> happy_number(0)
    False
    >>> happy_number(1)
    True
    """
    if not isinstance(n, int):
        return False
    renum = []
    temp = n
    while n != 1:
        n = temp
        temp = 0
        while n > 0:
            temp += (n % 10) ** 2
            n //= 10
        if temp in renum:
            return False
        renum.append(temp)
        if temp == 1:
            return True
    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
