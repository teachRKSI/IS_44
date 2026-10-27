#Задание 1
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def temp(self):
        return self._celsius

    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (273.15)")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * (9/5) + 32)

#Задание 2
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand}, {self.year} г."

class Car(Vehicle):
    def __init__(self, brand, year, fuel):
        super().__init__(brand, year)
        self.fuel = fuel

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, тип топлива: {self.fuel}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_volume):
        super().__init__(brand, year)
        self.engine_volume = engine_volume

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, объём двигателя: {self.engine_volume}"

my_car = Car("Kia", 2013, "Бензин")
print(my_car.info())
my_moto = Motorcycle("Suzuki", 2022, "2000")
print(my_moto.info())

#Задание 3
class Dog:
    def sound(self):
        return "Гав"

class Cat:
    def sound(self):
        return "Мяу"

class Cow:
    def sound(self):
        return "Му"

class Robot:
    def sound(self):
        return "Бип-бип"

def chorus(animals):
    chorus = ""
    for pet in animals:
        chorus += f'"<{pet.sound(pet)}>!" '
    print(chorus)

chorus([Robot, Cat, Cow, Dog, Robot])