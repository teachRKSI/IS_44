class Temperature:
    def __init__(self, celsius=0.0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


if __name__ == "__main__":
    t = Temperature(25)
    print(f"Температура в Цельсиях: {t.celsius}")
    print(f"Температура в Фаренгейтах: {t.fahrenheit}")

    t.celsius = 100
    print(f"После изменения: {t.celsius} = {t.fahrenheit}")

    try:
        t.celsius = -300
    except ValueError as error:
        print("Error:", error)
