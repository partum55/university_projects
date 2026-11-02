import math

num = float(input())

cosh = math.cosh(num)
exp = (math.exp(num)+((math.exp(num))**-1))/2
e = ((math.e**num)+(math.e**(0-num)))/2

print(f'COS = {cosh:.4f}')
print(f'EXP = {exp:.4f}')
print(f'E = {e:.4f}')