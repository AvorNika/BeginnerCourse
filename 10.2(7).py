# раздел 10.2 экзамен, задание 7 Каждый третий
s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')
