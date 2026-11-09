class Temperature:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < Temperature.ABSOLUTE_ZERO:
            raise ValueError(
                f"Температура не может быть ниже нуля "
                f"({Temperature.ABSOLUTE_ZERO} °C)"
            )
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    def __repr__(self):
        return f"Temperature({self._celsius} °C)"

t = Temperature(25)
print(t.celsius)
print(t.fahrenheit)

t.celsius = 100
print(t.fahrenheit)

t.celsius = -273.15
print(t.celsius)

try:
    t.celsius = -300
except ValueError as e:
    print("Ошибка:", e)

try:
    t.fahrenheit = 100
except AttributeError as e:
    print("Ошибка:", e)