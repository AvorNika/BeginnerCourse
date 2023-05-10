# раздел 13.5 Функции с возвратом значения, задание 4** Next Prime
# объявление функции
def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def get_next_prime(num):
    while is_prime(num + 1) == False:
        num += 1
        continue
    return num + 1


# считываем данные
n = int(input())

print(get_next_prime(n))
