#8.1 + 8.2 + 8.3

try:
    a = int(input("числитель: "))
    b = int(input("знаменатель: "))
    n = a/b
except ZeroDivisionError:
    print("ноль убери") # obrabotka isklucheniya - deleniye na 0
except ValueError: #obrabotka iskluchenya - neverny tip dannyh
    print("Введено не число")
else:
    print(n) # yesli uspeshno
finally:
    print("Готово") # v lubom sluchaye

