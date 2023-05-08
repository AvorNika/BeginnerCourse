# раздел 7.4 Цикл while, задание 13 Количество пятёрок
score = int(input())
total = 0
while 0 < score <= 5:
    if score == 5:
        total += 1
    score = int(input())
print(total)
