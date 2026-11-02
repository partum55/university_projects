a = []

with open("keywords_updated.list", "r", encoding="iso-8859-1") as textfile1, open("keywords_updated_d.list", "r", encoding="iso-8859-1") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()
        if x != y:
            a.append(f"{x} -> {y}")

with open("result_checker.csv", "w", encoding="utf-8") as file:
    for line in a:
        file.write(a + "\n")