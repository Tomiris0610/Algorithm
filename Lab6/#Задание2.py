#Задание2
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

# Формирование матрицы
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

# Вывод матрицы
print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Общие вычисления
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма всех элементов:", total)
print("Максимальный элемент:", maximum)

# -------------------------
# Задание 2
# -------------------------

# Сумма по строкам
row_sums = []

print("\nСуммы строк:")
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

# Сумма по столбцам
print("\nСуммы столбцов:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

# Поиск строки с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("\nСтрока с максимальной суммой:", max_row_index)