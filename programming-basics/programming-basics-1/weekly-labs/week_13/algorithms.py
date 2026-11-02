"""Sorting and Searching Algorithms Module

This module contains implementations of common searching and sorting algorithms, including:
- Linear Search
- Binary Search
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

Each function is documented with examples and can be tested using Python's `doctest` module.

Usage:
Run this script directly to execute the embedded doctests for all functions.

"""


def linear_search(list_of_values, value):
    """
    Perform a linear search to find the index of a given value in a list.

    :param list_of_values: A list of elements to search.
    :param value: The value to search for.
    :return: The index of the value if found, otherwise -1.

    Examples:
    >>> linear_search([1, 2, 3, 4, 5], 3)
    2
    >>> linear_search([1, 2, 3, 4, 5], 6)
    -1
    """
    for i, elem in enumerate(list_of_values):
        if elem == value:
            return i
    return -1


def binary_search(list_of_values, value):
    """
    Perform binary search on a sorted list to find the index of a given value.

    :param list_of_values: A sorted list of elements.
    :param value: The value to search for.
    :return: The index of the value if found, otherwise -1.

    Examples:
    >>> binary_search([1, 2, 3, 4, 5], 4)
    3
    >>> binary_search([1], 1)
    0
    >>> binary_search([1], 3)
    -1
    """
    left, right = 0, len(list_of_values) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_of_values[mid] == value:
            return mid
        if list_of_values[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def selection_sort(lst: list) -> list:
    """
    Perform selection sort on a list.

    :param lst: The list to be sorted.
    :return: A new sorted list.

    Examples:
    >>> selection_sort([74, 12, 75, 35, 6, 54, 71, 58, 8, 8, 91])
    [6, 8, 8, 12, 35, 54, 58, 71, 74, 75, 91]
    """
    for i, _ in enumerate(lst):
        min_index = i
        for j in range(i, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def insertion_sort(lst: list) -> list:
    """
    Perform insertion sort on a list.

    :param lst: The list to be sorted.
    :return: A new sorted list.

    Examples:
    >>> insertion_sort([7, 3, 2, 6, 9, 4, 5, 8, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(lst):
    """
    Perform merge sort on a list and return the sorted list.

    :param lst: The list to be sorted.
    :return: A new sorted list.

    Examples:
    >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """
    Helper function to merge two sorted lists.

    :param left: The left sorted list.
    :param right: The right sorted list.
    :return: A merged sorted list.
    """
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


def quick_sort(lst):
    """
    Perform quick sort on a list and return the sorted list.

    :param lst: The list to be sorted.
    :return: A new sorted list.

    Examples:
    >>> quick_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def block_sort(lst):
    """
    Sort a list of numbers using the Block Sort algorithm.

    The algorithm divides the input list into blocks based on the range of values,
    sorts each block individually, and then merges them into a single sorted list.

    :param lst: List of numbers to be sorted.
    :return: A new list containing the sorted numbers.

    Examples:
    >>> block_sort([4, 2, 7, 3, 8, 6, 1, 5])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> block_sort([100, 50, 20, 75, 25])
    [20, 25, 50, 75, 100]
    >>> block_sort([])
    []
    >>> block_sort([1])
    [1]
    >>> block_sort([3, 3, 3])
    [3, 3, 3]
    """
    if not lst:
        return []

    max_value = max(lst)
    min_value = min(lst)
    range_of_values = max_value - min_value + 1

    num_blocks = len(lst) // 10 + 1
    block_size = range_of_values // num_blocks + 1

    blocks = [[] for _ in range(num_blocks)]
    for num in lst:
        index = (num - min_value) // block_size
        blocks[index].append(num)

    for i in range(num_blocks):
        blocks[i] = sorted(blocks[i])

    sorted_list = []
    for block in blocks:
        sorted_list.extend(block)

    return sorted_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
