# раздел 7.9 Вложенные циклы, задание 1 Численный треугольник 3
n = int(input())
total = 0
for i in range(1, n + 1):
    for j in range(i):
        total += 1
        print(total, end=' ')
    print()
