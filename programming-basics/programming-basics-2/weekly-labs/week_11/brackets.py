"""Brackets"""

from collections import deque

opening = {'(': ')', '[': ']', '{': '}', '<': '>'}
closing = {v: k for k, v in opening.items()}

def read_file(filename):
    """Read file and return list of lines"""
    with open(filename, encoding='utf-8') as f:
        return [line.strip() for line in f]

def review_brackets(lines):
    """
    Fix brackets and calculate total compensation

    :param lines: list of strings with brackets
    :return: (total_cents, list of corrected strings)
    """
    def check(line):
        """Temp"""
        stack = deque()
        for i, char in enumerate(line):
            if char in opening:
                stack.append((char, i))
            elif char in closing:
                if not stack:
                    return True, 'insert_open', None, closing[char]
                top, _ = stack[-1]
                if opening[top] != char:
                    return True, 'replace', i, opening[top]
                stack.pop()
        if stack:
            last_unclosed, _ = stack[-1]
            return True, 'insert_close', None, opening[last_unclosed]
        return False, None, None, None

    def fix(line):
        """Temp"""
        total = 0
        cost = 1
        while True:
            has_error, action, index, char = check(line)
            if not has_error:
                break
            if action == 'insert_open':
                line = char + line
            elif action == 'insert_close':
                line = line + char
            elif action == 'replace' and index is not None:
                line = line[:index] + char + line[index + 1:]
            total += cost
            cost *= 2
        return line, total

    fixed_lines = []
    total_cents = 0
    for line in lines:
        fixed, earned = fix(line)
        fixed_lines.append(fixed)
        total_cents += earned
    return total_cents, fixed_lines

def write_correct_lines(lines, filename):
    """Write corrected lines to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')
