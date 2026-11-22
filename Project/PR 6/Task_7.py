nums = [4, 1, 7, 3]

print("7.1 Сумма:", sum(nums))
print("7.1 Минимум:", min(nums))
print("7.1 Максимум:", max(nums))
print("7.1 Отсортированный:", sorted(nums))


print("\n7.2 Элементы с индексами:")
for index, value in enumerate(nums):
    print(f"Индекс: {index}, Значение: {value}")


names = ["Анна", "Борис"]
ages = [20, 22]
print("\n7.3 Пары zip:")
for name, age in zip(names, ages):
    print(f"{name}: {age} лет")


has_greater_than_10 = any(x > 10 for x in nums)
all_positive = all(x > 0 for x in nums)

print(f"\n7.4 Есть ли числа больше 10? {has_greater_than_10}")
print(f"7.4 Все ли числа положительные? {all_positive}")