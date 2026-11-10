print("Задача 7.1")
nums = [4, 1, 7, 3]
print("Сумма (sum):", sum(nums))
print("Минимум (min):", min(nums))
print("Максимум (max):", max(nums))
print("Отсортированный список (sorted):", sorted(nums))


print("\nЗадача 7.2")
nums = [4, 1, 7, 3]
for i, val in enumerate(nums):
    print(f"Элемент под индексом {i}: {val}")


print("\nЗадача 7.3")
names = ["Анна", "Борис"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(f"{name} — {age} лет")


print("\nЗадача 7.4")
nums = [4, 1, 7, 3]
print("Есть ли числа больше 10?", any(x > 10 for x in nums))
print("Все ли числа больше 0 (положительные)?", all(x > 0 for x in nums))
