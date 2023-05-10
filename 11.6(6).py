# раздел 11.6 Методы списков, задание 6 Переставить min и max
s = input()
s2 = s.split()
for i in range(len(s2)):
    s2[i] = int(s2[i])

s_min = min(s2)
i_min = s2.index(s_min)
s_max = max(s2)
i_max = s2.index(s_max)
s2[i_min] = s_max
s2[i_max] = s_min
for j in s2:
    print(j, end=' ')
