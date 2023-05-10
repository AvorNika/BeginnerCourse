# раздел 12.2 экзамен, задание 1 Список чётных
n = int(input())
s = []
for i in range(2, n + 1, 2):
    s += [i]
print(s)
