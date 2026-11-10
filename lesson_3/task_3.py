class Dog:
    def sound(self):
        return "Гав"

class Cat:
    def sound(self):
        return "Мяу"

class Cow:
    def sound(self):
        return "Му"

class Robot:
    def sound(self):
        return "Beep"


def chorus(animals):
    for animal in animals:
        print(f"{animal.sound()}!")


if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow(), Dog(), Robot()]
    chorus(animals)
