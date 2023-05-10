# раздел 11.5 Методы строк: split, join, задание 9 Количество совпадающих пар
s = input()
s = s.split()
counter = 0

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j] and i != j:
            counter += 1

print(int(counter / 2))
