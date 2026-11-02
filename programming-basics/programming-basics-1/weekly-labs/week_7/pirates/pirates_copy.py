"""
treasure.py

This module provides functions solves problems related to treasure maps. Series of movements defines
a path, and the vertices of the path form a polygon. Module includes functions to compute the path
based on the movements, adjust the path to positive coordinates, calculate the map size, generate a
string representation of the map, find vertices of the polygon, compute the polygon's area, and
determine the number of treasures (interior points) using Pick's theorem.

Functions:
- find_path(treasure_map): Calculates the path in coordinates based on the treasure map.
- find_positive_path(path): Shifts the path so that all coordinates are non-negative.
- find_size(path): Finds the size of the map (height and width) based on the given path.
- view_map(path): Creates a string representation of the map using the path.
- find_vertices(treasure_map): Finds the vertices of the polygon formed by path in the treasure map.
- calculate_polygon_area(vertices): Calculates the area of the polygon using its vertices.
- find_volume_treasure(area, length): Finds the number of interior points using Pick's theorem.

Usage:
The module operates on a series of movements given as a list of tuples, where each tuple contains a
direction ('U', 'D', 'L', 'R') and the number of steps to move in direction. Use these functions
to analyze the path, map out territory, and calculate properties of polygon formed by movements.
"""

from operator import itemgetter


def find_path(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    """
    Finds the path in coordinates according to treasure_map assuming that the start is (0, 0).
    - 'U' moves up (negative x), 'D' moves down (positive x), 'L' moves left (negative y),
      'R' moves right (positive y).

    :param treasure_map: A list of movements (direction, steps).
    :return: A list of coordinates representing the path.

    >>> find_path([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
    ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    [(0, 0), (-1, 0), (-2, 0), (-2, 1), (-2, 2), \
(-1, 2), (0, 2), (0, 3), (0, 4), (-1, 4), (-2, 4), \
(-3, 4), (-4, 4), (-4, 3), (-4, 2), (-4, 1), (-4, 0), \
(-4, -1), (-4, -2), (-4, -3), (-4, -4), (-4, -5), \
(-4, -6), (-4, -7), (-3, -7), (-2, -7), (-1, -7), \
(0, -7), (1, -7), (2, -7), (3, -7), (3, -6), (3, -5), \
(3, -4), (3, -3), (3, -2), (3, -1), (3, 0), (2, 0), (1, 0), (0, 0)]
    """
    output = [(0, 0)]
    for direction, steps in treasure_map:
        length = len(output) - 1
        for j in range(length, steps + length):
            if direction == "U":
                output.append((output[j][0] - 1, output[j][1]))
            elif direction == "D":
                output.append((output[j][0] + 1, output[j][1]))
            elif direction == "R":
                output.append((output[j][0], output[j][1] + 1))
            elif direction == "L":
                output.append((output[j][0], output[j][1] - 1))
    return output if output[0] == output[-1] else None


def find_positive_path(path: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Shift the path to ensure all coordinates are non-negative.

    :param path: List of coordinates.
    :return: A list of coordinates with all non-negative values.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
    ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> find_positive_path(path)
    [(4, 7), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (4, 10), (4, 11), (3, 11), (2, 11), \
(1, 11), (0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), \
(0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), \
(7, 4), (7, 5), (7, 6), (7, 7), (6, 7), (5, 7), (4, 7)]
    """
    min_x = min(path, key=itemgetter(0))
    min_y = min(path, key=itemgetter(1))
    output = [(x - min_x[0], y - min_y[1]) for x, y in path]
    return output if output[0] == output[-1] else None


def find_size(path: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Find the size of the map based on the path.

    :param path: List of coordinates.
    :return: Tuple containing height and width of the map.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
    ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_size(find_positive_path(find_path(treasure_map)))
    (8, 12)
    """
    max_x = max(path, key=itemgetter(0))
    max_y = max(path, key=itemgetter(1))
    return max_x[0] + 1, max_y[1] + 1


def view_map(path: list[tuple[int, int]]) -> str:
    """
    Create a string representation of the map. Use 'x' for points on the path and '.' otherwise.

    :param path: List of coordinates.
    :return: String representation of the map.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
    ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> view_map(path)
    'xxxxxxxxxxxx\\n\
x..........x\\n\
x......xxx.x\\n\
x......x.x.x\\n\
x......x.xxx\\n\
x......x....\\n\
x......x....\\n\
xxxxxxxx....'
    """
    output = ""
    path = find_positive_path(path)
    size = find_size(path)
    for i in range(size[0]):
        for j in range(size[1]):
            output += "x" if (i, j) in path else "."
        output += "\n" if i != size[0] - 1 else ""
    return output if output != "" else None


def find_vertices(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    """
    Find the vertices of the polygon formed by the path in the treasure map.

    :param treasure_map: List of movements (direction, steps).
    :return: List of vertices of the polygon.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
    ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_vertices(treasure_map)
    [(-2, 0), (-2, 2), (0, 2), (0, 4), (-4, 4), (-4, -7), (3, -7), (3, 0)]
    """
    x, y = 0, 0
    vertices = [(x, y)]
    i = 0
    while i < len(treasure_map):
        direction, steps = treasure_map[i]
        total_steps = steps

        while i + 1 < len(treasure_map) and treasure_map[i + 1][0] == direction:
            total_steps += treasure_map[i + 1][1]
            i += 1

        if direction == 'U':
            x -= total_steps
        elif direction == 'D':
            x += total_steps
        elif direction == 'L':
            y -= total_steps
        elif direction == 'R':
            y += total_steps

        vertices.append((x, y))
        i += 1

    return vertices[1:-1] if treasure_map[0][0] == treasure_map[-1][0] else vertices[0:-1]


def calculate_polygon_area(vertices: list[tuple[int, int]]) -> int:
    """
    Calculate the polygon area using the list of vertices.

    :param vertices: List of vertices.
    :return: Area of the polygon.

    >>> vertices = find_vertices([('U', 2), ('R', 2), ('D', 2), \
    ('R', 2), ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    >>> calculate_polygon_area(vertices)
    61
    """
    area = 0
    i = 0
    while i < len(vertices):
        area += vertices[i][0] * vertices[i+1][1] - vertices[i+1][0] * vertices[i][1] \
            if i != len(vertices) - 1 \
            else vertices[i][0] * vertices[0][1] - vertices[0][0] * vertices[i][1]
        i += 1
    return int(abs(area) / 2)


def find_volume_treasure(area: int, length: int) -> int:
    """
    Find the number of interior points (treasures) using Pick's theorem.

    :param area: Area of the polygon.
    :param length: Perimeter (number of points on the path).
    :return: Number of interior points (treasures).

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
    ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> vertices = find_vertices(treasure_map)
    >>> area = calculate_polygon_area(vertices)
    >>> length = len(find_path(treasure_map))-1
    >>> find_volume_treasure(area, length)
    42
    """
    return area + 1 - length // 2


def read_file(pathname):
    """
    Read map from a file with pathname.
    Return list of tuples, where the first element
    is direction and the second is the number of steps.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('U 2\\nR 2\\nD 2\\nL 2')
    >>> with open(tmpfile.name, 'r', encoding='utf-8') as file:
    ...    print(file.read())
    U 2
    R 2
    D 2
    L 2
    >>> read_file(tmpfile.name)
    [('U', 2), ('R', 2), ('D', 2), ('L', 2)]
    >>> read_file("treasure.txt")
    [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    """
    with open(pathname, "r", encoding="utf-8") as file:
        coordinates = [((x := line.strip().split())[0], int(x[1])) for line in file]
    return coordinates


def write_map_to_file(mapa, pathname):
    '''
    Write the mapa to the file with path pathname.
    Returns nothing.

    >>> mapa = 'xxx\\nx.x\\nxxx'
    >>> import tempfile
    >>> mapa = output
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', delete=False) as tmpfile:
    ...    write_map_to_file(mapa, tmpfile.name)
    ...    print(tmpfile.read())
    xxx
    x.x
    xxx
    '''
    with open(pathname, "w", encoding="utf-8") as file:
        file.write(mapa)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
