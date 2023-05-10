# раздел 10.2 экзамен, задание 10 Второе вхождение
s = input()
counter = 0
for i in range(len(s)):
    if s[i] == 'f':
        counter += 1
        if counter == 2:
            print(i)
if counter == 1:
    print('-1')
elif counter == 0:
    print('-2')
