"""Card game"""

from collections import deque

def play_cardgame(num_players, num_cards):
    """
    Simulates a card game and returns the winning score and winners.

    :param num_players: Number of players.
    :param num_cards: Total number of cards.
    :return: Tuple (winning_score, winners_set). Returns (0, set()) if no scoring occurs or if there are no players.
    """
    if num_players <= 0:
        return 0, set()
    scores = [0] * num_players
    circle = deque([0])
    for card in range(1, num_cards):
        current_player = (card - 1) % num_players
        if card % 23 == 0:
            scores[current_player] += card
            circle.rotate(7)
            scores[current_player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(card)
    max_score = max(scores) if scores else 0
    if max_score == 0:
        return 0, set()
    winners = {i + 1 for i, score in enumerate(scores) if score == max_score}
    return max_score, winners
