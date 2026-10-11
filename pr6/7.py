#7.1
nums = [4, 1, 7, 3]
print(sum(nums))
print(min(nums))
print(max(nums))
print(sorted(nums))

#7.2
for i, val in enumerate(nums):
    print(i, val)

#7.3
names = ["Анна", "Борис"]
ages = [20, 22]

for name, age in zip(names, ages):
    print(name, age)

#7.4
print(any(x > 10 for x in nums))
print(all(x > 0 for x in nums))


