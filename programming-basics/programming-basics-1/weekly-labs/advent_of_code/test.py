def strip_comments(strng, markers):
    strng = strng.split("\n")
    ans = []
    for row in strng:
        for i, el in enumerate(row):
            if el in markers:
                ans.append(row[:i].strip())
                break
        else:
            ans.append(row)
    return "\n".join(ans)


if __name__ == "__main__":
    print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))