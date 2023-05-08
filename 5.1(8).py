# раздел 5.1 экзамен, задание 8 Ход ферзя
line1, column1, line2, column2 = int(input()), int(input()), int(input()), int(input())
if line1-line2 == column1-column2 or line2-line1 == column2-column1 or line1-line2 == column2-column1 or line2-line1 == column1-column2:
    print('YES')
elif line1 == line2 or column1 == column2:
    print('YES')
else:
    print('NO')
