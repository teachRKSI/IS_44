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
        return f"{super().info()}, топливо: {self.fuel}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_volume):
        super().__init__(brand, year)
        self.engine_volume = engine_volume

    def info(self):
        return f"{super().info()}, объем двигателя: {self.engine_volume} см³"

car = Car("Toyota", 2020, "бензин")
moto = Motorcycle("Yamaha", 2019, 600)

print(car.info())
print(moto.info())

print(isinstance(car, Vehicle))     
print(isinstance(moto, Vehicle))
print(issubclass(Car, Vehicle))