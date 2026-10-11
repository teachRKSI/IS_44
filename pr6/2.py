#2.1
print("Задание 2.1")

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        #continue
    elif i % 3 == 0:
        print("Fizz")
        #continue
    elif i % 5 == 0:
        print("Buzz")
        #continue
    else:
        print(i)

#2.2
print("\n Задание 2.2")

l = 1
while l <= 20:
    if l % 3 == 0 and l % 5 == 0:
        print("FizzBuzz")
    elif l % 3 == 0:
        print("Fizz")
    elif l % 5 == 0:
        print("Buzz")
    else:
        print(l)
    l+=1

#2.3
print("\n Задание 2.3")

n = int(input("Введите число N: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#2.4

for r in range(1, 101):
    if r % 7 == 0 and r % 5 != 0:
        print(r, end=" ")
