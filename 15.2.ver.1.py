# раздел 15.2 Числовая угадайка
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


import random
num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!')


def input_num():
    while True:
        digit_ = input('Пожалуйста, введите число от 1 до 100: ')
        if is_valid(digit_) is True:
            return int(digit_)
        else:
            print('А может быть всё-таки введём целое число от 1 до 100?')
            continue


def compare_num():
    while True:
        if input_num() < num:
            print('Ваше число меньше загаданного, попробуйте ещё разок')
        elif input_num() > num:
            print('Ваше число больше загаданного, попробуйте ещё разок')
        else:
            print('Вы угадали, поздравляем!')
            break


compare_num()
print()
print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')
