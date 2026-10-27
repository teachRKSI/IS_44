# 9.1. 
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!\n")
print("9.1: Файл записан.")

# 9.2. 
print("\n9.2:")
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 9.3.
print("\n9.3:")
with open("hello.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())