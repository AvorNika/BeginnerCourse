# раздел 4.3 Вложенные и каскадные условия, задание 5 Среднее число
a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
elif b < a < c or c < a < b:
    print(a)
    