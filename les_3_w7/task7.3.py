class Dog:
    def sound(self):
        return "Гав"

class Cat:
    def sound(self):
        return "Мяу"

class Cow:
    def sound(self):
        return "Му"
    
class Rabbit:
    def sound(self):
        return "Фффф"
    
def chorus(animals):
    """Принимает список любых объектов с методом sound()."""
    for animal in animals:
        print(f"{animal.sound()}!")

animals = [Dog(), Cat(), Cow(), Dog(), ()]
chorus(animals)
