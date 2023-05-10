# раздел 13.6 Функции с возвратом значения, задание 5** Корни уравнения
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        xmax = max(x1, x2)
        xmin = min(x1, x2)
        return xmin, xmax
    elif d == 0:
        x = -b / (2 * a)
        return x, x

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
