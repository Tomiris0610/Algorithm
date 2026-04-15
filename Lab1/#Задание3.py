#Задание3
# Ввод числа
n = int(input("Введите натуральное число: "))

# Вычисление суммы
sum_result = 0
for i in range(1, n + 1):
    sum_result += i

# Вывод результата
print("Сумма чисел от 1 до", n, "равна:", sum_result)