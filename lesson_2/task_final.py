from pathlib import Path


students = {
    "Анна": [4, 5, 3, 4],
    "Борис": [3, 3, 2, 5],
    "Вика": [5, 5, 5, 5],
    "Глеб": [2, 3, 4, 3],
}


def save_report(
    path: Path,
    averages: dict[str, float],
    best: str,
) -> None:
    """Сохраняет средние баллы и имя лучшего студента в файл."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            for name, average in averages.items():
                file.write(f"{name}: {average}\n")

            file.write(f"Лучший студент: {best}\n")
    except OSError as error:
        print("Не удалось записать отчёт:", error)
    else:
        print("Отчёт сохранён:", path.name)


def main() -> None:
    """Вычисляет показатели успеваемости и сохраняет отчёт."""

    # 1. Средний балл каждого студента через comprehension.
    averages = {
        name: sum(marks) / len(marks)
        for name, marks in students.items()
    }

    # 2. Студент с самым высоким средним баллом.
    best = max(averages, key=averages.get)

    # 3. Студенты со средним баллом не ниже 4.5.
    excellent = [
        name
        for name, average in averages.items()
        if average >= 4.5
    ]

    # 4. Студенты, у которых есть хотя бы одна двойка.
    with_twos = [
        name
        for name, marks in students.items()
        if 2 in marks
    ]

    print("Средние баллы:", averages)
    print("Лучший студент:", best)
    print("Отличники:", excellent)
    print("Есть двойки у:", ", ".join(with_twos))

    # 5. Сохранение отчёта рядом со скриптом.
    report_path = Path(__file__).with_name("report.txt")
    save_report(report_path, averages, best)


if __name__ == "__main__":
    main()