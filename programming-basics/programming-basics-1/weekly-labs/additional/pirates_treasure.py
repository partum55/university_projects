"""
Pirate's Treasure Map Decoder

This module provides a set of functions to read, process, and visualize pirate maps
to help locate the treasure. Each pirate has a starting location, moves in a biased
direction based on a given azimuth, and takes a series of steps to reach their destination.

The module functions allow you to:
- Interpret the pirate's movement based on azimuth and initial direction.
- Parse the map files to determine starting coordinates and movement directions.
- Generate a complete path for each pirate, calculating intermediate coordinates.
- Locate the treasure by finding the intersection point(s) of both pirates' paths.
- Draw a map representation of the paths and the treasure.

The visualized map includes:
- The pirates' paths, marked with `.` symbols.
- Start locations: '1' for the first path, '2' for the second path,
    or '3' if both paths share a starting point.
- Treasure location marked with 'x' if it exists.

Usage:
Run the module as a standalone script to perform doctests, or use individual
functions for custom map processing and visualization.

Functions:
- define_direction: Determines new movement direction based on the current direction and azimuth.
- read_map: Reads a file to extract the starting position and a list of movement steps.
- find_path: Calculates the full path of a pirate based on a series of directional steps.
- find_treasure: Identifies the treasure's location based on the intersection of two paths.
- find_size: Calculates the minimum map dimensions to encompass a path.
- shift_path: Adjusts path coordinates to start at (0, 0).
- decode_map: Draws the paths and treasure on a map and writes it to an output file.
"""


def define_direction(previous_direction, azimuth):
    """
    Calculate the new path direction based on the current direction
    and the pirate's biased azimuth. The azimuth is given in degrees
    and can be any non-negative multiple of 90. The directions are
    represented as 'N' for North, 'E' for East, 'S' for South, and 'W'
    for West.

    Args:
    previous_direction (str): The current direction ('N', 'E', 'S', 'W').
    azimuth (int): The azimuth in degrees (non-negative multiple of 90).

    Returns:
    str: The new direction as a single character string.

    For example:
    - If the current direction is North ('N') and the azimuth is 90 degrees,
      the new direction will be East ('E').
    - If the current direction is South ('S') and the azimuth is 90 degrees,
      the new direction will be West ('W').

    >>> define_direction('N', 0)
    'N'
    >>> define_direction('N', 90)
    'E'
    >>> define_direction('N', 180)
    'S'
    >>> define_direction('N', 270)
    'W'
    >>> define_direction('E', 90)
    'S'
    >>> define_direction('W', 270)
    'S'
    """
    angle = 0
    match previous_direction:
        case "N": angle += azimuth
        case "S": angle = 180 + azimuth
        case "W": angle = 270 + azimuth
        case "E": angle = 90 + azimuth
    match angle:
        case 0 | 360: return "N"
        case 90 | 450: return "E"
        case 180 | 540: return "S"
        case 270 | 630: return "W"


def read_map(file_name):
    """
    Reads a map from the specified file and interprets the directions
    and steps for navigation. The map file contains information about
    the starting coordinates and the steps to be taken in a specified
    direction. The initial direction is assumed to be North.

    The map file should be structured in such a way that it lists the
    starting coordinates (x, y) followed by directions (N, E, S, W)
    and the corresponding number of steps to take in each direction.

    Note: The file may contain empty lines, which should be ignored.

    Args:
    file_name (str): The pathname of the file containing the map data.

    Returns:
    tuple: A tuple containing two elements:
        - The first element is a tuple (x, y) representing the starting
          coordinates.
        - The second element is a list of tuples, where each tuple contains:
            - A direction (str): 'N' for North, 'E' for East, 'S' for South,
              or 'W' for West.
            - The number of steps (int) to take in that direction.

    >>> read_map("treasure_3.txt")
    ((0, 11), \
[('W', 5), ('W', 6), ('S', 7), ('E', 3), ('E', 4), \
('N', 5), ('E', 2), ('S', 2), ('E', 2), ('N', 4)])
    """
    with open(file_name, "r", encoding="utf-8") as file:
        output = []
        previous_direction = "N"
        start = file.readline().strip().split()
        start_coords = (int(start[0]), int(start[1]))
        for line in file:
            line = line.strip().split()
            if not line:
                continue
            azimuth = int(line[0])
            steps = int(line[1])
            direction = define_direction(previous_direction, azimuth)
            output.append((direction, steps))
            previous_direction = direction
        return start_coords, output


def find_path(start, treasure_directions):
    """
    Calculates the path of coordinates based on the given start position
    and a series of directional steps. The start position is provided as
    a tuple of coordinates (x, y).

    The function interprets movement based on the following directional
    rules, with steps determining how far to move in a given direction:
    - 'W' (West): decreases the y-coordinate (moves left).
    - 'E' (East): increases the y-coordinate (moves right).
    - 'N' (North): decreases the x-coordinate (moves up).
    - 'S' (South): increases the x-coordinate (moves down).

    Args:
    start (tuple): A tuple representing the starting coordinates (x, y).
    treasure_directions (list of tuple): A list of tuples where each tuple
                                         contains:
                                         - A direction ('N', 'E', 'W', 'S')
                                         - An integer representing the number
                                           of steps to take in that direction.

    Returns:
    list of tuple: A list of coordinates (x, y) representing the path taken 
                   from the start position, including all intermediate steps.

    >>> start = (0, 0)
    >>> path = [('E', 3), ('S', 3), ('W', 3), ('N', 3)]
    >>> find_path(start, path)
    [(0, 0), \
(0, 1), (0, 2), (0, 3), \
(1, 3), (2, 3), (3, 3), \
(3, 2), (3, 1), (3, 0), \
(2, 0), (1, 0), (0, 0)\
]
    """
    path = [start]
    for direction, steps in treasure_directions:
        for _ in range(steps):
            x, y = path[-1]
            match direction:
                case "N":
                    path.append((x - 1, y))
                case "S":
                    path.append((x + 1, y))
                case "E":
                    path.append((x, y + 1))
                case "W":
                    path.append((x, y - 1))
    return path


def find_treasure(path1, path2):
    """
    Determines the location of the treasure based on the intersection of
    two paths. The function identifies the point of intersection and
    calculates the treasure's location based on the following conditions:

    - If the paths intersect at exactly one point, that point is the
      treasure's location.
    - If the paths intersect at exactly two points, the treasure is located
      at the midpoint between these two points. If the coordinates of the
      midpoint are fractional, they are rounded down to the nearest integer.
    - If the paths intersect at more than two points, it is impossible
      to determine the treasure's exact location, and the function
      returns `None`.

    Args:
    path1 (list of tuple): The first path, represented as
                           a list of coordinates (x, y).
    path2 (list of tuple): The second path, represented as
                           a list of coordinates (x, y).

    Returns:
    tuple or None: The coordinates (x, y) of the treasure if it
    can be determined, or `None`  if the treasure's location
    cannot be identified.

    >>> path1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    >>> path2 = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> path3 = [(1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)]
    >>> find_treasure(path1, path2)
    (2, 2)
    >>> find_treasure(path1, path3)
    (1, 2)
    >>> find_treasure(path2, path3)
    """
    intersections = [point for point in path1 if point in path2]
    if len(intersections) == 1:
        return intersections[0]
    if len(intersections) == 2:
        x1, y1 = intersections[0]
        x2, y2 = intersections[1]
        return (x1 + x2) // 2, (y1 + y2) // 2
    return None


def find_size(path):
    """
    Calculates the size of the map based on the given path. The size of the map
    is determined by the minimal number of points needed vertically and
    horizontally to encompass the entire path. The height is the difference
    between the maximum and minimum x-coordinates, and the width is the
    difference between the maximum and minimum y-coordinates.

    Args:
    path (list of tuple): A list of coordinates (x, y) representing the path.

    Returns:
    tuple: A tuple (height, width) where:
        - height is the number of points needed vertically.
        - width is the number of points needed horizontally.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> find_size(path)
    (3, 3)
    """
    x_values = [point[0] for point in path]
    y_values = [point[1] for point in path]
    height = max(x_values) + 1 - min(x_values)
    width = max(y_values) + 1 - min(y_values)
    return height, width


def shift_path(path):
    """
    Shifts the given path to ensure that all coordinates are non-negative
    and the smallest coordinate is positioned at (0, 0).

    The function returns a tuple, where the first element is a tuple
    containing the minimum y and x values before the shift, and the second
    element is the list of shifted coordinates.

    Args:
    path (list of tuple): A list of tuples where each tuple represents a
                          coordinate (x, y) along the path.

    Returns:
    tuple: A tuple where:
        - The first element is a tuple representing the minimum
          y-coordinate and x-coordinate found in the path.
        - The second element is a list of tuples representing the shifted path,
          where all coordinates are non-negative.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> shift_path(path)
    ((2, 2), [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    """
    min_x = min(point[0] for point in path)
    min_y = min(point[1] for point in path)
    shifted_path = [(x - min_x, y - min_y) for x, y in path]
    return (min_x, min_y), shifted_path


def decode_map(file_name1, file_name2, map_file_name):
    """
    Draws a map that visualizes two paths and the treasure (if it exists)
    based on the paths provided in two input files. The map is written
    to the specified output file.

    - The paths are marked with `.`.
    - The start of the first path is marked with `1`.
    - The start of the second path is marked with `2`.
    - If the start of the first and second path coincides, it is
      marked with `3`.
    - If the treasure is found (i.e., the paths intersect at a specific point),
      it is marked with `x`. The treasure marker `x` overwrites the start
      markers '1' and '2' if they coincide with the treasure's location.

    Args:
    file_name1 (str): The name of the file containing the first path.
    file_name2 (str): The name of the file containing the second path.
    map_file_name (str): The name of the output file where the map will be drawn.

    Returns:
    None: The map is written directly to the output file.

    >>> decode_map('treasure_1.txt', 'treasure_2.txt', 'output.txt')
    >>> with open('output.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    1..
    . .
    ..x.2
      . .
      ...
    """
    start1, directions1 = read_map(file_name1)
    start2, directions2 = read_map(file_name2)
    map1 = find_path(start1, directions1)
    map2 = find_path(start2, directions2)
    full_map = map1 + map2
    shiffed, full_map = shift_path(full_map)
    map_size = find_size(full_map)
    map_visual = [[" " for _ in range(map_size[1])] for _ in range(map_size[0])]
    for point in full_map:
        map_visual[point[0]][point[1]] = "."
    treasure_coordinates = find_treasure(map1, map2)
    if start1 == start2:
        map_visual[start1[0] - shiffed[0]][start1[1] - shiffed[1]] = "3"
    else:
        map_visual[start1[0] - shiffed[0]][start1[1] - shiffed[1]] = "1"
        map_visual[start2[0] - shiffed[0]][start2[1] - shiffed[1]] = "2"
    if treasure_coordinates:
        map_visual[treasure_coordinates[0] - shiffed[0]][treasure_coordinates[1] - shiffed[1]] = "x"
    final_map = []
    for line in map_visual:
        final_map.append(''.join(line))
    with open(map_file_name, "w", encoding='utf-8') as out_file:
        for i, line in enumerate(final_map):
            out_file.write(line)
            if i != len(final_map) - 1:
                out_file.write('\n')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
