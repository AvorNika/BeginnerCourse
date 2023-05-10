# раздел 11.7 Списочные выражения, задание 8 Списочное выражение 2
numbers = [int(i) ** 3 for i in input().split()]
for i in range(len(numbers)):
    print(numbers[i], end=' ')
    