#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)

def parse_field_info():
    height, width = (int(i) for i in input().strip(":").split()[1:])
    return height, width

def parse_field(height):
    _ = input()
    field = [input()[4:] for _ in range(height)]
    return field

def parse_figure():
    height = int(input().strip(':').split()[1])
    figure = [list(input()) for _ in range(height)]

    while figure and all(cell == '.' for cell in figure[-1]):
        figure.pop()

    if figure:
        while all(row[-1] == '.' for row in figure):
            for row in figure:
                row.pop()
    return figure

def parse_info_about_player():
    i = input()
    player = 1 if "p1 :" in i else 2
    debug(f"Player Info: Player {player}")
    return player

def can_place(field, figure, row, col, player_char):
    overlap = 0
    for i, fig_row in enumerate(figure):
        for j, cell in enumerate(fig_row):
            if cell == '*':
                field_row = row + i
                field_col = col + j
                if not (0 <= field_row < len(field)) or not (0 <= field_col < len(field[0])):
                    return False
                if field[field_row][field_col].lower() == player_char:
                    overlap += 1
                elif field[field_row][field_col] != '.':
                    return False
    return overlap == 1

def calculate_placement_score(field, figure, row, col):
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
    height, _ = parse_field_info()
    field = parse_field(height)
    figure = parse_figure()
    best_move = find_best_move(field, figure, player)
    return best_move

def main():
    player = parse_info_about_player()

    try:
        while True:
            move = step(player)
            if move:
                debug(f"player{player} = {move}")
                print(*move)
            else:
                debug("No valid move found, ending game.")
                break
    except EOFError:
        debug("Cannot get input - EOFError.")

if __name__ == "__main__":
    main()
