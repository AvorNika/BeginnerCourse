# раздел 11.5 Методы строк: split, join, задание 7 Коректный ip-адрес
s = input()
flag = False
s = s.split('.')
for i in range(len(s)):
    if 0 <= int(s[i]) <= 255:
        flag = True
    else:
        flag = False
        break

if flag == True:
    print('ДА')
else:
    print('НЕТ')
