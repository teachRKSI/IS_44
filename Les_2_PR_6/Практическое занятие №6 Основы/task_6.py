print("6.1")
spisok = [x ** 2 for x in range(1, 11)]
print(spisok)

print("\n6.2")
nums = [1, -2, 3, -4, 5, -6]
result = [x for x in nums if x > 0]
print(result)

print("\n6.3")
list = {x: x ** 2 for x in range(5)}
print(list)

print("\n6.4")
s = "quick brown fox"
lengths = {word: len(word) for word in s.split()}
print(lengths)