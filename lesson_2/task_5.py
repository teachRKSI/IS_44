print("Задача 5.1")
def calculate_stats(numbers):
    if not numbers:
        return (None, None, None)

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return (minimum, maximum, average)

print("Для списка [10, 20, 30]:", calculate_stats([10, 20, 30]))
print("Для пустого списка:", calculate_stats([]))


print("\nЗадача 5.2")
def is_prime(n: int) -> bool:
    """Проверяет, является ли число n простым (с аннотацией типов по заданию 5.5)."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 21) if is_prime(x)]
print("Простые числа от 1 до 20:", primes)


print("\nЗадача 5.3")
def count_words(text):
    words = text.split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

sample = "кот собака кот птица кот собака собака"
print("Словарь слов:", count_words(sample))


print("\nЗадача 5.4")
def apply_twice(func, x):
    return func(func(x))

res = apply_twice(lambda x: x + 3, 5)
print("Результат:", res)
