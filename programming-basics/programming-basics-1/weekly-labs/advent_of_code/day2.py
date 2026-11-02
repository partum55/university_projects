def check_all(file_path):
    codes = [list(map(int, line.strip().split())) for line in open(file_path, "r", encoding="utf-8")]
    counter = 0
    for i in codes:
        if ((all(i[j - 1] < i[j] for j in range(1, len(i))) or all(i[j - 1] > i[j] for j in range(1, len(i)))) and
                all(abs(i[j] - i[j - 1]) in {1, 2, 3 } for j in range(1, len(i)))):
            counter += 1
    return counter


def check_safe_2(file_path):
    codes = [list(map(int, line.strip().split())) for line in open(file_path, "r", encoding="utf-8")]
    counter = 0
    for i in codes:
        if ((all(i[j - 1] < i[j] for j in range(1, len(i))) or all(i[j - 1] > i[j] for j in range(1, len(i)))) and
                all(abs(i[j] - i[j - 1]) in {1, 2, 3} for j in range(1, len(i)))):
            counter += 1
        else:
            for k in i:
                temp = i[:]
                temp.remove(k)
                if ((all(temp[j - 1] < temp[j] for j in range(1, len(temp))) or all(temp[j - 1] > temp[j] for j in range(1, len(temp)))) and
                        all(abs(temp[j] - temp[j - 1]) in {1, 2, 3} for j in range(1, len(temp)))):
                    counter += 1
                    break
    return counter


if __name__ == "__main__":
    print(check_all("input_2.txt"))
    print(check_safe_2("input_2.txt"))
