# 8.1
try:
    x = int(input("Введите число: "))
    print(f"Вы ввели {x}")
except ValueError:
    print("Это не число")

# 8.2
try:
    a = float(input("Делимое: "))
    b = float(input("Делитель: "))
    print(a / b)
except ZeroDivisionError:
    print("Деление на ноль!")

# 8.3 try/except/else/finally
try:
    x = int(input("Введите число: "))
except ValueError:
    # выполняется, если было исключение
    print("Ошибка ввода")
else:
    # выполняется, если исключения НЕ было
    print(f"OK, x = {x}")
finally:
    # выполняется ВСЕГДА (и при ошибке, и без)
    print("Конец блока")