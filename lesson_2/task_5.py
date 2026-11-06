# 5.1
def calculate_stats(numbers: list[float]) -> tuple:
    """Возвращает минимум, максимум и среднее значение."""
    if not numbers:
        return None, None, None

    average = sum(numbers) / len(numbers)
    return min(numbers), max(numbers), average


print("5.1:", calculate_stats([1, 2, 3, 4]))
print("Пустой список:", calculate_stats([]))


# 5.2
def is_prime(n: int) -> bool:
    """Проверяет, является ли целое число простым."""
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


print("5.2: Проверка чисел от 1 до 20")
for number in range(1, 21):
    print(number, is_prime(number))


# 5.3
def count_words(text: str) -> dict[str, int]:
    """Подсчитывает количество появлений каждого слова."""
    counts = {}

    for word in text.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


print("5.3:", count_words("кот пёс кот птица пёс кот"))


# 5.4
def apply_twice(func, x):
    """Применяет переданную функцию два раза подряд."""
    return func(func(x))


print("5.4:", apply_twice(lambda x: x + 3, 5))