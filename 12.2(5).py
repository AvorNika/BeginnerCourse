# раздел 12.2 экзамен, задание 5 Самый длинный
s = input().split()
print((max([len(s[i]) for i in range(len(s))])))
