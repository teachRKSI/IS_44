class Temperature:
    def __init__(self, _celsius):
        self._celsius = _celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, _celsius):
        if _celsius < -273.15:
            raise ValueError('это абсолютный ноль((')
        self._celsius = _celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32
