# 6.1
squares = [x ** 2 for x in range(1, 11)]
print("Квадраты:", squares)

# 6.2
nums = [1, -2, 3, -4, 5, -6]
positives = [x for x in nums if x > 0]
print("Положительные:", positives)

# 6.3
squares_dict = {x: x ** 2 for x in range(5)}
print("Словарь квадратов:", squares_dict)

# 6.4
text = "quick brown fox"
lengths = [len(word) for word in text.split()]
print("Длины слов:", lengths)