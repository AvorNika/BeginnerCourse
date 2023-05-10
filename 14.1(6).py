# раздел 14.1 экзамен, задание 6* Биноминальный коэффициент
# объявление функции
def compute_binom(n, k):
    import math
    binom = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(binom)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
