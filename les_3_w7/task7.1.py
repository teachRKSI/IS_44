class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        """Геттер: возвращает температуру."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер: проверяет значение перед присваиванием."""
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Вычисляемое свойство (только геттер)."""
        return self._celsius * 9 / 5 + 32
    
t = Temperature(25)
print("Цельсий:", t.celsius)
print("Фаренгейт:", t.fahrenheit)