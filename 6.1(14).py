# раздел 6.1 Числовые типы данных, задание 14 Интересное число
a = int(input())
s = a // 100
d = (a % 100) // 10
e = a % 10
num1 = max(s, d, e)
num2 = min(s, d, e)
if num1-num2 == (s+d+e)-num1-num2:
    print('Число интересное')
else:
    print('Число неинтересное')
