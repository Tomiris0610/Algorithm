#Задание1 блок1
import random
import time
import matplotlib.pyplot as plt

# ----------------------------
# Алгоритмы поиска
# ----------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ----------------------------
# Замер времени
# ----------------------------

def measure_time(search_func, arr, target):
    start = time.perf_counter()
    search_func(arr, target)
    end = time.perf_counter()
    return end - start


# ----------------------------
# Эксперимент
# ----------------------------

sizes = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]

linear_times = []
binary_times = []

for n in sizes:
    arr = list(range(n))  # отсортированный массив
    target = random.randint(0, n - 1)

    # Линейный поиск
    t_lin = measure_time(linear_search, arr, target)
    linear_times.append(t_lin)

    # Бинарный поиск
    t_bin = measure_time(binary_search, arr, target)
    binary_times.append(t_bin)

    print(f"n={n}: linear={t_lin:.6f}s, binary={t_bin:.6f}s")


# ----------------------------
# График
# ----------------------------

plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, marker='o', label='Linear Search')
plt.plot(sizes, binary_times, marker='o', label='Binary Search')

plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение линейного и бинарного поиска')
plt.legend()
plt.grid(True)

plt.xscale('log')  # удобно для больших диапазонов
plt.yscale('log')  # чтобы различия были видны

plt.show()