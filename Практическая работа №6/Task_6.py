# 6.1
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# 6.2
nums = [1, -2, 3, -4, 5, -6]
positives = [x for x in nums if x > 0]
print(positives)   # [1, 3, 5]

# 6.3
d = {x: x ** 2 for x in range(5)}
print(d)           # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 6.4
text = "quick brown fox"
lengths = [len(w) for w in text.split()]
print(lengths)     # [5, 5, 3]