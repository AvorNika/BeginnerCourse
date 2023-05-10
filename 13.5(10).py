# раздел 13.5 Функции с возвратом значения, задание 10 Змеиный регистр
# объявление функции
def convert_to_python_case(text):
    s = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper():
            s = s + '_' + text[i].lower()
        else:
            s += text[i]
    return s

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
