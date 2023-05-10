# раздел 15.2 Числовая угадайка
import random

print('Добро пожаловать в цифровую угадайку!')


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= right_board


def function():
    global right_board
    global secret_num
    right_board = input('Введите, пожалуйста, число, обозначающее правую границу числового диапазона: ')
    right_board = int(right_board)
    secret_num = random.randint(1, right_board)
    counter = 0  # общее число попыток
    while True:
        user_num = input('Введите, пожалуйста, число от 1 до числа, указанного в качестве правой границы диапазона: ')
        counter += 1
        if is_valid(user_num) is False:
            print('А может быть всё-таки введём целое число от 1 до числа, указанного в качестве правой границы диапазона?')
        elif is_valid(user_num) is True:
            user_num = int(user_num)
            if user_num > secret_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif user_num < secret_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем! Общее количество попыток:', counter)
                break


def game():
    function()
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    answer = input('Хотите продолжить игру? (Да/Нет): ')
    if answer.lower() == 'Да':
        return True
    elif answer.lower() == 'Нет':
        print('До новых встреч!')
        return False
    else:
        input('Я не понимаю, что вы хотите сказать. Хотите продолжить игру? (Да/Нет): ')
        if answer.lower() == 'Да':
            return True
        elif answer.lower() == 'Нет':
            print('До новых встреч!')
            return False


while game() is True:
    game()
