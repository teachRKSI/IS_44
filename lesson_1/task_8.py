# 8.1. 
print("8.1:")
try:
    num = int(input("Введите число: "))
    print("Вы ввели:", num)
except ValueError:
    print("Ошибка: это не число!")

# 8.2.
print("\n8.2:")
try:
    a = float(input("Делимое: "))
    b = float(input("Делитель: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: на ноль делить нельзя!")

# 8.3.
print("\n8.3:")
try:
    x = int(input("Введите число: "))
except ValueError:
    print("Сработал except: была ошибка ввода.")
else:
    print("Сработал else: ошибки не было, x =", x)
finally:
    print("Сработал finally: выполняется всегда.")