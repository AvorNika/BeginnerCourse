# раздел 7.6 break, continue и else, задание 7 Наименьший делитель
num = int(input())
for i in range(2, num + 1):
    if num % i == 0:
        print(i)
        break
