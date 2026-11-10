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
        return f"{parent_info}, объем двигателя: {self.engine_volume} см³"


if __name__ == "__main__":
    car = Car("Toyota Camry", 2021, "бензин")
    moto = Motorcycle("Yamaha R1", 2023, 998)

    print(car.info())
    print(moto.info())
