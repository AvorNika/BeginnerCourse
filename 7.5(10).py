# раздел 7.5 Цикл while: обработка цифр числа, задание 10* Упорядоченные цифры
num = int(input())
flag = True
a = num % 10
while num != 0:
    b = num % 10
    if b < a:
        flag = False
    else:
        a = b
    num //= 10
if flag == True:
    print('YES')
else:
    print('NO')
