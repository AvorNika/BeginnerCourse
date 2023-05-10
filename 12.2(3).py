# раздел 12.2 экзамен, задание 3 Сумма чисел
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s_sum = sum(s)
for j in range(len(s) - 1):
    s.insert(j * 2 + 1, '+')
s.append('=')

s.append(s_sum)

print(*s, sep='')
