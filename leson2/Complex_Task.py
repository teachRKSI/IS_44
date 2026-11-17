# Комплексное задание

students = {
    "Анна": [4, 5, 3, 4],
    "Борис": [3, 3, 2, 5],
    "Вика": [5, 5, 5, 5],
    "Глеб": [2, 3, 4, 3],
}

def calculate_average(marks: list[int]) -> float:
    """Вычисляет средний балл по списку оценок."""
    return sum(marks) / len(marks)

# 1. Средний балл каждого студента через генератор словаря
averages = {
    name: calculate_average(marks)
    for name, marks in students.items()
}

# 2. Студент с самым высоким средним баллом
best_student = max(averages, key=averages.get)

# 3. Список отличников со средним баллом не ниже 4.5
excellent = [
    name for name, average in averages.items()
    if average >= 4.5
]

# 4. Студенты, у которых есть хотя бы одна двойка
students_with_twos = [
    name for name, marks in students.items()
    if 2 in marks
]

print("Средние баллы:", averages)
print("Лучший студент:", best_student)
print("Отличники:", excellent)
print("Есть двойки у:", ", ".join(students_with_twos))

# 5. Сохранение отчёта в файл
with open("report.txt", "w", encoding="utf-8") as file:
    for name, average in averages.items():
        file.write(f"{name}: {average}\n")
    file.write(f"Лучший студент: {best_student}\n")
