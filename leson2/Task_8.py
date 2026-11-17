# Тема 8. Обработка исключений

# 8.1
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: введено не целое число.")
else:
    print("Вы ввели:", number)

# 8.2
try:
    first = float(input("\nВведите делимое: ").replace(",", "."))
    second = float(input("Введите делитель: ").replace(",", "."))
    result = first / second
except ValueError:
    print("Ошибка: нужно вводить числа.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
else:
    print("Результат деления:", result)

# 8.3 — пример try/except/else/finally
try:
    value = int(input("\nВведите ещё одно целое число: "))
except ValueError:
    print("Введено не число.")
else:
    print("Успешно! Квадрат числа:", value ** 2)
finally:
    print("Проверка завершена.")
