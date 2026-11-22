print("\nЗадание 4.1:")

raw_string = " Python — это здорово! "
cleaned_string = raw_string.strip().lower()
print(f"Очищенная строка: '{cleaned_string}', Длина: {len(cleaned_string)}")

print("\nЗадание 4.2:")

fruits_str = "яблоко,банан,вишня"
print("Фрукты:")
for fruit in fruits_str.split(","):
    print(fruit.upper())

print("\nЗадание 4.3:")

def is_palindrome(s: str) -> bool:
    normalized = "".join(s.lower().split())
    return normalized == normalized[::-1]

test_str1 = "А роза упала на лапу Азора"
test_str2 = "Python"
print(f"'{test_str1}' палиндром? {is_palindrome(test_str1)}")
print(f"'{test_str2}' палиндром? {is_palindrome(test_str2)}")

print("\nЗадание 4.4:")

text = "hello world"
replaced_text = text.replace(" ", "_")
print("Замена пробелов:", replaced_text)