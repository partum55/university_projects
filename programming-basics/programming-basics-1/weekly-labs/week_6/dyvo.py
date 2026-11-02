"""
dyvo_insert_module.py

This module provides a function `dyvo_insert` that inserts the word "Диво"
before every word in a sentence that starts with a specific prefix (flag).

The module is designed to work with sentences written in Ukrainian and
is case-sensitive, preserving the capitalization of words when modifying them.
"""


def insert_dyvo(sentence: str, flag: str) -> str:
    """
    Insert the word "Диво" before every word in the sentence that starts with the given flag.

    The function checks each word in the sentence to see if it starts with the given flag (prefix).
    If a word matches the prefix, "Диво" is inserted before it. The function handles case-sensitivity
    and ensures that the capitalization of the word is preserved when "Диво" is added.

    :param sentence: The sentence in which to insert "Диво" before words starting with the flag.
    :type sentence: str
    :param flag: The prefix to look for in words where "Диво" will be inserted before.
    :type flag: str
    :return: The modified sentence where "Диво" is inserted before each word starting with the flag.
    :rtype: str

    Examples:
    >>> insert_dyvo('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'

    >>> insert_dyvo('Козаки і коні, корови і кит', 'ко')
    'Дивокозаки і дивоконі, дивокорови і кит'

    >>> insert_dyvo('кіт кота кит', 'кі')
    'дивокіт кота кит'
    """
    if not (isinstance(sentence, str) or isinstance(flag, str)):
        return None

    output = []
    words = sentence.split(" ")
    dyvo = "Диво"

    for word in words:
        if word[:len(flag)].lower() == flag.lower():
            if word[0].isupper():
                output.append(dyvo + word.lower())
            else:
                output.append(dyvo.lower() + word)
        else:
            output.append(word)

    return " ".join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
