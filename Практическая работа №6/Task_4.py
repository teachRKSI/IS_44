# 4.1
s = "  Python — это здорово!  "
clean = s.strip().lower()
print(repr(clean), "длина:", len(clean))

# 4.2
fruits = "яблоко,банан,вишня".split(",")
for f in fruits:
    print(f.upper())

# 4.3 Палиндром
def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом (без учёта регистра и пробелов)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("А роза упала на лапу Азора"))   # True

# 4.4
print("hello world".replace(" ", "_"))