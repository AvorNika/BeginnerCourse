# раздел 7.5 Цикл while: обработка цифр числа, задание 8 Вторая цифра
num = int(input())
last_digit = 0
while num > 9:
    last_digit = num % 10
    num //= 10
print(last_digit)
