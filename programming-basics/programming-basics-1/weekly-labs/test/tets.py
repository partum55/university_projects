def top_3_words(text):
    new_text = ""
    for i in text:
        if i.isalpha() or i in [" ", "'"]:
            new_text += i.lower()
    new_text = new_text.split()
    new_text = sorted(new_text, key=lambda x: new_text.count(x), reverse=True)
    n = 0
    i = 0
    res = []
    while n < 3 and i < len(new_text):
        if all(s == "'" for s in new_text[i]):
            i += 1
            continue
        if new_text[i] not in res:
            res.append(new_text[i])
            n += 1
        i += 1
    return res


if __name__ == "__main__":
    a = "In a village of La Mancha, the name of which I have no desire to call tomind, there lived not long since one of those gentlemen that keep a lancein the lance-rack, an old buckler, a lean hack, and a greyhound forcoursing. An olla of rather more beef than mutton, a salad on mostnights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extraon Sundays, made away with three-quarters of his income."
    print(top_3_words("  //wont won't won't "))
