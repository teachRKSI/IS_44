# 2.1 FizzBuzz через for
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("-" * 20)

# 2.2 FizzBuzz через while
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

print("-" * 20)

# 2.3 Сумма от 1 до n
n = int(input("Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Сумма 1..{n} = {total}")

# 2.4 Числа 1..100, делятся на 7 и не делятся на 5
result = [str(i) for i in range(1, 101) if i % 7 == 0 and i % 5 != 0]
print(" ".join(result))