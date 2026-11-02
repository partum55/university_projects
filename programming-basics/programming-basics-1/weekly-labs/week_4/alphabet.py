"""
    Author: Nazar Mykhailyshchuk
    Program to output the alphabet in triangle form
"""

first_char = 65
n = int(input())
k = 0
i = 1
temp = 0
ans = ""
ans2 = ""


while temp < n:
    temp += i
    i += 1
    k += 1

temp = 0

for i in range(1, k + 1):
    for j in range(i):
        if temp == (n + 64):
            break
        else:
            temp = first_char + j
            ans += " "
            ans += chr(temp)
    if i < k:
        print(f'{" " * ((k*2-1) - len(ans))}{ans}')
        ans = ""
        first_char += i
    else:
        for i in range(1, len(ans)):
            ans2 += ans[i]
        print(f"{ans2}")
print(k)
