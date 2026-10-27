print("5.1")
def calculate_stats(numbers: list[float]) -> tuple:
    if not numbers:
        return (None, None, None)
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

print(calculate_stats([1, 2, 3, 4, 5]))
print(calculate_stats([]))

print("\n5.2")
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(1, 21):
    print(i, is_prime(i))

print("\n5.3")
def count_words(text: str) -> dict[str, int]:
    result = {}
    for word in text.split():
        result[word] = result.get(word, 0) + 1
    return result
print(count_words("Коля колол колья, Коля колол"))

print("\n5.4")
def apply_twice(func, x):
    return func(func(x))
print(apply_twice(lambda x: x + 6, 2))