# раздел 4.3 Вложенные и каскадные условия, задание 4 Вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
elif a != b != c:
    print('Разносторонний')
    