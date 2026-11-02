n = 2 * int(input())

for i in range(1, n+1):
    if  i%2 == 1:
        print(i, end = "")
        print("/", end = "")
    elif i == n:
        print(i)
    elif (i/2)%2 == 1:
        print(i, "- ", end = "")
    elif (i/2)%2 == 0:
        print(i, "+ ", end = "")