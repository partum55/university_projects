def leave_keyword_from_file(file_input: str, keyword: str, file_output: str) -> int:
    """Leaves only the specified category in the output file.

    Args:
        file_input (str): The input file containing the keywords.
        keyword (str): The category to leave in the output file.
        file_output (str): The output file to write the filtered keywords.

    Returns:
        int: The number of lines removed from the input file.

    Examples:
    >>> leave_keyword_from_file('keywords.list', 'friendship', 'keywords_updated_i.list')
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
    result = ''
    c = 0
    with open(file_input, 'r', encoding='iso-8859-1') as file:
        fl = False
        have_keyword = False
        temp = ''
        for line in file:
            if '8: THE KEYWORDS LIST' in line:
                fl = True
                file.readline()
                file.readline()
                c += 3
            if fl:
                if temp.split('\n', maxsplit=1)[0].split()[:-1] != line.split()[:-1]:
                    if have_keyword:
                        result += temp
                        have_keyword = False
                    else:
                        c += temp.count('\n')
                    temp = line
                    if keyword == line.split()[-1]:
                        have_keyword = True
                else:
                    if keyword == line.split()[-1]:
                        have_keyword = True
                    temp += line
            else:
                c += 1
    return c


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
    with open (filename, 'r', encoding='iso-8859-1') as file:
        line_ = file.readline().strip()
        result = {}
        if line_ == 'CRC: 0x79027061  File: keywords.list  Date: Fri Nov 27 00:00:00 2015':
            while '8: THE KEYWORDS LIST' not in file.readline():
                pass
            file.readline()
            file.readline()
        else:
            sp = line_.split()
            movie_name = ' '.join(sp[:-1])
            result[movie_name] = set()
            result[movie_name].add(sp[-1])
        for line in file:
            line = line.strip()
            splited = line.split()
            movie_name = ' '.join(splited[:-1])
            if movie_name not in result:
                result[movie_name] = set()
            result[movie_name].add(splited[-1])
        return result