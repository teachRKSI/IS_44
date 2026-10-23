# 8.1
print("8.1:")
try:
    print(f"Вы ввели: {num}")
except ValueError:
    print("Ошибка: введено не число.")

print("\n8.2:")
try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    print(f"Результат: {a / b}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: нужно вводить числа!")

# 8.3
print("\n8.3:")
try:
    val = int(input("Введите число: "))
    print("Сработал except: введено не число.")
else:
    print("Сработал else: ошибок нет, число введено корректно.")
finally:
    print("Сработал finally: выполняется всегда (например, для закрытия ресурсов).")
