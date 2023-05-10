# раздел 15.5 Шифр Цезаря
print('Вас приветствует программа "Шифр Цезаря"')
choice_1 = input('Введите номер желаемой процедуры, где 1 - шифрование, 2 - дешифрование:\n')
choice_2 = input('Выберите язык: (English/Русский)\n')
choice_3 = input('Укажите шаг сдвига:\n')
text_cesar = input('Введите текст для начала процедуры:\n')
new_text = ''


def latin_up(char_):
    a = ord(char_) + int(choice_3)
    if a > 90:
        a = 64 + (a - 90)
    return(chr(a))


def latin_low(char_):
    a = ord(char_) + int(choice_3)
    if a > 122:
        a = 96 + (a - 122)
    return (chr(a))


def cyrillic_up(char_):
    a = ord(char_) + int(choice_3)
    if a > 1071:
        a =1039 + (a - 1071)
    return (chr(a))


def cyrillic_low(char_):
    a = ord(char_) + int(choice_3)
    if a > 1103:
        a = 1071 + (a - 1103)
    return (chr(a))


def de_latin_up(char_):
    a = ord(char_) - int(choice_3)
    if a < 65:
        a = 90 - (64 - a)
    return(chr(a))


def de_latin_low(char_):
    a = ord(char_) - int(choice_3)
    if a < 97:
        a = 122 - (96 - a)
    return (chr(a))


def de_cyrillic_up(char_):
    a = ord(char_) - int(choice_3)
    if a < 1040:
        a =1071 - (1039 - a)
    return (chr(a))


def de_cyrillic_low(char_):
    a = ord(char_) - int(choice_3)
    if a < 1072:
        a = 1103 - (1071 - a)
    return (chr(a))


if choice_1 == '1':
    if choice_2.lower() == 'english' or choice_2.lower() == 'английский':
        for i in range(len(text_cesar)):
            if text_cesar[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_text += latin_up(text_cesar[i])
            elif text_cesar[i] in 'abcdefghigklmnopqrstuvwxyz':
                new_text += latin_low(text_cesar[i])
            else:
                new_text += text_cesar[i]

    elif choice_2.lower() == 'russian' or choice_2.lower() == 'русский':
        for i in range(len(text_cesar)):
            if text_cesar[i] in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                new_text += cyrillic_up(text_cesar[i])
            elif text_cesar[i] in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
                new_text += cyrillic_low(text_cesar[i])
            else:
                new_text += text_cesar[i]

    print('Зашифрованный текст:', new_text)


if choice_1 == '2':
    if choice_2.lower() == 'english' or choice_2.lower() == 'английский':
        for i in range(len(text_cesar)):
            if text_cesar[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_text += de_latin_up(text_cesar[i])
            elif text_cesar[i] in 'abcdefghigklmnopqrstuvwxyz':
                new_text += de_latin_low(text_cesar[i])
            else:
                new_text += text_cesar[i]

    elif choice_2.lower() == 'russian' or choice_2.lower() == 'русский':
        for i in range(len(text_cesar)):
            if text_cesar[i] in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                new_text += de_cyrillic_up(text_cesar[i])
            elif text_cesar[i] in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
                new_text += de_cyrillic_low(text_cesar[i])
            else:
                new_text += text_cesar[i]

    print('Дешифрованный текст:', new_text)
    