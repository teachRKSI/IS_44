print("6.1")
nums = [4, 1, 7, 3]
print("сумма:", + sum(nums))
print("минимум:", + min(nums), "\nмаксимум:", + max(nums))
print(sorted(nums))

print("\n7.2")
nums = [1, 2, 3, 4]
for i, val in enumerate(nums):
    print(i, val)

print("\n7.3")
names = ["Анна", "Борис"]
ages = [20, 22]
for a, b in zip(names, ages):
    print(a, b)

print("\n7.4")
nums = [7, 1, 3, 9]
print("Числа больше 10: ", any(x > 10 for x in nums)) # True, если хотя бы один > 10
print("Числа больше 0: ", all(x > 0 for x in nums)) # True, если все > 0



