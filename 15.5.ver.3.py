# раздел 15.5 Шифр Цезаря
eng = [chr(i) for i in range(97, 123)]
rus = [chr(i) for i in range(1072, 1104)]
lang_keys = {'language': ['английский', 'русский'],
             'max_key': [25, 31],
             'abc': [eng, rus]}

print('- ' * 30)
print('Добро пожаловать в "Шифр Цезаря".')
print('Данная программа шифрует и дешифрует текст алгоритмом Цезаря.')
print('- ' * 30)


def check_0_1(message):
    while True:
        print(message)
        d = input()
        if d == '0' or d == '1':
            print()
            break
        print('ОШИБКА: можно вводить только 0 или 1.\n')
    return int(d)


def encryption(text_in, abc, key):
    text_out = ''
    for c in text_in:
        if c in abc:
            text_out += abc[(abc.index(c) + key) % len(abc)]
        elif c.lower() in abc:
            text_out += abc[(abc.index(c.lower()) + key) % len(abc)].upper()
        else:
            text_out += c
    return text_out


def decryption(text_in, abc, key):
    text_out = ''
    for c in text_in:
        if c in abc:
            text_out += abc[(abc.index(c) - key) % len(abc)]
        elif c.lower() in abc:
            text_out += abc[(abc.index(c.lower()) - key) % len(abc)].upper()
        else:
            text_out += c
    return text_out


def main_menu():
    process = check_0_1('Введите 0, если хотите зашифровать текст. Введите 1, если хотите дешифровать текст.')
    lang = check_0_1('Введите 0 для выбора английского алфавита. Введите 1 для выбора русского алфавита.')
    if process == 0:
        encryption_menu(lang)
    else:
        decryption_menu(lang)


def encryption_menu(lang):
    print(f"Введите целое число от 1 до {lang_keys['max_key'][lang]}, которое будет ключом при шифровании текста.")
    while True:
        try:
            key = int(input())
            if 1 <= key <= lang_keys['max_key'][lang]:
                break
            else:
                print(f"ОШИБКА: можно вводить только числа от 1 до {lang_keys['max_key'][lang]}.\n")
        except:
            print('ОШИБКА: можно вводить только натуральные числа.\n')
    print()
    print(f"Введите текст, который нужно зашифровать. Язык текста должен быть {lang_keys['language'][lang]}.")
    text_input = input()
    text_output = encryption(text_input, lang_keys['abc'][lang], key)
    print()
    print('Текст зашифрован:')
    print('-  ' * 20 + '>')
    print(text_output)
    print('-  ' * 20 + '>')


def decryption_menu(lang):
    print(
        f"Введите целое число от 1 до {lang_keys['max_key'][lang]}, которое является ключом расшифровки. Если ключ неизвествен, просто нажмите Enter.")
    while True:
        key = input()
        if key.isdigit() and 1 <= int(key) <= lang_keys['max_key'][lang]:
            key = int(key)
            break
        elif key == '':
            break
        else:
            print(
                f"ОШИБКА: можно вводить только целые числа от 1 до {lang_keys['max_key'][lang]} или оставлять поле пустым.\n")
    print()
    print(f"Введите текст, который нужно расшифровать. Язык текста должен быть {lang_keys['language'][lang]}.")
    text_input = input()
    if key == '':
        flag = True
        print()
        print('Сейчас будут производиться попытки подбора ключа')
        if len(text_input) > 10:
            for i in range(1, 32):
                text_output = decryption(text_input[:11], lang_keys['abc'][lang], i)
                print('-  ' * 5)
                print(text_output)
                print('-  ' * 5)
                if check_0_1(
                        'Проверьте, сможете ли Вы прочитать данный отрывок и введите 0, если нет, и 1, если да.') == 1:
                    key = i
                    break
        else:
            for i in range(1, 32):
                text_output = decryption(text_input, lang_keys['abc'][lang], i)
                print('-  ' * 5)
                print(text_output)
                print('-  ' * 5)
                if check_0_1(
                        'Проверьте, сможете ли Вы прочитать данный текст и введите 0, если нет, и 1, если да.') == 1:
                    key = i
                    break
    text_output = decryption(text_input, lang_keys['abc'][lang], key)
    print()
    if flag:
        print(f'Значение ключа: {key}')
    print('Текст расшифрован:')
    print('-  ' * 20 + '>')
    print(text_output)
    print('-  ' * 20 + '>')


main_menu()
