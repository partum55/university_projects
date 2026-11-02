"""Temp"""


def leave_keyword_from_file(file_input: str, keyword: str, file_output: str) -> int:
    """Leaves only the specified category in the output file.

    Args:
        file_input (str): The input file containing the keywords.
        keyword (str): The category to leave in the output file.
        file_output (str): The output file to write the filtered keywords.

    Returns:
        int: The number of lines removed from the input file.

    Examples:
    >>> leave_keyword_from_file('keywords.list', 'friendship', 'keywords_updated.list')
    3815451
    >>> keywords = create_film_keywords_dictionary('keywords_updated.list')
    >>> sum(len(values) for values in keywords.values())
    246990
    >>> values = iter(keywords.items())
    >>> movie, keywords = next(values)
    >>> movie
    '"#ATown" (2014)'
    >>> keywords == {'friendship', 'texas', 'drugs', 'beer', \
    'austin-texas', 'love', 'web-series'}
    True
    >>> movie, keywords = next(values)
    >>> movie
    '"11-11 En mi cuadra nada cuadra" (2013)'
    >>> keywords == {'friendship', 'pop-star', 'movie-director', 'inventor', \
    'time-machine', 'geek', 'cooking', 'musician', 'price-of-fame', 'singing', \
    'star', 'mad-scientist', 'time-travel', 'missing-mother', 'teenage-love'}
    True
    """
    with open(file_input, "r", encoding="iso-8859-1") as inn:
        v_films = {l.split("\t")[0].strip() for l in inn if l.split("\t")[-1].strip() == keyword}

    with open(file_input, "r", encoding="iso-8859-1") as inn, \
            open(file_output, "w", encoding="iso-8859-1") as out:
        counter = 0
        while (line := inn.readline()) != "8: THE KEYWORDS LIST\n":
            out.write(line)
            counter += 1
        out.write(line)
        out.write(inn.readline())
        out.write(inn.readline())
        for line in inn:
            if line.split("\t")[0].strip() in v_films:
                out.write(line)
                counter += 1
        return 4062787 - counter - 2


def create_film_keywords_dictionary(filename: str) -> dict[str, list]:
    """Creates a dictionary where the key is the name of the movie
    and the year in brackets as in the file, and the values
    are the set of keywords.

    Args:
        filename (str): The name of the file containing the keywords.

    Returns:
        dict[str, list]: A dictionary with movie names and years as keys
                         and sets of keywords as values.

    Examples:
    >>> keywords = create_film_keywords_dictionary('keywords.list')
    >>> sum(len(values) for values in keywords.values())
    4062441
    >>> values = iter(keywords.items())
    >>> next(values)
    ('"#1 Single" (2006)', {'number-in-title'})
    >>> next(values)
    ('"#1MinuteNightmare" (2014)', {'web-series'})
    >>> movie = next(values)
    >>> movie[0]
    '"#30Nods" (2016)'
    >>> movie[1] == {'friend', 'vlog', 'heroin'}
    True
    """
    with open (filename, "r", encoding="iso-8859-1") as file:
        while (line := file.readline()) != "8: THE KEYWORDS LIST\n":
            ...
        file.readline()
        file.readline()
        ans = {}
        for line in file:
            ans.setdefault(line.split("\t")[0].strip(), set()).add(line.split("\t")[-1].strip())
        return ans


def find_films_with_max_keywords(film_keywords: dict[str, list], num_of_films: int) -> list[tuple]:
    """Finds the films with the maximum number of keywords.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        num_of_films (int): The number of films to return.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the name of the film
                     and the number of keywords, sorted by number of keywords in descending order.
                     If the number of keywords are equal, names of films should be sorted by names
                     with usual string comparison.

    Examples:
    >>> find_films_with_max_keywords(create_film_keywords_dictionary('keywords.list'), 3)
    [('Clouds of Sils Maria (2014)', 642), \
('The Dark Knight (2008)', 530), ('The Dark Knight Rises (2012)', 446)]
    """
    ans = sorted([(film, len(keywords)) for film, keywords in film_keywords.items()],
                 key=lambda x: (-x[1], x[0]))
    return ans[:num_of_films]


def find_most_popular_keywords(film_keywords: dict, num_of_keywords: int) -> list[tuple]:
    """Finds the most popular keywords.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        num_of_keywords (int): The number of keywords to return.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the keyword
                     and the number of films associated with that keyword, sorted by the number
                     of films in descending order. If the number of films are equal, the keywords
                     should be sorted by names with usual string comparison.

    Examples:
    >>> find_most_popular_keywords(create_film_keywords_dictionary('keywords.list'), 3)
    [('character-name-in-title', 40946), ('independent-film', 31213), ('based-on-novel', 28564)]
    """
    keyword_counts = {}
    for keywords in film_keywords.values():
        for keyword in keywords:
            if keyword in keyword_counts:
                keyword_counts[keyword] += 1
            else:
                keyword_counts[keyword] = 1
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_keywords[:num_of_keywords]


def find_films_keyword_year(film_keywords: dict, keyword: str, year: int) -> set:
    """Finds films that contain a specific keyword and were released in a specific year.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        keyword (str): The keyword to search for.
        year (int): The year of release to search for.

    Returns:
        set: A set of film names that match the keyword and year.

    Examples:
    >>> find_films_keyword_year(create_film_keywords_dictionary('keywords.list'), \
'supernatural', 1988) == {'Kumander Bawang (1988)', '"Monsters" (1988) {Rain Dance (#1.19)}', \
'Saturday the 14th Strikes Back (1988)', '"Tian xia" (1988)', \
'A Nightmare on Elm Street 4: The Dream Master (1988)'}
    True
    """
    res = {film for film, keywords in film_keywords.items() \
           if keyword in keywords and f"({year})" in film}
    return res


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
