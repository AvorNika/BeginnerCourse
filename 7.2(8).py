# раздел 7.2 Цикл for: функция range, задание 8* Последовательность чисел 2
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
elif m == n:
    print(m)
