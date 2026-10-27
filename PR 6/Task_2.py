print("\nЗадание 2.1:")

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\nЗадание 2.2:")

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

print("\nЗадание 2.3:")

n = int(input("Введите число n: "))
total_sum = sum(range(1, n + 1))
print(f"Сумма чисел от 1 до {n}: {total_sum}")

print("\nЗадание 2.4:")

result_numbers = [str(x) for x in range(1, 101) if x % 7 == 0 and x % 5 != 0]
print(" ".join(result_numbers))