"""
This module contains functions for a word-based grid game. The game generates a 3x3 grid of letters
with a balanced mix of vowels and consonants. The user must form valid words from the grid, and the
system checks if those words exist in a predefined dictionary file.

The main functionalities include:
- Generating a 3x3 grid of random letters.
- Checking user-provided words based on game rules.
- Comparing user words with a dictionary file.
- Counting valid user words and identifying missed words.
"""


import random as r


def generate_grid() -> list[list[str]]:
    """
    Generates a 3x3 grid of random letters, with 3 vowels and 6 consonants.

    :return: A 3x3 list of lists containing letters
    :rtype: list[list[str]]
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                  'V', 'W', 'X', 'Y', 'Z']
    selected_vowels = r.choices(vowels, k=3)
    selected_consonants = r.choices(consonants, k=6)
    letters = selected_vowels + selected_consonants
    r.shuffle(letters)
    return [letters[i:i + 3] for i in range(0, 9, 3)]


def check_word(word: str, letters: list[str]) -> bool:
    """
    Checks if a word can be formed from the available letters in the grid.
    The word must be at least 4 letters long, and it must contain the middle letter of the grid.

    :param word: The word to check.
    :type word: str
    :param letters: The list of letters available in the grid.
    :type letters: list[str]
    :return: True if the word is valid, False otherwise.
    :rtype: bool
    """
    if len(word) < 4:
        return False
    temp_letters = letters.copy()
    if temp_letters[4] in word:
        for letter in word:
            if letter in temp_letters:
                temp_letters.remove(letter)
            else:
                return False
        return True
    return False


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f, checks the words with rules, and returns a list of valid words.

    :param f: The file path of the dictionary.
    :type f: str
    :param letters: The list of letters available in the grid.
    :type letters: list[str]
    :return: A list of valid words from the dictionary.
    :rtype: list[str]
    """
    with open(f, "r", encoding="utf-8") as file:
        output = []
        words = file.read().split("\n")
        for word in words:
            word = word.lower()
            if check_word(word, letters):
                output.append(word)
        return output


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list of these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter for Windows.

    :return: A list of words entered by the user.
    :rtype: list[str]
    """
    output = []
    try:
        while True:
            output.append(input())
    except (KeyboardInterrupt, EOFError):
        return output


def get_pure_user_words(user_words: list[str], letters: list[str],
                        words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns a list of those words that are not in dictionary.

    :param user_words: The words suggested by the user.
    :type user_words: list[str]
    :param letters: The list of letters available in the grid.
    :type letters: list[str]
    :param words_from_dict: The valid words from the dictionary.
    :type words_from_dict: list[str]
    :return: A list of words suggested by the user but not found in the dictionary.
    :rtype: list[str]
    """
    output = []
    for word in user_words:
        if word not in words_from_dict and check_word(word, letters):
            output.append(word)
    return output


def count_user_words(user_words: list[str], letters: list[str],
                     words_from_dict: list[str]) -> int:
    """
    Counts valid user words that are found in the dictionary.

    :param user_words: The words suggested by the user.
    :type user_words: list[str]
    :param letters: The list of letters available in the grid.
    :type letters: list[str]
    :param words_from_dict: The valid words from the dictionary.
    :type words_from_dict: list[str]
    :return: The count of valid words found in both the user input and the dictionary.
    :rtype: int
    """
    k = 0
    user_words = set(user_words)
    for word in user_words:
        if check_word(word, letters) and word in words_from_dict:
            k += 1
    return k


def missed_words(user_words: list[str], letters: list[str],
                 words_from_dict: list[str]) -> list[str]:
    """
    Identifies words from the dictionary that the user missed.

    :param user_words: The words suggested by the user.
    :type user_words: list[str]
    :param letters: The list of letters available in the grid.
    :type letters: list[str]
    :param words_from_dict: The valid words from the dictionary.
    :type words_from_dict: list[str]
    :return: A list of words from the dictionary that the user failed to suggest.
    :rtype: list[str]
    """
    user_words = set(user_words)
    miss = [word for word in words_from_dict if word not in user_words and check_word(word,letters)]
    return miss


def main():
    """
    Main function to execute the game logic. Generates the grid, accepts user input, compares with
    the dictionary, and prints results.
    """
    letters = generate_grid()
    print(f"Your board is {letters}")
    letters_new = [elem.lower() for line in letters for elem in line]
    print("Please, suggest your words here:")
    words = get_user_words()
    file_path = "en.txt"
    all_words = get_words(file_path, letters_new)
    print(f"Number of the right words: {count_user_words(words, letters_new, all_words)}")
    print(f"All possible words:\n {all_words}")
    print(f"You missed the following words:\n {missed_words(words, letters_new, all_words)}")
    print(f"You suggested, but we don't have them in the dictionary: "
          f"{get_pure_user_words(words, letters_new, all_words)}")


print("Test 3")
print(get_words('en.txt', list('wumrovkif')))
print(['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', 'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf'])
print()
print("Test 4")
print(get_words('en.txt', list('jniarnoah')))
print(['aaron', 'ahir', 'aira', 'airan', 'ajar', 'ajari', 'ajhar', 'arain', 'aria', 'arian', 'arion', 'arna', 'arni', 'aronia', 'hair', 'haori', 'harn', 'hiro', 'hoar', 'hora', 'horn', 'inro', 'iran', 'iroha', 'iron', 'jara', 'nahor', 'nair', 'noir', 'nonair', 'nora', 'norah', 'nori', 'noria', 'norn', 'norna', 'orna', 'raia', 'raia', 'rain', 'raja', 'raja', 'rajah', 'rajah', 'rana', 'rana', 'rani', 'ranina', 'rann', 'rhina', 'rhino', 'roan', 'rohan', 'ronni'])
print()
print("Test 5")
print(get_words('en.txt', list('vhtdsrael')))
print(['arles', 'arse', 'arsle', 'asher', 'ashet', 'aster', 'ates', 'aves', 'dares', 'darst', 'darts', 'dash', 'dasher', 'deash', 'desalt', 'devast', 'drest', 'east', 'eats', 'elsa', 'esth', 'hades', 'hals', 'halse', 'halves', 'harvest', 'haslet', 'haste', 'haster', 'hastler', 'havers', 'hearst', 'hearts', 'hers', 'hest', 'lars', 'laser', 'lash', 'lasher', 'last', 'laster', 'lastre', 'leads', 'leash', 'least', 'lesath', 'lest', 'lestrad', 'rase', 'rash', 'rastle', 'relast', 'resalt', 'resh', 'rest', 'sade', 'sadh', 'sadhe', 'sadr', 'sadr', 'sale', 'salt', 'salted', 'salter', 'salve', 'salver', 'sard', 'sard', 'sardel', 'sare', 'sart', 'sart', 'sate', 'save', 'saved', 'saver', 'sdeath', 'seah', 'seal', 'sear', 'seat', 'sedat', 'selah', 'selt', 'selva', 'sera', 'seral', 'sert', 'serta', 'serval', 'seta', 'setal', 'seth', 'seth', 'shad', 'shade', 'shader', 'shale', 'shalt', 'shard', 'share', 'shat', 'shave', 'shaved', 'shaver', 'shea', 'sheal', 'shear', 'sheard', 'sheat', 'shed', 'shel', 'shela', 'sheld', 'shelta', 'sher', 'sheva', 'shrave', 'shred', 'slad', 'slade', 'slae', 'slare', 'slart', 'slarth', 'slat', 'slate', 'slater', 'slath', 'slather', 'slav', 'slave', 'slave', 'slaved', 'slaver', 'sled', 'stade', 'stale', 'star', 'star', 'stare', 'starve', 'starved', 'stave', 'staver', 'stead', 'steal', 'stela', 'stelar', 'stra', 'strad', 'strad', 'strade', 'stradl', 'strae', 'strave', 'stre', 'tales', 'tars', 'tarse', 'tash', 'tavers', 'teras', 'trash', 'tsar', 'valse', 'vase', 'vast', 'versal', 'verst', 'versta', 'vest', 'vesta', 'vestal', 'vestral'])
print()
print("Test 6")
print(get_words('en.txt', list('gecthpoak')))
print(['ache', 'ahet', 'cahot', 'caph', 'caph', 'cathop', 'chao', 'chap', 'chape', 'chapt', 'chat', 'cheap', 'cheat', 'cheka', 'chet', 'choate', 'choga', 'chogak', 'chokage', 'choke', 'chop', 'chopa', 'coth', 'cothe', 'each', 'echo', 'epha', 'epoch', 'epocha', 'etch', 'gatch', 'getah', 'ghat', 'gotch', 'goth', 'gotha', 'hack', 'haec', 'haet', 'hake', 'hako', 'hate', 'heap', 'heat', 'heck', 'hepcat', 'hock', 'hocket', 'hoga', 'hope', 'kath', 'keach', 'ketch', 'khat', 'khet', 'khot', 'koch', 'koph', 'oath', 'ocht', 'opah', 'othake', 'pacht', 'paho', 'patch', 'path', 'peach', 'pech', 'pecht', 'peho', 'phaet', 'phage', 'phoca', 'phot', 'poach', 'poche', 'poha', 'potch', 'tach', 'tache', 'tche', 'tcheka', 'teach', 'tech', 'tech', 'thack', 'thea', 'theca', 'theo', 'thoke', 'toph'])
print()
print("Test 7")
print(get_words('en.txt', list('emxpczwpi')))
print(['cimex', 'epic', 'mice', 'pice', 'wice'])
print()