# раздел 11.5 Методы строк: split, join, задание 8 Добавь разделитель
s = input()
a = input()
s1 = []
for i in range(len(s)):
    s1 += s[i]
s1 = a.join(s1)
print(s1)
