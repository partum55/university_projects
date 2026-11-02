n = int(input())

if n == 1:
    print("*")
elif n == 2:
    print("*")
    print("**")
else:
    print("*")
    print("**")
    for i in range (3, (n)):
        print(f"*{" " * (i - 2)}*")
    print("*" * n)