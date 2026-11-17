# Тема 4. Строки

# 4.1
text = " Python — это здорово! "
clean_text = text.strip()
print("Без пробелов по краям:", clean_text)
print("Размер строки:", len(clean_text))

# 4.2
fruits = "яблоко,банан,вишня"
for fruit in fruits.split(","):
    print(fruit.strip().upper())

# 4.3
word = input("Введите строку для проверки на палиндром: ")
normalized = word.replace(" ", "").lower()
if normalized == normalized[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")

# 4.4
phrase = "hello world"
print(phrase.replace(" ", "_"))
