# раздел 9.3 Методы строк, задание 11 Нижний регистр
s = input()
s1 = s.upper()
counter = 0
for i in range(len(s)):
    if s[i] != s1[i]:
        counter += 1
print(counter)
