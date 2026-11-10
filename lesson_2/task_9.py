# Задача 9.1
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!\n")
    f.write("Привет, мир 2!\n")
    f.write("Привет, мир 3!\n")


print("\nЗадача 9.2")
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Содержимое:")
print(content)


print("\nЗадача 9.3")
with open("hello.txt", "r", encoding="utf-8") as f:
    for num, line in enumerate(f, 1):
        print(f"[{num}] - {line.strip()}")
