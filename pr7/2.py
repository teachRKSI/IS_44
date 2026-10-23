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
        return parent_info, self.fuel

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_volume):
            super().__init__(brand, year)
            self.engine_volume = engine_volume

    def info(self):
        parent_info = self.info()
        return parent_info, self.engine_volume
