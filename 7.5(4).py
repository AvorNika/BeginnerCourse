# раздел 7.5 Цикл while: обработка цифр числа, задание 4 Обратный порядок 1
n = int(input())
while n != 0:
    last_digit = n % 10
    print(last_digit)
    n //= 10
