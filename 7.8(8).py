# раздел 7.8 Вложенные циклы, задание 8** Звёздный треугольник
n = int(input())
for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for k in range(n // 2, 0, -1):
    for g in range(k):
        print('*', end='')
    print()
