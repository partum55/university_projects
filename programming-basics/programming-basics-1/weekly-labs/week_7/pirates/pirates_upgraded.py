def read_file(pathname):
    """
    Read map from a file with pathname.
    Return list of tuples, where the first element
    is direction and the second is the number of steps.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('U 2\\nR 2\\nD 2\\nL 2')
    >>> with open(tmpfile.name, 'r', encoding='utf-8') as file:
    ...    print(file.read())
    U 2
    R 2
    D 2
    L 2
    >>> read_file(tmpfile.name)
    [('U', 2), ('R', 2), ('D', 2), ('L', 2)]
    >>> read_file("treasure.txt")
    [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    """
    with open(pathname, "r", encoding="utf-8") as file:
        coordinates = [((x := line.strip().split())[0], int(x[1])) for line in file]
    return coordinates


def write_map_to_file(mapa, pathname):
    '''
    Write the mapa to the file with path pathname.
    Returns nothing.

    >>> mapa = 'xxx\\nx.x\\nxxx'
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', delete=False) as tmpfile:
    ...    write_map_to_file(mapa, tmpfile.name)
    ...    print(tmpfile.read())
    xxx
    x.x
    xxx
    '''
    with open(pathname, "w", encoding="utf-8") as file:
        file.write(mapa)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
