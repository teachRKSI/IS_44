#5.1
def calculate_stats(numbers):
    """Возвращает кортеж (min, max, average). Для пустого списка — (None, None, None)."""
    if not numbers:
        return (None, None, None)
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))
print(calculate_stats([1, 2, 3]))
print(calculate_stats([]))

#5.2
def is_prime(n: int) -> bool:
    """Возвращает True, если n — простое число, иначе False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for n in range(1, 21):
    print(n, is_prime(n))

#5.3
def count_words(text: str) -> dict:
    """Возвращает словарь: слово → количество вхождений."""
    result = {}
    for word in text.split():
        result[word] = result.get(word, 0) + 1
    return result
print(count_words("КУРСОВАЯ ПО 9S 9S 9S 9S 9S 9S 9S КУРСОВАЯ ПРОЕКТ ГЕШТАЛЬТ ПРОЕКТ ПО 9S КУРСОВАЯ"))

#5.4
def apply_twice(func, x):
    """Применяет func к x дважды: func(func(x))."""
    return func(func(x))

print(apply_twice(lambda x: x + 3, 10))