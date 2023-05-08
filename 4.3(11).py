# раздел 4.3 Вложенные и каскадные условия, задание 11** Пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
amax = max(a1, a2)
bmin = min(b1, b2)
if a1 == b2 and b1 != a2:
    print(a1)
elif a2 == b1 and b2 != a1:
    print(a2)
elif a1 <= a2 <= b1 or a2 <= a1 <= b2:
    print(amax, bmin)
else:
    print('пустое множество')
