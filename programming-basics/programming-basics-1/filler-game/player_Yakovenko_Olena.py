#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)

def is_valid_position(field, figure, h_fig, w_fig, x, y, player_char):
    """
    Checks if placing the figure at a specific position (x, y) is valid.

    A valid position must:
    1. Have exactly one overlap between the figure and the player's territory.
    2. Ensure all other figure cells fall on empty ('.') cells.
    3. Stay within the bounds of the field.

    :param field: The current game field as a 2D list of characters.
    :param figure: The figure to place, represented as a list of strings.
    :param h_fig: Height of the figure.
    :param w_fig: Width of the figure.
    :param x: The x-coordinate (row) to place the figure.
    :param y: The y-coordinate (column) to place the figure.
    :param player_char: The player's character ('o' or 'x').
    :return: True if the position is valid, False otherwise.
    """
    overlap = 0
    for row in range(h_fig):
        for col in range(w_fig):
            if figure[row][col] == '*':
                new_x, new_y = x + row, y + col
                if new_x < 0 or new_y < 0 or new_x >= len(field) or new_y >= len(field[0]):
                    return False
                if field[new_x][new_y].lower() == player_char:
                    overlap += 1
                    if overlap > 1:
                        return False
                elif field[new_x][new_y] != '.':
                    return False
    return overlap == 1

def generate_moves(field, h_field, w_field, figure, h_fig, w_fig, player_char):
    """
    Generates all valid moves where the figure can be placed.

    It iterates over all positions on the field and checks if placing the figure 
    at each position is valid using the `is_valid_position` function.

    :param field: The current game field as a 2D list of characters.
    :param h_field: Height of the field.
    :param w_field: Width of the field.
    :param figure: The figure to place, represented as a list of strings.
    :param h_fig: Height of the figure.
    :param w_fig: Width of the figure.
    :param player_char: The player's character ('o' or 'x').
    :return: A list of tuples representing all valid moves (x, y).
    """
    moves = []
    for x in range(h_field):
        for y in range(w_field):
            if is_valid_position(field, figure, h_fig, w_fig, x, y, player_char):
                moves.append((x, y))
    return moves

def choose_move_encircle_opponent(field, h_field, w_field, figure, h_fig, w_fig, player_char):
    """
    Selects the best move to encircle the opponent's cells.

    The move is chosen to minimize the distance to the opponent's nearest cell, 
    effectively "closing in" on the opponent's positions.

    :param field: The current game field as a 2D list of characters.
    :param h_field: Height of the field.
    :param w_field: Width of the field.
    :param figure: The figure to place, represented as a list of strings.
    :param h_fig: Height of the figure.
    :param w_fig: Width of the figure.
    :param player_char: The player's character ('o' or 'x').
    :return: A tuple (x, y) representing the best move, or None if no moves are valid.
    """
    opponent_char = 'x' if player_char == 'o' else 'o'
    moves = generate_moves(field, h_field, w_field, figure, h_fig, w_fig, player_char)
    
    if not moves:
        return None

    def distance_to_opponent(x, y):
        """
        Calculates the Manhattan distance from a position (x, y) 
        to the nearest opponent's cell.

        :param x: The x-coordinate (row).
        :param y: The y-coordinate (column).
        :return: The minimum Manhattan distance to any opponent cell.
        """
        return min(
            abs(x + row - i) + abs(y + col - j)
            for row in range(h_fig)
            for col in range(w_fig)
            if figure[row][col] == '*'
            for i in range(h_field)
            for j in range(w_field)
            if field[i][j].lower() == opponent_char
        )
    best_move = min(moves, key=lambda move: distance_to_opponent(*move))
    return best_move



def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    _, height, width = l.split()
    return int(height), int(width[:-1])


def parse_field(height: int):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

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

    :param player int: Represents whether we're the first or second player
    """
    _ = input()
    field = []
    for _ in range(height):
        l = input().strip()
        field.append(l[4:])
    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input().split()
    figure = []
    height, width = int(l[1]), int(l[2][:-1])
    for _ in range(height):
        l = input()
        figure.append(l)
    return height, width, figure


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    h_field, w_field = parse_field_info()
    field = parse_field(h_field)
    h_fig, w_fig, figure = parse_figure()

    player_char = 'o' if player == 1 else 'x'

    # move = choose_move(field, h_field, w_field, figure, h_fig, w_fig, player_char)
    move = choose_move_encircle_opponent(field, h_field, w_field, figure, h_fig, w_fig, player_char)

    if move:
        return move
    return None


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")
    except TypeError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
