from enum import unique

print("3.1")
nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique = sorted(set(nums), reverse=True)
print(unique)

print("\n3.2")
nums = [1, 2, 2, 3, 4, 4, 5, 1]
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print(counts)

print("\n3.3")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = set(a) & set(b)
a = set(a) - set(b)
unique = set(a) | set(b)

print("Пересечение:", intersection)
print("Только из a:", a)
print("Все уникальные:", unique)

print("\n3.4")
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for name, grade in grades.items():
    if grade >= 4:
        print(f"{name} ", end="")
