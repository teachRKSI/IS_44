# 4.1.
print("4.1:")
s = "  Python — это здорово!  "
s = s.strip().lower()
print(s)
print("Длина:", len(s))

# 4.2.
print("\n4.2:")
s = "яблоко,банан,вишня"
for fruit in s.split(","):
    print(fruit.upper())

# 4.3.
print("\n4.3:")
s = "А роза упала на лапу Азора"
clean_s = s.lower().replace(" ", "")
if clean_s == clean_s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

# 4.4.
print("\n4.4:")
s = "hello world"
print(s.replace(" ", "_"))