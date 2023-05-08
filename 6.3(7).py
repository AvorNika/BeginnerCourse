# раздел 6.3 Модуль math, задание 7** Квадратное уравнение
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    xmax = max(x1, x2)
    xmin = min(x1, x2)
    print(xmin)
    print(xmax)
elif d == 0:
    x = -b / (2 * a)
    print(x)
elif d < 0:
    print('Нет корней')
    