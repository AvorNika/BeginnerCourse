# раздел 13.5 Функции с возвратом значения, задание 5* Good password
# объявление функции
def is_password_good(password):
    s = []

    for i in range(len(password)):
        s += password[i]
    counter_lower = 0
    counter_upper = 0
    counter_digit = 0
    for j in range(len(s)):
        if s[j] in '0123456789':
            counter_digit += 1
    for k in range(len(s)):
        if s[k] in 'abcdefghijklmnopqrstuvwxyz':
            counter_lower += 1
        elif s[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            counter_upper += 1

    if counter_digit > 0 and counter_lower > 0 and counter_upper > 0 and len(password) >= 8:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
