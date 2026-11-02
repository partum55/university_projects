"""Maze"""


def read_file(filename):
    """
    Reads and returns the content of a file.

    This function opens the specified file in read mode, reads its content,
    and returns it as a string. If the file does not exist or cannot be
    opened, the function may raise an exception related to file handling.

    Args:
        filename: str. The path to the file that needs to be read.

    Returns:
        str. The content of the file as a string.

    Raises:
        OSError: If the file cannot be accessed or read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [i.strip("\n") for i in file]


def find_paths(map, start_symbol, end_symbol):
    """
    Find all possible paths from a start symbol to an end symbol in a given map.

    This function traverses a 2D list representation of a map to find all
    possible paths connecting a starting point, identified by the start_symbol,
    to an ending point, identified by the end_symbol. Each path is represented
    as a sequence of coordinates indicating the positions in the map. The
    function assumes the map consists of valid symbols and may traverse in
    any direction as per the logic defined in the implementation.

    Parameters:
    map : list
        A 2D list representing the map where each element is a symbol.
    start_symbol : Any
        The symbol in the map that represents the starting point of the path.
    end_symbol : Any
        The symbol in the map that represents the ending point of the path.

    Returns:
    list
        A list of paths, where each path is represented as a list of coordinate
        tuples (row, column) in the map.

    Raises:
    ValueError
        If the start_symbol or end_symbol is not found in the map.
    TypeError
        If the map is not a list of lists or if the elements are not valid.
    """
    graph = {}
    teleports = {}
    start_pos = None
    end_pos = None
    rows = len(map)
    cols = len(map[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            cell = map[r][c]  # Fixed indentation
            pos = (r, c)
            if cell == '#':
                continue
            if cell == start_symbol:
                start_pos = pos
            elif cell == end_symbol:
                end_pos = pos
            graph[pos] = []
            if cell not in ['#', '.', ' ', start_symbol, end_symbol]:
                if cell not in teleports:
                    teleports[cell] = []
                teleports[cell].append(pos)
    if not start_pos or not end_pos:
        return [], []
    all_paths = []

    def dfs(current, path, visited):
        if current == end_pos:
            all_paths.append(path.copy())
            return
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                path.append(neighbor)
                dfs(neighbor, path, visited)
                path.pop()
        visited.remove(current)

    dfs(start_pos, [start_pos], set([start_pos]))
    return [len(i) for i in all_paths], all_paths


if __name__ == '__main__':
    map = read_file("plan1_cms.txt")
    print("\n".join(map))
    paths = find_paths(map, '?', '!')
    print(paths)
