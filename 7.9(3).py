# раздел 7.9 Вложенные циклы, задание 3* Делители-1
a, b = int(input()), int(input())
counter_max = 0
max_number = 0
for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += j
            if counter >= counter_max:
                counter_max = counter
                max_number = j
print(max_number, counter_max)
