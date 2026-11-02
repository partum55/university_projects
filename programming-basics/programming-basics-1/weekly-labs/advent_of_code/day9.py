def main(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.read().strip()
    temp_str = ""
    curr = 0
    for i, el in enumerate(data):
        if i % 2 == 0:
            temp_str += str(curr) * int(el)
            curr += 1
        else:
            temp_str += "." * int(el)
    res_str = ""
    copy_str = temp_str.replace(".", "")
    length = len(copy_str)
    for i in range(length):
        temp_str = temp_str.strip(".")
        if temp_str[i] != ".":
            res_str += temp_str[i]
        else:
            res_str += temp_str[-1]
            temp_str = temp_str[:-1]
    res = 0
    for i, el in enumerate(res_str):
        res += i * int(el)
    return res


if __name__ == "__main__":
    print(main("input_test.txt"))
    print(main("input_9.txt"))
    print(0)
