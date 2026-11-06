# 4.1
text = "  Python — это здорово!  "
clean = text.strip().lower()

print("Обработанная строка:", clean)
print("Длина:", len(clean))

# 4.2
text = "яблоко,банан,вишня"

for fruit in text.split(","):
    print(fruit.upper())

# 4.3
text = input("Введите строку для проверки на палиндром: ")
clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")

# 4.4
text = "hello world"
print(text.replace(" ", "_"))