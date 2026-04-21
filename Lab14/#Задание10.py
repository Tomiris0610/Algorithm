#Задание10
arr = [1, 1, 2, 2, 2, 3, 3, 1]

max_len = 1
current_len = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print(max_len)