class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


temperature = Temperature(25)
print("Цельсий:", temperature.celsius)
print("Фаренгейт:", temperature.fahrenheit)

temperature.celsius = 0
print("После изменения:", temperature.fahrenheit, "°F")

try:
    temperature.celsius = -300
except ValueError as error:
    print("Ошибка:", error)

try:
    invalid_temperature = Temperature(-300)
except ValueError as error:
    print("Ошибка при создании:", error)