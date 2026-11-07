class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 1. Исправление: добавили вызов родительского __init__
        self.breed = breed

    def info(self):
        return f"{self.name}, порода: {self.breed}"

    # 3. Переопределяем speak с использованием super()
    def speak(self):
        return f"{super().speak()} (гав!)"


# 2. Проверка
d = Dog("Рекс", "Лабрадор")
print(d.info())   # Рекс, порода: Лабрадор
print(d.speak())  # Рекс издаёт звук (гав!)