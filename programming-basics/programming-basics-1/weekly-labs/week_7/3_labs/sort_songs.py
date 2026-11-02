"""
This module provides a function to sort the song in 3 different ways.
"""

from typing import Callable

def song_length(x: tuple[str, str]) -> float:
    """
    Returns the length of the song as a float, used for sorting by song length.

    :param x: A tuple containing the song title and its length as a string.
    :type x: tuple[str, str]
    :return: The length of the song converted to a float.
    :rtype: float

    >>> song_length(('Янанебібув', '3.19'))
    3.19
    """
    return float(x[1])

def title_length(x: tuple[str, str]) -> int:
    """
    Returns the length of the song title, used for sorting by title length.

    :param x: A tuple containing the song title and its length.
    :type x: tuple[str, str]
    :return: The length of the song title.
    :rtype: int

    >>> title_length(('Сосни', '4.31'))
    5
    """
    return len(x[0])

def last_word(x: tuple[str, str]) -> str:
    """
    Returns the first letter of the last word of the song title, used for sorting by last word.

    :param x: A tuple containing the song title and its length.
    :type x: tuple[str, str]
    :return: The first letter of the last word in the song title.
    :rtype: str

    >>> last_word(('Той день', '3.58'))
    'д'
    """
    return x[0].split()[-1][0]

def sort_songs(
        song_titles: list[str],
        length_songs: list[str],
        key: Callable[[tuple], int | str | float]) -> list[tuple] | None:
    """
    Sorts songs based on the specified key.

    :param song_titles: A list of song titles.
    :type song_titles: list[str]
    :param length_songs: A corresponding list of song lengths.
    :type length_songs: list[str]
    :param key: The key by which to sort (song_length, title_length, last_word).
    :type key: Callable[[tuple], int | str | float]
    :return: A sorted list of tuples (song title, song length) or None if input is invalid.
    :rtype: list[tuple[str, str]] | None

    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни'],\
                   ['3.19', '3.58', '5.06', '4.31'],  song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58'), ('Сосни', '4.31'), ('Мало мені', '5.06')]
    """
    if len(song_titles) != len(length_songs):
        return None

    for song in song_titles:
        if not isinstance(song, str):
            return None

    for length in length_songs:
        if not isinstance(length, str):
            return None
    songs = []
    for i, elem in enumerate(song_titles):
        songs.append((elem, length_songs[i]))
    return sorted(songs, key=key)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
