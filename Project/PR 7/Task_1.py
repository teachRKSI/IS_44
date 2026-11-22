class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15 °C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(f"{t.celsius} °C = {t.fahrenheit} °F")

t.celsius = -10
print(f"{t.celsius} °C = {t.fahrenheit} °F")