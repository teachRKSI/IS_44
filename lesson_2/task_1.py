def task_1_1():
    name: str = "Никита"
    age: int = 19
    height: float = 1.66

    result: str = f"Меня зовут {name}, мне {age} лет, мой рост {height} м."
    print(result)

def task_1_2():
    a = "5"
    b = 5

    try:
        print(a + b)
    except TypeError as error:
        print(f"Error: {error}")

def task_1_3():
    raw_num1 = input("Введите первое число: ")
    raw_num2 = input("Введите второе число: ")

    num1 = float(raw_num1)
    num2 = float(raw_num2)

    total = num1 + num2

    print("Сумма числе:", total)


if __name__ == "__main__":
    task_1_1()
    task_1_2()
    task_1_3()
