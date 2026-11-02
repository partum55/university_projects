"""
Smart People Rescue System

This module implements a system for organizing people based on their IQ scores into groups
that respect a maximum combined IQ limit.
"""


def sort_people(lst: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    Custom Quick Sort to sort a list of tuples (name, score).

    :param lst: List of tuples where each tuple contains (name, score)
    :return: Sorted list in descending order by score, then ascending by name

    Examples:
    >>> sort_people(list(read_file("smart_people.txt").items()))
    [('Marilyn vos Savant', 186), ('Judith Polgar', 170), ('Elon Musk', 165), \
('Quentin Tarantino', 163), ('Bill Gates', 160), ("Conan O'Brien", 160), \
('Will Smith', 157), ('Mark Zuckerberg', 152), ('Barack Obama', 137), ('Emma Watson', 132)]
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left = [x for x in lst[:-1] if (x[1] > pivot[1]) or (x[1] == pivot[1] and x[0] <= pivot[0])]
    right = [x for x in lst[:-1] if (x[1] < pivot[1]) or (x[1] == pivot[1] and x[0] > pivot[0])]
    return sort_people(left) + [pivot] + sort_people(right)


def read_file(file_path: str) -> dict[str, int]:
    """
    Reads a CSV file containing people's names and IQ scores.

    :param file_path: Path to the CSV file (format: Name,IQ)
    :return: Dictionary mapping names to IQ scores
    :raises FileNotFoundError: If file doesn't exist
    :raises ValueError: If file format is invalid

    Examples:
    >>> read_file("smart_people.txt")
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    """
    with open(file_path, "r", encoding="utf-8") as file:
        rescue = dict(map(lambda x: (x[0], int(x[1])),
                          (line.strip().split(",") for line in file if not line.startswith("#"))))
    return rescue


def rescue_people(smarties: dict[str, int], limit_iq: int) -> tuple[int, list]:
    """
    Groups people into teams while respecting a maximum combined IQ limit per team.

    :param smarties: Dictionary mapping names to IQ scores
    :param limit_iq: Maximum allowed sum of IQ scores per group
    :return: Tuple (number of groups, list of groups with names)

    Example:
    >>> rescue_people({'Steve Jobs': 161, 'Albert Einstein': 160, \
    'Sir Isaac Newton': 140, 'Nikola Tesla': 139}, 300)
    (2, [['Steve Jobs', 'Nikola Tesla'], ['Albert Einstein', 'Sir Isaac Newton']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
    "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    """
    ans = []
    smarties = sort_people(list(smarties.items()))
    while smarties:
        group = []
        total_iq = 0
        remaining = []
        for name, iq in smarties:
            if total_iq + iq <= limit_iq:
                group.append(name)
                total_iq += iq
            else:
                remaining.append((name, iq))
        ans.append(group)
        smarties = remaining
    return len(ans), ans


if __name__ == "__main__":
    import doctest
    doctest.testmod()
