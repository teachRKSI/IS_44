nums = [1, 2, 2, 3, 4, 4, 5, 1]

# 3.1
unique_sorted_nums = sorted(list(set(nums)), reverse=True)
print("3.1:", unique_sorted_nums)

# 3.2
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print("3.2:", counts)

# 3.3
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = list(set(a) & set(b))
only_a = list(set(a) - set(b))
all_unique = list(set(a) | set(b))
print("3.3:")
print("  Пересечение:", intersection)
print("  Только из a:", only_a)
print("  Все уникальные:", all_unique)

# 3.4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
print("\n3.4: Студенты с оценкой >= 4:")
for name, grade in grades.items():
    if grade >= 4:
        print(name)
