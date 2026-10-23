# 4.1
s1 = "  Python — это здорово!  "
s1_clean = s1.strip().lower()
print("4.1:", s1_clean, f"(длина: {len(s1_clean)})")

# 4.2
s2 = "яблоко,банан,вишня"
print("\n4.2:")
for item in s2.split(","):
    print(item.upper())

# 4.3
def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("\n4.3:", is_palindrome("А роза упала на лапу Азора"))

# 4.4
s3 = "hello world"
print("\n4.4:", s3.replace(" ", "_"))
