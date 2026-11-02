import time as t

a, b, c = 3, 4 ,5

for i in range(3, 10000):
    if (a ** i + b ** i) == c ** i:
        print(i)
        break