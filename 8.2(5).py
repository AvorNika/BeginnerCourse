# раздел 8.2 экзамен, задание 5 Третья цифра
n = int(input())
while n > 1000:
    n //= 10
else:
    print(n % 10)
