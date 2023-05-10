# раздел 11.6 Методы списков, задание 7 Количество артиклей
s = input()
s1 = s.lower().split()

cnt_a = s1.count('a')

cnt_an = s1.count('an')

cnt_the = s1.count('the')

print('Общее количество артиклей:', cnt_a + cnt_an + cnt_the)
