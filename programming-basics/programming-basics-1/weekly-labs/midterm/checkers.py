"""Midterm. Chechers"""


def read_checkerboard(path: str) -> list:
    """
    Reads a checkerboard configuration from a file and
    returns a list of lists representing the checkers on the board.

    The file at the given path should contain lines
    with comma-separated values representing
    the positions and states of checkers on the board.
    Each line corresponds to one square on
    the board, with the following format:
        column_label, row_number, square_color, checker_info

    Parameters:
    -----------
    path : str
        The file path to read the checkerboard configuration from.

    Returns:
    --------
    list[list[str]]:
        A list of lists where each inner list contains four elements:
        [column_label, row_number, square_color, checker_info]

    Example:
    --------
    >>> read_checkerboard('board.txt')
    [['a', '1', 'B', 'W'], ['b', '1', 'W', 'False'], ['c', '1', 'B', 'False'],\
 ['a', '2', 'W', 'False'], ['b', '2', 'B', 'B'], ['c', '2', 'W', 'W'],\
 ['a', '3', 'B', 'False'], ['b', '3', 'W', 'False'], ['c', '3', 'B', 'False']]
    """
    with open(path, "r", encoding="utf-8") as file:
        file = file.read().strip().split(",")
        return file


def decode_checkerboard(content: str) -> list:
    """
    Decodes the checkerboard information into a 2D list
    representing the board with checkers.

    Parameters:
    -----------
    content : list[list[str]]
        The checkerboard information as read from the file, where
        each inner list contains:
        [column_label, row_number, square_color, checker_info]

    Returns:
    --------
    list[list[tuple[str, str]]]:
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), where 'square_color' is 'b' or 'w',
        and 'checker' is 'w', 'b', or '' (empty string) for no checker.

    Example:
    --------
    >>> board = [['a', '1', 'B', 'W'], ['b', '1', 'W', 'False'], ['c', '1', 'B', 'False'],\
 ['a', '2', 'W', 'False'], ['b', '2', 'B', 'B'], ['c', '2', 'W', 'W'],\
 ['a', '3', 'B', 'False'], ['b', '3', 'W', 'False'], ['c', '3', 'B', 'False']]
    >>> decode_checkerboard(board)
    [[('b', 'w'), ('w', ''), ('b', '')], \
[('w', ''), ('b', 'b'), ('w', 'w')], \
[('b', ''), ('w', ''), ('b', '')]]
    """
    k = 0
    output = []
    temp = []
    for _, elem in enumerate(content):
        if elem[3] != "False":
            temp.append((elem[2].lower(), elem[3].lower()))
        else:
            temp.append((elem[2].lower(), ""))
        k += 1
        if k == 3:
            output.append(temp)
            temp = []
            k = 0
    return output


def remove_wrong_checkers(board: list, inplace=True) -> list | None:
    """
    Removes checkers that are placed on white squares,
    which is not allowed in the game of checkers.

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), with 'square_color' as 'b' or 'w',
        and 'checker' as 'w', 'b', or ''.

    inplace : bool, optional
        If True, modifies the input board in place and returns None.
        If False, returns a new board with the wrong checkers removed,
            leaving the input board unchanged.

    Returns:
    --------
    None or list[list[tuple[str, str]]]:
        If inplace is True, returns None after modifying the board in place.
        If inplace is False, returns a new board with checkers
            removed from white squares.
        If there were no wrong checkers to remove, returns None.

    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board)
    >>> board
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board) is None
    True
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board, inplace=False)
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> board
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    """
    if inplace:
        output = []
        for _, row in enumerate(board):
            temp = []
            for _, elem in enumerate(row):
                if elem[0] == "w" and (elem[1] == "w" or elem [1] == "b"):
                    temp.append((elem[0], ""))
                else:
                    temp.append(elem)
            output.append(temp)
        return output if not inplace else None
    for i, row in enumerate(board):
        temp = []
        for _, elem in enumerate(row):
            if elem[0] == "w" and (elem[1] == "w" or elem [1] == "b"):
                temp.append((elem[0], ""))
            else:
                temp.append(elem)
        output[i] = temp
    return output if not inplace else None


def get_possible_captures_for_checker(board: list, position: tuple) -> list:
    """
    Checks all possible capture moves for a single checker at a given position.

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        The game board.
    position : tuple[int, int]
        The (row_index, column_index) of the checker.

    Returns:
    --------
    list[tuple[tuple[int, int]]]:
        A list of possible capture moves for the checker at the given position.
        Each move is represented as:
        - ((start_row, start_col), (end_row, end_col)), (captured_row, captured_col))
        The list should be sorted by the (end_row, end_col) move. For example,
        if possible end moves are (5, 5), (1, 1), (1, 5), (5, 1) than the order should be
        corresponding to the following order:
        (1, 1), (1, 5), (5, 1), (5, 5)


    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> get_possible_captures_for_checker(board, (0, 0))
    [((0, 0), (2, 2), (1, 1))]
    >>> get_possible_captures_for_checker(board, (1, 1))
    []
    >>> get_possible_captures_for_checker(board, (0, 1))
    []
    >>> board = [[('b', ''), ('w', ''), ('b', ''), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', ''), ('b', ''), ('w', '')],\
 [('b', ''), ('w', ''), ('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', ''), ('w', ''), ('b', 'b'), ('w', '')],\
 [('w', ''), ('b', ''), ('w', ''), ('b', ''), ('w', '')]]
    >>> get_possible_captures_for_checker(board, (2, 2))
    [((2, 2), (0, 0), (1, 1)), ((2, 2), (4, 4), (3, 3))]
    """
    for i, row in enumerate(board):
        for j, _  in enumerate(row):
            if i == position[0] and j == position[1]:
                ...


def write_board_to_file(board: list, pathname: str) -> None:
    """
    Writes the board to a file in a human-readable format.

    The board is represented as lines of squares, where each square
    is represented as:
    - |_| for a black empty square
    - | | for a white empty square
    - |w| or |b| for a square with a white or black checker

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), with 'square_color' as 'b' or 'w',
        and 'checker' as 'w', 'b', or ''.

    pathname : str
        The file path to write the board to.

    Returns:
    --------
    None

    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')], \
[('w', ''), ('b', 'b'), ('w', 'w')], \
[('b', ''), ('w', ''), ('b', '')]]
    >>> write_board_to_file(board, 'result.txt')
    >>> with open('result.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    |w| |_|
    | |b|w|
    |_| |_|
    >>> board = [[('b', ''), ('w', ''), ('b', '')],\
 [('w', ''), ('b', ''), ('w', '')],\
 [('b', ''), ('w', ''), ('b', 'w')]]
    >>> write_board_to_file(board, 'result.txt')
    >>> with open('result.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    |_| |_|
    | |_| |
    |_| |w|
    """
    with open(pathname, "w", encoding="utf-8") as file:
        board = board[::-1][::-1]
        for i, row in enumerate(board):
            temp = "|"
            for _, elem in enumerate(row):
                if elem[0] == "b" and elem[1] == "":
                    temp += "_|"
                elif elem[0] == "w" and elem[1] == "":
                    temp += " |"
                elif elem[0] == "w" and elem[1] == "b":
                    temp += "b|"
                elif elem[0] == "w" and elem[1] == "w":
                    temp += "w|"
                elif elem[0] == "b" and elem[1] == "b":
                    temp += "b|"
                elif elem[0] == "b" and elem[1] == "w":
                    temp += "w|"
            if len(board) - 1 == i:
                file.write(temp)
            else:
                file.write(temp+ "\n")
    return None


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
