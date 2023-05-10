# раздел 11.6 Методы списков, задание 8* Взлом Братства Стали
s_n = input()  # количество строк программы
n = s_n[1:]  # убираем знак #
n = int(n)  # преобразуем в число
s = []
for i in range(n):
    str_prog = input()
    if '#' in str_prog:
        str_prog = str_prog[:str_prog.index('#')]
        print(str_prog.rstrip())

    else:
        print(str_prog)
        