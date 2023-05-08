# раздел 6.2 Строковый тип данных, задание 8 Три города
city1, city2, city3 = str(input()), str(input()), str(input())
len1 = len(city1)
len2 = len(city2)
len3 = len(city3)
lenmin = min(len1, len2, len3)
lenmax = max(len1, len2, len3)
if lenmin == len1 and lenmax == len2:
    print(city1)
    print(city2)
elif lenmin == len1 and lenmax == len3:
    print(city1)
    print(city3)
elif lenmin == len2 and lenmax == len1:
    print(city2)
    print(city1)
elif lenmin == len2 and lenmax == len3:
    print(city2)
    print(city3)
elif lenmin == len3 and lenmax == len1:
    print(city3)
    print(city1)
elif lenmin == len3 and lenmax == len2:
    print(city3)
    print(city2)
    