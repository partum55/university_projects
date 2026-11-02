#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This is an example of a bot for the 3rd project.
"""

from logging import DEBUG, debug, getLogger
getLogger().setLevel(DEBUG)

def parse_field_info():
    """
    Parses the field dimensions from the input.
    """
    height, width = (int(i) for i in input().strip(":").split()[1:])
    # debug(f"Description of the field: {height}, {width}")
    return height, width

def parse_field(height):
    """
    Parses the current state of the game field.
    """
    _ = input()
    field = [input()[4:] for _ in range(height)]
    return field

def parse_figure():
    """
    Parses the figure dimensions and structure.
    """
    height = int(input().strip(':').split()[1])
    figure = []
    for _ in range(height):
        line = input()
        figure.append(line)
    debug(f"Figure: {figure}")
    return figure

def parse_info_about_player():
    """
    Parses the player's identity from the input.
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2

def can_place(field, figure, row, col, player_char):
    """
    Determines if the figure can be placed at the specified position.
    """
    overlap = 0
    for i, fig_row in enumerate(figure):
        for j, cell in enumerate(fig_row):
            if cell == '*':
                field_row = row + i
                field_col = col + j
                if not (0 <= field_row < len(field)) or not (0 <= field_col < len(field[0])):
                    return False
                if field[field_row][field_col] == player_char:
                    overlap += 1
                elif field[field_row][field_col] != '.':
                    return False
    return overlap == 1

def calculate_placement_score(field, figure, row, col):
    """
    Calculates a heuristic score for a potential placement.
    """
    score = 0
    for i, fig_row in enumerate(figure):
        for j, cell in enumerate(fig_row):
            if cell == '*':
                field_row = row + i
                field_col = col + j
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = field_row + dr, field_col + dc
                    if 0 <= nr < len(field) and 0 <= nc < len(field[0]):
                        if field[nr][nc] == '.':
                            score += 1
                        elif field[nr][nc].lower() != '.':
                            score -= 1
    return score

def find_best_move(field, figure, player):
    """
    Finds the best move for the current step.
    """
    player_char = 'o' if player == 1 else 'x'
    height, width = len(field), len(field[0])
    fig_height, fig_width = len(figure), len(figure[0])

    best_score = float('-inf')
    best_move = None

    for row in range(height - fig_height + 1):
        for col in range(width - fig_width + 1):
            if can_place(field, figure, row, col, player_char):
                score = calculate_placement_score(field, figure, row, col)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def step(player):
    """
    Executes a single step in the game.
    """
    height, _ = parse_field_info()
    field = parse_field(height)
    figure = parse_figure()
    player_id = parse_info_about_player()

    if player_id == player:
        best_move = find_best_move(field, figure, player)
        return best_move
    return None


def main():
    """
    Main function to execute the bot logic.
    """
    player = parse_info_about_player()

    try:
        while True:
            height, _ = parse_field_info()
            field = parse_field(height)
            figure = parse_figure()
            move = find_best_move(field, figure, player)
            if move:
                debug(f"{move}")
                print(*move)
            else:
                debug("End game")
                break
    except EOFError:
        debug("Cannot get input.")

if __name__ == "__main__":
    main()
