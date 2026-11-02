"""Temp"""


def sites_on_date(visits: list, date: str)-> set[str]:
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in the browser history
    (you get it as the result of the function get_chrome_os
    from get_browser_history module)
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    """
    output = set()
    for line in visits:
        if line[2] == date:
            output.add(line[0])
    return output


def most_frequent_sites(visits: list, number: int)-> set[str]:
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    If the frequency is the same choose sites in the alphabetical order
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    """
    output = {}
    urls_lst = []
    for elem in visits:
        urls_lst.append(elem[0])
    for url in urls_lst:
        output.setdefault(urls_lst.count(url), []).append(url)
    for key, elem in output.items():
        output.setdefault(key, elem).sort()
    max_elems = sorted(output)[::-1]
    result = set()
    if number >= len(max_elems):
        for i, elem in enumerate(max_elems):
            result.add(output[elem][0])
    else:
        for i in range(number):
            result.add(output[max_elems[i]][0])
    return result


def get_url_info(visits: list, url: str) -> tuple:
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([ \
    ("https://learn.ucu.edu.ua/mod/vpl/view.php?id=34856", "LMS", \
    "2024-11-01", "00:00:01.01", 1230984), \
    ("https://www.youtube.com/watch?v=TtkFsfOP9QI", "youtube", \
    "2024-11-01", "23:59:31.00", 1984), \
    ("https://www.youtube.com/watch?v=TtkFsfOP9QI", "youtube", \
    "2024-11-01", "21:16:31.00", 123092), \
    ("https://www.startpage.com", "startpage", \
    "2024-11-02", "32:12:99.95", 123) \
    ], "https://www.youtube.com/watch?v=TtkFsfOP9QI")
    ('youtube', '2024-11-01', '23:59:31.00', 2, 62538.0)
    >>> get_url_info([ \
    ("https://learn.ucu.edu.ua/mod/vpl/view.php?id=34856", "LMS", \
    "2024-11-01", "00:00:01.01", 1230984), \
    ("https://www.youtube.com/watch?v=TtkFsfOP9QI", "youtube", \
    "2024-11-01", "23:59:31.00", 1984), \
    ("https://www.youtube.com/watch?v=TtkFsfOP9QI", "youtube", \
    "2024-11-01", "21:16:31.00", 123092), \
    ("https://www.youtube.com/watch?v=TtkFsfOP9QI", "youtube", \
    "2024-10-01", "23:59:59.99", 123092), \
    ("https://www.startpage.com", "startpage", \
    "2024-11-02", "32:12:99.95", 123) \
    ], "https://www.youtube.com/watch?v=TtkFsfOP9QI")
    ('youtube', '2024-11-01', '23:59:31.00', 3, 82722.66666666667)
    """
    counter = 0
    for line in visits:
        counter += 1 if line[0] == url else 0
    for line in visits:
        if line[0] == url:
            max_date = max(elem[2] for elem in visits if elem[0] == url)
            max_time = max(elem[3] for elem in visits if elem[0] == url and elem[2] == max_date)
            average = sum(elem[4] for elem in visits if elem[0] == url) / counter
            output = line[1], max_date, max_time, counter, average
            return output
    return '', '', '', 0, 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
