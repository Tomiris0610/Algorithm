#Задание3 
import random

# Функция сдвига строки вправо
def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

# Создание поля 4x4 (заполняем случайными числами, включая 0)
matrix = []

for i in range(4):
    row = []
    for j in range(4):
        # 30% шанс, что будет 0 (пустая клетка)
        value = random.choice([0, random.randint(1, 9)])
        row.append(value)
    matrix.append(row)

# Вывод до сдвига
print("До сдвига:")
for row in matrix:
    print(row)

# Сдвиг каждой строки вправо
for i in range(4):
    matrix[i] = shift_right(matrix[i])

# Вывод после сдвига
print("\nПосле сдвига вправо:")
for row in matrix:
    print(row)