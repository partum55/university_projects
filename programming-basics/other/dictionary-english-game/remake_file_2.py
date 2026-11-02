def open_dictionary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        output = []
        i = 0
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
            if word not in output:
                i += 1
                output.append(temp)
                if i % 10000 == 0: print(i)
    return output


def only_noun(dictionary: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of nouns from the dictionary.

    :param dictionary: The list of tuples returned by open_dictionary().
    :type dictionary: list[tuple[str, str]]
    :return: A list of nouns (str).
    :rtype: list[str]
    """
    nouns = [word[0] for word in dictionary if word[1] == "noun"]
    with open ("nouns_ua.csv", "w", encoding = "utf-8") as file:
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
    with open ("verbs_ua.csv", "w", encoding = "utf-8") as file:
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
    with open ("adverbs_ua.csv", "w", encoding = "utf-8") as file:
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
    with open ("adjectives_ua.csv", "w", encoding = "utf-8") as file:
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
    filename = "base.lst"
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