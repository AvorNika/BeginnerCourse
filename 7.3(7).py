# раздел 7.3 Частые сценарии, задание 7 Асимптотическое приближение
from math import *
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total-log(n))
