from typing import List, Tuple, Optional, Dict, Callable

# Задания 5.1 и 5.5
def calculate_stats(numbers: List[float]) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


# Задание 5.2
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Задание 5.3
def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    word_freq: Dict[str, int] = {}
    for word in words:
        word_clean = word.strip(".,!?:;\"'").lower()
        if word_clean:
            word_freq[word_clean] = word_freq.get(word_clean, 0) + 1
    return word_freq


# Задание 5.4
def apply_twice(func: Callable[[float], float], x: float) -> float:
    return func(func(x))


if __name__ == "__main__":
    print("5.1 Stats:", calculate_stats([10, 20, 30]))
    print("5.1 Empty Stats:", calculate_stats([]))

    primes = [x for x in range(1, 21) if is_prime(x)]
    print("5.2 Простые числа от 1 до 20:", primes)

    text_sample = "hello world hello python"
    print("5.3 Подсчёт слов:", count_words(text_sample))

    result = apply_twice(lambda x: x + 3, 5)
    print("5.4 apply_twice(lambda x: x + 3, 5):", result)