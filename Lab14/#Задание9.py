#Задание9
arr = [1, 2, 3, 4, 5, 6]

even = [x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2 != 0]

print("Even:", even)
print("Odd:", odd)