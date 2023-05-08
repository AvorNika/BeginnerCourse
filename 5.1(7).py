# раздел 5.1 экзамен, задание 7 Ход коня
line1, column1, line2, column2 = int(input()), int(input()), int(input()), int(input())
if line1-line2 == 2 and column1-column2 == 1:
    print('YES')
elif line1-line2 == 1 and column1-column2 == 2:
    print('YES')
elif line2-line1 == 1 and column2-column1 == 2:
    print('YES')
elif line2-line1 == 2 and column2-column1 == 1:
    print('YES')
elif line1-line2 == 1 and column2-column1 == 2:
    print('YES')
elif line2-line1 == 1 and column1-column2 == 2:
    print('YES')
elif line1-line2 == 2 and column2-column1 == 1:
    print('YES')
elif line2-line1 == 2 and column1-column2 == 1:
    print('YES')
else:
    print('NO')
