# раздел 11.7 Списочные выражения, задание 7 Списочное выражение 1
numbers = [i ** 2 for i in range(1, int(input()) + 1)]
print(*numbers, sep='\n')
