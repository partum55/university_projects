"""
Word Navigation Module
======================

This module provides functionality to read and follow instructions from a file, specifically navigating through a series of commands based on given directions. The primary goal is to determine the number of steps required to reach a certain endpoint.

Global Constants:
-----------------
FIRST_KEY : str
    The starting key in the sequence.
LAST_KEY : str
    The ending key in the sequence.

Functions:
----------
read_file(filename: str) -> tuple[str, dict[str, tuple[str, str]]]
    Reads instructions and commands from a file.

follow_instructions(instructions: str, commands: dict[str, tuple[str, str]]) -> int
    Follows the given instructions and counts the steps until the last key is reached.
"""

FIRST_KEY = "AAA"
LAST_KEY = "ZZZ"

def read_file(filename: str) -> tuple[str, dict[str, tuple[str, str]]]:
    """
    Reads instructions and commands from a file.

    :param filename: The name of the file to read from.
    :type filename: str
    :return: A tuple containing the instruction string and a dictionary of commands.
    :rtype: tuple[str, dict[str, tuple[str, str]]]

    Example:
    >>> import tempfile
    >>> inf = "LLR\\n\\nAAA = (BBB, BBB)\\nBBB = (AAA, ZZZ)\\nZZZ = (ZZZ, ZZZ)"
    >>> with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmpfile:
    ...     _ = tmpfile.write(inf)
    >>> read_file(tmpfile.name) == ('LLR', {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')})
    True
    """
    with open(filename, "r", encoding="utf-8") as file:
        instruction = file.readline().strip()
        commands = {}
        for line in file:
            line = line.strip()
            if not line:
                continue

            left, right = line.split(" = ")
            right = right[1:-1].split(", ")
            commands[left] = tuple(right)
        return instruction, commands

def follow_instructions(instructions: str, commands: dict[str, tuple[str, str]]) -> int:
    """
    Follows the given instructions and counts the steps until the last key is reached.

    :param instructions: The instructions to follow.
    :type instructions: str
    :param commands: The commands dictionary containing movements.
    :type commands: dict[str, tuple[str, str]]
    :return: The number of steps taken to reach the last key.
    :rtype: int

    Example:
    >>> steps = 'LLR'
    >>> moves = {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')}
    >>> follow_instructions(steps, moves)
    6
    """
    instructions_number = 0
    len_instructions = len(instructions)
    current_symbol = FIRST_KEY

    while current_symbol != LAST_KEY:
        current_instraction = instructions[instructions_number % len_instructions]
        current_symbol = commands[current_symbol][0] if \
            current_instraction == "L" else commands[current_symbol][1]
        instructions_number += 1

    return instructions_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()
