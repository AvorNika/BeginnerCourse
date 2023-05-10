# раздел 9.6 Строки в памяти компьютера, задание 6* Шифр Цезаря
n, s = int(input()), input()
for i in range(len(s)):
    a = ord(s[i]) - n
    if a < 97:
        a = 122 - (96 - a)
    print(chr(a), end='')
