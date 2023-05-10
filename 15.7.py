# раздел 15.7 Угадайка слов (виселица)
import random
word_list = ['ладонь', 'пылесос', 'король', 'зеркало', 'табурет', 'красота', 'волк', 'переход', 'желание', 'конфета', 'учитель', 'опушка', 'снежинка', 'силач', 'корабль', 'куртка', 'сказка', 'пирог', 'сахар', 'пряник', 'пирамида', 'дружба', 'рыба', 'телевизор', 'покрывало', 'секрет', 'тесто']


def get_word():
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
                ''',
                # голова и торс
                '''
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                ''',
                # голова
                '''
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                ''',
                # начальное состояние
                '''
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                '''
    ]
    return stages[tries]


def play():
    unknown_word = get_word()
    word_comletion = list('_' * len(unknown_word))   # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []   # список уже названных букв
    guessed_words = []   # список уже названных слов
    tries = 6   # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print('Загаданное слово:', *word_comletion, '(', len(unknown_word), 'букв )')
    print('Количество оставшихся попыток:', tries)

    while tries > 0:
        user_char = input('Введите букву или слово целиком:\n')
        if len(user_char) == 1:
            if user_char.upper() in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                if user_char.upper() not in guessed_letters:
                    guessed_letters += user_char.upper()
                    if user_char.upper() not in unknown_word:
                        tries -= 1
                        print(display_hangman(tries))
                        print('Загаданное слово:', *word_comletion, '(', len(unknown_word), 'букв )')
                        print('Такой буквы нет в загаданном слове, попробуйте другую.')
                        print('Количество оставшихся попыток:', tries)
                        print('Ранее введённые буквы:', guessed_letters)
                        print('Ранее введённые слова:', guessed_words)
                    else:
                        for i in range(len(unknown_word)):
                            if unknown_word[i] == user_char.upper():
                                word_comletion[i] = user_char.upper()
                        print(display_hangman(tries))
                        print('Загаданное слово:', *word_comletion, '(', len(unknown_word), 'букв )')
                        print('Количество оставшихся попыток:', tries)
                        print('Ранее введённые буквы:', guessed_letters)
                        print('Ранее введённые слова:', guessed_words)
                        if '_' in word_comletion:
                            continue
                        else:
                            print(display_hangman(tries))
                            print('Вы отгадали слово! Поздравляем!')
                            print(unknown_word)
                            print('Количество совершённых попыток:', tries)
                            print('Введённые буквы:', guessed_letters)
                            print('Введённые слова:', guessed_words)
                            break
                else:
                    print('Вы уже пытались вводить эту букву ранее. Попробуйте другую.')
            else:
                print('Необходимо ввести букву или слово целиком, попробуйте ещё раз.')
        else:
            counter = 0
            for i in range(len(user_char)):
                if user_char.upper()[i] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                    counter += 1
                else:
                    break
            if counter == int(len(user_char)):
                if user_char.upper() not in guessed_words:
                    guessed_words.append(user_char.upper())
                    if user_char.upper() == unknown_word:
                        print(display_hangman(tries))
                        print('Вы отгадали слово! Поздравляем!')
                        print(unknown_word)
                        print('Количество совершённых попыток:', tries)
                        print('Введённые буквы:', guessed_letters)
                        print('Введённые слова:', guessed_words)
                        break
                    else:
                        tries -= 1
                        print(display_hangman(tries))
                        print('Загаданное слово:', *word_comletion, '(', len(unknown_word), 'букв )')
                        print('Введённое слово не совпадает с загаданным, попробуйте ещё раз.')
                        print('Количество оставшихся попыток:', tries)
                        print('Ранее введённые буквы:', guessed_letters)
                        print('Ранее введённые слова:', guessed_words)
                else:
                     print('Вы уже пытались вводить это слово ранее. Попробуйте другое.')
            else:
                print('Необходимо ввести букву или слово целиком, попробуйте ещё раз.')
    else:
        print('Попыток больше нет. Загаданное слово -', unknown_word)


play()
while True:
    question = input('Хотите продолжить игру? (Да/Нет)\n')
    if question.lower() == 'да':
        play()
    elif question.lower() == 'нет':
        print('Спасибо за игру!')
        break
    else:
        input('Я не понимаю, что вы хотите сказать. Введите Да или Нет:\n')
