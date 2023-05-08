# раздел 7.3 Частые сценарии, задание 13** Наибольшие числа
n = int(input())
largest1 = 0
largest2 = 1
for num in range(1, n + 1):
    num = int(input())
    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num > largest2:
        largest2 = num
print(largest1)
print(largest2)
