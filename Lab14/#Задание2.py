#Задание2
from collections import Counter

arr = [1, 3, 3, 2, 1, 3, 4]

counter = Counter(arr)
most_common = counter.most_common(1)[0]

print(most_common)  # (число, количество)