# Задание 1.1
name: str = "Иван"
age: int = 20
height: float = 1.78

print(f"Меня зовут {name}, мне {age} лет, мой рост {height} м.")


# Задание 1.2
a = "5"
b = 5

try:
    print(a + b)
except TypeError as e:
    print(f"\nПроверка ошибки: {e}")


# Задание 1.3
print("\nЗадание 1.3:")
num1_str = input("Введите первое число: ")
num2_str = input("Введите второе число: ")

num1 = float(num1_str)
num2 = float(num2_str)
print(f"Сумма чисел: {num1 + num2}")