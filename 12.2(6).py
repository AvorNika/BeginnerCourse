# раздел 12.2 экзамен, задание 6 Молодёжный жаргон
s = input().split()
print(*[(s[i][1:] + s[i][0] + 'ки') for i in range(len(s))])
