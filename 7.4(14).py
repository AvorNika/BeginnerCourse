# раздел 7.4 Цикл while, задание 14 Ведьмаку заплатите чеканной монетой
n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n -= 25
while 10 <= n < 25:
    counter += 1
    n -= 10
while 5 <= n < 10:
    counter += 1
    n -= 5
while 0 < n < 5:
    counter += n
    n = 0
print(counter)
