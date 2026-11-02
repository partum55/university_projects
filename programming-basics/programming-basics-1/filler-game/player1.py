#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import DEBUG, debug, getLogger
from typing import List, Tuple

getLogger().setLevel(DEBUG)


# --- Parsing Functions ---

def parse_field_info() -> Tuple[int, int]:
    """
    Parse the info about the field and return its height and width.
    """
    height, width = (int(i) for i in input().strip(":").split()[1:])
    return height, width


def parse_field(height: int) -> List[str]:
    """
    Parse the field based on the given height.
    """
    _ = input()  # Skip the line containing field description
    field = [input()[4:] for _ in range(height)]
    return field


def parse_figure() -> List[str]:
    """
    Parse the figure and return its matrix representation.
    """
    height, width = [int(i) for i in input().strip(':').split()[1:]]
    figure = [input() for _ in range(height)]
    return figure


# --- Game Logic ---

def generate_heatmap(field: List[str], player_cell: str, opponent_cell: str) -> Tuple[
    List[List[int]], List[Tuple[int, int]]]:
    """
    Generates a heatmap for move evaluation and identifies opponent positions.
    """
    height, width = len(field), len(field[0])
    heatmap = [[0] * width for _ in range(height)]
    opponent_positions = []

    for i in range(height):
        for j in range(width):
            if field[i][j] == opponent_cell:
                opponent_positions.append((i, j))
                # Increase heatmap values around the opponent
                for dr in range(-2, 3):  # Larger range for better strategic depth
                    for dc in range(-2, 3):
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < height and 0 <= nc < width:
                            heatmap[nr][nc] += max(2 - abs(dr) - abs(dc), 0)  # Weighted proximity scoring
    return heatmap, opponent_positions


def evaluate_move(field: List[str], figure: List[str], move: Tuple[int, int], heatmap: List[List[int]],
                  player_cell: str) -> int:
    """
    Evaluates a move based on the heatmap and strategic scoring.
    """
    x, y = move
    score = heatmap[x][y]

    # Additional scoring for future blocking and zone control
    for k in range(-1, 2):
        for s in range(-1, 2):
            nr, nc = x + k, y + s
            if 0 <= nr < len(field) and 0 <= nc < len(field[0]) and field[nr][nc] == '.':
                score += 1  # Encourages moves near open spaces
    return score


def predict_opponent_moves(opponent_positions: List[Tuple[int, int]], heatmap: List[List[int]]) -> List[
    Tuple[int, int]]:
    """
    Predicts the most likely opponent moves based on proximity to player positions.
    """
    predicted_moves = []
    for x, y in opponent_positions:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(heatmap) and 0 <= ny < len(heatmap[0]):
                    predicted_moves.append((nx, ny))
    return predicted_moves


def find_valid_moves(field: List[str], figure: List[str], player_cell: str) -> List[Tuple[int, int]]:
    """
    Finds all valid moves for the given figure on the field.
    """
    rows, cols = len(field), len(field[0])
    fig_rows, fig_cols = len(figure), len(figure[0])
    valid_moves = []

    for i in range(rows - fig_rows + 1):
        for j in range(cols - fig_cols + 1):
            match = 0
            bad_match = 0
            for k in range(fig_rows):
                for s in range(fig_cols):
                    if figure[k][s] == '*':
                        field_row, field_col = i + k, j + s
                        cell = field[field_row][field_col].lower()
                        if cell == player_cell:
                            match += 1
                        elif cell != '.':
                            bad_match += 1
            if match == 1 and bad_match == 0:
                valid_moves.append((i, j))
    return valid_moves


def determine_mode(player_positions: List[Tuple[int, int]], opponent_positions: List[Tuple[int, int]]) -> str:
    """
    Determines the bot's mode based on player and opponent positions.
    """
    if any(abs(px - ox) <= 1 and abs(py - oy) <= 1 for px, py in player_positions for ox, oy in opponent_positions):
        return "defense"
    elif len(opponent_positions) < 3:
        return "attack"
    return "standard"


# --- Main Game Loop ---

def step(player: int) -> Tuple[int, int]:
    """
    Executes a single step in the game.
    """
    height, _ = parse_field_info()
    field = parse_field(height)
    figure = parse_figure()
    player_cell = 'o' if player == 1 else 'x'
    opponent_cell = 'x' if player_cell == 'o' else 'o'

    heatmap, opponent_positions = generate_heatmap(field, player_cell, opponent_cell)
    player_positions = find_positions(field, player_cell)

    mode = determine_mode(player_positions, opponent_positions)

    valid_moves = find_valid_moves(field, figure, player_cell)
    if mode == "attack":
        move = max(valid_moves, key=lambda m: evaluate_move(field, figure, m, heatmap, player_cell), default=())
    elif mode == "defense":
        move = min(valid_moves, key=lambda m: evaluate_move(field, figure, m, heatmap, player_cell), default=())
    else:
        move = max(valid_moves, key=lambda m: evaluate_move(field, figure, m, heatmap, player_cell), default=())

    return move


def parse_info_about_player() -> int:
    """
    Determines if the bot is player 1 or player 2.
    """
    return 1 if "p1 :" in input() else 2


def find_positions(field: List[str], cell: str) -> List[Tuple[int, int]]:
    """
    Finds all positions of the given cell type.
    """
    return [(i, j) for i, row in enumerate(field) for j, c in enumerate(row) if c == cell]


def main():
    """
    Main function to execute the bot logic.
    """
    player = parse_info_about_player()
    try:
        while True:
            move = step(player)
            if move:
                print(*move)
            else:
                break
    except EOFError:
        debug("Game ended - EOF received")


if __name__ == "__main__":
    main()
