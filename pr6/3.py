#3.1
print("3.1")
nums = [1, 2, 2, 3, 4, 4, 5, 1]
set_nums = set(nums)
print(set_nums)
set_nums = list(set_nums)
set_nums.sort(reverse=True)
print(set_nums)

#3.2
print("\n3.2")
counts = {}

for num in nums:
    counts[num] = counts.get(num, 0) + 1

print(counts)

#3.3
print("\n3.3")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set_a = set(a)
set_b = set(b)
print(list(set_a & set_b))
print(list(set_a - set_b))
print(list(set_a ^ set_b))

#3.4
print("\n3.4")
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for name, grade in grades.items():
    if grade >= 4:
        print(name)