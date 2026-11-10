students = {
    "Анна":  [4, 5, 3, 4],
    "Борис": [3, 3, 2, 5],
    "Вика":  [5, 5, 5, 5],
    "Глеб":  [2, 3, 4, 3],
}

def calculate_average(grades: list) -> float:
    """Вычисляет средний балл для переданного списка оценок."""
    return sum(grades) / len(grades)

averages = {name: calculate_average(grades) for name, grades in students.items()}

# Лучший студент
best_student = ""
max_score = 0.0
for name, avg in averages.items():
    if avg > max_score:
        max_score = avg
        best_student = name

# Список отличников
excellent = [name for name, avg in averages.items() if avg >= 4.5]

# Студенты, если есть 2
poor_grade = [name for name, grades in students.items() if 2 in grades]

print("Средние баллы:", averages)
print("Лучший студент:", best_student)
print("Отличники:", excellent)
print("Есть двойки у:", ", ".join(poor_grade))

# Запись в файл
with open("report.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{name}: {avg}\n" for name, avg in averages.items())
    f.write(f"Лучший студент: {best_student}\n")
