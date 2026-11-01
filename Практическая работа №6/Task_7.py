nums = [4, 1, 7, 3]

# 7.1
print("sum:", sum(nums))
print("min:", min(nums))
print("max:", max(nums))
print("sorted:", sorted(nums))

# 7.2
for i, val in enumerate(nums):
    print(i, val)

# 7.3
names = ["Анна", "Борис"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(name, age)

# 7.4
nums2 = [5, 15, 20, -3]
print("есть > 10:", any(x > 10 for x in nums2))   # True
print("все > 0:", all(x > 0 for x in nums2))      # False (из-за -3)