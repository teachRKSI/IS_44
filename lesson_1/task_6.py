# 6.1.
squares = [x ** 2 for x in range(1, 11)]
print("6.1:", squares)

# 6.2. 
print("\n6.2:")
nums = [1, -2, 3, -4, 5, -6]
positives = [x for x in nums if x > 0]
print(positives)

# 6.3. 
print("\n6.3:")
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)

# 6.4.
print("\n6.4:")
text = "quick brown fox"
lengths = [len(word) for word in text.split()]
print(lengths)