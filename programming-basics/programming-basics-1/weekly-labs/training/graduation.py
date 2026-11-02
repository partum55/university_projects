def read_file(file_name: str) -> list[tuple[str, int, int]]:
    """

    :param file_name: name of file
    :return: list of tuples
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return [(name.strip(), int(age), int(sex.strip())) for line in file for name, age, sex in [line.split(',')]]


def guests_arrange(people: list[tuple[str, int, int]], n: int, m: int) -> dict[str, tuple[int, int]]:
    male = []
    female = []
    for i in people:
        if i[2] == 0:
            male.append(i)
        else:
            female.append(i)
    male = sorted(male, key = lambda x: x[1])
    female = sorted(female, key=lambda x: x[1])
    flag = True
    n_c = n
    m_c = 1
    dct = {}
    while male or female:
        if m_c == m + 1:
            m_c = 1
            n_c -= 1
            flag = not flag

        if flag:
            if male:
                p = male.pop(0)[0]
                dct[p] = n_c, m_c
                m_c += 1
                flag = False
            else:
                flag = False
                continue
        else:
            if female:
                p = female.pop(0)[0]
                dct[p] = n_c, m_c
                m_c += 1
                flag = True
            else:
                flag = True
                continue

    names = sorted(dct)
    with open ("guests_arrangement.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(f"{name}, {dct[name]}\n")
    return dct


if __name__ == "__main__":
    data = read_file("guests.txt")
    formatted = guests_arrange(data, 2, 3)
    print(formatted)
