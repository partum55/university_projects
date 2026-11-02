#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from logging import DEBUG, debug, getLogger

# Configure debug logging
getLogger().setLevel(DEBUG)


def parse_field_info():
    """Parse board dimensions."""
    line = input()
    _, height, width = line.split()
    return int(height), int(width)


def parse_field(height):
    """Parse the current game board."""
    field = []
    for _ in range(height):
        line = input()
        field.append(line)
    return field


def parse_piece():
    """Parse the current piece and its dimensions."""
    line = input()
    _, piece_height, piece_width = line.split()
    piece_height, piece_width = int(piece_height), int(piece_width)

    piece = []
    for _ in range(piece_height):
        line = input()
        piece.append(line)

    return piece, piece_height, piece_width


def is_valid_placement(board, piece, piece_height, piece_width, x, y, bot_char):
    """Check if the piece can be placed at (x, y) on the board."""
    overlap = 0
    for i in range(piece_height):
        for j in range(piece_width):
            board_x, board_y = x + i, y + j

            # Check bounds
            if board_x < 0 or board_y < 0 or board_x >= len(board) or board_y >= len(board[0]):
                if piece[i][j] == '*':
                    return False
                continue

            # Check overlap
            if piece[i][j] == '*':
                if board[board_x][board_y] == bot_char:
                    overlap += 1
                elif board[board_x][board_y] != '.':
                    return False

    return overlap == 1  # Must overlap exactly one cell


def calculate_score(board, piece, piece_height, piece_width, x, y, bot_char):
    """Calculate a heuristic score for placing the piece at (x, y)."""
    score = 0
    for i in range(piece_height):
        for j in range(piece_width):
            board_x, board_y = x + i, y + j

            if piece[i][j] == '*' and 0 <= board_x < len(board) and 0 <= board_y < len(board[0]):
                if board[board_x][board_y] == '.':
                    score += 1  # Favor gaining new cells
    return score


def find_best_move(board, piece, piece_height, piece_width, bot_char):
    """Find the optimal placement for the piece."""
    best_score = -1
    best_move = None

    for x in range(-piece_height + 1, len(board)):
        for y in range(-piece_width + 1, len(board[0])):
            if is_valid_placement(board, piece, piece_height, piece_width, x, y, bot_char):
                score = calculate_score(board, piece, piece_height, piece_width, x, y, bot_char)
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move


def play():
    """Main game loop."""
    # Parse player info
    line = input()
    bot_char = 'O' if "p1 :" in line else 'X'

    while True:
        try:
            # Parse the board and piece
            board_height, board_width = parse_field_info()
            board = parse_field(board_height)
            piece, piece_height, piece_width = parse_piece()

            # Find and output the best move
            move = find_best_move(board, piece, piece_height, piece_width, bot_char)
            if move:
                print(f"{move[0]} {move[1]}")
            else:
                # Output sentinel value if no valid move exists
                print("0 0")
        except EOFError:
            break


if __name__ == "__main__":
    play()
