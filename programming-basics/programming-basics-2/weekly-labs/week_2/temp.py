"""target game in OOP"""

import random

class Word:
    """check if the word valid"""
    def __init__(self, word):
        self.word = word.strip().lower()

    def is_valid(self, board):
        """checks if the word valid
        >>> board = Board([['E', 'S', 'Z'], ['Y', 'C', 'I'], ['D', 'P', 'Y']])
        >>> Word('spicy').is_valid(board)
        True
        >>> Word('float').is_valid(board)
        False
        """
        lst = [letter.lower() for row in board.grid for letter in row]
        return len(self.word) >= 4 and\
            all(letter in lst for letter in self.word) and\
            all(self.word.count(letter) <= lst.count(letter) for letter in self.word)\
            and board.grid[1][1].lower() in self.word

    def __eq__(self, other):
        return isinstance(other, Word) and self.word == other.word

    def __repr__(self):
        return self.word


class Board:
    """shows game board"""
    def __init__(self, grid=None):
        self.grid = grid if grid else self.generate_grid()

    @staticmethod
    def generate_grid():
        """_summary_
        """
        vowels = "AIOUE"
        cons = "BCDFGHJKLMNPQRSTVWXYZ"
        letters = random.sample(vowels, 3) + random.sample(cons, 6)
        random.shuffle(letters)
        grid = []
        lst = []
        for i in letters:
            lst.append(i)
            if len(lst) == 3:
                grid.append(lst)
                lst = []
        return grid

    def get_words(self, filename):
        """reads file with word dictionsry"""
        with open(filename, "r", encoding='utf-8') as file:
            dictionary = [line.strip() for line in file]
        return [Word(word) for word in dictionary if Word(word).is_valid(self)]

    def __str__(self) -> str:
        return "Your board is:\n" + "\n".join("".join(row) for row in self.grid)

class TargetGame:
    """the main game class"""
    def __init__(self, filename, grid=None, user_words=None):
        self.board = Board(grid)
        if not grid:
            print(self.board)
        self.__possible_words = self.board.get_words(filename)
        self.__user_words = self.get_user_words(user_words)

    @property
    def user_words(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return [Word(w) for w in self.__user_words]

    @user_words.setter
    def user_words(self, words):
        """_summary_

        Args:
            words (_type_): _description_
        """
        self.__user_words = words

    @property
    def correct_user_words(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return [word for word in self.user_words if word.is_valid(self.board)]

    def get_user_words(self, words):
        """_summary_

        Args:
            words (_type_): _description_

        Returns:
            _type_: _description_
        """
        if words:
            return [w.strip() for w in words]
        print("Please, suggest your words.")
        print("When you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return")
        res = []
        try:
            while a := input().strip():
                res.append(a)
        except EOFError:
            pass
        return res

    def __str__(self):
        return f"""---------Game results---------:
The list of your words is:
{self.user_words}
The list of your correct words:
{self.correct_user_words}
The number of possible words: {len(self.__possible_words)}
You guess {round(len(self.correct_user_words) /
len(self.__possible_words) * 100)}% of possible words."""


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
