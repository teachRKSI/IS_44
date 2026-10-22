#1.1
name = "Андрей"
age = 19
height = 1.79
print(f"Меня зовут {name}, мне {19} лет, мой рост {height} м")

#1.2
a = "5"
b = 5
print(a+b)

#1.3
a = int(input(" Введите число"))
b = int(input(" Введите число"))
print(a+b)

#2.1-#2.2
a = 1
while (a <= 20):
    if a % 3 == 0 and a % 5 == 0: print("FizzBuzz")
    elif a % 3 == 0: print("Fizz")
    elif a % 5 == 0: print("Buzz")
    else: print(a)
    a += 1

#2.3
n = int(input("Введите число"))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)

#3.1
nums = [1, 2, 2, 3, 4, 4, 5, 1]
new_nums = list(set(nums))
for i in range(len(new_nums), 0, -1):
    new_nums.append(i)
    new_nums.remove(i)
print(new_nums)

#3.2
nums = [1, 2, 2, 3, 4, 4, 5, 1]
dict_nums = {}
for i in nums:
    dict_nums[i] = dict_nums.get(i, 0) + 1
print(dict_nums)

#3.3
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(f"{set(a) & set (b)} - пересечение")
print(f"{a} - элементы только из a")
print(f"{set(a+b)} - все уникальные элементы из обоих")

#3.4
grades = {"Анна": 5, "Борис": 3, "Вика": 4}
for i in grades:
    if(grades.get(i)) >= 4: print(i)

#4.1
string = " Python - это здорово! "
print((string.lower()).strip())
print(f"{len(string)} - длина строки")

#4.2
string = "яблоко,банан,вишня"
string_elements = string.split(",")
for i in string_elements:
    print(i.upper())

#4.3
string = input("Введите слово ")
if string == string[::-1]: print(f"Слово: {string} является палиндромом")
else: print(f"Слово: {string} не является палиндромом")

#4.4
string = "hello world"
print(string.replace(" ", "_"))

#5.1
def calculate_stats(numbers=None):
    output = []
    if not numbers: output = [None, None, None]
    else: output.extend([max(numbers), min(numbers), round(sum(numbers)/len(numbers), 2)])
    return output

nums = [1, 2, 5, 6, 2, 4]
print(calculate_stats(nums))

#5.2
def is_prime(n):
    isPrime = False
    nums = [2, 3, 4, 5, 6, 7, 8, 9]
    if(n in (2, 3, 5, 7)):
        isPrime = True
        return isPrime
    if((n ** 0.5) % 1 == 0):
        isPrime = False
        return isPrime
    for i in nums:
        if (n % i != 0):
            isPrime = True
        else:
            isPrime = False
            break
    return isPrime

print(is_prime(int(input("Введите число"))))

#5.3
def count_words(text):
    words_counter = {}
    text = (text.lower()).split(" ")
    for i in text:
        words_counter[i] = words_counter.get(i, 0) + 1
    return words_counter

for key, value in count_words(input("Введите текст")).items():
    print(f"Слово: {key} | Количество: {value}")

#5.4 - #5.5
def apply_twice(func, x) -> int:
    "Дважды применяет арифметическое действие к данному числу"
    return func(func(x))

print(apply_twice(lambda x: x+3, 6))
help(apply_twice)

#6.1
squares = [(x+1)**2 for x in range(10)]
print(squares)

#6.2
nums = [1, -2, 3, -4, 5, -6]
plus = [x for x in nums if x>0]
print(plus)

#6.3
nums = {x: x ** 2 for x in range(5)}
print(nums.items())

#6.4
text = "quick brown fox"
words = [len(word) for word in text.split(" ")]
print(words)

#7.1
nums = [4, 7, 1, 3]
print(f"Сумма {sum(nums)} | Максимум {max(nums)} | Минимум {min(nums)} | Сортировка {sorted(nums)}")

#7.2
nums = [4, 7, 1, 3]
for index, num in enumerate(nums):
    print(index, num, sep=" | ")

#7.3
names = ["Анна", "Борис"]
ages = [20, 22]

for a, b in zip(names, ages):
    print(a, b, sep=" | ")

#7.4 
nums = [1, 4, 75, 13, 43, 2, -5, 63]
print(any(x > 10 for x in nums), all(x > 0 for x in nums), sep=" | ")

#8.1
try:
    x = int(input())
except ValueError:
    print("Введено не число")
else: 
    print(x)

#8.2-8.3
x = int(input("Введите делимое"))
y = int(input("Введите делитель"))
try:
    x / y
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
else: 
    print(round(x/y, 2))
finally:
    print("Выполнение кода завершено")

#9.1
with open("hello.txt", "a", encoding="utf8") as file:
    file.write("Привет, мир!")

#9.2
with open("hello.txt", "r", encoding="utf8") as file:
    print(file.read())

#9.3
lines = {}
with open("hello.txt", "r", encoding="utf8") as file:
    for index, line in enumerate(file):
        print(line.strip(), index, sep=" | ")

#10.1
import math

print(math.sqrt(144), math.pi, sep=" | ")

#10.2
from random import randint
print(randint(1, 100))

#10.3
def main():
    print("Привет!")

if __name__ == "__main__":
    main()

#Финальное
students = {
    "Анна":  [4, 5, 3, 4],
    "Борис": [3, 3, 2, 5],
    "Вика":  [5, 5, 5, 5],
    "Глеб":  [2, 3, 4, 3],}

averages = {key: sum(students.get(key))/len(students.get(key)) for key in students}

Max = 0
BestStudent = ""
for key in averages:
    if averages.get(key) > Max:
        Max = averages.get(key)
        BestStudent = key

with open("text.txt", "w", encoding="utf8") as f:
    for key in averages:
        f.write(f"{key}: {students.get(key)} \n")
    f.write(f"Лучший студент: {BestStudent}")

excelent = [x for x in averages if averages.get(x) >= 4.5]

dvoechniki = ""
for key in students:
    if 2 in students.get(key):
        dvoechniki += f"{key} "

def printer(a: dict, bs: str, ex: list, dv: str):
    """Вывод результатов в консоль"""
    print(f"Средние баллы: {a}\nЛучший студент: {bs}\nОтличники: {ex}\nДвойки есть у: {dv}")

printer(averages, BestStudent, excelent, dvoechniki)

#Самая длинная подстрока
s = "edfwefwefwefasxasfwqa"
maxResult = ""
if len(s) == 0:
    maxResult = s
elif len(s) == 1:
    maxResult = s[0]
else:
    result = s[0]
    for sign in s:
        if sign in result:
            result = sign
        else: 
            result += sign
            if len(result) > len(maxResult):
                maxResult = result

print(f"Самая длинная подстрока: {maxResult} | Длина: {len(maxResult)}")