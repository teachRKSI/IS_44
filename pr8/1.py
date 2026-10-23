class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def info(self):
        return f"{self.name}, порода: {self.breed}"

    def speak(self):
        return f'{super().speak()} (гав!)'

d = Dog("Рекс", "Лабрадор")
print(d.info())
print(d.speak())
