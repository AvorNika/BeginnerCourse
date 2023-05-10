# раздел 9.4 Методы строк, задание 11 Количество цифр
s = input()
counter = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        counter += 1
print(counter)
