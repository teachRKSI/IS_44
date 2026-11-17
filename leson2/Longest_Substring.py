# Самая длинная подстрока без повторяющихся символов

def longest_unique_substring_length(s: str) -> int:
    """Возвращает длину самой длинной подстроки без повторов."""
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


# Проверка примеров из задания
examples = ["abcabcbb", "bbbbb", "pwwkew", ""]
for example in examples:
    print(f"{example!r} -> {longest_unique_substring_length(example)}")

# Ввод собственной строки
user_string = input("\nВведите строку: ")
print("Длина самой длинной подстроки:", longest_unique_substring_length(user_string))
