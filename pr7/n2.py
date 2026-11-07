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
        return f"{parent_info}, топливо: {self.fuel}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_volume):
        super().__init__(brand, year)
        self.engine_volume = engine_volume

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, объем двигателя: {self.engine_volume} см³"

# Проверка:
car = Car("Toyota", 2020, "бензин")
moto = Motorcycle("Yamaha", 2022, 600)

print(car.info())   # Toyota, 2020 г., топливо: бензин
print(moto.info())  # Yamaha, 2022 г., объем двигателя: 600 см³