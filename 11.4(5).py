# раздел 11.4 Вывод элементов списка, задание 5 Без дубликатов
n = int(input())
s = []
counter = 0
for i in range(n):
    a = input()
    if a not in s:
        s += [a]

print(*s, sep='\n')
