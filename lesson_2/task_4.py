print("Задача 4.1")
s = "  Python — это здорово!  "
cleaned_s = s.strip().lower()
print("Обработанная строка:", cleaned_s)
print("Длина строки:", len(cleaned_s))


print("\nЗадача 4.2")
fruits_str = "яблоко,банан,вишня"
fruits = fruits_str.split(",")
for item in fruits:
    print(item.upper())


print("\nЗадача 4.3")
text = "А роза упала на лапу Азора"
normalized = text.replace(" ", "").lower()
if normalized == normalized[::-1]:
    print(f"Строка '{text}' является палиндромом!")
else:
    print(f"Строка '{text}' НЕ является палиндромом.")


print("\nЗадача 4.4")
phrase = "hello world"
result = phrase.replace(" ", "_")
print("Результат:", result)
