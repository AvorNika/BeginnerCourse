# раздел 7.9 Вложенные циклы, задание 2 Численный треугольник 4
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()
