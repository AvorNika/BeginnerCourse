# раздел 6.2 Строковый тип данных, задание 9 Арифметические строки
str1, str2, str3 = str(input()), str(input()), str(input())
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)
if (len1 != len2 and len1 != len3 and len2 != len3) and (abs(len1-len2) == abs(len1-len3) or abs(len2-len3) == abs(len2-len1) or abs(len3-len1) == abs(len3-len2)):
    print('YES')
else:
    print('NO')
