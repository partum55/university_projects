def count_words(file_path):
    with open (file_path, "r", encoding="utf-8") as file:
        data = [line.strip() for line in file]
    counter = 0
    new_data = ["" for _ in range(140)]
    for i in range(140):
        for j in range(140):
            new_data[i] += data[j][i]
    for line in data:
        counter += line.count("XMAS")
        counter += line.count("SAMX")
    for line in new_data:
        counter += line.count("XMAS")
        counter += line.count("SAMX")
    new_data = ["" for _ in range(279)]
    for i in range(140):
        for j in range(140-i):
            new_data[i] += data[j][j+i]
    for i in range(1, 140):
        for j in range(140-i):
            new_data[139+i] += data[j+1][j]
    for line in new_data:
        counter += line.count("XMAS")
        counter += line.count("SAMX")
    new_data = ["" for _ in range(279)]
    for i in range(140):
        data[i] = data[i][::-1]
    print(data)
    for i in range(140):
        for j in range(140-i):
            new_data[i] += data[j][j+i]
    for i in range(1, 140):
        for j in range(140-i):
            new_data[139+i] += data[j+1][j]
    for line in new_data:
        counter += line.count("XMAS")
        counter += line.count("SAMX")
    return counter


def find_word_in_matrix(matrix, word):
    n = len(matrix)
    word_len = len(word)
    count = 0

    def check_word(x, y, dx, dy, word):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or matrix[nx][ny] != word[i]:
                return False
        return True

    directions = [(1, 1), (1, -1)]

    # Find occurrences of the word "XMAS" and its reverse "SAMX"
    for i in range(n):
        for j in range(n):
            for dx, dy in directions:
                if check_word(i, j, dx, dy, word):
                    count += 1
                if check_word(i, j, dx, dy, word[::-1]):
                    count += 1

    return count


if __name__ == "__main__":
    with open ("input_4.txt", "r", encoding="utf-8") as file:
        data = [line.strip() for line in file]
    data = data[:-2]
    for i, line in enumerate(data):
        data[i] = line[:-2]
    a = find_word_in_matrix(data, "MAS")
    print(a)
