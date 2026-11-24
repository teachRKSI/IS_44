class Temperature:
def __init__(self, celsius):
self.celsius = celsius

@property
def celsius(self):
return self._celsius

@celsius.setter
def celsius(self, value):
if value < -273.15:
raise ValueError("Температура ниже абсолютного нуля!")
self._celsius = value

@property
def fahrenheit(self):
return self._celsius * 9 / 5 + 32


temp = Temperature(25)

print("Цельсий:", temp.celsius)
print("Фаренгейт:", temp.fahrenheit)
