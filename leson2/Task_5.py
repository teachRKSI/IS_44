# Тема 5. Функции

from typing import Optional

# 5.1
def calculate_stats(numbers: list[float]) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """Возвращает минимальное, максимальное и среднее значения списка."""
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

print("Статистика:", calculate_stats([4, 8, 2, 6]))
print("Пустой список:", calculate_stats([]))

# 5.2
def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

print("Простые числа от 1 до 20:", [n for n in range(1, 21) if is_prime(n)])

# 5.3
def count_words(text: str) -> dict[str, int]:
    """Подсчитывает количество каждого слова в тексте."""
    counts = {}
    for word in text.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts

print("Подсчёт слов:", count_words("кот пес кот попугай пес кот"))

# 5.4
def apply_twice(func, x):
    """Применяет переданную функцию к значению два раза подряд."""
    return func(func(x))

print("Результат apply_twice:", apply_twice(lambda x: x + 3, 5))
