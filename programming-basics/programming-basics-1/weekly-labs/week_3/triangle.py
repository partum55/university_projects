a, b = int(input()), int(input())
k = 0

for i in range(b):
    for j in range(b):
        if j == b-1:
            print(a+k, end = "")
        else:
            print(a+k, end = " ")
        k += 1
    print()
    b -= 1
    k = 0