# 1.1
name = "Анна"
age = 20
height = 1.68
print(f"Меня зовут {name}, мне {age} лет, мой рост {height} м.")

# 1.2
# Объяснение:
# a = "5" (str), b = 5 (int).
# a + b вызовет TypeError: нельзя складывать str и int
a = "5"
b = 5
try:
    print(a + b)
except TypeError as e:
    print(f"Ошибка: {e}")
# Правильно: int(a) + b  или  a + str(b)

# 1.3
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
print(f"Сумма: {x + y}")