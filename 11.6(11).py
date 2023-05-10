# раздел 11.6 Методы списков, задание 11 Сортировка чисел
s = input()
s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)
