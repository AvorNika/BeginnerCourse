# раздел 6.3 Модуль math, задание 5 Тригонометрическое выражение
from math import *
x = float(input())
r = radians(x)
y = sin(r) + cos(r) + pow(tan(r), 2)
print(y)
