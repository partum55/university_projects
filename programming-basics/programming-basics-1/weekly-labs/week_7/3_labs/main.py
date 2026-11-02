import calendar as c


def insert_dyvo(sentence: str, flag: str) -> str:
    """
    Examples:
    >>> insert_dyvo('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> insert_dyvo('Козаки і коні, корови і кит', 'ко')
    'Дивокозаки і дивоконі, дивокорови і кит'
    >>> insert_dyvo('кіт кота кит', 'кі')
    'дивокіт кота кит'
    """
    return None if not (isinstance(sentence, str) and isinstance(flag, str)) \
        else " ".join(["Диво" + word.lower() if word[:len(flag)].lower() == flag.lower() and word[0].isupper() \
        else "Диво".lower() + word if word[:len(flag)].lower() == flag.lower() \
        else word for word in sentence.split(" ")])

def get_semester_calendar(output_type: str, year: int, first_month: int, last_month: int) -> str | None:
    """
    Examole:
    >>> get_semester_calendar("txt", 2023, 2, 1)

    >>> get_semester_calendar("html", 2023, 2, 1)

    """
    return None if not (isinstance(output_type, str) and isinstance(year, int) and isinstance(first_month, int) and isinstance(last_month, int)) or not (1 <= first_month <= 12 and 1 <= last_month <= 12) or first_month > last_month else "".join([c.TextCalendar().formatmonth(year, month) if output_type == "txt" else c.HTMLCalendar().formatmonth(year, month) if output_type == "html" else None for month in range(first_month, last_month + 1)]) if output_type in ["txt", "html"] else None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
