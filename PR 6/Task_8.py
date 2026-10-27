print("--- Задание 8.1 ---")

try:
    user_num = int(input("Введите целое число: "))
    print(f"Вы ввели: {user_num}")
except ValueError:
    print("Ошибка: Введено не целое число!")


print("\n--- Задание 8.2 ---")

try:
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель: "))
    res = num1 / num2
    print(f"Результат деления: {res}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")
except ValueError:
    print("Ошибка: Введено некорректное число!")


print("\n--- Задание 8.3 ---")

try:
    val = int(input("Введите число для проверки try/except/else/finally: "))
    result = 100 / val
except ZeroDivisionError:
    print("-> Блок EXCEPT: Перехвачена ошибка деления на 0!")
except ValueError:
    print("-> Блок EXCEPT: Перехвачена ошибка ввода не числа!")
else:
    print(f"-> Блок ELSE: Вычисления прошлы успешно! Результат: {result}")
finally:
    print("-> Блок FINALLY: Данный блок выполняется всегда.")