"""
Code 2
"""


from math import ceil
def find_the_most_profitable_plan(visits: int) -> str:
    """
    This feature searches for the best plan to choose for gym customers.
    Parameters:
    v (int): The number of training sessions.
    Returns:
    str: The most profitable plan.
    >>> find_the_most_profitable_plan(4)
    '5-visit package'
    >>> find_the_most_profitable_plan(10)
    '5-visit package'
    >>> find_the_most_profitable_plan(11)
    'membership'
    >>> find_the_most_profitable_plan(16)
    'membership'
    >>> find_the_most_profitable_plan(1)
    'pay per visit'
    """
    pay_per_visit = visits * 25
    cnt_package = ceil(visits / 5)
    pay_with_package = cnt_package * 5 * 18
    pay_with_card = 100 + visits * 25 * 0.6
    min_pay = min(pay_per_visit, pay_with_package, pay_with_card)
    if min_pay == pay_per_visit:
        return "pay per visit"
    if min_pay == pay_with_package:
        return "5-visit package"
    return "membership"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
