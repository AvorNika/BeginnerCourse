# раздел 11.4 Вывод элементов списка, задание 6 Google search-1
n = int(input())
s = []
for i in range(n):
    a = input()
    s += [a]
b = input()
for j in range(len(s)):
    if b.lower() in s[j].lower():
        print(s[j])
