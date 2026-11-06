from pathlib import Path

file_path = Path(__file__).with_name("hello.txt")

# 9.1
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Привет, мир!")

print("Файл записан.")

# 9.2
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print("Содержимое файла:", content)

# 9.3
with open(file_path, "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line.rstrip()}")