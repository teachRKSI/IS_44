class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Здесь сработает сеттер из-за @property

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

# Проверка:
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

# t.celsius = -300    # Вызовет ValueError