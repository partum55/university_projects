"""
Word Game Script

This script implements a word game where the user has to come up with words that:
1. Start and end with randomly generated letters from the Ukrainian alphabet.
2. Belong to a specified part of speech (noun, verb, adjective, adverb).
3. Contain no more than 5 letters.

The script generates a list of letters, picks a random part of speech, prompts user to input words,
and validates them against a vocabulary file. At the end, it shows the correctly guessed words and
any missed valid words.
"""


import random as r


def generate_grid() -> list[str]:
    """
    Generates a grid of 5 unique letters from the Ukrainian alphabet.

    :return: A list of 5 unique letters.
    :rtype: list[str]
    """
    alphabet = list("бвгґджзклмнпрстфхцчшщаеиіоуйєюяїь")
    return r.sample(alphabet, 5)


def get_language_part() -> str:
    """
    Randomly selects a language part.

    :return: A random language part.
    :rtype: str
    """
    language_parts = ["adjective", "adverb", "noun", "verb"]
    return r.choice(language_parts)


def get_user_words() -> list[str]:
    """
    Collects user words until an interruption (Ctrl+C or EOF).

    :return: A list of user-entered words.
    :rtype: list[str]
    """
    output = []
    try:
        while True:
            output.append(input())
    except (KeyboardInterrupt, EOFError):
        return output


def check_word(word: str, letters: list[str]) -> bool:
    """
    Checks if the user's word is valid based on certain criteria.

    :param word: The user's word.
    :type word: str
    :param letters: The letters that the word must start and end with.
    :type letters: list[str]
    :return: True if the word is valid, False otherwise.
    :rtype: bool


    >>> check_word("гараж", ["г", "а", "р", "ж", "б"])
    True
    """
    return word[0] in letters and word[-1] in letters and len(word) <= 5


def get_words(file_path: str, letters: list[str]) -> list[tuple[str, str]]:
    """
    Gets words from the file and categorizes them.

    :param file_path: Path to the file containing words.
    :type file_path: str
    :param letters: Letters that the words must start and end with.
    :type letters: list[str]
    :return: A list of tuples where each tuple contains a word and its category.
    :rtype: list[tuple[str, str]]


    >>> get_words("base.lst", ["щ", "ь", "ї", "ґ", "й"])
    [('ґалій', 'noun'), ('ґедзь', 'noun'), ('ґлей', 'noun'), ('ґудзь', 'noun'),\
 ('їдець', 'noun'), ('їдкий', 'adjective'), ('їнь', 'noun'), ('їхній', 'adjective'),\
 ('йодль', 'noun'), ('щирий', 'adjective'), ('щіть', 'noun'), ('щучий', 'adjective')]

    """
    with open(file_path, "r", encoding="utf-8") as file:
        output = []
        temp = []
        words = file.read().split("\n")
        for word in words:
            word_parts = word.lower().split(" ")
            if word_parts[0].startswith("+cs="):
                continue
            if word_parts[0] == "":
                continue
            if "/n" in word_parts[1][:4] or "noun" in word_parts[1][:4]:
                temp = word_parts[0], "noun"
            elif "/adj" in word_parts[1][:4] or "adj" in word_parts[1][:4]:
                temp = word_parts[0], "adjective"
            elif "/v" in word_parts[1][:4] or "verb" in word_parts[1][:4]:
                temp = word_parts[0], "verb"
            elif "/adv" in word_parts[1][:4] or "adv" in word_parts[1][:4]:
                temp = word_parts[0], "adverb"
            if check_word(temp[0], letters) and temp not in output:
                output.append(temp)
    return output


def check_user_words(user_words: list[str], language_part: str, letters: list[str], \
    vocablary: list[tuple[str, str]]) -> tuple[list[str], list[str]]:
    """
    Checks the user's words against the vocabulary.

    :param user_words: The user's words.
    :type user_words: list[str]
    :param language_part: The language part to check against.
    :type language_part: str
    :param letters: The letters that the words must start and end with.
    :type letters: list[str]
    :param vocablary: The vocabulary to check against.
    :type vocablary: list[tuple[str, str]]
    :return: Two lists - correctly proposed words and missed words.
    :rtype: tuple[list[str], list[str]]


    >>> check_user_words(["щука"], "noun", ["щ", "ь", "ї", "ґ", "й"], "base.lst")
    ([], ['ґалій', 'ґедзь', 'ґлей', 'ґудзь', 'їдець', 'їнь', 'йодль', 'щіть'])
    """
    vocablary = get_words(vocablary, letters)
    entered_words = []
    skipped_words = []
    for word in user_words:
        for w in vocablary:
            if word == w[0] and language_part == w[1]:
                entered_words.append(word)
                break
    for w in vocablary:
        if w[0] not in entered_words and check_word(w[0], letters) and language_part == w[1]:
            skipped_words.append(w[0])
    return entered_words, skipped_words


def main():
    """
    Main function to run the word game.
    """
    letters = generate_grid()
    language_part = get_language_part()
    print("Пограймо в гру!")
    print()
    print(f"Придумай якомога більше слів, що мають не більше 5 літер та починаються \
    і закінчуються на одну з наступних літер:\n {letters}")
    print(f"А ще ці слова мають бути наступною частиною мови:\n {language_part}")
    print("Твій список слів:")
    file_path = "base.lst"
    user_words = get_user_words()
    vocablary = get_words(file_path, letters)
    checked_words = check_user_words(user_words, language_part, letters, vocablary)
    print(f"Правильно запропоновані слова: {checked_words[0]}")
    print(f"Пропущені слова: {checked_words[1]}")


print(get_words("base.lst", ['л', 'є', 'я', 'і', 'ч']))
print([('єті', 'noun'), ('івасі', 'noun'), ('ідеал', 'noun'), ('ідея', 'noun'), ('ідол', 'noun'), ('іжиця', 'noun'), ('іксія', 'noun'), ("ім'я", 'noun'), ('індол', 'noun'), ('іноді', 'adverb'), ('іонол', 'noun'), ('ітися', 'verb'), ('лазня', 'noun'), ('ламач', 'noun'), ('ланч', 'noun'), ('ларі', 'noun'), ('латач', 'noun'), ('лаття', 'noun'), ("лев'я", 'noun'), ('ледач', 'noun'), ('леді', 'noun'), ('лелія', 'noun'), ('ленч', 'noun'), ('лея', 'noun'), ('лижня', 'noun'), ('листя', 'noun'), ('литія', 'noun'), ('лиття', 'noun'), ('лихач', 'noun'), ('ліві', 'noun'), ('лізол', 'noun'), ('лілея', 'noun'), ('лілія', 'noun'), ('лінія', 'noun'), ('літія', 'noun'), ('ліція', 'noun'), ('лічі', 'noun'), ('лобі', 'noun'), ('ловля', 'noun'), ('лорі', 'noun'), ('лоція', 'noun'), ("луб'я", 'noun'), ('льє', 'noun'), ('льоля', 'noun'), ('людці', 'noun'), ('лютня', 'noun'), ('люшня', 'noun'), ('ля', 'noun'), ('ляля', 'noun'), ('чаєня', 'noun'), ('чапля', 'noun'), ('чвал', 'noun'), ('чвиря', 'noun'), ('чері', 'noun'), ('чилі', 'noun'), ('чиря', 'noun'), ('читач', 'noun'), ('чортя', 'noun'), ('чохол', 'noun'), ('чувал', 'noun'), ('чуня', 'noun'), ('чуття', 'noun'), ('ягня', 'noun'), ('яєчня', 'noun'), ('яєшня', 'noun'), ('ял', 'noun'), ('ялиця', 'noun'), ('янгол', 'noun'), ('янкі', 'noun'), ('япі', 'noun'), ('яппі', 'noun'), ('яриця', 'noun'), ('ярі', 'noun'), ('ярові', 'noun')])
print()

print(get_words("base.lst", ['ц', 'и', 'д', 'щ', 'л']))
print([('дати', 'verb'), ('дбати', 'verb'), ('дебіл', 'noun'), ('дерти', 'verb'), ('дибки', 'noun'), ('дибки', 'adverb'), ('динод', 'noun'), ('дід', 'noun'), ('дійти', 'verb'), ('діл', 'noun'), ('діод', 'noun'), ('діти', 'verb'), ('дітки', 'noun'), ('діяти', 'verb'), ('дніти', 'verb'), ('довід', 'noun'), ('доїзд', 'noun'), ('доїти', 'verb'), ('досіл', 'noun'), ('доти', 'adverb'), ('дохід', 'noun'), ('дощ', 'noun'), ('драти', 'verb'), ('дреди', 'noun'), ('дрил', 'noun'), ('дрізд', 'noun'), ('дроги', 'noun'), ('дрозд', 'noun'), ('друїд', 'noun'), ('дувал', 'noun'), ('дути', 'verb'), ('дятел', 'noun'), ('ирод', 'noun'), ('лад', 'noun'), ('ланди', 'noun'), ('ланц', 'noun'), ('лапки', 'noun'), ('лати', 'noun'), ('лахи', 'noun'), ('лаяти', 'verb'), ('лити', 'verb'), ('лід', 'noun'), ('лізол', 'noun'), ('лізти', 'verb'), ('ліки', 'noun'), ('ліпід', 'noun'), ('лови', 'noun'), ('лорд', 'noun'), ('люд', 'noun'), ('ляги', 'noun'), ('лягти', 'verb'), ('лярд', 'noun'), ('ляси', 'noun'), ('лящ', 'noun'), ('цикл', 'noun'), ('щотри', 'adverb')])
print()

print(get_words("base.lst", ['й', 'ц', 'з', 'ь', 'ш']))
print([('забій', 'noun'), ('завіз', 'noun'), ('завій', 'noun'), ('заєць', 'noun'), ('заніз', 'noun'), ('запій', 'noun'), ('зараз', 'adverb'), ('заріз', 'noun'), ('збій', 'noun'), ('звій', 'noun'), ('згірш', 'adverb'), ('зельц', 'noun'), ('зернь', 'noun'), ('зизий', 'adjective'), ('злий', 'adjective'), ('змій', 'noun'), ('знать', 'noun'), ('золь', 'noun'), ('зріз', 'noun'), ('зять', 'noun'), ('йодль', 'noun'), ('цвіль', 'noun'), ('цвіть', 'noun'), ('цезій', 'noun'), ('ценз', 'noun'), ('ценоз', 'noun'), ('церій', 'noun'), ('цинь', 'noun'), ('цироз', 'noun'), ('цитоз', 'noun'), ('цілий', 'adjective'), ('ціль', 'noun'), ('шабаш', 'noun'), ('шалаш', 'noun'), ('шаль', 'noun'), ('шатуш', 'noun'), ('шваль', 'noun'), ('швець', 'noun'), ('шитий', 'adjective'), ('шкіц', 'noun'), ('шліц', 'noun'), ('шлюз', 'noun'), ('шпень', 'noun'), ('шпиль', 'noun'), ('шпіц', 'noun'), ('шприц', 'noun'), ('штиль', 'noun'), ('шугай', 'noun'), ('шулий', 'adjective'), ('шутий', 'adjective')])
print()

print(check_user_words([], "verb", ['л', 'є', 'я', 'і', 'ч'], "base.lst"))
print(([], ['ітися']))
print()
 # not enough values to unpack (expected 2, got 1) on line 105
print(check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb", ['и', 'щ', 'я', 'ц', 'г'], "base.lst"))
print((['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', 'явити', 'яріти', 'ячати']))
print()

 # not enough values to unpack (expected 2, got 1) on line 105
print(check_user_words(['бабин', 'битий', 'бичий', 'білий', 'бісів', 'богів', 'божий', 'босий', 'булий', 'булів', 'бурий', 'ласий', 'лисий', 'литий', 'лихий', 'лівий', 'любий', 'лютий', 'усний', 'утлий', 'щирий', 'щучий', 'щучин'], "adjective", ['н', 'у', 'й', 'б', 'л'], "base.lst"))
print((['бабин', 'битий', 'бичий', 'білий', 'божий', 'босий', 'булий', 'бурий', 'ласий', 'лисий', 'литий', 'лихий', 'лівий', 'любий', 'лютий', 'усний', 'утлий'], ['нагий', 'ненин', 'ниций', 'німий', 'нічий', 'новий', 'нянин']))
print()

 # not enough values to unpack (expected 2, got 1) on line 105
print(check_user_words([], "adjective", ['й', 'ц', 'з', 'ь', 'ш'], "base.lst"))
print(([], ['зизий', 'злий', 'цілий', 'шитий', 'шулий', 'шутий']))
print()
 # not enough values to unpack (expected 2, got 1) on line 105
print(check_user_words(['єресь', 'їхній', 'ґай'], 'noun', ['ґ', 'ь', 'й', 'є', 'ї'], 'base.lst'))
print((['єресь'], ['ґалій', 'ґедзь', 'ґлей', 'ґудзь', 'єврей', 'єлей', 'їдець', 'їнь', 'йодль']))
print()
 # not enough values to unpack (expected 2, got 1) on line 105