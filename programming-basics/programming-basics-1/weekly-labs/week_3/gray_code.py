a = input()

bit_len = len(a)
a = int(a, 2)
a = a ^ (a >> 1)

print(f"{a:0{bit_len}b}")