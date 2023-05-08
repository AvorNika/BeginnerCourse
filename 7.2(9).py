# раздел 7.2 Цикл for: функция range, задание 9* Последовательность чисел 3
m, n = int(input()), int(input())
if m % 2 == 0 and n % 2 == 0:
    for i in range(m-1, n, -2):
        print(i)
elif m % 2 == 1 and n % 2 == 1:
    for i in range(m, n-1, -2):
        print(i)
elif m % 2 == 1 and n % 2 == 0:
    for i in range(m, n, -2):
        print(i)
elif m % 2 == 0 and n % 2 == 1:
    for i in range(m-1, n-1, -2):
        print(i)
        