"""
calculate_expression_module.py

This module provides a function `calculate_expression` that processes simple arithmetic
expressions written in Ukrainian. It supports addition, subtraction, multiplication,
and division operations, parsing expressions in natural language.

Example expressions:
- "Скільки буде 8 відняти 3?"
- "Скільки буде 7 додати 3 помножити на 5?"
- "Скільки буде 10 поділити на -2 додати 11 мінус -3?"
"""

def calculate_expression(expression: str) -> int:
    """
    Evaluate simple arithmetic expressions in Ukrainian.

    This function takes a Ukrainian arithmetic question and computes the result.
    It recognizes operations such as addition, subtraction, multiplication, and division.
    It is designed to parse natural language expressions in the form of
    "Скільки буде X операція Y?", where X and Y are integers and "операція" can be one of
    "додати" (add), "відняти" (subtract), "помножити на" (multiply by), or "поділити на"
    (divide by). The function returns "Неправильний вираз!" if the expression is invalid.

    :param expression: A string containing an arithmetic expression in Ukrainian.
    :type expression: str
    :return: The result of the arithmetic expression, or an error message.
    :rtype: int or str

    Examples:
    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 7 додати 3 помножити на 5?')
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression('Скільки буде 3 в кубі?')
    'Неправильний вираз!'
    """
    expression = expression.split(" ")
    if expression[0] != "Скільки" or expression[1] != "буде" or\
    not "?" in expression[-1]:
        return "Неправильний вираз!"

    expression[-1] = expression[-1][:-1]
    expression = expression[2:]
    result = int(expression[0])

    while len(expression) != 1:
        try:
            if expression[1] in ["додати", "плюс"]:
                result += int(expression[2])
                expression = expression[2:]
            elif expression[1] in ["відняти", "мінус"]:
                result -= int(expression[2])
                expression = expression[2:]
            elif expression[1] == "помножити" and expression[2] == "на":
                result *= int(expression[3])
                expression = expression[3:]
            elif expression[1] == "поділити" and expression[2] == "на":
                result /= int(expression[3])
                expression = expression[3:]
            else:
                return "Неправильний вираз!"
        except (ValueError, IndexError, ZeroDivisionError):
            return "Неправильний вираз!"

    return int(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
