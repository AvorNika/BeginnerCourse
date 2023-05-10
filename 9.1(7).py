# раздел 9.1 Индексация, задание 7 В столбик 1
s = input()
for i in range(len(s)):
    if i == 0 or i % 2 == 0:
        print(s[i])
