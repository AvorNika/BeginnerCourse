# раздел 15.6 Калькулятор системы счисления
# перевод в десятичную систему счисления
notation_in = int(input('Введите число, обозначающее основание системы счисления имеющегося числа:\n'))
number_in = input('Введите число, которое необходимо перевести:\n')
new_number_in = []
number_out = 0
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for j in range(len(number_in)):
    new_number_in += number_in[j]


for i in range(len(new_number_in)):
    if new_number_in[i] in abc:
        new_number_in[i] = 10+abc.index(new_number_in[i])
    number_out += int(new_number_in[i])*notation_in**(len(new_number_in)-i-1)


print(number_out)
