# раздел 13.5 Функции с возвратом значения, задание 8 BEEGEEK
# объявление функции
def is_valid_password(password):
    s = password.split(':')
    counter_all = 0
    counter_b = 0
    a = s[0]
    b = int(s[1])
    c = int(s[2])
    if a == a[::-1]:
        counter_all += 1
    for i in range(1, b + 1):
        if b % i == 0:
            counter_b += 1
    if counter_b == 2:
        counter_all += 1
    if c % 2 == 0:
        counter_all += 1
    if counter_all == 3 and len(s) == 3:
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
