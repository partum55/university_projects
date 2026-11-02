"""
Target Word Game

This module defines a word-based puzzle game where players attempt to form valid words using
letters from a randomly generated 3x3 board. Words must meet certain criteria to be valid.

Classes:
    Word: Represents a word and checks its validity.
    Board: Represents the game board, generates a random letter grid, and finds valid words.
    TargetGame: Manages the game, including user input and scoring.
"""

import random


class Word:
    """
    Represents a word and checks if it adheres to the game rules.
    """

    def __init__(self, word: str):
        self.word = word.strip().lower()

    def is_valid(self, board: "Board") -> bool:
        """
        Checks the validity of the word according to the game rules:
        - The word must have at least 4 letters.
        - The count of each letter in the word does not exceed its count on the board.
        - The word must include the central letter of the board.

        :param board: The game board containing letters.
        :return: True if the word is valid, False otherwise.
        """
        return (
                len(self.word) >= 4
                and board.grid[1][1].lower() in self.word
                and all(self.word.count(l) <= board.letters.count(l) for l in set(self.word))
        )

    def __repr__(self):
        return f"{self.word}"

    def __eq__(self, other):
        if isinstance(other, Word):
            return self.word == other.word
        if isinstance(other, str):
            return self.word == other
        return False


class Board:
    """
    Represents the game board, generates a letter grid, and finds valid words.
    """

    def __init__(self, grid=None):
        self.grid = grid if grid else self.generate_grid()
        self.letters = [i.lower() for row in self.grid for i in row]

    def __str__(self):
        return "Your board is:\n" + "\n".join("".join(row) for row in self.grid)

    @staticmethod
    def generate_grid():
        """
        Generates a random 3x3 grid with exactly 3 vowels and 6 consonants.

        :return: A 3x3 list (grid) where each row is a list of letters.
        """
        letters = random.choices("AIOUE", k=3) + random.choices("BCDFGHJKLMNPQRSTVWXYZ", k=6)
        random.shuffle(letters)
        return [letters[i: i + 3] for i in range(0, 9, 3)]

    def get_words(self, filename: str):
        """
        Temp
        """
        with open(filename, encoding="utf-8") as f:
            words = []
            for w in f:
                w = Word(w.strip().lower())
                if w.is_valid(self) and w not in words:
                    words.append(w)
            return words


class TargetGame:
    """
    Manages the game, including board generation, user input, and scoring.
    """

    def __init__(self, filename:str, board=None, user_words=None):
        self.board = Board(board)
        self.__possible_words = self.board.get_words(filename)
        if not board:
            print(self.board)
        self.__user_words = []
        self.__user_words = self.get_user_words(user_words)

    def get_user_words(self, user_words=None):
        """
        Temp
        """
        if user_words:
            return [w.strip().lower() for w in user_words]
        print("Please, suggest your words.")
        print("When you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return")
        words = []
        try:
            while w := input().lower().strip():
                if w not in words and w not in self.__user_words:
                    words.append(w)
        except (EOFError, KeyboardInterrupt):
            pass
        return words

    @property
    def user_words(self):
        """
        Temp
        """
        return [Word(w) for w in self.__user_words]

    @user_words.setter
    def user_words(self, words):
        self.__user_words = [w.strip().lower() for w in words]

    @property
    def correct_user_words(self):
        """
        Temp
        """
        return [w for w in self.user_words if w in self.__possible_words]

    def __str__(self):
        total = len(self.__possible_words)
        percent = round((len(self.correct_user_words) / total) * 100) if total else 0

        return (
            "---------Game results---------:\n"
            "The list of your words is:\n"
            f"{self.user_words}\n"
            "The list of your correct words:\n"
            f"{self.correct_user_words}\n"
            f"The number of possible words: {total}\n"
            f"You guess {percent}% of possible words."
        )


game = TargetGame("en.txt")
print(game)
