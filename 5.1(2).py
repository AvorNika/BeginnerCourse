# раздел 5.1 экзамен, задание 2 Шахматная доска
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1 % 2 == 1 and b1 % 2 == 1 and a2 % 2 == 0 and b2 % 2 == 0) or (a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 == 1 and b2 % 2 == 1) or (a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 == 0 and b2 % 2 == 0) or (a1 % 2 == 1 and b1 % 2 == 1 and a2 % 2 == 1 and b2 % 2 == 1):
    print('YES')
elif (a1 % 2 == 1 and b1 % 2 == 0 or a1 % 2 == 0 and b1 % 2 == 1) and (a2 % 2 == 1 and b2 % 2 == 0 or a2 % 2 == 0 and b2 % 2 == 1):
    print('YES')
else:
    print('NO')
