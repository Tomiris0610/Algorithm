# Задание 2
n=int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Chislo delitsa na 3 i na 5")
elif n % 3 == 0:
    print("Chislo delitsa tolko na 3")
elif n % 5 == 0:
    print("Chislo delitsa tolko na 5")
else:
    print("Chislo ne delitsa ni na 3 ni na 5")