"""
This module provides functionality to analyze a list of
names from a file and derive specific insights.

The primary functionality includes:
 - Determining the three most popular names.
 - Identifying names that occur only once and counting them.
 - Finding the most common starting letter for names and analyzing related statistics.

This module contains a single function, find_names, which implements the above functionality.
"""


def find_names(file_path: str) -> tuple[set[str], tuple[int, set[str]], tuple[str, int, int]]:
    """
    Analyzes a list of names from a file and returns specific insights.

    This function processes a text file containing one name per line and calculates:
    1. The three most popular names.
    2. The count and set of names that occur only once in the file.
    3. The letter with which the most names begin, the count of such names,
       and the total number of children with names starting with that letter.

    :param file_path: The path to the text file containing names.
                      Each line in the file should represent one name.
    :return: A tuple containing three elements:
        - A set of the three most popular names.
        - A tuple where:
            - The first element is the count of names that occur only once.
            - The second element is a set of names that occur only once.
        - A tuple where:
            - The first element is the letter with which the most names begin.
            - The second element is the count of different names starting with that letter.
            - The third element is the total number of children with these names.
    """
    with open (file_path, "r", encoding="utf-8") as file:
        next(file)
        names = []
        for line in file:
            line = line.strip().split()
            names.append((line[0], int(line[-1][1:-1])))
    for i in range(3):
        min_index = i
        for j in range(i, len(names)):
            if names[min_index][1] < names[j][1]:
                names[min_index], names[j] = names[j], names[min_index]
    first = set(name[0] for name in names[:3])

    counter = 0
    unic_names = set()
    for el in names:
        if el[1] == 1:
            counter += 1
            unic_names.add(el[0])
    second = counter, unic_names

    letter_dct = {}
    for el in names:
        letter_dct.setdefault(el[0][0], 0)
        letter_dct[el[0][0]] += 1
    letter_dct = list(letter_dct.items())
    min_index = 0
    for i in range(1, len(letter_dct)):
        if letter_dct[min_index][1] < letter_dct[i][1]:
            min_index = i
    popular_letter = letter_dct[min_index][0]
    counter = 0
    min_index = 0
    for el in names:
        if el[0][0] == popular_letter:
            counter += 1
            min_index += el[1]
    third = popular_letter, counter, min_index

    return first, second, third


if __name__ == "__main__":
    print(find_names("girl_names"))
    print(find_names("boy_names"))
