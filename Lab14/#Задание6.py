#Задание6
arr = [1, 2, 2, 3, 1, 4]

seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)