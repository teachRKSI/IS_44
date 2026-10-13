class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand}, {self.year} г."

class Car(Vehicle):
    def __init__(self, brand, year, fuel):
        Vehicle.__init__(self, brand, year, fuel)
        self.brand = brand
        self.year = year
        self.fuel = fuel
