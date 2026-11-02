import math

radius = float(input())
hight = float(input())

volume = radius*radius*math.pi*hight
surface = ((2*radius*math.pi)*hight) + (2*(radius*radius*math.pi))

print(f'V = {volume:.3f}')
print(f'A = {surface:.3f}')