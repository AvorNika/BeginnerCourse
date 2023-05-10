# раздел 11.4 Вывод элементов списка, задание 3 Значение функции
n = int(input())
s1 = []
s2 = []

for i in range(n):
    x = int(input())
    s1 += [x]
    s2 += [x * x + 2 * x + 1]

print(*s1, sep='\n')
print()
print(*s2, sep='\n')
