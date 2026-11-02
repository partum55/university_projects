import math

# input
x, y, z = (float(input()), float(input()), float(input())) #(x, μ, σ)

# test
# x, y, z = 1, 0, 1

# main
power = - (((x-y) * (x-y))/(2 * (z * z)))
result = (1 / (math.sqrt(2 * math.pi * (z * z)))) * (math.e ** power)

# output
print(f"{result:.10f}")