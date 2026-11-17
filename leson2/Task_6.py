# Тема 6. Генераторы списков

# 6.1
numbers = [number for number in range(1, 11)]
print("Числа от 1 до 10:", numbers)

# 6.2
nums = [1, -2, 3, -4, 5, -6]
positive_numbers = [number for number in nums if number > 0]
print("Положительные числа:", positive_numbers)

# 6.3
squares = {x: x ** 2 for x in range(5)}
print("Словарь квадратов:", squares)

# 6.4
text = "quick brown fox"
# Под длинными словами здесь понимаются слова длиннее 3 символов.
long_words = [word for word in text.split() if len(word) > 3]
print("Длинные слова:", long_words)
