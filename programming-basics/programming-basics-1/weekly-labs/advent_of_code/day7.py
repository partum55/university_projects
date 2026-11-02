from itertools import product


def read_file(file_path: str) -> dict[int, list[int]]:
    with open(file_path, "r", encoding="utf-8") as file:
        res = {}
        for i in file:
            i = i.strip().split(":")
            res[int(i[0])] = [int(j) for j in i[1].split()]
    return res


def is_valid(number: int, numbers: list[int]) -> bool:
    operators = ["+", "*", "||"]
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    for ops in operator_combinations:
        result = numbers[0]
        for num, op in zip(numbers[1:], ops):
            if op == "||":
                result = int(str(result) + str(num))
            elif op == "+":
                result += num
            elif op == "*":
                result *= num
        if result == number:
            return True
    return False


def main(check: dict[int, list[int]]) -> int:
    k = 0
    for i, nums in check.items():
        if is_valid(i, nums):
            k += i
    return k


if __name__ == "__main__":
    numbers_to_check = read_file("input_7.txt")
    print(main(numbers_to_check))
