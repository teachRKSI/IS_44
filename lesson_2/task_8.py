print("Задача 8.1")
try:
    num = int(input("Введите целое число: "))
    print("Вы успешно ввели число:", num)
except ValueError:
    print("Ошибка: введено не целое число!")


print("\nЗадача 8.2")
try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    print(f"Результат: {a / b}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно!")
except ValueError:
    print("Ошибка: нужно ввести числа!")


print("\nЗадача 8.3")
try:
    x = float(input("Введите число для деления 100 на него: "))
    result = 100 / x
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    print(f"Всё прошло успешно, 100 / {x} = {result}")
finally:
    print("тут что-то делает")
