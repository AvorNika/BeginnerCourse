# раздел 4.1 Выбор из двух, задание 6 Соотношение
abcd = int(input())
a = abcd // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if a+d == b-c:
    print('ДА')
else:
    print('НЕТ')
