# раздел 7.3 Частые сценарии, задание 14* Only even numbers
flag = 'YES'
for _ in range(1, 11):
    num = int(input())
    if num % 2 == 1:
        flag = 'NO'
print(flag)
