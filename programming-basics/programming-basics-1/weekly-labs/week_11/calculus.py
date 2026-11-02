"""Temp"""


def find_max_value(func: callable, points: list[float]) -> float:
    """Find the maximal value of a function at given points.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        float: The maximal value of the function at the given points
               round to 2 decimal points.

    Examples:

    >>> find_max_value(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return round(max(func(a) for a in points), 2)


def find_max_points(func: callable, points: list[float]) -> set[float]:
    """Find the points where the function has the maximal value.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        set[float]: A set of points where the function has the maximal value.

    Examples:
    >>> find_max_points(lambda x: x ** 2 + x, [1, 2, 3, -1])
    {3}
    >>> find_max_points(lambda x: -x ** 2 + 4*x, [1, 0, 3, -1])
    {1, 3}
    """
    return {a for a in points if func(a) == max(func(a) for a in points)}


def compute_limit(seq: callable) -> float:
    """Compute the limit of a convergent sequence.

    Args:
        seq (callable): A function representing the sequence.

    Returns:
        float: The limit of the sequence rounded up to 2 decimal points.

    Examples:
        >>> compute_limit(lambda n: (n ** 2 + n) / (3*n ** 2))
        0.33
    """
    prev_value = seq(1)
    n = 10
    while True:
        current_value = seq(n)
        if abs(current_value - prev_value) < 0.001:
            return round(current_value, 2)
        prev_value = current_value
        n *= 10

def compute_derivative(func: callable, x_0: float) -> float:
    """Compute the derivative of a function at a given point.

    Args:
        func (callable): The function to differentiate.
        x_0 (float): The point at which to compute the derivative.

    Returns:
        float: The derivative of the function at the given point.

    Examples:
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    >>> compute_derivative(lambda x: 4, 0)
    0.0
    """
    delta = 1
    prev_derivative = 0
    while True:
        try:
            derivative = (func(x_0 + delta) - func(x_0)) / delta
        except ZeroDivisionError:
            return 0.0
        if prev_derivative and abs(derivative - prev_derivative) < 0.001:
            return round(derivative, 2)
        prev_derivative = derivative
        delta /= 10


def get_tangent(func: callable, x_0: float) -> str:
    """Calculate the equation of the tangent line to a given function at a specified point.

    This function computes the tangent line to the input function `func` at the point `x_0`.
    The tangent line is represented in the form of a linear equation.

    Args:
        func (callable): A function for which the tangent line is to be calculated.
        x_0 (float): The x-coordinate at which the tangent line is computed.

    Returns:
        str: A string representing the equation of the tangent line in the format 'm * x + c',
             where 'm' is the slope (rounded to 2 decimal point) and 'c' is the y-intercept
             (also rounded to 2 decimal point).

    Examples:
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x, 2)
    'x'
    >>> get_tangent(lambda x: -x, 2)
    '- x'
    >>> get_tangent(lambda x: x**2-2, 0.5)
    'x - 2.25'
    >>> get_tangent(lambda x: -x**2-2, 0.5)
    '- x - 1.75'
    >>> get_tangent(lambda x: 4, 1)
    '4.0'
    >>> get_tangent(lambda x: 0, 1)
    '0.0'
    >>> get_tangent(lambda x: -3, 2)
    '- 3.0'
    >>> get_tangent(lambda x: x + 4, -10)
    'x + 4.0'
    >>> get_tangent(lambda x: x ** 2, 5)
    '10.0 * x - 25.0'
    >>> get_tangent(lambda x: 2 * x ** 2 + 2, 1)
    '4.0 * x'
    """
    result = ""
    k = compute_derivative(func, x_0)
    y_0 = round(func(x_0), 2)
    b = round((y_0 - k * x_0), 2)
    if k == 0:
        return f"{b}" if b >= 0 else f"- {abs(b)}"
    elif k == 1:
        result += "x"
    elif k == -1:
        result += "- x"
    elif k < 0:
        result += f"- {abs(k)} * x"
    else:
        result += f"{k} * x"
    if b > 0:
        result += f" + {b}"
    elif b < 0:
        result += f" - {abs(b)}"
    return result.strip() if result else '0.0'


def get_root(func: callable, a: float, b: float) -> float:
    """Compute the root of a function in a given interval.

    Args:
        func (callable): The function to evaluate.
        a (float): The start of the interval.
        b (float): The end of the interval.

    Returns:
        float: The root of the function in the interval.

    Examples:
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: x ** 2, 1, 3)
    2.99
    >>> get_root(lambda x: x ** 2, 7, 18)
    17.99
    """
    while (b - a) / 2 > 0.01:
        mid = (a + b) / 2
        if func(mid) == 0:
            return round(mid, 2)
        if func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
    return round((a + b) / 2, 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
