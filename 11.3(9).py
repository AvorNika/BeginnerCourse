# раздел 11.3 Методы списков, задание 9 Список кубов
n = int(input())
s = []
for i in range(n):
    a = int(input())
    b = a ** 3
    s += [b]
print(s)
