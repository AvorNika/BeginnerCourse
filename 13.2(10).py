# раздел 13.2 Функции с параметрами, задание 10 Сумма цифр
# объявление функции
def print_digit_sum(num):
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num //= 10
    print(sum_)

# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)
