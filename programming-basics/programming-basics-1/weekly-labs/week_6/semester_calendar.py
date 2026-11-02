"""
calendar_semester_module.py

This module provides functionality to generate a semester calendar either in text or HTML format
for a specified range of months within a given year.

It utilizes Python's built-in `calendar` module to generate calendar representations.
"""
import calendar as c


def get_semester_calendar(output_type: str, year: int, first_month: int, last_month: int) -> str | None:
    """
    Generate a semester calendar for the given year and month range in the specified format.

    This function allows the user to generate a calendar for a specified semester
    within a given year. The user can choose to output the calendar in either plain text ('txt') or
    HTML ('html') format.

    :param output_type: The format of calendar. It must be 'txt' for plain text or 'html' for HTML.
    :type output_type: str
    :param year: The year for which the calendar should be generated (e.g., 2024).
    :type year: int
    :param first_month: The first month of the semester (1 to 12).
    :type first_month: int
    :param last_month: The last month of the semester.
    :type last_month: int
    :return: A string containing the formatted calendar for the given range of months,
             either in plain text or HTML, depending on the specified `output_type`.
             Returns `None` if invalid input is provided.
    :rtype: str

    Examole:
    >>> get_semester_calendar("txt", 2023, 2, 1)

    >>> get_semester_calendar("html", 2023, 2, 1)

    >>> get_semester_calendar('txt', 2022, 2, 2)
    '   February 2022\\n\
Mo Tu We Th Fr Sa Su\\n\
    1  2  3  4  5  6\\n\
 7  8  9 10 11 12 13\\n\
14 15 16 17 18 19 20\\n\
21 22 23 24 25 26 27\\n\
28\\n'
    """
    if not (isinstance(output_type, str) and isinstance(year, int) and
        isinstance(first_month, int) and isinstance(last_month, int)):
        return None
    if not (1 <= first_month <= 12 and 1 <= last_month <= 12) or first_month > last_month:
        return None

    output = ""
    if output_type == "txt":
        for month in range(first_month, last_month + 1):
            output += c.TextCalendar().formatmonth(year, month)
    elif output_type == "html":
        for month in range(first_month, last_month + 1):
            output += c.HTMLCalendar().formatmonth(year, month)
    else:
        return None

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
