# раздел 7.5 Цикл while: обработка цифр числа, задание 7 Все вместе
num = int(input())
total = 0
sum = 0
prod = 1
srarif = 0
last_digit = num % 10
while num > 0:
    last_digit = num % 10
    total += last_digit
    sum += 1
    prod *= last_digit
    srarif = total / sum
    first_digit = last_digit
    num //= 10
print(total)
print(sum)
print(prod)
print(srarif)
print(first_digit)
print(first_digit + last_digit)
