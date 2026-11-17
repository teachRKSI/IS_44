# Тема 9. Файлы

# 9.1 — запись в файл
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!\n")
    file.write("Это практическая работа №6.\n")

# 9.2 — чтение всего файла
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Содержимое файла:")
print(content)

# 9.3 — чтение построчно с нумерацией
print("Строки файла с номерами:")
with open("hello.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.rstrip()}")
