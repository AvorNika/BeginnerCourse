# раздел 14.1 экзамен, задание 8 Искомый месяц
# объявление функции
def get_month(language, number):
    month_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return month_ru[number]
    else:
        return month_en[number]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
