with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("hello.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.rstrip()}")
