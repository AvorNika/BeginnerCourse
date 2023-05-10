# раздел 13.6 Функции с возвратом значения, задание 4 Площадь и длина
# объявление функции
def get_circle(radius):
    import math
    c = math.pi * 2 * radius
    s = math.pi * radius ** 2
    return c, s
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
