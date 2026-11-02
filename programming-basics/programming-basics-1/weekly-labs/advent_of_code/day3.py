import re


def multiplying(file_path):
    with open (file_path, "r", encoding="utf-8") as file:
        data = file.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    results = 0
    for x, y in matches:
        results += int(x) * int(y)
    return results


def pro_multiplying(file_path):
    with open (file_path, "r", encoding="utf-8") as file:
        data = file.read()
    total = 0
    is_enabled = True
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    components = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", data)
    for component in components:
        if re.match(do_pattern, component):
            is_enabled = True
        elif re.match(dont_pattern, component):
            is_enabled = False
        elif re.match(mul_pattern, component):
            if is_enabled:
                x, y = map(int, re.findall(r"\d{1,3}", component))
                total += x * y
    return total


if __name__ == "__main__":
    print(multiplying("input_3.txt"))
    print(pro_multiplying("input_3.txt"))
