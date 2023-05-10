# раздел 11.4 Вывод элементов списка, задание 8 Negatives, Zeros and Positives
n = int(input())
sn = []
for i in range(n):
    a = input()
    sn += [a]
k = int(input())
sk = []
for j in range(k):
    b = input()
    sk += [b]

s = []
for m in range(n):
    counter = 0
    for h in range(k):
        if sk[h].lower() in sn[m].lower():
            counter += 1
            if counter == k:
                s += [sn[m]]

print(*s, sep='\n')
