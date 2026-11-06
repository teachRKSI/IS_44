# 8.1
try:
    number = int(input("8.1. Введите целое число: "))
    print("Вы ввели:", number)
except ValueError:
    print("Ошибка: нужно ввести целое число.")

# 8.2
try:
    first = float(input("8.2. Введите делимое: "))
    second = float(input("Введите делитель: "))
    print("Результат деления:", first / second)
except ValueError:
    print("Ошибка: нужно вводить числа.")
except ZeroDivisionError:
    print("Ошибка: делить на ноль нельзя.")

# 8.3
try:
    # Выполняем действие, при котором возможна ошибка.
    number = int(input("8.3. Введите целое число: "))
except ValueError:
    # Выполняется, если в блоке try возникла ValueError.
    print("Ошибка: введено не целое число.")
else:
    # Выполняется, если блок try завершился без ошибки.
    print("Ввод успешен:", number)
finally:
    # Выполняется как при успешном вводе, так и при ошибке.
    print("Проверка ввода завершена.")