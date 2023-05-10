# раздел 11.3 Методы списков, задание 8 Алфавит
s = 'abcdefghijklmnopqrstuvwxyz'
s1 = []
for i in range(len(s)):
    a = s[i] * (i + 1)
    s1 += [a]
print(s1)
