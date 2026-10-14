# Задание 4.1
raw_string = " Python — это здорово! "
cleaned_string = raw_string.strip().lower()
print(f"4.1 Очищенная строка: '{cleaned_string}', Длина: {len(cleaned_string)}")

# Задание 4.2
fruits_str = "яблоко,банан,вишня"
print("4.2 Фрукты:")
for fruit in fruits_str.split(","):
    print(fruit.upper())

# Задание 4.3
def is_palindrome(s: str) -> bool:
    normalized = "".join(s.lower().split())
    return normalized == normalized[::-1]

test_str1 = "А роза упала на лапу Азора"
test_str2 = "Python"
print(f"4.3 '{test_str1}' палиндром? {is_palindrome(test_str1)}")
print(f"4.3 '{test_str2}' палиндром? {is_palindrome(test_str2)}")

# Задание 4.4
text = "hello world"
replaced_text = text.replace(" ", "_")
print("4.4 Замена пробелов:", replaced_text)