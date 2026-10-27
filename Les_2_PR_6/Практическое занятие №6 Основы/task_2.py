print("2.1")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\n2.2")
i = 1
while i <= 20:
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

print("\n2.3")
try:
    n = int(input("Введите n: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Сумма от 1 до {n} = {total}")
except ValueError:
    print("Нужно целое число")

print("\n2.4")
result = []
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
print(" ".join(result))