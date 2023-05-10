# раздел 13.5 Функции с возвратом значения, задание 9* Правильная скобочная последовательность
# объявление функции
def is_correct_bracket(text):
    s = []
    s_all = []
    text = text.replace('(', '1 ')
    text = text.replace(')', '-1 ')
    s = text.split(' ')
    while '' in s:
        del s[s.index('')]

    for i in range(len(s)):
        s_all.append(int(s[i]))
        if sum(s_all) < 0:
            return False

    if sum(s_all) == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
