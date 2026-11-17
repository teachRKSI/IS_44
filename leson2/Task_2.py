# Тема 2. Управляющие конструкции

# 2.1 — FizzBuzz с помощью for
print("2.1 — FizzBuzz (for):")
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 2.2 — то же самое с помощью while
print("\n2.2 — FizzBuzz (while):")
number = 1
while number <= 20:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1

# 2.3
n = int(input("\nВведите n для задания 2.3: "))
for number in range(1, n + 1):
    print(number, end=" ")
print()

# 2.4
result = [number for number in range(1, 101)
          if number % 7 == 0 and number % 5 != 0]
print("Числа от 1 до 100, кратные 7, но не кратные 5:")
print(*result)
