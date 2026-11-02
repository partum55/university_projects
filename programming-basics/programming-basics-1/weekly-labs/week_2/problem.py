import scipy.constants as sc
from math import *

m = float(input())
v = float(input())

m_r = m/(sqrt(1 - (pow(v, 2)/pow(sc.c, 2))))
result = m*(sc.c**2)

print(f'{result}') 