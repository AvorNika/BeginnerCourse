# раздел 5.1 экзамен, задание 5 YES or NO вот в чём вопрос
digit = int(input())
if digit % 2 == 1:
    print('YES')
elif digit % 2 == 0 and 2 <= digit <= 5:
    print('NO')
elif digit % 2 == 0 and 6 <= digit <= 20:
    print('YES')
elif digit % 2 == 0 and digit > 20:
    print('NO')
