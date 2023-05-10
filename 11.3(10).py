# раздел 11.3 Методы списков, задание 10 Список делителей
n = int(input())
s = []
for i in range(1, n + 1):
    if n % i == 0:
        s += [i]
print(s)
