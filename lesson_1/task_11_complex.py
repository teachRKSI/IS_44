def calculate_averages(students: dict) -> dict:
    """Вычисляет средний балл для каждого студента."""
    return {name: sum(grades) / len(grades) for name, grades in students.items()}

def get_best_student(averages: dict) -> str:
    """Возвращает имя студента с самым высоким средним баллом."""
    return max(averages, key=averages.get)

def main():
    students = {
        "Анна":  [4, 5, 3, 4],
        "Борис": [3, 3, 2, 5],
        "Вика":  [5, 5, 5, 5],
        "Глеб":  [2, 3, 4, 3],
    }

    averages = calculate_averages(students)
    print("Средние баллы:", averages)

    best = get_best_student(averages)
    print("Лучший студент:", best)

    excellent = [name for name, avg in averages.items() if avg >= 4.5]
    print("Отличники:", excellent)

    bad_students = [name for name, grades in students.items() if 2 in grades]
    print("Есть двойки у:", ", ".join(bad_students))

    try:
        with open("report.txt", "w", encoding="utf-8") as f:
            for name, avg in averages.items():
                f.write(f"{name}: {avg}\n")
            f.write(f"Лучший студент: {best}\n")
        print("Отчёт успешно сохранён в report.txt")
    except IOError as e:
        print(f"Ошибка при записи файла: {e}")

if __name__ == "__main__":
    main()
