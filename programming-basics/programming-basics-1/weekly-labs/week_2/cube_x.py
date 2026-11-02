import math

# input
a, b, c, d = (float(input()), float(input()), float(input()), float(input()))
x = 0

# test
# a, b, c, d = 1, 0, 0, 8

# main part
part_0 = b/(3*a)
part_1 = (-(part_0 * part_0 * part_0))+((b*c) / (6* a ** 2))-(d/(2*a))
part_2 = (c / (3 * a)) - (part_0 ** 2)
x = (math.cbrt(part_1 + (math.sqrt(((part_1 ** 2) + (part_2 ** 3)))))) + (math.cbrt(part_1 - (math.sqrt(((part_1 ** 2) + (part_2 ** 3)))))) - part_0

# output
print(f"x = {x:.2f}")