# раздел 13.5 Функции с возвратом значения, задание 3* Is a Number Prime?
# объявление функции
def is_prime(num):
    counter =0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
