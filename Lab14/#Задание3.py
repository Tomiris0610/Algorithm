#Задание3
arr = [2, 7, 11, 15]
target = 9

seen = {}

for num in arr:
    complement = target - num
    if complement in seen:
        print(f"{complement} + {num} = {target}")
        break
    seen[num] = True