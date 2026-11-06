# 2.1
print("-------------Задание 2.1----------------")

for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 2.2
print("-------------Задание 2.2----------------")

number = 1
while number <= 20:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1


# 2.3
print("-------------Задание 2.3----------------")

n = int(input("Введите целое положительное число: "))
total = 0
for number in range(1, n + 1):
    total += number
print(f"Сумма чисел от 1 до {n}: {total}")


# 2.4
print("---------------Задание 2.4------------------")

for number in range(1, 101):
    if number % 7 == 0 and number % 5 !=0:
        print(number, end = " ")