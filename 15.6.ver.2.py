# раздел 15.6 Калькулятор систем счисления
# перевод из десятичной системы счисления
notation_out = int(input('Введите число, являющееся основанием новой системы счисления:\n'))
number_in = int(input('Введите число, которое необходимо перевести в новую систему счисления:\n'))
number_out = ''
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


while number_in > notation_out:
    if notation_out < 10:
        number_out += str(number_in % notation_out)
        number_in //= notation_out
        if number_in < notation_out:
            number_out += str(number_in)
    else:
        result = number_in % notation_out
        if result > 9:
            result = abc[result-10]
        number_out += str(result)
        number_in //= notation_out
        if number_in < notation_out:
            number_out += str(number_in)

print(number_out[::-1])
