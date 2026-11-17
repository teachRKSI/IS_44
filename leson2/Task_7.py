# Тема 7. Встроенные функции

# 7.1
nums = [4, 1, 7, 3]
print("Сумма:", sum(nums))
print("Минимум:", min(nums))
print("Максимум:", max(nums))
print("Сортировка:", sorted(nums))

# 7.2
print("\nИндекс и значение:")
for index, value in enumerate(nums):
    print(index, value)

# 7.3
names = ["Анна", "Борис"]
ages = [20, 22]
print("\nИмя и возраст:")
for name, age in zip(names, ages):
    print(name, age)

# 7.4
print("\nЕсть число больше 10:", any(number > 10 for number in nums))
print("Все числа положительные:", all(number > 0 for number in nums))
