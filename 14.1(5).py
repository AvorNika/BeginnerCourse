# раздел 14.1 экзамен, задание 5 Калькулятор доставки
# объявление функции
def get_shipping_cost(quantity):
    cost = 1000
    if quantity == 1:
        return cost
    if quantity > 1:
        for i in range(quantity - 1):
            cost += 120
    return cost

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
