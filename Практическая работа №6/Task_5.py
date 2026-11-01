# 5.1
def calculate_stats(numbers: list[float]) -> tuple:
    """Возвращает (min, max, average) или (None, None, None) для пустого списка."""
    if not numbers:
        return (None, None, None)
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

print(calculate_stats([1, 2, 3, 4]))   # (1, 4, 2.5)
print(calculate_stats([]))             # (None, None, None)

# 5.2
def is_prime(n: int) -> bool:
    """True, если n — простое число."""
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

print([n for n in range(1, 21) if is_prime(n)])
# [2, 3, 5, 7, 11, 13, 17, 19]

# 5.3
def count_words(text: str) -> dict[str, int]:
    """Словарь: слово → количество вхождений."""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(count_words("a b a c b a"))   # {'a': 3, 'b': 2, 'c': 1}

# 5.4
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x: x + 3, 5))   # 11

# 5.5 — аннотации и docstring уже добавлены выше (см. функции).