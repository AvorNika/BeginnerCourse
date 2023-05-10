# раздел 11.3 Методы списков, задание 12 Удалите нечётные индексы
n = int(input())
s = []
for i in range(n):
    s += [int(input())]
del s[1::2]
print(s)
