# 2.1.
print("--- 2.1 (for) ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 2.2. 
print("\n--- 2.2 (while) ---")
i = 1
while i <= 20:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# 2.3.
print("\n--- 2.3 ---")
n = int(input("Введите n: "))
total = 0
for x in range(1, n + 1):
    total += x
print("Сумма:", total)

# 2.4.
print("\n--- 2.4 ---")
for x in range(1, 101):
    if x % 7 == 0 and x % 5 != 0:
        print(x, end=" ")
print()