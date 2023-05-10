# раздел 11.5 Методы строк: split, join, задание 6 Диаграмма
s = input()
s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
    print(s[i] * '+')
