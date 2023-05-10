# раздел 13.4 Функции с возвратом значения, задание 11 Merge lists 1
# объявление функции
def merge(list1, list2):
    s = list1 + list2
    s.sort()
    return s

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
