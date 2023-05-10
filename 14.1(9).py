# раздел 14.1 экзамен, задание 9 Магические даты
# объявление функции
def is_magic(date):
    s = date.split('.')
    if int(s[0]) * int(s[1]) == int(s[2]) % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
