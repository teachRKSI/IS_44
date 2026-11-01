# 9.1 Запись
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!\n")

# 9.2 Чтение
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 9.3 Построчно с номерами
with open("hello.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")