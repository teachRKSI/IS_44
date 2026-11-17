# Тема 3. Коллекции

# 3.1
nums = [1, 2, 2, 3, 4, 4, 5, 1]
duplicates = sorted({number for number in nums if nums.count(number) > 1},
                    reverse=True)
print("Дубликаты по убыванию:", duplicates)

# 3.2
counts = {}
for number in nums:
    counts[number] = counts.get(number, 0) + 1
print("Количество повторений:", counts)

# 3.3
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_a = set(a)
set_b = set(b)
print("Пересечение:", sorted(set_a & set_b))
print("Только из a:", sorted(set_a - set_b))
print("Объединение:", sorted(set_a | set_b))

# 3.4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
print("Оценка не ниже 4:")
for student, grade in grades.items():
    if grade >= 4:
        print(student)
