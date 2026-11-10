def task_2_1():
    print("Цикл for")
    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(str(num))
    print()

def task_2_2():
    print("Цикл while")
    num = 1
    while num <= 20:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(str(num))
        num += 1
    print()

def task_2_3():
    print("Сумма числа")
    raw_input = input("Введите число n: ")
    n = int(raw_input)

    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"Сумма числа {n}: {total}\n")

def task_2_4():
    numbers = []
    for num in range(1, 101):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(str(num))

    print(",".join(numbers))

if __name__ == "__main__":
    task_2_1()
    task_2_2()
    task_2_3()
    task_2_4()
