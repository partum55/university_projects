"""
Wordle-style Game Module

This module implements a simple Wordle-style word guessing game in which the player
can select between two languages, English and Ukrainian. The player will be asked to
guess a word of a specified length, with each attempt providing feedback on letter
positions via color-coded markers:

    - Green: Correct letter in the correct position.
    - Yellow: Correct letter but in the wrong position.
    - Gray: Incorrect letter.

The game continues until the player guesses the word correctly or exhausts their
available attempts. The player can also quit the game at any time by typing '_q_'.

Main Functions:
---------------
1. `print_ascii_art()`:
    - Returns ASCII art for the game's header.

2. `print_rules()`:
    - Prints the rules of the game, explaining how guesses are color-coded.

3. `get_words(url_path: str, length: int) -> list[str]`:
    - Retrieves a list of words of the specified length from an online resource.

4. `random_word(wordlist: list[str]) -> str`:
    - Chooses a random word from the given list of words.

5. `check_user_word(user_word: str, word: str, length: int) -> tuple[str, bool]`:
    - Compares the user's guessed word with the target word, marking each letter
      as green, yellow, or gray as appropriate.

6. `en()`:
    - Initiates the game in English, guiding the player through the process and
      validating inputs.

7. `ua()`:
    - Initiates the game in Ukrainian, guiding the player through the process
      and validating inputs.

8. `main()`:
    - The entry point for the game. Prompts the player to select a language
      and begins the corresponding game mode.

Usage:
------
To play the game, simply run the module and follow the prompts by calling the `main()` function.
The player will be asked to select a language ('en' for English, 'ua' for Ukrainian) and specify
the word length they would like to guess. Each guess provides feedback until the player
guesses the word correctly or the game ends.

Example:
--------
$ python wordle_game.py

Choose language | Виберіть мову:
'en' | 'ua'

After selecting a language, the player will specify the word length and start guessing.

Dependencies:
-------------
- `random` for random word selection.
- `time` for sleep functionality to enhance the user experience.
- `urllib` to fetch words from online resources.

"""


import random as r
import time as t
import urllib.request
from pathlib import Path


GREEN = "\033[92m{}\033[00m"
YELLOW = "\033[93m{}\033[00m"
GRAY = "\033[90m{}\033[00m"
# Word lists (nouns.csv, nouns_ua.csv) are not stored in git, see DATASETS.md.
# Put them into programming-basics/other/dictionary-english-game/.
_WORDS_DIR = Path(__file__).resolve().parents[3] / "other" / "dictionary-english-game"
LINK_EN = (_WORDS_DIR / "nouns.csv").as_uri()
LINK_UA = (_WORDS_DIR / "nouns_ua.csv").as_uri()


def print_ascii_art() -> str:
    """
    Prints the game's ASCII art.

    :return: ASCII art for the game header.
    :rtype: str
    """
    art = YELLOW.format("""
    ░█──░█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▄ ░█─── ░█▀▀▀
    ░█░█░█ ░█──░█ ░█▄▄▀ ░█─░█ ░█─── ░█▀▀▀
    ░█▄▀▄█ ░█▄▄▄█ ░█─░█ ░█▄▄▀ ░█▄▄█ ░█▄▄▄
    """)
    return art


def print_rules() -> None:
    """
    Prints the rules of the game.
    """
    print(f"""
    Welcome to the Wordle-style Game! Here are the rules:
    - Guess the target word in 6 attempts or fewer.
    - Each letter in your guess will be color-coded:
        - {GREEN.format("Green")}: Correct letter in the correct position.
        - {YELLOW.format("Yellow")}: Correct letter in the wrong position.
        - {GRAY.format("Gray")}: Incorrect letter.
    - Enter '_q_' to quit the game anytime.
    """)


def get_words(url_path: str, length: int) -> list[str]:
    """
    Reads words from a URL and returns a list of words with a specific length.

    :param url_path: The URL containing the list of words.
    :type url_path: str
    :param length: The required length of the words to filter.
    :type length: int
    :return: A list of words matching the given length.
    :rtype: list[str]
    """
    with urllib.request.urlopen(url_path) as response:
        content = response.read().decode("utf-8")
        words = content.splitlines()
        wordlist = [word.strip() for word in words if len(word.strip()) == length]
    return wordlist


def random_word(wordlist: list[str]) -> str:
    """
    Selects a random word from a list of words.

    :param wordlist: A list of words to choose from.
    :type wordlist: list[str]
    :return: A randomly selected word.
    :rtype: str
    """
    return r.choice(wordlist)


def check_user_word(user_word: str, word: str, length: int) -> tuple[str, bool]:
    """
    Compares the user's word with the target word and marks each letter as green (correct position),
    yellow (correct letter, wrong position), or gray (incorrect letter).

    :param user_word: The word entered by the user.
    :type user_word: str
    :param word: The target word to compare against.
    :type word: str
    :param length: The length of the word being checked.
    :type length: int
    :return: A tuple containing the formatted result and a boolean indicator of validity.
    :rtype: tuple[str, bool]
    """
    if len(user_word) != length:
        return "Wrong word length, please try again", False
    if not user_word.isalpha():
        return "Invalid format, please enter only letters", False

    word_letter_count = {letter: word.count(letter) for letter in set(word)}
    used_letters = {letter: 0 for letter in set(word)}
    result = [""] * length
    user_word_list = list(user_word)
    for i in range(length):
        if user_word[i] == word[i]:
            result[i] = GREEN.format(user_word[i])
            used_letters[user_word[i]] += 1
            user_word_list[i] = None
    for i in range(length):
        if user_word_list[i] is not None:
            if user_word_list[i] in word and used_letters[user_word_list[i]] < \
                    word_letter_count[user_word_list[i]]:
                result[i] = YELLOW.format(user_word_list[i])
                used_letters[user_word_list[i]] += 1
            else:
                result[i] = GRAY.format(user_word_list[i])
    output_word = "".join(result)
    return output_word, True


def en() -> None:
    """
    Starts the game in English, asking the player for word length and guiding through guesses.

    :return: None
    """
    print(print_ascii_art())
    t.sleep(2)
    print_rules()
    t.sleep(2)
    print("Enter the word length (from 4 to 11)")
    try:
        while True:
            try:
                n = input(">>> ")
                if n == "_q_":
                    print("Have a nice day!")
                    return None
                n = int(n)
                if 4 <= n <= 11:
                    break
                print("Please enter a number between 4 and 11.")
            except ValueError:
                print("Please enter a valid number.")
    except (KeyboardInterrupt, EOFError):
        print("Have a good day!")
        return None
    wordlist = get_words(LINK_EN, n)
    word = random_word(wordlist)
    print("Enter your guess:")
    print("To quit, type '_q_'")
    attempts = 6
    while attempts > 0:
        try:
            user_word = input(">>> ").lower().strip()
            if user_word == "_q_":
                print("Are you sure? Enter 'YES' to quit or 'NO' to continue.")
                user_word = input(">>> ")
                if user_word.upper() == "YES":
                    print(f"The word was: {word}")
                    break
                continue
            if user_word == word:
                print("Congratulations! You guessed the word!")
                break
            if user_word in wordlist:
                checked = check_user_word(user_word, word, n)
                attempts = attempts - 1 if checked[1] else attempts
                print(f"{checked[0]} | attempts left: {attempts}")
            else:
                print(f"Invalid word. Try again | attempts left: {attempts}")
        except (EOFError, KeyboardInterrupt):
            print(f"Have a good day! The word was: {word}")
            return None
    else:
        print(f"Game over. The word was: {word}")
        return None


def ua() -> None:
    """
    Starts the game in Ukrainian, asking the player for word length and guiding through guesses.

    :return: None
    """
    t.sleep(1)
    print(print_ascii_art())
    print_rules()
    t.sleep(1)
    print("Введіть довжину слова (від 4 до 11)")
    t.sleep(1)
    try:
        while True:
            try:
                n = input(">>> ")
                if n == "_q_":
                    print("Гарного дня!")
                    return None
                n = int(n)
                if 4 <= n <= 11:
                    break
                print("Будь ласка, введіть число від 4 до 11.")
            except ValueError:
                print("Будь ласка, введіть правильне число.")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Гарного вам дня!")
        return None
    wordlist = get_words(LINK_UA, n)
    word = random_word(wordlist)
    print("Введіть ваше слово:")
    print("Для виходу введіть '_q_'")
    attempts = 6
    while attempts > 0:
        try:
            user_word = input(">>> ").lower().strip()
            if user_word == "_q_":
                print("Ви впевнені? Введіть 'YES' щоб вийти або 'NO' щоб продовжити.")
                user_word = input(">>> ")
                if user_word.upper() == "YES":
                    print(f"Загадане слово було: {word}")
                    break
                continue
            if user_word == word:
                print("Вітаємо! Ви вгадали слово!")
                break
            if user_word in wordlist:
                checked = check_user_word(user_word, word, n)
                attempts = attempts - 1 if checked[1] else attempts
                print(f"{checked[0]} | спроб залишилось: {attempts}")
            else:
                print(f"Неправильне слово. Спробуйте знову | спроб залишилось: {attempts}")
        except (EOFError, KeyboardInterrupt):
            print(f"Гарного вам дня! Загадане слово: {word}")
            return None
    else:
        print(f"Гра закінчена. Загадане слово було: {word}")
        return None


def main() -> None:
    """
    Main function to choose language and start the corresponding game mode.

    :return: None
    """
    print("Choose language | Виберіть мову:")
    print("'en' | 'ua'")
    language = ""
    while language != "ua" or language != "en":
        try:
            language = input(">>> ").lower().strip()
        except (KeyboardInterrupt, EOFError):
            print("You don`t even try to play game( | А ти так і не спробував пограти в гру(")
            return None
        if language == "_q_":
            print("You don`t even try to play game( | А ти так і не спробував пограти в гру(")
            return None
        if language == "ua":
            ua()
            return None
        if language == "en":
            en()
            return None
        print("Будь ласка, введіть коректну мову.")


if __name__ == "__main__":
    main()
