# раздел 7.5 Цикл while: обработка цифр числа, задание 9 Одинаковые цифры
num = int(input())
flag = True
a = num % 10
while num != 0:
    b = num % 10
    if a != b:
        flag = False
    num //= 10
if flag == False:
    print('NO')
else:
    print('YES')
