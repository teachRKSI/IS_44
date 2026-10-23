nums = [4, 1, 7, 3]

print("7.1:")
print("  Сумма:", sum(nums))
print("  Минимум:", min(nums))
print("  Максимум:", max(nums))
print("  Отсортированный:", sorted(nums))
# 7.2
print("\n7.2:")
for i, val in enumerate(nums):
    print(f"  Индекс: {i}, Значение: {val}")

# 7.3
names = ["Анна", "Борис"]
print("\n7.3:")
for name, age in zip(names, ages):

# 7.4
print("\n7.4:")
print("  Есть ли числа > 10:", any(x > 10 for x in nums))
