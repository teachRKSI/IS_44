# 2.1
print("2.1: FizzBuzz через for:")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print("\n")

# 2.2
print("2.2: FizzBuzz через while:")
i = 1
while i <= 20:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
    i += 1
print("\n")

# 2.3
print("\n2.3: Сумма чисел от 1 до n")
try:
    n = int(input("Введите n: "))
    total = 0
    for x in range(1, n + 1):
        total += x
    print(f"Сумма от 1 до {n} равна {total}")
except ValueError:
    print("Ошибка: нужно целое число!")

# 2.4
print("\n2.4: Числа от 1 до 100, делящиеся на 7 и не делящиеся на 5:")
result = [str(x) for x in range(1, 101) if x % 7 == 0 and x % 5 != 0]
print(" ".join(result))
