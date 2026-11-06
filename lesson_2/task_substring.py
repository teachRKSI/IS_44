#Самая длинная подстрока

s = input("Введите строку: ")
last = {}
start = 0
best = 0

for i, char in enumerate(s):
    start = max(start, last.get(char, -1) + 1)
    last[char] = i
    best = max(best, i - start + 1)

print("Максимальная длина:", best)