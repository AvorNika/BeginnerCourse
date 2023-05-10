# раздел 8.2 экзамен, задание 6 Все вместе 2
n = int(input())
counter_3 = 0
last_digit_1 = n % 10
counter_last_digit = 0
counter_chet = 0
total_5 = 0
prod_7 = 1
counter_0_5 = 0
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        counter_3 += 1
    if last_digit == last_digit_1:
        counter_last_digit += 1
    if last_digit % 2 == 0:
        counter_chet += 1
    if last_digit > 5:
        total_5 += last_digit
    if last_digit > 7:
        prod_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        counter_0_5 += 1
    n //= 10
print(counter_3)
print(counter_last_digit)
print(counter_chet)
print(total_5)
print(prod_7)
print(counter_0_5)
