# раздел 11.5 Методы строк: split, join, задание 4 Инициалы
s = input()
s = s.split()
for i in range(len(s)):
    a = s[i]
    print(a[0], end='.')
