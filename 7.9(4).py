# раздел 7.9 Вложенные циклы, задание 4 Делители-2
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', sep='', end='')
    print()
