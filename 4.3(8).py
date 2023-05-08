# раздел 4.3 Вложенные и каскадные условия, задание 8* Самописный калькулятор
a, b = int(input()), int(input())
c = input()
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/' and b == 0:
    print('На ноль делить нельзя!')
elif c == '/' and b != 0:
    print(a/b)
elif c != '+' or c != '-' or c != '*' or c != '/':
    print('Неверная операция')
