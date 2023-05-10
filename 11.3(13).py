# раздел 11.3 Методы списков, задание 13** k-ая буква слова
n = int(input())
s = []
s1 = ''
for i in range(n):
    s += [input()]
k = int(input())
for j in range(len(s)):
    a = s[j]
    if len(a) < k:
        continue
    print(a[k - 1], end='')
