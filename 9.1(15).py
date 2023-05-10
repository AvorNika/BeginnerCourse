# раздел 9.1 Индексация, задание 15 Decimal to Binary
n = int(input())
str2 = ''
counter = 0
while n > 0:
    str1 = str(n % 2)
    str2 += str1
    n //= 2
for i in range(-1, -len(str2)-1, -1):
    print(str2[i], end='')
