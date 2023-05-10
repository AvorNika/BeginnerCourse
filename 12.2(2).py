# раздел 12.2 экзамен, задание 2 Сумма двух списков
L = input().split()
for i in range(len(L)):
    L[i] = int(L[i])
M = input().split()
for j in range(len(M)):
    M[j] = int(M[j])
s = L + M

for k in range(int(len(s) / 2)):
    s[k] = s[k] + s[k + int(len(s) / 2)]

print(*s[:int(len(s) / 2)])
