# раздел 13.5 Функции с возвратом значения, задание 7* Палиндром
# объявление функции
def is_palindrome(text):
    text = text.lower()
    s = []
    s1 = []
    for i in range(len(text)):
        if text[i] in 'abcdefghigklmnopqrstuvwxyz' or text[i] in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            s += text[i]
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
