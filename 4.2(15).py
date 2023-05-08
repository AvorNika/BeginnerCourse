# раздел 4.2 Логические операции, задание 15 Ход короля
stol1 = int(input())
stroka1 = int(input())
stol2 = int(input())
stroka2 = int(input())
if (stol1-1 <= stol2 <= stol1+1) and (stroka1-1 <= stroka2 <= stroka1+1):
    print('YES')
else:
    print('NO')
