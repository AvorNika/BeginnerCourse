# раздел 8.2 экзамен, задание 4 Звёздная рамка
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19)
    else:
        print('*', '               ', '*')
