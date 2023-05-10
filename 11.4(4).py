# раздел 11.4 Вывод элементов списка, задание 4 Remove outliers
n = int(input())
s = []
j_min = n - 1
j_max = 0
for i in range(n):
    a = int(input())
    s += [a]

for j in range(len(s)):
    if s[j] != max(s) and s[j] != min(s):
        print(s[j])
        