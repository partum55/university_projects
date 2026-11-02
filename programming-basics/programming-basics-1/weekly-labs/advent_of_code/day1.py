def first_part_day1(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        a = []
        b = []
        for line in file:
            line = line.strip().split()
            a.append(int(line[0]))
            b.append(int(line[-1]))
    all_dist = 0
    count = len(a)
    for _ in range(count):
        min_b = min(b)
        min_a = min(a)
        min_dist = abs(min_b - min_a)
        a.remove(min_a)
        b.remove(min_b)
        all_dist += min_dist
    return all_dist


def second_part_day1(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        a = []
        b = []
        for line in file:
            line = line.strip().split()
            a.append(int(line[0]))
            b.append(int(line[-1]))
    all_dist = 0
    for el in a:
        all_dist += el * b.count(el)
    return all_dist


if __name__ == "__main__":
    print(first_part_day1("input.txt"))
    print(second_part_day1("input.txt"))