# раздел 13.4 Функции с возвратом значения, задание 9 Делители 2
# объявление функции
def number_of_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors += [i]
    return len(factors)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
