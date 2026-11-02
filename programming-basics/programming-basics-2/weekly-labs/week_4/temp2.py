row = [0, 1, 2, 1, 2, 0, 0, 1, 2]
ROW = {0, 1, 2}
for i in range(len(row) - 1):
    row = [list(ROW - {row[i], row[i + 1]})[0] if row[i] != row[i + 1] else row[i] for i in range(len(row) - 1)]
    print(row)
print(row[0])