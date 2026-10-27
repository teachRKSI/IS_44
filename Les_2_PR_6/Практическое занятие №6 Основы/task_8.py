print("8.1")
try:
    x = int(input("Введите число: "))
except ValueError:
    print("Это не число")
finally:
    print("Конец")

print("\n8.2")
try:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    print("Ответ: ", a / b)
except ValueError:
    print("Введите ЧИСЛА")
except ZeroDivisionError:
    print("Деление на ноль невозможно")

print("\n8.3")
try: # try    — блок, где может возникнуть исключение
    x = int(input("Введите число: "))
except ValueError: # except — срабатывает, если исключение возникло
    print("Не число")
else: # else   — срабатывает, если исключения НЕ было
    print(f"Всё хорошо, x = {x}")
finally: # finally — срабатывает ВСЕГДА (и при ошибке, и без неё)
    print("Конец")