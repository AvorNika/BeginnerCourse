# раздел 11.6 Методы списков, задание 5* Все и сразу 2
numbers = [8, 9, 10, 11]
numbers.insert(1, 17)
del numbers[2]
odds = [4, 5, 6]
numbers.extend(odds)
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)
