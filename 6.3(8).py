# раздел 6.3 Модуль math, задание 8 Правильный многоугольник
n, a = float(input()), float(input())
from math import *
s = (n * a ** 2) / (4 * tan(pi/n))
print(s)
