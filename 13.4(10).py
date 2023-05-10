# раздел 13.4 Функции с возвратом значения, задание 10 Найти всех
# объявление функции
def find_all(target, symbol):
    abc = []
    while symbol in target:
        abc += [target.find(symbol)]
        target = target[:target.find(symbol)] + '_' + target[target.find(symbol) + 1:]
    return abc

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
