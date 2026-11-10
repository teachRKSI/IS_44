print("Задача 3.1")
nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique_nums = list(set(nums))
unique_nums.sort(reverse=True)
print("Без дубликатов по убыванию:", unique_nums)


print("\nЗадача 3.2")
nums = [1, 2, 2, 3, 4, 4, 5, 1]
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print("Количество вхождений каждого числа:", counts)


print("\nЗадача 3.3")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_a = set(a)
set_b = set(b)
print("Пересечение:", list(set_a & set_b))
print("Только из a:", list(set_a - set_b))
print("Все уникальные из обоих:", list(set_a | set_b))


print("\nЗадача 3.4")
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
print("Студенты с оценкой >= 4:")
for name, grade in grades.items():
    if grade >= 4:
        print(f"{name} с оценкой {grade}")
