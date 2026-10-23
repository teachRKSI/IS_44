# 5.1
def calculate_stats(numbers: list) -> tuple:
    """Возвращает (min, max, average) для списка чисел."""
    if not numbers:
        return (None, None, None)
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

print("5.1:", calculate_stats([4, 2, 9, 7]))

# 5.2
def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\n5.2: Простые числа от 1 до 20:", [x for x in range(1, 21) if is_prime(x)])

# 5.3
def count_words(text: str) -> dict:
    """Возвращает словарь слово -> количество."""
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print("\n5.3:", count_words("hello world hello python"))

# 5.4
def apply_twice(func, x):
    return func(func(x))

print("\n5.4:", apply_twice(lambda x: x + 3, 10))
