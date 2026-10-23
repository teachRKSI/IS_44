# 9.1
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!\n")
print("9.1: Файл записан.")

# 9.2
print("\n9.2: Содержимое файла:")
with open("hello.txt", "r", encoding="utf-8") as file:
    print(file.read().strip())

# 9.3
print("\n9.3: Построчное чтение:")
with open("hello.txt", "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
