# раздел 6.2 Строковый тип данных, задание 14 Корректный email
email = str(input())
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')
