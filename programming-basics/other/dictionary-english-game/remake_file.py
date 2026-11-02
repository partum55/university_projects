"""
Dictionary Processing Script

This script reads a dictionary from a CSV file and allows filtering words based on their parts of speech:
nouns, verbs, adverbs, and adjectives. It provides functions to process the data and print the results.
"""


def open_dictionary(filename: str) -> list[tuple[str, str]]:
    """
    Reads the dictionary file and returns a list of words with their parts of speech.

    :param filename: The path to the CSV file.
    :type filename: str
    :return: A list of tuples in the format [(word, part_of_speech), ...].
    :rtype: list[tuple[str, str]]
    """
    with open(filename, "r", encoding="utf-8") as file:
        dictionary = []
        for line in file:
            try:
                line = line.strip().split(",")
                word = line[0].lower()
                language_part = ("noun" if line[1] == "n." else
                                 "verb" if line[1] == "v." else
                                 "adverb" if line[1] == "adv." else
                                 "adjective" if line[1] == "a." else "")
                if language_part != "": dictionary.append((word, language_part))
            except IndexError:
                continue
        return dictionary


def only_noun(dictionary: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of nouns from the dictionary.

    :param dictionary: The list of tuples returned by open_dictionary().
    :type dictionary: list[tuple[str, str]]
    :return: A list of nouns (str).
    :rtype: list[str]
    """
    nouns = [word[0] for word in dictionary if word[1] == "noun"]
    with open ("nouns.csv", "w", encoding = "utf-8") as file:
        for word in nouns:
            file.write(word + "\n")
    return nouns


def only_verb(dictionary: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of verbs from the dictionary.

    :param dictionary: The list of tuples returned by open_dictionary().
    :type dictionary: list[tuple[str, str]]
    :return: A list of verbs (str).
    :rtype: list[str]
    """
    verbs = [word[0] for word in dictionary if word[1] == "verb"]
    with open ("verbs.csv", "w", encoding = "utf-8") as file:
        for word in verbs:
            file.write(word + "\n")
    return verbs


def only_adverb(dictionary: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of adverbs from the dictionary.

    :param dictionary: The list of tuples returned by open_dictionary().
    :type dictionary: list[tuple[str, str]]
    :return: A list of adverbs (str).
    :rtype: list[str]
    """
    adverbs = [word[0] for word in dictionary if word[1] == "adverb"]
    with open ("adverbs.csv", "w", encoding = "utf-8") as file:
        for word in adverbs:
            file.write(word + "\n")
    return adverbs


def only_adjective(dictionary: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of adjectives from the dictionary.

    :param dictionary: The list of tuples returned by open_dictionary().
    :type dictionary: list[tuple[str, str]]
    :return: A list of adjectives (str).
    :rtype: list[str]
    """
    adjectives = [word[0] for word in dictionary if word[1] == "adjective"]
    with open ("adjectives.csv", "w", encoding = "utf-8") as file:
        for word in adjectives:
            file.write(word + "\n")
    return adjectives


def main() -> None:
    """
    Main function to run the dictionary processing script.

    This function reads the dictionary from a file, filters the words by their parts of speech,
    and prints the results to the console.

    :return: None
    """
    filename = "dictionary.csv"
    dictionary = open_dictionary(filename)
    nouns = only_noun(dictionary)
    verbs = only_verb(dictionary)
    adverbs = only_adverb(dictionary)
    adjectives = only_adjective(dictionary)

    print("All dictionary:")
    print(dictionary)
    print()
    print("Only nouns:")
    print(nouns)
    print()
    print("Only verbs:")
    print(verbs)
    print()
    print("Only adverbs:")
    print(adverbs)
    print()
    print("Only adjectives:")
    print(adjectives)
    print()

    return None


main()
