# раздел 13.4 Функции с возвратом значения, задание 7 Количество дней
# объявление функции
def get_days(month):
    days = -1
    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        days = 31
    elif num == 4 or num == 6 or num == 9 or num == 11:
        days = 30
    else:
        days = 28
    return days

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
