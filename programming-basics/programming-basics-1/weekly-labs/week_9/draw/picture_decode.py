def read_file(file_path: str) -> dict:
    """
    Reads a file and constructs a dictionary mapping symbols to a list of coordinates.

    Each symbol is found on an odd-numbered line, followed by a line of coordinates in
    the format "x_y x_y ...", representing where the symbol should be placed.

    :param file_path: Path to the input file.
    :return: Dictionary mapping each symbol to a list of coordinates.

    Example:
    >>> with open("test_file.txt", "w") as f:
    ...     _ = f.write("X\\n0_1 1_2\\nY\\n1_1\\n")
    >>> read_file("test_file.txt")
    {'X': [(0, 1), (1, 2)], 'Y': [(1, 1)]}
    """
    with open(file_path, "r", encoding="utf-8") as file:
        picture = {}
        symbol = ""
        for i, line in enumerate(file):
            if (i+1) % 2 == 0:
                picture[symbol] = [(int(elem.split("_")[0]), int(elem.split("_")[1])) \
                                   for elem in line.strip().split()]
            else:
                symbol = line.strip("\n")
        return picture


def save_pict_to_file(symbols: dict[str, tuple[int, int]], textfile: str):
    """
    Saves a text-based graphical representation of symbols to a file.

    :param symbols: Dictionary where each key is a symbol and each value is a list of
                    (x, y) coordinates indicating where the symbol should be placed.
    :param textfile: Path to the output text file.

    :return: 2D matrix representing the graphical layout.

    Example:
    >>> symbols = {'X': [(0, 1), (1, 2)], 'Y': [(1, 1)]}
    >>> matrix = save_pict_to_file(symbols, "output_file.txt")
    >>> matrix
    [[' ', 'X', ' '], [' ', 'Y', 'X']]
    >>> with open("output_file.txt") as f:
    ...     f.readlines()
    [' X \\n', ' YX\\n']
    """
    width = max([coord[0] for coords in symbols.values() for coord in coords]) + 1
    height = max([coord[1] for coords in symbols.values() for coord in coords]) + 1
    matrix = [[" " for _ in range(height)] for _ in range(width)]
    for key, value in symbols.items():
        for coord in value:
            matrix[coord[0]][coord[1]] = key

    with open(textfile, "w", encoding="utf-8") as file:
        for line in matrix:
            line = "".join(line) + "\n"
            file.write(line)
    return matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
