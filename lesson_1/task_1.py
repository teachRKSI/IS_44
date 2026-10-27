# 1.1.
name = "Вася"
age = 20
height = 1.80
print(f"Меня зовут {name}, мне {age} лет, мой рост {height} м.")

# 1.2.а
a = "5"
b = 5
# ОТВЕТ: Произойдет ошибка TypeError, так как в Python нельзя складывать строку (str) и число (int).
# print(a + b) 

# 1.3.
num1 = float(input("\nВведите первое число: "))
num2 = float(input("Введите второе число: "))
print("Сумма:", num1 + num2)