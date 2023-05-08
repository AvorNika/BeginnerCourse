# раздел 7.3 Частые сценарии, задание 5 Количество чисел
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)
