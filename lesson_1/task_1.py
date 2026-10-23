# 1.1
name = "Айжан"
age = 20
height = 1.65
print(f"Меня зовут {name}, мне {age} лет, мой рост {height} м.")

# 1.2
print("\n1.2: При выполнении a + b будет ошибка TypeError,")
print("так как нельзя складывать строку (str) и число (int).")
a = "5"
b = 5
try:
    print(a + b)
except TypeError as e:
    print(f"Перехваченная ошибка: {e}")

# 1.3
print("\n1.3: Введите два числа:")
try:
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    print(f"Сумма: {num1 + num2}")
except ValueError:
    print("Ошибка: нужно вводить числа!")
