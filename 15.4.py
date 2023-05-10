# раздел 15.4 Генератор безопасных паролей
from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghigklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
new_chars = ''


count_password = input('Какое количество паролей необходимо сгенерировать?\n')
while True:
    if count_password == int(count_password):
        count_password = int(count_password)
    else:
        print('Для работы программы необходимо ввести целое число.')
        input('Какое количество паролей необходимо сгенерировать?\nВведите целое число: ')


len_password = input('Какой длины должен быть пароль?\n')
while True:
    if len_password.isdigit() is not True:
        print('Для работы программы необходимо ввести целое число.')
        input('Какой длины должен быть пароль?\nВведите целое число: ')
    len_password = int(len_password)


digit_password = input('Включить в пароль цифры 0123456789? (Да/Нет)\n')
if digit_password.lower() == 'да' or digit_password.lower() == 'yes':
    chars += digits
print(chars)


up_letter_password = input('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Да/Нет)\n')
if up_letter_password.lower() == 'да' or up_letter_password.lower() == 'yes':
    chars += uppercase_letters
print(chars)


low_letter_password = input('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz? (Да/Нет)\n')
if low_letter_password.lower() == 'да' or low_letter_password.lower() == 'yes':
    chars += lowercase_letters
print(chars)


punctuation_password = input('Включить в пароль символы "!#$%&*+-=?@^_"? (Да/Нет)\n')
if punctuation_password.lower() == 'да' or punctuation_password.lower() == 'yes':
    chars += punctuation
print(chars)


other_letter_password = input('Исключить из пароля неоднозначные символы il1Lo0O? (Да/Нет)\n')
if other_letter_password.lower() == 'да' or other_letter_password.lower() == 'yes':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            new_chars += chars[i]
print(new_chars)


def generate_password(length, chars):
    return sample(chars, length)

