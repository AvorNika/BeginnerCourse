# раздел 7.5 Цик while: обработка цифр числа, задание 6 max и min
n = int(input())
min_digit = 9
max_digit = 0
while n != 0:
    last_digit = n % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    n //= 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
