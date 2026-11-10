print("Задача 6.1")
squares = [x ** 2 for x in range(1, 11)]
print("Квадраты от 1 до 10:", squares)


print("\nЗадача 6.2")
nums = [1, -2, 3, -4, 5, -6]
positives = [x for x in nums if x > 0]
print("Только положительные:", positives)


print("\nЗадача 6.3")
squares_dict = {x: x ** 2 for x in range(5)}
print("Словарь квадратов:", squares_dict)


print("\nЗадача 6.4")
text = "quick brown fox"
lengths = [len(w) for w in text.split()]
print("Длины слов:", lengths)
