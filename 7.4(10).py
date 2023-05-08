# раздел 7.4 Цикл while, задание 10 Количество членов
text = input()
counter = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    counter += 1
    text = input()
print(counter)
