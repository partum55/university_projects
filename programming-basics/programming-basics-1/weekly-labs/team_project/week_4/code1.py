"""
Code 1
"""


def check_circle_inscribed_square(r: int | float, a: int | float) -> bool:
    """
    Checks if a circle with radius `r` can be inscribed within a square 
    with side length `a`.
    Parameters:
    r (int | float): Radius of the circle.
    a (int | float): Side length of the square.
    Returns:
    bool: True if the circle can be inscribed within the square, 
          otherwise False.
    """
    if isinstance(r,(float,int)) and isinstance(a,(float,int)) and r*2 == a:
        return True
    return False
