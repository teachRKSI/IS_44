# 9.1
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!\n")

# 9.2
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 9.3
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("hello\n")
    f.write("hello 67\n")
    f.write("tak nado\n")
i = 1

with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(i, line.strip())
        i+=1
