def leave_keyword_from_file(file_input: str, keyword: str, file_output: str) -> int:
    """Leaves only the specified category in the output file.

    Args:
        file_input (str): The input file containing the keywords.
        keyword (str): The category to leave in the output file.
        file_output (str): The output file to write the filtered keywords.

    Returns:
        int: The number of lines removed from the input file.

    Examples:
    >>> leave_keyword_from_file('keywords.list', 'friendship', 'keywords_updated_d.list')
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
    with open(file_input, 'r', encoding="iso-8859-1") as file:
        keywords = False
        text = ""
        removed = 0
        curr_movies = []
        curr_movie = ""
        add = False
        while line:= file.readline():
            if "THE KEYWORDS LIST" in line:
                text += f"{line}{file.readline()}{file.readline()}"
                keywords = True
                continue
            if not keywords:
                text += line
                continue
            data = line.split("\t")
            name_year, keyword_ = data[0].strip(), data[-1].strip()
            if curr_movie != name_year:
                if add:
                    removed -= len(curr_movies)
                curr_movies = []
                curr_movie = name_year
                add = False

            if add:
                text += line
            else:
                removed += 1
                curr_movies.append(line)

            if keywords:
                if keyword == keyword_:
                    for line_ in curr_movies:
                        text += line_
                    add = True

    with open(file_output, "w", encoding="iso-8859-1") as file:
        file.write(text)
    return removed


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


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())