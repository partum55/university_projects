a = 15
base = input()
substraction = 0
floor = 1
while a > 0:
    mid = input()
    for i in range(9):
        if base[i] != mid[i]:
            substraction += 0.5

    if substraction == 1:
        a -= 1
        base = mid
        floor += 1
    elif substraction == 2:
        a -= 2
        base = mid
        floor += 1
    elif substraction == 0:
        base = mid
        floor += 1
    else:
        a -= 3
print(floor)
