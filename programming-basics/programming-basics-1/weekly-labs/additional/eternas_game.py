"""Temp"""


import random as r


def winning_combination(board: list[list]) -> tuple[bool, list[list]]:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there is winning combination or False if not.

    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], \
['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], \
[0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], \
[0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], \
[0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], \
[0, 'w', 'w', 'w'], ['g', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], \
['g', 'g', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1)], \
[(3, 15), (3, 0), (3, 1), (3, 2)]])

    """
    winning_combinations = []
    for i in board:
        if i[0] != 0 and i.count(i[0]) == 4:
            winning_combinations.append(i)

    for i in range(12):
        for j in range(4):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != 0:
                winning_combinations.append([(j ,i), (j, i+1), (j, i+2), (j, i+3)])
    for j in range(4):
        if board[-2][j] == board[-1][j] == board[0][j] == board[1][j] != 0:
            winning_combinations.append([(j, 14), (j, 15), (j, 0), (j, 1)])
        if board[-3][j] == board[-2][j] == board[-1][j] == board[0][j] != 0:
            winning_combinations.append([(j, 13), (j, 14), (j, 15), (j, 0)])
        if board[0][j] == board[1][j] == board[2][j] == board[-1][j] != 0:
            winning_combinations.append([(j, 15), (j, 0), (j, 1), (j, 2)])

    for i in range(12):
        if board[i][0] == board[i+1][1] == board[i+2][2] == board[i+3][3] != 0:
            winning_combinations.append([(0, i), (1, i+1), (2, i+2), (3, i+3)])
        if board[i][3] == board[i + 1][2] == board[i + 2][1] == board[i + 3][0] != 0:
            winning_combinations.append([(3, i), (2, i+1), (1, i+2), (0, i+3)])

    if board[-2][0] == board[-1][1] == board[0][2] == board[1][3] != 0:
        winning_combinations.append([(14, 0), (15, 1), (10, 2), (1, 3)])
    if board[-3][0] == board[-2][1] == board[-1][2] == board[0][3] != 0:
        winning_combinations.append([(13, 0), (14, 1), (15, 2), (0, 3)])
    if board[0][0] == board[1][2] == board[2][3] == board[-1][4] != 0:
        winning_combinations.append([(15, 0), (0, 1), (1, 2), (2, 3)])

    if board[-2][3] == board[-1][2] == board[0][1] == board[1][0] != 0:
        winning_combinations.append([(14, 3), (15, 2), (10, 1), (1, 0)])
    if board[-3][3] == board[-2][2] == board[-1][1] == board[0][0] != 0:
        winning_combinations.append([(13, 0), (14, 1), (15, 2), (0, 3)])
    if board[0][3] == board[1][2] == board[2][1] == board[-1][0] != 0:
        winning_combinations.append([(15, 0), (0, 1), (1, 2), (2, 3)])

    if winning_combinations:
        return True, winning_combinations
    return False


def board_generation() -> list[list]:
    """
    Generates a game board of 16 x 4 size, i.e. two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    board = [[] for _ in range(16)]
    green_count = 0
    white_count = 0
    total_moves = 0
    while total_moves < 64:  # Maximum moves
        position = r.randint(0, 15)
        if len(board[position]) < 4:
            if green_count < 16 and (green_count <= white_count or white_count >= 16):
                board[position].append('g')
                green_count += 1
            elif white_count < 16 and (white_count <= green_count or green_count >= 16):
                board[position].append('w')
                white_count += 1
            else:
                board[position].append(0)
            total_moves += 1
    return board
