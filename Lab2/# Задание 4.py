# Задание 4
n=int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        count +=1
print("Количество честных чисел:", count)