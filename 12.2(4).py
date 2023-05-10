# раздел 12.2 экзамен, задание 4** Валидный номер
s = input()
counter = 0
if ((s[3] == '-' and s[7] == '-') or (s[0] == '7' and s[1] == '-' and s[5] == '-' and s[9] == '-')):
    counter += 1
for i in range(len(s)):
    if s[i] in '0123456789-':
        counter += 1
if counter == len(s) + 1:
    print('YES')
else:
    print('NO')
