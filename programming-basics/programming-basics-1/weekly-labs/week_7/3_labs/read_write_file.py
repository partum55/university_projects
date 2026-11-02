import urllib.request as u


def read_input_file(url: str, number: int) -> list[list[str]]:
    """
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url

    >>> read_input_file('https://rb.gy/97llc',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://rb.gy/97llc',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    output = []
    with u.urlopen(url) as data:
        for line in data:
            line = line.decode("utf").strip().split("\t")
            
            if line[0].isdigit():
                output.append([line[0], line[1], "+", line[3], line[]])
    return output[:3]


def write_csv_file(url: str):
    '''write info to csv file with the path total.csv'''
    pass

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())