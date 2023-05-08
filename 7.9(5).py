# раздел 7.9 Вложенные циклы, задание 5 Цифровой корень
n = int(input())
total = 0
while n >= 10:
    total += n % 10
    n = n // 10 + n % 10
else:
    total = n
print(total)
