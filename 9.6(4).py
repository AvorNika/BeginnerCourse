# раздел 9.6 Строки в памяти компьютера, задание 4 Символы в диапазоне
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')
