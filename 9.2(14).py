# раздел 9.2 Срезы, задание 14 Две половинки
s = input()
s = s[len(s) // 2 + len(s) % 2:]+s[:len(s) // 2 + len(s) % 2]
print(s)
