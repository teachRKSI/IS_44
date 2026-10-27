nums = [1, 2, 2, 3, 4, 4, 5, 1]

# 3.1.
unique_nums = list(set(nums))
unique_nums.sort(reverse=True)
print("3.1:", unique_nums)

# 3.2.
print("\n3.2:")
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print(counts)

# 3.3.
print("\n3.3:")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_a = set(a)
set_b = set(b)
print("Пересечение:", set_a & set_b)
print("Только из a:", set_a - set_b)
print("Все уникальные:", set_a | set_b)

# 3.4. 
print("\n3.4:")
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for name, grade in grades.items():
    if grade >= 4:
        print(name)
