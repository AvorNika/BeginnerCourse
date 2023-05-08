# раздел 7.8 Вложенные циклы, задание 9 Численный треугольник 1
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end='')
    print()
