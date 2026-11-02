#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filler Bot
"""
from logging import DEBUG, debug, getLogger
getLogger().setLevel(DEBUG)


def parse_field_info() -> tuple[int, int]:
    """
    Parse the info about the field.

    The function reads a line describing the size of the field and returns its height and width.

    Example input:
    Plateau 15 17:

    :return: tuple[int, int], A tuple containing the height and width of the field.
    """
    l = input().strip(':\n').split()[1:]
    height, width = int(l[0]), int(l[1])
    # debug(f"Size of the field: {height=}, {width=}")
    return height, width


def parse_field(height: int) -> list[str]:
    """
    Parse the field.

    This function reads the game field from input and returns it as a list of strings,
    where each string represents a row of the field.

    Example input:
        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param height: int, The number of rows in the field.
    :return: list[str], A list of strings, each representing a row of the field.
    """
    field = []
    _ = input()
    for _ in range(height):
        line = input().split()[-1]
        field.append(line)
        # debug(f"Field: {line}")
    return field


def parse_figure() -> list[str]:
    """
    Parse the figure.

    This function reads the piece's dimensions and shape from input and returns
    it as a list of strings, where each string represents a row of the piece.

    Example input:
        Piece 2 2:
        **
        ..

    :return: list[str], A list of strings, each representing a row of the figure.
    """
    height, width = [int(i) for i in input().strip(':').split()[1:]]
    # debug(f"Piece: {height=}, {width=}")

    figure = []
    for _ in range(height):
        line = input()
        # debug(f"Piece: {line}")
        figure.append(line)

    # debug(f"Figure: {figure}")

    while figure and all(cell == '.' for cell in figure[-1]):
        figure.pop()

    if figure:
        max_col = max((len(row.rstrip('.')) for row in figure), default=0)
        figure = [row[:max_col] for row in figure]

    # debug(f"Cropped Figure: {figure}")
    return figure


def get_possible_place_for_figure(field: list[str], figure: list[str],
                                  player_cell: str) -> list[tuple[int, int]]:
    """
    Finds all valid positions to place a figure on the field.

    A valid position:
    - Overlaps exactly one cell of the player's territory.
    - Does not overlap any part of the opponent's territory.
    - Fits entirely within the boundaries of the field.

    :param field: list[str], The game field represented as a list of strings.
    :param figure: list[str], The figure to be placed, represented as a list of strings.
    :param player_cell: str, The character representing the player's cells ('o' or 'x').

    :return: list[tuple[int, int]], A list of tuples, where each tuple contains the row and column
    coordinates of a valid top-left position for placing the figure.
    """
    opponent_cell = "x" if player_cell == "o" else "o"
    field_rows, field_cols = len(field), len(field[0])
    fig_rows, fig_cols = len(figure), len(figure[0])

    figure_positions = [(k, s) for k in range(fig_rows)
                        for s in range(fig_cols) if figure[k][s] == "*"]


    def is_valid_position(i: int, j: int) -> bool:
        """
        Checks if placing the figure at position (i, j) is valid.
        """
        match, bad_match = 0, 0
        for k, s in figure_positions:
            cell = field[i + k][j + s].lower()
            if cell == player_cell:
                match += 1
            elif cell == opponent_cell:
                return False
        return match == 1 and bad_match == 0


    all_variants = [(i, j) for i in range(field_rows - fig_rows + 1)
                    for j in range(field_cols - fig_cols + 1) if is_valid_position(i, j)]

    # debug(f"All variants: {all_variants}")
    return all_variants


def get_nearest_to_opponent(possible_moves: list[tuple[int, int]],
                            field: list[str], opponent_cell: str) -> tuple[int, int]:
    """
    Finds the move nearest to the opponent's cells.

    :param possible_moves: list[tuple[int, int]], List of tuples representing
    valid move coordinates.
    :param field: list[str], List of strings representing the game field.
    :param opponent_cell: str, Character ('o' or 'x') representing the opponent's cell.

    :return: tuple[int, int], A tuple with the coordinates of the nearest move, or
    (-1, -1) if no moves are available.
    """
    if not possible_moves:
        return (-1, -1)

    opponent_cells = [(i, j) for i, row in enumerate(field) for j, cell in enumerate(row)
                      if cell.lower() == opponent_cell.lower()]

    def min_dist_to_opponent(move):
        x, y = move
        return min(abs(x - ox) + abs(y - oy) for ox, oy in opponent_cells)

    return min(possible_moves, key=min_dist_to_opponent)


def get_nearest_to_center(possible_moves: list[tuple[int, int]],
                          center: tuple[int, int]) -> tuple[int, int]:
    """
    Finds the move nearest to the center of the field.

    The function takes a list of valid move coordinates and determines which one is
    closest to the specified center using the Manhattan distance.

    :param possible_moves: list[tuple[int, int]], A list of tuples representing valid
    move coordinates, where each tuple contains row and column indices.
    :param center: tuple[int, int], A tuple representing the coordinates (row, column)
    of the center of the field.

    :return: tuple[int, int], A tuple containing the coordinates of the move nearest to
    the center. Returns (-1, -1) if the list of possible moves is empty.
    """
    if not possible_moves:
        return (-1, -1)
    cx, cy = center

    def find_total_dist(possible_move):
        x, y = possible_move
        return abs(x - cx) + abs(y - cy)

    return min(possible_moves, key=find_total_dist)


def step(player: int) -> tuple[int, int]:
    """
    Perform one step of the game by calculating the next move for the given player.

    The function determines the player's cell ('o' or 'x'), retrieves the game field and figure,
    calculates the possible valid positions to place the figure, and then selects the best move
    based on the shortest distance to the opponent's cells.

    :param player: int, Represents whether the player is Player 1 (1) or Player 2 (2).

    :return: tuple[int, int], A tuple representing the row and column coordinates of the best
    move for the current player. Returns None if no valid move is available.
    """
    height, width = parse_field_info()

    center = (height // 2, width // 2)
    field = parse_field(height)
    figure = parse_figure()

    player_cell = "o" if player == 1 else "x"
    opponent_cell = "x" if player_cell == "o" else "o"
    possible_moves = get_possible_place_for_figure(field, figure, player_cell)

    if field[center[0]][center[1]].lower() not in [player_cell, opponent_cell]:
        # debug(f'Searching near center {center=}, {field[center[0]][center[1]]}')
        return get_nearest_to_center(possible_moves, center)

    # debug('Searching near opponent')
    return get_nearest_to_opponent(possible_moves, field, opponent_cell)


def parse_info_about_player() -> int:
    """
    Parse the info about the player

    Example input:
    $$$ exec p2 : [./player1.py]

    :return: int, 1 if Player 1 is identified, 2 if Player 2 is identified.
    """
    i = input()
    # debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main() -> None:
    """
    Main game loop that repeatedly prompts for the next move and outputs it.

    The function first determines which player is making the move, then enters an infinite loop
    where it repeatedly computes and outputs the next move for the player. If no input is received
    (EOFError), it will stop the game.

    It expects that the `step` function will determine the next move for the player based on the
    current state of the game.

    :return: None
    """
    player = parse_info_about_player()
    try:
        while True:
            move = step(player)
            # debug(f'Move: {move}')
            print(*move)
    except EOFError:
        debug(f"Player {player}: Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
