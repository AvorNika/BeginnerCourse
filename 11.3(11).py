# раздел 11.3 Методы списков, задание 11 Сумма двух
n = int(input())
s = []
s1 = []
for i in range(n):
    s += [int(input())]
    s1 += [s[i - 1] + s[i]]
del s1[0]
print(s1)
