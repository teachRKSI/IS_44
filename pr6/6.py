#6.1
squares = [x ** 2 for x in range(10)]
print(squares)

#6.2
nums = [1, -2, 3, -4, 5, -6]
nums_pos = [i for i in nums if i >= 0]
print(nums_pos)

#6.3
slovar = {x: x ** 2 for x in range(5)}
print(slovar)

#6.4
str = "quick brown fox"
lengths = [len(word) for word in str.split()]
print(lengths)
