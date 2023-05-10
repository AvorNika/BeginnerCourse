# раздел 9.4 Методы строк, задание 13 Самый частотный символ
s = input()
amax = 0
n = 0
for i in range(len(s)):
    if s.count(s[i]) >= amax:
        amax = s.count(s[i])
        n = s[i]
print(n)
