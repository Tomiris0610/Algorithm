#Задание8
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 88)
]

top_student = max(students, key=lambda x: x[1])

print(top_student)