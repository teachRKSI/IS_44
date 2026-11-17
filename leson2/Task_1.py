# Тема 1. Переменные, типы, вывод, f-строки

# 1.1
name = "Иван"
age = 19
height = 1.75
print(f"Меня зовут {name}, мне {age} лет, мой рост {height} м.")

# 1.2
a = "5"
b = 5
# Ошибка TypeError: нельзя складывать строку и целое число.
# print(a + b)
print("Результат 1.2: TypeError, str и int нельзя складывать напрямую.")
print("Если нужно сложить числа:", int(a) + b)

# 1.3
first = float(input("Введите первое число: ").replace(",", "."))
second = float(input("Введите второе число: ").replace(",", "."))
print("Сумма:", first + second)
