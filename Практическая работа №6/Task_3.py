nums = [1, 2, 2, 3, 4, 4, 5, 1]

# 3.1 Уникальные, по убыванию
unique_desc = sorted(set(nums), reverse=True)
print(unique_desc)   # [5, 4, 3, 2, 1]

# 3.2 Частоты
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print(counts)        # {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}

# 3.3 Множества
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
sa, sb = set(a), set(b)
print("Пересечение:", sa & sb)          # {3, 4}
print("Только из a:", sa - sb)          # {1, 2}
print("Все уникальные:", sa | sb)       # {1, 2, 3, 4, 5, 6}

# 3.4 Оценки >= 4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for name, mark in grades.items():
    if mark >= 4:
        print(name)