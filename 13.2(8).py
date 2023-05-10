# раздел 13.2 Функции с параметрами, задание 8 Звёздный треугольник
# объявление функции
def draw_triangle(fill, base):
    for i in range(base // 2 + 1):
        for j in range(i + 1):
            print(fill, end='')
        print()
    for k in range(base//2, 0, -1):
        for g in range(k):
            print(fill, end='')
        print()

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
