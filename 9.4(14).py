# раздел 9.4 Методы строк, задание 14 Первое и последнее вхождение
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
