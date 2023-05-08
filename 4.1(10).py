# раздел 4.1 Выбор из двух, задание 10* Наименьшее из четырёх чисел
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    min1 = a
else:
    min1 = b
if c < d:
    min2 = c
else:
    min2 = d
if min1 < min2:
    min_ = min1
else:
    min_ = min2
print(min_)
