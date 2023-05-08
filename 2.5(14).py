# раздел 2.5 Целочисленная арифметика, задание 14 Перестановка цифр
abc = int(input())
a = abc // 100
b = (abc % 100) // 10
c = abc % 10
print(abc)
print(a*100+c*10+b)
print(b*100+a*10+c)
print(b*100+c*10+a)
print(c*100+a*10+b)
print(c*100+b*10+a)
