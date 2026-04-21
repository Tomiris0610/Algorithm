#Задание11
users = {}

def add_user(name, age):
    users[name] = age

def find_user(name):
    return users.get(name, "Not found")

def delete_user(name):
    if name in users:
        del users[name]

# Пример использования
add_user("Alice", 25)
add_user("Bob", 30)

print(find_user("Alice"))

delete_user("Alice")
print(find_user("Alice"))