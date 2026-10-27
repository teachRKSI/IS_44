nums = [4, 1, 7, 3]

# 7.1.
print("7.1:")
print("Сумма:", sum(nums))
print("Минимум:", min(nums))
print("Максимум:", max(nums))
print("Отсортированный:", sorted(nums))

# 7.2.
print("\n7.2:")
for index, value in enumerate(nums):
    print("Индекс:", index, "Значение:", value)

# 7.3. 
print("\n7.3:")
names = ["Анна", "Борис"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(name, age)

# 7.4.
print("\n7.4:")
print("Есть числа > 10:", any(x > 10 for x in nums))
print("Все числа положительные:", all(x > 0 for x in nums))