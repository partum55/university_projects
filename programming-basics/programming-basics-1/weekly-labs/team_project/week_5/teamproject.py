"""Temp"""


def read_file(pathname: str, year: int=0) -> \
    list[list[str, str, str, str, str, str, str, str, str, str, str]]:
    """

    :param pathname:
    :param year:
    :return:

    >>> read_file('films.csv', 2014)[:2]
    [['1', 'Guardians of the Galaxy', 'Action,Adventure,Sci-Fi', \
'A group of intergalactic criminals are forced to work together to stop a fanatical \
warrior from taking control of the universe.', \
'James Gunn', 'Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana', '2014', '121', \
'8.1', '757074', '333.13', '76.0'], ['3', \
'Split', 'Horror,Thriller', 'Three girls are kidnapped by a man with a diagnosed 23 \
distinct personalities. They must try to \
escape before the apparent emergence of a frightful new 24th.', 'M. Night Shyamalan', \
'James McAvoy, Anya Taylor-Joy, Haley Lu Richardson, Jessica Sula', \
'2016', '117', '7.3', '157606', '138.12', '62.0']]
    """
    with open(pathname, "r", encoding="utf-8") as file:
        file.readline()
        result = [line.strip().split(";") for line in file if int(line.split(";")[6]) >= year]
        return result



def top_n(data: list, genre: str='', n: int=0):
    """

    :param data:
    :param genre:
    :param n:
    :return:
    """
    result = {}
    for line in data:
        actors = line[5].split(", ")
        for elem in actors:
            result.setdefault(elem, []).append(float(line[8]))
    return result

def write_file(top: list, file_name: str):
    """

    :param top:
    :param file_name:
    :return:
    """
    ...


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

a = read_file("films.csv", 2014)
print(top_n(a, genre='Action', n=5))