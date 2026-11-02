from turtledemo.paint import switchupdown


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
    if n < 0:
        return []

    index = 0
    output_list = list(start)
    summary = []

    for i in range(1, n + 1):
        for j in range(1, len(output_list) + 1):
            summary.append(j + i)
    summary = sorted(summary)

    while index < n:
        if summary[0] > output_list[-1]:
            index += 1
            output_list += summary[0]
            summary [1:]= summary
        else:
            summary [1:]= summary

    return output_list[:n]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())