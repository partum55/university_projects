#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)


def parse_field_info() -> tuple[int, int]:
    """
    Parse field dimensions from input.

    :return: Tuple (height, width) where height is the number of rows
             and width is the number of columns.
    """
    height, width = (int(i) for i in input().strip(":").split()[1:])
    return height, width


def parse_field(height: int) -> list[list[str]]:
    """
    Parse the game field from input.

    :param height: Number of rows in the game field.
    :return: 2D list representing the field, with each cell as a string.
    """
    _ = input()
    return [list(input()[4:]) for _ in range(height)]


def parse_figure() -> list[list[str]]:
    """
    Parse the current figure from input.

    :return: 2D list representing the figure to place on the game field.
    """
    height= int(input().strip(':').split()[1])
    figure = [list(input()) for _ in range(height)]
    while figure and all(cell == '.' for cell in figure[-1]):
        figure.pop()
    while figure and all(row[-1] == '.' for row in figure):
        for row in figure:
            row.pop()
    return figure


def parse_info_about_player() -> int:
    """
    Determine whether the bot is player 1 or 2 based on input.

    :return: 1 if player 1, 2 if player 2.
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def calculate_encirclement_score(field: list[list[str]], pos: tuple[int, int], player_cell: str) -> float:
    """
    Calculate the encirclement score for a given position on the field.

    :param field: 2D list representing the game field.
    :param pos: Tuple (x, y) representing the position.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Encirclement score as a float.
    """
    rows, cols = len(field), len(field[0])
    x, y = pos
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    score = 0.0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    opponent_directions = set()
    friendly_directions = set()

    for idx, (dx, dy) in enumerate(directions):
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if field[nx][ny].lower() == opponent_cell:
                opponent_directions.add(idx)
            elif field[nx][ny].lower() == player_cell:
                friendly_directions.add(idx)

    if opponent_directions and friendly_directions:
        opposite_dirs = {0: 6, 1: 7, 2: 8, 3: 5, 5: 3, 6: 0, 7: 1, 8: 2}
        for opp_dir in opponent_directions:
            if opposite_dirs.get(opp_dir) in friendly_directions:
                score += 2.0

        direction_groups = [(0, 1, 2), (2, 4, 7), (5, 6, 7), (0, 3, 5)]
        for group in direction_groups:
            if any(d in opponent_directions for d in group) and any(d in friendly_directions for d in group):
                score += 1.0

    return score


def analyze_opponent_clusters(field: list[list[str]], player_cell: str) -> list[tuple[int, int]]:
    """
    Analyze clusters of opponent cells to identify strategic points.

    :param field: 2D list representing the game field.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: List of tuples representing strategic points.
    """
    rows, cols = len(field), len(field[0])
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    visited = set()
    clusters = []

    def find_cluster(x: int, y: int) -> set[tuple[int, int]]:
        cluster = set()
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in cluster:
                continue
            cluster.add((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                        field[nx][ny].lower() == opponent_cell and
                        (nx, ny) not in cluster):
                    stack.append((nx, ny))
        return cluster

    for i in range(rows):
        for j in range(cols):
            if field[i][j].lower() == opponent_cell and (i, j) not in visited:
                cluster = find_cluster(i, j)
                visited.update(cluster)
                clusters.append(cluster)

    strategic_points = []
    for cluster in clusters:
        perimeter = set()
        for x, y in cluster:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                        field[nx][ny] == '.' and
                        (nx, ny) not in perimeter):
                    perimeter.add((nx, ny))

        for point in perimeter:
            encirclement_score = calculate_encirclement_score(field, point, player_cell)
            if encirclement_score > 1.0:
                strategic_points.append(point)

    return strategic_points


def analyze_territory_control(field: list[list[str]], player_cell: str) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    """
    Analyze the opponent's territory and potential expansion points.

    :param field: 2D list representing the game field.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Tuple (opponent_territory, expansion_points) as sets of coordinates.
    """
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    rows, cols = len(field), len(field[0])
    opponent_territory = set()
    expansion_points = set()

    for i in range(rows):
        for j in range(cols):
            if field[i][j].lower() == opponent_cell:
                opponent_territory.add((i, j))

    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    for x, y in opponent_territory:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                    field[nx][ny] == '.' and
                    (nx, ny) not in expansion_points):
                expansion_points.add((nx, ny))

    return opponent_territory, expansion_points


def evaluate_blocking_potential(field: list[list[str]], move: tuple[int, int],
                                figure: list[list[str]], player_cell: str) -> float:
    """
    Evaluate the blocking effectiveness of a move.

    :param field: 2D list representing the game field.
    :param move: Tuple (x, y) representing the move coordinates.
    :param figure: 2D list representing the figure to place.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Blocking score as a float.
    """
    opponent_territory, expansion_points = analyze_territory_control(field, player_cell)
    blocking_score = 0
    move_x, move_y = move

    for i in range(len(figure)):
        for j in range(len(figure[0])):
            if figure[i][j] == '*':
                pos = (move_x + i, move_y + j)
                if pos in expansion_points:
                    blocking_score += 1
                if is_creating_wall(field, pos, player_cell):
                    blocking_score += 0.5

    return blocking_score


def is_creating_wall(field: list[list[str]], pos: tuple[int, int], player_cell: str) -> bool:
    """
    Check if a move creates a wall to block the opponent.

    :param field: 2D list of the game field.
    :param pos: Tuple (x, y) of the move coordinates.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: True if the move creates a wall, False otherwise.
    """
    rows, cols = len(field), len(field[0])
    x, y = pos
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    consecutive_friendly = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (0 <= nx < rows and 0 <= ny < cols and
                field[nx][ny].lower() == player_cell):
            consecutive_friendly += 1

    return consecutive_friendly >= 2


def calculate_heat_map(field: list[list[str]], player_cell: str) -> list[list[float]]:
    """
    Calculate a heat map of the field for scoring potential moves.

    :param field: 2D list representing the game field.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: 2D list of floats representing the heat map.
    """
    rows, cols = len(field), len(field[0])
    heat_map = [[0.0] * cols for _ in range(rows)]
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    center_row, center_col = rows // 2, cols // 2

    for i in range(rows):
        for j in range(cols):
            if field[i][j] == '.':
                center_dist = 1 - (((i - center_row) ** 2 + (j - center_col) ** 2) ** 0.5 /
                                   ((rows ** 2 + cols ** 2) ** 0.5))
                min_opponent_dist = float('inf')
                for ri in range(rows):
                    for rj in range(cols):
                        if field[ri][rj].lower() == opponent_cell:
                            dist = ((i - ri) ** 2 + (j - rj) ** 2) ** 0.5
                            min_opponent_dist = min(min_opponent_dist, dist)

                opponent_factor = 1 - (
                            min_opponent_dist / ((rows ** 2 + cols ** 2) ** 0.5)) if min_opponent_dist != float(
                    'inf') else 0
                heat_map[i][j] = 0.4 * center_dist + 0.6 * opponent_factor

                if has_capture_potential(field, (i, j), player_cell):
                    heat_map[i][j] += 0.3

    return heat_map


def has_capture_potential(field: list[list[str]], pos: tuple[int, int], player_cell: str) -> bool:
    """
    Check if a position has the potential to capture opponent cells.

    :param field: 2D list representing the game field.
    :param pos: Tuple (x, y) representing the position.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: True if the position has capture potential, False otherwise.
    """
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    rows, cols = len(field), len(field[0])
    x, y = pos
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)}
    opponent_count = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and field[nx][ny].lower() == opponent_cell:
            opponent_count += 1

    return opponent_count >= 2


def get_valid_moves(field: list[list[str]], figure: list[list[str]], player_cell: str) -> set[tuple[int, int]]:
    """
    Get all valid moves for the current figure.

    :param field: 2D list representing the game field.
    :param figure: 2D list representing the figure to place.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Set of tuples representing valid move coordinates.
    """
    rows, cols = len(field), len(field[0])
    fig_rows, fig_cols = len(figure), len(figure[0])
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    valid_moves = set()

    for i in range(rows - fig_rows + 1):
        for j in range(cols - fig_cols + 1):
            match = bad_match = 0
            for k in range(fig_rows):
                for s in range(fig_cols):
                    if figure[k][s] == '*':
                        cell = field[i + k][j + s].lower()
                        if cell == player_cell:
                            match += 1
                        elif cell == opponent_cell or cell != '.':
                            bad_match += 1
            if match == 1 and bad_match == 0:
                valid_moves.add((i, j))
    return valid_moves


def calculate_covered_opponent_territory(field: list[list[str]], figure: list[list[str]],
                                         move: tuple[int, int], player_cell: str) -> float:
    """
    Calculates the percentage of the opponent's territory covered by the placed figure.

    :param field: 2D list representing the current game field with 'o', 'x', or '.'.
    :param figure: 2D list representing the figure to be placed with '*' (occupied) and '.' (empty).
    :param move: Tuple (x, y) representing the placement position of the figure.
    :param player_cell: String ('o' or 'x') representing the player's character.

    :return: A float representing the percentage of the opponent's cells covered by the figure.
    """
    opponent_cell = 'x' if player_cell == 'o' else 'o'
    rows, cols = len(field), len(field[0])
    fig_rows, fig_cols = len(figure), len(figure[0])
    opponent_territory = {(i, j) for i in range(rows) for j in range(cols)
                          if field[i][j].lower() == opponent_cell}
    total_opponent_cells = len(opponent_territory)
    if total_opponent_cells == 0:
        return 0.0
    move_x, move_y = move
    covered_cells = 0
    for i in range(fig_rows):
        for j in range(fig_cols):
            if figure[i][j] == '*':
                x, y = move_x + i, move_y + j
                if (0 <= x < rows and 0 <= y < cols) and (x, y) in opponent_territory:
                    covered_cells += 1
    return covered_cells / total_opponent_cells


def evaluate_move(figure: list[list[str]], move: tuple[int, int],
                  heat_map: list[list[float]], field: list[list[str]],
                  player_cell: str) -> float:
    """
    Evaluate a move based on its coverage and encirclement potential.

    :param figure: 2D list representing the figure to place.
    :param move: Tuple (x, y) representing the move coordinates.
    :param heat_map: 2D list representing the heat map.
    :param field: 2D list representing the game field.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Move score as a float.
    """
    move_i, move_j = move
    rows, cols = len(heat_map), len(heat_map[0])
    coverage_score = 0.0
    encirclement_score = 0.0
    strategic_points = set(analyze_opponent_clusters(field, player_cell))
    for i in range(len(figure)):
        for j in range(len(figure[0])):
            if figure[i][j] == '*':
                x, y = move_i + i, move_j + j
                if 0 <= x < rows and 0 <= y < cols:
                    coverage_score += heat_map[x][y]
                    if (x, y) in strategic_points:
                        encirclement_score += 2.0
                    encirclement_score += calculate_encirclement_score(field, (x, y), player_cell)
    opponent_coverage_score = calculate_covered_opponent_territory(field, figure, move, player_cell) * 2.0
    game_progress = sum(row.count('o') + row.count('x') + row.count('O') + row.count('X')
                        for row in field) / (rows * cols)
    encirclement_weight = min(0.6, game_progress * 1.2)
    coverage_weight = 1 - encirclement_weight
    opponent_coverage_weight = 0.3
    return coverage_weight * coverage_score + \
        encirclement_weight * encirclement_score + \
        opponent_coverage_weight * opponent_coverage_score


def find_best_move(field: list[list[str]], figure: list[list[str]], player_cell: str) -> tuple:
    """
    Find the best move based on valid moves and their scores.

    :param field: 2D list representing the game field.
    :param figure: 2D list representing the figure to place.
    :param player_cell: Symbol of the current player ('o' or 'x').
    :return: Tuple (x, y) representing the best move.
    """
    heat_map = calculate_heat_map(field, player_cell)
    valid_moves = get_valid_moves(field, figure, player_cell)

    if not valid_moves:
        return ()

    move_scores = {}
    for move in valid_moves:
        score = evaluate_move(figure, move, heat_map, field, player_cell)
        move_scores[move] = score

    return max(move_scores.items(), key=lambda x: x[1])[0]


def main() -> None:
    """
    Main function to parse input, evaluate moves, and determine the bot's actions.

    :return: None
    """
    getLogger().setLevel(DEBUG)
    player = parse_info_about_player()

    try:
        while True:
            height, width = parse_field_info()
            field = parse_field(height)
            figure = parse_figure()
            player_cell = 'o' if player == 1 else 'x'

            move = find_best_move(field, figure, player_cell)
            if move:
                debug(f"player{player} = {move}")
                print(*move)
            else:
                break
    except EOFError:
        debug("Game ended - EOF received")


if __name__ == "__main__":
    main()
