print("4.1")
s = "  Python — это здорово!  "
a = s.strip().lower()
print(a)
print("Длина:", len(a))

print("\n4.2")
s = "яблоко,банан,вишня"
for item in s.split(","):
    print(item.upper())

print("\n4.3")
def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
print(is_palindrome("Я иду с мечем судия"))
print(is_palindrome("хай"))

print("\n4.4")
s = "hello world"
a = s.replace(" ", "_")
print(a)

