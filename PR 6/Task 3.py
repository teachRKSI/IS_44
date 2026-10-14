nums = [1, 2, 2, 3, 4, 4, 5, 1]

# Задание 3.1
unique_nums = list(set(nums))
unique_nums.sort(reverse=True)
print("3.1 Уникальные по убыванию:", unique_nums)

# Задание 3.2
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print("3.2 Подсчёт элементов:", counts)

# Задание 3.3
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set_a, set_b = set(a), set(b)
intersection = list(set_a & set_b)
only_a = list(set_a - set_b)
all_unique = list(set_a | set_b)

print("3.3 Пересечение (a & b):", intersection)
print("3.3 Элементы только из a:", only_a)
print("3.3 Все уникальные из обоих:", all_unique)

# Задание 3.4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
good_students = [name for name, grade in grades.items() if grade >= 4]
print("3.4 Студенты с оценкой >= 4:", good_students)