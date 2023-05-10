# раздел 9.4 Методы строк, задание 10 Очень странные дела
n = int(input())
counter = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        counter += 1
print(counter)
