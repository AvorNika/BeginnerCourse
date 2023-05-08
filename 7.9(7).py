# раздел 7.9 Вложенные циклы, задание 7 Простые числа
a, b = int(input()), int(input())
for i in range(a, b + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag == True and i != 1:
        print(i)
