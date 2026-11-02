"""
This module provides functionality to process a train ticket identifier and
determine its seat location based on the principle of binary search. Specifically,
it decodes a ticket string representing seating and compartment information and
returns a tuple with the details of the compartment, seat number, and position.

It includes:
 - A single function, transform_ticket, for decoding ticket strings.
 - Example usage of the function with the doctest module for testing.
"""


def transform_ticket(ticket: str) -> tuple[int, int, int] | None:
    """
    Decodes a train ticket identifier into its corresponding compartment, seat number, and position.

    This function takes a 10-character string (`ticket`) as input. The first seven characters
    (`Г` or `Х`) represent a binary split to determine the seat number within the train.
    The last three characters (`Л` or `П`) determine the seat position within a compartment.

    The function processes these characters, calculates the compartment number, seat number,
    and position, and returns them as a tuple.

    :param ticket: A 10-character string where:
                   - Characters 1–7 are 'Г' (front half) or 'Х' (back half).
                   - Characters 8–10 are 'Л' (left side) or 'П' (right side).
    :return: A tuple `(compartment_number, seat_number, position)` where:
             - `compartment_number` is the compartment index (1-based).
             - `seat_number` is the specific seat within the train.
             - `position` is the seat's position within the compartment (1–8).
             Returns `None` if the input is invalid.

    Examples:
    >>> transform_ticket("ГГХГХХЛЛГП")
    >>> transform_ticket("Вагон 7, місце 3")
    >>> transform_ticket("ГГХГХХГЛЛП")
    (3, 7, 2)
    >>> transform_ticket("ГГГГГГГЛЛЛ")
    (1, 1, 1)
    >>> transform_ticket("ХХХХХХХППП")
    (16, 8, 8)
    >>> transform_ticket("ГГГГГГХППЛ")
    (1, 2, 7)
    >>> transform_ticket(1234567890)
    >>> transform_ticket("ГГХГХХГЛЛП")
    (3, 7, 2)
    >>> transform_ticket("ГГХГХХЛЛГП")
    >>> transform_ticket("ХХХХХХХЛЛП")
    (16, 8, 2)
    >>> transform_ticket("ГГГГГГГППП")
    (1, 1, 8)
    >>> transform_ticket("Вагон 7, місце 3")
    >>> transform_ticket(3.3)
    >>> transform_ticket("ГГГГгГГППП")
    >>> transform_ticket("ГХХХГЛППГГ")
    >>> transform_ticket("")
    >>> transform_ticket("ГГГГГГГГГГГ")
    >>> transform_ticket(["Г", "Г", "Г", "Г", "Г", "Г", "Г", "П", "П", "П"])
    """
    if not isinstance(ticket, str):
        return None
    if len(ticket) != 10:
        return None
    lst = list(range(1, 129))
    for i in range(7):
        l = int(len(lst) / 2)
        if ticket[i] == "Г":
            lst = lst[:l]
        elif ticket[i] == "Х":
            lst = lst[l:]
        else:
            return None
    lst2 = list(range(1, 9))
    for i in range(7, 10):
        l = int(len(lst2) / 2)
        if ticket[i] == "Л":
            lst2 = lst2[:l]
        elif ticket[i] == "П":
            lst2 = lst2[l:]
        else:
            return None
    vagon = int(-(-(lst[0] / 8) // 1))
    kupe = lst[0] - int(lst[0] / 8) * 8
    if not kupe:
        kupe = 8
    seat = lst2[0]
    return vagon, kupe, seat


if __name__ == "__main__":
    import doctest
    doctest.testmod()
