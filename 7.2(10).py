# раздел 7.2 Цикл for: функция range, задание 10 Последовательность чисел 4
m, n = int(input()), int(input())
for i in range(m, n+1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)
