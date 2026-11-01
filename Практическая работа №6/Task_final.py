students = {
    "Анна":  [4, 5, 3, 4],
    "Борис": [3, 3, 2, 5],
    "Вика":  [5, 5, 5, 5],
    "Глеб":  [2, 3, 4, 3],
}


def save_report(path: str, averages: dict[str, float], best: str) -> None:
    """Сохраняет отчёт по студентам в файл.

    Args:
        path: путь к файлу.
        averages: словарь имя → средний балл.
        best: имя лучшего студента.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            for name, avg in averages.items():
                f.write(f"{name}: {avg}\n")
            f.write(f"Лучший студент: {best}\n")
    except OSError as e:
        print(f"Не удалось записать файл: {e}")


def main() -> None:
    """Основная логика отчёта по студентам."""
    # 1. Средние баллы
    averages = {name: sum(marks) / len(marks) for name, marks in students.items()}

    # 2. Лучший студент
    best = max(averages, key=averages.get)

    # 3. Отличники
    excellent = [name for name, avg in averages.items() if avg >= 4.5]

    # 4. У кого есть двойка
    with_twos = [name for name, marks in students.items() if 2 in marks]

    # Вывод
    print("Средние баллы:", averages)
    print("Лучший студент:", best)
    print("Отличники:", excellent)
    print("Есть двойки у:", ", ".join(with_twos))

    # 5. Запись в файл
    save_report("report.txt", averages, best)


if __name__ == "__main__":
    main()