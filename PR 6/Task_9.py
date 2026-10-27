filename = "hello.txt"


with open(filename, "w", encoding="utf-8") as file:
    file.write("Привет, мир!\nВторая строка файла.\nТретья строка файла.")
print("9.1 Файл успешно записан.")


print("\n9.2 Содержимое файла:")
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


print("9.3 Построчное чтение:")

with open(filename, "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Строка {line_num}: {line.strip()}")