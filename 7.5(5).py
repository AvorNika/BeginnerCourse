# раздел 7.5 Цикл while: обработка цифр числа, задание 5 Обратный порядок 2
n = int(input())
while n != 0:
    last_digit = n % 10
    print(last_digit, end='')
    n //= 10
