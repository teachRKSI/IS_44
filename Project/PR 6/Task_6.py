
squares = [x ** 2 for x in range(1, 11)]
print("6.1 Квадраты чисел 1..10:", squares)


nums = [1, -2, 3, -4, 5, -6]
positives = [x for x in nums if x > 0]
print("6.2 Положительные числа:", positives)


squares_dict = {x: x ** 2 for x in range(5)}
print("6.3 Словарь квадратов:", squares_dict)


sentence = "quick brown fox"
word_lengths = [len(word) for word in sentence.split()]
print("6.4 Длины слов:", word_lengths)