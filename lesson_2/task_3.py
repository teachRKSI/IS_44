# 3.1
nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique_nums = set(nums)
result = list(unique_nums)
result.sort(reverse=True)
print(result)


#3.2
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1

print(counts)


#3.3
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set_a = set(a)
set_b = set(b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a | set_b)


#3.4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for name, mark in grades.items():
    if mark >= 4:
        print(name)